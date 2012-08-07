import bottle
from bottle import route, run, debug, Bottle, default_app
from bottle import static_file, response, template, request, redirect
from bottle import HTTPError
from bottle import jinja2_view as view
from util import deployed_on_sae

from inspect import isfunction

app = default_app()
bottle.debug(True)

from weibo import APIClient, APIError

redirect_url_weibo = "http://weiboapidebugger.sinaapp.com/weibo"
weibo_appid = '3179652632'
weibo_app_secret='3bc523e4528f6f4de2efb48d4eddec81'

@app.route('/')
@view('static/view/main.html')
def main_page():
	isLogged, username = session_login()
	if isLogged == True:
		return {'username' : username}
	return {}

@app.route('/api')
def get_api_json():
	response.content_type = 'application/json'
	session = request.environ['beaker.session']
	if deployed_on_sae:
		return receive_weibo_api()
	else:
		d = {};
		for i in range(1, 10):
			d[str(i)] = i
		return {'status': 'success', 'rst': {'uid':12345, 'other': d}}
	return {'status': 'error'}

def receive_weibo_api():
	if is_logged_session():
		client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, 
			redirect_uri=redirect_url_weibo)
		client.set_access_token(get_access_token(), get_expires_in())
		if request.GET.get('method'):
			api_func = construct_weibo_api()
			if not api_func:
				return {'status': 'api_not_found'}
			print api_func
			try:
				json_rst = eval(api_func)
			except APIError as e:
				return {'status': str(e)}
			except:
				return {'status': 'unkown exception'}
			return {'status': 'success', 'rst': json_rst}
		else:
			weibo_user = client.get.users__show(uid=get_uid())
			return {'status': 'success', 'rst': weibo_user}
	return {'status': 'not_login'}

def get_uid() :
	session = request.environ['beaker.session']
	return session['uid']

g_apis = {
	'statuses/user_timeline': {'uid': get_uid, 'count': 10},
	'users/counts': {'uids': get_uid},
	'users/domain_show': {'domain': "\"\""},
	'users/show': {'uid': get_uid}
}

def construct_weibo_api():
	method = request.GET.get('method')
	if method not in g_apis:
		return None
	params = ''
	for key in g_apis[method]:
		if isfunction(g_apis[method][key]):
			params += '%s=%s,' %(key, str(g_apis[method][key]()))
		else:
			params += '%s=%s,' %(key, str(g_apis[method][key]))
	api_func = ('client.get.%s' % (method.replace('/','__'))) + '(' + params + ')'
	return api_func

@app.route('/weibo')
def weibo():
	return handle_weibo_oauth()

def handle_weibo_oauth():
	code = bottle.request.GET.get('code')
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, 
		redirect_uri=redirect_url_weibo)
	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in
	client.set_access_token(access_token, expires_in)

	weibo_user = client.get.users__show(uid=r.uid)
	session_save(weibo_user.screen_name, r.uid, access_token, expires_in)
	return redirect('/')

@app.route('/login_to_weibo')
def login_to_weibo():
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, 
		redirect_uri=redirect_url_weibo)
	url = client.get_authorize_url()
	return redirect(url)

@app.route('/logout')
def logout():
	session_logout()
	return redirect('/')

def session_login() :
	session = request.environ['beaker.session']
	if 'username' in session:
		username = session['username']
		return True, username
	return False, None

def is_logged_session() :
	session = request.environ['beaker.session']
	if 'username' in session and 'access_token' in session:
		return True
	return False

def get_username() :
	session = request.environ['beaker.session']
	return session['username']



def get_access_token() :
	session = request.environ['beaker.session']
	return session['access_token']

def get_expires_in() :
	session = request.environ['beaker.session']
	return session['expires_in']

def session_logout() :
	session_delete()

def session_save(username, uid, access_token, expires_in):
	session = request.environ['beaker.session']
	session['username'] = username
	session['uid'] = uid
	session['access_token'] = access_token
	session['expires_in'] = expires_in
	session.save()

def session_delete():
	session = request.environ['beaker.session']
	session.delete()

from beaker.middleware import SessionMiddleware
session_opts = {
  'session.type': 'cookie',
  'session.expires': 3600,
  'session.validate_key': '1234',
}
app = SessionMiddleware( app, session_opts )



import bottle
from bottle import route, run, debug, Bottle, default_app
from bottle import static_file, response, template, request, redirect
from bottle import HTTPError
from bottle import jinja2_view as view
from util import deployed_on_sae

app = default_app()
bottle.debug(True)

from weibo import APIClient

redirect_url_weibo = "http://gzb1985.sinaapp.com/login/weibo"
weibo_appid = '2023070208'
weibo_app_secret='abb0afabbd3b82348971b1c6ad891c2c'

@app.route('/')
@view('static/view/main.html')
def main_page():
	isLogged, username = session_login(request)
	if isLogged == True:
		return {'username' : username}
	return {}

@app.route('/api')
def get_api_json():
	response.content_type = 'application/json'
	session = request.environ['beaker.session']
	if deployed_on_sae:
		if 'uid' in session and 'access_token' in session:
			uid = session['uid']
			access_token = session['access_token']
			expires_in = session['expires_in']
			client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, redirect_uri=redirect_url_weibo)
			client.set_access_token(access_token, expires_in)
			weibo_user = client.get.users__show(uid=uid)
			return {'status': 'success', 'rst': weibo_user}
	else:
		return {'status': 'success', 'rst': {'uid':12345}}
	return {'status': 'error'}

@app.route('/logout')
def logout():
	session_logout(request)
	return redirect('/')

def handle_weibo_oauth():
	code = bottle.request.GET.get('code')
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, redirect_uri=redirect_url_weibo)
	r = client.request_access_token(code)

	access_token = r.access_token
	expires_in = r.expires_in
	client.set_access_token(access_token, expires_in)

	weibo_user = client.get.users__show(uid=r.uid)
	session = request.environ['beaker.session']
	session['username'] = weibo_user.screen_name
	session['uid'] = r.uid
	session['access_token'] = access_token
	session['expires_in'] = expires_in
	session.save()
	return {'username' : weibo_user.screen_name, 'profile_image_url' : weibo_user.profile_image_url}

@app.route('/weibo')
@view('static/view/main.html')
def weibo():
	return handle_weibo_oauth()

@app.route('/login_to_weibo')
def login_to_weibo():
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, redirect_uri=redirect_url_weibo)
	url = client.get_authorize_url()
	return redirect(url)

def session_login(request) :
	session = request.environ['beaker.session']
	if 'username' in session:
		username = session['username']
		if isUserExsit(username) :
			return True, username
	return False, None

def session_logout(request) :
	session = request.environ['beaker.session']
	session.delete()

from beaker.middleware import SessionMiddleware
session_opts = {
  'session.type': 'cookie',
  'session.expires': 300,
  'session.validate_key': '1234',
}
app = SessionMiddleware( app, session_opts )

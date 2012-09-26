from bottle import request, redirect
from weibo import APIClient, APIError
from weibo_api_const import *
from session_util import session_save
from private_const import *



def redirect_to_weibo_oauth_url():
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, 
		redirect_uri=redirect_url_weibo)
	url = client.get_authorize_url()
	return redirect(url)

def handle_weibo_oauth_callback():
	code = request.GET.get('code')
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, 
		redirect_uri=redirect_url_weibo)
	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in
	client.set_access_token(access_token, expires_in)
	user = client.get.users__show(uid=r.uid)
	session_save(user.screen_name, r.uid, user.profile_image_url, access_token, expires_in)
	return redirect('/')
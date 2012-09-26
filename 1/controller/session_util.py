from bottle import request

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

def get_uid() :
	session = request.environ['beaker.session']
	return session['uid']

def get_avatar() :
	session = request.environ['beaker.session']
	return session['avatar']

def get_access_token() :
	session = request.environ['beaker.session']
	return session['access_token']

def get_expires_in() :
	session = request.environ['beaker.session']
	return session['expires_in']

def session_logout() :
	session_delete()

def session_save(username, uid, profile_image_url, access_token, expires_in):
	session = request.environ['beaker.session']
	session['username'] = username
	session['uid'] = uid
	session['avatar'] = profile_image_url
	session['access_token'] = access_token
	session['expires_in'] = expires_in
	session.save()

def session_delete():
	session = request.environ['beaker.session']
	session.delete()
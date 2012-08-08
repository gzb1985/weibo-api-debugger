import sys
from bottle import request
from inspect import isfunction

from session_util import *
from weibo_api_const import *
from weibo import APIClient, APIError

def receive_weibo_api(method):
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, 
		redirect_uri=redirect_url_weibo)
	client.set_access_token(get_access_token(), get_expires_in())
	api_func = construct_weibo_api_url(method)
	if not api_func:
		return {'status': 'api_not_found'}
	print api_func
	try:
		json_rst = eval(api_func)
	except APIError as e:
		return {'status': str(e)}
	except:
		return {'status': str(sys.exc_info())}
	return {'status': 'success', 'rst': json_rst}

def construct_weibo_api_url(method):
	if method not in g_api:
		return None
	pos = g_api.index(method)
	params_dict = g_param[pos]
	params = ''
	for key in params_dict:
		if params_dict[key]:
			if isfunction(params_dict[key]):
				params += '%s=%s,' %(key, str(params_dict[key]()))
			else:
				params += '%s=%s,' %(key, str(params_dict[key]))
	api_func = ('client.get.%s' % (method.replace('/','__'))) + '(' + params + ')'
	return api_func

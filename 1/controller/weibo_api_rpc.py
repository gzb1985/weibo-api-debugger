import sys
from bottle import request
from inspect import isfunction
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

from session_util import *
from weibo_api_const import *
from weibo import APIClient, APIError, _obj_hook
from util import *

def receive_weibo_api(method):
	client = APIClient(app_key=weibo_appid, app_secret=weibo_app_secret, 
		redirect_uri=redirect_url_weibo)
	client.set_access_token(get_access_token(), get_expires_in())
	api_func = construct_weibo_api_url(method)
	if not api_func:
		return {'status': 'api_not_found'}
	print api_func
	json_rst = None
	try:
		json_rst = eval(api_func)
	except APIError as apierr:
		return {'status': 'success', 'rst': str(apierr)}
	except urllib2.HTTPError as err:
		r = json.loads(err.read(), object_hook=_obj_hook)
		return {'status': 'error', 'status_code': str(err), 'rst': r}
	except:
		return {'status': str(sys.exc_info())}
	return {'status': 'success', 'rst': json_rst}

def construct_weibo_api_url(method):
	params = ''
	for key in request.GET:
		if key != 'method':
			value = request.GET.get(key)
			if value != '':
				if isWeiboApiStringParameter(value):
					params += '%s=\'%s\',' %(key, value)
				else:
					params += '%s=%s,' %(key, value)
	api_func = ('client.get.%s' % (method.replace('/','__'))) + '(' + params + ')'
	return api_func


redirect_url_weibo = "http://weiboapidebugger.sinaapp.com/weibo"
weibo_appid = '3179652632'
weibo_app_secret='3bc523e4528f6f4de2efb48d4eddec81'

g_api = [
	'statuses/public_timeline',
	'statuses/friends_timeline',
	'statuses/user_timeline',
	'users/counts',
	'users/domain_show',
	'users/show'
]

from session_util import get_uid

g_param = [
	{'count': 10, 'page': None, 'base_app': None}, # statuses/public_timeline
	{'count': 10}, # statuses/friends_timeline
	{'uid': get_uid, 'count': 10}, # statuses/user_timeline
	{'uids': get_uid}, # users/counts
	{'domain': 'ifanr'}, # users/domain_show
	{'uid': get_uid} # users/show
]
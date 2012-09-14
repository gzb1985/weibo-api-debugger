
redirect_url_weibo = "http://weiboapidebugger.sinaapp.com/weibo"
weibo_appid = '3179652632'
weibo_app_secret='3bc523e4528f6f4de2efb48d4eddec81'

g_api = [
	'account/get_uid',
	'account/rate_limit_status',
	'account/get_privacy',
	'statuses/public_timeline',
	'statuses/friends_timeline',
	'statuses/user_timeline',
	'users/counts',
	#'users/domain_show',
	'users/show',
	'place/friends_timeline',
	'place/user_timeline',
	'place/users/photos',
	'location/pois/search/by_location',
	'place/nearby/pois',
    'place/pois/photos'
]

from session_util import get_uid

g_param = [
	{}, # account/get_uid
	{}, # account/rate_limit_status
	{}, # account/get_privacy
	{'count': 10, 'page': None, 'base_app': None}, # statuses/public_timeline
	{'count': 10}, # statuses/friends_timeline
	{'uid': get_uid, 'count': 10}, # statuses/user_timeline
	{'uids': get_uid}, # users/counts
	#{'domain': 'ifanr'}, # users/domain_show
	{'uid': get_uid}, # users/show
	{'count': 10}, # place/friends_timeline
	{'uid': get_uid, 'count': 10}, # place/user_timeline
	{'uid': get_uid}, #place/users/photos
	{'category': '110201'}, #location/pois/search/by_location
	{'lat': 31.196784, 'long': 121.586530}, #place/nearby/pois
    {'poiid': 'B2094655D26DA5F54593'} #place/pois/photos
]

g_apis = {
	'api': [
	    {'name': 'account/get_uid', 'param': []},
	    {'name': 'account/rate_limit_status', 'param': []},
	    {'name': 'account/get_privacy', 'param': []},
	    {'name': 'statuses/public_timeline', 'param': ['count', 'page', 'base_app']},
	    {'name': 'statuses/friends_timeline', 'param': ['count']},
	    {'name': 'statuses/user_timeline', 'param': ['uid', 'count']},
	    {'name': 'users/counts', 'param': ['uids']},
	    {'name': 'users/show', 'param': ['uid']},
	    {'name': 'place/friends_timeline', 'param': ['count']},
	    {'name': 'place/user_timeline', 'param': ['uid', 'count']},
	    {'name': 'place/users/photos', 'param': ['uid']},
	    {'name': 'location/pois/search/by_location', 'param': ['category']},
	    {'name': 'place/nearby/pois', 'param': ['lat', 'long']},
	    {'name': 'place/pois/photos', 'param': ['poiid']},
	    {'name': 'statuses/hot/repost_daily', 'param': []}
	]
}
# -*- coding: utf-8 -*-  

redirect_url_weibo = "http://weiboapidebugger.sinaapp.com/weibo"
weibo_appid = '3179652632'
weibo_app_secret='3bc523e4528f6f4de2efb48d4eddec81'

g_apis = {
	'api': [
	    {'name': '微博读取接口', 'id': 1, 'apilist': [{'name': 'statuses/public_timeline', 'param': ['count']}, 
	    									 {'name': 'statuses/friends_timeline', 'param': ['count']}, 
	    									 {'name': 'statuses/user_timeline', 'param': ['uid', 'count']},
	    									 {'name': 'statuses/hot/repost_daily', 'param': []}
	    									]
	    },

	    {'name': '用户读取接口', 'id': 3, 'apilist': [{'name': 'users/counts', 'param': ['uids']}, 
	    									 {'name': 'users/show', 'param': ['uid']}
	    									]
	    },

	    {'name': '账号读取接口', 'id': 5, 'apilist': [{'name': 'account/get_uid', 'param': []}, 
	    									 {'name': 'account/rate_limit_status', 'param': []}, 
	    									 {'name': 'account/get_privacy', 'param': []}
	    									]
	    },

	    {'name': '位置服务动态读取接口', 'id': 7, 'apilist': [{'name': 'place/friends_timeline', 'param': ['count']}, 
	    									 {'name': 'place/user_timeline', 'param': ['uid', 'count']}, 
	    									]
	    },

	    {'name': '位置服务用户读取接口', 'id': 9, 'apilist': [{'name': 'place/users/photos', 'param': ['uid']}
	    									]
	    },

	    {'name': '位置服务地点读取接口', 'id': 11, 'apilist': [{'name': 'place/pois/photos', 'param': ['poiid']}
	    									]
	    },

	    {'name': '位置服务附近读取接口', 'id': 13, 'apilist': [{'name': 'place/nearby/pois', 'param': ['lat', 'long']}
	    									]
	    },

	    {'name': '地理信息POI数据读取接口', 'id': 15, 'apilist': [{'name': 'location/pois/search/by_location', 'param': ['category']}
	    									]
	    }
	]
}
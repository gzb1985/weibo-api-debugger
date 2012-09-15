# -*- coding: utf-8 -*-  

redirect_url_weibo = "http://weiboapidebugger.sinaapp.com/weibo"
weibo_appid = '3179652632'
weibo_app_secret='3bc523e4528f6f4de2efb48d4eddec81'

g_apis = {
	'api': [
	    {'name': '微博读取接口', 'id': 1, 'apilist': [
	    										{'name': 'statuses/public_timeline', 'param': ['count']}, 
												{'name': 'statuses/friends_timeline', 'param': ['count']}, 
												{'name': 'statuses/home_timeline', 'param': ['count']}, 
												{'name': 'statuses/friends_timeline/ids', 'param': ['count']}, 
												{'name': 'statuses/user_timeline', 'param': ['uid', 'count']},
												{'name': 'statuses/user_timeline/ids', 'param': ['uid', 'count']},
												{'name': 'statuses/repost_timeline', 'param': ['id', 'count']},
												{'name': 'statuses/repost_timeline/ids', 'param': ['id', 'count']},
												{'name': 'statuses/repost_by_me', 'param': ['count']},
												{'name': 'statuses/mentions', 'param': ['count']},
												{'name': 'statuses/mentions/ids', 'param': ['count']},
												{'name': 'statuses/bilateral_timeline', 'param': ['count']},
												{'name': 'statuses/show', 'param': ['id']},
												{'name': 'statuses/querymid', 'param': ['id', 'type']},
												{'name': 'statuses/queryid', 'param': ['mid', 'type']},
												{'name': 'statuses/hot/repost_daily', 'param': ['count']},
												{'name': 'statuses/hot/repost_weekly', 'param': ['count']},
												{'name': 'statuses/hot/comments_daily', 'param': ['count']},
												{'name': 'statuses/hot/comments_weekly', 'param': ['count']},
												{'name': 'statuses/count', 'param': ['ids']}
	    									]
	    },

	    {'name': '评论读取接口', 'id': 3, 'apilist': [
	    										{'name': 'comments/show', 'param': ['id']}, 
												{'name': 'comments/by_me', 'param': ['count']}, 
												{'name': 'comments/to_me', 'param': ['count']}, 
												{'name': 'comments/timeline', 'param': ['count']}, 
												{'name': 'comments/mentions', 'param': ['count']},
												{'name': 'comments/show_batch', 'param': ['cids']}
	    									]
	    },

	    {'name': '用户读取接口', 'id': 5, 'apilist': [
	    										{'name': 'users/counts', 'param': ['uids']}, 
	    										{'name': 'users/domain_show', 'param': ['domain']},
	    										{'name': 'users/show', 'param': ['uid']}
	    									]
	    },

	    {'name': '关系读取接口', 'id': 7, 'apilist': [
	    										{'name': 'friendships/friends', 'param': ['uid']}, 
	    										{'name': 'friendships/friends/in_common', 'param': ['uid', 'suid']},
	    										{'name': 'friendships/friends/bilateral', 'param': ['uid', 'count']},
	    										{'name': 'friendships/friends/bilateral/ids', 'param': ['uid', 'count']}, 
	    										{'name': 'friendships/friends/ids', 'param': ['uid']},
	    										{'name': 'friendships/followers', 'param': ['uid']},
	    										{'name': 'friendships/followers/ids', 'param': ['uid']}, 
	    										{'name': 'friendships/followers/active', 'param': ['uid']},
	    										{'name': 'friendships/friends_chain/followers', 'param': ['uid', 'count']},
	    										{'name': 'friendships/show', 'param': ['source_id', 'target_id']}
	    									]
	    },

	    {'name': '账号读取接口', 'id': 9, 'apilist': [
	    										{'name': 'account/get_privacy', 'param': []},
	    										{'name': 'account/profile/school_list', 'param': []}, 
	    										{'name': 'account/rate_limit_status', 'param': []}, 
	    										{'name': 'account/get_uid', 'param': []}
	    									]
	    },

	    {'name': '收藏读取接口', 'id': 11, 'apilist': [
	    										{'name': 'favorites', 'param': ['count']},
	    										{'name': 'favorites/ids', 'param': ['count']}, 
	    										{'name': 'favorites/show', 'param': ['id']}, 
	    										{'name': 'favorites/by_tags', 'param': ['tid', 'count']},
	    										{'name': 'favorites/tags', 'param': ['count']},
	    										{'name': 'favorites/by_tags/ids', 'param': ['tid', 'count']}
	    									]
	    },

	    {'name': '话题读取接口', 'id': 13, 'apilist': [
	    										{'name': 'trends', 'param': ['uid', 'count']},
	    										{'name': 'trends/is_follow', 'param': ['trend_name']},
	    										{'name': 'trends/hourly', 'param': []},
	    										{'name': 'trends/daily', 'param': []},
	    										{'name': 'trends/weekly', 'param': []}
	    									]
	    },

	    {'name': '标签读取接口', 'id': 15, 'apilist': [
	    										{'name': 'tags', 'param': ['uid', 'count']},
	    										{'name': 'tags/tags_batch', 'param': ['uids']},
	    										{'name': 'tags/suggestions', 'param': ['count']}
	    									]
	    },

	    {'name': '注册读取接口', 'id': 17, 'apilist': [
	    										{'name': 'register/verify_nickname', 'param': ['nickname']}
	    									]
	    },

	    {'name': '搜索联想接口', 'id': 19, 'apilist': [
	    										{'name': 'search/suggestions/users', 'param': ['q', 'count']},
	    										{'name': 'search/suggestions/statuses', 'param': ['q', 'count']},
	    										{'name': 'search/suggestions/schools', 'param': ['q', 'count', 'type']},
	    										{'name': 'search/suggestions/companies', 'param': ['q', 'count']},
	    										{'name': 'search/suggestions/apps', 'param': ['q', 'count']},
	    										{'name': 'search/suggestions/at_users', 'param': ['q', 'count', 'type', 'range']}
	    									]
	    },

	    {'name': '推荐读取接口', 'id': 21, 'apilist': [
	    										{'name': 'suggestions/users/hot', 'param': ['category']},
	    										{'name': 'suggestions/users/may_interested', 'param': ['count']},
	    										{'name': 'suggestions/users/by_status', 'param': ['content', 'num']},
	    										{'name': 'suggestions/statuses/hot', 'param': ['type', 'is_pic', 'count']},
	    										{'name': 'suggestions/statuses/reorder', 'param': ['section', 'count']},
	    										{'name': 'suggestions/statuses/reorder/ids', 'param': ['section', 'count']},
	    										{'name': 'suggestions/favorites/hot', 'param': ['count']}
	    									]
	    },

	    {'name': '提醒读取接口', 'id': 23, 'apilist': [
	    										{'name': 'remind/unread_count', 'param': ['uid']}
	    									]
	    },

	    {'name': '短链数据接口', 'id': 25, 'apilist': [
	    										{'name': 'short_url/shorten', 'param': ['url_long']},
	    										{'name': 'short_url/expand', 'param': ['url_short']},
	    										{'name': 'short_url/clicks', 'param': ['url_short']},
	    										{'name': 'short_url/referers', 'param': ['url_short']},
	    										{'name': 'short_url/locations', 'param': ['url_short']},
	    										{'name': 'short_url/share/counts', 'param': ['url_short']},
	    										{'name': 'short_url/share/statuses', 'param': ['url_short', 'count']},
	    										{'name': 'short_url/comment/counts', 'param': ['url_short']},
	    										{'name': 'short_url/comment/comments', 'param': ['url_short', 'count']},
	    										{'name': 'short_url/info', 'param': ['url_short']}
	    									]
	    },

	    {'name': '公共服务读取接口', 'id': 27, 'apilist': [
	    										{'name': 'common/code_to_location', 'param': ['codes']},
	    										{'name': 'common/get_city', 'param': ['province', 'capital', 'language']},
	    										{'name': 'common/get_province', 'param': ['country', 'capital', 'language']},
	    										{'name': 'common/get_country', 'param': ['capital', 'language']},
	    										{'name': 'common/get_timezone', 'param': ['language']}
	    									]
	    },

	    {'name': '位置服务动态读取接口', 'id': 29, 'apilist': [
	    										{'name': 'place/public_timeline', 'param': ['count']},
	    										{'name': 'place/friends_timeline', 'param': ['count']}, 
	    										{'name': 'place/user_timeline', 'param': ['uid', 'count']}, 
	    										{'name': 'place/poi_timeline', 'param': ['poiid']},
	    										{'name': 'place/nearby_timeline', 'param': ['lat', 'long']},
	    										{'name': 'place/statuses/show', 'param': ['id']},
	    										{'name': 'place/users/show', 'param': ['uid']},
	    										{'name': 'place/users/checkins', 'param': ['uid', 'count']},
	    										{'name': 'place/users/photos', 'param': ['uid']},
	    										{'name': 'place/users/tips', 'param': ['uid', 'count']},
	    										{'name': 'place/users/todos', 'param': ['uid', 'count']},
	    										{'name': 'place/pois/show', 'param': ['poiid']},
	    										{'name': 'place/pois/users', 'param': ['poiid']},
	    										{'name': 'place/pois/tips', 'param': ['poiid', 'count']},
	    										{'name': 'place/pois/photos', 'param': ['poiid']},
	    										{'name': 'place/pois/search', 'param': ['keyword']},
	    										{'name': 'place/pois/category', 'param': ['pid']},
	    										{'name': 'place/nearby/pois', 'param': ['lat', 'long']},
	    										{'name': 'place/nearby/users', 'param': ['lat', 'long']},
	    										{'name': 'place/nearby/photos', 'param': ['lat', 'long']},
	    										{'name': 'place/nearby_users/list', 'param': ['lat', 'long']},
	    									]
	    },

	    {'name': '地理信息读取接口', 'id': 31, 'apilist': [
	    										{'name': 'location/base/get_map_image', 'param': ['center_coordinate']},
	    										{'name': 'location/geo/ip_to_geo', 'param': ['ip']},
	    										{'name': 'location/geo/address_to_geo', 'param': ['address']},
	    										{'name': 'location/geo/geo_to_address', 'param': ['coordinate']},
	    										{'name': 'location/geo/gps_to_offset', 'param': ['coordinate']},
	    										{'name': 'location/geo/is_domestic', 'param': ['coordinate']},
	    										{'name': 'location/pois/show_batch', 'param': ['srcids']},
	    										{'name': 'location/pois/search/by_location', 'param': ['category']},
	    										{'name': 'location/pois/search/by_geo', 'param': ['q', 'coordinate']},
	    										{'name': 'location/pois/search/by_area', 'param': ['q', 'coordinates']},
	    										{'name': 'location/mobile/get_location', 'param': ['json']},
	    										{'name': 'location/line/drive_route', 'param': ['begin_coordinate', 'end_coordinate']},
	    										{'name': 'location/line/bus_route', 'param': ['begin_coordinate', 'end_coordinate']},
	    										{'name': 'location/line/bus_line', 'param': ['begin_coordinate', 'end_coordinate']},
	    										{'name': 'location/line/bus_station', 'param': ['begin_coordinate', 'end_coordinate']}
	    									]
	    }
	]
}
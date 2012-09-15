import os

import re

deployed_on_sae = False

if 'SERVER_SOFTWARE' in os.environ:
	deployed_on_sae = True


def isWeiboApiStringParameter(param):
	alphaList = [a for a in param if a.isalpha() or a==',' or a=='.']
	if alphaList:
		return True

	if re.findall('[\x80-\xff].', param):
		return True

	return False
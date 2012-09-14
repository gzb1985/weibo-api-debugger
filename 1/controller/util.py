import os

deployed_on_sae = False

if 'SERVER_SOFTWARE' in os.environ:
	deployed_on_sae = True


def isWeiboApiStringParameter(param):
	alphaList = [a for a in param if a.isalpha()]
	if alphaList:
		return True
	return False
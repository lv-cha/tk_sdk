'''
Created by auto_sdk on 2020.02.25
'''
from top.api.base import RestApi
class TbkItemInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ip = None
		self.num_iids = None
		self.platform = None

	def getapiname(self):
		return 'taobao.tbk.item.info.get'

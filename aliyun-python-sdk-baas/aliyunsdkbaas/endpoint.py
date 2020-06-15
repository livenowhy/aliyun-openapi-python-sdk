# # Licensed to the Apache Software Foundation (ASF) under one
# # or more contributor license agreements.  See the NOTICE file
# # distributed with this work for additional information
# # regarding copyright ownership.  The ASF licenses this file
# # to you under the Apache License, Version 2.0 (the
# # "License"); you may not use this file except in compliance
# # with the License.  You may obtain a copy of the License at
# #
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# #
# # Unless required by applicable law or agreed to in writing,
# # software distributed under the License is distributed on an
# # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# # KIND, either express or implied.  See the License for the
# # specific language governing permissions and limitations
# # under the License.


class EndpointData():
	def __init__(self):
		self.endpoint_map = {
			"cn-shenzhen": "baas.aliyuncs.com",
			"cn-beijing": "baas.aliyuncs.com",
			"ap-south-1": "baas.ap-southeast-1.aliyuncs.com",
			"eu-west-1": "baas.ap-southeast-1.aliyuncs.com",
			"ap-northeast-1": "baas.ap-southeast-1.aliyuncs.com",
			"cn-qingdao": "baas.aliyuncs.com",
			"cn-shanghai": "baas.aliyuncs.com",
			"cn-hongkong": "baas.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "baas.ap-southeast-1.aliyuncs.com",
			"eu-central-1": "baas.ap-southeast-1.aliyuncs.com",
			"cn-huhehaote": "baas.aliyuncs.com",
			"us-east-1": "baas.ap-southeast-1.aliyuncs.com",
			"cn-zhangjiakou": "baas.aliyuncs.com",
			"us-west-1": "baas.ap-southeast-1.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()

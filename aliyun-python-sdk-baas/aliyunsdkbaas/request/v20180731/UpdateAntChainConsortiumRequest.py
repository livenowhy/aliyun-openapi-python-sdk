# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkbaas.endpoint import endpoint_data

class UpdateAntChainConsortiumRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'UpdateAntChainConsortium')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConsortiumName(self):
		return self.get_body_params().get('ConsortiumName')

	def set_ConsortiumName(self,ConsortiumName):
		self.add_body_params('ConsortiumName', ConsortiumName)

	def get_ConsortiumDescription(self):
		return self.get_body_params().get('ConsortiumDescription')

	def set_ConsortiumDescription(self,ConsortiumDescription):
		self.add_body_params('ConsortiumDescription', ConsortiumDescription)

	def get_ConsortiumId(self):
		return self.get_body_params().get('ConsortiumId')

	def set_ConsortiumId(self,ConsortiumId):
		self.add_body_params('ConsortiumId', ConsortiumId)
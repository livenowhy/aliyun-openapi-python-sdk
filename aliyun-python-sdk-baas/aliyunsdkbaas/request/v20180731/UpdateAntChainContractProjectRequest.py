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

class UpdateAntChainContractProjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'UpdateAntChainContractProject')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProjectVersion(self):
		return self.get_body_params().get('ProjectVersion')

	def set_ProjectVersion(self,ProjectVersion):
		self.add_body_params('ProjectVersion', ProjectVersion)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_ProjectName(self):
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_body_params('ProjectName', ProjectName)

	def get_ProjectDescription(self):
		return self.get_body_params().get('ProjectDescription')

	def set_ProjectDescription(self,ProjectDescription):
		self.add_body_params('ProjectDescription', ProjectDescription)
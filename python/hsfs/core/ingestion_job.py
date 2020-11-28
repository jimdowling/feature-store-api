#
#   Copyright 2020 Logical Clocks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import humps


class IngestionJob:
    def __init__(
        self,
        data_path,
        job_path,
        job_conf_path,
        href=None,
        expand=None,
        items=None,
        count=None,
        type=None,
    ):
        self._data_path = data_path
        self._job_path = job_path
        self._job_conf_path = job_conf_path

    @classmethod
    def from_response_json(cls, json_dict):
        json_decamelized = humps.decamelize(json_dict)
        return cls(**json_decamelized)

    @property
    def data_path(self):
        return self._data_path

    @property
    def job_path(self):
        return self._job_path

    @property
    def job_conf_path(self):
        return self._job_conf_path

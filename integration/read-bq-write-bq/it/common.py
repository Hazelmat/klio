# Copyright 2020 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Variables and functions shared between the stages of integration testing."""
import os
import yaml

from klio_core import config

def get_config():
    """Load KlioConfig object."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "klio-job.yaml")
    try:
        with open(config_path) as f:
            cfg_dict = yaml.safe_load(f)

        return config.KlioConfig.from_raw_config(cfg_dict)

    except IOError as e:
        logging.error(e)
        raise SystemExit(1)

entity_ids = ['1', '2', '3', '4', '5']


#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import warnings

from ._version import (  # noqa: F401
    __author__,
    __author_email__,
    __description__,
    __maintainer__,
    __maintainer_email__,
    __title__,
    __url__,
    __version__,
)
from .common import ElandDeprecationWarning, SortOrder
from .dataframe import DataFrame
from .etl import csv_to_eland, eland_to_pandas, pandas_to_eland
from .index import Index
from .ndframe import NDFrame
from .series import Series

# Display Eland deprecation warnings by default
warnings.simplefilter("default", category=ElandDeprecationWarning)

__all__ = [
    "DataFrame",
    "Series",
    "NDFrame",
    "Index",
    "pandas_to_eland",
    "eland_to_pandas",
    "csv_to_eland",
    "SortOrder",
]

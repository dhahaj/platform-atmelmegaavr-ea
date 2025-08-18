# Copyright 2014-present PlatformIO <contact@platformio.org>
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

from platformio.public import PlatformBase
from platformio.util import get_systype


class AtmelmegaavreaPlatform(PlatformBase):

    def configure_default_packages(self, variables, targets):
        if not variables.get("board"):
            return super().configure_default_packages(variables, targets)

        sys_type = get_systype()
        toolchain_package_systype = "windows_amd64"
        if "linux" in sys_type:
            toolchain_package_systype = "linux_x86_64"
        elif "darwin" in sys_type:
            toolchain_package_systype = "darwin_x86_64"

        toolchain_version = self.packages["toolchain-atmelavr-dxcore"][
            "version"
        ]
        self.packages["toolchain-atmelavr-dxcore"]["optional"] = False
        self.packages["toolchain-atmelavr-dxcore"][
            "version"
        ] = f"https://github.com/valeros/platform-atmelmegaavr-ea/releases/download/v1.9.0/toolchain-atmelavr-dxcore-{toolchain_package_systype}-{toolchain_version}.tar.gz"

        return super().configure_default_packages(variables, targets)

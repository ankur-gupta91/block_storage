# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import tabs

from openstack_dashboard.dashboards.admin.block_storage \
    import tables

class BackendUsageTab(tabs.TableTab):
    name = _("Backend Usage")
    slug = "backend_usage_tab"
    table_classes = (tables.BackendUsageTable,)
    template_name = ("horizon/common/_detail_table.html")
    preload = False

    def get_backend_usage_data(self):
        try:
            volume = []
            return volume
        except Exception:
            return []

class VolumeQuotaTab(tabs.TableTab):
    name = _("Volume Quota")
    slug = "volume_quotas_tab"
    table_classes = (tables.VolumeQuotasTable,)
    template_name = ("horizon/common/_detail_table.html")
    preload = False

    def get_volume_quota_data(self):
        try:
            volume = []
            return volume
        except Exception:
            return []


class BlockStorageTabs(tabs.TabGroup):
    slug = "block_storage_tabs"
    tabs = (VolumeQuotaTab, BackendUsageTab)
    sticky = True

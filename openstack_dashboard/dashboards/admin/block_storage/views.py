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

from horizon import exceptions
from horizon import tabs

from openstack_dashboard import api

from openstack_dashboard.dashboards.admin.block_storage \
    import tabs as block_storage_tabs

class IndexView(tabs.TabbedTableView):
    # A very simple class-based view...
    tab_group_class = block_storage_tabs.BlockStorageTabs
    template_name = 'admin/block_storage/index.html'

    def get_data(self, request, context, *args, **kwargs):
        import pdb; pdb.set_trace()
        try:
            quota_types = api.cinder.tenant_quota_get(self)
        except Exception:
            quota_types = []
            msg = _("Unable to retrieve quotas")
            exceptions.handle(self.request, msg)
        return quota_types
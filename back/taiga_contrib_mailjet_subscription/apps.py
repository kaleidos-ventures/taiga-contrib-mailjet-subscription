# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.apps import AppConfig
from django.conf import settings
from django.core.checks import Warning, register
import logging

logger = logging.getLogger(__name__)

warnings = []

# Checks
@register
def check_mailjet_config(**kwargs):
    if not getattr(settings, "MAILJET_API_KEY"):
        warnings.append(
            Warning(
                "MAILJET_API_KEY must be set on settings",
                id="mailjet_subscription.A001",
            )
        )
    if not getattr(settings, "MAILJET_SECRET_KEY"):
        warnings.append(
            Warning(
                "MAILJET_SECRET_KEY must be set on settings",
                id="mailjet_subscription.A002",
            )
        )
    if not getattr(settings, "MAILJET_CONTACTLIST_ID"):
        warnings.append(
            Warning(
                "MAILJET_CONTACTLIST_ID must be set on settings",
                id="mailjet_subscription.A003",
            )
        )
    return warnings

# Signals

def connect_signals():
    from taiga.auth.signals import user_registered as user_registered_signal
    from taiga.users.signals import user_change_email as user_change_email_signal
    from taiga.users.signals import user_cancel_account as user_cancel_account_signal
    from . import signal_handlers as handlers
    user_registered_signal.connect(handlers.subscribe_user_to_mailjet,
                                   dispatch_uid="subscribe_user_to_mailjet")
    user_change_email_signal.connect(handlers.change_user_email_in_mailjet,
                                     dispatch_uid="change_user_email_in_mailjet")
    user_cancel_account_signal.connect(handlers.unsubscribe_user_from_mailjet,
                                       dispatch_uid="unsubscribe_user_from_mailjet")


def disconnect_signals():
    from taiga.auth.signals import user_registered as user_registered_signal
    from taiga.users.signals import user_change_email as user_change_email_signal
    from taiga.users.signals import user_cancel_account as user_cancel_account_signal
    user_registered_signal.disconnect(dispatch_uid="subscribe_user_to_mailjet")
    user_change_email_signal.disconnect(dispatch_uid="change_user_email_in_mailjet")
    user_cancel_account_signal.disconnect(dispatch_uid="unsubscribe_user_from_mailjet")


class MailjetSubscriptionAppConfig(AppConfig):
    name = "taiga_contrib_mailjet_subscription"
    verbose_name = "Mailjet Subscription App Config"

    def ready(self):
        if not len(warnings):
            connect_signals()

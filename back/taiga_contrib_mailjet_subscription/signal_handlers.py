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

from . import services


def subscribe_user_to_mailjet(sender, **kwargs):
    user = kwargs["user"]

    services.add_user(user.username, user.full_name, user.email, is_taiga_user=True)


def change_user_email_in_mailjet(sender, **kwargs):
    user = kwargs["user"]
    old_email = kwargs["old_email"]
    new_email = kwargs["new_email"]

    services.delete_user(old_email, is_taiga_user=False)
    services.add_user(user.username, user.full_name, new_email, is_taiga_user=True)


def unsubscribe_user_from_mailjet(sender, **kwargs):
    user = kwargs["user"]
    request_data = kwargs.get("request_data", None)
    if not request_data:
        return

    unsuscribe_from_newsletter = request_data.get("unsuscribe", None)
    if unsuscribe_from_newsletter:
        services.delete_user(user.email, is_taiga_user=False)
    else:
        services.add_user(user.username, user.full_name, user.email, is_taiga_user=False)

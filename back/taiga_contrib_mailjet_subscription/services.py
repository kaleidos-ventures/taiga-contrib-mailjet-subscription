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

from django.conf import settings

import mailjet_rest as mailjet

from .import utils


def _get_api_client():
    api_key = settings.MAILJET_API_KEY
    secret_key = settings.MAILJET_SECRET_KEY
    return mailjet.Client(auth=(api_key, secret_key))


@utils.catch_connection_errors
@utils.log_api_response
def add_user(username, full_name, email, is_taiga_user=True):
    contactlist_id = settings.MAILJET_CONTACTLIST_ID
    data = {
        "Action": "addforce",
        "Email": email,
        "Properties": {
            "username": username,
            "full_name": full_name,
            "is_taiga_user": is_taiga_user,
        }
    }

    client = _get_api_client()
    return client.contactslist_managecontact.create(id=contactlist_id, data=data)


@utils.catch_connection_errors
@utils.log_api_response
def delete_user(email, is_taiga_user=False):
    contactlist_id = settings.MAILJET_CONTACTLIST_ID
    data = {
        "Action": "remove",
        "Email": email,
        "Properties": {
            "is_taiga_user": is_taiga_user,
        }
    }

    client = _get_api_client()
    return client.contactslist_managecontact.create(id=contactlist_id, data=data)

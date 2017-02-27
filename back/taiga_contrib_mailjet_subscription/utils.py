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

from functools import wraps
import logging

logger = logging.getLogger(__name__)


def log_api_response(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        res = function(*args, **kwargs)

        if res.ok:
            logger.info("[Mailjet] {call}{args} - {message}:\n\t{data}".format(
                call=function.__name__,
                args=str(args),
                message=" ".join((str(res.status_code), res.reason)),
                data=res.content or "-no data-"
            ))
        else:
            logger.error("[Mailjet] error on {call}{args} - {message}:\n\t{data}\n\tREQUEST:{request_call}\n\t{request_data}".format(
                call=function.__name__,
                args=str(args),
                message=" ".join((str(res.status_code), res.reason)),
                data=res.content or "-no data-",
                request_call="{} {}".format(res.request.method, res.request.url),
                request_data=str(res.request.body)
            ))

        return res

    return decorator


def catch_connection_errors(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            logger.error("[Mailjet] error on {call}{args}:\n\t{err}".format(
                call=function.__name__,
                args=str(args),
                err=e
            ))

    return decorator

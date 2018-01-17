"""
    A python Library to help make python apps/bots using the 42 API
    Copyright (C) 2017-2018  Jules LASNE jlasne@student.42.fr

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from decouple import config

"""
    Those lines here will get the values from the .env/.ini file
    APP_UID: The app uid given by 42
    APP_SECRET: the app secret given by 42
    TOKEN_FILE: The filename you want your token to be stored in
"""
APP_UID = config('APP_UID', cast=str, default = None)
APP_SECRET = config('APP_SECRET', cast=str, default=None)
TOKEN_FILE = config('TOKEN_FILE', cast=str, default=None)

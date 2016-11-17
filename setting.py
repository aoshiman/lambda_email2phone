## -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from ast import literal_eval
import lamvery

try:
    _conf = literal_eval(lamvery.secret.get('conf'))
    SID = _conf['SID']
    SECRET = _conf['SECRET']
    TARGET = _conf['TARGET']
    FROM = _conf['FROM']
    URL = _conf['URL']

except Exception as e:
    print(e)

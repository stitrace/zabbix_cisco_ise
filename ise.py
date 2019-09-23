#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import requests
import json
import xmltodict
import datetime

from requests.packages.urllib3.exceptions import InsecureRequestWarning  # @UnresolvedImport
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # @UndefinedVariable

if not len(sys.argv) == 5:
    print('ZBX_NOTSUPPORTED')
    exit(1)

host = sys.argv[1]
user = sys.argv[2]
passw = sys.argv[3]
comm = sys.argv[4]

ise = requests.session()
ise.auth = (user, passw)
ise.verify = False
ise.headers.update({'Connection': 'keep_alive'})

if comm == 'count':
    try:
        resp = ise.get('https://{0}/admin/API/mnt/Session/ActiveCount'.format(host))
    except:
        print(0)
        exit(1)
    resp = json.loads(json.dumps(xmltodict.parse(resp.text)))
    print(int(resp['sessionCount']['count']))
elif comm == 'active':
    today = datetime.datetime.today() - datetime.timedelta(hours=0, minutes=30)
    today = today.strftime("%Y-%m-%d %H:%M:%S")
    try:
        resp = ise.get('https://{0}/admin/API/mnt/Session/AuthList/{1}/null'.format(host, today))
    except:
        print(0)
        exit(1)
    resp = json.loads(json.dumps(xmltodict.parse(resp.text)))
    print(int(resp['activeList']['@noOfActiveSession']))

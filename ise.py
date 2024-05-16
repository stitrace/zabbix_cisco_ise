#!/usr/bin/env python

import sys
import requests
import json
import xmltodict
import datetime

from requests.packages.urllib3.exceptions import InsecureRequestWarning  # @UnresolvedImport
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # @UndefinedVariable

def get_item(url):
    try:
        user = sys.argv[2]
        passw = sys.argv[3]
        ise_request = requests.session()
        ise_request.auth = (user, passw)
        ise_request.verify = False
        ise_request.headers.update({'Connection': 'keep_alive'})
        ise_response = ise_request.get(url)
        response = json.loads(json.dumps(xmltodict.parse(ise_response.text)))
    except Exception as exc:
        print(exc)
        exit(1)
    return response

def get_count(node_url):
    try:
        gc_resp = get_item(node_url + 'Session/ActiveCount')
        return (int(gc_resp['sessionCount']['count']))
    except Exception as exc:
        print(exc)
        exit(1)

def get_active(node_url):
    try:
        today = datetime.datetime.today() - datetime.timedelta(hours=0, minutes=30)
        today = today.strftime("%Y-%m-%d %H:%M:%S")
        gc_resp = get_item(node_url + 'Session/AuthList/{0}/null'.format(today))
        return (int(gc_resp['activeList']['@noOfActiveSession']))
    except Exception as exc:
        print(exc)
        exit(1)

if not len(sys.argv) >= 5:
    print('ZBX_NOTSUPPORTED')
    exit(1)
host = sys.argv[1]
comm = sys.argv[4]
ise_url = 'https://{0}/admin/API/mnt/'.format(host)
if comm == 'count':
    print(get_count(ise_url))
elif comm == 'active':
    print(get_active(ise_url))
elif comm == 'test':
    print(host)
    print(ise_url)
    print("count")
    print(get_count(ise_url))
    print("active")
    print(get_active(ise_url))

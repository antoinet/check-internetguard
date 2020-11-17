#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import json
import urllib.request
import urllib.parse

# curl 'https://www.swisscom.ch/etc/swisscom/servlets/public/urlchecker.urlchecker.json' \
#  -F 'url=igtest.bluewin.org' -F 'language=en' \
#  -F 'path=/en/residential/help/internet/internetguard/url-checker.html'
#
# {"success":true,"data":{"blocked":true,"captcha":true,"additionalInfo":"<p>Blocked due to phishing.<br>\n</p>\n"}}
# {"success":true,"data":{"blocked":false,"captcha":true,"additionalInfo":"<p>Blocked<br>\n</p>\n"}}

RED="\033[0;31m"
GREEN="\033[0;32m"
NC="\033[0m"
baseurl = 'https://www.swisscom.ch/etc/swisscom/servlets/public/urlchecker.urlchecker.json'
strip_re = re.compile('<[^>]*>')

def sanitize(value):
    return strip_re.sub('', value).strip()

def check_internetguard(domain):
    data = urllib.parse.urlencode({'url': domain, 'language': 'en',
        'path': '/en/residential/help/internet/internetguard/url-checker.html'})
    data = data.encode('ascii')
    with urllib.request.urlopen(baseurl, data) as f:
        res = json.load(f)
        if res['success']:
            if res['data']['blocked']:
                print("{}block{}\t{}\t{}".format(RED, NC, domain, sanitize(res['data']['additionalInfo'])))
            else:
                print("{}pass{}\t{}".format(GREEN, NC, domain))
        else:
            print("error\t{}\t{}".format(domain, sanitize(res['data']['description'])))


if __name__ == '__main__':
    for domain in sys.argv[1::]:
        check_internetguard(domain)


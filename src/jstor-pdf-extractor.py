import sys
import requests
import logging
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', help='full url of the paper\'s first page')
parser.add_argument('cookies', help='cookie string')
#parser.add_argument('-o', help='output file')
args = parser.parse_args()

headers = { 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' }

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

def get_cookies_dict(cookies_string):
    cookies_list = cookies_string.replace('cookie: ', '').split('; ')
    cookie_dict = {}
    for cookie in cookies_list:
        key, value = cookie.split('=')
        cookie_dict[key] = value
    return cookie_dict

def extract_image(index):
    url_with_index = args.url.replace('seq=1', 'seq={}'.format(index))
    res = requests.get(url_with_index, cookies=get_cookies_dict(args.cookies))
    dom = BeautifulSoup(res.content, 'lxml')
    dom.find(id='page-scan-container')
    from IPython.core.debugger import set_trace;set_trace()

extract_image(1)

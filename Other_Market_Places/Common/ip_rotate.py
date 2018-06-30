import time
from stem import Signal
from stem.control import Controller
import requests

def set_new_ip():
    """Change IP using TOR"""
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='eunimart_data_8hr')
        controller.signal(Signal.NEWNYM)

def show_ip():
    local_proxy = '127.0.0.1:8118'
    http_proxy = {
        'http': local_proxy,
        'https': local_proxy
    }
    current_ip = requests.get(
        url='http://icanhazip.com/',
        proxies=http_proxy,
        verify=False
    )
    print current_ip.content

while True:
    set_new_ip()
    time.sleep(10)
    show_ip()

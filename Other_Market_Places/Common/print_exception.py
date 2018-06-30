from datetime import date
from datetime import datetime


class print_exception:
    def __init__(self, msg_type, marketplace, hierarchy, url, msg):
        today = str(date.today())
        time = str(datetime.time(datetime.now()))
        complete_msg = today + " | " + time + " | " + msg_type + " | " + str(marketplace) + " | " + str(
            hierarchy) + " | " + str(url) + " | " + str(msg)
        print complete_msg

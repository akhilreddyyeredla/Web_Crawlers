HEADERS_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36' ]

PROXY_LIST = []

PROXY = {"https": ""}

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9", "Connection": "keep-alive",
    "Content-Type" : "application/json;charset=UTF-8",
    "User-Agent": ''
}


# GOOD status resposne 200
GOOD_STATUS = 200

# BAD status response 503 it means amazon has blocked us
BAD_STATUS = 503

# Page not found response 404
PAGE_NOT_FOUND = 404


MAX_RETRIES = 1

# to compare with config.write_to value
WRITE_TO_DB = 1

# to compare with config.write_to value
WRITE_TO_FILE = 2

# to compare with config.write_to value
WRITE_TO_CASSANDRA = 3

# to compare with config.write_to_value

WRITE_TO_BIGQUERY = 5

WRITE_TO_KAFKA = 6

WRITE_TO_REDIS = 7



MAIN_PAGE_URL = 'https://www.amazon.com/gp/site-directory/ref=nav_shopall_fullstore'

MAX_RETRIES = 5

CATEGORIES_TO_BE_SKIPPED = ' '

DOMAIN_NAME = 'https://www.amazon.com'

PROJECT_DOMAIN = 'www.amazon.com'

MARKET_PLACE_NAME = 'AMAZON_US'

CURRENCY = 'USD'

# GOOD status resposne 200
GOOD_STATUS = 200

# BAD status response 503 it means amazon has blocked us
BAD_STATUS = 503

# Page not found response 404
PAGE_NOT_FOUND = 404

DEBUG_ON = "ON"
# to compare with config.write_to value
WRITE_TO_DB = 1

# to compare with config.write_to value
WRITE_TO_FILE = 2

# to compare with config.write_to value
WRITE_TO_CASSANDRA = 3

# to compare with config.url_flag value
URL_FLAG = 1

#to compare with config.info_flag value
PRODUCT_FlAG = 1

# category_names
AMAZON_GLOBAL = "amazon_global"
BOOKS = "books"
HOME_GARDEN_AND_TOOLS = "home_garden_and_tools"
BEAUTY_AND_HEALTH = "beauty_and_health"
TOYS_AND_GAMES = "toys_and_games"
SPORTS_AND_OUTDOOR = "sports_and_outdoor"
CLOTHING = "clothing"
ELECTRONICS = 'Electronics__Computers_and_Office'
HANDMADE = "handmade"

# QUEUE_FILE_NAME = PROJECT_NAME + '/queued_files.txt'

# COMPLETED_FILE_NAME = PROJECT_NAME + '/completed_files.txt'

# This is the file name which will searched recursivly in a category folder while product url collection
PODUCTS_PAGE = 'products_page_links.txt'
COMPLETED_PAGE = 'products_page_completed.txt'

# To store product urls links
PRODUCTS_INFO_FILE = 'products_info_links.txt'
COMPLETED_INFO_FILE = 'products_info_completed.txt'

# To store hierarchy queue files
QUEUE_FILE = 'queue_file.txt'
COMPLETED_QUEUE_FILE = 'completed_file.txt'


# Request
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch, br",
#     "Accept-Language": "en-US,en;q=0.8",
#     "User-Agent": "Chrome/51.0.2704.103 Safari/537.36",
# }

HEADERS_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36' ]

PROXY_LIST = ['176.9.34.116:1080', '188.166.61.125:8080', '13.126.198.137:80', '128.199.160.48:3128', '79.137.42.124:3128', '80.73.9.75:3128', '128.199.95.132:3128', '82.165.135.253:3128', '159.203.16.98:8080', '94.249.236.195:3128', '139.59.111.57:8080', '95.110.215.103:80', '41.184.208.123:8080', '35.158.235.18:3128', '51.15.137.26:3128', '217.61.121.110:3128', '186.0.210.228:8080', '124.124.99.210:3128', '85.10.241.247:1080', '62.210.105.103:3128', '10.206.196.35.bc.googleusercontent.com:80', '182.253.190.122:8080', '212.98.58.154:8080', '176.221.42.213:3130', '165.227.186.69:3128', '163.172.220.221:8888', '86.105.51.105:3128', 'ns3014181.ip-149-202-192.eu:80', 'ns333111.ip-37-187-125.eu:3128', '13.127.8.153:80', 'pxy04twctx.dldc.tx.charter.com:3128', 'j308149.servers.jiffybox.net:3130', '54.37.18.54:3128', '139.59.86.118:80', '38.ip-158-69-48.net:3128', '137.74.171.76:3128', '24.174.198.85:3128', '190.142.152.48:80', '144.76.176.72:80', 'staticline-31-182-52-156.toya.net.pl:3129', 'pxy03twcca.ladc.ca.charter.com:3128', '35.195.65.241:3128', '185.13.22.23:8080', '94.130.187.214:3128', '106.ip-145-239-92.eu:3128', '192.99.245.228:3128', '103.10.169.79:80', '50.113.182.83:3128', 'ec2-34-207-150-171.compute-1.amazonaws.com:3128', '190.2.132.11:1080', 'pxy04twcca.ladc.ca.charter.com:3128', 'ip213.ip-188-165-4.eu:8080', '229.ip-217-182-76.eu:8888', 'ec2-35-162-160-108.us-west-2.compute.amazonaws.com:8080', '166.26.196.35.bc.googleusercontent.com:3128', '54.159.195.142:808', 'pxy02twcca.ladc.ca.charter.com:3128', 'pxy01twcca.ladc.ca.charter.com:3128', '138.197.142.206:3128', '71.13.112.152:3128', '165.227.37.214:3128', '189.173.12.5:8080', '189.161.119.50:80', '179.185.16.21:3130', '103.43.149.152:80', '191.102.72.10:8080', '96.30.72.50:80', '54.193.18.175:80', '147.135.210.114:54566', '165.255.75.6:80', '192.99.56.254:8080', '212.22.86.114:3130', '162.219.120.107:80', '103.85.162.94:8080', '114.ip-147-135-210.eu:54566', '124.81.208.244:80', 'clevery.xyz:3128', '98.8.198.85:3128', '98.8.198.82:3128', '192.241.190.167:8080', '162.243.33.71:8080', '47.91.240.173:80', '103.75.54.66:80', '128.199.190.130:8080', '178.254.36.21:1080', '169.239.126.150:3128', '13.126.64.69:80', '198.27.65.39:3128', '186.103.226.220:3129', '110.77.159.142:8080', '186.219.31.11:8080', '159.89.14.211:3128', '18.ip-151-80-159.eu:8080', '104.131.94.221:8080', 'ns3008014.ip-151-80-44.eu:3129', 'system88.magnetic.cc:3128', '45.5.45.214:8080', '193.194.69.36:3128', '37.187.119.226:3128', '45.55.86.49:8080', '52.213.95.230:80', '45.32.114.139:3128', '247.red-83-56-8.staticip.rima-tde.net:3128', 'u16842616.onlinehome-server.com:3128', '80.211.9.88:3128', '45.76.156.198:3128', 'h246.128.141.40.ip.windstream.net:3128', 'h226.242.132.40.static.ip.windstream.net:3128', 'rrcs-67-78-143-182.se.biz.rr.com:8080']

PROXY = {"https": ""}

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9", "Connection": "keep-alive",
    "Content-Type" : "application/json;charset=UTF-8",
    "Cookie": "skin=noskin; session-id=143-2818618-8121852; session-id-time=2082787201l; ubid-main=132-6469559-3316216; x-wl-uid=1NFxQZXwrJq9XohmtI8guiACk8rieEYCCCJpuaq6zff6cCO6IOQPL+ORofXI+bV1vy5aVVZEpQRs=; session-token=wBO32EXZou3JZgTUVRqvh/ENZrLUImOJXtKTrqDBEf0pF6/cKAyWxTwBU1u5RBJIQJYraCxAAKxeqzst7gNkPbQqGnQlgL42WJUzrFW7zrcH/JSXLRVfvjXCKVophpHeSXm1yeum6khe9G7EiHJeMUxRCTmD1PcNphR017WvHT9T81AiKAQ+DBKiAtbAjcilmBEBQFJp9VEQ8lt8ZznFkAR3G7IuK2p83zkKEO4rT5PQyiMr9pA1TFrk3tJCV0LT; csm-hit=s-WX643X7E7M5TZ9XWW4S0|1517478574572",
    "DNT": "1", "Host": "www.amazon.com"
    ,
    "User-Agent": ""
}

# Tags Class Names
H4_TAG_CLASS = 'a-size-small a-color-base a-text-bold'

LAST_PAGE_CLASS = "pagnDisabled"

NORMAL_ANCHOR_TAG_CLASS = 'a-link-normal s-ref-text-link'

CATEGORY_LIST_ANCHOR_TAG_CLASS = 'list-item__category-link'

SUB_CATEGORY_LIST_ANCHOR_TAG_CLASS = 'sub-categories__list__item__link'

INDENT_ONE_CLASS = 'a-unordered-list a-nostyle a-vertical s-ref-indent-one'

INDENT_NONE_CLASS = "a-unordered-list a-nostyle a-vertical s-ref-indent-none"

INDENT_TWO_CLASS = 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'

LEFT_NAV_CLASS = 'left_nav browseBox'

CAROUSAL_CLASS = 'a-carousel'

SMALL_BOX_GRID_CLASS = "bxc-grid__column bxc-grid__column--3-of-12 bxc-grid__column--light"

LARGE_BOX_GRID_CLASS = "bxc-grid__column bxc-grid__column--6-of-12 bxc-grid__column--light"

BOX_GRID_CONTAINER_CLASS = 'bxc-grid__container bxc-grid__container--width-1500'

ACS_WIDGET_LEFT_NAV_CLASS = 'acswidget acswidget-left-nav celwidget acsUxWidget acs-ln-widget'

ACS_SECTION_CLASS = 'acs-ln-nav-section'

ACS_HEADER_CLASS = 'acs-ln-header acs-ln-no-image '

SEE_MORE_CLASS = "seeMore"

LAYOUT_PICKER = 'Image View'

# Ignore_list:
IGNORE_LIST = 'Pet_Profile|Pet_Care_Tips|Top_Deals|See_all_|Shop_by_Room|Office_Supplies|Handmade|Amazon_s_Choice|Amazon_Devices|Smart_Home|Featured_Stores|All_|Sports_Deals|Gift_Cards|Fan_Shop|Sports_Collectibles||outdoor_deals'

# This list is used to select certain categories from electronics or extract seemore button
SELECTED_LIST = 'TV__Audio_and_Home_Theater|Camera__Photo_and_Video|Car_Electronics_and_GPS|Portable_Audio_and_Accessories|Musical_Instruments|Business_and_Office_Electronics|Sports_and_Fitness|Outdoor_Recreation'


# PROXIES = {'https': 'http://123.236.215.131:6588'}


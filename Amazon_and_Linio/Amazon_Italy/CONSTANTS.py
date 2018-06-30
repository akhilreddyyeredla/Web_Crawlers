

MAIN_PAGE_URL = ''

MAX_RETRIES = 5

CATEGORIES_TO_BE_SKIPPED = ' '

DOMAIN_NAME = 'https://www.amazon.it'

PROJECT_DOMAIN = 'www.amazon.it'

MARKET_PLACE_NAME = 'AMAZON_IT'

CURRENCY = 'EUR'
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
MUSICA_FILM_E_TV = 'Musica_Film_e_TV'
VIDEOGIOCHI_E_CONSOLE = 'Videogiochi_e_Console'
ALIMENTARI_E_CURA_DELLA_CASA = 'Alimentari_e_Cura_della_casa'
ELETTRONICA_E_INFORMATICA = 'Elettronica_e_Informatica'
COMMERCIO_INDUSTRIA_E_SCIENZA = 'Commercio_Industria_e_Scienza'
SPORT_E_TEMPO_LIBERO = 'Sport_e_tempo_libero'
LIBRI_E_AUDIBLE = 'Libri_e_Audible'
CASA_GIARDINO_FAI_DA_TE_E_ANIMALI = 'Casa_Giardino_Fai_da_te_e_Animali'
GIOCHI_E_PRIMA_INFANZIA = 'Giochi_e_Prima_infanzia'
BELLEZZA_E_SALUTE = 'Bellezza_e_Salute'
ABBIGLIAMENTO_SCARPE_E_GIOIELLI = 'Abbigliamento_Scarpe_e_Gioielli'
AUTO_E_MOTO = 'Auto_e_Moto'
HANDMADE = 'Handmade'


# QUEUE_FILE_NAME = PROJECT_NAME + '/queued_files.txt'

# COMPLETED_FILE_NAME = PROJECT_NAME + '/completed_files.txt'

# This is the file name which will searched recursivly in a category folder while product url collection
PODUCTS_PAGE = 'products_page_links.txt'
COMPLETED_PAGE = 'products_page_completed.txt'

# To store product urls links
PRODUCTS_INFO_FILE = 'products_info_links.txt'
COMPLETED_INFO_FILE = 'products_info_completed.txt'

# To store hierarchy queue files
QUEUE_FILE = '_file_queue.txt'
COMPLETED_QUEUE_FILE = '_file_completed.txt'



# Request
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch, br",
#     "Accept-Language": "en-US,en;q=0.8",
#     "User-Agent": "Chrome/51.0.2704.103 Safari/537.36",
# }

HEADERS_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36' ]

PROXY_LIST = []

PROXY = {"https": ""}

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9", "Connection": "keep-alive",
    "Content-Type" : "application/json;charset=UTF-8",
    "User-Agent": ''
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
IGNORE_LIST = 'Pet_Profile|Pet_Care_Tips|Top_Deals|See_all_|Shop_by_Room|Office_Supplies|Handmade|Amazon_s_Choice|Amazon_Devices|Smart_Home|Featured_Stores|All_|Sports_Deals|Gift_Cards|Fan_Shop|Sports_Collectibles|outdoor_deals|New_Arrivals'

# This list is used to select certain categories from electronics or extract seemore button
SELECTED_LIST = 'TV__Audio_and_Home_Theater|Camera__Photo_and_Video|Car_Electronics_and_GPS|Portable_Audio_and_Accessories|Musical_Instruments|Business_and_Office_Electronics|Sports_and_Fitness|Outdoor_Recreation'


# PROXIES = {'https': 'http://123.236.215.131:6588'}


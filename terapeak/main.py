# Simple fetcher to show how to use cookies with crawler on terapeak

import amazonTera
import requests
import json
#curl 'https://sell.terapeak.com/services/research/listings?buyerCountryCodes=US&categoryId=&endDate=1530687599999&fromPrice=&isAnyCriteria=false&keywords=jewelry&listingConditions=&listingTypes=&productId=&sellerCountryCodes=&sellerName=&site=ALL&startDate=1528095600000&toPrice=&transactionSite=&isTypeAheadSearch=false&source=&pageSize=10&pageNumber=1&sortBy=&sortDirection=' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0' -H 'Accept: application/json' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://sell.terapeak.com/product-research?buyerCountryCodes=US&categoryId&endDate=1530687599999&fromPrice&isAnyCriteria=false&keywords=jewelry&listingConditions=&listingTypes=&productId=&sellerCountryCodes&sellerName=&site=ALL&startDate=1528095600000&toPrice&transactionSite' -H 'content-type: application/json' -H 'pragma: no-cache' -H 'cache-control: no-cache, max-age=0' -H 'authorization: Bearer t2airih7qpho97s16ip61jnodenjcrg7ib64kcot75o08v6tuah' -H 'origin: https://sell.terapeak.com' -H 'Cookie: tp_ee_last_visit=1530863166; tp_ee_last_activity=1531108826; totango.heartbeat.last_module=product-research; totango.heartbeat.last_ts=1531112427052; TPSERVERID=blue_e; tp_ee_tracker=%7B%220%22%3A%22index%22%2C%22token%22%3A%222ad40c2b997ade901d715b9f00a41b39%22%7D; i18next=en-US; localeHeader=en-US,en; optimizelyEndUserId=oeu1530866742887r0.815676442607611; optimizelySegments=%7B%22229813889%22%3A%22ff%22%2C%22229833781%22%3A%22direct%22%2C%22229852304%22%3A%22false%22%7D; optimizelyBuckets=%7B%7D; currency=USD; tpebayCurrencyId=1; tp_ee_csrf_token=f9f71c42b9f66e91ba8ecc10773612f0769e8a5f' -H 'DNT: 1' -H 'Connection: keep-alive'


f = open('hometerapeak.txt','a+')

# url = 'https://sell.terapeak.com/product-research?buyerCountryCodes=US&categoryId&endDate=1530687599999&fromPrice&isAnyCriteria=false&keywords=jewelry&listingConditions=&listingTypes=&productId=&sellerCountryCodes&sellerName=&site=ALL&startDate=1528095600000&toPrice&transactionSite'

# This URL will fetch the page but finally, it makes several AJAX calls and this is the one which gets the actual data. You can investigate this using the FF devloper tools

data_url = 'https://sell.terapeak.com/services/research/listings?buyerCountryCodes=US&categoryId=&endDate=1530687599999&fromPrice=&isAnyCriteria=false&keywords=home%20decor&listingConditions=&listingTypes=&productId=&sellerCountryCodes=&sellerName=&site=ALL&startDate=1528095600000&toPrice=&transactionSite=&isTypeAheadSearch=false&source=&pageSize=10&pageNumber=1&sortBy=&sortDirection='

# The following extra headers will make this site think that this is coming from Firefox.
headers = {
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
    # 'Accept': 'application/json',
    # 'Accept-Language': 'en-US,en;q=0.5',
    # 'Referer': 'https://sell.terapeak.com/product-research?buyerCountryCodes=US&categoryId&endDate=1530687599999&fromPrice&isAnyCriteria=false&keywords=jewelry&listingConditions=&listingTypes=&productId=&sellerCountryCodes&sellerName=&site=ALL&startDate=1528095600000&toPrice&transactionSite',
    # 'content-type': 'application/json',
    # 'pragma': 'no-cache',
    # 'cache-control': 'no-cache, max-age=0',
    'authorization': 'Bearer 1a6jd3c3hgcrhmk4rlqivaok4gijev7faanfnhobkb1imdkh1lt4',
    # 'origin': 'https://sell.terapeak.com',
    # 'DNT': '1' ,
    # 'Connection': 'keep-alive'
}

# The following are cookies that we can use to get the auth working fine.





cookies = {"tp_ee_last_visit":"1217651514",
           "tp_ee_last_activity":"1533020299",
           "tp_ee_tracker":"%5B%5D",
           "tp_ee_csrf_token":"f225fd1aa28fc3003323ce2366bd03c2a2318411",
           # "totango.heartbeat.last_module":"product-research",
           # "totango.heartbeat.last_ts":"1530859573614",
           # "TPSERVERID":"blue_e",
           # "tp_ee_tracker":"%7B%220%22%3A%22index%22%2C%22token%22%3A%222ad40c2b997ade901d715b9f00a41b39%22%7D",
           # "i18next":"en-US",
           # "localeHeader":"en-US,en",
           # "optimizelyEndUserId":"oeu1530858706054r0.37924157291285776",
           # "optimizelySegments":"%7B%22229813889%22%3A%22ff%22%2C%22229833781%22%3A%22direct%22%2C%22229852304%22%3A%22false%22%7D",
           # "optimizelyBuckets":"%7B%7D",
           # "currency":"USD",
           # "tpebayCurrencyId":"1"
}

lastPage=False
page_number = 72
obj_ = amazonTera.workers()
while not lastPage:
    print ("Page number {}".format(page_number))
    x = data_url.replace("pageNumber=1", "pageNumber={}".format(page_number))
    r = requests.get(x, cookies = cookies, headers = headers)

    for q in r.json()["listings"]:
        l = json.dumps(q)
        #print l
        #num = q['itemId']
        obj_.process(l)
    lastPage = r.json()['lastPage']
    page_number = page_number + 1

import datetime
import re
import response_getter
import json
from helpers import  url_format, text_format
from CONSTANTS import *
import DataCollectors_Configuration
import uuid


def get_date_and_time():
    current_date = datetime.datetime.now()
    current_date.strftime("%y-%m-%d %H:%M:%S")
    current_date = str(current_date)
    return current_date.split(" ")


def get_hirerachy(hirerachy):
    items = hirerachy.split('|')
    length = len(items)
    category_names = ''
    for level in range(0, 10):
        if level < length:
            category_names = category_names + '{},'.format(items[level])
        else:
            category_names = category_names + 'not_available,'
    return category_names.split(',')


def get_product_specifications(raw_data):
    product_details_1 = raw_data.find('div', {'id': 'prodDetails'})
    product_details_2 = raw_data.find('table', {'id': 'productDetailsTable'})
    product_details_3 = raw_data.find('div', {'id': 'detailBullets_feature_div'})
    product_details_4 = raw_data.find('div', {'class': 'a-section a-spacing-large pzr-features-containers'})
    product_details_5 = raw_data.find('div', {'id': 'detail-bullets'})
    product_details_6 = raw_data.find('table', {'id': 'product-specification-table'})
    product_details_7 = raw_data.find('div', {'id': 'technicalSpecifications_feature_div'})
    product_details_8 = raw_data.find('div', {'id': 'detail_bullets_id'})
    specifications = {'default': 'not_available'}
    if product_details_2 and product_details_6:

        specification_container = product_details_2.find('td', {'class': 'bucket'})
        if specification_container:
            list1 = specification_container.findAll('li')
            for specs in list1:

                try:
                    spec = text_format(specs).split(':')
                    specifications.update(((spec[0], spec[1]),))
                except IndexError:
                    continue

        tr_tags = product_details_6.findAll('tr')
        if len(tr_tags) != 0:
            for tr_tag in tr_tags:
                if tr_tag.th:
                    key = text_format(tr_tag.th)
                    if key in 'Customer Reviews':
                        continue
                    else:
                        value = text_format(tr_tag.td)
                        specifications.update(((key, value),))
        return specifications

    elif product_details_4 and product_details_5:
        list1 = product_details_5.find_all('li')
        for specs in list1:
            try:
                spec = text_format(specs).split(':')

                specifications.update(((spec[0], spec[1]),))
            except IndexError:
                continue
        t_body = product_details_4.findAll('table')
        if len(t_body) != 0:
            for tag in t_body:
                tr_tags = tag.findAll('tr')
                for tr_tag in tr_tags:
                    if tr_tag.th:
                        key = text_format(tr_tag.th)
                        if key in 'Customer Reviews':
                            continue
                        else:
                            value = text_format(tr_tag.td)
                            specifications.update(((key, value),))
        return specifications

    elif product_details_8:
        list1 = product_details_8.find_all('li')
        for specs in list1:
            try:
                spec = text_format(specs).split(':')

                specifications.update(((spec[0], spec[1]),))
            except IndexError:
                continue
        return specifications

    elif product_details_7:
        table_container = product_details_7.find('table', {'id': 'technicalSpecifications_section_1'})
        if table_container:
            tr_tags = table_container.findAll('tr')
            if len(tr_tags) != 0:
                for tr in tr_tags:
                    if tr.th:
                        key = tr.th.text.strip()
                        if tr.td:
                            value = tr.td.text.strip()
                            specifications.update(((key, value),))
                        return specifications
    elif product_details_5:
        list1 = product_details_5.find_all('li')
        for specs in list1:
            try:
                spec = text_format(specs).split(':')

                specifications.update(((spec[0], spec[1]),))
            except IndexError:
                continue
        return specifications

    elif product_details_1:
        t_body = product_details_1.findAll('table')

        if len(t_body) != 0:
            for tag in t_body:

                tr_tags = tag.findAll('tr')
                for tr_tag in tr_tags:
                    if tr_tag.th:
                        key = text_format(tr_tag.th)
                        if key in 'Customer Reviews':
                            continue
                        else:
                            value = tr_tag.td.text.strip()
                            specifications.update(((key, value),))
                    else:
                        td_tags = tr_tag.findAll('td')
                        if len(td_tags) != 0 and len(td_tags) >= 2:
                            specifications.update(((text_format(td_tags[0]), text_format(td_tags[1])),))

            return specifications

    elif product_details_2:
        specification_container = product_details_2.find('td', {'class': 'bucket'})
        if specification_container:
            list1 = specification_container.findAll('li')
            for specs in list1:

                try:
                    spec = text_format(specs).split(':')
                    specifications.update(((spec[0], spec[1]),))
                except IndexError:
                    continue
        return specifications

    elif product_details_3:
        list2 = product_details_3.find_all('span', {'class': 'a-list-item'})
        for specs in list2:
            try:
                spec = text_format(specs).split(':')
                specifications.update(((spec[0], spec[1]),))
            except IndexError:
                continue
        return specifications
    else:
        return specifications

    return specifications


def get_brand(raw_data):
    brand_tag_1 = raw_data.find('a', {'id': 'bylineInfo'})
    brand_tag_2 = raw_data.find('a', {'id': 'brand'})
    if brand_tag_1:
        return text_format(brand_tag_1)
    elif brand_tag_2:
        brand_name = text_format(brand_tag_2)
        if len(brand_name) == 0:
            brand_image_tag = brand_tag_2.find('img')
            if brand_image_tag:
                brand_img = brand_image_tag['src']
                return brand_img
        return text_format(brand_tag_2)
    return 'not_availabe'


def get_title(raw_data):
    title_tag_1 = raw_data.find('span', {'id': 'productTitle'})
    title_tag_2 = raw_data.find('span', {'id': 'ebooksProductTitle'})
    if title_tag_1:
        title = text_format(title_tag_1)
        return title
    if title_tag_2:
        title = text_format(title_tag_2)
        return title
    else:
        return 'not_available'


def get_author_name(raw_data):
    author_tag_1 = raw_data.find('a', {'class': 'a-link-normal contributorNameID'})
    author_tag_2 = raw_data.find_all("span", {'class': 'author notFaded'})
    if author_tag_1:
        author_name = text_format(author_tag_1)
        return author_name
    elif author_tag_2:
        author_name = ''
        for auth in author_tag_2:
            auther_details = auth.text.replace("Author", "").replace("()", "").replace(",", "").replace("\n",
                                                                                                        "").strip() + "|"
            author_name = author_name + auther_details
        return author_name
    else:
        return 'not_available'


def get_product_rating(raw_data):
    rating_tag_1 = raw_data.find('a', {'id': 'cmrsSummary-popover'})
    rating_tag_2 = raw_data.find('div', {'class': 'a-spacing-none', 'id': 'averageCustomerReviews'})
    if rating_tag_2:

        rating_tag = rating_tag_2.find('span', {'class': 'a-icon-alt'})
        if rating_tag:
            rating = text_format(rating_tag)
            if rating:
                return rating.split('stars')[0]

    if rating_tag_1:
        rating_tag = rating_tag_1.find('span', {'class': 'a-icon-alt'})
        if rating_tag:
            rating = text_format(rating_tag)
            if rating:
                return rating.split('stars')[0]

    return 'not_available'


def get_selling_price(raw_data):
    price_tag_1 = raw_data.find('span', {'class': 'a-size-medium a-color-price offer-price a-text-normal'})
    price_tag_2 = raw_data.find('span', {'class': 'a-size-medium a-color-price header-price'})
    price_tag_3 = raw_data.find('span', {'id': 'priceblock_ourprice'})
    price_tag_4 = raw_data.find('span', {'class': 'a-size-medium a-color-price'})
    price_tag_5 = raw_data.find('tr', {'id': 'newPriceRow'})
    price_tag_6 = raw_data.find('tr', {'id': 'usedPriceRow'})
    price_tag_7 = raw_data.find('div', {'id': 'price-quantity-container'})
    price_tag_8 = raw_data.find('td', {'class': 'a-color-price a-size-medium a-align-bottom'})
    if price_tag_1:
        price_tag = price_tag_1.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
        return price
    elif price_tag_2:
        price_tag = price_tag_2.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
        return price
    elif price_tag_5:
        price_tag = price_tag_5.find('span', {'class': 'buyingPrice'})
        if price_tag:
            price_text = price_tag.text
            if 'EUR' in price_text:
                price = re.sub('[^0-9\-.,]', '', price_text).replace(',', '.')
            else:
                price = re.sub('[^0-9\-.]', '', price_text).replace(',', '')
            if len(price) != 0:
                return price
            elif price_tag_6:
                price_tag = price_tag_6.find('span', {'class': 'buyingPrice'})
                if price_tag:
                    price_text = price_tag.text
                    if 'EUR' in price_tag:
                        price = re.sub('[^0-9\-.,]', '', price_text).replace(',', '.')
                    else:
                        price = re.sub('[^0-9\-.]', '', price_text).replace(',', '')
                    return price
    elif price_tag_3:
        price_tag = price_tag_3.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
        return price
    elif price_tag_4:
        price_tag = price_tag_4.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
        return price
    elif price_tag_7:
        price_tag = price_tag_7.find('span', {'class':'a-size-large a-color-price guild_priceblock_ourprice'})
        if price_tag:
            price_tag = price_tag.text
            if 'EUR' in price_tag:
                price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
            else:
                price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
            return price
    elif price_tag_8:
        price_tag = price_tag_8.text
        if 'EUR' in price_tag:
            # I am spiting it because selling price and saved price are comming from same tag
            price_text = price_tag.strip().split(" ")
            price = re.sub('[^0-9\-.,]', '', price_text[1]).replace(',', '.')
        else:
            price_text = price_tag.strip().split(" ")
            price = re.sub('[^0-9\-.]', '', price_text[1]).replace(',', '')
        return price
    return 'not_available'


def get_original_price(raw_data):
    price_tag_1 = raw_data.find('span', {'class': 'a-color-secondary a-text-strike'})
    price_tag_2 = raw_data.find('span', {'class': 'a-text-strike'})
    price_tag_3 = raw_data.find('td', {'class': 'a-color-base a-align-bottom a-text-strike'})

    if price_tag_3:
        price_tag = price_tag_3.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
        return price

    elif price_tag_1:
        price_tag = price_tag_1.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
        return price

    elif price_tag_2:
        price_tag = price_tag_2.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-.]', '', price_tag).replace(',', '')
        return price


    return 'not_available'

def get_saved_price(raw_data):
    price_container_1 = raw_data.find('ul', {'class': 'a-unordered-list a-nostyle a-vertical'})
    price_container_2 = raw_data.findAll('div', {'class': 'a-section a-spacing-none a-text-right'})
    price_container_3 = raw_data.find('td', {'class': 'a-span12 a-color-price a-size-base'})
    price_container_4 = raw_data.find('p',{'class': 'a-size-mini a-color-price ebooks-price-savings a-text-normal'})
    if len(price_container_2) != 0:

        for price_container in price_container_2:
            price_tag = price_container.find('span', {'class': 'a-nowrap'})
            if price_tag:
                saved_price = price_tag.find('span', {'class': 'a-size-base a-color-secondary'})
                if saved_price:
                    saved_price_tag = saved_price.text
                    if 'EUR' in price_tag:
                        price = re.sub('[^0-9\-()%.,]', '', str(saved_price_tag)).replace(',', '.')
                    else:
                        price = re.sub('[^0-9\-()%.]', '', str(saved_price_tag)).replace(',', '')
                    return price

    if price_container_1:
        price_tag = price_container_1.find('span', {'class': 'a-size-base a-color-secondary'})
        if price_tag:
            price_tag = price_tag.text
            if 'EUR' in price_tag:
                price = re.sub('[^0-9\-()%.,]', '', price_tag).replace(',', '.')
            else:
                price = re.sub('[^0-9\-()%.]', '', price_tag).replace(',', '')
            return price

    if price_container_3:
        price_tag = price_container_3.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-()%.,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-()%.]', '', price_tag).replace(',', '')
        return price

    if price_container_4:
        price_tag = price_container_4.text
        if 'EUR' in price_tag:
            price = re.sub('[^0-9\-.()%,]', '', price_tag).replace(',', '.')
        else:
            price = re.sub('[^0-9\-()%.]', '', price_tag).replace(',', '')
        return price

    return 'not_available'

def get_availablity(raw_data):
    availablity_tag_1 = raw_data.find('div', {'id': 'availability'})
    availablity_tag_2 = raw_data.find('p', {'class': 'a-spacing-micro a-color-secondary a-text-bold'})
    if availablity_tag_1:
        availablity = text_format(availablity_tag_1)
        return availablity
    elif availablity_tag_2:
        availablity = text_format(availablity_tag_2)
        return availablity
    return 'not_available'


def get_highlights(raw_data):
    highlights_tag_1 = raw_data.find('div', {'id': 'bookDescription_feature_div'})
    highlights_tag_2 = raw_data.find('div', {'id': 'feature-bullets'})
    highlights = {'text': []}
    if highlights_tag_1:
        highlights_container = highlights_tag_1.find('noscript')
        if highlights_container:
            highlights['text'].append(text_format(highlights_container))
            return highlights

    elif highlights_tag_2:

        highlights_container_1 = highlights_tag_2.find('ul', {'class': 'a-unordered-list a-vertical a-spacing-none'})
        highlights_container_2 = highlights_tag_2.find('span', {'class': 'a-color-base technicalData'})

        if highlights_container_1:
            highlights_list = highlights_container_1.findAll('li')
            if len(highlights_list) !=0:
                for highlights_text in highlights_list:
                    text = highlights_text.text.strip()
                    highlights['text'].append(text)
                return highlights

        if highlights_container_2:
            highlights_list = highlights_container_2.findAll('li')
            if len(highlights_list) != 0:
                for highlights_text in highlights_list:
                    text = highlights_text.text.strip()
                    highlights['text'].append(text)
                return highlights


    highlights['text'].append('not_available')
    return highlights


# returrns json object
def get_other_format_books_price(raw_data):
    other_format_price_container = raw_data.find('div', {'id': 'tmmSwatches'})
    other_prices = {'default': 'not_available'}
    if other_format_price_container:
        price_tags = other_format_price_container.findAll('span', {'class': 'a-list-item'})
        if len(price_tags) != 0:

            for price_tag in price_tags:
                book_type_tag = price_tag.find('a')
                price_container = price_tag.find('span', {'class': 'a-color-secondary'})
                if book_type_tag and price_container:
                    book_type = text_format(book_type_tag.span)
                    price = text_format(price_container)

                    other_prices.update(((book_type, price.replace('_', '')),))
            return other_prices
    else:
        return other_prices


def get_quantity(raw_data):
    quantity_container = raw_data.find('select', {'name': 'quantity'})
    if quantity_container:
        quantity_no = quantity_container.findAll('option')
        if len(quantity_no) != 0:
            quantity = text_format(quantity_no[-1])
            return quantity
        else:
            return 'not_available'
    else:
        return 'not_available'


def get_image_url(raw_data):
    image_container_1 = raw_data.find('div', {'id': 'img-wrapper'})
    image_container_2 = raw_data.find('div', {'id': 'mainImageContainer'})
    image_container_3 = raw_data.find('div', {'id': 'imgTagWrapperId'})
    image_container_4 = raw_data.find('div', {'id': 'ebooks-img-canvas'})
    if image_container_1:
        image_url_tag = image_container_1.find('img')
        if image_url_tag:
            image_url = image_url_tag['data-a-dynamic-image']
            return image_url
        else:
            return 'not_available'
    elif image_container_2:
        image_url_tag = image_container_2.find('img')
        if image_url_tag:
            image_url = image_url_tag['data-a-dynamic-image']
            return image_url
    elif image_container_3:
        image_url_tag = image_container_3.find('img')
        if image_url_tag:
            image_url = image_url_tag['data-a-dynamic-image']
            return image_url
        else:
            return 'not_available'
    elif image_container_4:
        image_url_tag = image_container_4.find('img')
        if image_url_tag:
            image_url = image_url_tag['data-a-dynamic-image']
            return image_url
        else:
            return 'not_available'

    return 'not_available'


# returns json object
def get_product_description(raw_data):
    description_container = raw_data.find('div', {'id': 'productDescription'})
    description = {'text': ''}
    if description_container:
        description_text_tag = description_container.find('div', {
            'class': 'a-expander-content a-expander-partial-collapse-content'})
        if description_text_tag:
            description['text'] = text_format(description_text_tag)
            return description
        else:
            description['text'] = text_format(description_container)
            return description

    else:
        description['text'] = 'not_available'
        return description


# Gets manufacturer of the product
def get_product_manufacturer(response):
    product_info_table_container_2 = response.find('div', {'class': 'aplus-v2 desktop celwidget'})
    from_manufracture = {'img': [], 'text': []}
    if product_info_table_container_2:

        description_images = product_info_table_container_2.findAll('img')
        description_paragraph = product_info_table_container_2.findAll('p')
        description_text = product_info_table_container_2.findAll('span', {'class': 'a-list-item'})

        if len(description_images) and len(description_text) and len(description_paragraph):

            for image in description_images:
                from_manufracture['img'].append(image['src'])
            for text in description_text:
                from_manufracture['text'].append(text_format(text))
            for text in description_paragraph:
                from_manufracture['text'].append(text_format(text))
            return from_manufracture

        elif len(description_images) and len(description_text):

            for image in description_images:
                from_manufracture['img'].append(image['src'])
            for text in description_text:
                from_manufracture['text'].append(text_format(text))
            return from_manufracture

        elif len(description_images) and len(description_paragraph):

            for image in description_images:
                from_manufracture['img'].append(image['src'])
            for text in description_paragraph:
                from_manufracture['text'].append(text_format(text))
            return from_manufracture

        elif len(description_images):
            for image in description_images:
                from_manufracture['img'].append(image['src'])
            return from_manufracture

        elif len(description_text):

            for text in description_text:
                from_manufracture['text'].append(text_format(text))
            return from_manufracture
    else:
        from_manufracture['text'].append('not_available')
        from_manufracture['img'].append('not_available')
        return from_manufracture

    # return 'not_available'


def get_product_no_of_reviews(page_soup):
    noofreviews = page_soup.find('span', {'id': 'acrCustomerReviewText'})
    if noofreviews:
        reviews_text = noofreviews.text.replace("customer reviews", "").replace(",", "")
        if reviews_text:
            reviews = re.sub('[^0-9\-:]', '', reviews_text)
            return reviews
        else:
            return "not_available"
    else:
        return "not_available"


def get_color_variantes(raw_data):
    varaiants_tag = raw_data.find('div', {'id': 'variation_color_name'})
    if varaiants_tag:
        varaiants_list = varaiants_tag.findAll('li')
        if len(varaiants_list):
            color_list = []
            for varaiants in varaiants_list:
                varaiant_1 = varaiants.find('img')
                varaiant_2 = varaiants.find('div',{'class':'twisterTextDiv text'})
                if varaiant_1:
                    # print varaiant
                    color = varaiant_1['alt']
                    color_list.append(color)
                elif varaiant_2:
                    color = text_format(varaiant_2)
                    color_list.append(color)
            return '|'.join(color_list)

    return 'not_available'


def get_style_variants(raw_data):
    style_tag_container = raw_data.find('div', {'id': 'twisterContainer'})
    if style_tag_container:

        style_list = style_tag_container.findAll('li')
        if len(style_list) != 0:
            style = []
            for style_tag in style_list:
                style_text = style_tag.find('span', {'class': 'a-size-base'})
                if style_text:
                    style_text = text_format(style_text)
                    if style_text:
                        style.append(style_text)
                else:
                    return 'not_available'
            return '|'.join(style)
        else:
            return 'not_available'
    else:
        return 'not_available'


def get_specail_promotion(raw_data):
    promotion_container = raw_data.find('div', {'id': 'quickPromoBucketContent'})
    promotion = {'text': []}
    if promotion_container:
        text_list = promotion_container.find_all('li')
        if len(text_list):
            for text_tag in text_list:
                text_string = text_format(text_tag)
                if text_string:
                    promotion['text'].append(text_string)
            return promotion
    promotion['text'].append('not_available')
    return promotion


def get_seller_info(seller_name, seller_raw_data):
    seller_rating = get_seller_rating(seller_raw_data)
    seller_store_link = get_seller_strore_link(seller_raw_data)
    seller_postive_rating = get_seller_positive_rating(seller_raw_data)
    seller_overall_rating = get_seller_overall_rating(seller_raw_data)  # json
    seller_description = get_seller_description(seller_raw_data)
    seller_detailed_information = get_seller_detailed_information(seller_raw_data)  # json

    return seller_name, seller_store_link, seller_rating, seller_postive_rating, \
           seller_overall_rating, seller_description, seller_detailed_information


def check_and_get_seller_data(raw_data):
    seller_name_tag = raw_data.find('a')
    if seller_name_tag:
        seller_name = text_format(seller_name_tag)
        seller_link = url_format(seller_name_tag['href'])
        seller_raw_data = response_getter.get_content(seller_link)
        if seller_raw_data:
            return get_seller_info(seller_name, seller_raw_data)
        else:
            return seller_name, 'not_available', 'not_available', 'not_available', 'not_available', 'not_available', 'not_available'
    else:
        seller_name = text_format(raw_data)
        if seller_name:
            return seller_name, 'not_available', 'not_available', 'not_available', 'not_available', 'not_available', 'not_available'
    return 'not_available', 'not_available', 'not_available', 'not_available', 'not_available', 'not_available', 'not_available'



def get_seller_details(page_soup):
    seller_container_1 = page_soup.find('div', {'id': 'merchant-info'})
    sellar_container_2 = page_soup.find('p', {'class': 'a-spacing-micro a-color-base'})
    if seller_container_1:
        return check_and_get_seller_data(seller_container_1)
    elif sellar_container_2:
        return check_and_get_seller_data(sellar_container_2)

    return 'not_available', 'not_available', 'not_available', 'not_available', 'not_available', 'not_available', 'not_available'


# returns json data
def get_seller_overall_rating(page_soup):
    seller_raing = {'30_days': {'positive': 'not_available', 'negative': 'not_available', 'neutral': 'not_available',
                                'count': 'not_available'},
                    '90_days': {'positive': 'not_available', 'negative': 'not_available', 'neutral': 'not_available',
                                'count': 'not_available'},
                    '120_days': {'positive': 'not_available', 'negative': 'not_available', 'neutral': 'not_available',
                                 'count': 'not_available'},
                    'life_time': {'positive': 'not_available', 'negative': 'not_available', 'neutral': 'not_available',
                                  'count': 'not_available'}
                    }

    rating_container = page_soup.find('table', {'id': 'feedback-summary-table'})
    if rating_container:
        tables = rating_container.findAll('tr')
        if len(tables) != 0:
            for row in tables[1:]:
                row_list = []
                td_tags = row.findAll('td')
                if len(td_tags) != 0:
                    for element in td_tags:
                        row_list.append((text_format(element)))
                    seller_raing['30_days'][row_list[0].lower()] = row_list[1]
                    seller_raing['90_days'][row_list[0].lower()] = row_list[2]
                    seller_raing['120_days'][row_list[0].lower()] = row_list[3]
                    seller_raing['life_time'][row_list[0].lower()] = row_list[4]
    return seller_raing


def get_seller_strore_link(raw_data):
    store_link_tag = raw_data.find('div', {'id': 'storefront-link'})
    if store_link_tag:
        if store_link_tag.a:
            return url_format(store_link_tag.a['href'])
        else:
            return 'not_avaible'
    else:
        return 'not_avaible'


def get_seller_rating(raw_data):
    rating_container = raw_data.find('span', {'class': 'a-icon-alt'})
    if rating_container:
        rating = text_format(rating_container)
        if 'template-formatted' in rating:
            return 'no_feedback'
        else:
            return rating
    else:
        return 'not_available'


def get_seller_positive_rating(raw_data):
    positive_rating = raw_data.find('a', {'class': 'a-link-normal feedback-detail-description'})
    if positive_rating:
        return text_format(positive_rating.b)
    else:
        return 'not_available'


def get_seller_detailed_information(raw_data):
    information_container = raw_data.findAll('div', {'class': 'a-column a-span6'})
    information = {'default': []}
    if len(information_container) != 0:
        for info_container in information_container:
            info_table_container = info_container.find('ul', {'class': 'a-unordered-list a-nostyle a-vertical'})
            if info_table_container:
                info_list = info_table_container.findAll('span', {'class': 'a-list-item'})
                for info_tag in info_list:
                    info_text = info_tag.find('ul', {'class': 'a-unordered-list a-nostyle a-vertical'})
                    if info_text:
                        key = text_format(info_tag.span)
                        information.update(((key, []),))

                        text_list = info_text.findAll('li')

                        if len(text_list) != 0:
                            for text_tag in text_list:
                                information[key].append(text_tag.text)
                    else:
                        text_tag = info_tag.text
                        if text_tag:
                            try:
                                key_value_pair = text_tag.split(':')
                                information.update(((key_value_pair[0], key_value_pair[1]),))
                            except IndexError:
                                continue
                return information
    information['default'].append('not_available')
    return information


def get_seller_description(raw_data):
    description_container_1 = raw_data.find('span', {'id': 'about-seller-text'})
    description_container_2 = raw_data.find('div', {'id': 'about-seller'})
    if description_container_1:
        description = text_format(description_container_1)
        if len(description) != 0:
            return description
    elif description_container_2:
        description = text_format(description_container_2)
        if len(description) != 0:
            return description
    else:
        return 'not_available'
    return 'not_available'


def get_rating_details(raw_data):
    rating_types = {'5_star': 'not_available',
                    '4_star': 'not_available',
                    '3_star': 'not_available',
                    '2_star': 'not_available',
                    '1_star': 'not_available'}
    review_container = raw_data.find('table', {'id': 'histogramTable'})
    if review_container:
        rating_tr_tag = review_container.findAll('tr')
        if len(rating_tr_tag) != 0:
            for rating_tr in rating_tr_tag:
                rt_list = []
                td_tags = rating_tr.findAll('td')
                if len(td_tags) != 0:
                    for td in td_tags:
                        if td.a:
                            rt_list.append(text_format(td.a))
                        else:
                            rt_list.append('0')
                    rating_types[rt_list[0]] = rt_list[-1]

            return rating_types
        else:
            return rating_types
    return rating_types


def find_if_handmade(raw_data):
    hand_made_container = raw_data.find('div', {'id': 'handmadeLogo_feature_div'})
    if hand_made_container:
        return True
    else:
        return False


def find_if_exits(input_val):
    if input_val:
        if 'not_available' in input_val:
            return 'not_available'
        return input_val.replace('_', '')
    else:
        return 'not_available'


def validate_selling_price(input_val):
    if input_val == '.':
        return 'not_available'
    else:
        return input_val


def find_average_price(input_val):
    if '-' in input_val:
        values = input_val.split('-')
        if len(values) !=0:
            avg = 0
            for value in values:
                avg = avg+float(value)
            avg = avg/2
            return avg
    if 'not_available' == input_val:
        return float(0)

    else:
        return float(input_val)


def get_data_for_cassandra(product_dic):
    product = dict()
    product['id']               = uuid.uuid1()
    product['asin']             = product_dic['asin']
    product['category']         = product_dic['category']
    product['category_level_1'] = product_dic['category_level_1']
    product['category_level_2'] = product_dic['category_level_2']
    product['category_level_3'] = product_dic['category_level_3']
    product['currency']         = product_dic['currency']
    product['date']             = product_dic['date']
    product['marketplace']      = product_dic['marketplace']
    product['price']            = find_average_price(product_dic['product_selling_price'])
    product['product_id']       = product_dic['product_id']
    product['seller_name']      = product_dic['seller_name']
    product['additional_info']  = {}

    product_keys = product.keys()
    product_dic_keys = product_dic.keys()

    for key in product_dic_keys:
        if key not in product_keys:
            product['additional_info'].update(((key, product_dic[key]),))

    return product


def get_data(raw_data, hierarchy, product_url):
    hirerachy_list = get_hirerachy(hierarchy)
    date = get_date_and_time()
    seller_name, seller_store_link, seller_rating, seller_postive_rating, seller_overall_rating, seller_description, seller_detailed_information = get_seller_details(
        raw_data)
    product = dict()
    specifications = get_product_specifications(raw_data)
    asin = 'not_available'
    try:
        asin = specifications.get('ASIN').replace('_', '')
    except AttributeError:
        if find_if_handmade(raw_data):
            pass
        else:
            return None

    # print(hirerachy_list)
    # product is a dictionary and used superset field names as keys and get values by your own
    # parsing methods and assign them key values

    product['sku']                            = 'NA'
    product['asin']                           = asin
    product['date']                           = date[0]
    product['time']                           = date[1]
    product['marketplace']                    = MARKET_PLACE_NAME
    product['domain']                         = DOMAIN_NAME
    product['category']                       = hirerachy_list[0]
    product['category_level_1']               = hirerachy_list[1]
    product['category_level_2']               = hirerachy_list[2]
    product['category_level_3']               = hirerachy_list[3]
    product['category_level_4']               = hirerachy_list[4]
    product['category_level_5']               = hirerachy_list[5]
    product['category_level_6']               = hirerachy_list[6]
    product['category_level_7']               = hirerachy_list[7]
    product['category_level_8']               = hirerachy_list[8]
    product['category_level_9']               = hirerachy_list[9]

    if DataCollectors_Configuration.WRITE_TO == WRITE_TO_CASSANDRA:
        product['condition']                    = 'NA'
        product['additional_policies']          = 'NA'
        product['description']                  = get_product_description(raw_data)
        product['highlights']                   = get_highlights(raw_data)
        product['rating_details']               = get_rating_details(raw_data)
        product['specifications']               = get_product_specifications(raw_data)
        product['seller_overall_rating']        = seller_overall_rating
        product['seller_description']           = seller_description
        product['return_policies']              = 'NA'
        product['warrenty']                     = 'NA'
        product['shipping_policies']            = 'NA'
        product['from_manufracture']            = get_product_manufacturer(raw_data)
        product['promotion']                    = get_specail_promotion(raw_data)
        product['other_format_prices']          = get_other_format_books_price(raw_data)
        product['seller_detailed_information']  = seller_detailed_information
    else:
        product['condition']                    = json.dumps({'condition': 'NA'})
        product['additional_policies']          = json.dumps({'Additional_policies': 'NA'})
        product['description']                  = json.dumps({'description': get_product_description(raw_data)})
        product['highlights']                   = json.dumps({'highlights': get_highlights(raw_data)})
        product['rating_details']               = json.dumps(get_rating_details(raw_data))
        product['specifications']               = json.dumps(get_product_specifications(raw_data))
        product['seller_overall_rating']        = json.dumps(seller_overall_rating)
        product['seller_description']           = json.dumps({'seller_description': seller_description})
        product['return_policies']              = json.dumps({'return_policies': 'NA'})
        product['warrenty']                     = json.dumps({'warrenty': 'NA'})
        product['shipping_policies']            = json.dumps({'shipping_policies': 'NA'})
        product['from_manufracture']            = json.dumps(get_product_manufacturer(raw_data))
        product['promotion']                    = json.dumps(get_specail_promotion(raw_data))
        product['other_format_prices']          = json.dumps(get_other_format_books_price(raw_data))
        product['seller_detailed_information']  = json.dumps(seller_detailed_information)

    product['saved_price']                  = get_saved_price(raw_data)
    product['added_date']                   = 'NA'
    product['availability']                 = get_availablity(raw_data)
    product['brand']                        = get_brand(raw_data)
    product['discount_percentage']          = 'NA'
    product['product_selling_price']        = validate_selling_price(get_selling_price(raw_data))
    product['product_EAN']                  = find_if_exits(specifications.get('EAN'))
    product['product_id']                   = 'NA'
    product['image_url']                    = get_image_url(raw_data)
    product['likes']                        = 'NA'
    product['isbn']                         = 'NA'
    product['isbn-10']                      = find_if_exits(specifications.get('ISBN-10'))
    product['isbn-13']                      = find_if_exits(specifications.get('ISBN-13'))
    product['MPN']                          = find_if_exits(specifications.get('Manufacturer_Part_Number'))
    product['name']                         = get_title(raw_data)
    product['no_of_reviews']                = get_product_no_of_reviews(raw_data)
    product['original_price']               = get_original_price(raw_data)
    product['rating']                       = get_product_rating(raw_data)
    product['shipping_price']               = 'NA'
    product['size']                         = 'NA'
    product['upc']                          = find_if_exits(specifications.get('UPC'))
    product['url']                          = product_url
    product['quantity_available']           = get_quantity(raw_data)
    product['products_slod']                = 'NA'
    product['seller_code']                  = 'NA'
    product['seller_location']              = 'NA'
    product['seller_name']                  = find_if_exits(seller_name)
    product['seller_negative_rating']       = 'NA'
    product['seller_neutral_rating']        = 'NA'
    product['seller_positive_rating']       = seller_postive_rating
    product['seller_rank']                  = 'NA'
    product['seller_store_link']            = seller_store_link
    product['seller_year_of_joining']       = 'NA'
    product['shipping_available_countries'] = 'NA'
    product['shipping_location']            = 'NA'
    product['shipping_logistic_name']       = 'NA'
    product['shipping_price']               = 'NA'
    product['shop_location']                = 'NA'
    product['shop_name']                    = 'NA'
    product['no_of_sales']                  = 'NA'
    product['shop_rating']                  = seller_rating
    product['Tax_info']                     = 'NA'
    product['Visibility']                   = 'NA'
    product['currency']                     = CURRENCY
    product['color_variants']               = get_color_variantes(raw_data)
    product['style_variants']               = get_style_variants(raw_data)
    product['author_name']                  = get_author_name(raw_data)

    return product
from Common.Ebay_common_imports import *
def to_db(product):
    # Assign your respective connection details

    db = pymysql.connect(host= DataCollectors_Configuration.MYSQL_HOST,
                         user= DataCollectors_Configuration.MYSQL_USER_NAME,
                         passwd= DataCollectors_Configuration.MYSQL_PASSWORD,
                         db= DataCollectors_Configuration.MYSQL_DB_name,
                         use_unicode= True,
                         charset= "utf8")

    # to execute PostgreSQL command in a database session
    cursor = db.cursor()

    # Assign values in VALUES variable with respect to COLUMN NAMES in SQL variable
    values = product
    sql = "INSERT INTO `products` " \
          "(" \
          "  `product_date`,               `product_time`,                    `product_marketplace`,         `product_domain`,  " \
          "  `product_category`,           `product_subcategory_1`,       `product_subcategory_2`,       `product_subcategory_3`," \
          "    `product_subcategory_4`,       `product_subcategory_5`,       `product_subcategory_6`,       `product_subcategory_7`," \
          "    `product_subcategory_8`,       `product_subcategory_9`,       `product_condition`,           `product_saved_price`, " \
          " `product_added_Date`,          `product_additional_policies`, `product_availability`,            `product_brand`," \
          "    `product_description`,         `product_discount_percentage`, `product_selling_price`,       `product_ean`," \
          "    `product_highlights`,          `product_id`,                  `product_image_url`,           `product_likes`,           `product_isbn`," \
          "    `product_isbn_10`,             `product_isbn_13`,             `product_mpn`,                 `product_name`," \
          "    `product_no_of_reviews`,       `product_original_price`,      `product_rating`,              `product_rating_details`," \
          "    `product_shipping_policies`,   `product_size`,                    `product_sku`,                 `product_upc`," \
          "    `product_url`,                 `products_available`,          `products_sold`,               `product_return_policies`," \
          "    `seller_code`,                 `seller_location`,             `seller_name`,                 `seller_negative_rating`," \
          "    `seller_neutral_rating`,       `seller_positive_rating`,      `seller_overall_rating`,       `seller_rank`," \
          "    `seller_store_link`,           `seller_year_of_joining`,      `shipping_available_countries`,    `shipping_location`," \
          "    `shipping_logistic_name`,      `shipping_price`,              `shop_location`,               `shop_name`," \
          "    `shop_noofsales`,              `shop__rating`,                    `tax_information`,             `product_visibility`," \
          "    `product_warranty`,                `product_currency`,                `product_specifications`,      `product_shipping_price`," \
          "    `from_manufacture`,                `color_variants`,              `style_variants`,              `promotion`," \
          "    `author_name`,                 `other_format_prices`,          `seller_description`,           `product_asin`, " \
          " `sellar_detailed_information`) " \
          "VALUES" \
          "(  %s,  %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          " %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s,    %s," \
          "    %s,    %s,    %s, %s, " \
          " %s, %s)"

    cursor.execute(sql, values)
    cursor.close()
    db.commit()
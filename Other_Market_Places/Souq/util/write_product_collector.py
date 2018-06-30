destination_path = '/home/eunimart-04/eunimart_dev_akhil/Souq/product_info_collectors'

source_path = '/home/eunimart-04/eunimart_dev_akhil/Souq/util/product_info_collector.py'

category_list = ['Apparel_Shoes_and_Accessories', 'Art_Crafts_and_Collectibles', 'Baby', 'Beauty', 'Bed_and_Bath',
                 'Books',
                 'Cameras', 'Coins_Stamps_and_Paper_money', 'Computers_IT_and_Networking', 'Electronics',
                 'Eyewear_and_Optics', 'Furniture', 'Gaming', 'Garden_and_Outdoor', 'Grocery_Food_and_Beverages',
                 'Health_and_Personal_Care', 'Home_Appliances', 'Home_Decor_and_Furniture', 'Jewelry_and_Accessories',
                 'Kitchen_and_Home_Supplies', 'Kitchen_Appliances', 'Mobile_Phones_Tablets_and_Accessories',
                 'Music_and_Movies', 'Office_Products_and_Supplies', 'Perfumes_and_Fragrances', 'Pet_Food_and_Supplies',
                 'Sports_and_Fitness', 'Tools_and_Home_Improvements', 'Toys', 'Vehicle_Parts_and_Accessories',
                 'Vouchers_and_Tickets', 'Wearable_Technology_Devices']


file_path = '{}/{}_info_collector.py'

line_1 = "Apparel_Shoes_and_Accessories_info_collection:"
Changed_line_1 = "{}_info_collection:"

line_2 = "DataCollectors_Configuration.APPAREL_SHOES_AND_ACCESSORIES"
Changed_line_2 ="DataCollectors_Configuration.{}"

line_3 = 'Apparel_Shoes_and_Accessories_ProductDetails'
Changed_line_3 = '{}_ProductDetails'

line_4 = "starting Apparel_Shoes_and_Accessories information collection"
Changed_line_4 = "starting {} information collection"

for category in category_list:
    files = open(source_path,'rt')
    lines = []
    for line in files:
        if line_1 in line:
            lines.append(line.replace(line_1, Changed_line_1.format(category)))
        elif line_2 in line:

            lines.append(line.replace(line_2, Changed_line_2.format(category.upper())))
        elif line_3 in line:

            lines.append(line.replace(line_3, Changed_line_3.format(category)))
        elif line_4 in line:

            lines.append(line.replace(line_4, Changed_line_4.format(category)))
        else:

            lines.append(line)
    write_file = open(file_path.format(destination_path, category),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
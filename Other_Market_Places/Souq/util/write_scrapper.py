

destination_path = '/home/eunimart-04/eunimart_dev_akhil/Souq/scrappers'

source_path = '/home/eunimart-04/eunimart_dev_akhil/Souq/util/scrape_urls.py'

category_list = ['Apparel_Shoes_and_Accessories', 'Art_Crafts_and_Collectibles', 'Baby', 'Beauty', 'Bed_and_Bath',
                 'Books',
                 'Cameras', 'Coins_Stamps_and_Paper_money', 'Computers_IT_and_Networking', 'Electronics',
                 'Eyewear_and_Optics', 'Furniture', 'Gaming', 'Garden_and_Outdoor', 'Grocery_Food_and_Beverages',
                 'Health_and_Personal_Care', 'Home_Appliances', 'Home_Decor_and_Furniture', 'Jewelry_and_Accessories',
                 'Kitchen_and_Home_Supplies', 'Kitchen_Appliances', 'Mobile_Phones_Tablets_and_Accessories',
                 'Music_and_Movies', 'Office_Products_and_Supplies', 'Perfumes_and_Fragrances', 'Pet_Food_and_Supplies',
                 'Sports_and_Fitness', 'Tools_and_Home_Improvements', 'Toys', 'Vehicle_Parts_and_Accessories',
                 'Vouchers_and_Tickets', 'Wearable_Technology_Devices']

file_path = "{}/{}_scrape_urls.py"

line_1 = "self.queue_file = Souq.path_CONSTANTS.Apparel_Shoes_and_Accessories_QUEUE_FILE"
Changed_line_1 = "self.queue_file = Souq.path_CONSTANTS.{}_QUEUE_FILE"

line_2 = "self.completed_file = Souq.path_CONSTANTS.Apparel_Shoes_and_Accessories_COMPLETED_FILE"
Changed_line_2 = "self.completed_file = Souq.path_CONSTANTS.{}_COMPLETED_FILE"

line_3 = "self.skipped_file = Souq.path_CONSTANTS.Apparel_Shoes_and_Accessories_SKIPPED_FILE"
Changed_line_3 = "self.skipped_file = Souq.path_CONSTANTS.{}_SKIPPED_FILE"

line_4 = "Apparel_Shoes_and_Accessories urls collected in"
Changed_line_4 = "{} urls collected in"

line_5 = 'started Apparel_Shoes_and_Accessories urls collection'
Changed_line_5 = "started {} urls collection"

line_6 = 'from product_info_collectors.Baby_info_collector import start_info_collection'
Changed_line_6 = 'from product_info_collectors.{}_info_collector import start_info_collection'

for category in category_list:
    file = open(source_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1,Changed_line_1.format(category)))
        elif line_2 in line:
            lines.append(line.replace(line_2,Changed_line_2.format(category)))
        elif line_3 in line:
            lines.append(line.replace(line_3,Changed_line_3.format(category)))
        elif line_4 in line:
            lines.append(line.replace(line_4,Changed_line_4.format(category)))
        elif line_5 in line:
            lines.append(line.replace(line_5,Changed_line_5.format(category)))
        elif line_6 in line:
            lines.append(line.replace(line_6,Changed_line_6.format(category)))
        else:
            lines.append(line)
    write_file = open(file_path.format(destination_path,category),'w')
    for line in lines:
        write_file.write(line)


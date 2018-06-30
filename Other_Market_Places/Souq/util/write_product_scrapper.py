destination_path = '/home/eunimart-04/eunimart_dev_akhil/Souq/product_parsers'

source_path = '/home/eunimart-04/eunimart_dev_akhil/Souq/util/product_parser.py'

category_list = ['Apparel_Shoes_and_Accessories', 'Art_Crafts_and_Collectibles', 'Baby', 'Beauty', 'Bed_and_Bath',
                 'Books',
                 'Cameras', 'Coins_Stamps_and_Paper_money', 'Computers_IT_and_Networking', 'Electronics',
                 'Eyewear_and_Optics', 'Furniture', 'Gaming', 'Garden_and_Outdoor', 'Grocery_Food_and_Beverages',
                 'Health_and_Personal_Care', 'Home_Appliances', 'Home_Decor_and_Furniture', 'Jewelry_and_Accessories',
                 'Kitchen_and_Home_Supplies', 'Kitchen_Appliances', 'Mobile_Phones_Tablets_and_Accessories',
                 'Music_and_Movies', 'Office_Products_and_Supplies', 'Perfumes_and_Fragrances', 'Pet_Food_and_Supplies',
                 'Sports_and_Fitness', 'Tools_and_Home_Improvements', 'Toys', 'Vehicle_Parts_and_Accessories',
                 'Vouchers_and_Tickets', 'Wearable_Technology_Devices']


file_path = '{}/{}_product_parser.py'

line = 'from Souq.product_parsers.{}_product_parser import ProductDetails as {}_ProductDetails'

for category in category_list:
    file = open(source_path,'rt')
    lines = []
    for line in file:

            lines.append(line)
    write_file = open(file_path.format(destination_path,category),'w')
    for line in lines:
        write_file.write(line)

    #print line.format(category, category)
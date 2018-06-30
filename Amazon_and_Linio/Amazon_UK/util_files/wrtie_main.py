import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_UK/main.py'


category_list = ['Amazon_Pantry', 'Books_and_Audible', 'Business_Industry_and_Science', 'Car_and_Motorbike',
                 'Clothes_Shoes_and_Watches', 'Electronics_and_Computers', 'Handmade', 'Health_and_Beauty',
                 'Home_Garden_Pets_and_DIY', 'Movies_TV_Music_and_Games', 'Sports_and_Outdoors', 'Toys_Children_and_Baby']

# file = open(source_path,'w')
# count =1
# for category in category_list:
#     line_2 ='   if {} in category_list:\n'.format(category.upper())
#     line_3 =    '       thread_{} = Thread(target={}_info_collector.start_info_collection, args=({},))\n'.format(count, category.lower(),category.upper())
#     line_4 =    '       thread_{}.daemon = True\n'.format(count)
#     line_5 =    '       jobs.append(thread_{})\n\n'.format(count)
#     count = count+1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)
# count =1
# for category in category_list:
#     line_2 ='     if {} in category_list:\n'.format(category.upper())
#     line_3 =      '     thread_{} = Thread(target={}_url_collector.start_program, args=({},))\n'.format(count,category.lower(),category.upper())
#     line_4 =      '     thread_{}.daemon = True\n'.format(count)
#     line_5 =      '     jobs.append(thread_{})\n\n'.format(count)
#     count = count +1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)
#
# count =1
# for category in category_list:
#     line_2 ='   if {} in category_list:\n'.format(category.upper())
#     line_3 =    '       thread_{} = Thread(target={}_hierarchy.start_program)\n'.format(count,category.lower())
#     line_4 =    '       thread_{}.daemon = True\n\n'.format(count)
#     line_5 =    '       jobs.append(thread_{})\n\n'.format(count)
#     count = count + 1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)


print os.listdir('/home/eunimart/Documents/eunimart_dev_pavan/Amazon_UK/url_collectors')
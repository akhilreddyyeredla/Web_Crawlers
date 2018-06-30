import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Germany/main.py'


category_list = [ 'Kleidung_Schuhe_and_Uhren', 'Haushalt_Garten_Baumarkt',
                 'Auto_Motorrad_and_Gewerbe', 'Handmade_and_Amazon_Launchpad', 'Spielzeug_and_Baby',
                 'Sport_and_Freizeit', 'Filme_Serien_Musik_and_Games', 'Elektronik_and_Computer',
                 'Beauty_Drogerie_and_Lebensmittel']


line = 'from url_collectors import'
line_1 = '{}_hierarchy,'
line_2 = ''
for category in category_list:
    line_2 = line_2+line_1.format(category.lower())

print(line_2)
# file = open(source_path,'w')
# count =1
# for category in category_list:
#     line_2 ='   if {} in category_list:\n'.format(category.upper())
#     line_3 ='       thread_{} = Thread(target={}_info_collector.start_info_collection, args=({},))\n'.format(count, category.lower(),category.upper())
#     line_4 ='       thread_{}.daemon = True\n'.format(count)
#     line_5 ='       jobs.append(thread_{})\n\n'.format(count)
#     count = count+1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)
# count =1
# for category in category_list:
#     line_2 ='     if {} in category_list:\n'.format(category.upper())
#     line_3 ='         thread_{} = Thread(target={}_url_collector.start_program, args=({},))\n'.format(count,category.lower(),category.upper())
#     line_4 ='         thread_{}.daemon = True\n'.format(count)
#     line_5 ='         jobs.append(thread_{})\n\n'.format(count)
#     count = count +1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)
#
# count =1
# for category in category_list:
#     line_2 ='   if {} in category_list:\n'.format(category.upper())
#     line_3 ='       thread_{} = Thread(target={}_hierarchy.start_program)\n'.format(count,category.lower())
#     line_4 ='       thread_{}.daemon = True\n\n'.format(count)
#     line_5 ='       jobs.append(thread_{})\n\n'.format(count)
#     count = count + 1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)




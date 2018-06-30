import os
import fnmatch

import_file = open('ETSY_import_statments.txt', 'w')
import_file.close()
statment_set = set()


def get_all_files(root, pattern):
    """
    :param root: Root folder location
    :param pattern: pattern of file name which to be searched ex: '*_links.txt' is pattern
    :return: list of paths that matches with pattern
    """
    links_files = []
    # The below lines perform recurvise search of directories in the root folder and returns paths of file which
    # matches the pattern
    for root, dirs, files in os.walk(root):  # os.walk is python library to collect all directories
        for filename in fnmatch.filter(files, pattern):
            links_files.append(os.path.join(root, filename))
    return links_files


def collection_start(root):
    pattern_1 = "*.py"
    get_queue__file = get_all_files(root, pattern_1)
    for file in get_queue__file:
        with open(file, 'rt') as read_file:
            for line in read_file:
                if line.startswith('from') or line.startswith('import'):
                    statment_set.add(line)
                # import_file.write(line)
                # print line
            # break
    # break


collection_start('/usr/datacollector/Etsy')
for line in statment_set:
    print line
    import_file.write(line)

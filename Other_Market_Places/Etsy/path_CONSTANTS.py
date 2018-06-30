import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Etsy_common_imports import *
ACCESSORIES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER + '/accessories/products_page_links.txt'
ACCESSORIES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER + '/accessories/sub_sub_category_completed_accessories.txt '
ACCESSORIES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER + '/accessories/skipped_queue_accessories.txt'

ART_AND_COLLECTIBLES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER + '/art_and_collectibles/products_page_links.txt'
ART_AND_COLLECTIBLES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/art_and_collectibles/sub_sub_category_completed_art_and_collectibles.txt '
ART_AND_COLLECTIBLES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/art_and_collectibles/skipped_queue_art_and_collectibles.txt'

BAGS_AND_PURSES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/bags_and_purses/products_page_links.txt'
BAGS_AND_PURSES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/bags_and_purses/sub_sub_category_completed_bags_and_purses.txt '
BAGS_AND_PURSES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/bags_and_purses/skipped_queue_bags_and_purses.txt'

BATH_AND_BEAUTY_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/bath_and_beauty/products_page_links.txt'
BATH_AND_BEAUTY_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/bath_and_beauty/sub_sub_category_completed_bath_and_beauty.txt '
BATH_AND_BEAUTY_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/bath_and_beauty/skipped_queue_bath_and_beauty.txt'

BOOKS_MOVIES_AND_MUSIC_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/books_movies_and_music/products_page_links.txt'
BOOKS_MOVIES_AND_MUSIC_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/books_movies_and_music/sub_sub_category_completed_books_movies_and_music.txt '
BOOKS_MOVIES_AND_MUSIC_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/books_movies_and_music/skipped_queue_books_movies_and_music.txt'

CLOTHING_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/clothing/products_page_links.txt'
CLOTHING_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/clothing/sub_sub_category_completed_clothing.txt '
CLOTHING_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/clothing/skipped_queue_clothing.txt'

CRAFT_SUPPLIES_AND_TOOLS_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/craft_supplies_and_tools/products_page_links.txt'
CRAFT_SUPPLIES_AND_TOOLS_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/craft_supplies_and_tools/sub_sub_category_completed_craft_supplies_and_tools.txt '
CRAFT_SUPPLIES_AND_TOOLS_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/craft_supplies_and_tools/skipped_queue_craft_supplies_and_tools.txt'

ELECTRONICS_AND_ACCESSORIES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/electronics_and_accessories/products_page_links.txt'
ELECTRONICS_AND_ACCESSORIES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/electronics_and_accessories/sub_sub_category_completed_electronics_and_accessories.txt '
ELECTRONICS_AND_ACCESSORIES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/electronics_and_accessories/skipped_queue_electronics_and_accessories.txt'

HOME_AND_LIVING_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/home_and_living/products_page_links.txt'
HOME_AND_LIVING_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/home_and_living/sub_sub_category_completed_home_and_living.txt '
HOME_AND_LIVING_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/home_and_living/skipped_queue_home_and_living.txt'
JEWELRY_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/jewelry/products_page_links.txt'
JEWELRY_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/jewelry/sub_sub_category_completed_jewelry.txt '
JEWELRY_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/jewelry/skipped_queue_jewelry.txt'

PAPER_AND_PARTY_SUPPLIES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/paper_and_party_supplies/products_page_links.txt'
PAPER_AND_PARTY_SUPPLIES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/paper_and_party_supplies/sub_sub_category_completed_paper_and_party_supplies.txt '
PAPER_AND_PARTY_SUPPLIES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/paper_and_party_supplies/skipped_queue_paper_and_party_supplies.txt'

PET_SUPPLIES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/pet_supplies/products_page_links.txt'
PET_SUPPLIES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/pet_supplies/sub_sub_category_completed_pet_supplies.txt '
PET_SUPPLIES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/pet_supplies/skipped_queue_pet_supplies.txt'

SHOES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/shoes/products_page_links.txt'
SHOES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/shoes/sub_sub_category_completed_shoes.txt '
SHOES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/shoes/skipped_queue_shoes.txt'

TOYS_AND_GAMES_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/toys_and_games/products_page_links.txt'
TOYS_AND_GAMES_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/toys_and_games/sub_sub_category_completed_toys_and_games.txt '
TOYS_AND_GAMES_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/toys_and_games/skipped_queue_toys_and_games.txt'

WEDDINGS_QUEUE_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/weddings/products_page_links.txt'
WEDDINGS_COMPLETED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/weddings/sub_sub_category_completed_weddings.txt '
WEDDINGS_SKIPPED_PATH = ETSY_HIERARCHY_ROOT_FOLDER+'/weddings/skipped_queue_weddings.txt'



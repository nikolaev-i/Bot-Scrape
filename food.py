import random
food_places=['IKEA', 'БМС', 'Ядеш и Ревеш', 'Jambo24', 'Вин Завод', 'Готвеното в Мола на 3тия етаж', 'Китайско']


def get_food():

    number = random.randint(0,len(food_places)-1)
    return(food_places[number])




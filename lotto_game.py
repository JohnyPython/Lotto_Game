import random
import sys


all_kegs_in_bag = 90
num_in_card_player = 15
num_in_card_comp = 15
list_of_numbers = list(range(1, 91))
list_of_kegs = random.sample(list_of_numbers, 90)


# добавляет пробелы в список
def insert_space_func(name):
    for space in name:
        space.sort()
        space.insert(random.randint(0, 4), ' ')
        space.insert(random.randint(0, 5), ' ')
        space.insert(random.randint(0, 6), ' ')
        space.insert(random.randint(0, 7), ' ')


# шаблон карточки
def create_card(name, card_n):
    print('{:-^30}'.format(f'{name}'))
    for elem in card_n:
        for j in elem:
            print('{0:>2}'.format(j), end=' ')
        print()
    print('{:-^30}'.format('-'))


card_n1_set = random.sample(list_of_kegs, 15)
card_n2_set = random.sample(list_of_kegs, 15)
card_n1 = [card_n1_set[:5], card_n1_set[5:10], card_n1_set[10:]]
card_n2 = [card_n2_set[:5], card_n2_set[5:10], card_n2_set[10:]]
insert_space_func(card_n1)
insert_space_func(card_n2)


def card_name(name):
    if name == 'player':
        create_card('Your card', card_n1)
    if name == 'computer':
        create_card('Computer', card_n2)


def player_action():
    answer = input('Cross out the number? (y/n): ')
    if answer == 'y':
        if keg in card_n1_set:
            for k in card_n1:
                try:
                    k.insert(k.index(keg), 'x')
                    k.pop(k.index(keg))
                except ValueError:
                    continue
            return True
        else:
            print('This number is not in your card!!You Lose!!!')
            sys.exit()
    elif answer == 'n':
        if keg in card_n1_set:
            print('This number is in your card!!You Lose!!!')
            sys.exit()
        else:
            print('Ok,continue to play')


def computer_action():
    if keg in card_n2_set:
        for k in card_n2:
            try:
                k.insert(k.index(keg), 'x')
                k.pop(k.index(keg))
            except ValueError:
                continue
        return True


if __name__ == "__main__":
    for keg in list_of_kegs:
        all_kegs_in_bag -= 1
        print(f'New kegs:{keg} (Remains:{all_kegs_in_bag})')
        card_name('player')
        card_name('computer')
        if player_action():
            num_in_card_player -= 1
        if computer_action():
            num_in_card_comp -= 1
        if num_in_card_player == 0:
            print('You WIN!!!')
            sys.exit()
        if num_in_card_comp == 0:
            print('Computer WIN!!! You lose!!!')
            sys.exit()




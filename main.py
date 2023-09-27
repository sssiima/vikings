gr_to_kuns = 4
gr_to_silver = 68.22
gr_to_gold = 125.6367

emer = 5287500 / gr_to_gold
pearl = 1516129 / gr_to_gold
corn = 1.5
things = {'мясо': 3, 'зерно': 0.5, 'шкура': 5, 'кожа': 5, 'соль': 0.1, 'мед': 0.4, 'мех': 4, 'украшения': 42085, 'оружие': 10}
mass = {'мясо': 500, 'зерно': 0, 'шкура': 100, 'кожа': 100, 'соль': 70, 'мед': 0, 'мех': 100, 'украшения': 0, 'оружие': 132}
res = 0
weight = 11680 - mass['мясо'] - mass['шкура'] - mass['мех'] - mass['оружие'] - mass['соль']


def buy(thing, count, town, res, weight):
    if town == 'смоленск':
        res -= ((things[thing] + smol) * count)
    elif town == 'киев':
        res -= ((things[thing] + kiev) * count)
    elif town == 'старая русса':
        res -= ((things[thing] + star_rus) * count)
    elif town == 'великие луки':
        res -= ((things[thing] + vel_luk) * count)
    elif town == 'константинополь':
        res -= ((things[thing] + konst) * count)
    else:
        res -= (things[thing] * count)
    weight += count
    mass[thing] += count
    if weight <= 0:
        print('Места нет!!')
        return False
    print(f'Куплено {count} килограмм товара {thing} в городе {town.capitalize()}')
    return True


def sell(thing, count, town, res, weight):
    if town == 'смоленск':
        res += ((things[thing] + smol) * count)
    elif town == 'киев':
        res += ((things[thing] + kiev) * count)
    elif town == 'старая русса':
        res += ((things[thing] + star_rus) * count)
    elif town == 'великие луки':
        res += ((things[thing] + vel_luk) * count)
    elif town == 'константинополь':
        res += ((things[thing] + konst) * count)
    else:
        res += (things[thing] * count)
    weight -= count
    mass[thing] -= count
    if mass[thing] < 0:
        print('недостаточно этого товара для продажи')
    print(f'Продано {count} килограмм товара {thing} в городе {town.capitalize()}')
    return True


smol = 1
kiev = 3
star_rus = vel_luk = -0.5
konst = 4


def main():
    res = 0
    weight = 11680 - mass['мясо'] - mass['шкура'] - mass['мех'] - mass['оружие']
    while True:
        num = float(input("если покупаете, выберите 1, если продаете, то 2. иначе 0 \n"))
        line = input("укажите товар, вес в кг, город торговли \n").split()
        if num == 0:
            print(f'торговля окончена, выручка составила {res * gr_to_gold} кг золота')
        elif num == 1:
            buy(line[0], int(line[1]), line[2], res, weight)
        else:
            sell(line[0], int(line[1]), line[2], res, weight)


main()
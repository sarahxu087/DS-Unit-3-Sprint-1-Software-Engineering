from acme import Product
from random import randint, sample, uniform
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        prod = Product(name, price, weight, flammability)
        products.append(prod)
    return products


def inventory_report(products):
    print("ACME CORPORATION OFFICIAL UNVENTORY REPORT")
    total_products = len(products)
    total_price = 0
    total_weight = 0
    total_flamm = 0.0
    for x in products:
        total_price += x.price
        total_weight += x.weight
        total_flamm += x.flammability

    average_price = total_price/total_products
    average_weight = total_weight/total_products
    average_flamm = total_flamm/float(total_products)

    print(f'Average price: {average_price}')
    print(f'\nAverage weight:{average_weight}')
    print(f'\nAverage flammability: {average_flamm}')


if __name__ == '__main__':
    inventory_report(generate_products())

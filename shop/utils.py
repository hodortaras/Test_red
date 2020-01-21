import json
from .models import Product
from testshop.settings import BASE_DIR



def load_to_bd():
    path = BASE_DIR + '\parserproduct\products.json'
    print(path)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)
    for line in data:
        Product.objects.create(name=line['name'],
                              slug=line['slug'],
                              image=line['image'],
                              price=line['price'],
                              description=line['description'])

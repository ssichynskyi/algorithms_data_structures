"""Challenge: given a json string, which represents a list of goods
with every good is a dict with keys "name" and "price", sort it in
the following way:
- main sorting criterion is price, ASC
- if prices are equal, sort goods using their name in alphabetical order

"""

import json


def sort_by_price_ascending(json_string):
    """Solution using sorting function with key"""
    goods_list = json.loads(json_string)
    # first sort using secondary criterion
    goods_list.sort(key=lambda good: good['name'])
    # then sort using main criterion:
    goods_list.sort(key=lambda good: good['price'])
    return json.dumps(goods_list)


sorted_json_string = sort_by_price_ascending(
    """[{"name":"eggs","price":1},{"name":"bubblegum","price":1},{"name":"bubblegum","price":5.3},
{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]"""
)
print(sorted_json_string)


from GildedRose import *

if __name__ == '__main__':

    item = NormalItem("Elixir of the Mongoose", 5, 7)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.updateQuality()
        print(item)
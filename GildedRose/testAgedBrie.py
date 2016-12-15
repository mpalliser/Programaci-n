
from GildedRose import *

if __name__ == '__main__':
    #Caso valido
    item = NormalItem("Aged Brie", 2 , 0)
    #chequeo herencia __repr__
    print(item)
    #test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)
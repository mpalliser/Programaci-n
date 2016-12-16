
from GildedRose import *

if __name__ == '__main__':
    #Caso valido
    item = AgedBrie("Aged Brie", 2 , 45)
    #chequeo herencia __repr__
    print(item)
    #test update_quality
    for dia in range(1, 10):
        item.updateQuality()
        print(item)
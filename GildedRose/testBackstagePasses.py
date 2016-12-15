
from GildedRose import *

if __name__ == '__main__':
    #Caso valido
    item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 15 , 20)
    #chequeo herencia __repr__
    print(item)
    #test update_quality
    for dia in range(1, 20):
        item.updateQuality()
        print(item)
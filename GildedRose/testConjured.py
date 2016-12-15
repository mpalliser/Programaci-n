from GildedRose import *

if __name__ == '__main__':
    #Caso valido
    item = Conjured("Mana Cake", 3 , 30)
    #chequeo herencia __repr__
    print(item)
    #test update_quality
    for dia in range(1, 10):
        item.updateQuality()
        print(item)
from GildedRose import *

if __name__ == '__main__':

    item = Sulfuras("Sulfuras, mano de dios", 5, 80)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    
    for dia in range(1, 10):
        item.update_quality()
        item.setSell_in()
        print(item)
    
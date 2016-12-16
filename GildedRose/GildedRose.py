class Item:


    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Interfaz():


    def updateQuality(self):
        # Comportamiento a implementar en las subclases
        pass


class NormalItem(Item, Interfaz):
    # Herencia múltiple

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__
    # Override metodo update_quality de la interfaz
    def updateQuality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()


class Sulfuras(NormalItem):


    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        assert self.quality == 80, "La quality de %s tiene que ser 80" % self.__class__.__name__
        self.setSell_in()


class AgedBrie(NormalItem):


    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        self.setQuality(+1)
        self.setSell_in()


class Conjured(NormalItem):


    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.sell_in > 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()


class BackstagePasses(NormalItem):


    def updateQuality(self):
        if self.sell_in >10:
            self.quality +=1
        elif self.sell_in >5:
            self.quality +=2
        elif self.sell_in > 0:
            self.quality +=3
        else:
            self.quality = 0
        self.setSell_in()


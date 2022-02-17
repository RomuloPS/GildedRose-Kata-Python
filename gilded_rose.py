# -*- coding: utf-8 -*-

class GildedRose(object):

    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    CONJURED = "Conjured"

    def __init__(self, items):
        self.items = items

    def change_quality(self, item, value):
        if (item.quality + value) <= 50 and (item.quality + value)>= 0:
            item.quality = item.quality + value

    def change_sell_in(self,item,value):
        item.sell_in = item.sell_in + value

    def is_conjured(self,item):
        return item.name.startswith(self.CONJURED)

    def is_mutable(self, item):
        return item.name != self.SULFURAS
    

    def update_quality(self):
        for item in self.items:
            if self.is_mutable(item):
                self.update_item_quality(item)


    def update_item_quality(self, item):
        decrease = -2 if self.is_conjured(item) else -1

        if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASS:
            self.change_quality(item, decrease)
        else:
            self.change_quality(item,1)
            if item.name == self.BACKSTAGE_PASS:
                if item.sell_in < 11:
                    self.change_quality(item, 1)
                if item.sell_in < 6:
                    self.change_quality(item, 1)

        self.change_sell_in(item,-1)

        if item.sell_in < 0:
            if item.name != self.AGED_BRIE:
                if item.name != self.BACKSTAGE_PASS:
                    self.change_quality(item, decrease)
                else:
                    self.change_quality(item, -item.quality)
            else:
                # Is this wrong? It Looks wrong.
                # This line was on the original Kata, but I believe it was a bug.
                # self.change_quality(item,1)
                pass


    


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
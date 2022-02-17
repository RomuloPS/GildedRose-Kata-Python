# -*- coding: utf-8 -*-

class GildedRose(object):

    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


    def __init__(self, items):
        self.items = items


    def update_item_quality(self, item):
        if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASS:
            if item.name != self.SULFURAS:
                self.change_quality(item,-1)
        else:
            item.quality = item.quality + 1
            if item.name == self.BACKSTAGE_PASS:
                if item.sell_in < 11:
                    self.change_quality(item,1)
                if item.sell_in < 6:
                    self.change_quality(item,1)
        if item.name != self.SULFURAS:
            self.change_sell_in(item,-1)
        if item.sell_in < 0:
            if item.name != self.AGED_BRIE:
                if item.name != self.BACKSTAGE_PASS:
                    if item.name != self.SULFURAS:
                        self.change_quality(item,-1)
                else:
                    item.quality = item.quality - item.quality
            else:
                self.change_quality(item,1)
        
        pass


    def change_quality(self, item, value):
        if (item.quality + value) <= 50 and (item.quality + value)>= 0:
            item.quality = item.quality + value


    def change_sell_in(self,item,value):
        item.sell_in = item.sell_in + value


    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
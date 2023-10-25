class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update(self):
        if self.name == "Aged Brie":
            self.update_aged_brie()
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes()
        elif self.name == "Bananas":
            self.update_bananas()
        elif self.name == "Conjured":
            self.update_conjured_item() 
        elif self.name == "Sulfuras, Hand of Ragnaros":
            pass 
        else:
            self.update_normal_item()

    def update_aged_brie(self):
        self.sell_in -= 1
        self.quality = min(50, self.quality + 1)

    def update_backstage_passes(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality = min(50, self.quality + 3)
        elif self.sell_in <= 10:
            self.quality = min(50, self.quality + 2)
        else:
            self.quality = min(50, self.quality + 1)
            
    def update_bananas(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality = min(50, self.quality + 1)
        else:
            self.quality = min(50, self.quality - 1)

    def update_normal_item(self):
        self.sell_in -= 1
        if self.sell_in > 0:
            self.quality = max(0, self.quality - 1)
            
    def update_conjured_item(self):
        self.sell_in -= 1
        if self.sell_in > 0:
            self.quality = max(0, self.quality - 2)

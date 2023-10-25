import unittest
from gilded_rose import GildedRose, Item

class TestGildedRose(unittest.TestCase):
    
    def test_update_quality_normal_item(self):
        # Prueba para actualizacion de calidad de un Item normal
        # Su fecha de caducidad y calidad se reduce en 1 
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[0].quality, 19)

    def test_update_quality_aged_brie(self):
        # Prueba para actualizacion de calidad para el Item "Aged Brie"
        # Su fecha de caducidad se reduce en 1 y su calidad aumenta en 1 
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[0].quality, 21)

    def test_update_quality_backstage_passes(self):
        # Prueba para actualización de calidad para el Item "Backstage passes"
        # Su fecha de caducidad se reduce en 1 y su calidad aumenta en 
        # 1 si hay mas de 10 dias, en 2 si hay 10 o menos dias y en 3 si hay 5 o menos dias
        # cuando su fecha de caducidad llega a 0, su calidad es 0 tambien.
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 9, 20), 
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20), 
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 30),
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 5)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 8)
        self.assertEqual(gilded_rose.items[0].quality, 22)
        
        self.assertEqual(gilded_rose.items[1].sell_in, 4)
        self.assertEqual(gilded_rose.items[1].quality, 23)
        
        self.assertEqual(gilded_rose.items[2].sell_in, 14)
        self.assertEqual(gilded_rose.items[2].quality, 31)
        
        self.assertEqual(gilded_rose.items[3].sell_in, 0)
        self.assertEqual(gilded_rose.items[3].quality, 0)

    def test_update_quality_sulfuras(self):
        # Prueba para actualización de calidad para el item "Sulfuras"
        # Para este caso no se actualiza ningun valor
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 0)
        self.assertEqual(gilded_rose.items[0].quality, 80)
        
    def test_update_quality_conjured(self):
        # Prueba para actualización de calidad para el item "Conjured"
        # Su fecha de caducidad disminuye en 1 y su calidad disminuye en 2 
        items = [Item("Conjured", 12, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 11)
        self.assertEqual(gilded_rose.items[0].quality, 28)
        
        
    # ---------------------------- NUEVA FUNCIONALIDAD --------------------------- #
    def test_update_quality_bananas(self):
        # Prueba para actualización de calidad para el Item "Bananas"
        # Su fecha de caducidad y su calidad disminuye en 1
        # y si hay 5 o menos dias su calidad aumenta en 2
        # cuando su fecha de caducidad llega a 0, su calidad es 0 tambien.
        items = [Item("Bananas", 3, 10), Item("Bananas", 8, 10), Item("Bananas", 1, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 2)
        self.assertEqual(gilded_rose.items[0].quality, 11)
        
        self.assertEqual(gilded_rose.items[1].sell_in, 7) 
        self.assertEqual(gilded_rose.items[1].quality, 9) 
        
        self.assertEqual(gilded_rose.items[2].sell_in, 0) 
        self.assertEqual(gilded_rose.items[2].quality, 0) 

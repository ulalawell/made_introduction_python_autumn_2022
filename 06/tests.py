import unittest

from LRUCache import LRUCache

class TestString(unittest.TestCase):
    def test_01(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

    
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")


    def test_02(self):
        cache = LRUCache(5)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        cache.set("k5", "val5")

        self.assertEqual(cache.get("k5"), "val5")
        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

    def test_03(self):
        cache = LRUCache(1)

        cache.set("k1", "val1")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k2", "val2")
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")


    def test_04(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")

        cache.set("k3", "val3")
        cache.set("k1", "val1")
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"), "val3")

        print(cache.get("k1"))
        print(cache.get("k2"))
        print(cache.get("k3"))




if __name__ == "__main__":
    unittest.main()

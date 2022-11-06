import unittest
from io import StringIO
from unittest import mock
import sys


from LRUCache import LRUCache

@mock.patch("sys.stdout", new=StringIO())
class TestString(unittest.TestCase):
    def test_01(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        print(cache.get("k3"))
        print(cache.get("k2"))
        print(cache.get("k1"))

        cache.set("k3", "val3")

        print(cache.get("k3"))
        print(cache.get("k2"))
        print(cache.get("k1"))

        output = sys.stdout.getvalue().strip().splitlines()

        self.assertEqual(output[0], "None")
        self.assertEqual(output[1], "val2")
        self.assertEqual(output[2], "val1")
        self.assertEqual(output[3], "val3")
        self.assertEqual(output[4], "None")
        self.assertEqual(output[5], "val1")

    def test_02(self):
        cache = LRUCache(5)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        cache.set("k5", "val5")

        print(cache.get("k5"))
        print(cache.get("k4"))
        print(cache.get("k3"))
        print(cache.get("k2"))
        print(cache.get("k1"))


        output = sys.stdout.getvalue().strip().splitlines()

        self.assertEqual(output[6], "val5")
        self.assertEqual(output[7], "val4")
        self.assertEqual(output[8], "val3")
        self.assertEqual(output[9], "val2")
        self.assertEqual(output[10], "val1")

    def test_03(self):
        cache = LRUCache(1)

        cache.set("k1", "val1")
        print(cache.get("k1"))

        cache.set("k2", "val2")
        print(cache.get("k1"))
        print(cache.get("k2"))

        output = sys.stdout.getvalue().strip().splitlines()

        self.assertEqual(output[11], "val1")
        self.assertEqual(output[12], "None")
        self.assertEqual(output[13], "val2")


    def test_04(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        print(cache.get("k1"))
        print(cache.get("k2"))

        cache.set("k3", "val3")
        cache.set("k1", "val1")
        print(cache.get("k1"))
        print(cache.get("k2"))
        print(cache.get("k3"))


        output = sys.stdout.getvalue().strip().splitlines()

        self.assertEqual(output[14], "val1")
        self.assertEqual(output[15], "val2")
        self.assertEqual(output[16], "val1")
        self.assertEqual(output[17], "None")
        self.assertEqual(output[18], "val3")



if __name__ == "__main__":
    unittest.main()

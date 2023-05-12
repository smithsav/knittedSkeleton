from KnittedGuts import YarnCollection, validate_color, validate_material, validate_weight
import unittest
from unittest.mock import patch
from io import StringIO
from tkinter import Tk
from app import YarnCollection


class TestYarnCollection(unittest.TestCase):

    def test_addYarn(self):
        yarnCollection = YarnCollection()
        yarnCollection.addYarn("red", "1", "cotton")
        self.assertEqual(len(yarnCollection.collection), 1)
        self.assertEqual(yarnCollection.collection[("red", "1", "cotton")], 1)

        # Test adding yarn with existing properties
        yarnCollection.addYarn("red", "1", "cotton")
        self.assertEqual(len(yarnCollection.collection), 1)
        self.assertEqual(yarnCollection.collection[("red", "1", "cotton")], 2)

    def test_getYarnsByColor(self):
        yarnCollection = YarnCollection()
        yarnCollection.addYarn("red", "1", "cotton")
        yarnCollection.addYarn("blue", "2", "wool")
        yarnCollection.addYarn("red", "3", "synthetic")

        self.assertEqual(len(yarnCollection.getYarnsByColor("red")), 2)
        self.assertEqual(len(yarnCollection.getYarnsByColor("green")), 0)

    def test_getYarnsByWeight(self):
        yarnCollection = YarnCollection()
        yarnCollection.addYarn("red", "1", "cotton")
        yarnCollection.addYarn("blue", "2", "wool")
        yarnCollection.addYarn("red", "3", "synthetic")

        self.assertEqual(len(yarnCollection.getYarnsByWeight("1")), 1)
        self.assertEqual(len(yarnCollection.getYarnsByWeight("4")), 0)

    def test_getYarnsByMaterial(self):
        yarnCollection = YarnCollection()
        yarnCollection.addYarn("red", "1", "cotton")
        yarnCollection.addYarn("blue", "2", "wool")
        yarnCollection.addYarn("red", "3", "synthetic")

        self.assertEqual(len(yarnCollection.getYarnsByMaterial("cotton")), 1)
        self.assertEqual(len(yarnCollection.getYarnsByMaterial("silk")), 0)

    def test_validate_color(self):
        # Test with a valid color
        self.assertIsNone(validate_color("red"))

        # Test with an invalid color
        with self.assertRaises(ValueError):
            validate_color("orange")

    def test_validate_weight(self):
        # Test with a valid weight
        self.assertIsNone(validate_weight("1"))

        # Test with an invalid weight
        with self.assertRaises(ValueError):
            validate_weight("0")

    def test_validate_material(self):
        # Test with a valid material
        self.assertIsNone(validate_material("wool"))

        # Test with an invalid material
        with self.assertRaises(ValueError):
            validate_material("nylon")


if __name__ == '__main__':
    unittest.main()

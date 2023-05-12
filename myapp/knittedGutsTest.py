import unittest
from tkinter import Tk
from KnittedGuts import YarnCollectionApp


class TestYarnCollectionGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = YarnCollectionApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_addYarn(self):
        # Test valid input
        self.app.colorEntry.insert(0, "Red")
        self.app.weightEntry.insert(0, "4")
        self.app.materialEntry.insert(0, "Wool")
        self.app.addYarn()
        self.assertEqual(len(self.app.collection.collection), 1)

        # Test invalid color input
        self.app.colorEntry.delete(0, "end")
        self.app.colorEntry.insert(0, "Pinkish-Red")
        self.app.weightEntry.delete(0, "end")
        self.app.weightEntry.insert(0, "3")
        self.app.materialEntry.delete(0, "end")
        self.app.materialEntry.insert(0, "Cotton")
        with self.assertRaises(ValueError):
            self.app.addYarn()
        self.assertEqual(len(self.app.collection.collection), 1)

        # Test invalid weight input
        self.app.colorEntry.delete(0, "end")
        self.app.colorEntry.insert(0, "Pink")
        self.app.weightEntry.delete(0, "end")
        self.app.weightEntry.insert(0, "8")
        self.app.materialEntry.delete(0, "end")
        self.app.materialEntry.insert(0, "Synthetic")
        with self.assertRaises(ValueError):
            self.app.addYarn()
        self.assertEqual(len(self.app.collection.collection), 1)

        # Test invalid material input
        self.app.colorEntry.delete(0, "end")
        self.app.colorEntry.insert(0, "Green")
        self.app.weightEntry.delete(0, "end")
        self.app.weightEntry.insert(0, "5")
        self.app.materialEntry.delete(0, "end")
        self.app.materialEntry.insert(0, "Leather")
        with self.assertRaises(ValueError):
            self.app.addYarn()
        self.assertEqual(len(self.app.collection.collection), 1)

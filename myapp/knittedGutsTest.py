import unittest
import tkinter as tk
from unittest.mock import MagicMock

from myapp import MyApp, YarnCollection, YarnCollectionApp


class TestYarnCollectionApp(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.app = YarnCollectionApp(root)

    def test_addYarn(self):
        self.app.colorEntry.insert(0, "red")
        self.app.weightEntry.insert(0, "3")
        self.app.materialEntry.insert(0, "cotton")
        self.app.addYarn()
        self.assertEqual(self.app.colorListbox.get(0), "red")
        self.assertEqual(self.app.weightListbox.get(0), "3")
        self.assertEqual(self.app.materialListbox.get(0), "cotton")

    def test_showHelpWindow(self):
        self.app.showHelpWindow()
        help_window = self.app.children["!toplevel"][".!toplevel"]
        help_label = help_window.children["!label"]
        self.assertEqual(help_label.cget("text"), "You should enter the color of the yarn, "
                                                 "the weight of the yarn (1-superfine, 2-fine,"
                                                 "3-light, 4-medium, 5-bulky, 6-super bulky, 7-jumbo), and "
                                                 "the material of the yarn.")

    def test_showAboutWindow(self):
        self.app.showAboutWindow()
        about_window = self.app.children["!toplevel"][".!toplevel"]
        about_label = about_window.children["!label"]
        self.assertTrue(about_label.cget("text").startswith("Knitted was create for the yarn craft lovers"))

    def test_syncListBoxes(self):
        source = MagicMock()
        dest1 = MagicMock()
        dest2 = MagicMock()
        source.curselection.return_value = [0]
        self.app.syncListBoxes(source, dest1, dest2)
        dest1.selection_clear.assert_called_once_with(0, tk.END)
        dest1.selection_set.assert_called_once_with(0)
        dest2.selection_clear.assert_called_once_with(0, tk.END)
        dest2.selection_set.assert_called_once_with(0)

    def tearDown(self):
        self.app.master.destroy()


if __name__ == '__main__':
    unittest.main()

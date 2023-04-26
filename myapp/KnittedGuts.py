import tkinter as tk


class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("My App")

    def run(self):
        self.master.mainloop()


def addToIndex(key, index, yarn):
    index.setdefault(key, [])
    index[key].append(yarn)


class YarnCollection:
    def __init__(self):
        self.collection = {}
        self.colors = {}
        self.weights = {}
        self.materials = {}

    def addYarn(self, color, weight, material):
        yarn = (color, weight, material)
        self.collection.setdefault(yarn, 0)
        self.collection[yarn] += 1
        addToIndex(color, self.colors, yarn)
        addToIndex(weight, self.weights, yarn)
        addToIndex(material, self.materials, yarn)

    def getYarnsByColor(self, color):
        return self.colors.get(color, [])

    def getYarnsByWeight(self, weight):
        return self.weights.get(weight, [])

    def getYarnsByMaterial(self, material):
        return self.materials.get(material, [])


class YarnCollectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Yarn Collection")

        self.collection = YarnCollection()

        self.colorLabel = tk.Label(master, text="Color:")
        self.colorLabel.grid(row=0, column=0)

        self.colorEntry = tk.Entry(master)
        self.colorEntry.grid(row=0, column=1)

        self.weightLabel = tk.Label(master, text="Weight:")
        self.weightLabel.grid(row=1, column=0)

        self.weightEntry = tk.Entry(master)
        self.weightEntry.grid(row=1, column=1)

        self.materialLabel = tk.Label(master, text="Material:")
        self.materialLabel.grid(row=2, column=0)

        self.materialEntry = tk.Entry(master)
        self.materialEntry.grid(row=2, column=1)

        self.addButton = tk.Button(master, text="Add Yarn", command=self.addYarn)
        self.addButton.grid(row=3, column=0)

        self.colorListbox = tk.Listbox(master)
        self.colorListbox.grid(row=4, column=0)

        self.weightListbox = tk.Listbox(master)
        self.weightListbox.grid(row=4, column=1)

        self.materialListbox = tk.Listbox(master)
        self.materialListbox.grid(row=4, column=2)

        self.helpButton = tk.Button(master, text="Help", command=self.showHelp)
        self.helpButton.grid(row=5, column=0)

        self.aboutButton = tk.Button(master, text="About", command=self.showAbout)
        self.aboutButton.grid(row=5, column=1)

        self.exitButton = tk.Button(master, text="Exit", command=master.quit)
        self.exitButton.grid(row=5, column=2)

    def addYarn(self):
        color = self.colorEntry.get()
        weight = self.weightEntry.get()
        material = self.materialEntry.get()
        self.collection.addyarn(color, weight, material)
        self.updateListboxes()

    def updateListbox(self):
        self.colorListbox.delete(0, tk.END)
        self.weightListbox.delete(0, tk.END)
        self.materialListbox.delete(0, tk.END)

        for color in sorted(self.collection.colors):
            self.coloListbox.insert(tk.END, color)
            for yarn in self.collection.getYarnsByColor(color):
                self.colorListbox.insert(tk.END, f"  {yarn[1]}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    app.run()

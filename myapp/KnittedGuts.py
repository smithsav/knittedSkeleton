import tkinter as tk


class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("My App")

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    app.run()



class YarnCollection:
    def __init__(self):
        self.collection = {}
        self.colors = {}
        self.weights = {}
        self.materials = {}

    def add_yarn(self, color, weight, material):
        yarn = (color, weight, material)
        self.collection.setdefault(yarn, 0)
        self.collection[yarn] += 1
        self.add_to_index(color, self.colors, yarn)
        self.add_to_index(weight, self.weights, yarn)
        self.add_to_index(material, self.materials, yarn)

    def add_to_index(self, key, index, yarn):
        index.setdefault(key, [])
        index[key].append(yarn)

    def get_yarns_by_color(self, color):
        return self.colors.get(color, [])

    def get_yarns_by_weight(self, weight):
        return self.weights.get(weight, [])

    def get_yarns_by_material(self, material):
        return self.materials.get(material, [])


class YarnCollectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Yarn Collection")

        self.collection = YarnCollection()

        self.color_label = tk.Label(master, text="Color:")
        self.color_label.grid(row=0, column=0)

        self.color_entry = tk.Entry(master)
        self.color_entry.grid(row=0, column=1)

        self.weight_label = tk.Label(master, text="Weight:")
        self.weight_label.grid(row=1, column=0)

        self.weight_entry = tk.Entry(master)
        self.weight_entry.grid(row=1, column=1)

        self.material_label = tk.Label(master, text="Material:")
        self.material_label.grid(row=2, column=0)

        self.material_entry = tk.Entry(master)
        self.material_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Yarn", command=self.add_yarn)
        self.add_button.grid(row=3, column=0)

        self.color_listbox = tk.Listbox(master)
        self.color_listbox.grid(row=4, column=0)

        self.weight_listbox = tk.Listbox(master)
        self.weight_listbox.grid(row=4, column=1)

        self.material_listbox = tk.Listbox(master)
        self.material_listbox.grid(row=4, column=2)

        self.help_button = tk.Button(master, text="Help", command=self.show_help)
        self.help_button.grid(row=5, column=0)

        self.about_button = tk.Button(master, text="About", command=self.show_about)
        self.about_button.grid(row=5, column=1)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.grid(row=5, column=2)

    def add_yarn(self):
        color = self.color_entry.get()
        weight = self.weight_entry.get()
        material = self.material_entry.get()
        self.collection.add_yarn(color, weight, material)
        self.update_listboxes()

    def update_listboxes(self):
        self.color_listbox.delete(0, tk.END)
        self.weight_listbox.delete(0, tk.END)
        self.material_listbox.delete(0, tk.END)

        for color in sorted(self.collection.colors):
            self.color_listbox.insert(tk.END, color)
            for yarn in self.collection.get_yarns_by_color(color):
                self.color_listbox.insert(tk.END, f"  {yarn[1]}")

mainloop()

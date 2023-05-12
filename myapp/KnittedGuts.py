import tkinter as tk
from tkinter import messagebox


class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("Knitted")


def addToIndex(key, index, yarn):
    index.setdefault(key, [])
    index[key].append(yarn)


class YarnCollection:
    def __init__(self):
        """
        A collection of yarns, each represented as a tuple of (color, weight, material)
        """
        self.collection = {}
        self.colors = {}
        self.weights = {}
        self.materials = {}

    def addYarn(self, color, weight, material):
        """
        Add a new yarn to the collection.
        Args:
            color (str): The color of the yarn.
            weight (str): The weight of the yarn, from 1 (superfine) to 7 (jumbo).
            material (str): The material of the yarn.
        """
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


def syncListBoxes(source, dest1, dest2):
    # Synchronize the selected item in source with dest1 and dest2
    selected = source.curselection()
    if selected:
        index = selected[0]
        dest1.selection_clear(0, tk.END)
        dest1.selection_set(index)
        dest2.selection_clear(0, tk.END)
        dest2.selection_set(index)

# validate color
def validate_color(color):
    valid_colors = ['red', 'Red', 'blue', 'Blue', 'green', 'Green', 'yellow', 'Yellow', 'orange', 'Orange',
                    'blue', 'Blue', 'purple', 'Purple', 'pink', 'Pink', 'black', 'Black', 'white',
                    'White', 'gray', 'Gray', 'beige', 'Beige', 'colorful multi', 'Colorful Multi', 'neutral multi',
                    'Neutral Multi']  # list of valid colors
    if color not in valid_colors:
        raise ValueError(f"Invalid color: {color}. Please choose from {valid_colors}.")

# validate weight
def validate_weight(weight):
    valid_weights = ['1', '2', '3', '4', '5', '6', '7'] # list of valid weights
    if weight not in valid_weights:
        raise ValueError(f"Invalid weight: {weight}. Please choose from {valid_weights}.")

# validate material
def validate_material(material):
    valid_materials = ['cotton', 'Cotton', 'wool', 'Wool', 'synthetic', 'Synthetic'] #list of valid materials
    if material not in valid_materials:
        raise ValueError(f"Invalid material: {material}. Please choose from {valid_materials}.")


class YarnCollectionApp:
    def __init__(self, master):
        """
        Initialize the GUI.
        Args:
            master: The Tkinter root object.
        """
        self.master = master
        master.title("Knitted: Yarn Collection")

        self.collection = YarnCollection()

        # Add an image to the window
        image_path = r"C:\Users\smith\OneDrive\SDEV 140\Yarn_assortment.png"
        image = tk.PhotoImage(file=image_path)
        image = image.subsample(7, 7)  # Reduce the image size
        self.image_label = tk.Label(master, image=image)
        self.image_label.image = image
        self.image_label.grid(row=0, column=0, columnspan=3)

        # Create list boxes for displaying the collection of yarns
        self.colorListbox = tk.Listbox(master)
        self.colorListbox.grid(row=1, column=0)

        self.weightListbox = tk.Listbox(master)
        self.weightListbox.grid(row=1, column=1)

        self.materialListbox = tk.Listbox(master)
        self.materialListbox.grid(row=1, column=2)

        # Create labels and entry boxes for the color, weight, and material of a yarn
        self.colorLabel = tk.Label(master, text="Color:")
        self.colorLabel.grid(row=2, column=0)

        self.colorEntry = tk.Entry(master)
        self.colorEntry.grid(row=2, column=1)

        self.weightLabel = tk.Label(master, text="Weight:")
        self.weightLabel.grid(row=3, column=0)

        self.weightEntry = tk.Entry(master)
        self.weightEntry.grid(row=3, column=1)

        self.materialLabel = tk.Label(master, text="Material:")
        self.materialLabel.grid(row=4, column=0)

        self.materialEntry = tk.Entry(master)
        self.materialEntry.grid(row=4, column=1)

        # Create a button for adding a new yarn to the collection
        self.addButton = tk.Button(master, text="Add Yarn", command=self.addYarn)
        self.addButton.grid(row=5, column=0)

        # Create buttons for showing help and about windows, and for exiting the program
        self.helpButton = tk.Button(master, text="Help", command=self.showHelpWindow)
        self.helpButton.grid(row=6, column=0)

        self.aboutButton = tk.Button(master, text="About", command=self.showAboutWindow)
        self.aboutButton.grid(row=6, column=1)

        self.exitButton = tk.Button(master, text="Exit", command=master.quit)
        self.exitButton.grid(row=6, column=2)

    def updateListbox(self):
        """
        Update the list boxes with the current collection of yarns.
        """
        self.colorListbox.delete(0, tk.END)
        self.weightListbox.delete(0, tk.END)
        self.materialListbox.delete(0, tk.END)

        # Convert each yarn tuple to a dictionary for easy access to the color, weight, and material
        yarns = []
        for yarn in self.collection.collection:
            color, weight, material = yarn
            yarns.append({"color": color, "weight": weight, "material": material})

        # sort the yarns by color, weight, and material
        yarns.sort(key=lambda yarn: (yarn["color"], yarn["weight"], yarn["material"]))

        for yarn in yarns:
            self.colorListbox.insert(tk.END, yarn["color"])
            self.weightListbox.insert(tk.END, yarn["weight"])
            self.materialListbox.insert(tk.END, yarn["material"])

        # Bind the list boxes together, so they highlight the same item
        self.colorListbox.bind('<<ListboxSelect>>', lambda event: syncListBoxes(event, self.colorListbox,
                                                                                self.weightListbox))
        self.weightListbox.bind('<<ListboxSelect>>', lambda event: syncListBoxes(event, self.weightListbox,
                                                                                 self.colorListbox))
        self.materialListbox.bind('<<ListboxSelect>>', lambda event: syncListBoxes(event, self.materialListbox,
                                                                                   self.colorListbox))



    def addYarn(self):
        color = self.colorEntry.get()
        weight = self.weightEntry.get()
        material = self.materialEntry.get()
        try:
            validate_color(color)  # perform validation check
            validate_weight(weight)  # perform validation check
            validate_material(material)  # perform validation check
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        self.collection.addYarn(color, weight, material)
        self.updateListbox()

    def showHelpWindow(self):
        # create a new window
        help_window = tk.Toplevel(self.master)
        help_window.title("Help")

        # create a label with text and pack it
        help_label = tk.Label(help_window,
                              text="You should enter:\n\n- The color of the yarn (red, orange, yellow, green, blue, purple, pink, black, gray, white, beige, neutral multi, colorful multi)\n\n- The weight of the yarn (1-superfine, 2-fine, 3-light, 4-medium, 5-bulky, 6-super bulky, 7-jumbo)\n\n- The material of the yarn (cotton, wool, synthetic).",
                              wraplength=300)
        help_label.pack()

        # add an image to the window
        image_path = r"C:\Users\smith\OneDrive\SDEV 140\knittedYarnWeighting.png"
        image = tk.PhotoImage(file=image_path)
        image = image.subsample(3, 3)  # Reduce the image size
        image_label = tk.Label(help_window, image=image)
        image_label.image = image
        image_label.pack()

        # grab focus for the window
        help_window.grab_set()

    def showAboutWindow(self):
        aboutWindow = tk.Toplevel(self.master)
        aboutWindow.title("About")

        # creating a label
        aboutLabel = tk.Label(aboutWindow,
                              text="Knitted was create for the yarn craft lovers of the world. "
                                   "When shopping for yarn we tend to forget what's already in our "
                                   "collection and may end up buying too many of the same product. "
                                   "So I created Knitted to help resolve this problem.")
        aboutLabel.pack(padx=20, pady=20)

        okButton = tk.Button(aboutWindow, text="OK", command=aboutWindow.destroy)
        okButton.pack(pady=10)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = YarnCollectionApp(root)
    app.run()

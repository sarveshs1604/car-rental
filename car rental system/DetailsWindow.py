import tkinter as tk
from tkinter import ttk, messagebox
import csv
from PIL import Image, ImageTk


class DetailsWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Car Details")
        self.root.geometry("800x500")

        image = Image.open("background1.jpg")  # Open the image
        self.bg_image = ImageTk.PhotoImage(image)  # Convert to PhotoImage
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)
        # Title Label
        title_label = tk.Label(self.root, text="Search Car Details", font=("Arial", 20), bg="cyan")
        title_label.pack(fill=tk.X)

        # Dropdown for Car Details
        tk.Label(self.root, text="Select a Car:", font=("Arial", 14)).pack(pady=10)
        self.car_dropdown = ttk.Combobox(self.root, state="readonly", font=("Arial", 12))
        self.car_dropdown.pack(pady=10)
        self.load_car_data()

        # Back Button
        back_button = tk.Button(self.root, text="Back to Home", font=("Arial", 12), bg="lightblue", command=self.go_back)
        back_button.pack(pady=20)

        # Search Button
        search_button = tk.Button(self.root, text="Search", font=("Arial", 12), bg="lightgreen",
                                  command=self.display_details)
        search_button.pack(pady=10)

        # Details Display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=20)

        self.root.mainloop()

    def load_car_data(self):
        # Load car data from CSV
        try:
            with open("data.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                car_list = [f"{row[0]} {row[1]} ({row[2]})" for row in reader]
            self.car_dropdown["values"] = car_list
        except FileNotFoundError:
            messagebox.showerror("Error", "Car data file (data.csv) not found.")

    def display_details(self):
        car = self.car_dropdown.get()
        if not car:
            messagebox.showwarning("Warning", "Please select a car!")
            return

        # Simulating car detail retrieval
        details = f"Details for {car}\nMake: Toyota\nModel: Corolla\nYear: 2022\nPrice: $20,000"
        self.result_label.config(text=details)

    def go_back(self):
        self.root.destroy()
        from HomeWindow import HomeWindow  # Return to the Home Window
        root = tk.Tk()
        HomeWindow(root)
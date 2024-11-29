import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import date
import random
from PIL import Image, ImageTk


class BookingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Car Booking")
        self.root.geometry("800x500")

        image = Image.open("background1.jpg")  # Open the image
        self.bg_image = ImageTk.PhotoImage(image)  # Convert to PhotoImage
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Title Label
        title_label = tk.Label(self.root, text="Place Your Order", font=("Arial", 20), bg="cyan")
        title_label.pack(fill=tk.X)

        # Back Button
        back_button = tk.Button(self.root, text="Back to Home", font=("Arial", 12), bg="lightblue", command=self.go_back)
        back_button.pack(pady=20)

        # Dropdown for Car Selection
        tk.Label(self.root, text="Select a Car to Book:", font=("Arial", 14)).pack(pady=10)
        self.car_dropdown = ttk.Combobox(self.root, state="readonly", font=("Arial", 12))
        self.car_dropdown.pack(pady=10)
        self.load_car_data()

        # Book Button
        book_button = tk.Button(self.root, text="Place Order", font=("Arial", 12), bg="yellow",
                                command=self.book_car)
        book_button.pack(pady=20)

        # Confirmation Display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), fg="green")
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

    def book_car(self):
        car = self.car_dropdown.get()
        if not car:
            messagebox.showwarning("Warning", "Please select a car!")
            return

        # Simulating booking process
        booking_id = random.randint(1000, 9999)
        today = date.today()
        confirmation = (f"Booking Confirmed!\n\nBooking ID: {booking_id}\n"
                        f"Car: {car}\nDate: {today.strftime('%Y-%m-%d')}\n"
                        "Please visit our showroom to complete the process.")
        self.result_label.config(text=confirmation)

    def go_back(self):
        self.root.destroy()
        from HomeWindow import HomeWindow  # Return to the Home Window
        root = tk.Tk()
        HomeWindow(root)
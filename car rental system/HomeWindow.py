import tkinter as tk
from PIL import Image, ImageTk

class HomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental System")
        self.root.geometry("800x500")

        image = Image.open("background.jpg")  # Open the image
        self.bg_image = ImageTk.PhotoImage(image)  # Convert to PhotoImage
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)
        # Title Label
        title_label = tk.Label(self.root, text="Welcome to AutoShack", font=("Arial", 20), bg="cyan")
        title_label.pack(fill=tk.X)

        # Buttons
        self.details_button = tk.Button(self.root, text="Search Car Details", font=("Arial", 14), bg="lightblue",
                                         command=self.open_details)
        self.details_button.place(x=250, y=150, width=300, height=50)

        self.book_button = tk.Button(self.root, text="Place Order", font=("Arial", 14), bg="lightblue",
                                      command=self.open_booking)
        self.book_button.place(x=250, y=250, width=300, height=50)

    def open_details(self):
        self.root.destroy()
        from DetailsWindow import DetailsWindow
        DetailsWindow()

    def open_booking(self):
        self.root.destroy()
        from BookingWindow import BookingWindow
        BookingWindow()

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeWindow(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow

class BusTicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Booking System")
        self.root.geometry("700x600")  # Reduced height (600 instead of 700)
        self.users = {}  # In-memory storage for registered users
        self.bookings = []  # List to store booking information
        self.routes = {
            "Chennai to Pondy": {"price": 500, "timing": "08:00 AM"},
            "Pondy to Chennai": {"price": 500, "timing": "09:00 AM"},
            "Chennai to Bangalore": {"price": 1000, "timing": "10:00 AM"},
            "Bangalore to Chennai": {"price": 1000, "timing": "11:00 AM"},
            "Chennai to Nellore": {"price": 2000, "timing": "12:00 PM"},
            "Nellore to Chennai": {"price": 2000, "timing": "01:00 PM"},
            "Chennai to Ooty": {"price": 1500, "timing": "02:00 PM"},
            "Ooty to Chennai": {"price": 1500, "timing": "03:00 PM"},
            "Chennai to Kerala": {"price": 3000, "timing": "04:00 PM"},
            "Kerala to Chennai": {"price": 3000, "timing": "05:00 PM"},
            "Namakkal to Chennai": {"price": 1200, "timing": "06:00 PM"},
            "Chennai to Namakkal": {"price": 1200, "timing": "07:00 PM"}
        }

        # Start with the login page
        self.login_page()

    def set_background(self):
        """Set the background image for the window."""
        img = Image.open("C:/Users/Lenovo/Desktop/group-buses-driving-along-road-sunset.jpg")  # Adjust path if necessary
        img = img.resize((700, 600), Image.Resampling.LANCZOS)  # Resize the image to fit the window size (700x600)

        # Convert the image to a Tkinter-compatible photo image
        self.bg_image = ImageTk.PhotoImage(img)

        # Create a Canvas widget and add the background image to it
        self.canvas = tk.Canvas(self.root, width=700, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

    def login_page(self):
        """Login or Register Page"""
        self.clear_window()

        # Call the set_background function to display the background image
        self.set_background()

        self.title_label = tk.Label(self.root, text="Bus Ticket Booking System", font=("Helvetica", 16), bg="#FFFFFF")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.login_label = tk.Label(self.root, text="Login", font=("Helvetica", 14), bg="#FFFFFF")
        self.login_label.place(relx=0.5, rely=0.2, anchor="center")

        self.username_label = tk.Label(self.root, text="Username:", bg="#FFFFFF")
        self.username_label.place(relx=0.5, rely=0.3, anchor="center")
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.place(relx=0.5, rely=0.35, anchor="center")

        self.password_label = tk.Label(self.root, text="Password:", bg="#FFFFFF")
        self.password_label.place(relx=0.5, rely=0.4, anchor="center")
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.login_button = tk.Button(self.root, text="Login", width=20, command=self.login)
        self.login_button.place(relx=0.5, rely=0.55, anchor="center")

        self.register_button = tk.Button(self.root, text="Create Account", width=20, command=self.register_page)
        self.register_button.place(relx=0.5, rely=0.6, anchor="center")

    def register_page(self):
        """Registration Page"""
        self.clear_window()

        # Call the set_background function to display the background image
        self.set_background()

        self.title_label = tk.Label(self.root, text="Register", font=("Helvetica", 16), bg="#FFFFFF")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.username_label = tk.Label(self.root, text="Username:", bg="#FFFFFF")
        self.username_label.place(relx=0.5, rely=0.2, anchor="center")
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.place(relx=0.5, rely=0.25, anchor="center")

        self.password_label = tk.Label(self.root, text="Password:", bg="#FFFFFF")
        self.password_label.place(relx=0.5, rely=0.3, anchor="center")
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.place(relx=0.5, rely=0.35, anchor="center")

        self.register_button = tk.Button(self.root, text="Create Account", width=20, command=self.create_account)
        self.register_button.place(relx=0.5, rely=0.45, anchor="center")

        self.back_button = tk.Button(self.root, text="Back to Login", width=20, command=self.login_page)
        self.back_button.place(relx=0.5, rely=0.5, anchor="center")

    def create_account(self):
        """Create a new account"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            if username in self.users:
                messagebox.showerror("Error", "Username already exists!")
            else:
                self.users[username] = password
                messagebox.showinfo("Success", "Account created successfully! You can now log in.")
                self.login_page()
        else:
            messagebox.showerror("Error", "Please fill in both fields.")

    def login(self):
        """Login validation"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            self.route_selection_page(username)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def route_selection_page(self, username):
        """Route and Ticket Selection Page"""
        self.clear_window()

        self.username = username

        # Call the set_background function to display the background image
        self.set_background()

        self.title_label = tk.Label(self.root, text="Select Your Route", font=("Helvetica", 16), bg="#FFFFFF")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.from_label = tk.Label(self.root, text="From:", bg="#FFFFFF")
        self.from_label.place(relx=0.3, rely=0.2, anchor="center")
        self.from_var = tk.StringVar(self.root)
        self.from_var.set("Chennai")
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *["Chennai", "Pondy", "Bangalore", "Nellore", "Ooty", "Kerala", "Namakkal"])
        self.from_menu.place(relx=0.3, rely=0.25, anchor="center")

        self.to_label = tk.Label(self.root, text="To:", bg="#FFFFFF")
        self.to_label.place(relx=0.7, rely=0.2, anchor="center")
        self.to_var = tk.StringVar(self.root)
        self.to_var.set("Pondy")
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *["Chennai", "Pondy", "Bangalore", "Nellore", "Ooty", "Kerala", "Namakkal"])
        self.to_menu.place(relx=0.7, rely=0.25, anchor="center")

        self.tickets_label = tk.Label(self.root, text="Number of Tickets:", bg="#FFFFFF")
        self.tickets_label.place(relx=0.5, rely=0.4, anchor="center")
        self.tickets_entry = tk.Entry(self.root, width=30)
        self.tickets_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.calculate_button = tk.Button(self.root, text="Calculate Price", width=20, command=self.calculate_price)
        self.calculate_button.place(relx=0.5, rely=0.55, anchor="center")

        self.book_button = tk.Button(self.root, text="Book Ticket", width=20, state=tk.DISABLED, command=self.book_ticket)
        self.book_button.place(relx=0.5, rely=0.6, anchor="center")

        self.view_button = tk.Button(self.root, text="View My Bookings", width=20, command=self.view_booked_tickets)
        self.view_button.place(relx=0.5, rely=0.65, anchor="center")

    def calculate_price(self):
        """Calculate total price based on route and number of tickets"""
        from_city = self.from_var.get()
        to_city = self.to_var.get()
        route = f"{from_city} to {to_city}"
        
        if route not in self.routes:
            messagebox.showerror("Error", "Invalid route selected.")
            return
        
        price_per_ticket = self.routes[route]["price"]
        departure_time = self.routes[route]["timing"]
        try:
            num_tickets = int(self.tickets_entry.get())
            total_price = price_per_ticket * num_tickets
            self.total_price = total_price
            self.num_tickets = num_tickets
            self.book_button.config(state=tk.NORMAL)  # Enable Book Ticket button
            messagebox.showinfo("Price Calculated", f"Total Price: ₹{total_price}\nDeparture Time: {departure_time}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of tickets.")

    def book_ticket(self):
        """Book the ticket"""
        if not hasattr(self, 'total_price'):
            messagebox.showerror("Error", "Please calculate the price first.")
            return

        route = f"{self.from_var.get()} to {self.to_var.get()}"
        booking = {
            "username": self.username,
            "route": route,
            "tickets": self.num_tickets,
            "total_price": self.total_price
        }
        self.bookings.append(booking)
        messagebox.showinfo("Booking Confirmed", f"Your ticket has been booked!\nTotal Price: ₹{self.total_price}\nDeparture Time: {self.routes[route]['timing']}")

    def view_booked_tickets(self):
        """View previous bookings"""
        self.clear_window()

        self.set_background()

        self.title_label = tk.Label(self.root, text="My Bookings", font=("Helvetica", 16), bg="#FFFFFF")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        if not self.bookings:
            self.no_bookings_label = tk.Label(self.root, text="No bookings found.", bg="#FFFFFF")
            self.no_bookings_label.place(relx=0.5, rely=0.2, anchor="center")
        else:
            y_position = 0.3
            for booking in self.bookings:
                booking_info = f"Route: {booking['route']} | Tickets: {booking['tickets']} | Total: ₹{booking['total_price']}"
                booking_label = tk.Label(self.root, text=booking_info, bg="#FFFFFF")
                booking_label.place(relx=0.5, rely=y_position, anchor="center")
                y_position += 0.1

        self.back_button = tk.Button(self.root, text="Back", width=20, command=self.route_selection_page)
        self.back_button.place(relx=0.5, rely=y_position, anchor="center")

    def clear_window(self):
        """Clear the current window content"""
        for widget in self.root.winfo_children():
            widget.destroy()


# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BusTicketBookingSystem(root)
    root.mainloop()

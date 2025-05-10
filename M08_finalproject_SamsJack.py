# module 8 - final - order manager GUI application
# author: jrs
# created: 2025-05-08
# this program is a sample order mangment system i had to scale back a bit
# NO CODING ASSISTANCE was used in this program

# import tkinter as tk
# from tkinter import ttk, messagebox
# import os  
# class OrderManagementApp:
#    def __init__(self, root):
#        self.root = root
#        self.root.title("Order Management")
#        self.root.geometry("600x400")
#        self.create_main_window()
#    def create_main_window(self):
#        main_frame = ttk.Frame(self.root, padding="20")
#        main_frame.pack(fill=tk.BOTH, expand=True)
#        try:
#            image_path = os.path.join(os.path.dirname(__file__), "logo.png")
#            image = Image.open(image_path)  
#            image = image.resize((100, 100))  
#            photo = ImageTk.PhotoImage(image)
#            logo_label = ttk.Label(main_frame, image=photo, text="Company Logo", compound=tk.TOP) # Adding text description
#            logo_label.image = photo
#            logo_label.pack(pady=10)
#        except Exception as e:
#            print(f"Error loading image: {e}")
#            logo_label = ttk.Label(main_frame, text="[Company Logo - Image not available]")
#            logo_label.pack(pady=10)
#        welcome_label = ttk.Label(main_frame, te# module 8 - final - order manager GUI application
# author: jrs
# created: 2025-05-08
# this program is a sample order mangment system i had to scale back a bit
# NO CODING ASSISTANCE was used in this program

# import tkinter as tk
# from tkinter import ttk, messagebox
# import os  
# class OrderManagementApp:
#    def __init__(self, root):
#        self.root = root
#        self.root.title("Order Management")
#        self.root.geometry("600x400")
#        self.create_main_window()
#    def create_main_window(self):
#        main_frame = ttk.Frame(self.root, padding="20")
#        main_frame.pack(fill=tk.BOTH, expand=True)
#        try:
#            image_path = os.path.join(os.path.dirname(__file__), "logo.png")
#            image = Image.open(image_path)  xt="Welcome to Order Management!", font=("Arial", 16))
#        welcome_label.pack(pady=10)
#        order_button = ttk.Button(main_frame, text="Create New Order", command=self.open_order_window)
#        order_button.pack(pady=5)
#        view_order_button = ttk.Button(main_frame, text="View Orders", command=self.open_view_orders_window)
#        view_order_button.pack(pady=5)
#        exit_button = ttk.Button(main_frame, text="Exit", command=self.exit_app)
#        exit_button.pack(pady=5)
#    def open_order_window(self):
#        order_window = tk.Toplevel(self.root)
#        order_window.title("Create New Order")
#        OrderWindow(order_window, self)  
#    def open_view_orders_window(self):
#        view_window = tk.Toplevel(self.root)
#        view_window.title("View Orders")
#        ViewOrdersWindow(view_window)
#    def exit_app(self):
#        if messagebox.askokcancel("Quit", "Do you really want to exit?"):
#            self.root.destroy()
# class OrderWindow:
#    def __init__(self, master, main_app):  
#        self.master = master
#        self.main_app = main_app 
#        self.master.geometry("400x300")
#        self.create_order_form()
#    def create_order_form(self):
#        frame = ttk.Frame(self.master, padding="20")
#        frame.pack(fill=tk.BOTH, expand=True)
#        name_label = ttk.Label(frame, text="Customer Name:")
#        name_label.grid(row=0, column=0, sticky=tk.W, pady=5)
#        item_label = ttk.Label(frame, text="Item:")
#        item_label.grid(row=1, column=0, sticky=tk.W, pady=5)
#        quantity_label = ttk.Label(frame, text="Quantity:")
#        quantity_label.grid(row=2, column=0, sticky=tk.W, pady=5)
#        self.name_entry = ttk.Entry(frame)
#        self.name_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
#        self.item_entry = ttk.Entry(frame)
#        self.item_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
#        self.quantity_entry = ttk.Entry(frame)
#        self.quantity_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
#        submit_button = ttk.Button(frame, text="Submit Order", command=self.submit_order)
#        submit_button.grid(row=3, column=0, columnspan=2, pady=10)
#        back_button = ttk.Button(frame, text="Back to Main", command=self.back_to_main)
#        back_button.grid(row=4, column=0, columnspan=2, pady=5)
#    def submit_order(self):
#          name = self.name_entry.get()
#          item = self.item_entry.get()
#          quantity_str = self.quantity_entry.get()
#          if not name or not item or not quantity_str:
#             messagebox.showerror("Error", "All fields are required.")
#             return
#          try:
#            quantity = int(quantity_str)
#           if quantity <= 0:
#                messagebox.showerror("Error", "Quantity must be a positive number")
#                return
#          except ValueError:
#             messagebox.showerror("Error", "Quantity must be a valid number.")
#             return
#          messagebox.showinfo("Success", f"Order submitted: {name}, {item}, Quantity: {quantity}")
#          self.master.destroy()  
#    def back_to_main(self):
#          self.master.destroy()  
# class ViewOrdersWindow:
#    def __init__(self, master):
#        self.master = master
#        self.master.geometry("400x300")
#        self.create_view_orders_ui()
#    def create_view_orders_ui(self):
#        frame = ttk.Frame(self.master, padding="20")
#        frame.pack(fill=tk.BOTH, expand=True)
#        order_label = ttk.Label(frame, text="Order list (example):\n- Order 1\n- Order 2\n- Order 3")
#        order_label.pack(pady=10)
#        back_button = ttk.Button(frame, text="Back to Main", command=self.back_to_main)
#        back_button.pack(pady=10)
#    def back_to_main(self):
#           self.master.destroy()
# if __name__ == "__main__":
#    root = tk.Tk()
#    app = OrderManagementApp(root)
#    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import os  # Import os module for path handling

class OrderManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Order Management")
        self.root.geometry("600x400")

        self.create_main_window()

    def create_main_window(self):
        # Creates and configures the main application window
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Logo Image with alternate text
        try:
            # Construct a path to images within the same directory
            image_path = os.path.join(os.path.dirname(__file__), "logo.png")
            image = Image.open(image_path)  # Replace "logo.png" with a company image path
            image = image.resize((100, 100))  # Resize image
            photo = ImageTk.PhotoImage(image)
            logo_label = ttk.Label(main_frame, image=photo, text="Company Logo", compound=tk.TOP) # Adding text description
            logo_label.image = photo
            logo_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")
            logo_label = ttk.Label(main_frame, text="[Company Logo - Image not available]")
            logo_label.pack(pady=10)


        welcome_label = ttk.Label(main_frame, text="Welcome to Order Management!", font=("Arial", 16))
        welcome_label.pack(pady=10)

        # Buttons
        order_button = ttk.Button(main_frame, text="Create New Order", command=self.open_order_window)
        order_button.pack(pady=5)

        view_order_button = ttk.Button(main_frame, text="View Orders", command=self.open_view_orders_window)
        view_order_button.pack(pady=5)


        exit_button = ttk.Button(main_frame, text="Exit", command=self.exit_app)
        exit_button.pack(pady=5)

    def open_order_window(self):
        # Opens the window for creating new orders
        order_window = tk.Toplevel(self.root)
        order_window.title("Create New Order")
        OrderWindow(order_window, self)  

    def open_view_orders_window(self):
        # Opens window for viewing existing orders
        view_window = tk.Toplevel(self.root)
        view_window.title("View Orders")
        ViewOrdersWindow(view_window)

    def exit_app(self):
        # Exits the entire application with a confirmation message
        if messagebox.askokcancel("Quit", "Do you really want to exit?"):
            self.root.destroy()

class OrderWindow:
    def __init__(self, master, main_app):  
        self.master = master
        self.main_app = main_app 
        self.master.geometry("400x300")
        self.create_order_form()

    def create_order_form(self):
        # Creates and configures the new order form
        frame = ttk.Frame(self.master, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Labels
        name_label = ttk.Label(frame, text="Customer Name:")
        name_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        item_label = ttk.Label(frame, text="Item:")
        item_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        quantity_label = ttk.Label(frame, text="Quantity:")
        quantity_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        # Entry boxes
        self.name_entry = ttk.Entry(frame)
        self.name_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        self.item_entry = ttk.Entry(frame)
        self.item_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        self.quantity_entry = ttk.Entry(frame)
        self.quantity_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Submit Button
        submit_button = ttk.Button(frame, text="Submit Order", command=self.submit_order)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Back Button
        back_button = ttk.Button(frame, text="Back to Main", command=self.back_to_main)
        back_button.grid(row=4, column=0, columnspan=2, pady=5)



    def submit_order(self):
          # Handles order submission with validation
          name = self.name_entry.get()
          item = self.item_entry.get()
          quantity_str = self.quantity_entry.get()


          if not name or not item or not quantity_str:
             messagebox.showerror("Error", "All fields are required.")
             return


          try:
            quantity = int(quantity_str)
            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be a positive number")
                return
          except ValueError:
             messagebox.showerror("Error", "Quantity must be a valid number.")
             return

          messagebox.showinfo("Success", f"Order submitted: {name}, {item}, Quantity: {quantity}")
          self.master.destroy()  # Close order window after submission
    def back_to_main(self):
          # Handles moving back to main window
          self.master.destroy()  # Close order window

class ViewOrdersWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.create_view_orders_ui()

    def create_view_orders_ui(self):
        # Sets up the UI for viewing orders
        frame = ttk.Frame(self.master, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Example orders display replace with actual order display
        order_label = ttk.Label(frame, text="Order list (example):\n- Order 1\n- Order 2\n- Order 3")
        order_label.pack(pady=10)

        # Back button to main window
        back_button = ttk.Button(frame, text="Back to Main", command=self.back_to_main)
        back_button.pack(pady=10)

    def back_to_main(self):
           # Handles returning to the main window
           self.master.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = OrderManagementApp(root)
    root.mainloop()

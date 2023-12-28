import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dataBase import *
from tkinter import messagebox
import customtkinter
from tkinter import PhotoImage

# connection to DB
conn, cur = initialize_connection()

# colores
main_color = "#F6F6F2"
green_color = "#C2EDCE"
blue_light_color = "#BADFE7"
blue_mid_color = "#6FB3B8"
blue_str_color = "#388087"
red_color = "#ED2B2A"


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Gorceria")
        self.root.geometry("300x400")

        p1 = PhotoImage(file='Imegies/GroceriaLogo1.png')
        # Setting icon of master window
        self.root.iconphoto(False, p1)

        # font definition
        main_font = customtkinter.CTkFont(family="Helvetica", size=16)

        root.configure(bg=main_color)

        # Load the image file
        self.logo_image = Image.open("Imegies/GroceriaLogo.png")
        self.logo_image.resize((200, 200))
        self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)
        # Create a label widget
        self.logo_label = tk.Label(self.root, image=self.logo_image_tk, width=150, height=150)
        self.logo_label.grid(row=0, columnspan=2, pady=10)
        self.login_label = tk.Label(self.root, text="Login", font=("Helvetica", 16)
                                    , bg=main_color, fg=blue_str_color)
        self.login_label.grid(row=1, columnspan=2, pady=10)

        # label
        self.phone_number_label = tk.Label(self.root, text="Phone number:"
                                           , bg=main_color, fg=blue_str_color)
        self.phone_number_label.grid(row=2, column=0, padx=5, pady=5)
        # entry
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.grid(row=2, column=1, padx=5, pady=5)
        # label
        self.password_label = tk.Label(self.root, text="Password:"
                                       , bg=main_color, fg=blue_str_color)
        self.password_label.grid(row=3, column=0, padx=5, pady=5)

        # entry
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        # button
        self.login_button = customtkinter.CTkButton(
            master=self.root,
            command=self.login,
            text="Login",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=120,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)

        self.login_button.grid(row=5, columnspan=2, pady=10)
        # button
        self.register_button = customtkinter.CTkButton(
            master=self.root,
            command=self.show_registration_window,
            text="Sign up",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=120,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        self.register_button.grid(row=6, columnspan=2, pady=5)

    def login(self):
        # get phone_number and password that user enter
        phone_number = self.phone_number_entry.get()
        password = self.password_entry.get()
        global customer_id
        customer_id, order_id, first_name, last_name = login(cur, conn, phone_number, password)
        if customer_id:
            ProductWindow(self.root, first_name, last_name)

    #
    def show_registration_window(self):
        self.root.withdraw()
        registration_window = tk.Toplevel()
        registration_window.title("Registration")
        RegistrationWindow(registration_window, self)


class RegistrationWindow:
    def __init__(self, registration_window, main_window):
        self.registration_window = registration_window
        self.main_window = main_window

        p1 = PhotoImage(file='Imegies/GroceriaLogo1.png')
        # Setting icon of master window
        self.registration_window.iconphoto(False, p1)

        main_font = customtkinter.CTkFont(family="Helvetica", size=12)
        registration_window.configure(bg=main_color)

        # Create a label for the customer ID field
        self.customer_id_label = tk.Label(self.registration_window, text="Customer ID:"
                                          , bg=main_color, fg=blue_str_color)
        self.customer_id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.customer_id_entry = tk.Entry(self.registration_window)
        self.customer_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.first_name_label = tk.Label(self.registration_window, text="First Name:"
                                         , bg=main_color, fg=blue_str_color)
        self.first_name_label.grid(row=1, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(self.registration_window)
        self.first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.last_name_label = tk.Label(self.registration_window, text="Last Name:"
                                        , bg=main_color, fg=blue_str_color)
        self.last_name_label.grid(row=2, column=0, padx=5, pady=5)
        self.last_name_entry = tk.Entry(self.registration_window)
        self.last_name_entry.grid(row=2, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.registration_window, text="Email:"
                                    , bg=main_color, fg=blue_str_color)
        self.email_label.grid(row=3, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.registration_window)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.registration_window, text="Password:"
                                       , bg=main_color, fg=blue_str_color)
        self.password_label.grid(row=4, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.registration_window, show="*")
        self.password_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create a label for the street field
        self.street_label = tk.Label(self.registration_window, text="Street:"
                                     , bg=main_color, fg=blue_str_color)
        self.street_label.grid(row=5, column=0, padx=5, pady=5)

        # Create an entry widget for the street
        self.street_entry = tk.Entry(self.registration_window)
        self.street_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        # Create a label for the building number field
        self.building_label = tk.Label(self.registration_window, text="Building Number:"
                                       , bg=main_color, fg=blue_str_color)
        self.building_label.grid(row=6, column=0, padx=5, pady=5)

        # Create an entry widget for the building number
        self.building_entry = tk.Entry(self.registration_window)
        self.building_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        # Create a label for the city field
        self.city_label = tk.Label(self.registration_window, text="City:"
                                   , bg=main_color, fg=blue_str_color)
        self.city_label.grid(row=7, column=0, padx=5, pady=5)

        # Create an entry widget for the city
        self.city_entry = tk.Entry(self.registration_window)
        self.city_entry.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        self.phone_label = tk.Label(self.registration_window, text="Phone Number:"
                                    , bg=main_color, fg=blue_str_color)
        self.phone_label.grid(row=8, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.registration_window)
        self.phone_entry.grid(row=8, column=1, padx=5, pady=5)

        # Create a label for the gender field
        self.gender_label = tk.Label(self.registration_window, text="Gender:"
                                     , bg=main_color, fg=blue_str_color)
        self.gender_label.grid(row=9, column=0, padx=5, pady=5)

        # Create radio buttons for gender options
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")  # Set default value to "Male"
        genders = ["Male", "Female", "Others"]
        for i, gender in enumerate(genders):
            tk.Radiobutton(self.registration_window, text=gender, variable=self.gender_var, value=gender,
                           bg=main_color).grid(row=9 + i, column=1, padx=2, pady=2, sticky=tk.W)

        self.submit_button = customtkinter.CTkButton(
            master=self.registration_window,
            command=self.submit_registration,
            text="Submit",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=120,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        self.submit_button.grid(row=12, column=0, columnspan=2, pady=10)

        self.return_button = customtkinter.CTkButton(
            master=self.registration_window,
            command=self.return_to_main_window,
            text="Return",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=120,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        self.return_button.grid(row=13, column=0, columnspan=2, pady=5)

    def submit_registration(self):
        data = {}
        data['customer_id'] = self.customer_id_entry.get()
        data['first_name'] = self.first_name_entry.get()
        data['last_name'] = self.last_name_entry.get()
        data['email'] = self.email_entry.get()
        data['password'] = self.password_entry.get()
        data['phone_number'] = self.phone_entry.get()
        data['gender'] = self.gender_var.get()
        data['street'] = self.street_entry.get()
        data['building_num'] = self.building_entry.get()
        data['city'] = self.city_entry.get()

        register(cur, conn, data)
        # Close the registration window after submission
        self.registration_window.destroy()
        self.main_window.root.deiconify()

    def return_to_main_window(self):
        self.registration_window.destroy()
        self.main_window.root.deiconify()


class ProductWindow:
    def __init__(self, root, first_name, last_name):

        self.root = root
        # Bind the on_close function to the window close event
        self.root.withdraw()  # Hide the main window while the product window is open
        self.cart = {}
        product_window = tk.Toplevel(self.root)
        product_window.title("Groceria")

        p1 = PhotoImage(file='Imegies/GroceriaLogo1.png')
        # Setting icon of master window
        product_window.iconphoto(False, p1)

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # font definition
        main_font = customtkinter.CTkFont(family="Helvetica", size=13)
        logo_font = customtkinter.CTkFont(family="Gisha", size=45)
        # Set the size of the product window to match the screen size
        product_window.geometry(f"{screen_width}x{screen_height}")

        # Create a new frame for the "Show Cart" button
        show_cart_frame = tk.Frame(product_window, bg=blue_light_color)
        show_cart_frame.pack(fill="x")
        product_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(customer_id))

        # Display the user's name on the left side of show_cart_frame
        user_label = tk.Label(show_cart_frame, text=f"Welcome, {first_name} {last_name}!"
                              , bg=blue_light_color, fg=blue_str_color, font=main_font)
        user_label.grid(row=0, column=0, sticky='w', padx=5)

        logo_label = tk.Label(show_cart_frame, text="Groceria"
                              , bg=blue_light_color, fg=blue_str_color, font=logo_font)
        logo_label.grid(row=0, column=1, padx=500, pady=5, columnspan=5)

        # Create a label for the "Show Cart" button inside the show_cart_frame
        # cart_button = tk.Button(show_cart_frame, text="show cart", command=self.show_cart_window
        #                         , bg=blue_light_color, fg=blue_str_color)
        cart_button = customtkinter.CTkButton(
            master=show_cart_frame,
            command=self.show_cart_window,
            text="Show Cart",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=blue_light_color,
            fg_color=blue_str_color)
        cart_button.grid(row=0, column=8, sticky='e', padx=5)
        history_button = customtkinter.CTkButton(
            master=show_cart_frame,
            command=self.show_history_window,
            text="History",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=blue_light_color,
            fg_color=blue_str_color)
        history_button.grid(row=0, column=7, sticky='e', padx=5, pady=5)
        # color for category bar
        s = ttk.Style()
        s.configure("TNotebook", background=blue_light_color)  # Set the background color of the notebook
        s.configure("TNotebook.Tab", background=blue_light_color)  # Set tab colors
        # Create the category bar
        category_bar = ttk.Notebook(product_window, style='TNotebook')
        category_bar.pack(fill="x")

        dairy_tab = tk.Frame(category_bar, bg=main_color)
        category_bar.add(dairy_tab, text="Categories")

        # button1 = tk.Button(dairy_tab, text="Dairy and Eggs", command=lambda: self.show_products(1))
        button1 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(1),
            text="Dairy and Eggs",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        button1.pack(side="left", padx=5, pady=5)

        # button2 = tk.Button(dairy_tab, text="Bakery", command=lambda: self.show_products(2))
        button2 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(2),
            text="Bakery",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        button2.pack(side="left", padx=5, pady=5)
        button3 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(3),
            text="Snacks and sweets",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button3 = tk.Button(dairy_tab, text="Snacks and sweets", command=lambda: self.show_products(3))
        button3.pack(side="left", padx=5, pady=5)
        button4 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(4),
            text="Meat and Seafood",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button4 = tk.Button(dairy_tab, text="Meat and Seafood", command=lambda: self.show_products(4))
        button4.pack(side="left", padx=5, pady=5)
        button5 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(5),
            text="Beverages",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button5 = tk.Button(dairy_tab, text="Beverages", command=lambda: self.show_products(5))
        button5.pack(side="left", padx=5, pady=5)
        button6 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(6),
            text="Pet Supplies",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button6 = tk.Button(dairy_tab, text="Pet Supplies", command=lambda: self.show_products(6))
        button6.pack(side="left", padx=5, pady=5)
        button7 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(7),
            text="Household and Cleaning",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button7 = tk.Button(dairy_tab, text="Household and Cleaning", command=lambda: self.show_products(7))
        button7.pack(side="left", padx=5, pady=5)
        button8 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(8),
            text="Pantry Staples",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button8 = tk.Button(dairy_tab, text="Pantry Staples", command=lambda: self.show_products(8))
        button8.pack(side="left", padx=5, pady=5)
        button9 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(9),
            text="Hygiene",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button9 = tk.Button(dairy_tab, text="Hygiene", command=lambda: self.show_products(9))
        button9.pack(side="left", padx=5, pady=5)
        button10 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(10),
            text="Nuts and dried fruits",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button10 = tk.Button(dairy_tab, text="Nuts and dried fruits", command=lambda: self.show_products(10))
        button10.pack(side="left", padx=5, pady=5)
        button11 = customtkinter.CTkButton(
            master=dairy_tab,
            command=lambda: self.show_products(11),
            text="Frozen Foods",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=60,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        # button11 = tk.Button(dairy_tab, text="Frozen Foods", command=lambda: self.show_products(11))
        button11.pack(side="left", padx=5, pady=5)

        # Create a frame to display products dynamically
        self.products_frame = tk.Frame(product_window, bg=main_color)
        self.products_frame.pack(fill="both", expand=True)

    def show_products(self, category):
        main_font = customtkinter.CTkFont(family="Helvetica", size=13)
        # Clear the product frame
        for widget in self.products_frame.winfo_children():
            widget.destroy()

        # Fetch products for the selected category from the database
        products = get_all_products(cur, conn, category)
        x = 0

        num_columns = 5

        self.products_frame.columnconfigure([j for j in range(num_columns)], weight=1, minsize=75)

        for i in range(0, len(products), num_columns):
            for j in range(num_columns):
                if x >= len(products):
                    break

                product_id = products[x][0]
                product_description = products[x][1]
                product_price = products[x][2]
                product_stock = products[x][3]

                frame = tk.Frame(
                    master=self.products_frame,
                    relief=tk.FLAT,
                    borderwidth=1,
                    bg=blue_light_color

                )

                frame.grid(row=i // num_columns, column=j, padx=5, pady=5, sticky="nsew")

                # Configure rows for consistent sizing
                for row_index in range(4):
                    frame.grid_rowconfigure(row_index, weight=1)

                product_image = Image.open(self.getImage(product_id))
                product_image = product_image.resize((100, 100))  # Resize the image if needed
                product_image = ImageTk.PhotoImage(product_image)

                product_image_label = tk.Label(frame, image=product_image)
                product_image_label.image = product_image
                product_image_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10, rowspan=3)  # Adjust rowspan

                product_label = tk.Label(frame, text=product_description, anchor="w", bg=blue_light_color)
                product_label.grid(row=0, column=1, sticky="ew", padx=10, pady=10, columnspan=3)

                price_label = tk.Label(frame, text=f"Price: ₪{product_price}", anchor="w", bg=blue_light_color)
                price_label.grid(row=1, column=1, sticky="ew", padx=10, pady=10, columnspan=3)

                amount = tk.IntVar()

                amount.set(0)  # Initial value

                def decrease(amnt):

                    if amnt.get() > 0:
                        amnt.set(amnt.get() - 1)
                    print(amnt.get())

                def increase(amnt):
                    amnt.set(amnt.get() + 1)
                    print(amnt.get())

                # btn_decrease = tk.Button(master=frame, text="-", command=lambda amnt=amount: decrease(amnt))
                btn_decrease = customtkinter.CTkButton(
                    master=frame,
                    command=lambda amnt=amount: decrease(amnt),
                    text="-",
                    font=main_font,
                    text_color=main_color,
                    hover=True,
                    hover_color=blue_mid_color,
                    height=10,
                    width=25,
                    border_width=2,
                    corner_radius=20,
                    border_color="#d3d3d3",
                    bg_color=blue_light_color,
                    fg_color=blue_str_color)
                btn_decrease.grid(row=2, column=1, sticky=tk.NW)

                lbl_value = tk.Label(master=frame, textvariable=amount)
                lbl_value.grid(row=2, column=2, sticky=tk.NW)  # Center the label within its cell

                # btn_increase = tk.Button(master=frame, text="+", command=lambda amnt=amount: increase(amnt))
                btn_increase = customtkinter.CTkButton(
                    master=frame,
                    command=lambda amnt=amount: increase(amnt),
                    text="+",
                    font=main_font,
                    text_color=main_color,
                    hover=True,
                    hover_color=blue_mid_color,
                    height=10,
                    width=25,
                    border_width=2,
                    corner_radius=20,
                    border_color="#d3d3d3",
                    bg_color=blue_light_color,
                    fg_color=blue_str_color)
                btn_increase.grid(row=2, column=3, sticky=tk.NW)

                # add_to_cart_button = tk.Button(frame, text="Add to Cart",
                #                                command=lambda desc=product_description,
                #                                               qty=amount, prod_id=product_id: self.add_to_cart(
                #                                    desc, prod_id, qty.get()))
                add_to_cart_button = customtkinter.CTkButton(
                    master=frame,
                    command=lambda desc=product_description, qty=amount, prod_id=product_id: self.add_to_cart(
                        desc, prod_id, qty.get() if qty.get() != 0 else messagebox.showinfo("no product",
                                                                                            "Please enter the amount")

                    ),
                    text="Add to Cart",
                    font=main_font,
                    text_color=main_color,
                    hover=True,
                    hover_color=blue_mid_color,
                    height=20,
                    width=40,
                    border_width=2,
                    corner_radius=20,
                    border_color="#d3d3d3",
                    bg_color=blue_light_color,
                    fg_color=blue_str_color)
                add_to_cart_button.grid(row=3, column=1, sticky="ew", padx=10, pady=10, columnspan=2)

                x += 1

    def update_frame_color(self, frame, product_stock):
        if product_stock > 0:
            frame.config(bg=blue_light_color)
        else:
            frame.config(bg=red_color)

    def add_to_cart(self, description, product_id, quantity):
        print(description)
        print(product_id)
        print(quantity)
        add_to_order_item(cur, conn, product_id, quantity, customer_id)

    def getImage(self, prod_id):

        product_images = {
            1: "Imegies/TnuvaMilk.jpg", 2: "Imegies/YotvataMilk.jpg", 3: "Imegies/Tapochips_elite.jpg"
            , 4: "Imegies/pringels.jpg", 5: "Imegies/cottageTnuva.jpg", 6: "Imegies/emek_cheese.jpg",
            7: "Imegies/butter_Tnuva.jpg", 8: "Imegies/milki-Elite.jpg", 9: "Imegies/eggs.jpg",
            10: "Imegies/bread_angel.jpg",
            11: "Imegies/coca_cola.jpg", 12: "Imegies/sprite.jpg", 13: "Imegies/Prigat.jpg", 14: "Imegies/nestea.jpg",
            15: "Imegies/fanta.jpg",
            16: "Imegies/jacobs.jpg", 17: "Imegies/doveDeodorant.jpg", 18: "Imegies/deodorantGillette.jpg",
            19: "Imegies/colgate.jpg",
            20: "Imegies/listerine.jpg", 21: "Imegies/doveDeodorant.jpg", 22: "Imegies/headAndShoulders.jpg",
            23: "Imegies/chicken.jpg"
            , 24: "Imegies/salomon.jpg", 25: "Imegies/sano_javel_wc.jpg", 26: "Imegies/sano_javel_bleach cleaner.jpg",
            27: "Imegies/fairy.jpg"
            , 28: "Imegies/bread_american.jpg", 29: "Imegies/Rye bread.jpg", 30: "Imegies/buns_berman.jpg"
            , 31: "Imegies/monge- dog food.jpg", 32: "Imegies/mongo-cat food.jpg", 33: "Imegies/pro plan- dog food.jpg",
            34: "Imegies/friskies- cat food.jpg"
        }
        if prod_id in product_images:
            image_fileName = product_images[prod_id]
            return image_fileName
        else:
            return None

    def show_cart_window(self):
        cart_window = tk.Toplevel(self.root, background=main_color)
        cart_window.title("My Cart")
        cart_window.resizable(False, False)
        p1 = PhotoImage(file='Imegies/GroceriaLogo1.png')
        # Setting icon of master window
        cart_window.iconphoto(False, p1)
        main_font = customtkinter.CTkFont(family="Helvetica", size=13)
        my_cart_font = customtkinter.CTkFont(family="Helvetica", size=20)
        canvas = tk.Canvas(cart_window, width=440, height=500, bg=main_color)
        scrollbar = tk.Scrollbar(cart_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.grid(row=0, column=0, sticky="nsew")
        frame = tk.Frame(master=canvas, relief=tk.FLAT, borderwidth=1, bg=main_color, width=440, height=500)
        frame.grid(row=0, column=0, sticky="nsew")
        canvas.create_window((0, 0), window=frame, anchor="nw")
        # scroll with mouse
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        my_cart_label = tk.Label(frame, text="My cart", font=my_cart_font, bg=main_color, fg=blue_str_color)
        my_cart_label.grid(row=0, columnspan=2, pady=10)

        order_item_data = get_order_items(cur, conn, customer_id)
        frames_list = []
        order_item_id, product_id, price, quantity = order_item_data[0]
        print(product_id)
        print(price)
        print(quantity)

        for row, (order_item_id, product_id, price, quantity) in enumerate(order_item_data, start=1):
            product_name = get_product(cur, conn, product_id)

            Prod_frame = tk.Frame(
                master=frame,
                relief=tk.FLAT,
                borderwidth=1,
                bg=blue_light_color
            )

            Prod_frame.grid(row=row, column=0, padx=10, pady=10, sticky="nsew")
            Prod_frame.config(width=canvas.winfo_width() - scrollbar.winfo_width(),
                              height=canvas.winfo_height())
            label_width = 17
            frames_list.append(Prod_frame)
            # Configure columns for consistent sizing
            for column_index in range(4):
                Prod_frame.grid_columnconfigure(column_index, weight=1)

            product_label = tk.Label(Prod_frame, text=product_name, anchor="w", width=label_width
                                     , background=blue_light_color)
            product_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10, columnspan=3)

            price_label = tk.Label(Prod_frame, text=f"Price: ₪{price}", anchor="w", width=label_width
                                   , background=blue_light_color)
            price_label.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

            quantity_label = tk.Label(Prod_frame, text=f"Quantity: {quantity}", anchor="w", width=label_width,
                                      background=blue_light_color)
            quantity_label.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

            remove_button = customtkinter.CTkButton(
                master=Prod_frame,
                command=lambda del_order_item_id=order_item_id, remove_price=price,
                               del_frame=Prod_frame, id=product_id, qty=quantity:
                self.remove_from_cart(del_order_item_id, remove_price,
                                      del_frame, id, qty, customer_id),
                text="Remove",
                font=main_font,
                text_color=main_color,
                hover=True,
                hover_color="#FF6D60",
                height=20,
                width=40,
                border_width=2,
                corner_radius=20,
                border_color="#d3d3d3",
                bg_color=blue_light_color,
                fg_color="#F45050")
            remove_button.grid(row=1, column=2, sticky="ew", padx=10, pady=10)

        buy_button = customtkinter.CTkButton(
            master=cart_window,
            command=lambda: self.buy(root, cart_window),
            text="Buy",
            font=main_font,
            text_color="#001C30",
            hover=True,
            hover_color="#E2F6CA",
            height=60,
            width=200,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=green_color)
        buy_button.grid(row=len(order_item_data) + 1, columnspan=4, pady=10)
        # Update the scrollable region
        frame.update_idletasks()
        frame.bind("<Configure>", canvas.config(scrollregion=canvas.bbox("all")))

    def remove_from_cart(self, item_to_delete, price, del_frame, id, quantity, customer_id):
        print(id)
        print(quantity)
        update_stock(cur, conn, id, quantity)

        # Remove widgets from the frame
        for widget in del_frame.winfo_children():
            widget.destroy()
        # Destroy the frame and its widgets
        del_frame.destroy()
        remove_order_item(cur, conn, item_to_delete, price, customer_id)

    def buy(self, root, cart_frame):
        self.root = root
        # self.root.geometry('600x300')
        self.cart_frame = cart_frame
        self.cart_frame.withdraw()  # Hide the main window while the product window is open
        buy_window = tk.Toplevel(self.root, background=main_color)
        buy_window.title("Buy process")
        buy_window.resizable(False, False)
        p1 = PhotoImage(file='Imegies/GroceriaLogo1.png')
        # Setting icon of master window
        buy_window.iconphoto(False, p1)
        main_font = customtkinter.CTkFont(family="Helvetica", size=13)

        return_frame = tk.Frame(buy_window, background=main_color)
        checkout_frame = tk.Frame(buy_window, background=main_color)
        credit_card_frame = tk.Frame(buy_window, background=main_color)

        return_frame.grid()
        checkout_frame.grid()
        credit_card_frame.grid()

        # return_button = tk.Button(return_frame, text="Return", font=("Helvetica", 10),
        #                           command=lambda: self.return_to_cart(buy_window))
        return_button = customtkinter.CTkButton(
            master=return_frame,
            command=lambda: self.return_to_cart(buy_window),
            text="Return",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=20,
            width=40,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        return_button.grid(row=0, column=0, pady=10, sticky="w")
        # change_button = tk.Button(return_frame, text="change address", font=("Helvetica", 10))
        change_button = customtkinter.CTkButton(
            master=return_frame,
            command=lambda: self.change_costumer_address(root, buy_window, cart_frame),
            text="Change address",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=20,
            width=40,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        change_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        checkout_label = tk.Label(checkout_frame, text="Checkout:", font=("Helvetica", 16)
                                  , bg=main_color, fg=blue_str_color)
        checkout_label.grid(row=0, column=0, columnspan=4)

        shipment_city, shipment_street, shipment_building_num, email = get_shipment(cur, conn, customer_id)
        total_price = get_total_price(cur, conn, customer_id)

        shipment_city_label = tk.Label(checkout_frame, text=f"city: {shipment_city}", font=("Helvetica", 14)
                                       , bg=main_color, fg=blue_str_color)
        shipment_street_label = tk.Label(checkout_frame, text=f"street: {shipment_street}", font=("Helvetica", 14)
                                         , bg=main_color, fg=blue_str_color)
        shipment_building_num_label = tk.Label(checkout_frame,
                                               text=f"building number: {shipment_building_num}", font=("Helvetica", 14)
                                               , bg=main_color, fg=blue_str_color)
        email_label = tk.Label(checkout_frame, text=f"email: {email}", font=("Helvetica", 14)
                               , bg=main_color, fg=blue_str_color)
        total_price_label = tk.Label(checkout_frame, text=f"Total: ₪ {total_price}", font=("Helvetica", 14)
                                     , bg=main_color, fg=blue_str_color)

        shipment_city_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        shipment_street_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        shipment_building_num_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        email_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        total_price_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # Set uniform row and column weights for consistent sizes
        for i in range(10):  # Assuming you have 10 rows in total
            credit_card_frame.rowconfigure(i, weight=1)
        for i in range(3):  # Assuming you have 4 columns in total
            credit_card_frame.columnconfigure(i, weight=1)

        payment_label = tk.Label(credit_card_frame, text="Payment Method:", font=("Helvetica", 16), bd=2
                                 , bg=main_color, fg=blue_str_color)
        payment_label.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        # Create a label and entry for the credit card number
        credit_card_num_label = tk.Label(credit_card_frame, text="Credit card number", bd=2
                                         , bg=main_color, fg=blue_str_color)
        credit_card_num_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)
        credit_card_entry = tk.Entry(credit_card_frame, bd=2)
        credit_card_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.NW)

        # Month Label
        month_label = tk.Label(credit_card_frame, text="Month:", bd=2
                               , bg=main_color, fg=blue_str_color)
        month_label.grid(row=2, column=0, sticky=tk.NW, padx=5, pady=5)

        # Spinbox for Month
        sb_month = tk.Spinbox(credit_card_frame, from_=1, to=12, width=5, bd=2)
        sb_month.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NW)

        # Year Label
        year_label = tk.Label(credit_card_frame, text="Year:", bd=2
                              , bg=main_color, fg=blue_str_color)
        year_label.grid(row=2, column=2, sticky=tk.NW, padx=5, pady=5)

        # Spinbox for Year
        sb_year = tk.Spinbox(credit_card_frame, from_=2023, to=2050, width=5, bd=2)
        sb_year.grid(row=2, column=3, padx=5, pady=5)

        # CVC Entry
        cvc_label = tk.Label(credit_card_frame, text="CVC:", bd=2
                             , bg=main_color, fg=blue_str_color)
        cvc_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.NW)

        cvc_entry = tk.Entry(credit_card_frame, width=5, bd=2)  # Make it smaller
        cvc_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.NW)

        # Card Holder Label
        card_holder_label = tk.Label(credit_card_frame, text="Card Holder:", bd=2
                                     , bg=main_color, fg=blue_str_color)
        card_holder_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.NW)

        # Card Holder Entry
        card_holder_entry = tk.Entry(credit_card_frame, bd=2)
        card_holder_entry.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky=tk.NW)

        print(credit_card_entry.get())
        print(sb_month.get())
        print(sb_year.get())
        print(card_holder_entry.get())
        # buy_now_button = tk.Button(credit_card_frame, text="Buy Now", font=("Helvetica", 10), width=20, height=3, bd=2
        #                            , command=lambda: self.complete_payment(buy_window))
        buy_now_button = customtkinter.CTkButton(
            master=credit_card_frame,
            command=lambda: self.check_payment(credit_card_entry.get(), cvc_entry.get(),
                                               card_holder_entry.get(), buy_window),
            text="Buy",
            font=main_font,
            text_color="#001C30",
            hover=True,
            hover_color="#E2F6CA",
            height=60,
            width=200,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=green_color)
        buy_now_button.grid(row=5, column=0, padx=10, pady=10, columnspan=4)

    def check_payment(self, credit_card, cvc, name_holder, window):
        if credit_card != "" and cvc != "" and name_holder != "":
            self.complete_payment(window)
        else:
            messagebox.showinfo("enter payment", "Please enter payment method first")

    def complete_payment(self, del_window):
        create_shipment(cur, conn, customer_id)
        create_new_order(cur, conn, customer_id)
        del_window.destroy()  # Destroy the buy_window
        messagebox.showinfo("Payment Completed", "Payment has been successfully completed!")

    def return_to_cart(self, del_window):
        self.show_cart_window()  # Show the cart_window again
        del_window.destroy()  # Destroy the buy_window
        self.root.withdraw()

    def on_close(self, customer_id):
        result = messagebox.askyesno("Confirm Exit", "Do you want to exit and delete the order?")
        if result:
            delete_order(cur, conn, customer_id)
            root.destroy()

    def update_canvas_size(event, canvas, frame_width):
        canvas.config(width=frame_width)

    def change_costumer_address(self, root, window, cart_frame):
        self.root = root
        # self.root.geometry('600x300')
        self.window = window
        self.window.withdraw()  # Hide the main window while the product window is open
        change_address = tk.Toplevel(self.root, background=main_color)
        change_address.title("Change address")
        p1 = PhotoImage(file='Imegies/GroceriaLogo1.png')
        # Setting icon of master window
        change_address.iconphoto(False, p1)
        main_font = customtkinter.CTkFont(family="Helvetica", size=13)

        payment_label = tk.Label(change_address, text="Changing shipping address:", font=("Helvetica", 16), bd=2
                                 , bg=main_color, fg=blue_str_color)
        payment_label.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

        shipment_city, shipment_street, shipment_building_num, email = get_shipment(cur, conn, customer_id)
        shipment_city = tk.StringVar(value=shipment_city)  # StringVar to hold the variable's value
        shipment_street = tk.StringVar(value=shipment_street)  # StringVar to hold the variable's value
        shipment_building_num = tk.StringVar(value=shipment_building_num)  # StringVar to hold the variable's value
        email = tk.StringVar(value=email)  # StringVar to hold the variable's value

        change_cust_city_label = tk.Label(change_address, text="New city:", bd=2
                                          , bg=main_color, fg=blue_str_color)
        change_cust_city_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NW)
        change_cust_city_entry = tk.Entry(change_address, bd=2, textvariable=shipment_city)
        change_cust_city_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky=tk.NW)

        change_cust_street_label = tk.Label(change_address, text="New street:", bd=2
                                            , bg=main_color, fg=blue_str_color)
        change_cust_street_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.NW)
        change_cust_street_entry = tk.Entry(change_address, bd=2, textvariable=shipment_street)
        change_cust_street_entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky=tk.NW)

        change_cust_build_label = tk.Label(change_address, text="New building number:", bd=2
                                           , bg=main_color, fg=blue_str_color)
        change_cust_build_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.NW)
        change_cust_build_entry = tk.Entry(change_address, bd=2, textvariable=shipment_building_num)
        change_cust_build_entry.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky=tk.NW)

        return_button = customtkinter.CTkButton(
            master=change_address,
            command=lambda: self.return_to_buy(change_address, cart_frame),
            text="Return",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=20,
            width=40,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        return_button.grid(row=0, column=0, pady=10, sticky="w")

        submit_button = customtkinter.CTkButton(
            master=change_address,
            command=lambda: self.submit_shipping_changes(change_cust_city_entry.get(), change_cust_street_entry.get(),
                                                         change_cust_build_entry.get()),
            text="Submit",
            font=main_font,
            text_color=main_color,
            hover=True,
            hover_color=blue_mid_color,
            height=40,
            width=120,
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color=main_color,
            fg_color=blue_str_color)
        submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    def return_to_buy(self, del_window, cart_frame):
        self.buy(root, cart_frame)  # Show the buy again
        del_window.withdraw()
        del_window.destroy()  # Destroy the buy_window

    def submit_shipping_changes(self, city, street, bui_num):
        set_shipment(cur, conn, city, street, bui_num, customer_id)
        print("done")

    def _on_mousewheel(self, event, canvas):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def show_history_window(self):
        history_window = tk.Toplevel(self.root, background=main_color)
        history_window.title("My History")
        history_window.resizable(False, False)
        p1 = PhotoImage(file='Imegies/GroceriaLogo1.png')
        # Setting icon of master window
        history_window.iconphoto(False, p1)
        main_font = customtkinter.CTkFont(family="Helvetica", size=13)
        my_cart_font = customtkinter.CTkFont(family="Helvetica", size=20)

        canvas = tk.Canvas(history_window, width=550, height=500, bg=main_color, relief=FLAT)
        scrollbar = tk.Scrollbar(history_window, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.grid(row=0, column=0, sticky="nsew")

        frame = tk.Frame(master=canvas, relief=tk.FLAT, borderwidth=1, bg=main_color, width=canvas.winfo_width())
        frame.grid(row=0, column=0, sticky="nsew")
        canvas.create_window((0, 0), window=frame, anchor="nw", tags="frame")
        # scroll with mouse
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        my_history_label = tk.Label(frame, text="Order History", font=my_cart_font, bg=main_color, fg=blue_str_color)
        my_history_label.grid(row=0, columnspan=2, pady=10)
        orders_id = get_all_cust_order_id(cur, conn, customer_id)

        for row, (order_id) in enumerate(orders_id, start=1):
            order_details = get_cust_order(cur, order_id)
            for order in order_details:
                date, shipment_ct, shipment_st, shipment_bn, price, email = order

                order_history_frame = tk.Frame(
                    master=frame,
                    relief=tk.FLAT,
                    borderwidth=1,
                    bg=blue_light_color
                )

                order_history_frame.grid(row=row, column=0, padx=10, pady=10, sticky="nsew")
                order_history_frame.config(width=frame.winfo_width(),
                                           height=frame.winfo_height())
                label_width = 17
                # Configure columns for consistent sizing
                for column_index in range(4):
                    order_history_frame.grid_columnconfigure(column_index, weight=1)

                order_id = list(order_id)
                formatted_order_id = order_id[0]  # Extract the first element of the first tuple
                order_label = tk.Label(order_history_frame, text=f"Order ID: {formatted_order_id}"
                                       , anchor="w", width=label_width
                                       , background=blue_light_color)
                order_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

                date_label = tk.Label(order_history_frame, text=f"Date: {date}", anchor="w", width=label_width
                                      , background=blue_light_color)
                date_label.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
                total_price_label = tk.Label(order_history_frame, text=f"Total price: {price}", anchor="w",
                                             width=label_width
                                             , background=blue_light_color)

                total_price_label.grid(row=0, column=2, sticky="ew", padx=10, pady=10)
                show_details_button = customtkinter.CTkButton(
                    master=order_history_frame,
                    command=lambda c_order_id=formatted_order_id, c_shipment_ct=shipment_ct, c_shipment_st=shipment_st,
                                   c_shipment_bn=shipment_bn, c_date=date, t_price=price: self.show_check(c_order_id,
                                                                                                          c_shipment_ct,
                                                                                                          c_shipment_st,
                                                                                                          c_shipment_bn,
                                                                                                          c_date,
                                                                                                          t_price),
                    text="Invoice",
                    font=main_font,
                    text_color=main_color,
                    hover=True,
                    hover_color=blue_mid_color,
                    height=40,
                    width=40,
                    border_width=2,
                    corner_radius=20,
                    border_color="#d3d3d3",
                    bg_color=blue_light_color,
                    fg_color=blue_str_color)
                show_details_button.grid(row=0, column=3, padx=10, pady=10)

        frame.update_idletasks()
        frame.bind("<Configure>", canvas.config(scrollregion=canvas.bbox("all")))

    def show_check(self, order_id, shipment_city, shipment_str, shipment_bn, date, t_price):
        check_window = tk.Toplevel(self.root)  # Create a new Toplevel window
        check_window.title(f"Invoice number: {order_id}")
        check_window.geometry("470x600")
        check_window.resizable(False, False)
        scroll_y = Scrollbar(check_window, orient=VERTICAL)
        check_txt = tk.Text(check_window, height=36, width=55)
        check_txt.tag_configure("center", justify="center")

        # title of the check
        check_txt.insert("end", "          Groceria\n", "center")
        check_txt.insert("end", "          Online grocery shop\n", "center")
        check_txt.insert("end", "\n")
        check_txt.insert("end", "          Invoice\n", "center")
        check_txt.insert("end", f"Invoice number: {order_id}\n")
        check_txt.insert("end", f"Invoice date: {date}\n")
        # check_txt.insert("end", f"Customer name : {date}\n")
        check_txt.insert("end", "\n")
        check_txt.insert("end", "Customer address:\n")
        check_txt.insert("end", f"City: {shipment_city}\n")
        check_txt.insert("end", f"Street: {shipment_str}\n")
        check_txt.insert("end", f"Building number: {shipment_bn}\n")
        check_txt.insert("end", "\n")
        check_txt.insert("end", "=======================================================\n")
        check_txt.insert("end", "Product                      Qty                 Price\n")
        check_txt.insert("end", "=======================================================\n")
        cust_products = get_order_product(cur, order_id)

        for x, (desc, price, qty) in enumerate(cust_products, start=1):
            # Calculate the spaces needed to align the text
            padding_desc = 30 - len(desc)
            padding_qty = 20 - len(str(qty))
            formatted_line = f"{desc}{' ' * padding_desc}{qty}{' ' * padding_qty}{price * qty}\n"
            check_txt.insert("end", formatted_line)
        check_txt.insert("end", "=======================================================\n")
        check_txt.insert("end", f"Total:                                            {t_price}\n")

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=check_txt.yview)
        check_txt.pack(fill=tk.BOTH, expand=True)  # Fill both horizontally and vertically


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

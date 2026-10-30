import json
import os
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox, filedialog

# -------------------- CONFIGURATION --------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"  # Change this before using the software in a real shop.
PRODUCT_FILE = "products.json"

DEFAULT_PRODUCTS = [
    {"name": "Nutella Choco Spread", "category": "Snacks", "price": 120.0},
    {"name": "Noodles (1 Pack)", "category": "Snacks", "price": 40.0},
    {"name": "Lays (10 Rs)", "category": "Snacks", "price": 10.0},
    {"name": "Oreo (20 Rs)", "category": "Snacks", "price": 20.0},
    {"name": "Chocolate Muffin", "category": "Snacks", "price": 30.0},
    {"name": "Dairy Milk Silk", "category": "Snacks", "price": 60.0},
    {"name": "Namkeen (15 Rs)", "category": "Snacks", "price": 15.0},
    {"name": "Aashirvaad Atta (1kg)", "category": "Grocery", "price": 42.0},
    {"name": "Pasta (1kg)", "category": "Grocery", "price": 120.0},
    {"name": "Basmati Rice (1kg)", "category": "Grocery", "price": 160.0},
    {"name": "Sunflower Oil (1ltr)", "category": "Grocery", "price": 113.0},
    {"name": "Refined Sugar (1kg)", "category": "Grocery", "price": 55.0},
    {"name": "Daal (1kg)", "category": "Grocery", "price": 76.0},
    {"name": "Tea Powder (1kg)", "category": "Grocery", "price": 480.0},
    {"name": "Bathing Soap", "category": "Beauty & Hygiene", "price": 30.0},
    {"name": "Shampoo (1ltr)", "category": "Beauty & Hygiene", "price": 180.0},
    {"name": "Body Lotion (1ltr)", "category": "Beauty & Hygiene", "price": 500.0},
    {"name": "Face Cream", "category": "Beauty & Hygiene", "price": 130.0},
    {"name": "Shaving Foam", "category": "Beauty & Hygiene", "price": 85.0},
    {"name": "Face Mask (1 piece)", "category": "Beauty & Hygiene", "price": 100.0},
    {"name": "Hand Sanitizer (50ml)", "category": "Beauty & Hygiene", "price": 20.0},
]


class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Market Billing Software")
        self.root.geometry("1180x760")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#5B2C6F")

        self.products = self.load_products()
        self.quantity_vars = {}
        self.product_rows = {}
        self.last_bill_text = ""

        title = Label(
            root, text="SUPER MARKET BILLING SYSTEM",
            font=("Arial Black", 21), bg="#6C3483", fg="white",
            pady=12
        )
        title.pack(fill=X)

        top = Frame(root, bg="#5B2C6F")
        top.pack(fill=X, padx=12, pady=8)
        Button(
            top, text="Admin Login", command=self.open_admin_login,
            font=("Arial", 11, "bold"), bg="#F4D03F", fg="#4A235A",
            padx=18, pady=7
        ).pack(side=RIGHT)
        Label(
            top, text="Customer Billing Counter",
            font=("Arial", 14, "bold"), bg="#5B2C6F", fg="white"
        ).pack(side=LEFT)

        customer = LabelFrame(
            root, text="Customer Details", font=("Arial", 11, "bold"),
            bg="#A569BD", fg="white", padx=10, pady=8
        )
        customer.pack(fill=X, padx=12, pady=5)

        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        Label(customer, text="Customer Name", bg="#A569BD", fg="white").grid(row=0, column=0, padx=6)
        Entry(customer, textvariable=self.customer_name, width=28).grid(row=0, column=1, padx=6)
        Label(customer, text="Contact No.", bg="#A569BD", fg="white").grid(row=0, column=2, padx=6)
        Entry(customer, textvariable=self.customer_phone, width=22).grid(row=0, column=3, padx=6)

        main = Frame(root, bg="#5B2C6F")
        main.pack(fill=BOTH, expand=True, padx=12, pady=6)

        left = LabelFrame(
            main, text="Available Products (Enter Quantity)",
            font=("Arial", 11, "bold"), bg="#E5B4F3", fg="#6C3483"
        )
        left.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 6))

        columns = ("product", "category", "price", "quantity")
        self.product_tree = ttk.Treeview(left, columns=columns, show="headings", height=18)
        self.product_tree.heading("product", text="Product")
        self.product_tree.heading("category", text="Category")
        self.product_tree.heading("price", text="Price (Rs.)")
        self.product_tree.heading("quantity", text="Qty")
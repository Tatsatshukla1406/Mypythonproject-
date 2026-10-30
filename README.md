# Mypythonproject-
# Super Market Billing System with Admin Portal

## Project Overview

The **Super Market Billing System** is a desktop-based billing application developed using Python and Tkinter. It is designed to simplify supermarket billing operations and provide an easy-to-use interface for managing products, prices, and customer bills.

The application includes two main sections: **Admin Portal** and **Customer Billing System**. The Admin Portal allows authorized users to manage the product inventory, while the billing section helps generate customer bills quickly and accurately.

## Features

### 1. Admin Portal
- Secure admin login system.
- Add new products to the inventory.
- Remove existing products.
- Update product names and prices.
- Manage product categories.
- Save product information automatically in a JSON file.

### 2. Customer Billing System
- Enter customer details.
- Browse products by category.
- Select products and enter quantities.
- Calculate product-wise prices automatically.
- Generate customer bills.
- View the complete bill in the billing area.
- Save generated invoices as text files.

### 3. Automatic Tax Calculation
The system automatically calculates taxes according to product categories:
- Snacks: 5%
- Grocery: 1%
- Beauty & Hygiene: 10%

### 4. Data Management
Product information is stored in a JSON file, so changes made by the admin remain available when the application is reopened.

## Technologies Used

- **Programming Language:** Python
- **GUI Framework:** Tkinter
- **Data Storage:** JSON
- **Invoice Format:** TXT
- **IDE:** Visual Studio Code / PyCharm

## Installation and Usage

1. Download or clone this repository.
2. Make sure Python is installed on your computer.
3. Open the project folder.
4. Run the Python file using:

```bash
python Super_Market_Billing_Admin_Portal.py
```

5. Login to the Admin Portal using the demo credentials:

- Username: `admin`
- Password: `admin123`

**Note:** Change the default admin password before using this application in a real business environment.

## Project Objective

The main objective of this project is to reduce manual billing work, improve calculation accuracy, and make product management easier for small supermarkets and retail shops.

## Future Improvements

- Database integration using MySQL or SQLite.
- User-friendly sales reports.
- Daily and monthly sales tracking.
- PDF invoice generation.
- Improved admin authentication and security.

---

**Developed with Python ❤️**

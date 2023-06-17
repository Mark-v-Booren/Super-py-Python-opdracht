import csv
import os
from rich.table import Table
from rich.console import Console
from datetime import datetime

with open("date.txt", "r") as file:
    date_str = file.read().strip()
    date_from_file = datetime.strptime(date_str, "%Y-%m-%d").date()
    current_date = date_from_file.strftime("%Y-%m-%d")


def create_csv(str):
    if os.path.isfile(str):
        print(f"File '{str}' found.")
        return
    rows = []
    # Open the CSV file in write mode
    with open(str, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['id', 'name', 'price', 'exp-date', 'date'])
        # Write the data rows
        writer.writerows(rows)
        print(f"File '{str}' created.")
        return


# create sold.CSV-file
def create_sold_csv(sold):
    if os.path.isfile(sold):
        print(f"File '{sold}' found.")
        return
    rows = []
    # Open the CSV file in write mode
    with open(sold, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'price', 'date'])
        writer.writerows(rows)
        print(f"File '{sold}' created.")
        return


# add report data
def display_csv_in_stock(filename):
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    print("************* In stock: ***************: ")
    # Create a table
    table = Table(show_header=True, header_style="green")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Amount")
    table.add_column("Price")
    table.add_column("Expire Date")
    table.add_column("Entry Date")
    # Add rows to the table
    for row in rows:
        table.add_row(*row)
    # Create a console and print the table
    console = Console()
    console.print(table)


def display_csv_sold(filename):
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    print("************* Sold: ***************: ")
    # Create a table
    table = Table(show_header=True, header_style="green")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Price")
    table.add_column("Date")
    for row in rows:
        table.add_row(*row)
    console = Console()
    console.print(table)


def add_product_to_csv_in_stock(in_stock,
                                name,
                                price,
                                expire_date
                                ):
    # Open the CSV file in append mode
    date = current_date
    with open(in_stock, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the new product row
        writer.writerow([get_last_id(in_stock) + 1, name,
                         price, expire_date,
                         date])
    print(f"Product '{name}' added to '{in_stock}' successfully.")


def add_product_to_csv_sold(in_stock, sold, name, price):
    date = current_date

    found_product = None

    # Search for the product in the in_stock file
    with open(in_stock, 'r') as in_stock:
        reader = csv.reader(in_stock)
        for row in reader:
            if row[1].strip() == name.strip():
                found_product = row
                break

    # If the product is found, write it to the sold file
    if found_product:
        with open(sold, 'a', newline='') as sold:
            writer = csv.writer(sold)
            writer.writerow([found_product[0], name, price, date])
            print("Product sold successfully!")
    else:
        print("Product not found!")


def remove_when_sold(in_stock, name):

    with open(in_stock, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    # Find the row(s) with the specified name
        matching_rows = [row for row in rows if row['name'] == name]

    if not matching_rows:
        print(f"No rows found with the name '{name}'")
        return
    # Remove the matching rows from the list of rows
    for row in matching_rows:
        rows.remove(row)
    # Overwrite the CSV file with the updated contents
    with open("in_stock.csv", 'w', newline='') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Row(s) with the name '{name}' removed from in_stock.csv")


def get_last_id(in_stock):
    # Open the CSV file in read mode
    with open(in_stock, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        # Find the last ID in the existing data
        if len(rows) > 1:
            last_row = rows[-1]
            if len(last_row) > 0:
                last_id = int(last_row[0])
            else:
                last_id = 0
        else:
            last_id = 0
    return last_id


def calculate_profit(csv_file):
    # Read the contents of the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        total_profit = 0
        for row in reader:
            try:
                price = float(row['price'])
                total_profit += price
            except ValueError:
                print(f"Invalid price value found in row: {row}")

    print(f'The total profit of today is {total_profit}!')


def check_expired_products(file):

    # # Read the contents of the CSV file
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        # field_names = reader.fieldnames
        products = list(reader)
    # # Get the current date or a date in the future
    date_now = input("Enter the current date (YYYY-MM-DD): ")

    expired_products = []
    for product in products:
        expire_date_str = product['exp-date']
        if expire_date_str < date_now:
            expired_products.append(product)
            print(f'product {expired_products} == expired! ')
        else:
            print('all good!')

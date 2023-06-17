
import argparse
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import pandas as pd
from revenue import revenue
from profit import profit
from helpers import current_date, create_csv, remove_when_sold, create_sold_csv, check_expired_products, display_csv_sold, display_csv_in_stock, calculate_profit, add_product_to_csv_in_stock, add_product_to_csv_sold

__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def main():
    pass


create_csv('in_stock.csv')
create_sold_csv('sold.csv')

parser = argparse.ArgumentParser(description='Manage products in the in_stock.csv file')

subparsers = parser.add_subparsers(dest='command', help='Available commands')

add_parser = subparsers.add_parser('add', help='Add a product to the in_stock.csv file')
add_parser.add_argument('--name', type=str, help='Product name', required=True)
add_parser.add_argument('--price', type=float,
                        help='Price of product', required=True)
add_parser.add_argument('--expire_date', type=str,
                        help='Expiration date (DD-MM-YYYY)', required=True)

sell_parser = subparsers.add_parser('sold', help=' Add a product to the sold.csv file')
sell_parser.add_argument('--name', help=' Add a product to the sold.csv file')
sell_parser.add_argument('--price', type=float, help=' Add a product to the sold.csv file')

parser.add_argument('--report', help='Command for reports')
parser.add_argument('--expired', help='Check for expired dates in stock ')

profit_parser = subparsers.add_parser('profit', help='Get the profit on certain date')
profit_parser.add_argument('--date', type=str, help=' Add the date')

revenue_parser = subparsers.add_parser('revenue', help='Get the revenue on certain date')
revenue_parser.add_argument('--date', type=str, help='Add date')

parser.add_argument('--advance_time', type=int,
                    help='Advance time by specified number of days')

# Parse the arguments from the command line
args = parser.parse_args()


if args.command == 'revenue':
    revenue('sold.csv', args.date)

if args.command == 'profit':
    profit('sold.csv', 'in_stock.csv', args.date)

if args.expired == 'check':
    check_expired_products('in_stock.csv')

if args.command == 'add':
    add_product_to_csv_in_stock('in_stock.csv', args.name, args.price, args.expire_date)

if args.command == 'sold':
    add_product_to_csv_sold('in_stock.csv', 'sold.csv', args.name, args.price)
    remove_when_sold('in_stock.csv', args.name)

if args.advance_time:
    current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
    new_date = current_date + timedelta(days=args.advance_time)
    with open("date.txt", "w") as file:
        file.write(new_date.strftime("%Y-%m-%d"))
        current_date = new_date
else:
    new_date = current_date

if args.report == 'sold':
    display_csv_sold('sold.csv')

if args.report == 'in_stock':
    display_csv_in_stock('in_stock.csv')


if args.report == 'total':
    display_csv_in_stock('in_stock.csv')
    display_csv_sold('sold.csv')

if args.report == 'revenue':
    calculate_profit('sold.csv')
    df = pd.read_csv('sold.csv')
    x = df['name']
    y = df['price']
# Plot the data
    plt.plot(x, y)
    plt.xlabel('date')
    plt.ylabel('prices')
    plt.title('Revenue')
    plt.grid(True)
    plt.show()


print("Current date:", current_date)


if __name__ == "__main__":
    main()

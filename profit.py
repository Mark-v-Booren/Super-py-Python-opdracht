import csv
import matplotlib.pyplot as plt


def profit(sold_csv, in_stock, target_date):

    sold_products = []
    sold_prices = []
    total_revenue = 0.0
    total_in_stock = 0.0
    with open(sold_csv, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            date = row[3]
            price = float(row[2])
            product = row[1]
            if date <= target_date:
                total_revenue += price
                sold_products.append(product)
                sold_prices.append(price)
    with open(in_stock, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            date = row[4]
            price = float(row[2])

            if date <= target_date:
                total_in_stock += price
                 
    total_profit = total_revenue - total_in_stock
    formatted_profit = round(total_profit, 2)
    print('Profit', target_date, '=', formatted_profit, '!')
    plt.bar(sold_products, sold_prices)
    plt.xlabel('Product')
    plt.ylabel('Prices in €')
    plt.title('profit till: ' + target_date + ' is €' + str(formatted_profit))
    plt.show()

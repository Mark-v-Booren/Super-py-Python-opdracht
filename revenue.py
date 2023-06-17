import csv
import matplotlib.pyplot as plt


def revenue(sold_csv, target_date):

    products = []
    revenues = []

    total_revenue = 0.0
    with open(sold_csv, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            date = row[3]
            price = float(row[2])
            names = row[1]

            if date <= target_date:
                total_revenue += price
                products.append(names)
                revenues.append(price)

    plt.bar(products, revenues)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Total revenue til ' + target_date + ' is € ' + str(total_revenue))
    plt.xticks(rotation=45)
    plt.show()

    print('Revenue on', target_date, '=', total_revenue, '!')

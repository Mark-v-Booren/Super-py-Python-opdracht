

Please check for the right updates:

python --version
pip --version
pip install rich
pip install pandas
pip install matplotlib


Manage products in the in_stock.csv file: 

From the terminal choose the right directory-path:
Example C:/Winc/superpy/ always follewed by main.py 

The 'current date' is a fictional date.
All products added or sold are processed with the 'current date'
To adjust the date type the follwing:
(directory-path)main.py --advance_time (number)

To add product :
main.py add --name (here the product) --price (here the price) -- expire_date (YYYY-MM-DD) 

To sell a product :
main.py sold --name (here the product) --price (here the price) 

To get the revenue by date :
main.py revenue --date (YYYY-MM-DD)

To get the profit by date :
main.py profit --date (YYYY-MM-DD)

Options for reports: 

main.py --report sold

main.py --report in_stock

main.py --report total 

To check the expired date of the products in stock 

main.py --expired check (this will lead to an input for a date to check: handy to check which products will expire soon...)










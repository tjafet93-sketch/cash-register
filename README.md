<img width="330" height="1341" alt="Diagrama de flujo de registradora drawio" src="https://github.com/user-attachments/assets/225f193e-8df5-43c6-80b6-ce38577cdb91" />

🛒 Sales Register — Daily Sales Tracker
A simple Python console application that registers product sales, calculates totals, and displays a daily summary report.

📋 Description
This program allows a cashier or store operator to record multiple product sales in a single session. At the end, it displays a summary with all products sold and the total amount collected for the day.

🗂️ Project Structure
sales_register.py
│
├── register_sales()   → Handles user input and stores sales data
├── show_summary()     → Displays the final daily report
└── main()             → Entry point — runs the program

⚙️ How It Works
register_sales()

Initializes an empty sales dictionary and a daily_total of 0.
Asks the user for the product name, unit price, and quantity sold.
Calculates sale_total = price × quantity and adds it to daily_total.
If the product already exists in sales, it adds the quantity; otherwise it creates a new entry.
Repeats until the user answers no to registering another sale.
Returns sales and daily_total.

show_summary(sales, daily_total)

Receives the sales dictionary and the daily total.
Prints each product with its total quantity sold.
Displays the total amount collected formatted to 2 decimal places.

main()

Calls register_sales() to collect data.
Passes the results to show_summary() to display the report.

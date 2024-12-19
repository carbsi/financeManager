import csv
import matplotlib.pyplot as plt

# Save a CSV file of your transactions in the same folder as this project and put the name below
FILE = 'Safiirisiipi-FI5983117712939463-20241218.csv'

def plot_expenses_by_category(categories):
    labels = categories.keys()
    sizes = categories.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    plt.show()

#def categorize_expenses(transactions):
#    categories = {}
#    for _, name, amount in transactions:
#        name = name.strip().lower()  # Trim spaces and make lowercase
#        print(f"Processing: {name}, Amount: {amount}")  # Debugging line
#        if any(keyword in name for keyword in ["ruoka", "prisma", "kauppa", "k-market", "s-market", "KOLMIKULMA", "kolmikulma"]):
#            category = "Ruoka- ja paivittaisostokset"
#        if not name.strip():
#            continue  # Skip transactions with empty names
#        elif any(keyword in name for keyword in ["polttoaine", "neste", "st1"]):
#            category = "Polttoaineet"
#        elif any(keyword in name for keyword in ["servica", "compass", "anna"]):
#            category = "Lounasravintolat"
#        elif any(keyword in name for keyword in ["playtomic.io", "WWW.OPENPADEL.FI"]):
#            category = "Harrastukset"
#        else:
#            category = "Other"
#        print(f"Assigned Category: {category}")  # Debugging line
#        categories[category] = categories.get(category, 0) + abs(amount)
#    return categories
  
def export_to_csv(transactions, filename='processed_transactions.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Name", "Amount"])
        writer.writerows(transactions)
    print(f"Processed transactions saved to {filename}")

def summarize_expenses(categories):
    print("\nExpense Summary by Category:")
    for category, amount in categories.items():
        print(f"{category}: {round(amount, 2)} EUR")

def finance_manager(file):
    total_expenses = 0  # Initialize total expenses
    transactions = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')  # Using semicolon as the delimiter
        header = next(csv_reader)
        for row in csv_reader:
            #get date, class, class2, name, amount | Extracting fields (ensuring indices align with your data structure)
            date = row[0]
            class1 = row[1]  #
            class2 = row[2]  # 
            name = row[3]
            amount = float(row[4].replace(',', '.'))  # Replacing comma with period before conversion
            
            if amount < 0:  # Include only negative amounts
                total_expenses += amount
                transaction = (date, name.strip(), amount)  # Use only relevant fields
                transactions.append(transaction)
    print(f"The total of your expenses this month is {round(total_expenses, 2)} EUR")
    print(f"Total transactions: {len(transactions)}")
    
    print('')
    return transactions

# Passing the filename as a string | # Main execution
transactions = finance_manager(FILE)
for transaction in transactions:
    print(transaction)

# Categorize and visualize expenses
#categories = categorize_expenses(transactions)
#summarize_expenses(categories)
#plot_expenses_by_category(categories)

# Export processed transactions
export_to_csv(transactions)
# modules/visualization.py

import matplotlib.pyplot as plt

def radar_chart(data):
    """
    Create a radar chart.
    """
    # Radar chart implementation
    pass

def pie_chart(data):
    """
    Create a pie chart.
    """
    categories = data['category'].value_counts()
    plt.pie(categories, labels=categories.index, autopct='%1.1f%%')
    plt.title('Income vs Expenses')
    plt.show()

def subcategory_pie_chart(data):
    """
    Create a pie chart for subcategories.
    """
    subcategories = data['subcategory'].value_counts()
    plt.pie(subcategories, labels=subcategories.index, autopct='%1.1f%%')
    plt.title('Subcategory Distribution')
    plt.show()

def combined_pie_chart(data):
    """
    Create a pie chart for income, expenses, and subcategories, and display total income and total expense.
    """
    # Group data by category and subcategory, and sum the amounts
    subcategories = data.groupby(['category', 'subcategory'])['amount'].sum().reset_index()
    
    # Separate income and expenses
    income = subcategories[subcategories['amount'] > 0]
    expenses = subcategories[subcategories['amount'] < 0]
    
    # Calculate total income and total expense
    total_income = income['amount'].sum()
    total_expense = expenses['amount'].sum()
    
    # Take the absolute value of the amounts for pie chart
    subcategories['amount'] = subcategories['amount'].abs()
    
    # Create labels by combining category and subcategory, amount, and percentage
    labels = []
    for index, row in subcategories.iterrows():
        label = f"{row['category']} - {row['subcategory']}\n${row['amount']:,.2f} ({abs(row['amount']/subcategories['amount'].sum()*100):.2f}%)"
        labels.append(label)
    
    sizes = subcategories['amount']
    
    # Plotting the pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='', startangle=140)  # Remove autopct for values only
    
    # Add total income and total expense annotations with adjusted positions
    plt.text(-1.5, 1.1, f'Total Income: ${total_income:,.2f}', fontsize=12, color='green')
    plt.text(-1.5, 1.0, f'Total Expense: ${total_expense:,.2f}', fontsize=12, color='red')
    
    # Ensure equal aspect ratio for a circular pie chart
    plt.axis('equal')
    
    # Show the plot
    plt.show()

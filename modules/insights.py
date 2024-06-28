# modules/insights.py

def highlight_expenses(data):
    """
    Highlight new, sudden, or unwanted expenses.
    """
    # Implementation for highlighting expenses
    pass

def suggest_insights(data):
    """
    Suggest useful insights and trends.
    """
    # Implementation for suggesting insights
    pass

def subcategory_insights(data):
    """
    Provide insights based on subcategories.
    """
    subcategory_sums = data.groupby('subcategory')['amount'].sum().reset_index()
    largest_expenses = subcategory_sums[subcategory_sums['amount'] < 0].nsmallest(5, 'amount')
    largest_incomes = subcategory_sums[subcategory_sums['amount'] > 0].nlargest(5, 'amount')
    
    print("Top 5 Largest Expenses by Subcategory:")
    print(largest_expenses)
    print("\nTop 5 Largest Incomes by Subcategory:")
    print(largest_incomes)

# Financial Analyzer

Financial Analyzer is a Python application designed for managing and analyzing personal financial transactions. It provides functionalities to add transactions, categorize them, generate summaries, visualize data with charts, and gain insights into expenses and incomes.

## Features

- **Add Transactions:** Easily add new financial transactions with date, description, category, subcategory, and amount.
- **Categorization:** Transactions are categorized into income and expense categories with subcategory details.
- **Summaries:** Generate monthly and weekly summaries of expenses and incomes.
- **Visualization:** Visualize data with pie charts showing income vs expenses, subcategory distribution, and combined income-expense charts.
- **Insights:** Gain insights into largest expenses and incomes by subcategory.

## Project Structure

The project is structured as follows:

```
financial_analyzer/
│
├── main.py                 # Main script to run the application
│
├── modules/
│   ├── data_input.py       # Module for loading financial data
│   ├── data_processing.py  # Module for processing financial data
│   ├── insights.py         # Module for providing insights
│   ├── visualization.py    # Module for data visualization
│   └── ...                 # Other modules for specific functionalities
│
├── data/
│   ├── transactions.csv    # Sample CSV file for storing financial transactions
│   └── subcategories.csv   # CSV file for managing subcategories dynamically
│
├── README.md               # This file, providing an overview of the project
├── LICENSE                 # This file is for license
└── requirements.txt        # List of Python packages required by the project
```

## Getting Started

Follow these instructions to set up and run the Financial Analyzer application locally on your machine.

### Prerequisites

- Python 3.6 or higher
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:

```
git clone <repository_url>
cd financial_analyzer
```

2. Install dependencies:

```
pip install -r requirements.txt
```

### Usage

1. Run the application:

```
python main.py
```

2. Use the GUI to add transactions, analyze data, and visualize financial summaries.

### Configuration

- **Adding New Subcategories:** Modify `data/subcategories.csv` to add or remove subcategories for each category.

### Screenshots

Include screenshots of your application here, showcasing its various features and visualizations.

### Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

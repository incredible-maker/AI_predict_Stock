import yfinance as yf
import pandas as pd

def save_financial_data(ticker):
    stock = yf.Ticker(ticker)
    
    # Get income statement for the current year
    income_stmt = stock.get_income_stmt()
    
    # Filter columns for the previous year
    current_year = income_stmt.columns[0].year
    prev_year_income_stmt = income_stmt.iloc[:, income_stmt.columns.year == current_year - 1]
    
    # Get balance sheet for the current year
    balance_sheet = stock.balance_sheet
    
    # Filter columns for the previous year
    prev_year_balance_sheet = balance_sheet.iloc[:, balance_sheet.columns.year == current_year - 1]
    
    # Save income statement as Excel file
    income_stmt_file = f"{ticker}_income_statement.xlsx"
    with pd.ExcelWriter(income_stmt_file) as writer:
        income_stmt.to_excel(writer, sheet_name='Current Year')
        prev_year_income_stmt.to_excel(writer, sheet_name='Previous Year')
    
    # Save balance sheet as Excel file
    balance_sheet_file = f"{ticker}_balance_sheet.xlsx"
    with pd.ExcelWriter(balance_sheet_file) as writer:
        balance_sheet.to_excel(writer, sheet_name='Current Year')
        prev_year_balance_sheet.to_excel(writer, sheet_name='Previous Year')
    
    print(f"Income statement saved as {income_stmt_file}")
    print(f"Balance sheet saved as {balance_sheet_file}")
    
# Example usage
ticker_symbol = "TEMN.SW"
save_financial_data(ticker_symbol)

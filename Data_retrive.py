import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    print("Stock Info for", stock_info['symbol'])
    print("Company:", stock_info['longName'])
    print("Sector:", stock_info['sector'])
    print("Industry:", stock_info['industry'])
    print("Country:", stock_info['country'])
    print("Website:", stock_info['website'])
    
    while True:
        print("\nPlease select an indicator to view:")
        print("1. Historical Market Data")
        print("2. Dividends")
        print("3. Splits")
        print("4. Share Count")
        print("5. Income Statement")
        print("6. Balance Sheet")
        print("7. Cash Flow Statement")
        print("8. Major Holders")
        print("9. Institutional Holders")
        print("10. Earnings Dates")
        print("0. Exit")
        
        choice = input("Enter your choice (0-10): ")
        
        if choice == "0":
            break
        
        if choice == "1":
            hist = stock.history(period="1mo")
            print("\nHistorical Market Data:")
            print(hist)
        
        elif choice == "2":
            dividends = stock.dividends
            print("\nDividends:")
            print(dividends)
        
        elif choice == "3":
            splits = stock.splits
            print("\nSplits:")
            print(splits)
        
        elif choice == "4":
            shares = stock.get_shares_full(start="2023-01-01", end=None)
            print("\nShare Count:")
            print(shares)
        
        elif choice == "5":
            income_stmt = stock.income_stmt
            print("\nIncome Statement:")
            print(income_stmt)
        
        elif choice == "6":
            balance_sheet = stock.balance_sheet
            print("\nBalance Sheet:")
            print(balance_sheet)
        
        elif choice == "7":
            cashflow = stock.cashflow
            print("\nCash Flow Statement:")
            print(cashflow)
        
        elif choice == "8":
            major_holders = stock.major_holders
            print("\nMajor Holders:")
            print(major_holders)
        
        elif choice == "9":
            institutional_holders = stock.institutional_holders
            print("\nInstitutional Holders:")
            print(institutional_holders)
        
        elif choice == "10":
            earnings_dates = stock.earnings_dates
            print("\nEarnings Dates:")
            print(earnings_dates)
        
        else:
            print("Invalid choice. Please try again.")

# Example usage:
ticker_symbol = input("Enter the ticker symbol: ")
get_stock_info(ticker_symbol)

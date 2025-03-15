import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for BDC Investor Rankings
BDC_URL = "https://www.bdcinvestor.com/bdc-rankings"

def get_bdc_data():
    """Scrapes BDC data from BDCInvestor.com and returns a DataFrame"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(BDC_URL, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve data.")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Locate the data table (modify this if the site structure changes)
    table = soup.find("table", {"id": "bdc-rankings"})
    
    if not table:
        print("Error: Data table not found!")
        return None
    
    # Extract column headers
    headers = [th.text.strip() for th in table.find_all("th")]

    # Extract table rows
    data = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        cols = row.find_all("td")
        data.append([col.text.strip() for col in cols])

    # Create a DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Convert relevant columns to numeric
    df["Dividend Yield"] = df["Dividend Yield"].str.rstrip("%").astype(float) / 100
    df["NAV Premium/Discount"] = df["NAV Premium/Discount"].str.rstrip("%").astype(float) / 100
    df["Total Return (1Y)"] = df["Total Return (1Y)"].str.rstrip("%").astype(float) / 100
    df["EPS Growth (5Y)"] = df["EPS Growth (5Y)"].str.rstrip("%").astype(float) / 100

    return df

def select_top_bdcs(df):
    """Selects the top 5 BDCs based on long-term income criteria"""
    df["Income Score"] = (
        df["Dividend Yield"] * 0.5 +  # High yield (50% weight)
        (1 - abs(df["NAV Premium/Discount"])) * 0.2 +  # Low NAV premium/discount (20% weight)
        df["Total Return (1Y)"] * 0.2 +  # Strong total return (20% weight)
        df["EPS Growth (5Y)"] * 0.1  # Earnings growth (10% weight)
    )
    
    top_bdcs = df.sort_values(by="Income Score", ascending=False).head(5)
    return top_bdcs[["BDC Name", "Dividend Yield", "NAV Premium/Discount", "Total Return (1Y)", "EPS Growth (5Y)"]]

def main():
    print("Fetching BDC data from BDCInvestor.com...")
    df = get_bdc_data()

    if df is None:
        return

    print("\nTop 5 BDCs for Long-Term Income Portfolio:")
    top_bdcs = select_top_bdcs(df)
    print(top_bdcs.to_string(index=False))

if __name__ == "__main__":
    main()

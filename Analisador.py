# Requisitos: pip install yfinance pandas tabulate

import yfinance as yf
import pandas as pd
from tabulate import tabulate

def get_fundamentals(tickers):
    results = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info

        data = {
            "Ticker": ticker,
            "Nome": info.get("longName", "-"),
            "Setor": info.get("sector", "-"),
            "Preço Atual (R$)": round(info.get("currentPrice", 0), 2),
            "P/L": info.get("trailingPE", "-"),
            "ROE (%)": round(info.get("returnOnEquity", 0) * 100, 2) if info.get("returnOnEquity") else "-",
            "Dividend Yield (%)": round(info.get("dividendYield", 0) * 100, 2) if info.get("dividendYield") else "-",
            "Valor de Mercado (B)": round(info.get("marketCap", 0) / 1e9, 2) if info.get("marketCap") else "-"
        }

        results.append(data)

    return pd.DataFrame(results)

def main():
    print("Digite os tickers separados por vírgula (ex: PETR4.SA, VALE3.SA, ITUB4.SA):")
    entrada = input(">>> ")
    tickers = [t.strip().upper() for t in entrada.split(",")]

    print("\nBuscando dados...\n")
    df = get_fundamentals(tickers)

    if not df.empty:
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    else:
        print("Nenhuma informação encontrada.")

if __name__ == "__main__":
    main()

# Multi-Country Currency Converter (CLI)

A simple Python-based currency converter that fetches **live exchange rates** using OANDA’s public API.  
Supports **all global currencies** (e.g., USD, INR, JPY, EUR, etc.).

## Features
- Convert any currency to another using real-time data  
- Handles incorrect input and invalid currency codes  
- Displays clean, readable output  
- Uses Python’s `requests` and `datetime` modules  

## How It Works
1. Prompts user for:
   - Base currency (e.g., `USD`)
   - Target currency (e.g., `INR`)
   - Amount to convert  
2. Fetches the latest rate using an API call  
3. Calculates and prints the converted value  
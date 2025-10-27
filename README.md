# Colombo Stock Exchange (CSE) API 📈🏢

> **Unofficial API usage guide & Python example 🐍**  
> Explore stock market data from the Colombo Stock Exchange (CSE) via their public API endpoints — reverse-engineered since no official documentation exists. 🔍

---

<b>Visit <a href='https://gh0sth4cker.github.io/Colombo-Stock-Exchange-CSE-API-Documentation/'>this link</a> to see web view<b>

## Overview 📋

The Colombo Stock Exchange provides real-time and historical stock data via several public endpoints used by their web portal.  
This repository documents some of the known API endpoints, example responses, and Python code to fetch and parse data.

---

## API Endpoints 🔗

Base URL: `https://www.cse.lk/api/`

| Endpoint                                  | Description                                        | HTTP Method | Required Params/Data                  |
| ----------------------------------------- | -------------------------------------------------- | ----------- | ------------------------------------ |
| companyInfoSummery                        | Detailed info of a single stock/security by symbol | POST        | symbol                               |
| tradeSummary                              | Summary of trades for all securities               | POST        |                                      |
| todaySharePrice                           | Today's share price data                           | POST        | symbol                               |
| topGainers                                | List of top gaining stocks                         | POST        |                                      |
| topLooses                                 | List of top losing stocks                          | POST        |                                      |
| mostActiveTrades                          | Most active trades by volume                       | POST        |                                      |
| getNewListingsRelatedNoticesAnnouncements | New listings and related announcements             | POST        |                                      |
| getBuyInBoardAnnouncements                | Buy-in board announcements                         | POST        |                                      |
| approvedAnnouncement                      | Approved announcements                             | POST        |                                      |
| getCOVIDAnnouncements                     | COVID-related announcements                        | POST        |                                      |
| getFinancialAnnouncement                  | Financial announcements                            | POST        |                                      |
| circularAnnouncement                      | Circular announcements                             | POST        |                                      |
| directiveAnnouncement                     | Directive announcements                             | POST        |                                      |
| getNonComplianceAnnouncements             | Non-compliance announcements                       | POST        |                                      |
| marketStatus                              | Market open/close status                           | POST        |                                      |
| marketSummery                             | Market summary data                                | POST        |                                      |
| aspiData                                  | All Share Price Index data                         | POST        |                                      |
| snpData                                   | S&P Sri Lanka 20 Index data                        | POST        |                                      |
| chartData                                 | Chart data for stocks                              | POST        | symbol, chartId, period              |
| allSectors                                | Data for all sectors                               | POST        |                                      |
| detailedTrades                            | Detailed Trades                                    | POST        |                                      |
| dailyMarketSummery                        | Daily Market Summary                               | POST        |                                      |


---

visit <a href='https://github.com/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation/blob/main/api_endpoint_urls.txt'>this link</a> to view all complete endpoint urls.

## Usage Example 💻python

### Get detailed stock info by symbol 🔍

```python
import requests

base_url = "https://www.cse.lk/api/"
endpoint = "companyInfoSummery"

data = {"symbol": "LOLC.N0000"}

response = requests.post(base_url + endpoint, data=data)

print(f"Status code: {response.status_code}")
print(response.json())  # Prints the response as a Python dictionary
```

---

## Sample Response: `companyInfoSummery` 📝

```json
{
  "reqSymbolInfo": {
    "symbol": "LOLC.N0000",
    "name": "L O L C HOLDINGS PLC",
    "lastTradedPrice": 546.5,
    "change": -2.5,
    "changePercentage": -0.455,
    "marketCap": 259696800000
  },
  "reqLogo": {
    "id": 2168,
    "path": "upload_logo/378_1601611239.jpeg"
  },
  "reqSymbolBetaInfo": {
    "betaValueSPSL": 1.0227
  }
}
```

---

## Contribution 🤝

This is an **unofficial** reverse-engineered API.  
If you discover more endpoints or useful parameters, please submit a **Pull Request**!  
Help expand the community knowledge about the Colombo Stock Exchange API. 🚀
<br>
[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=FB9KXK4TEAUJ6)

---

## Disclaimer ⚠️

- Use responsibly and verify data accuracy with official CSE sources.
- API endpoints and formats may change without notice.
- This repository is for educational purposes only.

---

[![Stargazers repo roster for @GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation](https://reporoster.com/stars/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation)](https://github.com/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation/stargazers)

[![Forkers repo roster for @GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation](https://reporoster.com/forks/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation)](https://github.com/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation/network/members)

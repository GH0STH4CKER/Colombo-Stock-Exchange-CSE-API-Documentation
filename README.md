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

Only public, read-only market data endpoints are documented here (no login required).

### Request formats 📨

| Body | Content-Type | Python `requests` |
| ---- | ------------ | ----------------- |
| form-urlencoded | `application/x-www-form-urlencoded` | `requests.post(url, data={...})` |
| multipart/form-data | `multipart/form-data` | `requests.post(url, data={...})` also works |
| JSON | `application/json` | `requests.post(url, json={...})` |
| query string | (GET) | `requests.get(url, params={...})` |

- Endpoints without parameters accept an empty `POST` (or `GET`).
- Endpoints the website calls with multipart also accept form-urlencoded. Only `boardReason`, `smd` and `debtDetailTrades` need a JSON body.
- Logo paths (`logoUrl`, `reqLogo.path`) are relative to `https://cdn.cse.lk/cmt/`. Report / PDF paths are relative to `https://cdn.cse.lk/`.

### Market Overview

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `marketStatus` | POST | form-urlencoded | — | Market open/close status (e.g. `Regular Trading`, `Market Closed`) |
| `marketSummery` | POST | form-urlencoded | — | Market summary for the day (turnover, share volume, trades) |
| `dailyMarketSummery` | POST | form-urlencoded | — | Daily market summary (turnover, foreign/domestic split, PER, PBV, DY, indices) |
| `lastUpdateTime` 🆕 | GET | query string | — | Timestamp of the last market data update |
| `previousUpdateTime` 🆕 | GET | query string | — | Previous trading date |
| `cseDaily` 🆕 | POST | form-urlencoded | — | CSE daily market reports (PDF paths on cdn.cse.lk) |
| `cseDailyNew` 🆕 | GET | query string | — | Latest CSE daily market report |
| `cseWeekly` 🆕 | POST | form-urlencoded | — | CSE weekly market reports |
| `cseMonthly` 🆕 | POST | form-urlencoded | — | Latest CSE monthly market report |
| `quarterlySummary` 🆕 | POST | form-urlencoded | — | CSE quarterly market reports |

### Securities & Trades

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `companyInfoSummery` | POST | form-urlencoded | `symbol` | Detailed info of a single stock/security by symbol |
| `homeCompanyData` 🆕 | POST | multipart/form-data | `symbol` | Price snapshot of one security. The returned `id` is the `stockId` used by `companyChartDataByStock` |
| `tradeSummary` | POST | form-urlencoded | — | Summary of trades for all securities |
| `todaySharePrice` | POST | form-urlencoded | — | Today's share price data |
| `detailedTrades` | POST | form-urlencoded | `symbol` (optional) | Detailed trades for all (or one) security |
| `topGainers` | POST | form-urlencoded | — | Top gaining stocks |
| `topLooses` | POST | form-urlencoded | — | Top losing stocks |
| `mostActiveTrades` | POST | form-urlencoded | — | Most active trades |
| `mostActiveVolumes` 🆕 | POST | form-urlencoded | — | Most active securities by share volume |
| `mostActiveVolPercentage` 🆕 | POST | form-urlencoded | — | Most active securities by volume percentage |
| `chartData` | POST | form-urlencoded | `symbol`, `chartId`, `period` | Price chart points for a stock |
| `companyChartDataByStock` | POST | form-urlencoded | `stockId`, `period` (`1` = intraday) | OHLC / trade chart data for a stock |
| `list_by_market_cap` 🆕 | POST | form-urlencoded | — | All securities ranked by market capitalisation |
| `cntSecurity` 🆕 | GET | query string | — | All securities with id, symbol and board id |
| `allSecurityCode` 🆕 | GET | query string | — | All security codes with id and active flag |
| `dailyShortSellTradeSummary` 🆕 | GET | query string | `date` (optional, `YYYY-MM-DD`) | Daily short-sell trade summary |
| `sblBorrowingPool` 🆕 | GET | query string | `security` (`ALL` or symbol) | Securities borrowing & lending: borrowing pool |
| `sblLendingPool` 🆕 | GET | query string | `security` (`ALL` or symbol) | Securities borrowing & lending: lending pool |

### Trading Statistics

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `alphabetical` 🆕 | POST | multipart/form-data | `alphabet` (e.g. `A`) | Trading statistics for securities starting with a letter |
| `list_by_type` 🆕 | POST | multipart/form-data | `type` (e.g. `N`) | Trading statistics by issue type |

### Indices

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `aspiData` | POST | form-urlencoded | — | All Share Price Index (ASPI) value |
| `snpData` | POST | form-urlencoded | — | S&P Sri Lanka 20 index value |
| `aspi` 🆕 | POST | form-urlencoded | — | ASPI constituents with price / turnover |
| `aspi/year` 🆕 | POST | form-urlencoded | — | Year-to-date ASPI, S&P SL20 and total-return values |
| `spsl` 🆕 | POST | form-urlencoded | `indexType` (optional) | S&P SL20 constituents |
| `marketIndices` 🆕 | POST | form-urlencoded | — | All sector / market indices |
| `return_indices` 🆕 | POST | form-urlencoded | — | Total return indices (TRI) for market and sectors |
| `returnAspiSnp` 🆕 | GET | query string | — | ASPI / S&P SL20 return status flag |
| `getContributors` 🆕 | POST | form-urlencoded | — | Count of positive / negative ASPI contributors |
| `getContributorsChart` 🆕 | POST | form-urlencoded | — | Top contributors to ASPI |

### Sectors & GICS

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `allSectors` | POST | form-urlencoded | — | Data for all sectors |
| `listAllSectors` 🆕 | POST | form-urlencoded | — | List of all sector indices |
| `sector_list` 🆕 | POST | form-urlencoded | — | Sector index list (GET also works) |
| `listBySector` 🆕 | POST | multipart/form-data | `sectorId` (integer) | Companies in a sector, with trading data |
| `52WeekSectors` 🆕 | POST | form-urlencoded | `sectorId` (query string) | 52-week / YTD high and change for a sector, e.g. `52WeekSectors?sectorId=1` |
| `sectorHighLow` 🆕 | POST | form-urlencoded | `sectorId` (query string) | Daily open / high / low for a sector, e.g. `sectorHighLow?sectorId=1` |
| `GICSSectors` 🆕 | POST | form-urlencoded | — | GICS sectors |
| `GICSSectorSummery` 🆕 | POST | form-urlencoded | — | GICS industry group summary (PER, PBV, turnover) |
| `GICSIndustryGroup` 🆕 | POST | multipart/form-data | `sectorId` | GICS industry groups in a GICS sector |
| `gics_sector_companies` 🆕 | POST | multipart/form-data | `sectorId`, `industryGroupId` | Companies in a GICS industry group |

### Listed Entities & Boards

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `main_boards` 🆕 | POST | form-urlencoded | — | Companies on the Main Board |
| `secondBoard` 🆕 | POST | form-urlencoded | — | Companies on the Second Board |
| `divi_siri_board` 🆕 | POST | form-urlencoded | — | Companies on the Diri Savi Board |
| `empower_boards` 🆕 | POST | form-urlencoded | — | Companies on the Empower Board |
| `default_board` 🆕 | POST | form-urlencoded | — | Companies on the Watch List (default board) |
| `boardReason` 🆕 | POST | JSON | `symbole` (sic) | Reason a security is on its board |
| `listedEntitiesByTradingStatus` 🆕 | GET | query string | `tradingStatus` (`TS` = suspended, `TH` = halted) | Suspended / halted securities |
| `deListedEntities` 🆕 | GET | query string | — | De-listed entities |
| `investorCompanies` 🆕 | GET | query string | — | Investor relations companies and their advisors |
| `getAllIssuers` 🆕 | POST | form-urlencoded | — | All debt issuers |
| `upcomingListings` 🆕 | GET | query string | `newListingType` (`P` = primary, `S` = secondary) | Upcoming listings / IPOs |

### Debt Market

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `debtTrades` 🆕 | POST | form-urlencoded | — | Listed debt securities and trades |
| `debtDetailTrades` 🆕 | POST | JSON | — | Debt market detailed trades |

### Announcements & Disclosures

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `approvedAnnouncement` | POST | form-urlencoded | — | Approved announcements |
| `getFinancialAnnouncement` | POST | form-urlencoded | `companyIds`, `fromDate`, `toDate` (all optional) | Financial announcements |
| `getNewListingsRelatedNoticesAnnouncements` | POST | form-urlencoded | — | New listings and related announcements |
| `getBuyInBoardAnnouncements` | POST | form-urlencoded | — | Buy-in board announcements |
| `getCOVIDAnnouncements` | POST | form-urlencoded | — | COVID-related announcements |
| `getNonComplianceAnnouncements` | POST | form-urlencoded | — | Non-compliance announcements |
| `circularAnnouncement` | POST | form-urlencoded | — | Circular announcements |
| `directiveAnnouncement` | POST | form-urlencoded | — | Directive announcements |
| `corporateAnnouncementCategory` 🆕 | GET | query string | — | Corporate announcement categories |
| `getAnnouncementById` 🆕 | POST | form-urlencoded | `announcementId` (from `approvedAnnouncement`) | Full details of an approved announcement |
| `getGeneralAnnouncementById` 🆕 | POST | form-urlencoded | `announcementId` (from the announcement lists) | Full details of a general announcement |
| `smd` 🆕 | POST | JSON | `allCategories`, `allCompanies`, `companyIds`, `categories`, `fromDate`, `toDate` | Stock market disclosures, grouped by category |
| `smd/categories` 🆕 | GET | query string | — | SMD category names |
| `corporateCalender` 🆕 | POST | form-urlencoded | `year`, `month` | Corporate action calendar |
| `getAgmEgmEvents` 🆕 | POST | form-urlencoded | `year`, `month` | AGM / EGM events |
| `cseCircular` 🆕 | POST | multipart/form-data | `year`, `type` (optional) | CSE circulars for a year |
| `secDirective` 🆕 | POST | multipart/form-data | `year` | SEC directives for a year |
| `ruleBooks/web/list` 🆕 | GET | query string | `ruleType` | Rule books grouped by heading, e.g. `ruleBooks/web/list?ruleType=1` |

### News, Events & Content

| Endpoint | Method | Body | Params | Description |
| -------- | ------ | ---- | ------ | ----------- |
| `news/web` 🆕 | GET | query string | `top`, `type` (`CN` / `BN` / `MR`), `year`, `security`, `numberOfRecord` | News (CN = CSE news, BN = company news, MR = market reviews) |
| `events` 🆕 | GET | query string | `eventType`, `year` | Events grouped by month |
| `events/top` 🆕 | GET | query string | `top`, `year`, `numberOfRecord` | Latest events |
| `events/{id}` 🆕 | GET | query string | `id` in the path (from `events`) | Single event with body and images |
| `banners` 🆕 | GET | query string | `type`, `category` | Website banners |
| `branchOffices` 🆕 | GET | query string | — | Broker branch offices |
| `careers` 🆕 | GET | query string | — | CSE career vacancies |
| `members` 🆕 | GET | query string | — | Member firms |
| `tradingMembers` 🆕 | GET | query string | — | Trading members |
| `localSeminars` 🆕 | GET | query string | — | Investor education seminars |
| `local/courses` 🆕 | GET | query string | — | CSE Academy courses |
| `educationalVideos` 🆕 | GET | query string | — | Educational videos |

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

### Get a price snapshot, then the intraday chart 📊

```python
import requests

base_url = "https://www.cse.lk/api/"

snap = requests.post(base_url + "homeCompanyData", data={"symbol": "LOLC.N0000"}).json()
print(snap)  # {'id': 0, 'symbol': 'XXXX.N0000', 'price': 0.0, ...}

chart = requests.post(base_url + "companyChartDataByStock",
                      data={"stockId": snap["id"], "period": 1}).json()
print(len(chart["chartData"]), "points")
```

### GET endpoints with query parameters 🔎

```python
import requests

news = requests.get("https://www.cse.lk/api/news/web",
                    params={"top": "true", "type": "CN", "numberOfRecord": 3}).json()
for item in news["CN"]:
    print(item["publishedDate"], item["title"])
```

---

## Sample Response: `companyInfoSummery` 📝

Values are placeholders; only the structure of the response is shown.

```json
{
  "reqSymbolInfo": {
    "symbol": "XXXX.N0000",
    "name": "<name>",
    "lastTradedPrice": 0.0,
    "change": 0.0,
    "changePercentage": 0.0,
    "marketCap": 0
  },
  "reqLogo": {
    "id": 0,
    "path": "upload_logo/<file>.jpeg"
  },
  "reqSymbolBetaInfo": {
    "betaValueSPSL": 0.0
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

> This project is unofficial and not affiliated with or endorsed by the Colombo Stock Exchange. All data returned by these endpoints is the property of CSE and is subject to the [CSE Terms of Use](https://www.cse.lk/disclaimer): personal, non-commercial use only. Any commercial use, redistribution or republication of CSE data requires prior written permission from CSE. Keep request volumes low; CSE may block abusive IP addresses.

- Use responsibly and verify data accuracy with official CSE sources.
- API endpoints and formats may change without notice.
- This repository is for educational purposes only.

---

[![Stargazers repo roster for @GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation](https://reporoster.com/stars/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation)](https://github.com/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation/stargazers)

[![Forkers repo roster for @GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation](https://reporoster.com/forks/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation)](https://github.com/GH0STH4CKER/Colombo-Stock-Exchange-CSE-API-Documentation/network/members)

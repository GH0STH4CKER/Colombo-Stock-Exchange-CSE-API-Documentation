import requests
import urllib.parse
from datetime import datetime

# ==========================================
# CSE API: Financial Reports Archive Downloader
# ==========================================
# Endpoint: /api/financials
# Method: POST
#
# Description:
#   Retrieves a categorized list of PDF documents (Annual Reports, 
#   Quarterly Reports, Prospectuses) for a specific company.
#   It returns file paths which must be appended to the CSE CDN URL.
#
# Required Parameters (Form Data):
#   - symbol: The stock symbol (e.g., "SAMP.N0000")
#
# Required Headers:
#   - Origin: https://www.cse.lk
#   - Referer: https://www.cse.lk/company-profile?symbol={symbol}
#   - Content-Type: application/x-www-form-urlencoded
# ==========================================

BASE_URL = "https://www.cse.lk/api/financials"
CDN_BASE = "https://cdn.cse.lk/"

def format_date(timestamp_ms):
    """Helper to convert CSE epoch milliseconds to readable date."""
    if not timestamp_ms:
        return "Unknown Date"
    try:
        return datetime.fromtimestamp(timestamp_ms / 1000.0).strftime('%Y-%m-%d')
    except:
        return str(timestamp_ms)

def generate_cdn_link(raw_path):
    """
    Generates a valid download link by fixing common API path inconsistencies.
    
    Fixes handled:
    1. Legacy Paths: Files from ~2012-2018 often miss the 'cmt/' root folder in the API response.
    2. URL Encoding: Filenames with spaces (e.g., 'Report (Final).pdf') are encoded to be browser-safe.
    """
    if not raw_path:
        return None

    # Fix: The CDN requires the 'cmt/' prefix, but older API records often exclude it.
    # If we don't add this, links return 403 Access Denied.
    if not raw_path.startswith("cmt/"):
        raw_path = f"cmt/{raw_path}"

    # Fix: Encode special characters (like spaces) but keep slashes '/' intact.
    safe_path = urllib.parse.quote(raw_path, safe='/')
    
    return f"{CDN_BASE}{safe_path}"

def get_financial_archives(symbol):
    """
    Fetches and prints all available financial documents for a given symbol.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://www.cse.lk",
        "Referer": f"https://www.cse.lk/company-profile?symbol={symbol}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    print(f"📡 Fetching Financial Archive for {symbol}...")
    
    try:
        # Note: Data is sent as form-encoded, not JSON
        response = requests.post(BASE_URL, headers=headers, data={"symbol": symbol})
        response.raise_for_status()
        
        data = response.json()
        
        # --- 1. Annual Reports ---
        annuals = data.get('infoAnnualData', [])
        print(f"\n📚 ANNUAL REPORTS ({len(annuals)} found)")
        print("=" * 80)
        
        for report in annuals:
            date_str = format_date(report.get('manualDate'))
            title = report.get('fileText', 'Untitled')
            link = generate_cdn_link(report.get('path'))
            print(f"[{date_str}] {title}")
            print(f"🔗 {link}\n")

        # --- 2. Quarterly Reports ---
        quarterly = data.get('infoQuarterlyData', [])
        print(f"\n📊 QUARTERLY REPORTS ({len(quarterly)} found)")
        print("=" * 80)
        
        for report in quarterly:
            date_str = format_date(report.get('manualDate'))
            title = report.get('fileText', 'Untitled')
            link = generate_cdn_link(report.get('path'))
            print(f"[{date_str}] {title}")
            print(f"🔗 {link}\n")
            
        # --- 3. Other Documents (Prospectuses, Trust Deeds, etc.) ---
        others = data.get('infoOtherData', [])
        if others:
            print(f"\n📂 LEGAL & OTHER DOCUMENTS ({len(others)} found)")
            print("=" * 80)
            for report in others:
                date_str = format_date(report.get('manualDate'))
                title = report.get('fileText', 'Untitled')
                link = generate_cdn_link(report.get('path'))
                print(f"[{date_str}] {title}")
                print(f"🔗 {link}\n")

    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {e}")
    except Exception as e:
        print(f"❌ Error parsing data: {e}")

if __name__ == "__main__":
    # Example usage
    target_symbol = "SAMP.N0000"
    get_financial_archives(target_symbol)

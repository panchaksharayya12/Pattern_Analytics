"""
Supabase Integration Client for Pattern Analytics.
Provides connection management, query helpers, and transparent local CSV fallback.
"""

import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

_supabase_client = None

def get_supabase_client():
    """
    Initializes and returns the Supabase client instance if credentials exist.
    Returns None if credentials are not configured or package is unavailable.
    """
    global _supabase_client
    if _supabase_client is not None:
        return _supabase_client

    if not SUPABASE_URL or not SUPABASE_KEY or SUPABASE_URL == "https://your-project-id.supabase.co":
        return None

    try:
        from supabase import create_client, Client
        _supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return _supabase_client
    except Exception as e:
        print(f"[Supabase Client Warning] Failed to initialize Supabase client: {e}")
        return None


def fetch_customer_data(table_name="european_bank_customers", use_fallback=True):
    """
    Fetches customer records from Supabase table.
    Falls back to local data/European_Bank.csv if Supabase is offline or unconfigured.
    """
    client = get_supabase_client()
    if client:
        try:
            response = client.table(table_name).select("*").execute()
            if response.data:
                return pd.DataFrame(response.data)
        except Exception as e:
            print(f"[Supabase Client Warning] Query failed: {e}. Attempting local fallback.")

    if use_fallback:
        csv_path = BASE_DIR / "data" / "European_Bank.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        else:
            raise FileNotFoundError(f"Customer dataset not found at {csv_path}")

    return pd.DataFrame()

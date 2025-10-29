import pandas as pd
from pathlib import Path

# ===========================================================
# 🧩 CSV → Excel converter (simple version)
# -----------------------------------------------------------
# This script converts a CSV file into an Excel (.xlsx) file
# using pandas.
#
# ✅ Safe & shareable version:
# - Uses anonymized and relative paths
# - Keeps the original logic identical to your version
# - Includes English comments for documentation
# ===========================================================

# === File paths (anonymized and relative) ===
csv_file = Path("data/input.csv")        # Path to the input CSV file
excel_file = Path("output/output.xlsx")  # Path for the generated Excel file

# Ensure that the output directory exists
excel_file.parent.mkdir(parents=True, exist_ok=True)

# === CSV reading parameters ===
DELIMITER = ";"          # Change this to "," or "\t" depending on your file
ENCODING = "utf-8-sig"   # You can switch to "latin-1" if you encounter encoding errors

try:
    print("Loading CSV file...")

    # Read the CSV using pandas
    # The delimiter must match the one used in your file
    df = pd.read_csv(csv_file, delimiter=DELIMITER, encoding=ENCODING)

    print("Converting to Excel format...")

    # Export the DataFrame to Excel
    # index=False avoids adding the DataFrame index as a new column
    df.to_excel(excel_file, index=False)

    print(f"✅ Conversion completed successfully! File saved as: {excel_file}")

# === Error handling ===
except FileNotFoundError:
    # The CSV file path does not exist
    print(f"❌ Error: File not found. Please check the path: {csv_file}")

except pd.errors.ParserError as e:
    # pandas could not parse the CSV properly (bad delimiter, malformed rows, etc.)
    print("❌ Parsing error: The CSV file may contain formatting issues.")
    print(f"Details: {e}")

except Exception as e:
    # Generic catch-all for unexpected exceptions
    print(f"⚠️  Unexpected error during conversion: {e}")

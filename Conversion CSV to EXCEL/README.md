# 🐍 CSV → Excel Converter (pandas)
Small, reusable Python utility to convert **CSV** files to **Excel (.xlsx)** with sensible defaults, automatic delimiter detection, and basic formatting.

> ✅ **Anonymization note:** This project uses **generic, relative paths** (e.g., `data/input.csv`, `output/output.xlsx`).  
> Do **not** commit personal directories, usernames, or confidential file names. Replace any sensitive values before sharing.

---

## ✨ Features
- Auto-detects CSV **delimiter** (`,` `;` `\t`) when not provided
- Handles common **encodings** (`utf-8`, `utf-8-sig` → fallback to `latin-1`)
- Optional **sheet name**, **NA values**, **decimal** and **thousand** separators
- Basic Excel formatting: autosizes columns based on sample rows
- Friendly CLI with clear errors

---

## 📦 Installation
```bash
# Python 3.9+ recommended
pip install pandas openpyxl
```
*(No external dependencies like `chardet` are required.)*

---

## 🚀 Usage
```bash
python csv_to_excel.py data/input.csv output/output.xlsx
```

### Options
```bash
python csv_to_excel.py INPUT OUTPUT [options]

Options:
  --delimiter DELIM       CSV delimiter (default: auto-detect)
  --encoding ENC          File encoding (default: utf-8-sig → latin-1 fallback)
  --sheet-name NAME       Excel sheet name (default: "data")
  --na-values A,B,C       Extra strings to treat as NA (comma-separated)
  --decimal CHAR          Decimal separator (default: .)
  --thousands CHAR        Thousands separator (default: none)
  --no-header             Treat CSV as having no header row
  --keep-index            Keep DataFrame index in Excel
  --max-rows N            Only read first N rows (useful for testing)
  -v, --verbose           Verbose output
```

---

## 🧱 Project Layout (suggested)
```
.
├── csv_to_excel.py
├── README.md
├── data/                 # put your CSVs here (DO NOT commit confidential data)
└── output/               # converted .xlsx files (can be gitignored)
```


## 🪪 License
Released under the **MIT License**. Feel free to reuse and adapt.

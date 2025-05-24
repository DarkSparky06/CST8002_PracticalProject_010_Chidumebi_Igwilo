"""
data_processor.py
Author: Igwilo Chidumebi
Course: CST8002 010
Description: Loads dataset and returns list of Record objects.
"""

import csv
from record import Record

def load_records(file_path: str):
    """Read CSV and return list of Record instances."""
    records = []
    try:
        with open(file_path, newline='', encoding='cp1252') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rec = Record(
                    sample_no=row['Sample No. – No. d’échantillon'],
                    region=row['Region - Région'],
                    function=row['Function'],
                    origin=row['Origin'],
                    product=row['Product']
                )
                records.append(rec)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print("Unexpected error:", e)
        exit(1)
    return records

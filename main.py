"""
main.py
Author: Igwilo Chidumebi
Course: CST8002 010
Description: Entry point for data-processing application.
"""

from data_processor import load_records
from stats_api import get_average

def main():
    # Load and display first 5 records
    records = load_records('dataset.csv')
    for rec in records[:5]:
        print(f"{rec.sample_no} - {rec.region}")
    # Display author info
    print("Igwilo Chidumebi, CST8002 010")
    # Compute and display average (using 'product' numeric field for demo)
    try:
        values = [float(rec.product) for rec in records]
        avg = get_average(values)
        print(f"Average Value: {avg}")
    except ValueError:
        print("Could not convert product values to float for averaging.")

if __name__ == "__main__":
    main()

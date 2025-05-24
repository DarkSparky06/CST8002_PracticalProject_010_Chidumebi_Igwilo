"""
record.py
Author: Igwilo Chidumebi
Course: CST8002 010
Description: Defines the Record data class matching the real CSV headers with Pythonic names.
"""

from dataclasses import dataclass

@dataclass
class Record:
    sample_no: str   # maps 'Sample No. – No. d’échantillon'
    region: str      # maps 'Region - Région'
    function: str    # maps 'Function'
    origin: str      # maps 'Origin'
    product: str     # maps 'Product'

"""
Date normalizer plugin for Pelican.
Handles single-digit minutes in date formats.
"""

import re
from pelican import signals
from pelican.readers import BaseReader


def normalize_date_in_metadata(content_object):
    """
    Normalize date format to handle single-digit minutes.
    Converts dates like "25-8-2025 21:3" to "25-8-2025 21:03"
    """
    if hasattr(content_object, 'metadata') and 'date' in content_object.metadata:
        date_str = str(content_object.metadata['date'])
        
        # Pattern to match date with single-digit minute
        # Matches: "DD-M-YYYY HH:M" or "D-MM-YYYY HH:M" etc.
        pattern = r'(\d{1,2}-\d{1,2}-\d{4} \d{1,2}):(\d{1})$'
        match = re.search(pattern, date_str)
        
        if match:
            # Add leading zero to single-digit minute
            normalized_date = f"{match.group(1)}:0{match.group(2)}"
            content_object.metadata['date'] = normalized_date


def register():
    """Register the plugin with Pelican."""
    signals.content_object_init.connect(normalize_date_in_metadata)

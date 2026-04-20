"""
Streamlit entry point for Quran Semantic Search

Run with: streamlit run streamlit_app.py
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from quran_search.app import main

if __name__ == "__main__":
    main()

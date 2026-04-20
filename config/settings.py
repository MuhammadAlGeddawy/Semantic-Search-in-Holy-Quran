"""
Configuration settings for Quran Semantic Search

Author: Muhammad Al-Geddawy
"""

import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
MODEL_V1_DIR = MODELS_DIR / "v1"

# Model configuration
DEFAULT_MODEL_DIR = str(MODEL_V1_DIR)
DEFAULT_MODEL_NAME = "multilingual-e5-large"

# Search parameters
DEFAULT_TOP_K = 5
MAX_TOP_K = 20

# FAISS configuration
FAISS_INDEX_FILE = MODEL_V1_DIR / "quran_index.faiss"
FAISS_EMBEDDINGS_FILE = MODEL_V1_DIR / "quran_embeddings.npy"

# Verses data
VERSES_CSV_FILE = MODEL_V1_DIR / "quran_verses.csv"
CONFIG_FILE = MODEL_V1_DIR / "config.json"

# Text normalization
ARABIC_DIACRITICS_PATTERN = r"""
    ّ    | # Tashdid
    َ    | # Fatha
    ً    | # Tanwin Fath
    ُ    | # Damma
    ٌ    | # Tanwin Damm
    ِ    | # Kasra
    ٍ    | # Tanwin Kasr
    ْ    | # Sukun
    ـ     # Tatwil/Kashida
"""

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Feature flags
ENABLE_TAFSEER = False  # V2 feature
ENABLE_HYBRID_SEARCH = False  # V2 feature
ENABLE_ONTOLOGY = False  # V3 feature

"""
Quran Semantic Search - Production Package

A comprehensive semantic search engine for the Holy Quran using Arabic embeddings
and FAISS-powered vector search.

Version: 1.0
Author: Muhammad Al-Geddawy
"""

__version__ = "1.0.0"
__author__ = "Muhammad Al-Geddawy"
__email__ = "muhammad.anwar@ejust.edu.eg"

from .search_engine import SemanticSearchEngine

__all__ = ["SemanticSearchEngine"]

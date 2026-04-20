"""
Core Semantic Search Engine for Quran

This module contains the main search logic with FAISS integration.

Author: Muhammad Al-Geddawy
"""

import json
import re
from typing import List, Dict, Tuple
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


class SemanticSearchEngine:
    """Main semantic search engine for Quranic verses."""
    
    def __init__(self, model_dir: str = "models/v1"):
        """
        Initialize the search engine.
        
        Args:
            model_dir: Path to directory containing model artifacts
        """
        self.model_dir = model_dir
        self.model = None
        self.index = None
        self.verses_df = None
        self.config = None
        
        self._load_artifacts()
    
    def _load_artifacts(self):
        """Load model, index, and data."""
        # Load config
        with open(f"{self.model_dir}/config.json", 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        # Load model
        self.model = SentenceTransformer(self.config['model_path'])
        
        # Load FAISS index
        self.index = faiss.read_index(f"{self.model_dir}/quran_index.faiss")
        
        # Load verses dataframe
        self.verses_df = pd.read_csv(f"{self.model_dir}/quran_verses.csv")
    
    @staticmethod
    def normalize_arabic(text: str) -> str:
        """
        Normalize Arabic text by removing diacritics and standardizing characters.
        
        Args:
            text: Input text
            
        Returns:
            Normalized text
        """
        if pd.isna(text) or text is None:
            return ""
        
        # Remove Arabic diacritics
        arabic_diacritics = re.compile(r"""
            ّ    | # Tashdid
            َ    | # Fatha
            ً    | # Tanwin Fath
            ُ    | # Damma
            ٌ    | # Tanwin Damm
            ِ    | # Kasra
            ٍ    | # Tanwin Kasr
            ْ    | # Sukun
            ـ     # Tatwil/Kashida
        """, re.VERBOSE)
        
        text = re.sub(arabic_diacritics, '', text)
        text = re.sub(r"[إأآا]", "ا", text)
        text = text.replace("ى", "ي")
        text = text.replace("ة", "ه")
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def search(self, query: str, top_k: int = 10) -> List[Dict]:
        """
        Perform semantic search on Quranic verses.
        
        Args:
            query: Search query (Arabic or English)
            top_k: Number of results to return
            
        Returns:
            List of result dictionaries with verse info and similarity scores
        """
        # Normalize query if Arabic
        is_arabic = any('\u0600' <= c <= '\u06FF' for c in query)
        query_normalized = self.normalize_arabic(query) if is_arabic else query
        
        # Encode query
        query_embedding = self.model.encode(
            [query_normalized],
            convert_to_numpy=True
        ).astype('float32')
        
        # Search FAISS index
        distances, indices = self.index.search(query_embedding, top_k)
        
        # Prepare results
        results = []
        for rank, (idx, distance) in enumerate(zip(indices[0], distances[0]), start=1):
            if idx == -1:
                continue
            
            verse = self.verses_df.iloc[idx]
            similarity = 1 / (1 + distance)
            
            results.append({
                'rank': rank,
                'surah': int(verse['surah']),
                'surah_name': verse.get('surah_name', ''),
                'ayah': int(verse['ayah']),
                'verse_key': verse['verse_key'],
                'text': verse['text'],
                'text_normalized': verse.get('text_normalized', ''),
                'similarity': float(similarity),
                'distance': float(distance)
            })
        
        return results
    
    def get_model_info(self) -> Dict:
        """Get information about the loaded model."""
        return {
            'model_name': self.config['model_name'],
            'model_path': self.config['model_path'],
            'embedding_dimension': self.config['dimension'],
            'num_verses': self.config['num_verses'],
            'metrics': self.config['metrics']
        }

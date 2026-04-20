"""
Quran Semantic Search - Version 1
Streamlit Web Application

Author: [Your Name]
Description: Web interface for semantic search over 6,236 Quranic verses
"""

import streamlit as st
import pandas as pd
import numpy as np
import faiss
import os
import json
from sentence_transformers import SentenceTransformer
import re
from typing import List, Dict

# Page configuration
st.set_page_config(
    page_title="Quran Semantic Search",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subheader {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .verse-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2E7D32;
        margin-bottom: 1rem;
    }
    .verse-arabic {
        font-size: 1.5rem;
        line-height: 2;
        direction: rtl;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }
    .verse-meta {
        font-size: 0.9rem;
        color: #666;
    }
    .similarity-score {
        display: inline-block;
        background-color: #E8F5E9;
        color: #2E7D32;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ===========================
# HELPER FUNCTIONS
# ===========================

@st.cache_data
def load_surah_names():
    """Load surah names dictionary"""
    return {
        1: "الفاتحة", 2: "البقرة", 3: "آل عمران", 4: "النساء", 5: "المائدة",
        6: "الأنعام", 7: "الأعراف", 8: "الأنفال", 9: "التوبة", 10: "يونس",
        11: "هود", 12: "يوسف", 13: "الرعد", 14: "إبراهيم", 15: "الحجر",
        16: "النحل", 17: "الإسراء", 18: "الكهف", 19: "مريم", 20: "طه",
        21: "الأنبياء", 22: "الحج", 23: "المؤمنون", 24: "النور", 25: "الفرقان",
        26: "الشعراء", 27: "النمل", 28: "القصص", 29: "العنكبوت", 30: "الروم",
        31: "لقمان", 32: "السجدة", 33: "الأحزاب", 34: "سبأ", 35: "فاطر",
        36: "يس", 37: "الصافات", 38: "ص", 39: "الزمر", 40: "غافر",
        41: "فصلت", 42: "الشورى", 43: "الزخرف", 44: "الدخان", 45: "الجاثية",
        46: "الأحقاف", 47: "محمد", 48: "الفتح", 49: "الحجرات", 50: "ق",
        51: "الذاريات", 52: "الطور", 53: "النجم", 54: "القمر", 55: "الرحمن",
        56: "الواقعة", 57: "الحديد", 58: "المجادلة", 59: "الحشر", 60: "الممتحنة",
        61: "الصف", 62: "الجمعة", 63: "المنافقون", 64: "التغابن", 65: "الطلاق",
        66: "التحريم", 67: "الملك", 68: "القلم", 69: "الحاقة", 70: "المعارج",
        71: "نوح", 72: "الجن", 73: "المزمل", 74: "المدثر", 75: "القيامة",
        76: "الإنسان", 77: "المرسلات", 78: "النبأ", 79: "النازعات", 80: "عبس",
        81: "التكوير", 82: "الإنفطار", 83: "المطففين", 84: "الإنشقاق", 85: "البروج",
        86: "الطارق", 87: "الأعلى", 88: "الغاشية", 89: "الفجر", 90: "البلد",
        91: "الشمس", 92: "الليل", 93: "الضحى", 94: "الشرح", 95: "التين",
        96: "العلق", 97: "القدر", 98: "البينة", 99: "الزلزلة", 100: "العاديات",
        101: "القارعة", 102: "التكاثر", 103: "العصر", 104: "الهمزة", 105: "الفيل",
        106: "قريش", 107: "الماعون", 108: "الكوثر", 109: "الكافرون", 110: "النصر",
        111: "المسد", 112: "الإخلاص", 113: "الفلق", 114: "الناس"
    }

def normalize_arabic(text: str) -> str:
    """Normalize Arabic text"""
    if pd.isna(text):
        return ""
    
    # Remove Arabic diacritics
    arabic_diacritics = re.compile("""
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
    text = re.sub("[إأآا]", "ا", text)
    text = text.replace("ى", "ي")
    text = text.replace("ة", "ه")
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

@st.cache_resource
def load_search_engine(model_dir: str = "models/v1"):
    """Load the semantic search engine (cached)"""
    
    # Load config
    with open(f"{model_dir}/config.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Load model
    model = SentenceTransformer(config['model_path'])
    
    # Load FAISS index
    index = faiss.read_index(f"{model_dir}/quran_index.faiss")
    
    # Load verses dataframe
    df = pd.read_csv(f"{model_dir}/quran_verses.csv")
    
    return model, index, df, config

def search_quran(query: str, model, index, df, top_k: int = 10) -> List[Dict]:
    """
    Perform semantic search on Quran verses
    
    Args:
        query: Search query
        model: Sentence transformer model
        index: FAISS index
        df: Verses dataframe
        top_k: Number of results
        
    Returns:
        List of result dictionaries
    """
    # Normalize query if Arabic
    query_normalized = normalize_arabic(query) if any('\u0600' <= c <= '\u06FF' for c in query) else query
    
    # Encode query
    query_embedding = model.encode([query_normalized], convert_to_numpy=True).astype('float32')
    
    # Search
    distances, indices = index.search(query_embedding, top_k)
    
    # Prepare results
    results = []
    for rank, (idx, distance) in enumerate(zip(indices[0], distances[0]), start=1):
        if idx == -1:
            continue
        
        verse = df.iloc[idx]
        similarity = 1 / (1 + distance)
        
        results.append({
            'rank': rank,
            'surah': int(verse['surah']),
            'surah_name': verse['surah_name'],
            'ayah': int(verse['ayah']),
            'verse_key': verse['verse_key'],
            'text': verse['text'],
            'text_normalized': verse['text_normalized'],
            'similarity': float(similarity),
            'distance': float(distance)
        })
    
    return results

# ===========================
# MAIN APP
# ===========================

def main():
    # Header
    st.markdown('<h1 class="main-header">📖 Quran Semantic Search</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subheader">Discover verses through meaning, not just keywords</p>',
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        top_k = st.slider(
            "Number of results",
            min_value=1,
            max_value=20,
            value=5,
            help="How many verses to return"
        )
        
        show_scores = st.checkbox(
            "Show similarity scores",
            value=True,
            help="Display technical similarity metrics"
        )
        
        st.markdown("---")
        
        st.header("ℹ️ About")
        st.markdown("""
        **Version 1.0** - Basic Semantic Search
        
        This tool uses AI embeddings to find Quranic verses based on meaning, 
        not just exact word matches.
        
        **Features:**
        - 6,236 searchable verses
        - Arabic & English queries
        - Semantic similarity search
        - FAISS-powered fast retrieval
        
        **Coming in V2:**
        - Tafseer (interpretation) search
        - Hybrid keyword + semantic
        - Advanced filtering
        """)
        
        st.markdown("---")
        
        st.header("💡 Example Queries")
        
        example_queries_arabic = [
            "الرحمة والمغفرة",
            "الصبر في الشدائد",
            "يوم القيامة",
            "الجنة والنار",
            "التوبة والاستغفار"
        ]
        
        example_queries_english = [
            "mercy and forgiveness",
            "patience in hardship",
            "day of judgment",
            "paradise and hell",
            "repentance"
        ]
        
        st.markdown("**Arabic:**")
        for ex in example_queries_arabic:
            if st.button(ex, key=f"ar_{ex}"):
                st.session_state.query = ex
        
        st.markdown("**English:**")
        for ex in example_queries_english:
            if st.button(ex, key=f"en_{ex}"):
                st.session_state.query = ex
    
    # Main content area
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Search input
        query = st.text_input(
            "🔍 Enter your search query (Arabic or English)",
            value=st.session_state.get('query', ''),
            placeholder="e.g., الصبر أو patience in hardship",
            key="search_input"
        )
        
        # Search button
        if st.button("🔍 Search", type="primary", use_container_width=True):
            if query.strip():
                with st.spinner("🔎 Searching through 6,236 verses..."):
                    try:
                        # Load search engine
                        model, index, df, config = load_search_engine()
                        
                        # Perform search
                        results = search_quran(query, model, index, df, top_k)
                        
                        # Display results
                        st.success(f"✅ Found {len(results)} relevant verses")
                        
                        st.markdown("---")
                        
                        for result in results:
                            # Create verse card
                            st.markdown(f"""
                            <div class="verse-card">
                                <div class="verse-meta">
                                    <strong>#{result['rank']}</strong> | 
                                    {result['surah_name']} ({result['surah']}:{result['ayah']})
                                    {f'<span class="similarity-score">Similarity: {result["similarity"]:.2%}</span>' if show_scores else ''}
                                </div>
                                <div class="verse-arabic">
                                    {result['text']}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Download results
                        st.markdown("---")
                        results_df = pd.DataFrame(results)
                        csv = results_df.to_csv(index=False).encode('utf-8-sig')
                        
                        st.download_button(
                            label="📥 Download Results (CSV)",
                            data=csv,
                            file_name=f"quran_search_{query[:20]}.csv",
                            mime="text/csv"
                        )
                        
                    except FileNotFoundError:
                        st.error("""
                        ❌ **Model files not found!**
                        
                        Please run the Jupyter notebook first to:
                        1. Evaluate models
                        2. Select the best model
                        3. Build and save the FAISS index
                        
                        Expected directory: `models/v1/`
                        """)
                    except Exception as e:
                        st.error(f"❌ An error occurred: {str(e)}")
            else:
                st.warning("⚠️ Please enter a search query")
        
        # Info message
        if not query:
            st.info("""
            👆 **Enter a search query above to get started**
            
            You can search in:
            - **Arabic**: الصبر، الرحمة، يوم القيامة
            - **English**: patience, mercy, day of judgment
            
            The search uses AI to understand meaning, not just match keywords!
            """)

if __name__ == "__main__":
    main()

"""
Quran Semantic Search - Streamlit Web Application

Author: Muhammad Al-Geddawy
Description: Web interface for semantic search over 6,236 Quranic verses
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
from typing import List, Dict

from .search_engine import SemanticSearchEngine
from .data_loader import get_surah_names


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


@st.cache_resource
def load_search_engine(model_dir: str = "models/v1"):
    """Load the semantic search engine (cached)."""
    return SemanticSearchEngine(model_dir)


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
                        search_engine = load_search_engine()
                        
                        # Perform search
                        results = search_engine.search(query, top_k)
                        
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

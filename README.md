# 📖 Quran Semantic Search Engine

> AI-powered semantic search over 6,236 Quranic verses using Arabic embeddings

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)

---

## 🎯 Project Overview

This project builds a **semantic search engine** for the Holy Quran, enabling users to find verses based on **meaning** rather than exact keyword matches. The project demonstrates a complete ML pipeline from data cleaning to production deployment, with **three progressive versions** showcasing increasing sophistication.

### Why This Project?

- **Underserved Audience**: Millions of Muslims worldwide lack quality semantic search tools for Quranic study
- **Technical Depth**: Complete ML workflow (data cleaning, model evaluation, deployment)
- **Real-World Impact**: Enables deeper engagement with Islamic texts for students, researchers, and scholars
- **Open Source**: Transparent, reproducible, and community-driven

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Query (Arabic/English)              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  Text Normalization           │
         │  (Remove diacritics, etc.)    │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  Sentence Transformer Model   │
         │  (Best model via evaluation)  │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  Query Embedding (768-dim)    │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │   FAISS Vector Search         │
         │   (6,236 verse embeddings)    │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  Top-K Similar Verses         │
         │  (Ranked by L2 distance)      │
         └───────────────────────────────┘
```

---

## 📦 Version Roadmap

| Version | Status | Description | Timeline |
|---------|--------|-------------|----------|
| **V1** | ✅ **Complete** | Basic semantic search with model evaluation | 2-3 weeks |
| **V2** | 🚧 In Progress | Hybrid search (semantic + BM25) + Tafseer corpus | 3-4 weeks |
| **V3** | 📋 Planned | Ontology-based concept search with Neo4j | 2-3 months |

### Version 1: Basic Semantic Search ✅

**Features:**
- ✅ Semantic search over 6,236 Quranic verses
- ✅ Arabic and English query support
- ✅ Model evaluation framework (4 models compared)
- ✅ Metrics: MRR@10, Recall@10, Precision@1
- ✅ FAISS-powered fast retrieval (<100ms)
- ✅ Streamlit web interface

**Tech Stack:**
```
Data: Tanzil Quran dataset (tanzil.net)
Embeddings: multilingual-e5-large (best model selected via eval)
Vector Store: FAISS IndexFlatL2
Normalization: Arabic diacritics removal
Interface: Streamlit + Jupyter Notebook
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- 4GB+ RAM
- Internet connection (for downloading models)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/MuhammadAlGeddawy/Semantic-Search-in-Holy-Quran.git
cd Semantic-Search-in-Holy-Quran
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Prepare the data**

Download the Quran dataset and place it in `data/Quran Dataset/csv/`:
- `qurantexttanzil.csv` (required)

Or use the provided sample in the repo.

---

## 📊 Model Evaluation (V1)

### Run the Complete Evaluation Notebook

```bash
jupyter notebook quran_semantic_search_v1_complete.ipynb
```

This notebook will:

1. **Load and clean data** (6,236 verses)
2. **Test 4 embedding models**:
   - `paraphrase-multilingual-mpnet-base-v2`
   - `intfloat/multilingual-e5-large`
   - `CAMeL-Lab/bert-base-arabic-camelbert-msa`
   - `asafaya/bert-base-arabic`
3. **Evaluate each model** using synthetic queries
4. **Select the best model** based on MRR@10
5. **Save artifacts** to `models/v1/`

### Evaluation Metrics

We use **synthetic evaluation** (no manual annotation needed):

- **MRR@10**: Mean Reciprocal Rank (where does correct verse appear?)
- **Recall@10**: Is the correct verse in top 10?
- **Precision@1**: Is the top result correct?

**Evaluation Strategy:**
- Generate 100 query-verse pairs from the corpus
- Query types: prefix (first 3 words), middle segment
- Ground truth: original verse should rank high

---

## 🖥️ Running the Web App

After completing the notebook evaluation:

```bash
streamlit run streamlit_app.py
```

The app will launch at `http://localhost:8501`

### Features:
- 🔍 Arabic and English search
- 📊 Adjustable result count
- 💾 Download results as CSV
- 📱 Responsive design

### Example Queries:

**Arabic:**
```
الرحمة والمغفرة
الصبر في الشدائد
يوم القيامة
الجنة والنار
```

**English:**
```
mercy and forgiveness
patience in hardship
day of judgment
paradise and hell
```

---

## 📁 Project Structure

```
quran-semantic-search/
├── data/
│   └── Quran Dataset/
│       └── csv/
│           ├── qurantexttanzil.csv          # Main Quran text
│           ├── quranuthmanitanzil.csv       # Alternative script
│           └── quran.csv                    # Full metadata
├── models/
│   └── v1/
│       ├── quran_index.faiss                # FAISS vector index
│       ├── quran_embeddings.npy             # Verse embeddings
│       ├── quran_verses.csv                 # Processed verses
│       └── config.json                      # Model metadata
├── quran_semantic_search_v1_complete.ipynb  # Main evaluation notebook
├── app.py                                   # Streamlit web app
├── requirements.txt                         # Python dependencies
├── VERSION_COMPARISON.md                    # Detailed version comparison
└── README.md                                # This file
```

---

## 📊 Results (V1)

### Model Comparison

| Model | MRR@10 | Recall@10 | Precision@1 | Dimension |
|-------|--------|-----------|-------------|-----------|
| **paraphrase-multilingual** | 0.1119 | 0.1800 | 0.0800 | 768 |
| **multilingual-e5-large** | 0.2920 | 0.4600 | 0.2300 | 1024 |
| **camelbert-msa** | 0.0733 | 0.1000 | 0.0600 | 768 |
| **arabic-bert** | 0.0713 | 0.1200 | 0.0600 | 768 |

These results were produced by the V1 evaluation notebook and show that `multilingual-e5-large` achieved the best retrieval metrics.

### Best Model: `multilingual-e5-large`

**Why this model?**
- Highest MRR@10 score
- Good balance of retrieval quality and speed
- Supports both Arabic and English queries

---

## 🔬 Technical Deep Dive

### 1. Data Preprocessing

**Challenges:**
- Messy CSV column structure (no proper headers)
- Arabic diacritics (tashkeel) inconsistency
- Multiple Quran text variants

**Solutions:**
```python
# Normalize Arabic text
def normalize_arabic(text):
    # Remove diacritics
    text = re.sub(arabic_diacritics, '', text)
    # Normalize Alef variants: إأآا → ا
    text = re.sub("[إأآا]", "ا", text)
    # Normalize Yaa: ى → ي
    text = text.replace("ى", "ي")
    return text
```

### 2. Model Evaluation Without Labels

**Problem:** No existing annotated dataset for Quranic semantic search

**Solution:** Synthetic evaluation
```python
# Generate query-verse pairs
verse = "الله الرحمن الرحيم"
query_prefix = "الله الرحمن"    # First 3 words
query_middle = "الرحمن الرحيم"  # Middle segment

# Ground truth: original verse should be in top-k
```

### 3. Vector Similarity Search

**Why FAISS?**
- Fast exact search for 6k vectors (<100ms)
- No need for approximate search (ANN) at this scale
- Easy persistence (save/load index)

**Index Type:** `IndexFlatL2`
- Exact L2 distance calculation
- 100% recall guarantee

---

## 🛠️ Development

### Adding New Features

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Make your changes**
4. **Run tests** (if available)
5. **Submit a pull request**

### Extending to V2

To build V2 (Hybrid Search + Tafseer):

1. **Collect Tafseer corpus**
   - Ibn Kathir (Arabic)
   - Al-Tabari (Arabic)
   - Sahih International (English)

2. **Implement BM25**
   ```python
   from rank_bm25 import BM25Okapi
   bm25 = BM25Okapi(corpus_tokens)
   ```

3. **Fusion Strategy**
   - Reciprocal Rank Fusion (RRF)
   - Or learned weights (semantic vs keyword)

---

## 📚 Data Sources

All data sources are **open and freely available**:

- **Quran Text**: [tanzil.net](http://tanzil.net) - Clean XML, verified text
- **Tafseer (V2)**:
  - Ibn Kathir: [altafsir.com](http://altafsir.com)
  - Al-Tabari: Available via multiple Islamic websites
- **English Translation**: Sahih International (public domain)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- 🐛 Report bugs
- 💡 Suggest features
- 📖 Improve documentation
- 🧪 Add tests
- 🌍 Add translations

### Areas for Contribution:
- [ ] Add more evaluation metrics (NDCG, etc.)
- [ ] Implement BM25 baseline for comparison
- [ ] Add English translation display
- [ ] Build CLI interface
- [ ] Add unit tests
- [ ] Improve Arabic normalization
- [ ] Support more Quran text variants

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

**Important:** The Quran text itself is divine revelation and not subject to copyright. The code and ML pipeline are open source.

---

## 🙏 Acknowledgments

- **Tanzil.net** for providing clean, verified Quran text
- **Sentence-Transformers** team for excellent embedding models
- **FAISS** team at Meta AI for fast vector search
- The Muslim developer community for inspiration

---

## 📧 Contact

**Author:** Muhammad Al-Geddawy
- GitHub: [@MuhammadAlGeddawy](https://github.com/MuhammadAlGeddawy)
- LinkedIn: [MuhammadAlGeddawy](https://www.linkedin.com/in/muhammad-al-geddawy-08019019b/)
- Email: muhammad.anwar@ejust.edu.eg

---

## 🔮 Future Roadmap

### Version 2 (Next 1-2 months)
- [ ] Hybrid search (semantic + BM25)
- [ ] Tafseer corpus integration
- [ ] Metadata filtering (surah, revelation period)
- [ ] Improved UI with search history
- [ ] API endpoint for developers

### Version 3 (2-3 months)
- [ ] Islamic ontology design
- [ ] Neo4j knowledge graph
- [ ] Concept-based search
- [ ] Graph visualization
- [ ] Research paper publication

### Long-term
- [ ] Mobile app (React Native)
- [ ] Voice search (Arabic speech-to-text)
- [ ] Personalized recommendations
- [ ] Multi-language Tafseer support
- [ ] Integration with existing Islamic apps

---

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Built with ❤️ for the Muslim community**

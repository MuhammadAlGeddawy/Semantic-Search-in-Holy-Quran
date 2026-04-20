# Quran Semantic Search - Version Comparison

## 📊 Project Overview

This document compares three versions of the Quran Semantic Search Engine, showcasing the evolution from basic semantic search to advanced ontology-based retrieval.

---

## 🎯 Version Comparison Matrix

| Aspect | V1: Basic Semantic Search | V2: Hybrid Search + Tafseer | V3: Ontology-Based Search |
|--------|---------------------------|------------------------------|---------------------------|
| **Status** | ✅ Complete | 🚧 In Progress | 📋 Planned |
| **Core Technology** | Arabic embeddings + FAISS | V1 + Tafseer corpus + BM25 | V2 + Neo4j knowledge graph |
| **Data Sources** | 6,236 Quran verses | Quran + Ibn Kathir + Al-Tabari | V2 + Islamic ontology |
| **Search Type** | Semantic only | Hybrid (semantic + keyword) | Concept & theme-based |
| **Complexity** | Low | Medium | High |
| **Timeline** | 2-3 weeks | 3-4 weeks | 2-3 months |
| **Target Audience** | General users | Researchers & students | Islamic scholars |

---

## 📖 Detailed Breakdown

### Version 1: Basic Semantic Search (COMPLETE ✅)

**What It Does:**
- Semantic search over 6,236 Quranic verses using Arabic embeddings
- Supports both Arabic and English queries
- Returns top-k most semantically similar verses

**Technical Stack:**
```
├── Embeddings: Sentence-Transformers (best model selected via evaluation)
├── Vector Store: FAISS IndexFlatL2
├── Normalization: Arabic diacritics removal + character normalization
└── Interface: Jupyter Notebook + Python functions
```

**Key Features:**
- ✅ Model evaluation framework (4 models compared)
- ✅ Metrics: MRR@10, Recall@10, Precision@1
- ✅ Synthetic evaluation dataset (no manual annotation)
- ✅ Production-ready search function
- ✅ Persistent storage (FAISS index + embeddings saved)

**Evaluation Results:**
| Model | MRR@10 | Recall@10 | Precision@1 | Dimension |
|-------|--------|-----------|-------------|-----------|
| paraphrase-multilingual | 0.1119 | 0.1800 | 0.0800 | 768 |
| multilingual-e5-large | 0.2920 | 0.4600 | 0.2300 | 1024 |
| camelbert-msa | 0.0733 | 0.1000 | 0.0600 | 768 |
| arabic-bert | 0.0713 | 0.1200 | 0.0600 | 768 |

**Example Queries:**
```python
# Arabic
quran_semantic_search("الرحمة والمغفرة", top_k=5)
quran_semantic_search("الصبر في الشدائد", top_k=5)

# English (if multilingual model)
quran_semantic_search("mercy and forgiveness", top_k=5)
```

**Limitations:**
- ❌ No keyword matching (misses exact phrase matches)
- ❌ No Tafseer (interpretation) context
- ❌ No filtering by metadata (surah, revelation period)
- ❌ Semantic search only (can miss specific words)

**Files Delivered:**
```
v1/
├── quran_semantic_search_v1_complete.ipynb  # Main notebook
├── models/
│   └── v1/
│       ├── quran_index.faiss                # FAISS index
│       ├── quran_embeddings.npy             # Verse embeddings
│       ├── quran_verses.csv                 # Processed verses
│       └── config.json                      # Model metadata
└── README.md                                # Documentation
```

---

### Version 2: Hybrid Search + Tafseer (PLANNED 🚧)

**What It Does:**
- Combines semantic search with keyword (BM25) search
- Expands corpus to include Tafseer (Quranic interpretation)
- Enables filtering by metadata (surah, revelation context, themes)

**Technical Stack:**
```
├── Semantic: V1 embedding model (best from evaluation)
├── Keyword: BM25 / Elasticsearch
├── Hybrid Ranking: RRF (Reciprocal Rank Fusion) or learned weights
├── Corpus: Quran + Ibn Kathir + Al-Tabari Tafseer
├── Metadata: Surah info, revelation period (Meccan/Medinan), themes
└── Interface: Streamlit web app
```

**Planned Features:**
- 🔄 Hybrid search (semantic + keyword fusion)
- 📚 Tafseer corpus integration (~50k+ segments)
- 🔍 Metadata filtering (surah, theme, revelation context)
- 🎚️ Adjustable semantic/keyword weight sliders
- 🌐 Web-based UI (Streamlit)
- 📊 Search result explanations (why this verse ranked high)

**Data Sources:**
- **Quran Text**: tanzil.net (already integrated in V1)
- **Tafseer**: 
  - Ibn Kathir (Arabic): ~10k interpretations
  - Al-Tabari (Arabic): ~15k interpretations
  - Sahih International (English translation)

**Evaluation Strategy:**
- Compare hybrid vs pure semantic on V1 eval set
- Manual evaluation by domain experts (20-30 queries)
- A/B testing with real users

**Expected Improvements:**
- Higher Precision@1 for exact phrase queries
- Better coverage with Tafseer context
- More control for power users (filtering + weight adjustment)

**Challenges:**
- Tafseer corpus cleaning and segmentation
- Optimal fusion weight tuning
- Handling multi-lingual queries (Arabic query → English Tafseer?)

---

### Version 3: Ontology-Based Concept Search (PLANNED 📋)

**What It Does:**
- Search by Islamic concepts, themes, and topics
- Navigate related verses through knowledge graph
- Support complex queries ("verses about patience during hardship")

**Technical Stack:**
```
├── Knowledge Graph: Neo4j
├── Ontology Design: Custom Islamic concept taxonomy
│   ├── Themes: Belief, Worship, Ethics, Law, History, Eschatology
│   ├── Concepts: Prayer, Patience, Justice, Mercy, etc.
│   └── Relationships: related_to, exemplifies, contradicts
├── Search: Cypher queries + graph traversal
├── Embeddings: Concept embeddings (for similarity)
└── Interface: Graph visualization + advanced query builder
```

**Ontology Structure (Draft):**
```
Root Concepts
├── Aqeedah (Belief)
│   ├── Tawheed (Oneness of God)
│   ├── Prophethood
│   ├── Afterlife
│   └── Divine Attributes
├── Ibadah (Worship)
│   ├── Salah (Prayer)
│   ├── Zakat (Charity)
│   ├── Fasting
│   └── Hajj
├── Akhlaq (Ethics)
│   ├── Patience
│   ├── Gratitude
│   ├── Justice
│   ├── Mercy
│   └── Honesty
├── Fiqh (Islamic Law)
├── Seerah (Prophetic History)
└── Eschatology (End Times)
```

**Planned Features:**
- 🕸️ Concept-based navigation (explore related verses)
- 🎯 Theme-based search ("All verses about mercy")
- 🔗 Graph visualization (see connections between concepts)
- 🧠 Query understanding ("patience in hardship" → extracts concepts)
- 📈 Advanced analytics (concept co-occurrence, theme distribution)

**Research Contributions:**
- Novel Islamic ontology design
- Graph-based retrieval for religious texts
- Potential academic publication

**Challenges:**
- Ontology design requires Islamic scholarship expertise
- Manual concept tagging (or semi-automated with LLMs)
- Graph query performance at scale
- Validating ontology completeness

**Expected Timeline:**
- Month 1: Ontology design + expert review
- Month 2: Concept extraction + graph building
- Month 3: Query system + visualization + testing

---

## 🚀 Evolution Path

```
V1: Foundation                V2: Enhancement              V3: Research
┌─────────────┐              ┌─────────────┐              ┌─────────────┐
│  Semantic   │──────────────▶│   Hybrid    │──────────────▶│  Ontology   │
│   Search    │   + Keyword  │   Search    │  + Knowledge │   Search    │
│             │   + Tafseer  │             │     Graph    │             │
└─────────────┘              └─────────────┘              └─────────────┘
     2-3 weeks                   3-4 weeks                   2-3 months

  General users             Researchers                  Islamic scholars
```

---

## 📊 Performance Comparison

### Retrieval Quality

| Metric | V1 | V2 (Expected) | V3 (Expected) |
|--------|----|--------------|--------------| 
| MRR@10 | 0.2920 | +15-20% | +25-30% |
| Recall@10 | 0.4600 | +10-15% | +20-25% |
| Precision@1 | 0.2300 | +20-25% | +30-35% |
| User Satisfaction | - | TBD | TBD |

### System Performance

| Metric | V1 | V2 | V3 |
|--------|----|----|----|
| Index Size | ~50MB | ~200MB | ~500MB |
| Query Latency | <100ms | <200ms | <500ms |
| Corpus Size | 6,236 verses | ~60k segments | ~100k nodes |
| Storage | Local files | PostgreSQL + Files | Neo4j + Files |

---

## 🎓 Use Cases by Version

### V1: Basic Semantic Search
- ✅ Quick verse lookup by meaning
- ✅ Finding similar verses
- ✅ Beginner Quran study
- ✅ Personal reflection

### V2: Hybrid Search + Tafseer
- ✅ Academic research
- ✅ Detailed verse interpretation
- ✅ Comparative analysis (different Tafseer)
- ✅ Teacher/student use
- ✅ Sermon preparation

### V3: Ontology-Based Search
- ✅ Thematic Quran study
- ✅ Islamic jurisprudence research
- ✅ Concept exploration
- ✅ Advanced scholarly work
- ✅ Educational curriculum design

---

## 💡 Lessons Learned (Will Update)

### V1 Insights:
- Model evaluation is critical (don't assume multilingual = best for Arabic)
- Synthetic eval datasets work surprisingly well
- Arabic normalization significantly impacts retrieval quality
- FAISS is fast enough for 6k vectors (no need for approximate search)

### V2 Insights (Upcoming):
- TBD

### V3 Insights (Upcoming):
- TBD

---

## 📈 Metrics to Track

### Technical Metrics:
- Query latency (p50, p95, p99)
- Index build time
- Storage requirements
- Model inference time

### Quality Metrics:
- MRR@k, Recall@k, Precision@k
- NDCG (if we get relevance labels)
- User click-through rate (V2+)
- Session success rate

### Business Metrics:
- GitHub stars
- API usage (if deployed)
- User retention
- Community engagement

---

## 🔗 Resources

### V1:
- Code: `v1/quran_semantic_search_v1_complete.ipynb`
- Data: `data/Quran Dataset/csv/`
- Models: `models/v1/`

### V2:
- TBD

### V3:
- TBD

---

## 📝 Next Actions

### Immediate (This Week):
1. ✅ Complete V1 notebook execution
2. ✅ Run model evaluation and select best model
3. ✅ Test search function with 20+ queries
4. 📝 Document V1 results in this file
5. 🚀 Create GitHub repo with V1 code
6. 📱 Build Streamlit app for V1
7. 📢 LinkedIn post about V1 completion

### Short-term (Next 2 Weeks):
1. 📚 Collect and clean Tafseer corpus
2. 🔍 Research BM25 implementation options
3. 🎨 Design V2 UI mockups
4. 📊 Plan V2 evaluation strategy

### Long-term (Next 2 Months):
1. 🕸️ Design Islamic ontology (consult scholars)
2. 📖 Research Neo4j + graph RAG patterns
3. 📄 Draft research paper outline (if publishing V3)

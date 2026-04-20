# 🚀 Quick Start Guide - Quran Semantic Search V1

This guide will get you up and running with the Quran Semantic Search engine in **under 30 minutes**.

---

## ✅ Prerequisites Checklist

Before you begin, make sure you have:

- [ ] Python 3.8 or higher installed
- [ ] At least 4GB of free RAM
- [ ] Internet connection (for downloading models)
- [ ] Basic familiarity with Python and Jupyter notebooks

---

## 📥 Step 1: Installation

### 1.1 Clone the Repository

```bash
git clone https://github.com/yourusername/quran-semantic-search.git
cd quran-semantic-search
```

### 1.2 Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 1.3 Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected time:** 5-10 minutes (depending on internet speed)

---

## 📊 Step 2: Prepare Your Data

### 2.1 Verify Data Files

Make sure you have the Quran dataset in this structure:

```
data/
└── Quran Dataset/
    └── csv/
        └── qurantexttanzil.csv
```

### 2.2 Test Data Loading

Run the data loader script:

```bash
python data_loader.py
```

**Expected output:**
```
📖 Loading Quran data from: data/Quran Dataset/csv/qurantexttanzil.csv
   Initial shape: (6236, 5)
✅ Loaded 6236 verses
   Surahs: 1 to 114
```

If you see errors, check:
- File path is correct
- CSV file is not corrupted
- File encoding is UTF-8

---

## 🧪 Step 3: Run Model Evaluation

### 3.1 Open Jupyter Notebook

```bash
jupyter notebook quran_semantic_search_v1_complete.ipynb
```

### 3.2 Execute All Cells

In Jupyter:
1. Click `Kernel` → `Restart & Run All`
2. Wait for all cells to complete (15-30 minutes)

**What happens:**
- ✅ Data is loaded and cleaned
- ✅ Text is normalized (removing diacritics)
- ✅ 4 embedding models are tested
- ✅ Evaluation metrics are calculated
- ✅ Best model is selected
- ✅ FAISS index is built and saved

### 3.3 Check Output Directory

After completion, verify these files exist:

```
models/
└── v1/
    ├── quran_index.faiss        # Vector index
    ├── quran_embeddings.npy     # Embeddings
    ├── quran_verses.csv         # Processed verses
    └── config.json              # Model config
```

---

## 🖥️ Step 4: Launch Web App

### 4.1 Start Streamlit

```bash
streamlit run app.py
```

### 4.2 Access the Interface

Open your browser and go to:
```
http://localhost:8501
```

### 4.3 Test Queries

Try these example searches:

**Arabic:**
- `الرحمة والمغفرة`
- `الصبر في الشدائد`
- `يوم القيامة`

**English:**
- `mercy and forgiveness`
- `patience in hardship`
- `day of judgment`

---

## 🔧 Troubleshooting

### Issue: "Model files not found"

**Solution:**
1. Make sure you ran the Jupyter notebook completely
2. Check that `models/v1/` directory exists
3. Verify all 4 files are present in `models/v1/`

### Issue: "No module named 'sentence_transformers'"

**Solution:**
```bash
pip install sentence-transformers
```

### Issue: "CUDA out of memory"

**Solution:**
The models use CPU by default. If you're getting CUDA errors:
```bash
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Issue: "CSV has wrong structure"

**Solution:**
1. Check your CSV file format matches the expected structure
2. Run `python data_loader.py` to see detailed error messages
3. Update the column mapping in `data_loader.py` if needed

### Issue: Slow model loading

**Solution:**
- First time loading models downloads them (~500MB per model)
- Subsequent loads are fast (models are cached)
- Ensure stable internet connection

---

## 📋 Quick Reference

### Important Files

| File | Purpose |
|------|---------|
| `quran_semantic_search_v1_complete.ipynb` | Main evaluation notebook |
| `app.py` | Streamlit web interface |
| `data_loader.py` | Data preprocessing utility |
| `requirements.txt` | Python dependencies |
| `VERSION_COMPARISON.md` | Detailed version comparison |

### Key Directories

| Directory | Contents |
|-----------|----------|
| `data/` | Raw Quran datasets |
| `models/v1/` | Trained models & indices |
| `data/processed/` | Cleaned data files |

### Useful Commands

```bash
# Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook quran_semantic_search_v1_complete.ipynb

# Launch web app
streamlit run app.py

# Test data loading
python data_loader.py
```

---

## 🎯 Next Steps

After completing V1:

1. **Experiment with queries**
   - Test different Arabic/English queries
   - Compare results across models
   - Document interesting findings

2. **Customize the app**
   - Modify `app.py` styling
   - Add new features (bookmarks, history, etc.)
   - Improve Arabic text rendering

3. **Prepare for V2**
   - Collect Tafseer corpus (Ibn Kathir, Al-Tabari)
   - Research BM25 implementation
   - Plan hybrid search architecture

4. **Share your work**
   - Push to GitHub
   - Write a blog post
   - Share on LinkedIn/Twitter

---

## 💡 Tips for Success

### For Best Results:

1. **Model Evaluation**
   - Don't skip the evaluation step
   - Compare all 4 models systematically
   - Document which model works best for your use case

2. **Query Formulation**
   - Be specific but not too long (3-6 words ideal)
   - Use meaningful concepts, not just keywords
   - Try both Arabic and English

3. **Performance Optimization**
   - Use FAISS for fast search (<100ms)
   - Cache model loading in Streamlit
   - Normalize queries before encoding

4. **Data Quality**
   - Verify verse count (should be 6,236)
   - Check for duplicate verses
   - Ensure Arabic text is clean

---

## 📧 Get Help

If you're stuck:

1. **Check the README**: Detailed documentation with examples
2. **Review VERSION_COMPARISON.md**: Understanding the architecture
3. **Open an issue**: GitHub issues for bugs/questions
4. **Contact**: [your.email@example.com]

---

## ✅ Success Checklist

By the end of this guide, you should have:

- [ ] Installed all dependencies
- [ ] Loaded and cleaned Quran data
- [ ] Run model evaluation (4 models tested)
- [ ] Selected best model based on metrics
- [ ] Built FAISS index
- [ ] Launched Streamlit app
- [ ] Successfully searched for verses
- [ ] Understood the evaluation results

**Congratulations! You now have a working semantic search engine for the Quran! 🎉**

---

**Estimated Total Time:** 30-45 minutes (including model downloads)

**Next:** Explore VERSION_COMPARISON.md to plan V2 and V3

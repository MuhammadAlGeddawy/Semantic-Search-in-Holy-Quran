"""
Data Loading Utility for Quran Dataset

This script handles the messy CSV structure from tanzil.net exports
and creates a clean, normalized DataFrame for the search engine.

Author: [Your Name]
"""

import pandas as pd
import numpy as np
import os
from typing import Tuple

def load_tanzil_csv(file_path: str) -> pd.DataFrame:
    """
    Load Quran data from Tanzil CSV with proper column handling.
    
    The CSV structure from tanzil.net is:
    - No proper header row
    - Columns: [surah, ayah, arabic_text, verse_id, extra]
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        Cleaned DataFrame with columns: surah, ayah, text, verse_key
    """
    print(f"📖 Loading Quran data from: {file_path}")
    
    # Read without header
    df = pd.read_csv(file_path, header=None)
    
    print(f"   Initial shape: {df.shape}")
    print(f"   Columns detected: {df.columns.tolist()}")
    
    # Assign column names based on position
    # Based on your sample: [surah, ayah, text, verse_id, extra]
    if len(df.columns) >= 4:
        df.columns = ['surah', 'ayah', 'text', 'verse_id'] + [f'extra_{i}' for i in range(len(df.columns) - 4)]
    else:
        raise ValueError(f"Expected at least 4 columns, got {len(df.columns)}")
    
    # Keep only essential columns
    df = df[['surah', 'ayah', 'text', 'verse_id']].copy()
    
    # Drop rows with missing text
    df = df.dropna(subset=['text'])
    print(f"   After removing NaN text: {len(df)} rows")
    
    # Convert surah and ayah to numeric
    df['surah'] = pd.to_numeric(df['surah'], errors='coerce')
    df['ayah'] = pd.to_numeric(df['ayah'], errors='coerce')
    
    # Drop rows with invalid surah/ayah
    df = df.dropna(subset=['surah', 'ayah'])
    df['surah'] = df['surah'].astype(int)
    df['ayah'] = df['ayah'].astype(int)
    
    # Filter valid surah range (1-114)
    df = df[(df['surah'] >= 1) & (df['surah'] <= 114)]
    
    # Create verse_key (surah:ayah format)
    df['verse_key'] = df['surah'].astype(str) + ':' + df['ayah'].astype(str)
    
    # Reset index
    df = df.reset_index(drop=True)
    
    print(f"✅ Loaded {len(df)} verses")
    print(f"   Surahs: {df['surah'].min()} to {df['surah'].max()}")
    print(f"   Unique surahs: {df['surah'].nunique()}")
    
    return df

def get_surah_names() -> dict:
    """
    Get dictionary of surah numbers to Arabic names.
    
    Returns:
        Dictionary mapping surah number to Arabic name
    """
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

def prepare_quran_dataset(
    csv_path: str,
    output_dir: str = "data/processed"
) -> Tuple[pd.DataFrame, str]:
    """
    Complete pipeline to load and prepare Quran dataset.
    
    Args:
        csv_path: Path to the raw CSV file
        output_dir: Directory to save processed data
        
    Returns:
        Tuple of (cleaned DataFrame, path to saved CSV)
    """
    # Load raw data
    df = load_tanzil_csv(csv_path)
    
    # Add surah names
    surah_names = get_surah_names()
    df['surah_name'] = df['surah'].map(surah_names)
    
    # Verify all surahs have names
    missing_names = df[df['surah_name'].isna()]['surah'].unique()
    if len(missing_names) > 0:
        print(f"⚠️  Warning: Missing names for surahs: {missing_names}")
    
    # Save processed data
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "quran_clean.csv")
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    
    print(f"💾 Saved processed data to: {output_path}")
    
    # Print statistics
    print("\n📊 Dataset Statistics:")
    print(f"   Total verses: {len(df)}")
    print(f"   Total surahs: {df['surah'].nunique()}")
    print(f"   Avg verses per surah: {len(df) / df['surah'].nunique():.1f}")
    print(f"   Longest surah: {df.groupby('surah').size().idxmax()} ({df.groupby('surah').size().max()} verses)")
    print(f"   Shortest surah: {df.groupby('surah').size().idxmin()} ({df.groupby('surah').size().min()} verses)")
    
    return df, output_path

if __name__ == "__main__":
    # Example usage
    CSV_PATH = "data/Quran Dataset/csv/qurantexttanzil.csv"
    
    if os.path.exists(CSV_PATH):
        df, saved_path = prepare_quran_dataset(CSV_PATH)
        
        print("\n📋 Sample verses:")
        print(df.head(3)[['surah', 'surah_name', 'ayah', 'text']])
    else:
        print(f"❌ File not found: {CSV_PATH}")
        print("Please update the CSV_PATH variable with the correct path.")

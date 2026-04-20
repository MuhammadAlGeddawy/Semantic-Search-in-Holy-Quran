"""
Setup script for Quran Semantic Search
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="quran-semantic-search",
    version="1.0.0",
    author="Muhammad Al-Geddawy",
    author_email="muhammad.anwar@ejust.edu.eg",
    description="AI-powered semantic search engine for the Holy Quran",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MuhammadAlGeddawy/Semantic-Search-in-Holy-Quran",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Religion",
        "Intended Audience :: Education",
        "Topic :: Religion",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "quran-search=quran_search.app:main",
        ],
    },
    keywords="quran search semantic nlp arabic embeddings faiss",
    project_urls={
        "Bug Reports": "https://github.com/MuhammadAlGeddawy/Semantic-Search-in-Holy-Quran/issues",
        "Source": "https://github.com/MuhammadAlGeddawy/Semantic-Search-in-Holy-Quran",
        "Documentation": "https://github.com/MuhammadAlGeddawy/Semantic-Search-in-Holy-Quran/blob/main/README.md",
    },
)

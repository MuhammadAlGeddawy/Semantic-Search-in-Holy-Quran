# Contributing to Quran Semantic Search

Thank you for your interest in contributing! We welcome contributions that help improve this project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Semantic-Search-in-Holy-Quran.git
   cd Semantic-Search-in-Holy-Quran
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install the package in development mode**:
   ```bash
   pip install -e .
   ```

3. **(Optional) Install testing dependencies**:
   ```bash
   pip install pytest pytest-cov
   ```

## Making Changes

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to all functions and classes
- Keep functions focused and modular

### Before Submitting

1. **Test your changes**:
   ```bash
   pytest tests/
   ```

2. **Run the linter** (optional):
   ```bash
   pylint src/quran_search/
   ```

3. **Update documentation** if needed

## Submitting a Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** on GitHub with:
   - Clear description of changes
   - Reference to related issues (if any)
   - Screenshots for UI changes
   - Test results

3. **Wait for review** - we'll provide feedback or merge your contribution

## Contribution Areas

We welcome contributions in these areas:

### 📊 Data & Models
- [ ] Improve Arabic text normalization
- [ ] Test additional embedding models
- [ ] Add Tafseer corpus integration (V2)
- [ ] Create new evaluation metrics

### 🔧 Features
- [ ] Implement BM25 keyword search (V2)
- [ ] Add filtering by surah/revelation period
- [ ] Build CLI interface
- [ ] Create API endpoints

### 📚 Documentation
- [ ] Improve README
- [ ] Add API documentation
- [ ] Create tutorials
- [ ] Fix typos/clarity

### ✅ Testing
- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Test with different Python versions
- [ ] Test on different OS

### 🐛 Bug Fixes
- Report issues with clear steps to reproduce
- Include error messages and logs
- Suggest potential fixes

## Code of Conduct

- Treat all contributors with respect
- Provide constructive feedback
- Focus on ideas, not personal criticism
- Help others learn and grow

## Questions?

- Open an issue for discussion
- Check existing issues first
- Be clear and provide context

---

**Thank you for contributing to making Quranic scholarship more accessible!** 🤝

Built with ❤️ for the Muslim community


# 💰 Finance Learning Hub

[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-orange)](https://openrouter.ai)

**A comprehensive multipage financial education platform** featuring AI-powered assistants, interactive quizzes, real-time calculators, and curated learning resources.

> 🚀 **Final Project** - Demonstrating advanced Python programming with practical financial applications

<details>
<summary><b> English Version</b></summary>

## ✨ Features

### 🤖 Multi-Assistant Finance AI
- **6 Specialized Assistants**: Personal Finance, Investment Analysis, Budget Planning, Economic Research, Tax Help, Document Analysis
- **Smart Fallback System**: Automatic model switching with redundancy
- **Multilingual Support**: Auto-detection and response in English/Indonesian
- **Real-time Chat**: Beautiful interface with timestamps and model info

### 🎯 Interactive Finance Trivia
- **180+ Questions**: Across 3 difficulty levels with detailed explanations
- **Bilingual Content**: Full English and Indonesian support
- **Advanced Analytics**: Performance tracking, streaks, and category analysis
- **Real-time Feedback**: Instant scoring with progress visualization

### 📈 Advanced Financial Calculators
- **Stock Analysis**: Real-time market data with technical indicators (RSI, MACD, Moving Averages)
- **Investment Planner**: Compound interest with tax and inflation adjustments
- **Currency Converter**: Live exchange rates with historical data
- **Mortgage Calculator**: Complete amortization schedules

### 📚 Learning Resources
- **Curated Content**: 30+ YouTube channels and educational websites
- **Professional Categorization**: Organized by topic and difficulty
- **Bilingual Sections**: Separate English and Indonesian resources

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenRouter API account ([free tier available](https://openrouter.ai))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/finance-learning-hub.git
cd finance-learning-hub
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API keys**
Create `.streamlit/secrets.toml`:
```toml
OPENROUTER_API_KEY = "your-openrouter-api-key-here"
```

4. **Launch the application**
```bash
streamlit run app.py
```

5. **Open your browser** to `http://localhost:8501`

## 🏗️ Project Structure

```
finance-learning-hub/
├── app.py                          # Main application
├── pages/
│   ├── 1_🧠_Multi_Finance_AI.py    # AI Assistant (6 specialized bots)
│   ├── 2_🎯_Finance_Trivia.py      # Interactive quiz game
│   ├── 3_📈_Financial_Calculators.py # 4 advanced calculators
│   └── 4_📚_Learning_Resources.py   # Educational content
├── requirements.txt                # Dependencies
├── README.md                      # Documentation
└── .streamlit/
    └── secrets.toml              # API configuration
```

## 🛠️ Tech Stack

**Frontend & Framework**
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) - Web application framework
- ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly) - Interactive visualizations

**Backend & Data**
- ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) - Core programming language
- ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) - Data manipulation
- ![yFinance](https://img.shields.io/badge/yFinance-00A0D1?logo=yahoo) - Financial data

**APIs & External Services**
- ![OpenRouter](https://img.shields.io/badge/OpenRouter-FF6B35) - Multi-model AI API
- ![Yahoo Finance](https://img.shields.io/badge/Yahoo_Finance-720E9B?logo=yahoo) - Market data

## 📊 Python Concepts Demonstrated

### 🏗️ Object-Oriented Programming
```python
# Advanced class architecture
class QuestionBank:          # Manages 180+ questions with categories
class GameState:             # Comprehensive session management  
class ExplanationGenerator:  # Dynamic feedback system
```

### 🗂️ Data Structures
- **Dictionaries**: Assistant configs, translations, question banks
- **Lists & Arrays**: Question pools, chat history, performance data
- **Pandas DataFrame**: Analytics, amortization schedules, market data

### ⚡ Control Flow & State Management
- **Session State**: Multi-page state persistence
- **Error Handling**: API fallbacks and user input validation
- **Real-time Updates**: Live data streaming and UI updates

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Connect repository at [share.streamlit.io](https://share.streamlit.io)
3. Add `OPENROUTER_API_KEY` in secrets
4. Deploy and share public URL

### HuggingFace Spaces
1. Create new Space with Streamlit template
2. Upload code and `requirements.txt`
3. Configure secrets in Settings
4. Deploy automatically on push

## 📸 Application Preview

images/
├── ![Dashboard](images/dashboard.png)
├── ![AI Assistant](images/ai-assistant.png)
├── ![Finance Trivia](images/trivia-game.png)
├── ![Stock Analysis](images/stock-analysis.png)
├── ![Calculator](images/calculator.png)
└── ![Resources](images/resources.png)






## ❓ Frequently Asked Questions

### 🤖 AI Assistant Questions
**Q: How accurate is the financial advice?**  
A: The AI provides educational information only. Always consult certified professionals for financial decisions.

**Q: Which AI models are used?**  
A: Multiple models including Qwen, DeepSeek, Gemini, Grok with automatic fallback.

### 💰 Financial Data
**Q: Is stock data real-time?**  
A: Yes, during market hours. Data sourced from Yahoo Finance API.

**Q: How often are exchange rates updated?**  
A: Currency rates are cached for 10 minutes with real-time API fallbacks.

### 🔧 Technical
**Q: Can I use this on mobile?**  
A: Yes! Fully responsive design works on all devices.

**Q: Is there any cost?**  
A: Completely free. OpenRouter API has generous free tier.

**Q: How do I reset the quiz?**  
A: Use the "Restart" button in the sidebar or refresh the page.

## 🎯 Final Project Highlights

This project demonstrates **advanced Python programming** through:
- **Multipage Streamlit Architecture** with seamless navigation
- **AI Integration** with sophisticated fallback mechanisms  
- **Real-time Data Processing** from multiple financial APIs
- **Professional UI/UX** with custom styling and visualizations
- **Comprehensive Error Handling** and user experience optimization

</details>

<details>
<summary><b> Versi Bahasa Indonesia</b></summary>

## ✨ Fitur

### 🤖 Multi-Assistant Finance AI
- **6 Asisten Spesialis**: Keuangan Pribadi, Analisis Investasi, Perencana Anggaran, Peneliti Ekonomi, Bantuan Pajak, Analisis Dokumen
- **Sistem Fallback Cerdas**: Pergantian model otomatis dengan redundansi
- **Dukungan Multibahasa**: Deteksi otomatis dan respons dalam bahasa Inggris/Indonesia
- **Chat Real-time**: Antarmuka menarik dengan timestamp dan info model

### 🎯 Finance Trivia Interaktif
- **180+ Pertanyaan**: Di 3 level kesulitan dengan penjelasan detail
- **Konten Bilingual**: Dukungan penuh Inggris dan Indonesia
- **Analitik Lanjutan**: Pelacakan performa, streak, dan analisis kategori
- **Feedback Real-time**: Skoring instan dengan visualisasi progres

### 📈 Kalkulator Keuangan Tingkat Lanjut
- **Analisis Saham**: Data pasar real-time dengan indikator teknikal (RSI, MACD, Moving Averages)
- **Perencana Investasi**: Bunga majemuk dengan penyesuaian pajak dan inflasi
- **Konverter Mata Uang**: Kurs tukar live dengan data historis
- **Kalkulator KPR**: Jadwal amortisasi lengkap

### 📚 Sumber Belajar
- **Konten Terkurasi**: 30+ channel YouTube dan website edukasi
- **Kategorisasi Profesional**: Diurutkan berdasarkan topik dan kesulitan
- **Bagian Bilingual**: Sumber daya terpisah Inggris dan Indonesia

## 🚀 Mulai Cepat

### Prasyarat
- Python 3.8+
- Akun OpenRouter API ([tersedia tier gratis](https://openrouter.ai))

### Instalasi

1. **Clone repository**
```bash
git clone https://github.com/yourusername/finance-learning-hub.git
cd finance-learning-hub
```

2. **Install dependensi**
```bash
pip install -r requirements.txt
```

3. **Konfigurasi API keys**
Buat `.streamlit/secrets.toml`:
```toml
OPENROUTER_API_KEY = "openrouter-api-key-anda-di-sini"
```

4. **Jalankan aplikasi**
```bash
streamlit run app.py
```

5. **Buka browser** ke `http://localhost:8501`

## 🏗️ Struktur Proyek

```
finance-learning-hub/
├── app.py                          # Aplikasi utama
├── pages/
│   ├── 1_🧠_Multi_Finance_AI.py    # Asisten AI (6 bot spesialis)
│   ├── 2_🎯_Finance_Trivia.py      # Game kuis interaktif
│   ├── 3_📈_Financial_Calculators.py # 4 kalkulator lanjutan
│   └── 4_📚_Learning_Resources.py   # Konten edukasi
├── requirements.txt                # Dependensi
├── README.md                      # Dokumentasi
└── .streamlit/
    └── secrets.toml              # Konfigurasi API
```

## 🛠️ Tech Stack

**Frontend & Framework**
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) - Framework aplikasi web
- ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly) - Visualisasi interaktif

**Backend & Data**
- ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) - Bahasa pemrograman inti
- ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) - Manipulasi data
- ![yFinance](https://img.shields.io/badge/yFinance-00A0D1?logo=yahoo) - Data keuangan

**APIs & Layanan Eksternal**
- ![OpenRouter](https://img.shields.io/badge/OpenRouter-FF6B35) - API AI multi-model
- ![Yahoo Finance](https://img.shields.io/badge/Yahoo_Finance-720E9B?logo=yahoo) - Data pasar

## 📊 Konsep Python yang Ditunjukkan

### 🏗️ Pemrograman Berorientasi Objek
```python
# Arsitektur class tingkat lanjut
class QuestionBank:          # Mengelola 180+ pertanyaan dengan kategori
class GameState:             # Manajemen session yang komprehensif  
class ExplanationGenerator:  # Sistem feedback dinamis
```

### 🗂️ Struktur Data
- **Dictionaries**: Konfigurasi asisten, terjemahan, bank pertanyaan
- **Lists & Arrays**: Pool pertanyaan, riwayat chat, data performa
- **Pandas DataFrame**: Analitik, jadwal amortisasi, data pasar

### ⚡ Kontrol Alur & Manajemen State
- **Session State**: Persistensi state multi-halaman
- **Penanganan Error**: Fallback API dan validasi input pengguna
- **Update Real-time**: Streaming data live dan update UI

## 🌐 Penyebaran

### Streamlit Cloud (Rekomendasi)
1. Push code ke GitHub
2. Hubungkan repository di [share.streamlit.io](https://share.streamlit.io)
3. Tambahkan `OPENROUTER_API_KEY` di secrets
4. Deploy dan bagikan URL publik

### HuggingFace Spaces
1. Buat Space baru dengan template Streamlit
2. Upload code dan `requirements.txt`
3. Konfigurasi secrets di Settings
4. Deploy otomatis saat push

## 📸 Preview Aplikasi

images/
├── ![Dashboard](images/dashboard.png)
├── ![AI Assistant](images/ai-assistant.png)
├── ![Finance Trivia](images/trivia-game.png)
├── ![Stock Analysis](images/stock-analysis.png)
├── ![Calculator](images/calculator.png)
└── ![Resources](images/resources.png)


## ❓ Pertanyaan Umum

### 🤖 Pertanyaan Asisten AI
**Q: Seberapa akurat saran keuangannya?**  
A: AI hanya memberikan informasi edukasional. Selalu konsultasikan dengan profesional bersertifikat untuk keputusan keuangan.

**Q: Model AI mana yang digunakan?**  
A: Beberapa model termasuk Qwen, DeepSeek, Gemini, Grok dengan fallback otomatis.

### 💰 Data Keuangan
**Q: Apakah data saham real-time?**  
A: Ya, selama jam pasar. Data bersumber dari Yahoo Finance API.

**Q: Seberapa sering kurs tukar diperbarui?**  
A: Kurs mata uang di-cache selama 10 menit dengan fallback API real-time.

### 🔧 Teknis
**Q: Bisakah digunakan di mobile?**  
A: Ya! Desain responsive bekerja di semua perangkat.

**Q: Apakah ada biaya?**  
A: Sepenuhnya gratis. OpenRouter API memiliki tier gratis yang cukup.

**Q: Bagaimana cara reset kuis?**  
A: Gunakan tombol "Restart" di sidebar atau refresh halaman.

## 🎯 Highlight Final Project

Proyek ini mendemonstrasikan **pemrograman Python tingkat lanjut** melalui:
- **Arsitektur Streamlit Multi-halaman** dengan navigasi mulus
- **Integrasi AI** dengan mekanisme fallback yang canggih  
- **Pemrosesan Data Real-time** dari berbagai API keuangan
- **UI/UX Profesional** dengan styling kustom dan visualisasi
- **Penanganan Error Komprehensif** dan optimasi pengalaman pengguna

</details>

---

**Built with ❤️ using Streamlit, OpenRouter API, and Python**  
**Developer**: [Ina37]  • **Year**: 2025

<div align="center">

### 🌟 If you find this project helpful, please give it a star!
Now users can easily switch between languages and the README looks much more professional! 🚀

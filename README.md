# Finance Learning Hub - Multipage Financial Education Platform

## English Version

### **Finance Learning Hub: Your Comprehensive Financial Education Platform!**
An interactive multipage Streamlit application featuring AI-powered financial assistants, interactive quizzes, real-time calculators, and educational resources. This project was created as a **Final Project** and demonstrates advanced Python programming with comprehensive financial education tools.

### **Project Description**
This multipage financial education platform uses Streamlit to integrate AI assistants, interactive quizzes, financial calculators, and educational resources. The application provides users with comprehensive financial learning tools in both English and Indonesian languages.

### **Key Features**

#### 🧠 **Multi-Assistant Finance AI**
- **6 Specialized Finance Assistants**: Personal Finance, Investment Analysis, Budget Planning, Economic Research, Tax Help, Document Analysis
- **Smart Multi-Model System**: Automatic fallback across multiple AI models
- **Real-time Chat Interface**: Beautiful chat bubbles with timestamps
- **Multilingual Support**: Auto-detection and response in user's preferred language
- **Customizable Settings**: Adjustable temperature and token limits

#### 🎯 **Interactive Finance Trivia**
- **180+ Questions**: Comprehensive question bank across 3 difficulty levels
- **Bilingual Support**: English and Indonesian questions and interface
- **Real-time Analytics**: Performance tracking with charts and statistics
- **Progress Tracking**: Streak counters, accuracy metrics, and category analysis

#### 📈 **Advanced Financial Calculators**
- **Real-time Stock Analysis**: Live market data with technical indicators
- **Investment Calculator**: Compound interest with inflation and tax adjustments
- **Currency Converter**: Real-time exchange rates with historical trends
- **Mortgage Calculator**: Complete amortization schedules

#### 📚 **Learning Resources**
- **Curated Content**: YouTube channels and websites for financial education
- **Bilingual Resources**: Separate English and Indonesian resource sections
- **Professional Categorization**: Organized by topic and difficulty level

### **Prerequisites**
Before running, make sure you have:
* Python 3.8+ installed
* Package manager `pip`
* OpenRouter API account (free tier available)

### **Installation & Setup**

1. **Clone or download the project**

2. **Install required packages:**
   ```bash
   pip install streamlit pandas plotly requests yfinance numpy
   ```

3. **Set up API configuration:**
   Create `.streamlit/secrets.toml` file:
   ```toml
   OPENROUTER_API_KEY = "your-openrouter-api-key-here"
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the application:**
   Open your browser to `http://localhost:8501`

### **Project Structure**
```
finance-learning-hub/
├── app.py                          # Main multipage application file
├── pages/
│   ├── 1_🧠_Multi_Finance_AI.py    # AI Assistant page
│   ├── 2_🎯_Finance_Trivia.py      # Interactive quiz game
│   ├── 3_📈_Financial_Calculators.py # Calculators & market data
│   └── 4_📚_Learning_Resources.py   # Educational resources
├── requirements.txt                # Python dependencies
├── README.md                      # Project documentation
└── .streamlit/
    └── secrets.toml              # API configuration
```

### **Available Features by Page**

#### 🏠 **Homepage**
- Overview of all available features
- Navigation instructions
- Feature cards with descriptions

#### 🧠 **Multi Finance AI**
- **💼 Personal Finance Advisor**: Budgeting, savings, debt management
- **📈 Investment Analyst**: Asset analysis, portfolio construction
- **📊 Budget Planner**: Budget creation and optimization
- **🏛️ Economic Researcher**: Macroeconomic analysis and reports
- **🧾 Tax Helper**: General tax information and concepts
- **📚 Document Analyzer**: Financial document processing

#### 🎯 **Finance Trivia**
- **🟢 Easy Level**: Basic financial literacy, budgeting, savings
- **🟡 Medium Level**: Investment concepts, financial analysis
- **🔴 Hard Level**: Advanced economics, market theories, risk management
- **Real-time Statistics**: Accuracy tracking, performance analytics

#### 📈 **Financial Calculators**
- **Stock Analysis**: Real-time market data with technical charts
- **Investment Calculator**: Future value projections with tax implications
- **Currency Converter**: Live exchange rates with historical trends
- **Mortgage Calculator**: Complete loan amortization schedules

#### 📚 **Learning Resources**
- **YouTube Channels**: Curated financial education content
- **Educational Websites**: Professional financial learning platforms
- **Bilingual Content**: Separate English and Indonesian resources

### **Tech Stack & Dependencies**

#### **Core Technologies**
* **Language**: Python 3.8+
* **Framework**: [![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?logo=streamlit)](https://streamlit.io/)
* **API Integration**: OpenRouter API for AI assistants
* **Data Analysis**: Pandas, NumPy
* **Visualization**: Plotly, Streamlit Charts
* **Financial Data**: yFinance for market data

#### **External Libraries**
```python
streamlit>=1.28.0      # Web application framework
pandas>=2.0.0          # Data manipulation and analysis
plotly>=5.0.0          # Interactive visualizations
requests>=2.31.0       # HTTP API calls
yfinance>=0.2.18       # Financial market data
numpy>=1.24.0          # Numerical computations
```

### **Python Concepts Applied**

#### **Object-Oriented Programming**
- **Class Management**: QuestionBank, GameState, ExplanationGenerator
- **Encapsulation**: Data hiding with properties and methods
- **Modularity**: Separate systems for each functionality

#### **Data Structures**
- **Dictionaries**: Assistant configurations, questions, translations
- **Lists**: Question pools, chat history, performance data
- **Pandas DataFrame**: Analytics, amortization schedules, market data

#### **Control Structures**
- **State Management**: Comprehensive session state management
- **Error Handling**: Exception handling for API and user input
- **Loop Optimization**: Efficient looping for calculations and rendering

### **Deployment**

#### **Streamlit Cloud Deployment**
1. Push code to GitHub repository
2. Connect repository to Streamlit Cloud
3. Add secrets in Streamlit dashboard:
   - `OPENROUTER_API_KEY`
4. Deploy and share public URL

### **Frequently Asked Questions (FAQ)**

**Q: How accurate are the financial AI assistants?**
A: The AI assistants provide educational information and are not professional financial advice. Always consult with certified financial advisors for important decisions.

**Q: Is the stock data real-time?**
A: Yes, stock data is fetched from Yahoo Finance and updated in real-time during market hours.

**Q: Can I use this app on mobile?**
A: Yes, the app is responsive and can be accessed through mobile browsers.

**Q: Is there any cost to use this application?**
A: The application is completely free. Only requires OpenRouter API key which is available in free tier.

**Q: How to reset the quiz?**
A: Use the "Restart" button in the sidebar or refresh the page to start a new quiz.

### **Application Preview**

#### **Main Dashboard**
![Dashboard](https://via.placeholder.com/800x400/667eea/FFFFFF?text=Finance+Learning+Hub+Dashboard)

#### **AI Chat Interface**
![AI Chat](https://via.placeholder.com/800x400/28a745/FFFFFF?text=Multi+Assistant+Finance+AI)

#### **Interactive Quiz**
![Quiz Game](https://via.placeholder.com/800x400/ffc107/FFFFFF?text=Finance+Trivia+Game)

#### **Financial Calculators**
![Calculators](https://via.placeholder.com/800x400/dc3545/FFFFFF?text=Advanced+Financial+Calculators)

---

## Versi Bahasa Indonesia

### **Finance Learning Hub: Platform Edukasi Keuangan Komprehensif Anda!**
Aplikasi Streamlit multipage interaktif yang menampilkan asisten keuangan berbasis AI, kuis interaktif, kalkulator real-time, dan sumber daya edukasi. Proyek ini dibuat sebagai **Final Project** dan mendemonstrasikan pemrograman Python tingkat lanjut dengan alat edukasi keuangan yang komprehensif.

### **Deskripsi Proyek**
Platform edukasi keuangan multipage menggunakan Streamlit yang mengintegrasikan asisten AI, kuis interaktif, kalkulator keuangan, dan sumber daya edukasi. Aplikasi ini menyediakan alat pembelajaran keuangan komprehensif dalam bahasa Inggris dan Indonesia.

### **Fitur Utama**

#### 🧠 **Multi-Assistant Finance AI**
- **6 Asisten Keuangan Spesialis**: Keuangan Pribadi, Analisis Investasi, Perencana Budget, Peneliti Ekonomi, Bantuan Pajak, Analisis Dokumen
- **Sistem Multi-Model Cerdas**: Fallback otomatis dengan redundansi
- **Antarmuka Chat Real-time**: Bubble chat menarik dengan timestamp
- **Dukungan Multibahasa**: Deteksi otomatis dan respons dalam bahasa pilihan pengguna
- **Pengaturan Dapat Disesuaikan**: Temperature dan batas token yang dapat diatur

#### 🎯 **Finance Trivia Interaktif**
- **180+ Pertanyaan**: Bank pertanyaan komprehensif di 3 level kesulitan
- **Dukungan Bilingual**: Pertanyaan dan antarmuka dalam Inggris dan Indonesia
- **Analitik Real-time**: Pelacakan performa dengan chart dan statistik
- **Pelacakan Progress**: Penghitung streak, metrik akurasi, dan analisis kategori

#### 📈 **Kalkulator Keuangan Advanced**
- **Analisis Saham Real-time**: Data pasar live dengan indikator teknikal
- **Kalkulator Investasi**: Bunga majemuk dengan penyesuaian inflasi dan pajak
- **Konverter Mata Uang**: Kurs tukar real-time dengan tren historis
- **Kalkulator KPR**: Jadwal amortisasi lengkap dengan PMI dan pajak

#### 📚 **Sumber Belajar**
- **Konten Terkurasi**: Channel YouTube dan website untuk edukasi keuangan
- **Sumber Bilingual**: Bagian sumber daya terpisah Inggris dan Indonesia
- **Kategorisasi Profesional**: Diurutkan berdasarkan topik dan level kesulitan

### **Prasyarat**
Sebelum menjalankan, pastikan Anda memiliki:
* Python 3.8+ terinstall
* Package manager `pip`
* Akun OpenRouter API (tersedia tier gratis)

### **Instalasi & Setup**

1. **Clone atau download proyek**

2. **Install package yang diperlukan:**
   ```bash
   pip install streamlit pandas plotly requests yfinance numpy
   ```

3. **Setup konfigurasi API:**
   Buat file `.streamlit/secrets.toml`:
   ```toml
   OPENROUTER_API_KEY = "openrouter-api-key-anda-di-sini"
   ```

4. **Jalankan aplikasi:**
   ```bash
   streamlit run app.py
   ```

5. **Akses aplikasi:**
   Buka browser ke `http://localhost:8501`

### **Struktur Proyek**
```
finance-learning-hub/
├── app.py                          # File aplikasi multipage utama
├── pages/
│   ├── 1_🧠_Multi_Finance_AI.py    # Halaman Asisten AI
│   ├── 2_🎯_Finance_Trivia.py      # Game kuis interaktif
│   ├── 3_📈_Financial_Calculators.py # Kalkulator & data pasar
│   └── 4_📚_Learning_Resources.py   # Sumber daya edukasi
├── requirements.txt                # Dependensi Python
├── README.md                      # Dokumentasi proyek
└── .streamlit/
    └── secrets.toml              # Konfigurasi API
```

### **Fitur yang Tersedia per Halaman**

#### 🏠 **Halaman Utama**
- Ringkasan semua fitur yang tersedia
- Petunjuk navigasi
- Kartu fitur dengan deskripsi

#### 🧠 **Multi Finance AI**
- **💼 Personal Finance Advisor**: Budgeting, tabungan, manajemen utang
- **📈 Investment Analyst**: Analisis aset, konstruksi portofolio
- **📊 Budget Planner**: Pembuatan dan optimasi budget
- **🏛️ Economic Researcher**: Analisis makroekonomi dan laporan
- **🧾 Tax Helper**: Informasi dan konsep pajak umum
- **📚 Document Analyzer**: Pemrosesan dokumen keuangan

#### 🎯 **Finance Trivia**
- **🟢 Level Mudah**: Literasi keuangan dasar, budgeting, tabungan
- **🟡 Level Sedang**: Konsep investasi, analisis keuangan
- **🔴 Level Sulit**: Ekonomi lanjutan, teori pasar, manajemen risiko
- **Statistik Real-time**: Pelacakan akurasi, analitik performa

#### 📈 **Kalkulator Keuangan**
- **Analisis Saham**: Data pasar real-time dengan chart teknikal
- **Kalkulator Investasi**: Proyeksi nilai masa depan dengan implikasi pajak
- **Konverter Mata Uang**: Kurs tukar live dengan tren historis
- **Kalkulator KPR**: Jadwal amortisasi pinjaman lengkap

#### 📚 **Sumber Belajar**
- **Channel YouTube**: Konten edukasi keuangan terkurasi
- **Website Edukasional**: Platform pembelajaran keuangan profesional
- **Konten Bilingual**: Sumber daya terpisah Inggris dan Indonesia

### **Tech Stack & Dependencies**

#### **Teknologi Inti**
* **Bahasa**: Python 3.8+
* **Framework**: [![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?logo=streamlit)](https://streamlit.io/)
* **Integrasi API**: OpenRouter API untuk asisten AI
* **Analisis Data**: Pandas, NumPy
* **Visualisasi**: Plotly, Streamlit Charts
* **Data Keuangan**: yFinance untuk data pasar

#### **Library Eksternal**
```python
streamlit>=1.28.0      # Framework aplikasi web
pandas>=2.0.0          # Manipulasi dan analisis data
plotly>=5.0.0          # Visualisasi interaktif
requests>=2.31.0       # Panggilan API HTTP
yfinance>=0.2.18       # Data pasar keuangan
numpy>=1.24.0          # Komputasi numerik
```

### **Konsep Python yang Diterapkan**

#### **Pemrograman Berorientasi Objek**
- **Manajemen Class**: QuestionBank, GameState, ExplanationGenerator
- **Enkapsulasi**: Penyembunyian data dengan properti dan metode
- **Modularitas**: Sistem terpisah untuk setiap fungsionalitas

#### **Struktur Data**
- **Dictionaries**: Konfigurasi asisten, pertanyaan, terjemahan
- **Lists**: Pool pertanyaan, riwayat chat, data performa
- **Pandas DataFrame**: Analitik, jadwal amortisasi, data pasar

#### **Struktur Kontrol**
- **Manajemen State**: Manajemen session state yang komprehensif
- **Penanganan Error**: Exception handling untuk API dan input user
- **Optimasi Loop**: Looping efisien untuk kalkulasi dan rendering

### **Penyebaran**

#### **Deployment Streamlit Cloud**
1. Push code ke repository GitHub
2. Hubungkan repository ke Streamlit Cloud
3. Tambahkan secrets di dashboard Streamlit:
   - `OPENROUTER_API_KEY`
4. Deploy dan bagikan URL publik

### **Pertanyaan Umum (FAQ)**

**Q: Seberapa akurat asisten AI keuangan ini?**
A: Asisten AI memberikan informasi edukasional dan bukan saran finansial profesional. Selalu konsultasikan dengan penasihat keuangan bersertifikat untuk keputusan penting.

**Q: Apakah data saham real-time?**
A: Ya, data saham diambil dari Yahoo Finance dan diperbarui secara real-time selama jam pasar.

**Q: Bisakah saya menggunakan aplikasi ini di mobile?**
A: Ya, aplikasi ini responsive dan dapat diakses melalui browser mobile.

**Q: Apakah ada biaya untuk menggunakan aplikasi ini?**
A: Aplikasi ini sepenuhnya gratis. Hanya membutuhkan API key OpenRouter yang tersedia dalam tier gratis.

**Q: Bagaimana cara reset kuis?**
A: Gunakan tombol "Restart" di sidebar atau refresh halaman untuk memulai kuis baru.

### **Preview Aplikasi**

#### **Dashboard Utama**
![Dashboard](https://via.placeholder.com/800x400/667eea/FFFFFF?text=Finance+Learning+Hub+Dashboard)

#### **Antarmuka Chat AI**
![AI Chat](https://via.placeholder.com/800x400/28a745/FFFFFF?text=Multi+Assistant+Finance+AI)

#### **Kuis Interaktif**
![Quiz Game](https://via.placeholder.com/800x400/ffc107/FFFFFF?text=Finance+Trivia+Game)

#### **Kalkulator Keuangan**
![Calculators](https://via.placeholder.com/800x400/dc3545/FFFFFF?text=Advanced+Financial+Calculators)

---

**Dibuat untuk Final Project - Platform Edukasi Keuangan**  
**Dibuat dengan ❤️ menggunakan Streamlit, OpenRouter API, dan Python**  
**Developer**: [Your Name]  
**Program**: [Your Program Name]  
**Tahun**: 2025
```


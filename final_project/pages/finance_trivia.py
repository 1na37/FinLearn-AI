import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import random
from datetime import datetime

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Finance Trivia Master",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================

def load_custom_css():
    """Load custom CSS styles for the application"""
    st.markdown("""
    <style>
        .score-card {
            padding: 1.5rem;
            border-radius: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        .question-card {
            padding: 2rem;
            border-radius: 15px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-left: 5px solid #667eea;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .correct-answer {
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border: 2px solid #28a745;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        .wrong-answer {
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
            border: 2px solid #dc3545;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        .difficulty-badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: bold;
            margin: 0.5rem;
        }
        .easy { background-color: #d4edda; color: #155724; }
        .medium { background-color: #fff3cd; color: #856404; }
        .hard { background-color: #f8d7da; color: #721c24; }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# DATA STRUCTURES AND CONSTANTS
# ============================================================================

TRANSLATIONS = {
    'en': {
        'title': 'Finance Trivia Master',
        'subtitle': 'Test Your Financial Knowledge',
        'select_difficulty': 'Select Difficulty',
        'easy': 'Easy', 
        'medium': 'Medium', 
        'hard': 'Hard',
        'start_game': 'Start Quiz',
        'streak': 'Streak',
        'correct': 'Correct',
        'wrong': 'Incorrect',
        'total_questions': 'Total Questions',
        'correct_ans': 'Correct Answers',
        'wrong_ans': 'Wrong Answers',
        'accuracy': 'Accuracy',
        'next_question': 'Next Question',
        'finish_quiz': 'Finish Quiz',
        'category': 'Category',
        'statistics': 'Final Statistics',
        'explanation': 'Explanation',
        'select_answer': 'Select your answer',
        'performance': 'Performance Trend',
        'question_num': 'Question',
        'of': 'of',
        'play_again': 'Play Again'
    },
    'id': {
        'title': 'Master Trivia Keuangan',
        'subtitle': 'Uji Pengetahuan Keuangan Anda',
        'select_difficulty': 'Pilih Kesulitan',
        'easy': 'Mudah', 
        'medium': 'Sedang', 
        'hard': 'Sulit',
        'start_game': 'Mulai Kuis',
        'streak': 'Beruntun',
        'correct': 'Benar',
        'wrong': 'Salah',
        'total_questions': 'Total Soal',
        'correct_ans': 'Jawaban Benar',
        'wrong_ans': 'Jawaban Salah',
        'accuracy': 'Akurasi',
        'next_question': 'Soal Berikutnya',
        'finish_quiz': 'Selesai Kuis',
        'category': 'Kategori',
        'statistics': 'Statistik Akhir',
        'explanation': 'Penjelasan',
        'select_answer': 'Pilih jawaban Anda',
        'performance': 'Tren Performa',
        'question_num': 'Soal',
        'of': 'dari',
        'play_again': 'Main Lagi'
    }
}

DIFFICULTY_COLORS = {
    'easy': '#28a745',
    'medium': '#ffc107',
    'hard': '#dc3545'
}

# ============================================================================
# CORE CLASSES
# ============================================================================


    
class QuestionBank: #"""Manages the question database for different languages and difficulties"""
    def __init__(self):
        self.questions = {
            'id': {
                'easy': [
                    {'question': 'Apa tujuan utama dari anggaran (budget)?', 'options': ['Membelanjakan lebih banyak uang', 'Melacak pemasukan dan pengeluaran', 'Membayar pajak', 'Menambah utang'], 'correct': 1, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Berikut ini contoh pemasukan adalah:', 'options': ['Tagihan listrik', 'Gaji', 'Belanja bulanan', 'Sewa rumah'], 'correct': 1, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'ATM adalah singkatan dari:', 'options': ['All Time Money', 'Automatic Teller Machine', 'Account Transfer Method', 'Available Transaction Module'], 'correct': 1, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Menabung di bank biasanya menghasilkan:', 'options': ['Bunga', 'Dividen', 'Pajak', 'Utang'], 'correct': 0, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Dana darurat digunakan untuk:', 'options': ['Berinvestasi di saham', 'Membayar pengeluaran tak terduga', 'Membeli barang mewah', 'Membayar tagihan rutin'], 'correct': 1, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Contoh pengeluaran tetap adalah:', 'options': ['Sewa rumah', 'Belanja mingguan', 'Tagihan listrik', 'Bensin'], 'correct': 0, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Apa itu utang?', 'options': ['Uang yang dipinjam/terutang', 'Uang yang disimpan', 'Uang yang diinvestasikan', 'Uang yang diperoleh'], 'correct': 0, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Berikut ini contoh kebutuhan, bukan keinginan:', 'options': ['Sepatu bermerek', 'Smartphone terbaru', 'Makanan', 'Konsol game'], 'correct': 2, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Fungsi utama bank adalah:', 'options': ['Untuk berjudi dengan uang', 'Menyimpan dan mengelola uang', 'Menjual barang', 'Membuat film'], 'correct': 1, 'category': 'Dasar Keuangan Pribadi'},
                    {'question': 'Membayar barang dengan kartu debit artinya:', 'options': ['Meminjam uang dari bank', 'Membayar dengan uang tabungan', 'Membayar dengan utang', 'Mendapat diskon otomatis'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Investasi jangka panjang biasanya dilakukan untuk:', 'options': ['Membeli makanan harian', 'Mencapai tujuan keuangan di masa depan', 'Membayar tagihan bulan ini', 'Mengurangi gaji'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Bunga pinjaman artinya:', 'options': ['Hadiah dari bank', 'Biaya tambahan karena meminjam uang', 'Pajak pemerintah', 'Tabungan otomatis'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Contoh aset adalah:', 'options': ['Televisi pribadi', 'Tagihan air', 'Pinjaman bank', 'Pajak tahunan'], 'correct': 0, 'category': 'Uang & Tabungan'},
                    {'question': 'Uang logam disebut juga:', 'options': ['Kartu kredit', 'Koin', 'Cek', 'Investasi'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Menyimpan uang di bawah bantal termasuk cara:', 'options': ['Aman', 'Tidak aman', 'Menguntungkan', 'Investasi modern'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Rekening tabungan biasanya:', 'options': ['Tidak memberikan bunga', 'Memberikan bunga kecil', 'Memberikan dividen besar', 'Menghapus pajak'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Tujuan utama asuransi kesehatan adalah:', 'options': ['Menabung uang', 'Melindungi dari biaya pengobatan besar', 'Membeli saham', 'Mengurangi pajak'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Contoh pengeluaran variabel adalah:', 'options': ['Cicilan KPR', 'Tagihan internet', 'Belanja makanan', 'Sewa rumah'], 'correct': 2, 'category': 'Uang & Tabungan'},
                    {'question': 'Jika pengeluaran lebih besar dari pemasukan, maka akan terjadi:', 'options': ['Tabungan meningkat', 'Utang bertambah', 'Kekayaan bertambah', 'Inflasi menurun'], 'correct': 1, 'category': 'Uang & Tabungan'},
                    {'question': 'Inflasi artinya:', 'options': ['Harga barang naik secara umum', 'Harga barang turun', 'Utang berkurang', 'Uang berkurang'], 'correct': 0, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Siapa yang mencetak uang di Indonesia?', 'options': ['OJK', 'Bank Indonesia', 'BPK', 'Kementerian Keuangan'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Investasi emas umumnya dianggap:', 'options': ['Sangat berisiko', 'Relatif aman', 'Sama dengan tabungan', 'Tidak berguna'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Contoh investasi jangka pendek adalah:', 'options': ['Deposito 3 bulan', 'Saham 10 tahun', 'Properti', 'Emas'], 'correct': 0, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Apa fungsi pasar modal?', 'options': ['Tempat jual beli barang kebutuhan', 'Tempat transaksi saham & obligasi', 'Tempat simpan uang', 'Tempat mencetak uang'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Obligasi adalah:', 'options': ['Surat tanda kepemilikan perusahaan', 'Surat utang yang diterbitkan pemerintah/perusahaan', 'Kartu debit', 'Pajak'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'OJK adalah singkatan dari:', 'options': ['Otoritas Jaminan Keuangan', 'Otoritas Jasa Keuangan', 'Organisasi Jasa Konsumen', 'Operasional Jaringan Kredit'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Jika harga barang naik, tapi pendapatan tetap, maka daya beli akan:', 'options': ['Naik', 'Turun', 'Sama saja', 'Tidak berpengaruh'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Contoh pajak tidak langsung adalah:', 'options': ['Pajak penghasilan', 'Pajak pertambahan nilai (PPN)', 'Pajak bumi & bangunan', 'Pajak kendaraan bermotor'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Ekonomi mikro mempelajari:', 'options': ['Perekonomian negara secara keseluruhan', 'Perilaku individu dan rumah tangga', 'Hubungan antarnegara', 'Kebijakan moneter'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                    {'question': 'Apa yang dimaksud dengan investasi?', 'options': ['Menabung uang di bank', 'Menggunakan uang untuk menghasilkan lebih banyak uang', 'Meminjam uang dari bank', 'Membelanjakan uang untuk kebutuhan sehari-hari'], 'correct': 1, 'category': 'Ekonomi Dasar & Investasi'},
                ],
                'medium': [
                    {'question': 'Diversifikasi dalam investasi bertujuan untuk:', 'options': ['Menambah risiko', 'Mengurangi risiko', 'Menghapus pajak', 'Menjamin untung'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Bunga majemuk (compound interest) adalah:', 'options': ['Bunga hanya dihitung dari modal awal', 'Bunga dihitung dari modal + bunga sebelumnya', 'Pajak tabungan', 'Biaya pinjaman'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Neraca keuangan menunjukkan:', 'options': ['Pendapatan dan pengeluaran', 'Aset, kewajiban, dan ekuitas', 'Proyeksi pertumbuhan', 'Dividen tahunan'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Pinjaman dengan bunga tertinggi biasanya:', 'options': ['KPR', 'Pinjaman mobil', 'Kartu kredit', 'Pinjaman mahasiswa'], 'correct': 2, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Dampak utama inflasi adalah:', 'options': ['Meningkatkan daya beli', 'Menurunkan daya beli', 'Membuat barang gratis', 'Menghapus utang'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Saham adalah:', 'options': ['Surat utang', 'Bukti kepemilikan perusahaan', 'Bentuk tabungan', 'Kartu kredit'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Rasio utang terhadap pendapatan sebaiknya:', 'options': ['Setinggi mungkin', 'Rendah', 'Tidak perlu dihitung', 'Sama dengan 100%'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Apa itu likuiditas?', 'options': ['Kemampuan aset diubah menjadi uang tunai', 'Jumlah utang', 'Jumlah investasi', 'Tingkat keuntungan'], 'correct': 0, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Dana pensiun adalah contoh:', 'options': ['Investasi jangka pendek', 'Investasi jangka panjang', 'Pengeluaran variabel', 'Aset lancar'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Jika suku bunga naik, harga obligasi biasanya:', 'options': ['Naik', 'Turun', 'Tetap', 'Tidak berpengaruh'], 'correct': 1, 'category': 'Manajemen Keuangan & Investasi'},
                    {'question': 'Kebijakan moneter dilakukan oleh:', 'options': ['Bank sentral', 'Pemerintah daerah', 'DPR', 'OJK'], 'correct': 0, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Pajak penghasilan termasuk pajak:', 'options': ['Langsung', 'Tidak langsung', 'Final', 'Konsumsi'], 'correct': 0, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Salah satu tujuan APBN adalah:', 'options': ['Menentukan harga saham', 'Mengatur penerimaan dan pengeluaran negara', 'Menghapus inflasi', 'Mengatur jumlah deposito'], 'correct': 1, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Permintaan barang akan turun jika:', 'options': ['Harga barang naik', 'Harga barang turun', 'Pendapatan naik', 'Barang jadi langka'], 'correct': 0, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Apa itu resesi?', 'options': ['Pertumbuhan ekonomi yang negatif dalam periode tertentu', 'Inflasi yang sangat tinggi', 'Jumlah uang beredar banyak', 'Harga saham naik'], 'correct': 0, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Supply dalam ekonomi artinya:', 'options': ['Permintaan', 'Penawaran', 'Utang', 'Pengeluaran'], 'correct': 1, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Ekonomi makro mempelajari:', 'options': ['Perilaku individu', 'Perekonomian secara keseluruhan', 'Perusahaan tunggal', 'Pasar lokal'], 'correct': 1, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Pajak pertambahan nilai (PPN) dikenakan pada:', 'options': ['Tabungan', 'Transaksi barang/jasa', 'Upah pekerja', 'Dana pensiun'], 'correct': 1, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Kenaikan upah minimum biasanya bertujuan untuk:', 'options': ['Mengurangi daya beli', 'Meningkatkan daya beli', 'Menaikkan pajak', 'Menghapus inflasi'], 'correct': 1, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Salah satu indikator inflasi adalah:', 'options': ['Indeks Harga Konsumen (IHK)', 'Produk Domestik Bruto (PDB)', 'Suku bunga acuan', 'Utang luar negeri'], 'correct': 0, 'category': 'Ekonomi & Pajak'},
                    {'question': 'Return investasi adalah:', 'options': ['Total utang', 'Keuntungan atau kerugian dari investasi', 'Jumlah aset', 'Pajak'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Risiko investasi saham lebih tinggi dibanding:', 'options': ['Deposito', 'Obligasi', 'Reksa dana campuran', 'Dana pensiun'], 'correct': 0, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Reksa dana adalah:', 'options': ['Pinjaman pemerintah', 'Investasi kolektif yang dikelola manajer investasi', 'Tabungan biasa', 'Pajak tahunan'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Yield obligasi adalah:', 'options': ['Harga pasar obligasi', 'Tingkat pengembalian obligasi', 'Pajak obligasi', 'Nilai nominal obligasi'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Risiko gagal bayar pada obligasi disebut:', 'options': ['Risiko likuiditas', 'Risiko kredit', 'Risiko inflasi', 'Risiko pasar'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Jika nilai tukar rupiah melemah, maka impor akan menjadi:', 'options': ['Lebih murah', 'Lebih mahal', 'Tetap', 'Gratis'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Apa itu deflasi?', 'options': ['Turunnya harga-harga secara umum', 'Naiknya harga-harga', 'Pertumbuhan ekonomi positif', 'Utang pemerintah naik'], 'correct': 0, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Saham blue chip adalah:', 'options': ['Saham perusahaan kecil', 'Saham perusahaan besar yang stabil', 'Saham startup', 'Saham spekulatif'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Instrumen investasi syariah yang mirip obligasi adalah:', 'options': ['Deposito', 'Sukuk', 'Saham preferen', 'Tabungan'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                    {'question': 'Rasio harga terhadap pendapatan (P/E ratio) digunakan untuk:', 'options': ['Menilai utang perusahaan', 'Menilai valuasi saham', 'Mengukur inflasi', 'Menentukan pajak'], 'correct': 1, 'category': 'Investasi Lanjutan & Risiko'},
                ],
                'hard': [
                    {'question': 'Teori yang menjelaskan hubungan risiko dan keuntungan adalah:', 'options': ['Teori Keynesian', 'Modern Portfolio Theory', 'Supply-side theory', 'Behavioral finance'], 'correct': 1, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Rasio P/E mengukur:', 'options': ['Price-to-Earnings', 'Profit-to-Equity', 'Purchase-to-Earnings', 'Price-to-Equity'], 'correct': 0, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Hipotesis Pasar Efisien menyatakan bahwa:', 'options': ['Pasar selalu dapat diprediksi', 'Harga saham mencerminkan semua informasi', 'Pemerintah menentukan harga saham', 'Investor bisa selalu mengalahkan pasar'], 'correct': 1, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Risiko sistematis adalah:', 'options': ['Risiko unik perusahaan', 'Risiko pasar yang tidak bisa dihindari', 'Risiko manajemen', 'Risiko penipuan'], 'correct': 1, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Contoh kebijakan fiskal adalah:', 'options': ['Pengeluaran pemerintah', 'Menetapkan suku bunga', 'Mengatur jumlah uang beredar', 'Operasi pasar terbuka'], 'correct': 0, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Beta dalam saham menunjukkan:', 'options': ['Risiko pasar relatif terhadap indeks', 'Nilai buku perusahaan', 'Laba bersih', 'Dividen per saham'], 'correct': 0, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Arbitrase adalah:', 'options': ['Spekulasi harga saham', 'Membeli dan menjual aset di dua pasar berbeda untuk keuntungan tanpa risiko', 'Membayar pajak lebih rendah', 'Investasi jangka panjang'], 'correct': 1, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'CAPM digunakan untuk menghitung:', 'options': ['Return wajar suatu aset', 'Inflasi', 'Pertumbuhan GDP', 'Pajak penghasilan'], 'correct': 0, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Saham preferen biasanya memberikan:', 'options': ['Hak suara lebih besar', 'Dividen tetap', 'Tidak ada dividen', 'Gratis saham biasa'], 'correct': 1, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Instrumen derivatif yang digunakan untuk lindung nilai adalah:', 'options': ['Futures & options', 'Deposito', 'Obligasi', 'Tabungan'], 'correct': 0, 'category': 'Teori Investasi & Pasar Modal'},
                    {'question': 'Stagflasi adalah kondisi:', 'options': ['Inflasi tinggi + pertumbuhan ekonomi rendah', 'Inflasi rendah + pertumbuhan tinggi', 'Deflasi + ekspansi ekonomi', 'Inflasi 0%'], 'correct': 0, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Hukum Okun menjelaskan hubungan antara:', 'options': ['Inflasi dan suku bunga', 'Pengangguran dan pertumbuhan ekonomi', 'Utang dan pajak', 'Kurs dan ekspor'], 'correct': 1, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Kurva Phillips menunjukkan hubungan antara:', 'options': ['Inflasi dan pengangguran', 'GDP dan inflasi', 'Ekspor dan impor', 'Pajak dan pertumbuhan'], 'correct': 0, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Gini ratio digunakan untuk mengukur:', 'options': ['Ketimpangan distribusi pendapatan', 'Inflasi', 'Pertumbuhan ekonomi', 'Likuiditas pasar'], 'correct': 0, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Eksternalitas negatif dari produksi adalah:', 'options': ['Manfaat sosial', 'Polusi', 'Pajak', 'Subsidi'], 'correct': 1, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Subsidi pemerintah biasanya diberikan untuk:', 'options': ['Menaikkan harga barang', 'Menurunkan harga barang', 'Mengurangi konsumsi', 'Meningkatkan inflasi'], 'correct': 1, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Kurs mengambang (floating exchange rate) artinya:', 'options': ['Ditentukan pemerintah', 'Ditentukan oleh pasar', 'Tetap selamanya', 'Sama dengan emas'], 'correct': 1, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Apa itu crowding out effect?', 'options': ['Pengeluaran pemerintah mengurangi investasi swasta', 'Inflasi tinggi menurunkan daya beli', 'Deflasi mendorong konsumsi', 'Utang luar negeri berkurang'], 'correct': 0, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Purchasing Power Parity (PPP) membandingkan:', 'options': ['Utang antarnegara', 'Daya beli antarnegara', 'Inflasi global', 'Pajak antarwilayah'], 'correct': 1, 'category': 'Ekonomi Lanjutan'},
                    {'question': 'Value at Risk (VaR) digunakan untuk:', 'options': ['Mengukur potensi kerugian maksimum', 'Menghitung pajak', 'Menentukan dividen', 'Mengukur GDP'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Rasio Current Ratio mengukur:', 'options': ['Likuiditas jangka pendek', 'Profitabilitas', 'Efisiensi', 'Valuasi saham'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Apa itu leverage?', 'options': ['Penggunaan utang untuk memperbesar potensi keuntungan', 'Menyimpan dana cadangan', 'Diversifikasi aset', 'Pajak perusahaan'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Risiko likuiditas artinya:', 'options': ['Risiko sulit menjual aset menjadi uang tunai', 'Risiko gagal bayar', 'Risiko pasar global', 'Risiko pajak'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Indeks harga saham gabungan (IHSG) adalah:', 'options': ['Indeks semua saham di BEI', 'Indeks saham AS', 'Indeks obligasi', 'Indeks reksa dana'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Hedging bertujuan untuk:', 'options': ['Menghilangkan semua risiko', 'Mengurangi risiko', 'Menambah risiko', 'Memperbesar keuntungan pasti'], 'correct': 1, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Analisis fundamental saham memperhatikan:', 'options': ['Grafik harga', 'Laporan keuangan', 'Pola candlestick', 'Tren harian'], 'correct': 1, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Analisis teknikal saham fokus pada:', 'options': ['Grafik harga & volume perdagangan', 'Neraca perusahaan', 'Utang pemerintah', 'Kebijakan fiskal'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Risiko inflasi paling berpengaruh pada:', 'options': ['Obligasi jangka panjang', 'Saham', 'Tabungan', 'Reksa dana'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Jika harga obligasi turun, yield obligasi akan:', 'options': ['Naik', 'Turun', 'Tetap', 'Hilang'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                    {'question': 'Apa itu Return on Investment (ROI)?', 'options': ['Rasio yang mengukur efisiensi investasi', 'Jumlah dividen yang dibayarkan', 'Tingkat bunga pinjaman', 'Nilai pasar saham'], 'correct': 0, 'category': 'Analisis & Risiko Keuangan'},
                ]
            },
            'en': {
                'easy': [
                    {'question': 'What is the main purpose of a budget?', 'options': ['To spend more money', 'To track income and expenses', 'To pay taxes', 'To increase debt'], 'correct': 1, 'category': 'Personal Finance Basics'},
                    {'question': 'Which of the following is an example of income?', 'options': ['Electricity bill', 'Salary', 'Monthly grocery shopping', 'House rent'], 'correct': 1, 'category': 'Personal Finance Basics'},
                    {'question': 'ATM is an abbreviation for:', 'options': ['All Time Money', 'Automatic Teller Machine', 'Account Transfer Method', 'Available Transaction Module'], 'correct': 1, 'category': 'Personal Finance Basics'},
                    {'question': 'Saving money in a bank usually earns:', 'options': ['Interest', 'Dividends', 'Taxes', 'Debt'], 'correct': 0, 'category': 'Personal Finance Basics'},
                    {'question': 'Emergency funds are used for:', 'options': ['Investing in stocks', 'Paying unexpected expenses', 'Buying luxury goods', 'Paying routine bills'], 'correct': 1, 'category': 'Personal Finance Basics'},
                    {'question': 'An example of a fixed expense is:', 'options': ['House rent', 'Weekly groceries', 'Electricity bill', 'Gasoline'], 'correct': 0, 'category': 'Personal Finance Basics'},
                    {'question': 'What is debt?', 'options': ['Money borrowed/owed', 'Money saved', 'Money invested', 'Money earned'], 'correct': 0, 'category': 'Personal Finance Basics'},
                    {'question': 'Which of the following is an example of a need, not a want:', 'options': ['Branded shoes', 'Latest smartphone', 'Food', 'Game console'], 'correct': 2, 'category': 'Personal Finance Basics'},
                    {'question': 'The main function of a bank is:', 'options': ['To gamble with money', 'To store and manage money', 'To sell goods', 'To make films'], 'correct': 1, 'category': 'Personal Finance Basics'},
                    {'question': 'Paying for goods with a debit card means:', 'options': ['Borrowing money from the bank', 'Paying with savings money', 'Paying with debt', 'Getting an automatic discount'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'Long-term investment is usually done for:', 'options': ['Buying daily food', 'Achieving future financial goals', 'Paying this month\'s bills', 'Reducing salary'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'Loan interest means:', 'options': ['A gift from the bank', 'An additional cost for borrowing money', 'Government tax', 'Automatic savings'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'An example of an asset is:', 'options': ['Personal television', 'Water bill', 'Bank loan', 'Annual tax'], 'correct': 0, 'category': 'Money & Savings'},
                    {'question': 'Metal currency is also called:', 'options': ['Credit card', 'Coin', 'Check', 'Investment'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'Storing money under the pillow is considered a way that is:', 'options': ['Safe', 'Unsafe', 'Profitable', 'Modern investment'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'A savings account usually:', 'options': ['Does not give interest', 'Gives small interest', 'Gives large dividends', 'Eliminates taxes'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'The main purpose of health insurance is:', 'options': ['Saving money', 'Protecting against large medical costs', 'Buying stocks', 'Reducing taxes'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'An example of a variable expense is:', 'options': ['Mortgage installment', 'Internet bill', 'Grocery shopping', 'House rent'], 'correct': 2, 'category': 'Money & Savings'},
                    {'question': 'If expenses are greater than income, what will happen:', 'options': ['Savings increase', 'Debt increases', 'Wealth increases', 'Inflation decreases'], 'correct': 1, 'category': 'Money & Savings'},
                    {'question': 'Inflation means:', 'options': ['General increase in the price of goods', 'Decrease in the price of goods', 'Debt decreases', 'Money decreases'], 'correct': 0, 'category': 'Basic Economics & Investment'},
                    {'question': 'Who prints money in Indonesia?', 'options': ['OJK (Financial Services Authority)', 'Bank Indonesia (Central Bank)', 'BPK (Audit Board of Indonesia)', 'Ministry of Finance'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'Investing in gold is generally considered:', 'options': ['Very risky', 'Relatively safe', 'The same as savings', 'Useless'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'An example of a short-term investment is:', 'options': ['3-month deposit', '10-year stock', 'Property', 'Gold'], 'correct': 0, 'category': 'Basic Economics & Investment'},
                    {'question': 'What is the function of the capital market?', 'options': ['A place to buy and sell necessities', 'A place for stock & bond transactions', 'A place to store money', 'A place to print money'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'A bond is:', 'options': ['Certificate of company ownership', 'Debt security issued by the government/company', 'Debit card', 'Tax'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'OJK is an abbreviation for:', 'options': ['Otoritas Jaminan Keuangan (Financial Guarantee Authority)', 'Otoritas Jasa Keuangan (Financial Services Authority)', 'Organisasi Jasa Konsumen (Consumer Services Organization)', 'Operasional Jaringan Kredit (Credit Network Operations)'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'If the price of goods increases, but income remains the same, purchasing power will:', 'options': ['Increase', 'Decrease', 'Remain the same', 'Not be affected'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'An example of an indirect tax is:', 'options': ['Income tax', 'Value Added Tax (VAT)', 'Land and building tax', 'Motor vehicle tax'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'Microeconomics studies:', 'options': ['The economy of the country as a whole', 'The behavior of individuals and households', 'Relations between countries', 'Monetary policy'], 'correct': 1, 'category': 'Basic Economics & Investment'},
                    {'question': 'What does ROI stand for?', 'options': ['Return on Investment', 'Rate of Interest', 'Risk of Inflation', 'Revenue on Income'], 'correct': 0, 'category': 'Basic Economics & Investment'},
                ],
                'medium': [
                    {'question': 'Diversification in investment aims to:', 'options': ['Increase risk', 'Reduce risk', 'Eliminate taxes', 'Guarantee profit'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'Compound interest is:', 'options': ['Interest is calculated only from the initial capital', 'Interest is calculated from capital + previous interest', 'Savings tax', 'Loan cost'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'A financial balance sheet shows:', 'options': ['Income and expenses', 'Assets, liabilities, and equity', 'Growth projections', 'Annual dividends'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'The loan with the highest interest is usually:', 'options': ['Mortgage', 'Car loan', 'Credit card', 'Student loan'], 'correct': 2, 'category': 'Financial Management & Investment'},
                    {'question': 'The main impact of inflation is:', 'options': ['Increasing purchasing power', 'Decreasing purchasing power', 'Making goods free', 'Eliminating debt'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'A stock is:', 'options': ['Debt security', 'Proof of company ownership', 'A form of savings', 'Credit card'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'The debt-to-income ratio should ideally be:', 'options': ['As high as possible', 'Low', 'No need to calculate', 'Equal to 100%'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'What is liquidity?', 'options': ['The ability of assets to be converted into cash', 'The amount of debt', 'The amount of investment', 'The rate of return'], 'correct': 0, 'category': 'Financial Management & Investment'},
                    {'question': 'A pension fund is an example of:', 'options': ['Short-term investment', 'Long-term investment', 'Variable expense', 'Current asset'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'If interest rates rise, bond prices usually:', 'options': ['Increase', 'Decrease', 'Remain the same', 'Not be affected'], 'correct': 1, 'category': 'Financial Management & Investment'},
                    {'question': 'Monetary policy is carried out by:', 'options': ['Central bank', 'Local government', 'Parliament (DPR)', 'OJK (Financial Services Authority)'], 'correct': 0, 'category': 'Economics & Tax'},
                    {'question': 'Income tax is considered a/an:', 'options': ['Direct tax', 'Indirect tax', 'Final tax', 'Consumption tax'], 'correct': 0, 'category': 'Economics & Tax'},
                    {'question': 'One goal of the State Budget (APBN) is:', 'options': ['Determining stock prices', 'Regulating state revenue and expenditure', 'Eliminating inflation', 'Regulating the amount of deposits'], 'correct': 1, 'category': 'Economics & Tax'},
                    {'question': 'Demand for goods will decrease if:', 'options': ['The price of goods increases', 'The price of goods decreases', 'Income increases', 'Goods become scarce'], 'correct': 0, 'category': 'Economics & Tax'},
                    {'question': 'What is a recession?', 'options': ['Negative economic growth over a certain period', 'Very high inflation', 'A large amount of money in circulation', 'Stock prices increase'], 'correct': 0, 'category': 'Economics & Tax'},
                    {'question': 'Supply in economics means:', 'options': ['Demand', 'Offering/Availability', 'Debt', 'Expenditure'], 'correct': 1, 'category': 'Economics & Tax'},
                    {'question': 'Macroeconomics studies:', 'options': ['Individual behavior', 'The economy as a whole', 'A single company', 'Local markets'], 'correct': 1, 'category': 'Economics & Tax'},
                    {'question': 'Value Added Tax (VAT) is imposed on:', 'options': ['Savings', 'Goods/services transactions', 'Workers\' wages', 'Pension funds'], 'correct': 1, 'category': 'Economics & Tax'},
                    {'question': 'Raising the minimum wage usually aims to:', 'options': ['Reduce purchasing power', 'Increase purchasing power', 'Raise taxes', 'Eliminate inflation'], 'correct': 1, 'category': 'Economics & Tax'},
                    {'question': 'One indicator of inflation is:', 'options': ['Consumer Price Index (CPI)', 'Gross Domestic Product (GDP)', 'Benchmark interest rate', 'Foreign debt'], 'correct': 0, 'category': 'Economics & Tax'},
                    {'question': 'Investment return is:', 'options': ['Total debt', 'Profit or loss from investment', 'Total assets', 'Tax'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                    {'question': 'The risk of stock investment is higher than:', 'options': ['Deposits', 'Bonds', 'Mixed mutual funds', 'Pension funds'], 'correct': 0, 'category': 'Advanced Investment & Risk'},
                    {'question': 'A mutual fund (Reksa Dana) is:', 'options': ['Government loan', 'Collective investment managed by an investment manager', 'Ordinary savings', 'Annual tax'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                    {'question': 'Bond yield is:', 'options': ['Market price of the bond', 'Rate of return on the bond', 'Bond tax', 'Nominal value of the bond'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                    {'question': 'The risk of default on a bond is called:', 'options': ['Liquidity risk', 'Credit risk', 'Inflation risk', 'Market risk'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                    {'question': 'If the rupiah exchange rate weakens, imports will become:', 'options': ['Cheaper', 'More expensive', 'Remain the same', 'Free'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                    {'question': 'What is deflation?', 'options': ['General decrease in prices', 'Increase in prices', 'Positive economic growth', 'Government debt increases'], 'correct': 0, 'category': 'Advanced Investment & Risk'},
                    {'question': 'Blue chip stocks are:', 'options': ['Small company stocks', 'Stocks of large, stable companies', 'Startup stocks', 'Speculative stocks'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                    {'question': 'A sharia investment instrument similar to a bond is:', 'options': ['Deposit', 'Sukuk', 'Preferred stock', 'Savings'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                    {'question': 'The Price-to-Earnings ratio (P/E ratio) is used to:', 'options': ['Assess company debt', 'Assess stock valuation', 'Measure inflation', 'Determine taxes'], 'correct': 1, 'category': 'Advanced Investment & Risk'},
                ],
                'hard': [
                    {'question': 'The theory that explains the relationship between risk and return is:', 'options': ['Keynesian Theory', 'Modern Portfolio Theory', 'Supply-side theory', 'Behavioral finance'], 'correct': 1, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'The P/E ratio measures:', 'options': ['Price-to-Earnings', 'Profit-to-Equity', 'Purchase-to-Earnings', 'Price-to-Equity'], 'correct': 0, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'The Efficient Market Hypothesis states that:', 'options': ['The market is always predictable', 'Stock prices reflect all information', 'The government determines stock prices', 'Investors can always beat the market'], 'correct': 1, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'Systematic risk is:', 'options': ['Unique company risk', 'Market risk that cannot be avoided', 'Management risk', 'Fraud risk'], 'correct': 1, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'An example of fiscal policy is:', 'options': ['Government spending', 'Setting interest rates', 'Regulating the money supply', 'Open market operations'], 'correct': 0, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'Beta in stocks indicates:', 'options': ['Market risk relative to the index', 'Company book value', 'Net profit', 'Dividend per share'], 'correct': 0, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'Arbitrage is:', 'options': ['Stock price speculation', 'Buying and selling assets in two different markets for risk-free profit', 'Paying lower taxes', 'Long-term investment'], 'correct': 1, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'The CAPM is used to calculate:', 'options': ['The fair return of an asset', 'Inflation', 'GDP growth', 'Income tax'], 'correct': 0, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'Preferred stock usually provides:', 'options': ['Greater voting rights', 'Fixed dividend', 'No dividend', 'Free common stock'], 'correct': 1, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'A derivative instrument used for hedging is:', 'options': ['Futures & options', 'Deposit', 'Bond', 'Savings'], 'correct': 0, 'category': 'Investment Theory & Capital Market'},
                    {'question': 'Stagflation is a condition of:', 'options': ['High inflation + low economic growth', 'Low inflation + high growth', 'Deflation + economic expansion', '0% inflation'], 'correct': 0, 'category': 'Advanced Economics'},
                    {'question': 'Okun\'s Law explains the relationship between:', 'options': ['Inflation and interest rates', 'Unemployment and economic growth', 'Debt and taxes', 'Exchange rates and exports'], 'correct': 1, 'category': 'Advanced Economics'},
                    {'question': 'The Phillips Curve shows the relationship between:', 'options': ['Inflation and unemployment', 'GDP and inflation', 'Exports and imports', 'Taxes and growth'], 'correct': 0, 'category': 'Advanced Economics'},
                    {'question': 'The Gini ratio is used to measure:', 'options': ['Income distribution inequality', 'Inflation', 'Economic growth', 'Market liquidity'], 'correct': 0, 'category': 'Advanced Economics'},
                    {'question': 'A negative externality of production is:', 'options': ['Social benefits', 'Pollution', 'Taxes', 'Subsidies'], 'correct': 1, 'category': 'Advanced Economics'},
                    {'question': 'Government subsidies are usually given to:', 'options': ['Increase the price of goods', 'Decrease the price of goods', 'Reduce consumption', 'Increase inflation'], 'correct': 1, 'category': 'Advanced Economics'},
                    {'question': 'Floating exchange rate means:', 'options': ['Determined by the government', 'Determined by the market', 'Fixed forever', 'Equal to gold'], 'correct': 1, 'category': 'Advanced Economics'},
                    {'question': 'What is the crowding out effect?', 'options': ['Government spending reduces private investment', 'High inflation reduces purchasing power', 'Deflation encourages consumption', 'Foreign debt decreases'], 'correct': 0, 'category': 'Advanced Economics'},
                    {'question': 'Purchasing Power Parity (PPP) compares:', 'options': ['Debt between countries', 'Purchasing power between countries', 'Global inflation', 'Taxes between regions'], 'correct': 1, 'category': 'Advanced Economics'},
                    {'question': 'Value at Risk (VaR) is used to:', 'options': ['Measure maximum potential loss', 'Calculate taxes', 'Determine dividends', 'Measure GDP'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'The Current Ratio measures:', 'options': ['Short-term liquidity', 'Profitability', 'Efficiency', 'Stock valuation'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'What is leverage?', 'options': ['Using debt to amplify potential profit', 'Saving reserve funds', 'Asset diversification', 'Corporate tax'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'Liquidity risk means:', 'options': ['The risk of difficulty selling assets for cash', 'The risk of default', 'Global market risk', 'Tax risk'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'The Jakarta Composite Index (IHSG) is:', 'options': ['Index of all stocks on the IDX', 'US stock index', 'Bond index', 'Mutual fund index'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'Hedging aims to:', 'options': ['Eliminate all risk', 'Reduce risk', 'Increase risk', 'Amplify guaranteed profit'], 'correct': 1, 'category': 'Financial Analysis & Risk'},
                    {'question': 'Stock fundamental analysis focuses on:', 'options': ['Price charts', 'Financial statements', 'Candlestick patterns', 'Daily trends'], 'correct': 1, 'category': 'Financial Analysis & Risk'},
                    {'question': 'Stock technical analysis focuses on:', 'options': ['Price charts & trading volume', 'Company balance sheet', 'Government debt', 'Fiscal policy'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'Inflation risk is most influential on:', 'options': ['Long-term bonds', 'Stocks', 'Savings', 'Mutual funds'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'If bond prices fall, bond yields will:', 'options': ['Increase', 'Decrease', 'Remain the same', 'Disappear'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                    {'question': 'What is Return on Investment (ROI)?', 'options': ['A ratio that measures investment efficiency', 'The amount of dividends paid', 'The interest rate on loans', 'The market value of stocks'], 'correct': 0, 'category': 'Financial Analysis & Risk'},
                ]
            }
        }
    
def get_shuffled_questions(self, lang, diff):
    """Get shuffled list of questions for specified language and difficulty"""
    questions = self.questions[lang][diff].copy()  # Make a copy to avoid modifying original
    random.shuffle(questions)  # Shuffle the questions order
    
    # Randomize answer positions so correct answer isn't always A or B
    for question in questions:
        options = question['options']
        correct_answer = options[question['correct']]
        
        options_with_correctness = [(opt, opt == correct_answer) for opt in options]
        random.shuffle(options_with_correctness)
        
        question['options'] = [opt for opt, _ in options_with_correctness]
        question['correct'] = next(i for i, (_, is_correct) in enumerate(options_with_correctness) if is_correct)
    
    return questions
    
class ExplanationGenerator:
    """Generates explanations for quiz answers"""
    
    @staticmethod
    def generate_explanation(correct_answer, category, lang):
        """Generate a simple explanation for the correct answer"""
        if lang == 'en':
            return f"**Correct answer: {correct_answer}**\n\nThis question was about **{category}**. Understanding these concepts helps build your financial knowledge."
        else:
            return f"**Jawaban benar: {correct_answer}**\n\nPertanyaan ini tentang **{category}**. Memahami konsep ini membantu membangun pengetahuan keuangan Anda."


class GameState:
    """Manages the game state and session variables"""
    
    def __init__(self):
        if 'initialized' not in st.session_state:
            self.reset_session()
            st.session_state.initialized = True
    
    def reset_session(self):
        """Reset all session state variables"""
        st.session_state.score = 0
        st.session_state.correct_answers = 0
        st.session_state.wrong_answers = 0
        st.session_state.current_question_idx = 0
        st.session_state.question_pool = []
        st.session_state.selected_answer = None
        st.session_state.answered = False
        st.session_state.game_started = False
        st.session_state.game_finished = False
        st.session_state.difficulty = 'easy'
        st.session_state.history = []
        st.session_state.streak = 0
        st.session_state.best_streak = 0
        st.session_state.language = 'en'
    
    def start_game(self, difficulty, question_bank, num_questions=8):
        """Initialize a new game with selected difficulty"""
        st.session_state.difficulty = difficulty
        st.session_state.game_started = True
        st.session_state.game_finished = False
        st.session_state.score = 0
        st.session_state.correct_answers = 0
        st.session_state.wrong_answers = 0
        st.session_state.current_question_idx = 0
        st.session_state.history = []
        st.session_state.streak = 0
        
        all_questions = question_bank.get_shuffled_questions(
            st.session_state.language,
            difficulty
        )
        st.session_state.question_pool = all_questions[:num_questions]
    
    def get_current_question(self):
        """Get the current question from the pool"""
        if st.session_state.current_question_idx < len(st.session_state.question_pool):
            return st.session_state.question_pool[st.session_state.current_question_idx]
        return None
    
    def submit_answer(self, answer_idx):
        """Submit an answer and update game state"""
        st.session_state.selected_answer = answer_idx
        st.session_state.answered = True
        
        current_q = self.get_current_question()
        is_correct = answer_idx == current_q['correct']
        
        if is_correct:
            st.session_state.correct_answers += 1
            st.session_state.streak += 1
            if st.session_state.streak > st.session_state.best_streak:
                st.session_state.best_streak = st.session_state.streak
        else:
            st.session_state.wrong_answers += 1
            st.session_state.streak = 0
        
        st.session_state.history.append({
            'question': current_q['question'],
            'correct': is_correct,
            'difficulty': st.session_state.difficulty,
            'category': current_q['category'],
            'timestamp': datetime.now()
        })
    
    def next_question(self):
        """Move to the next question or finish the game"""
        st.session_state.current_question_idx += 1
        st.session_state.selected_answer = None
        st.session_state.answered = False
        
        if st.session_state.current_question_idx >= len(st.session_state.question_pool):
            st.session_state.game_finished = True

# ============================================================================
# UI RENDERING FUNCTIONS
# ============================================================================

def render_score_card(label, value, background_color=None):
    """Render a score card with custom styling"""
    bg_style = f"background: {background_color};" if background_color else ""
    html_content = f"""
    <div class="score-card" style="{bg_style}">
        <div style="font-size: 0.9rem; opacity: 0.9;">{label}</div>
        <div style="font-size: 2rem;">{value}</div>
    </div>
    """
    return html_content


def render_start_screen(translations):
    """Render the game start screen"""
    t = translations
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 4rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin: 2rem auto;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        max-width: 800px;
    ">
        <h1 style="font-size: 4rem; margin: 0 0 1rem 0; font-weight: bold;">{t['title']}</h1>
        <p style="font-size: 2rem; margin: 0; opacity: 0.9;">{t['subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Language / Bahasa")
        lang_choice = st.radio(
            "",
            options=['en', 'id'],
            format_func=lambda x: 'English' if x == 'en' else 'Bahasa Indonesia',
            index=0 if st.session_state.language == 'en' else 1,
            horizontal=True,
            label_visibility='collapsed'
        )
        
        if lang_choice != st.session_state.language:
            st.session_state.language = lang_choice
            st.rerun()
        
        t = TRANSLATIONS[st.session_state.language]
        
        if st.session_state.language == 'en':
            st.markdown("""
            ### 📚 What You'll Learn:
            
            **🟢 Easy:** Budgeting, savings, basic investing  
            **🟡 Medium:** Financial analysis, strategies  
            **🔴 Hard:** Advanced concepts, market theories
            """)
        else:
            st.markdown("""
            ### 📚 Apa yang Akan Anda Pelajari:
            
            **🟢 Mudah:** Anggaran, tabungan, investasi dasar  
            **🟡 Sedang:** Analisis keuangan, strategi  
            **🔴 Sulit:** Konsep lanjutan, teori pasar
            """)

        st.markdown(f"### {t['select_difficulty']}")
        diff_map = {'easy': t['easy'], 'medium': t['medium'], 'hard': t['hard']} 
        selected_difficulty = st.radio(
            "",
            options=['easy', 'medium', 'hard'],
            format_func=lambda x: diff_map[x],
            label_visibility='collapsed'
        )

        st.markdown("---")        
        st.markdown("### 🔢 Quiz Length" if st.session_state.language == 'en' else "### 🔢 Panjang Kuis")
        slider_label = "Number of questions in your quiz:" if st.session_state.language == 'en' else "Jumlah soal dalam kuis Anda:"
        total_questions = st.slider(
            slider_label,
            min_value=5,
            max_value=30,
            value=10,
            key='question_count'
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        return selected_difficulty, t, total_questions


import streamlit as st

def render_sidebar_stats(translations):
    """Render sidebar statistics during active game"""
    t = translations
    restart = False

    st.sidebar.markdown("## 📊 Game Stats")
    st.sidebar.markdown("---")

    if st.session_state.game_started and not st.session_state.game_finished:
        total_q = len(st.session_state.question_pool)
        current_q = st.session_state.current_question_idx + 1
        
        # Calculate actual performance metrics
        correct = st.session_state.correct_answers
        wrong = st.session_state.wrong_answers
        answered = correct + wrong
        
        # Grouped metrics in 2 columns
        col1, col2 = st.sidebar.columns(2)
        with col1:
            st.metric("❓ " + t['question_num'], f"{current_q}/{total_q}")
            st.metric("✅ " + t['correct_ans'], correct)
        with col2:
            st.metric("❌ " + t['wrong_ans'], wrong)
            st.metric("🔥 " + t['streak'], st.session_state.streak)

        # Accuracy with progress bar
        if answered > 0:
            accuracy = (correct / answered) * 100
            st.sidebar.metric("🎯 " + t['accuracy'], f"{accuracy:.1f}%")
            st.sidebar.progress(int(accuracy))
        else:
            st.sidebar.metric("🎯 " + t['accuracy'], "0%")
            st.sidebar.progress(0)

        st.sidebar.markdown("---")
        restart = st.sidebar.button("🔄 Restart", use_container_width=True)

    elif st.session_state.game_finished:
        st.sidebar.markdown("### 🎉 Game Finished!")
        
        # Show final stats
        total_q = len(st.session_state.question_pool)
        correct = st.session_state.correct_answers
        wrong = st.session_state.wrong_answers
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            st.metric("✅ " + t['correct_ans'], correct)
            st.metric("❓ " + t['total_questions'], total_q)
        with col2:
            st.metric("❌ " + t['wrong_ans'], wrong)
            if total_q > 0:
                accuracy = (correct / total_q) * 100
                st.metric("🎯 " + t['accuracy'], f"{accuracy:.1f}%")
        
        st.sidebar.metric("🔥 " + "Best Streak", st.session_state.best_streak)
        
        st.sidebar.markdown("---")
        restart = st.sidebar.button("🔄 Restart", use_container_width=True)

    return restart


def render_active_game(game_state, explainer, translations):
    """Render the active game screen with current question"""
    t = translations
    current_q = game_state.get_current_question()
    
    if current_q is None:
        st.session_state.game_finished = True
        st.rerun()
    
    total_q = len(st.session_state.question_pool)
    current_num = st.session_state.current_question_idx + 1
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(render_score_card(
            t['question_num'],
            f"{current_num} {t['of']} {total_q}"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(render_score_card(
            t['streak'],
            st.session_state.streak
        ), unsafe_allow_html=True)
    
    with col3:
        diff_color = DIFFICULTY_COLORS[st.session_state.difficulty]
        st.markdown(render_score_card(
            t['select_difficulty'],
            t[st.session_state.difficulty].upper(),
            diff_color
        ), unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="question-card">
        <div style="margin-bottom: 1rem;">
            <span class="difficulty-badge {st.session_state.difficulty}">{t[st.session_state.difficulty]}</span>
            <span style="background: #667eea; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-weight: bold; float: right;">
                {t['category']}: {current_q['category']}
            </span>
        </div>
        <h2 style="color: #333; clear: both;">{current_q['question']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.answered:
        st.markdown(f"### {t['select_answer']}")
        
        for idx, option in enumerate(current_q['options']):
            if st.button(
                f"{chr(65+idx)}. {option}",
                key=f"opt_{idx}_{current_num}",
                use_container_width=True,
                type='secondary'
            ):
                game_state.submit_answer(idx)
                st.rerun()
    
    else:
        is_correct = st.session_state.selected_answer == current_q['correct']
        
        if is_correct:
            st.markdown(f"""
            <div class="correct-answer">
                <h3 style="color: #155724; margin: 0;">✓ {t['correct']}</h3>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="wrong-answer">
                <h3 style="color: #721c24; margin: 0;">✗ {t['wrong']}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        for idx, option in enumerate(current_q['options']):
            if idx == current_q['correct']:
                st.success(f"✓ {chr(65+idx)}. {option}")
            elif idx == st.session_state.selected_answer and not is_correct:
                st.error(f"✗ {chr(65+idx)}. {option}")
            else:
                st.info(f"  {chr(65+idx)}. {option}")
        
        if not is_correct:
            st.markdown("---")
            st.markdown(f"### {t['explanation']}")
            
            explanation = explainer.generate_explanation(
                current_q['options'][current_q['correct']],
                current_q['category'],
                st.session_state.language
            )
            st.markdown(explanation)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if current_num < total_q:
                if st.button(t['next_question'], use_container_width=True, type='primary'):
                    game_state.next_question()
                    st.rerun()
            else:
                if st.button(t['finish_quiz'], use_container_width=True, type='primary'):
                    game_state.next_question()
                    st.rerun()


def render_performance_chart(df, translations):
    """Render performance trend chart"""
    t = translations
    
    cumulative_correct = []
    cumulative_accuracy = []
    
    for i in range(len(df)):
        cumulative_correct.append(df.iloc[:i+1]['correct'].sum())
        cumulative_accuracy.append((cumulative_correct[-1] / (i + 1)) * 100)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(1, len(df) + 1)),
        y=cumulative_accuracy,
        mode='lines+markers',
        name='Accuracy',
        line=dict(color='#667eea', width=3),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.1)',
        marker=dict(size=8, color='#667eea'),
        hovertemplate='Question %{x}<br>Accuracy: %{y:.1f}%<extra></extra>'
    ))
    fig.update_layout(
        xaxis_title=t['question_num'],
        yaxis_title=f"{t['accuracy']} (%)",
        height=350,
        hovermode='x unified',
        showlegend=False,
        yaxis=dict(range=[0, 100])
    )
    
    return fig


def render_category_chart(df, translations):
    """Render category performance chart"""
    t = translations
    
    category_data = df.groupby('category').agg({
        'correct': ['sum', 'count']
    }).reset_index()
    category_data.columns = ['category', 'correct', 'total']
    category_data['accuracy'] = (category_data['correct'] / category_data['total'] * 100).round(1)
    
    fig = px.bar(
        category_data,
        x='category',
        y='accuracy',
        text='accuracy',
        color='accuracy',
        color_continuous_scale=['#dc3545', '#ffc107', '#28a745'],
        labels={'accuracy': f"{t['accuracy']} (%)", 'category': t['category']}
    )
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='outside',
        hovertemplate='%{x}<br>Accuracy: %{y:.1f}%<extra></extra>'
    )
    fig.update_layout(
        height=350,
        showlegend=False,
        yaxis=dict(range=[0, 110]),
        xaxis_tickangle=-45
    )
    
    return fig


def render_finish_screen(translations):
    """Render the game completion screen with statistics"""
    t = translations
    
    st.balloons()
    
    total_q = len(st.session_state.question_pool)
    accuracy = (st.session_state.correct_answers / total_q) * 100
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        completion_text = 'Quiz Complete!' if st.session_state.language == 'en' else 'Kuis Selesai!'
        st.markdown(f"""
        <div class="score-card" style="font-size: 2rem;">
            {completion_text}
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(render_score_card(
            t['total_questions'],
            total_q
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(render_score_card(
            t['correct_ans'],
            st.session_state.correct_answers,
            "linear-gradient(135deg, #28a745 0%, #20c997 100%)"
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown(render_score_card(
            t['wrong_ans'],
            st.session_state.wrong_answers,
            "linear-gradient(135deg, #dc3545 0%, #e83e8c 100%)"
        ), unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem;">
        <h1 style="font-size: 3rem; color: #667eea;">{accuracy:.1f}%</h1>
        <p style="font-size: 1.2rem; color: #666;">{t['accuracy']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"## {t['statistics']}")
    
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### {t['performance']}")
            fig = render_performance_chart(df, t)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown(f"### Performance by {t['category']}")
            fig = render_category_chart(df, t)
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### Detailed Breakdown")
        
        breakdown_data = []
        for idx, row in df.iterrows():
            breakdown_data.append({
                'No': idx + 1,
                'Category': row['category'],
                'Result': '✅ Correct' if row['correct'] else '❌ Wrong'
            })
        
        breakdown_df = pd.DataFrame(breakdown_data)
        
        st.dataframe(
            breakdown_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "No": st.column_config.NumberColumn("Question #", width="small"),
                "Category": st.column_config.TextColumn("Category", width="medium"),
                "Result": st.column_config.TextColumn("Result", width="medium")
            }
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(t['play_again'], use_container_width=True, type='primary'):
            return True
    
    return False


def render_footer():
    """Render application footer"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem 0;">
        <p>Built with Streamlit | Interactive Financial Learning</p>
        <p style="font-size: 0.9rem;">Improve your financial literacy one question at a time</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point"""
    
    load_custom_css()
    
    # Initialize language if not exists
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    game_state = GameState()
    question_bank = QuestionBank()
    explainer = ExplanationGenerator()
    
    t = TRANSLATIONS[st.session_state.language]
    
    with st.sidebar:
        should_restart = render_sidebar_stats(t)
        if should_restart:
            game_state.reset_session()
            st.rerun()
    
    if not st.session_state.game_started:
        selected_difficulty, t, total_questions = render_start_screen(TRANSLATIONS[st.session_state.language])
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(t['start_game'], use_container_width=True, type='primary'):
                game_state.start_game(selected_difficulty, question_bank, total_questions)
                st.rerun()
    
    elif st.session_state.game_finished:
        should_restart = render_finish_screen(t)
        if should_restart:
            game_state.reset_session()
            st.rerun()
    
    else:
        render_active_game(game_state, explainer, t)
    
    render_footer()


if __name__ == "__main__":
    main()

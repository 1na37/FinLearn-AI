import streamlit as st

def show_learning_resources():
    st.set_page_config(
        page_title="Financial Learning Resources",
        page_icon="📚",
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
        .resource-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
        }
        .channel-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 1rem 0;
            border-left: 4px solid #667eea;
        }
        .website-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 1rem 0;
            border-left: 4px solid #f093fb;
        }
        .description {
            color: #666;
            font-style: italic;
            margin-top: 0.5rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="resource-section">
        <h1>📚 Free Financial Learning Resources</h1>
        <p>Comprehensive collection of YouTube channels and websites to enhance your financial knowledge</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Language selection
    col1, col2 = st.columns([1, 4])
    with col1:
        language = st.radio(
            "Select Language:",
            ["English", "Bahasa Indonesia"],
            index=0
        )
    
    st.markdown("---")
    
    if language == "English":
        show_english_resources()
    else:
        show_indonesian_resources()

def show_english_resources():
    st.markdown("## 🎥 YouTube Channels")
    
    english_channels = [
        {
            "name": "The Financial Diet",
            "url": "https://www.youtube.com/@thefinancialdiet",
            "description": "Budgeting, saving, and lifestyle finance for millennials"
        },
        {
            "name": "Graham Stephan",
            "url": "https://www.youtube.com/@GrahamStephan",
            "description": "Real estate investing, credit cards, passive income strategies"
        },
        {
            "name": "Andrei Jikh",
            "url": "https://www.youtube.com/@AndreiJikh",
            "description": "Stock investing, index funds, financial independence"
        },
        {
            "name": "Minority Mindset",
            "url": "https://www.youtube.com/@MinorityMindset",
            "description": "Wealth building, entrepreneurship, money mindset"
        },
        {
            "name": "Two Cents (PBS)",
            "url": "https://www.youtube.com/@TwoCentsPBS",
            "description": "Economics and personal finance explained simply"
        },
        {
            "name": "Our Rich Journey",
            "url": "https://www.youtube.com/@OurRichJourney",
            "description": "Financial independence, early retirement (FIRE)"
        },
        {
            "name": "The Plain Bagel",
            "url": "https://www.youtube.com/@ThePlainBagel",
            "description": "Investment concepts, financial news, market analysis"
        },
        {
            "name": "Ben Felix",
            "url": "https://www.youtube.com/@BenFelixCSI",
            "description": "Evidence-based investing, portfolio management"
        },
        {
            "name": "Marko - WhiteBoard Finance",
            "url": "https://www.youtube.com/@WhiteboardFinance",
            "description": "Stocks, ETFs, retirement accounts for beginners"
        },
        {
            "name": "Financial Education",
            "url": "https://www.youtube.com/@FinancialEducationJeremyPS1",
            "description": "Stock market investing and company analysis"
        },
        {
            "name": "Dave Ramsey",
            "url": "https://www.youtube.com/@TheDaveRamseyShow",
            "description": "Debt elimination, budgeting, financial peace"
        },
        {
            "name": "Money Guy Show",
            "url": "https://www.youtube.com/@moneyguy",
            "description": "Comprehensive financial planning and wealth building"
        },
        {
            "name": "Nate O'Brien",
            "url": "https://www.youtube.com/@NateOBrien",
            "description": "Passive income, investing for young adults"
        },
        {
            "name": "The Swedish Investor",
            "url": "https://www.youtube.com/@TheSwedishInvestor",
            "description": "Classic investment book summaries and strategies"
        },
        {
            "name": "Patrick Boyle",
            "url": "https://www.youtube.com/@PBoyle",
            "description": "Finance professor explaining markets and economics"
        }
    ]
    
    # Display channels in columns
    cols = st.columns(2)
    for idx, channel in enumerate(english_channels):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="channel-card">
                <h3>🎬 {channel['name']}</h3>
                <p><a href="{channel['url']}" target="_blank">{channel['url']}</a></p>
                <p class="description">{channel['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 🌐 Websites")
    
    english_websites = [
        {
            "name": "Investopedia",
            "url": "https://www.investopedia.com",
            "description": "Financial dictionary, investing tutorials, market analysis"
        },
        {
            "name": "Khan Academy Finance",
            "url": "https://www.khanacademy.org/economics-finance-domain",
            "description": "Free courses on economics, finance, and investing"
        },
        {
            "name": "Mr. Money Mustache",
            "url": "https://www.mrmoneymustache.com",
            "description": "Early retirement, frugal living, financial independence"
        },
        {
            "name": "NerdWallet",
            "url": "https://www.nerdwallet.com",
            "description": "Credit cards, banking, investing comparison and guides"
        },
        {
            "name": "Bogleheads",
            "url": "https://www.bogleheads.org",
            "description": "Index fund investing, low-cost investment strategies"
        },
        {
            "name": "The Balance",
            "url": "https://www.thebalancemoney.com",
            "description": "Personal finance guides, budgeting, investing basics"
        },
        {
            "name": "Financial Samurai",
            "url": "https://www.financialsamurai.com",
            "description": "Wealth building, real estate, passive income"
        },
        {
            "name": "Get Rich Slowly",
            "url": "https://www.getrichslowly.org",
            "description": "Personal finance stories, money management tips"
        },
        {
            "name": "ChooseFI",
            "url": "https://www.choosefi.com",
            "description": "Financial independence community and resources"
        },
        {
            "name": "Mad Fientist",
            "url": "https://www.madfientist.com",
            "description": "Tax optimization, early retirement strategies"
        },
        {
            "name": "Reddit r/personalfinance",
            "url": "https://www.reddit.com/r/personalfinance",
            "description": "Community Q&A, financial advice, wiki guides"
        },
        {
            "name": "Morningstar",
            "url": "https://www.morningstar.com",
            "description": "Investment research, fund analysis, market data"
        },
        {
            "name": "Corporate Finance Institute",
            "url": "https://corporatefinanceinstitute.com/resources",
            "description": "Free finance courses, career resources, articles"
        },
        {
            "name": "MyMoneyBlog",
            "url": "https://www.mymoneyblog.com",
            "description": "Investing strategies, credit card deals, savings tips"
        },
        {
            "name": "Wallet Hacks",
            "url": "https://wallethacks.com",
            "description": "Money hacks, investing tips, financial strategies"
        }
    ]
    
    # Display websites in columns
    cols = st.columns(2)
    for idx, website in enumerate(english_websites):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="website-card">
                <h3>🌐 {website['name']}</h3>
                <p><a href="{website['url']}" target="_blank">{website['url']}</a></p>
                <p class="description">{website['description']}</p>
            </div>
            """, unsafe_allow_html=True)

def show_indonesian_resources():
    st.markdown("## 🎥 YouTube Channels")
    
    indonesian_channels = [
        {
            "name": "Felicia Putri Tjiasaka",
            "url": "https://www.youtube.com/@feliciaputritjiasaka",
            "description": "Keuangan pribadi, investasi, dan mindset uang"
        },
        {
            "name": "Finansialku",
            "url": "https://www.youtube.com/@finansialku_com",
            "description": "Perencanaan keuangan, tips investasi, literasi keuangan"
        },
        {
            "name": "Erico Darmawan Handoyo",
            "url": "https://www.youtube.com/@ericohandoyo",
            "description": "Investasi saham, trading, analisis pasar modal"
        },
        {
            "name": "Raymond Chin",
            "url": "https://www.youtube.com/@RaymondChin",
            "description": "Bisnis, investasi, pengembangan diri"
        },
        {
            "name": "Investor Pemula",
            "url": "https://www.youtube.com/@investorpemula",
            "description": "Panduan investasi saham untuk pemula"
        },
        {
            "name": "Ngomongin Uang",
            "url": "https://www.youtube.com/@NgomongInUang",
            "description": "Edukasi keuangan, investasi, tips mengelola uang"
        },
        {
            "name": "Rivan Kurniawan",
            "url": "https://www.youtube.com/@RivanKurniawan",
            "description": "Properti, investasi, pengembangan diri"
        },
        {
            "name": "Denny Santoso",
            "url": "https://www.youtube.com/@DennySantosoTV",
            "description": "Bisnis, investasi, strategi keuangan"
        },
        {
            "name": "Ligwina Hananto",
            "url": "https://www.youtube.com/@ligwinahananto",
            "description": "Perencana keuangan, tips mengelola keuangan keluarga"
        },
        {
            "name": "Jouska Indonesia",
            "url": "https://www.youtube.com/@JouskaIndonesia",
            "description": "Konsultasi keuangan, solusi masalah finansial"
        },
        {
            "name": "Ajaib Sekuritas",
            "url": "https://www.youtube.com/@AjaibSekuritas",
            "description": "Investasi saham, reksadana, edukasi pasar modal"
        },
        {
            "name": "Sobat Budget",
            "url": "https://www.youtube.com/@sobatbudget",
            "description": "Budgeting, saving tips, manajemen keuangan"
        },
        {
            "name": "QM Financial",
            "url": "https://www.youtube.com/@QMFinancial",
            "description": "Perencanaan keuangan profesional, investasi"
        },
        {
            "name": "Ternak Uang",
            "url": "https://www.youtube.com/@TernakUang",
            "description": "Investasi, passive income, wealth building"
        },
        {
            "name": "Financial Advisor Indonesia",
            "url": "https://www.youtube.com/@FinancialAdvisorIndonesia",
            "description": "Konsultasi keuangan, tips investasi dan asuransi"
        }
    ]
    
    # Display channels in columns
    cols = st.columns(2)
    for idx, channel in enumerate(indonesian_channels):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="channel-card">
                <h3>🎬 {channel['name']}</h3>
                <p><a href="{channel['url']}" target="_blank">{channel['url']}</a></p>
                <p class="description">{channel['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 🌐 Websites")
    
    indonesian_websites = [
        {
            "name": "Finansialku",
            "url": "https://www.finansialku.com",
            "description": "Portal perencanaan keuangan, artikel, kalkulator"
        },
        {
            "name": "QM Financial",
            "url": "https://www.qmfinancial.com",
            "description": "Konsultasi dan edukasi perencanaan keuangan"
        },
        {
            "name": "Cermati",
            "url": "https://www.cermati.com",
            "description": "Perbandingan produk keuangan, kartu kredit, pinjaman"
        },
        {
            "name": "DuitPintar",
            "url": "https://www.duitpintar.com",
            "description": "Tips keuangan, investasi, asuransi"
        },
        {
            "name": "Bareksa",
            "url": "https://www.bareksa.com/id/text/category/berita",
            "description": "Platform reksadana, artikel investasi"
        },
        {
            "name": "Duwitmu (OJK)",
            "url": "https://sikapiuangmu.ojk.go.id",
            "description": "Literasi keuangan resmi dari OJK"
        },
        {
            "name": "IDX (Bursa Efek Indonesia)",
            "url": "https://www.idx.co.id/id/produk/edukasi",
            "description": "Edukasi pasar modal, investasi saham"
        },
        {
            "name": "Lifepal",
            "url": "https://lifepal.co.id/media",
            "description": "Asuransi, investasi, perencanaan keuangan"
        },
        {
            "name": "KoinWorks",
            "url": "https://koinworks.com/blog",
            "description": "P2P lending, investasi, tips keuangan"
        },
        {
            "name": "Pluang",
            "url": "https://www.pluang.com/id/blog",
            "description": "Investasi emas, saham, crypto untuk pemula"
        },
        {
            "name": "Bibit",
            "url": "https://blog.bibit.id",
            "description": "Reksadana, investasi otomatis, edukasi"
        },
        {
            "name": "Stockbit",
            "url": "https://stockbit.com",
            "description": "Komunitas investor, analisis saham, diskusi"
        },
        {
            "name": "Kontan",
            "url": "https://www.kontan.co.id",
            "description": "Berita ekonomi dan bisnis Indonesia"
        },
        {
            "name": "Seputar Forex",
            "url": "https://www.seputarforex.com/id",
            "description": "Trading forex, analisis pasar, edukasi"
        },
        {
            "name": "Kompas - Finansial",
            "url": "https://money.kompas.com",
            "description": "Berita keuangan, ekonomi, bisnis"
        }
    ]
    
    # Display websites in columns
    cols = st.columns(2)
    for idx, website in enumerate(indonesian_websites):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="website-card">
                <h3>🌐 {website['name']}</h3>
                <p><a href="{website['url']}" target="_blank">{website['url']}</a></p>
                <p class="description">{website['description']}</p>
            </div>
            """, unsafe_allow_html=True)

def main():
    show_learning_resources()

if __name__ == "__main__":
    main()
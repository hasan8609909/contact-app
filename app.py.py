import streamlit as st

# পেজ কনফিগারেশন
st.set_page_config(page_title="কন্টাক্ট ডিরেক্টরি সার্চ", page_icon="📱", layout="centered")

# কাস্টম ডার্ক এবং গ্লাসমোরফিজম সিএসএস (CSS)
st.markdown("""
    <style>
    /* মূল ব্যাকগ্রাউন্ড ও ডার্ক থিম */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #ffffff;
    }
    
    /* হেডার কার্ড স্টাইলিং */
    .header-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* ইনপুট ফিল্ড কাস্টমাইজেশন */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        color: white !important;
    }
    
    div[data-baseweb="input"] input {
        color: white !important;
    }

    /* বাটনের ডিজাইন */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #0083B0;
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# সেশন স্টেটে কন্টাক্ট ডেটা লোড করা
if "contacts" not in st.session_state:
    st.session_state.contacts = {
        "Shaik Nazrul Islam": {"e-TIN": "2886 9380 3054", "Circle": "34", "Zone": "3", "Number": "1"},
        "Abu Yousuf Joarder": {"e-TIN": "6583 6368 2606", "Circle": "138", "Zone": "8", "Number": "2"},
        "G M Khorshed Alam": {"e-TIN": "5672 3372 1805", "Circle": "186", "Zone": "9", "Number": "3"},
        "Rawshan Ara Kabir": {"e-TIN": "6977 7389 7003", "Circle": "235", "Zone": "11", "Number": "4"},
        "Farooq Ahmed": {"e-TIN": "7881 4121 7843", "Circle": "41", "Zone": "02", "Number": "5"},
        "Abdullah Al Mahmud": {"e-TIN": "6707 8250 6247", "Circle": "55", "Zone": "03", "Number": "6"},
        "Towfiq Elahi": {"e-TIN": "1288 0833 3865", "Circle": "152", "Zone": "07", "Number": "7"},
        "Mohammad Humayun Kabir": {"e-TIN": "4561 6667 0072", "Circle": "130", "Zone": "06", "Number": "8"},
        "Md Shahjahan Ali": {"e-TIN": "6881 1133 8091", "Circle": "241", "Zone": "11", "Number": "9"},
        "Saleha Sarwar": {"e-TIN": "1686 3877 2479", "Circle": "159", "Zone": "08", "Number": "10"},
        "Saida Begum": {"e-TIN": "8249 7955 4462", "Circle": "276", "Zone": "13", "Number": "11"},
        "Fariha Binte Quayum": {"e-TIN": "1840 3722 6881", "Circle": "215", "Zone": "10", "Number": "12"},
        "Sabera Belal": {"e-TIN": "4770 3972 1039", "Circle": "55", "Zone": "03", "Number": "13"},
        "Zakia Binte Quayum": {"e-TIN": "3243 3742 7116", "Circle": "41", "Zone": "02", "Number": "14"},
        "Gulshan Ara Begum": {"e-TIN": "7841 2955 1338", "Circle": "215", "Zone": "10", "Number": "15"},
        "Rawsan Ara Kibria": {"e-TIN": "1558 0588 2091", "Circle": "215", "Zone": "10", "Number": "16"},
        "A S Md Nazmul Huda": {"e-TIN": "1623 8479 4917", "Circle": "71", "Zone": "04", "Number": "17"},
        "Mahmuda Sultana": {"e-TIN": "8222 5736 0152", "Circle": "122", "Zone": "06", "Number": "18"},
        "Jakia Jasmin": {"e-TIN": "3950 3125 2471", "Circle": "323", "Zone": "15", "Number": "19"},
        "Sharmin Sultana (Neamul 173)": {"e-TIN": "2929 4120 2763", "Circle": "130", "Zone": "06", "Number": "20"},
        "Ms Joysna Khatun": {"e-TIN": "8231 3539 9302", "Circle": "92", "Zone": "05", "Number": "21"},
        "Sharmin Sultana (Bhabi 165)": {"e-TIN": "7525 2655 8124", "Circle": "176", "Zone": "08", "Number": "23"},
        "Munshi Darul Islam": {"e-TIN": "5670 6736 5297", "Circle": "122", "Zone": "06", "Number": "24"},
        "Dipa Chowdhury (Bhabi Munshi Bhai)": {"e-TIN": "2455 1782 9010", "Circle": "11", "Zone": "01", "Number": "25"},
        "Shaikh Sameen Yasar": {"e-TIN": "5814 1936 9401", "Circle": "281", "Zone": "13", "Number": "26"},
        "Mohammad Neamul Hasan (173)": {"e-TIN": "7641 5864 2013", "Circle": "190", "Zone": "09", "Number": "27"},
        "MD SHAFIQUL ISLAM": {"e-TIN": "2299 1357 0161", "Circle": "131", "Zone": "06", "Number": "28"}
    }

# টাইটেল এরিয়া
st.markdown("""
    <div class="header-card">
        <h2 style="color: white; margin:0;">📱 কন্টাক্ট ডিরেক্টরি সার্ভিস</h2>
    </div>
""", unsafe_allow_html=True)

# ১. সার্চ ইন্টারফেস
search_query = st.text_input("", placeholder="🔍 নাম দিয়ে অনুসন্ধান করুন").strip()

if search_query:
    matched_results = {
        name: info for name, info in st.session_state.contacts.items() 
        if name.lower().startswith(search_query.lower())
    }

    if matched_results:
        st.write(f"**পাওয়া গেছে ({len(matched_results)} টি):**")
        for name, info in matched_results.items():
            with st.expander(f"👤 {name}", expanded=True):
                st.write(f"**e-TIN:** {info.get('e-TIN', 'N/A')}")
                st.write(f"**Circle:** {info.get('Circle', 'N/A')}")
                st.write(f"**Zone:** {info.get('Zone', 'N/A')}")
                if "Number" in info:
                    st.write(f"**Number:** {info.get('Number')}")
    else:
        st.warning("এই নামে কোনো তথ্য পাওয়া যায়নি।")
else:
    st.markdown("<p style='text-align: center; color: #888;'>উপরে নাম টাইপ করে সার্চ করুন</p>", unsafe_allow_html=True)

st.markdown("---")

# ২. কন্টাক্ট ম্যানেজমেন্ট (যোগ ও মুছে ফেলা)
tab1, tab2 = st.tabs(["➕ নতুন কন্টাক্ট যোগ করুন", "🗑️ কন্টাক্ট মুছে ফেলুন"])

# কন্টাক্ট যোগ করা
with tab1:
    new_name = st.text_input("নাম (Assessee Name)")
    new_etin = st.text_input("e-TIN")
    new_circle = st.text_input("Circle")
    new_zone = st.text_input("Zone")
    new_number = st.text_input("Number (সিরিয়াল বা মো.)")
    
    if st.button("কন্টাক্ট সেভ করুন"):
        if new_name.strip():
            st.session_state.contacts[new_name.strip()] = {
                "e-TIN": new_etin,
                "Circle": new_circle,
                "Zone": new_zone,
                "Number": new_number
            }
            st.success(f"'{new_name}' সফলভাবে যোগ করা হয়েছে!")
        else:
            st.error("অনুগ্রহ করে নামটি লিখুন।")

# কন্টাক্ট মুছে ফেলা
with tab2:
    if st.session_state.contacts:
        delete_name = st.selectbox("মুছে ফেলার জন্য কন্টাক্ট সিলেক্ট করুন", list(st.session_state.contacts.keys()))
        if st.button("কন্টাক্ট মুছে ফেলুন"):
            del st.session_state.contacts[delete_name]
            st.success(f"'{delete_name}' সফলভাবে মুছে ফেলা হয়েছে!")
            st.rerun()
    else:
        st.info("কোনো কন্টাক্ট পাওয়া যায়নি।")

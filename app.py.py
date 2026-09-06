import os
import streamlit as st

# পেজ কনফিগারেশন
st.set_page_config(page_title="কন্টাক্ট ডিরেক্টরি সার্ভিস", page_icon="📱", layout="centered")

# ১. ভিজিটর/ভিউ গণনা করার ফাইল লজিক
def get_and_update_views():
    file_path = "views.txt"
    views = 0
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                views = int(f.read().strip())
            except ValueError:
                views = 0
    
    if "already_visited" not in st.session_state:
        views += 1
        st.session_state.already_visited = True
        with open(file_path, "w") as f:
            f.write(str(views))
            
    return views

total_views = get_and_update_views()

# CSS ডিজাইন ফিক্সিং
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
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* লাল বৃত্তের সার্চ ইনপুট বক্সে ফন্ট কালার কালো করা */
    div[data-testid="stTextInput"] input {
        color: #000000 !important;
        background-color: #ffffff !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    
    /* সিলেক্ট বক্স এবং অন্যান্য ইনপুটের কালার স্টাইলিং */
    div[data-baseweb="select"] div {
        color: #000000 !important;
        background-color: #ffffff !important;
        border-radius: 8px !important;
    }

    /* ড্রপডাউন অপশন পপআপ ব্যাকগ্রাউন্ড ও টেক্সট */
    ul[data-baseweb="menu"] {
        background-color: #ffffff !important;
    }
    li[data-baseweb="option"] {
        color: #000000 !important;
    }

    /* লেবেল ও টেক্সটের কালার সাদা রাখা */
    label, p, span {
        color: #ffffff !important;
    }

    /* সবুজ বৃত্তের গুরুত্বপুর্ণ লিংক কার্ড ডিজাইন (সুদৃশ্য বাটন স্টাইল) */
    .link-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .link-card:hover {
        transform: translateY(-3px);
        background: rgba(255, 255, 255, 0.15);
        border-color: #00d2ff;
        box-shadow: 0 6px 20px rgba(0, 210, 255, 0.3);
    }
    .link-card h4 {
        color: #ffffff !important;
        margin-bottom: 8px !important;
        font-size: 16px;
    }
    .link-card a {
        display: inline-block;
        color: #00d2ff !important;
        text-decoration: none;
        font-weight: bold;
        word-break: break-all;
        font-size: 14px;
        padding: 6px 12px;
        background: rgba(0, 210, 255, 0.1);
        border-radius: 6px;
        border: 1px solid rgba(0, 210, 255, 0.3);
    }
    .link-card a:hover {
        background: #00d2ff;
        color: #0f2027 !important;
    }

    /* বাটনের ডিজাইন */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #0083B0;
        color: #ffffff !important;
        border: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# সেশন স্টেটে কন্টাক্ট ডেটা লোড করা
if "contacts" not in st.session_state:
    st.session_state.contacts = {
        # Number 01
        "Shaikh Nazrul Islam": {"Drive": "1", "e-TIN": "2886 9380 3054", "Circle": "54", "Zone": "3", "E-Return": "65", "Remarks": "OUT"},
        "Abu Yousuf Joarder": {"Drive": "1", "e-TIN": "6585 6368 7606", "Circle": "158", "Zone": "8", "E-Return": "21", "Remarks": ""},
        "G.M. Khorshed Alam": {"Drive": "1", "e-TIN": "5622 2372 1805", "Circle": "186", "Zone": "9", "E-Return": "13", "Remarks": ""},
        "Rawshan Ara Kabir": {"Drive": "", "e-TIN": "6977 7389 7603", "Circle": "499", "Zone": "23", "E-Return": "52", "Remarks": ""},
        "Farooq Ahmed": {"Drive": "", "e-TIN": "7881 4121 7843", "Circle": "41", "Zone": "02", "E-Return": "112", "Remarks": ""},
        "Abdullah Al Mahmud": {"Drive": "", "e-TIN": "6707 8250 6247", "Circle": "55", "Zone": "03", "E-Return": "36", "Remarks": ""},
        "Towfiq Elahi": {"Drive": "1", "e-TIN": "1288 0833 3865", "Circle": "152", "Zone": "07", "E-Return": "104", "Remarks": ""},
        "Mohammad Humayun Kabir": {"Drive": "1", "e-TIN": "678822460329", "Circle": "130", "Zone": "06", "E-Return": "22", "Remarks": ""},
        "Md. Shahjahan Ali": {"Drive": "1", "e-TIN": "6881 1133 8091", "Circle": "241", "Zone": "11", "E-Return": "62", "Remarks": ""},
        "Saleha Sarwar": {"Drive": "", "e-TIN": "1686 3877 2479", "Circle": "159", "Zone": "08", "E-Return": "10", "Remarks": ""},
        "Saida Begum": {"Drive": "", "e-TIN": "8249 7955 4462", "Circle": "276", "Zone": "13", "E-Return": "37", "Remarks": ""},
        "Fariha Binte Quayum": {"Drive": "", "e-TIN": "1840 3722 6881", "Circle": "215", "Zone": "10", "E-Return": "54", "Remarks": ""},
        "Sabera Belal": {"Drive": "1", "e-TIN": "4770 3972 1039", "Circle": "55", "Zone": "03", "E-Return": "47", "Remarks": ""},
        "Zakia Binte Quayum": {"Drive": "1", "e-TIN": "3243 3742 7116", "Circle": "41", "Zone": "02", "E-Return": "51", "Remarks": ""},
        "Gulshan Ara Begum": {"Drive": "", "e-TIN": "7841 2955 1338", "Circle": "215", "Zone": "10", "E-Return": "53", "Remarks": ""},
        "A. S. Md Nazmul Huda": {"Drive": "", "e-TIN": "1623 8479 4917", "Circle": "71", "Zone": "04", "E-Return": "09", "Remarks": ""},
        "Mahmuda Sultana": {"Drive": "", "e-TIN": "8222 5736 0152", "Circle": "122", "Zone": "06", "E-Return": "93", "Remarks": ""},
        "Jakia Jasmin": {"Drive": "", "e-TIN": "3950 3125 2471", "Circle": "323", "Zone": "15", "E-Return": "63", "Remarks": ""},
        "Sharmin Sultana (Neamul 173)": {"Drive": "1", "e-TIN": "2929 4120 2763", "Circle": "130", "Zone": "06", "E-Return": "39", "Remarks": ""},
        "Ms. Joystna Khatun": {"Drive": "1", "e-TIN": "8231 3539 9302", "Circle": "92", "Zone": "05", "E-Return": "56", "Remarks": ""},
        "Atiq & Family": {"Drive": "1", "e-TIN": "", "Circle": "", "Zone": "", "E-Return": "", "Remarks": ""},
        "Sharmin Sultana (Bhabi 165)": {"Drive": "1", "e-TIN": "7525 2655 8124", "Circle": "176", "Zone": "08", "E-Return": "41", "Remarks": ""},
        "Munshi Darul Islam": {"Drive": "1", "e-TIN": "5670 6736 5297", "Circle": "122", "Zone": "06", "E-Return": "78", "Remarks": ""},
        "Dipa Chowdhury (Bhabi Munshi Bhai)": {"Drive": "1", "e-TIN": "2455 1782 9010", "Circle": "11", "Zone": "01", "E-Return": "83", "Remarks": ""},
        "Shaikh Sameen Yasar": {"Drive": "1", "e-TIN": "5814 1936 9401", "Circle": "281", "Zone": "13", "E-Return": "64", "Remarks": "OUT"},
        "Mohammad Neamul Hasan (173)": {"Drive": "1", "e-TIN": "7641 5864 2013", "Circle": "190", "Zone": "09", "E-Return": "68", "Remarks": ""},
        "Md. Shafiqul Islam (Sc. Lab)": {"Drive": "1", "e-TIN": "2299 1357 0161", "Circle": "131", "Zone": "06", "E-Return": "113", "Remarks": ""},
        
        # Number 02
        "Azizun Nessa": {"Drive": "2", "e-TIN": "7861 8466 4504", "Circle": "10", "Zone": "01", "E-Return": "30", "Remarks": ""},
        "Nurani Shams Palash": {"Drive": "2", "e-TIN": "7852 6862 2699", "Circle": "131", "Zone": "06", "E-Return": "152", "Remarks": ""},
        "Monira Sultana": {"Drive": "2", "e-TIN": "2507 7480 7167", "Circle": "234", "Zone": "11", "E-Return": "11", "Remarks": ""},
        "Md. Awal": {"Drive": "2", "e-TIN": "1673 2778 4450", "Circle": "43", "Zone": "02", "E-Return": "108", "Remarks": ""},
        "Sayeda Sabrina Akter": {"Drive": "2", "e-TIN": "1746 3875 4137", "Circle": "37", "Zone": "02", "E-Return": "107", "Remarks": ""},
        "Rumana Afroz (Wife of Dr. Hadi)": {"Drive": "22", "e-TIN": "1565 6966 7314", "Circle": "278", "Zone": "10", "E-Return": "151", "Remarks": ""},
        "Shammi Khan": {"Drive": "2", "e-TIN": "5448 9158 9874", "Circle": "131", "Zone": "06", "E-Return": "", "Remarks": "OUT"},
        "Farzana Noor": {"Drive": "2", "e-TIN": "1762 3115 9220", "Circle": "131", "Zone": "06", "E-Return": "", "Remarks": "OUT"},
        "Sharmin Islam": {"Drive": "2", "e-TIN": "5124 8978 8108", "Circle": "14", "Zone": "01", "E-Return": "", "Remarks": "OUT"},
        "Asifur Rahman": {"Drive": "2", "e-TIN": "2624 5954 2999", "Circle": "14", "Zone": "01", "E-Return": "18", "Remarks": ""},
        "Kaniz Sultana": {"Drive": "22", "e-TIN": "1763 0067 4920", "Circle": "215", "Zone": "10", "E-Return": "19", "Remarks": ""},
        "Md. Mafidul Hasan": {"Drive": "2", "e-TIN": "1618 8375 0303", "Circle": "247", "Zone": "12", "E-Return": "20", "Remarks": ""},
        "Sk. Saleq- Uz- Zaman": {"Drive": "2", "e-TIN": "7974 8322 3450", "Circle": "153", "Zone": "07", "E-Return": "34", "Remarks": ""},
        "Mariam Zamila": {"Drive": "2", "e-TIN": "6241 4926 0808", "Circle": "43", "Zone": "02", "E-Return": "35", "Remarks": ""},
        "Israt Jahan": {"Drive": "2", "e-TIN": "2299 5846 0244", "Circle": "115", "Zone": "06", "E-Return": "43", "Remarks": "OUT"},
        "A.Z.M. Shafiqur Hannan (PWD)": {"Drive": "2", "e-TIN": "2532 1414 8538", "Circle": "71", "Zone": "04", "E-Return": "44", "Remarks": "OUT"},
        "Shams Saad Mahmood Palash": {"Drive": "2", "e-TIN": "5498 0565 2019", "Circle": "131", "Zone": "06", "E-Return": "71", "Remarks": ""},
        "Suraia Ahmed": {"Drive": "2", "e-TIN": "4703 0198 4406", "Circle": "131", "Zone": "06", "E-Return": "61", "Remarks": ""},
        "Md. Islam": {"Drive": "2", "e-TIN": "1344 6737 1079", "Circle": "126", "Zone": "06", "E-Return": "46", "Remarks": ""},
        "Mohammad Mohiuddin": {"Drive": "2", "e-TIN": "6309 7818 5145", "Circle": "262", "Zone": "12", "E-Return": "", "Remarks": ""},
        "Md. Kabir Hossain": {"Drive": "2", "e-TIN": "6865 6311 8176", "Circle": "128", "Zone": "06", "E-Return": "27", "Remarks": ""},
        "Sabbir Ahmed": {"Drive": "2", "e-TIN": "1381 2155 2511", "Circle": "203", "Zone": "10", "E-Return": "", "Remarks": "OUT"},
        "Israt Jahan (Murad)": {"Drive": "2", "e-TIN": "7233 1539 1912", "Circle": "131", "Zone": "06", "E-Return": "17", "Remarks": ""},
        "Mst. Saleha Ahmed (PWD Hannan Vi)": {"Drive": "2", "e-TIN": "4728 7935 7124", "Circle": "148", "Zone": "07", "E-Return": "", "Remarks": "OUT"},
        
        # Number 03
        "Nilufar Momtaz": {"Drive": "3", "e-TIN": "3943 0220 6562", "Circle": "125", "Zone": "06", "E-Return": "105", "Remarks": ""},
        "Hosne Ara": {"Drive": "3", "e-TIN": "4140 3212 6598", "Circle": "125", "Zone": "06", "E-Return": "16", "Remarks": ""},
        "Nishat Subha": {"Drive": "3", "e-TIN": "4469 3486 4499", "Circle": "125", "Zone": "06", "E-Return": "90", "Remarks": ""},
        "Sanchita Morsalin": {"Drive": "3", "e-TIN": "1906 5111 9313", "Circle": "242", "Zone": "11", "E-Return": "33", "Remarks": ""},
        "Mohammad Sajibul Alam Morsalin": {"Drive": "3", "e-TIN": "7930 1214 4745", "Circle": "63", "Zone": "03", "E-Return": "32", "Remarks": ""},
        "Md. Riyed Mosharaf": {"Drive": "3", "e-TIN": "4923 9357 0604", "Circle": "125", "Zone": "06", "E-Return": "45", "Remarks": ""},
        "Yasmin Ara Khanam": {"Drive": "3", "e-TIN": "1385 6957 6406", "Circle": "235", "Zone": "11", "E-Return": "129", "Remarks": ""},
        "Nafisa Navall": {"Drive": "3", "e-TIN": "1353 7889 3187", "Circle": "252", "Zone": "12", "E-Return": "31", "Remarks": ""},
        "Md. Al Hasib Jamal": {"Drive": "3", "e-TIN": "3898 4268 9439", "Circle": "122", "Zone": "06", "E-Return": "24", "Remarks": ""},
        "Subarna Hoque": {"Drive": "3", "e-TIN": "2354 2674 3069", "Circle": "124", "Zone": "06", "E-Return": "70", "Remarks": ""},
        "Mohammad Harun Or Rashid": {"Drive": "3", "e-TIN": "2194 9465 3096", "Circle": "115", "Zone": "06", "E-Return": "80", "Remarks": ""},
        "Thouhidur Rahman Appollo": {"Drive": "3", "e-TIN": "1129 9154 3924", "Circle": "214", "Zone": "10", "E-Return": "94", "Remarks": ""},
        "Muhammad Yousuf": {"Drive": "3", "e-TIN": "2517 2416 2164", "Circle": "76", "Zone": "04", "E-Return": "28", "Remarks": ""},
        "Ranu Ara Kutub": {"Drive": "3", "e-TIN": "8497 7579 7273", "Circle": "292", "Zone": "14", "E-Return": "82", "Remarks": ""},
        "Sayeda Afroza Khanam (PWD)": {"Drive": "3", "e-TIN": "5808 8254 9428", "Circle": "97", "Zone": "05", "E-Return": "42", "Remarks": ""},
        "Mohammad Aminul Islam": {"Drive": "3", "e-TIN": "8221 8942 9164", "Circle": "300", "Zone": "14", "E-Return": "", "Remarks": "Dead"},
        "Md. Bellal Hossan": {"Drive": "3", "e-TIN": "5937 2546 1498", "Circle": "261", "Zone": "12", "E-Return": "66", "Remarks": ""},
        "Md. Moksudur Rahman": {"Drive": "3", "e-TIN": "4295 7266 4348", "Circle": "278", "Zone": "13", "E-Return": "", "Remarks": "OUT"},
        "Mst. Mukta Parvin": {"Drive": "3", "e-TIN": "2154 3634 5602", "Circle": "214", "Zone": "10", "E-Return": "", "Remarks": "OUT"},
        "Most. Shahanaj Parvin": {"Drive": "3", "e-TIN": "4757 7054 8347", "Circle": "215", "Zone": "10", "E-Return": "", "Remarks": "OUT"},
        "Md. Mamunur Rashid": {"Drive": "3", "e-TIN": "1997 7082 6318", "Circle": "215", "Zone": "10", "E-Return": "", "Remarks": "OUT"},
        "Md. Mashikur Rahman": {"Drive": "3", "e-TIN": "1177 1321 2437", "Circle": "226", "Zone": "11", "E-Return": "88", "Remarks": ""},
        "Sayeda Nasrin Akhter (Wife of Rizvi)": {"Drive": "3", "e-TIN": "6277 2587 2718", "Circle": "64", "Zone": "03", "E-Return": "69", "Remarks": ""},
        "Md. Shahidur Rahman Bhuiyan": {"Drive": "3", "e-TIN": "4107 1252 3714", "Circle": "103", "Zone": "05", "E-Return": "102", "Remarks": ""},
        "Md. Mahfujul Alam": {"Drive": "3", "e-TIN": "6233 2717 1582", "Circle": "307", "Zone": "14", "E-Return": "6", "Remarks": ""},
        "Hasan Mahmudul Huda": {"Drive": "3", "e-TIN": "4186 0520 3944", "Circle": "131", "Zone": "06", "E-Return": "", "Remarks": "USA"},
        "Md. Monoar Hossain (Zakir 195)": {"Drive": "3", "e-TIN": "8396 6557 6233", "Circle": "54", "Zone": "03", "E-Return": "38", "Remarks": ""},
        "Afsana Parvin": {"Drive": "3", "e-TIN": "3236 6690 4854", "Circle": "131", "Zone": "06", "E-Return": "18", "Remarks": ""},
        "Md. Rubaiat Morshed": {"Drive": "3", "e-TIN": "4723 0276 9990", "Circle": "160", "Zone": "08", "E-Return": "99", "Remarks": ""},
        "Ismat Jahan": {"Drive": "3", "e-TIN": "546259223961", "Circle": "366", "Zone": "17", "E-Return": "", "Remarks": ""},

        # Number 04
        "Muminun Nessa": {"Drive": "4", "e-TIN": "4786 4273 0930", "Circle": "15", "Zone": "01", "E-Return": "29", "Remarks": ""},
        "Md. Monowarul Islam": {"Drive": "4", "e-TIN": "8500 4892 6882", "Circle": "54", "Zone": "03", "E-Return": "", "Remarks": "OUT"},
        "Md. Abul Hasnat Mollah": {"Drive": "4", "e-TIN": "2504 2738 2655", "Circle": "131", "Zone": "06", "E-Return": "91", "Remarks": ""},
        "Tania Tanzeem": {"Drive": "4", "e-TIN": "1118 2657 8664", "Circle": "131", "Zone": "06", "E-Return": "92", "Remarks": ""},
        "Ahmed Ali": {"Drive": "4", "e-TIN": "8699 9491 7000", "Circle": "202", "Zone": "10", "E-Return": "89", "Remarks": ""},
        "Saiful Yakub": {"Drive": "4", "e-TIN": "2215 2524 2786", "Circle": "180", "Zone": "09", "E-Return": "", "Remarks": ""},
        "Md. Sirajul Islam": {"Drive": "4", "e-TIN": "8263 0794 8671", "Circle": "180", "Zone": "09", "E-Return": "23", "Remarks": ""},
        "Mohammad Anowarul Islam": {"Drive": "4", "e-TIN": "4451 0388 1221", "Circle": "180", "Zone": "09", "E-Return": "", "Remarks": ""},
        "Monirul Islam": {"Drive": "4", "e-TIN": "3896 2945 7932", "Circle": "180", "Zone": "09", "E-Return": "", "Remarks": ""},
        "Md. Jahirul Islam": {"Drive": "4", "e-TIN": "3288 3988 9977", "Circle": "180", "Zone": "09", "E-Return": "110", "Remarks": ""},
        "Md. Nazrul Islam": {"Drive": "4", "e-TIN": "6409 5925 0521", "Circle": "180", "Zone": "09", "E-Return": "109", "Remarks": ""},
        "Md. Daudul Islam": {"Drive": "4", "e-TIN": "7290 0224 0109", "Circle": "180", "Zone": "09", "E-Return": "", "Remarks": ""},
        "Mrs. Srabanti": {"Drive": "4", "e-TIN": "3559 9734 6089", "Circle": "115", "Zone": "06", "E-Return": "", "Remarks": "OUT"},
        "Md. Babul Hawlader": {"Drive": "4", "e-TIN": "1506 7150 4027", "Circle": "11", "Zone": "01", "E-Return": "", "Remarks": "OUT"},
        "Asif Chowdhury": {"Drive": "4", "e-TIN": "5547 2938 1245", "Circle": "131", "Zone": "06", "E-Return": "60", "Remarks": ""},
        "Din Mohammad": {"Drive": "4", "e-TIN": "2164 0774 0243", "Circle": "75", "Zone": "04", "E-Return": "11", "Remarks": ""},
        "Meher Abjun Begum": {"Drive": "4", "e-TIN": "6586 7620 3109", "Circle": "318", "Zone": "15", "E-Return": "12", "Remarks": ""},
        "Rama Shah": {"Drive": "4", "e-TIN": "6798 7997 7010", "Circle": "303", "Zone": "14", "E-Return": "40", "Remarks": ""},
        "S. A Trading": {"Drive": "4", "e-TIN": "", "Circle": "", "Zone": "", "E-Return": "", "Remarks": "Meherpur"},
        "Tryotel Travels Ltd.": {"Drive": "4", "e-TIN": "7351 0880 9611", "Circle": "74", "Zone": "04", "E-Return": "", "Remarks": "OUT"},
        "Saimon Global Ltd.": {"Drive": "4", "e-TIN": "8565 7067 8518", "Circle": "23", "Zone": "02", "E-Return": "", "Remarks": "OUT"},
        "Rowshan Ara Begum": {"Drive": "4", "e-TIN": "6829 4393 7393", "Circle": "41", "Zone": "02", "E-Return": "", "Remarks": "OUT"},
        "Hasina Begum": {"Drive": "4", "e-TIN": "8904 9894 0112", "Circle": "97", "Zone": "05", "E-Return": "", "Remarks": "OUT"},
        "Sharmin Akter": {"Drive": "4", "e-TIN": "3817 6613 4058", "Circle": "104", "Zone": "05", "E-Return": "", "Remarks": "OUT"},
        "Rajkumer Bhattacharya": {"Drive": "4", "e-TIN": "4433 3042 9583", "Circle": "222", "Zone": "11", "E-Return": "", "Remarks": "OUT"},
        "Yami Bin M. Muhaimin Saleh": {"Drive": "4", "e-TIN": "1660 5076 4632", "Circle": "74", "Zone": "04", "E-Return": "121", "Remarks": "OUT"},

        # Number 05
        "Fair Securities & Logistics": {"Drive": "5", "e-TIN": "3976 2966 8244", "Circle": "304", "Zone": "14", "E-Return": "", "Remarks": ""},
        "Saimon Global": {"Drive": "5", "e-TIN": "8565 7067 8518", "Circle": "23", "Zone": "02", "E-Return": "", "Remarks": "OUT"},
        "Arnaz Rahman": {"Drive": "5", "e-TIN": "5106 8768 5202", "Circle": "131", "Zone": "06", "E-Return": "127", "Remarks": ""},
        "Naba Habib Belim": {"Drive": "5", "e-TIN": "6742 4896 0396", "Circle": "147", "Zone": "07", "E-Return": "128", "Remarks": ""},
        "Sugar Shots": {"Drive": "5", "e-TIN": "4879 0197 7395", "Circle": "147", "Zone": "07", "E-Return": "", "Remarks": ""},
        "Md. Masud Rana": {"Drive": "5", "e-TIN": "5234 0962 9978", "Circle": "252", "Zone": "12", "E-Return": "81", "Remarks": ""},
        "Hasibul Haque": {"Drive": "5", "e-TIN": "4484 0068 4697", "Circle": "300", "Zone": "14", "E-Return": "", "Remarks": "OUT"},
        "Bird Place": {"Drive": "5", "e-TIN": "", "Circle": "", "Zone": "VAT", "E-Return": "", "Remarks": "OUT"},
        "Tareq Masud Enterprise": {"Drive": "5", "e-TIN": "1594 2340 9878", "Circle": "180", "Zone": "09", "E-Return": "", "Remarks": "OUT"},
        "Nascenia": {"Drive": "5", "e-TIN": "1754 1163 2080", "Circle": "311", "Zone": "15", "E-Return": "", "Remarks": "OUT"},
        "Mediaider": {"Drive": "5", "e-TIN": "1804 8633 0570", "Circle": "311", "Zone": "15", "E-Return": "", "Remarks": "OUT"},
        "Pets World": {"Drive": "5", "e-TIN": "", "Circle": "", "Zone": "", "E-Return": "", "Remarks": "OUT"},
        "Peark Bangla Ltd.": {"Drive": "5", "e-TIN": "", "Circle": "", "Zone": "", "E-Return": "", "Remarks": "OUT"},
        "Md. Tarequll Islam": {"Drive": "5", "e-TIN": "2139 0516 1246", "Circle": "207", "Zone": "10", "E-Return": "", "Remarks": "OUT"},
        "Jannat Jute Bag Industries": {"Drive": "5", "e-TIN": "", "Circle": "", "Zone": "", "E-Return": "", "Remarks": ""},
        "Shahruk Hossain": {"Drive": "5", "e-TIN": "1498 6585 6765", "Circle": "125", "Zone": "06", "E-Return": "135", "Remarks": ""},
        "Alif Hossain Mollah": {"Drive": "5", "e-TIN": "2962 2286 5289", "Circle": "04", "Zone": "01", "E-Return": "136", "Remarks": ""},
        "Mrs. Shahnaz Sharmin": {"Drive": "5", "e-TIN": "525893785966", "Circle": "128", "Zone": "06", "E-Return": "137", "Remarks": ""},
        "Md. Badrul Hossain Mollah": {"Drive": "5", "e-TIN": "273173324497", "Circle": "127", "Zone": "06", "E-Return": "", "Remarks": "Dead"},
        "Md. Azim-Ul-Ahsan": {"Drive": "5", "e-TIN": "2615 0819 7885", "Circle": "76", "Zone": "04", "E-Return": "26", "Remarks": ""},
        "Ferdosh Ara (Sister in Law OMI)": {"Drive": "5", "e-TIN": "8742 2329 0159", "Circle": "248", "Zone": "12", "E-Return": "", "Remarks": ""},
        "Abu Muhammad Sadat": {"Drive": "5", "e-TIN": "1295 8127 2250", "Circle": "125", "Zone": "06", "E-Return": "14", "Remarks": ""},
        "Khandokar Shamsud Tahid": {"Drive": "5", "e-TIN": "112488398070", "Circle": "05", "Zone": "01", "E-Return": "126", "Remarks": ""},

        # Number 06
        "Shahriar Rashid (185)": {"Drive": "6", "e-TIN": "881651747845", "Circle": "186", "Zone": "09", "E-Return": "57", "Remarks": ""},
        "Zakir 195": {"Drive": "6", "e-TIN": "765483350836", "Circle": "195", "Zone": "09", "E-Return": "97", "Remarks": ""},
        "Ismat Ara Asha (Apa Palash Bhai)": {"Drive": "6", "e-TIN": "1195 3879 9228", "Circle": "12", "Zone": "", "E-Return": "", "Remarks": "Gazipur"},
        "Nova Tasha (Palash Bhai)": {"Drive": "6", "e-TIN": "1189 1377 6925", "Circle": "192", "Zone": "09", "E-Return": "98", "Remarks": ""},
        "Tiva Tasha (Palash Bhai)": {"Drive": "6", "e-TIN": "5715 7534 1600", "Circle": "192", "Zone": "09", "E-Return": "08", "Remarks": ""},
        "Hosne Ara Begum": {"Drive": "6", "e-TIN": "6108 2571 2338", "Circle": "215", "Zone": "10", "E-Return": "87", "Remarks": ""},
        "Shameem Ara Eti (Zakir 195)": {"Drive": "6", "e-TIN": "3491 5135 0580", "Circle": "233", "Zone": "11", "E-Return": "95", "Remarks": ""},
        "Zahin Zeima (Zakir 195)": {"Drive": "6", "e-TIN": "3101 5088 7547", "Circle": "307", "Zone": "14", "E-Return": "96", "Remarks": ""},
        "Md. Ashfaqure Rahman": {"Drive": "6", "e-TIN": "5909 1758 3799", "Circle": "77", "Zone": "04", "E-Return": "79", "Remarks": ""},
        "Anika Sama": {"Drive": "6", "e-TIN": "6728 2620 2875", "Circle": "214", "Zone": "10", "E-Return": "142", "Remarks": ""},
        "Md. Abdur Rajib": {"Drive": "6", "e-TIN": "1554 7724 2029", "Circle": "215", "Zone": "10", "E-Return": "", "Remarks": ""},
        "Kazi Zahidur Rahman": {"Drive": "6", "e-TIN": "1320 4444 6266", "Circle": "214", "Zone": "10", "E-Return": "72", "Remarks": ""},
        "Kazi Mohammad Ashequr Rahman": {"Drive": "6", "e-TIN": "6793 8220 9247", "Circle": "215", "Zone": "10", "E-Return": "73", "Remarks": ""},
        "Kazi Mohammad Asifur Rahman": {"Drive": "6", "e-TIN": "4636 5039 1063", "Circle": "215", "Zone": "10", "E-Return": "74", "Remarks": ""},
        "Ms. Joystna Khatun / Sabrina Jahan(Chumki)": {"Drive": "6", "e-TIN": "823135399302", "Circle": "92", "Zone": "05", "E-Return": "56", "Remarks": "Double"},

        # Number 07
        "S. M. Quamrul Islam": {"Drive": "7", "e-TIN": "5442 8097 3859", "Circle": "168", "Zone": "08", "E-Return": "50", "Remarks": ""},
        "Bithika Hasan": {"Drive": "7", "e-TIN": "6238 9132 0172", "Circle": "15", "Zone": "01", "E-Return": "49", "Remarks": ""},
        "Feroza Akhter Kazol": {"Drive": "7", "e-TIN": "4944 1051 3391", "Circle": "18", "Zone": "01", "E-Return": "48", "Remarks": ""},
        "Morjina Begum": {"Drive": "7", "e-TIN": "460344348106", "Circle": "115", "Zone": "06", "E-Return": "123", "Remarks": ""},
        "Sk. Abdullah": {"Drive": "7", "e-TIN": "837872243719", "Circle": "115", "Zone": "05", "E-Return": "122", "Remarks": ""},
        "Mohammad Ali": {"Drive": "7", "e-TIN": "513243317102", "Circle": "408", "Zone": "19", "E-Return": "119", "Remarks": ""},
        "Md. Asif Ali": {"Drive": "7", "e-TIN": "437110316084", "Circle": "318", "Zone": "15", "E-Return": "120", "Remarks": ""},
        "Nasrin Zaman": {"Drive": "7", "e-TIN": "389307745851", "Circle": "121", "Zone": "06", "E-Return": "118", "Remarks": ""},
        "Saima Islam (Wife Of Mozib)": {"Drive": "7", "e-TIN": "846558265715", "Circle": "128", "Zone": "06", "E-Return": "", "Remarks": ""},
        "Md. Mozibur Rahman (Sc. Lab)": {"Drive": "7", "e-TIN": "125746976519", "Circle": "127", "Zone": "06", "E-Return": "", "Remarks": ""},
        "Mohammad Abdul Hakim Babu": {"Drive": "7", "e-TIN": "312431119784", "Circle": "128", "Zone": "06", "E-Return": "153", "Remarks": ""},
        "Md. Ziaur Rahman (Mujib Brother)": {"Drive": "7", "e-TIN": "546254959261", "Circle": "03", "Zone": "01", "E-Return": "124", "Remarks": ""},
        "Shamsun Naher (Zia, Mujib)": {"Drive": "7", "e-TIN": "241840853004", "Circle": "19", "Zone": "01", "E-Return": "132", "Remarks": ""},
        "Mia Md. Mortayez Amin": {"Drive": "7", "e-TIN": "779725198592", "Circle": "208", "Zone": "10", "E-Return": "149", "Remarks": ""},
        "Tamanna Begum": {"Drive": "7", "e-TIN": "788989997801", "Circle": "86", "Zone": "04", "E-Return": "150", "Remarks": ""}
    }

# টাইটেল এরিয়া
st.markdown("""
    <div class="header-card">
        <h2 style="color: white; margin:0;">📱 কন্টাক্ট ডিরেক্টরি সার্ভিস</h2>
    </div>
""", unsafe_allow_html=True)

# ২. স্ট্যাটিস্টিকস ড্যাশবোর্ড
total_contacts = len(st.session_state.contacts)
col1, col2 = st.columns(2)

with col1:
    st.metric(label="👥 মোট কন্টাক্ট সংখ্যা", value=f"{total_contacts} জন")

with col2:
    st.metric(label="👁️ অ্যাপ ভিজিট সংখ্যা", value=f"{total_views} বার")

st.markdown("---")

# ৩. গুরুত্বপূর্ণ লিংকসমূহ (সবুজ বৃত্তের অংশটি গুছিয়ে সাজানো হলো)
st.subheader("🔗 গুরুত্বপূর্ণ লিংকসমূহ")
l_col1, l_col2 = st.columns(2)

with l_col1:
    st.markdown('''
        <div class="link-card">
            <h4>চালান ভেরিফাই</h4>
            <a href="https://challanverification.finance.gov.bd/echalan/" target="_blank">ওয়েবসাইটে যান ↗</a>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
        <div class="link-card">
            <h4>eReturn Sign in</h4>
            <a href="https://etaxnbr.gov.bd/#/auth/sign-in" target="_blank">ওয়েবসাইটে যান ↗</a>
        </div>
    ''', unsafe_allow_html=True)

with l_col2:
    st.markdown('''
        <div class="link-card">
            <h4>পেমেন্ট এনবিআর</h4>
            <a href="https://nbr.sblesheba.com/IncomeTax/Payment" target="_blank">ওয়েবসাইটে যান ↗</a>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
        <div class="link-card">
            <h4>eReturn verified</h4>
            <a href="https://etaxnbr.gov.bd/#/submission-verification" target="_blank">ওয়েবসাইটে যান ↗</a>
        </div>
    ''', unsafe_allow_html=True)

st.markdown("---")

# ৪. সার্চ ইন্টারফেস (লাল বৃত্তের ইনপুট কালার ফিক্স করা হয়েছে)
search_query = st.text_input("", placeholder="🔍 নাম দিয়ে অনুসন্ধান করুন...").strip()

if search_query:
    matched_results = {
        name: info for name, info in st.session_state.contacts.items() 
        if search_query.lower() in name.lower()
    }

    if matched_results:
        st.write(f"**পাওয়া গেছে ({len(matched_results)} টি):**")
        for name, info in matched_results.items():
            with st.expander(f"👤 {name}", expanded=True):
                st.write(f"**Drive:** {info.get('Drive', 'N/A')}")
                st.write(f"**e-TIN:** {info.get('e-TIN', 'N/A')}")
                st.write(f"**Circle:** {info.get('Circle', 'N/A')}")
                st.write(f"**Zone:** {info.get('Zone', 'N/A')}")
                if info.get("E-Return"):
                    st.write(f"**E-Return:** {info.get('E-Return')}")
                if info.get("Remarks"):
                    st.write(f"**Remarks:** {info.get('Remarks')}")
    else:
        st.warning("এই নামে কোনো তথ্য পাওয়া যায়নি।")
else:
    st.markdown("<p style='text-align: center; color: #cccccc;'>উপরে নাম টাইপ করে সার্চ করুন</p>", unsafe_allow_html=True)

st.markdown("---")

# ৫. কন্টাক্ট ম্যানেজমেন্ট (যোগ, এডিট ও মুছে ফেলা)
tab1, tab2, tab3 = st.tabs(["➕ নতুন কন্টাক্ট যোগ করুন", "✏️ কন্টাক্ট এডিট করুন", "🗑️ কন্টাক্ট মুছে ফেলুন"])

# কন্টাক্ট যোগ করা
with tab1:
    new_name = st.text_input("নাম (Assessee Name)", key="add_name")
    new_drive = st.text_input("Drive Number", key="add_drive")
    new_etin = st.text_input("e-TIN", key="add_etin")
    new_circle = st.text_input("Circle", key="add_circle")
    new_zone = st.text_input("Zone", key="add_zone")
    new_ereturn = st.text_input("E-Return Number", key="add_ereturn")
    new_remarks = st.text_input("Remarks", key="add_remarks")
    
    if st.button("কন্টাক্ট সেভ করুন"):
        if new_name.strip():
            st.session_state.contacts[new_name.strip()] = {
                "Drive": new_drive,
                "e-TIN": new_etin,
                "Circle": new_circle,
                "Zone": new_zone,
                "E-Return": new_ereturn,
                "Remarks": new_remarks
            }
            st.success(f"'{new_name}' সফলভাবে যোগ করা হয়েছে!")
            st.rerun()
        else:
            st.error("অনুগ্রহ করে নামটি লিখুন।")

# কন্টাক্ট এডিট করা
with tab2:
    if st.session_state.contacts:
        selected_edit_name = st.selectbox("সংশোধন করার জন্য কন্টাক্ট সিলেক্ট করুন", list(st.session_state.contacts.keys()), key="edit_select")
        edit_info = st.session_state.contacts[selected_edit_name]

        updated_drive = st.text_input("Drive আপডেট করুন", value=edit_info.get("Drive", ""), key="edit_drive")
        updated_etin = st.text_input("e-TIN আপডেট করুন", value=edit_info.get("e-TIN", ""), key="edit_etin")
        updated_circle = st.text_input("Circle আপডেট করুন", value=edit_info.get("Circle", ""), key="edit_circle")
        updated_zone = st.text_input("Zone আপডেট করুন", value=edit_info.get("Zone", ""), key="edit_zone")
        updated_ereturn = st.text_input("E-Return আপডেট করুন", value=edit_info.get("E-Return", ""), key="edit_ereturn")
        updated_remarks = st.text_input("Remarks আপডেট করুন", value=edit_info.get("Remarks", ""), key="edit_remarks")

        if st.button("তথ্য আপডেট করুন"):
            st.session_state.contacts[selected_edit_name] = {
                "Drive": updated_drive,
                "e-TIN": updated_etin,
                "Circle": updated_circle,
                "Zone": updated_zone,
                "E-Return": updated_ereturn,
                "Remarks": updated_remarks
            }
            st.success(f"'{selected_edit_name}'-এর তথ্য সফলভাবে পরিবর্তন করা হয়েছে!")
            st.rerun()
    else:
        st.info("কোনো কন্টাক্ট পাওয়া যায়নি।")

# কন্টাক্ট মুছে ফেলা
with tab3:
    if st.session_state.contacts:
        delete_name = st.selectbox("মুছে ফেলার জন্য কন্টাক্ট সিলেক্ট করুন", list(st.session_state.contacts.keys()), key="del_select")
        if st.button("কন্টাক্ট মুছে ফেলুন"):
            del st.session_state.contacts[delete_name]
            st.success(f"'{delete_name}' সফলভাবে মুছে ফেলা হয়েছে!")
            st.rerun()
    else:
        st.info("কোনো কন্টাক্ট পাওয়া যায়নি।")

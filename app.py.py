import streamlit as st

# আপনার ২০০টি নামের লিস্ট ও তথ্য এখানে যোগ করবেন
contacts = {
    "Shaik Nazrul Islam": {"e-TIN": "2886 9380 3054", "Circle": "34", "Zone": "3"},
    "Abu Yousuf Joarder": {"e-TIN": "6583 6368 2606", "Circle": "138", "Zone": "8"},
    "G M Khorshed Alam": {"e-TIN": "5672 3372 1805", "Circle": "186", "Zone": "9"},
    "Rawshan Ara Kabir": {"e-TIN": "6977 7389 7003", "Circle": "235", "Zone": "11"},
    "Farooq Ahmed": {"e-TIN": "7881 4121 7843", "Circle": "41", "Zone": "02"},
    "Abdullah Al Mahmud": {"e-TIN": "6707 8250 6247", "Circle": "55", "Zone": "03"},
    "Towfiq Elahi": {"e-TIN": "1288 0833 3865", "Circle": "152", "Zone": "07"},
    "Mohammad Humayun Kabir": {"e-TIN": "4561 6667 0072", "Circle": "130", "Zone": "06"},
    "Md Shahjahan Ali": {"e-TIN": "6881 1133 8091", "Circle": "241", "Zone": "11"},
    "Saleha Sarwar": {"e-TIN": "1686 3877 2479", "Circle": "159", "Zone": "08"},
    "Saida Begum": {"e-TIN": "8249 7955 4462", "Circle": "276", "Zone": "13"},
    "Fariha Binte Quayum": {"e-TIN": "1840 3722 6881", "Circle": "215", "Zone": "10"},
    "Sabera Belal": {"e-TIN": "4770 3972 1039", "Circle": "55", "Zone": "03"},
    "Zakia Binte Quayum": {"e-TIN": "3243 3742 7116", "Circle": "41", "Zone": "02"},
    "Gulshan Ara Begum": {"e-TIN": "7841 2955 1338", "Circle": "215", "Zone": "10"},
    "Rawsan Ara Kibria": {"e-TIN": "1558 0588 2091", "Circle": "215", "Zone": "10"},
    "A S Md Nazmul Huda": {"e-TIN": "1623 8479 4917", "Circle": "71", "Zone": "04"},
    "Mahmuda Sultana": {"e-TIN": "8222 5736 0152", "Circle": "122", "Zone": "06"},
    "Jakia Jasmin": {"e-TIN": "3950 3125 2471", "Circle": "323", "Zone": "15"},
    "Sharmin Sultana (Neamul 173)": {"e-TIN": "2929 4120 2763", "Circle": "130", "Zone": "06"},
    "Ms Joysna Khatun": {"e-TIN": "8231 3539 9302", "Circle": "92", "Zone": "05"},
    "Sharmin Sultana (Bhabi 165)": {"e-TIN": "7525 2655 8124", "Circle": "176", "Zone": "08"},
    "Munshi Darul Islam": {"e-TIN": "5670 6736 5297", "Circle": "122", "Zone": "06"},
    "Dipa Chowdhury (Bhabi Munshi Bhai)": {"e-TIN": "2455 1782 9010", "Circle": "11", "Zone": "01"},
    "Shaikh Sameen Yasar": {"e-TIN": "5814 1936 9401", "Circle": "281", "Zone": "13"},
    "Mohammad Neamul Hasan (173)": {"e-TIN": "7641 5864 2013", "Circle": "190", "Zone": "09"},
    "MD SHAFIQUL ISLAM": {"e-TIN": "2299 1357 0161", "Circle": "131", "Zone": "06"}
}
st.title("📱 কন্টাক্ট ডিরেক্টরি সার্চ")

# সার্চ বক্স
search_query = st.text_input("যেকোনো নাম দিয়ে সার্চ করুন:", "").strip()

if search_query:
	# নামের শুরুর অক্ষরের সাথে মিলিয়ে সার্চ (Prefix Matching)
	matched_results = {
		name: info for name, info in contacts.items()
		if name.lower().startswith(search_query.lower())
	}

	if matched_results:
		st.subheader(f"পাওয়া গেছে ({len(matched_results)} টি):")
		for name, info in matched_results.items():
			with st.expander(f"👤 {name}", expanded=True):
				st.write(f"**মোবাইল:** {info['মোবাইল']}")
				st.write(f"**ঠিকানা:** {info['ঠিকানা']}")
				st.write(f"**ইমেইল:** {info['ইমেইল']}")
	else:
		st.warning("এই নামে কোনো তথ্য পাওয়া যায়নি।")
else:
	st.info("উপরে নাম টাইপ করে তথ্য সার্চ করুন।")

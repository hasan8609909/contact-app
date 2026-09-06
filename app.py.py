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
        margin-bottom: 20px;
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

    /* লিংক বাটনের বিশেষ স্টাইল */
    a.link-btn {
        display: block;
        padding: 10px;
        margin: 5px 0;
        background: rgba(255, 255, 255, 0.1);
        color: #00d2ff !important;
        text-decoration: none;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        text-align: center;
        font-weight: bold;
        transition: 0.3s;
    }
    a.link-btn:hover {
        background: rgba(255, 255, 255, 0.25);
        border-color: #00d2ff;
    }
    </style>
""", unsafe_allow_html=True)

# সেশন স্টেটে কন্টাক্ট ডেটা লোড করা
if "contacts" not in st.session_state:
    st.session_state.contacts = {
        "Shaikh Nazrul Islam": {"e-TIN": "2886 9380 3054", "Circle": "54", "Zone": "3", "E-Return": "65", "Remarks": "OUT"},
        "Abu Yousuf Joarder": {"e-TIN": "6585 6368 7606", "Circle": "158", "Zone": "8", "E-Return": "21", "Remarks": ""},
        "G.M. Khorshed Alam": {"e-TIN": "5622 2372 1805", "Circle": "186", "Zone": "9", "E-Return": "13", "Remarks": ""},
        "Rawshan Ara Kabir": {"e-TIN": "6977 7389 7603", "Circle": "499", "Zone": "23", "E-Return": "52", "Remarks": ""},
        "Farooq Ahmed": {"e-TIN": "7881 4121 7843", "Circle": "41", "Zone": "02", "E-Return": "112", "Remarks": ""}
    }

# চ্যাট হিস্ট্রি ইনিশিয়ালাইজেশন
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "হ্যালো! আমি আপনার AI অ্যাসিস্ট্যান্ট। ট্যাক্স, e-TIN বা কন্টাক্ট সংক্রান্ত কীভাবে সাহায্য করতে পারি?"}
    ]

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

# ৩. গুরুত্বপূর্ণ ওয়েব সাইটের সেকশন
st.subheader("🌐 গুরুত্বপূর্ণ সাইট ও লিংকসমূহ")
l_col1, l_col2 = st.columns(2)

with l_col1:
    st.markdown('<a class="link-btn" href="https://etaxnbr.gov.bd/" target="_blank">🌐 NBR e-Return Portal</a>', unsafe_allow_html=True)
    st.markdown('<a class="link-btn" href="https://secure.incometax.gov.bd/TINHome" target="_blank">📄 e-TIN Registration</a>', unsafe_allow_html=True)

with l_col2:
    st.markdown('<a class="link-btn" href="https://nbr.gov.bd/" target="_blank">🏛️ NBR Official Website</a>', unsafe_allow_html=True)
    st.markdown('<a class="link-btn" href="https://bdloans.org/" target="_blank">🔍 Tax & Finance Portal</a>', unsafe_allow_html=True)

st.markdown("---")

# ৪. সার্চ ইন্টারফেস
search_query = st.text_input("", placeholder="🔍 নাম দিয়ে অনুসন্ধান করুন").strip()

if search_query:
    matched_results = {
        name: info for name, info in st.session_state.contacts.items() 
        if search_query.lower() in name.lower()
    }

    if matched_results:
        st.write(f"**পাওয়া গেছে ({len(matched_results)} টি):**")
        for name, info in matched_results.items():
            with st.expander(f"👤 {name}", expanded=True):
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
    st.markdown("<p style='text-align: center; color: #888;'>উপরে নাম টাইপ করে সার্চ করুন</p>", unsafe_allow_html=True)

st.markdown("---")

# ৫. কন্টাক্ট ম্যানেজমেন্ট
tab1, tab2, tab3 = st.tabs(["➕ নতুন কন্টাক্ট যোগ করুন", "✏️ কন্টাক্ট এডিট করুন", "🗑️ কন্টাক্ট মুছে ফেলুন"])

with tab1:
    new_name = st.text_input("নাম (Assessee Name)", key="add_name")
    new_etin = st.text_input("e-TIN", key="add_etin")
    new_circle = st.text_input("Circle", key="add_circle")
    new_zone = st.text_input("Zone", key="add_zone")
    new_ereturn = st.text_input("E-Return Number", key="add_ereturn")
    new_remarks = st.text_input("Remarks", key="add_remarks")
    
    if st.button("কন্টাক্ট সেভ করুন"):
        if new_name.strip():
            st.session_state.contacts[new_name.strip()] = {
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

with tab2:
    if st.session_state.contacts:
        selected_edit_name = st.selectbox("সংশোধন করার জন্য কন্টাক্ট সিলেক্ট করুন", list(st.session_state.contacts.keys()), key="edit_select")
        edit_info = st.session_state.contacts[selected_edit_name]

        updated_etin = st.text_input("e-TIN আপডেট করুন", value=edit_info.get("e-TIN", ""), key="edit_etin")
        updated_circle = st.text_input("Circle আপডেট করুন", value=edit_info.get("Circle", ""), key="edit_circle")
        updated_zone = st.text_input("Zone আপডেট করুন", value=edit_info.get("Zone", ""), key="edit_zone")
        updated_ereturn = st.text_input("E-Return আপডেট করুন", value=edit_info.get("E-Return", ""), key="edit_ereturn")
        updated_remarks = st.text_input("Remarks আপডেট করুন", value=edit_info.get("Remarks", ""), key="edit_remarks")

        if st.button("তথ্য আপডেট করুন"):
            st.session_state.contacts[selected_edit_name] = {
                "e-TIN": updated_etin,
                "Circle": updated_circle,
                "Zone": updated_zone,
                "E-Return": updated_ereturn,
                "Remarks": updated_remarks
            }
            st.success(f"'{selected_edit_name}'-এর তথ্য সফলভাবে পরিবর্তন করা হয়েছে!")
            st.rerun()

with tab3:
    if st.session_state.contacts:
        delete_name = st.selectbox("মুছে ফেলার জন্য কন্টাক্ট সিলেক্ট করুন", list(st.session_state.contacts.keys()), key="del_select")
        if st.button("কন্টাক্ট মুছে ফেলুন"):
            del st.session_state.contacts[delete_name]
            st.success(f"'{delete_name}' সফলভাবে মুছে ফেলা হয়েছে!")
            st.rerun()

st.markdown("---")

# ৬. 🤖 AI Chatbot সেকশন
st.subheader("🤖 AI সাহায্যকারী (Chatbot)")

# পূর্বের মেসেজগুলো প্রদর্শন
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ইউজার ইনপুট নেওয়া
if user_prompt := st.chat_input("ট্যাক্স বা অ্যাপ সম্পর্কিত যেকোনো প্রশ্ন করুন..."):
    # ইউজারের মেসেজ প্রদর্শন ও সেভ
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

    # চ্যাটবটের রেসপন্স তৈরি (নমুনা লজিক)
    # আসল API কানেক্ট করতে গুগল জেমিনাই বা ওপেনএআই-এর লাইব্রেরি ব্যবহার করা যাবে
    bot_reply = f"ধন্যবাদ আপনার প্রশ্নের জন্য! আপনি বলেছেন: '{user_prompt}'। ট্যাক্স ও রিটার্ন সাবমিশনের ব্যাপারে যেকোনো আপডেটেড তথ্যের জন্য উপরের NBR অফিসিয়াল সাইট লিংক ব্যবহার করতে পারেন।"
    
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)

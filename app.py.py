import streamlit as st

# আপনার ২০০টি নামের লিস্ট ও তথ্য এখানে যোগ করবেন
contacts = {
	"রহিম শেখ": {"মোবাইল": "01700000001", "ঠিকানা": "ঢাকা", "ইমেইল": "rahim@example.com"},
	"রফিক ইসলাম": {"মোবাইল": "01800000002", "ঠিকানা": "চট্টগ্রাম", "ইমেইল": "rafiq@example.com"},
	"করিম উদ্দিন": {"মোবাইল": "01900000003", "ঠিকানা": "সিলেট", "ইমেইল": "karim@example.com"},
	"কামাল হোসেন": {"মোবাইল": "01500000004", "ঠিকানা": "রাজশাহী", "ইমেইল": "kamal@example.com"}
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

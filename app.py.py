import os
import google.generativeai as genai
import streamlit as st

# ১. এখানে আপনার Gemini API Key বসান
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)

# AI মডেল সিলেক্ট করুন
model = genai.GenerativeModel("gemini-1.5-flash")

# ... (আপনার অ্যাপের বাকি কোড অপরিবর্তিত থাকবে) ...

# 🤖 AI Chatbot সেকশন
st.subheader("🤖 AI সাহায্যকারী (Chatbot)")

# পূর্বের চ্যাট হিস্ট্রি ডিসপ্লে
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ইউজার মেসেজ দিলে তা এআই-এর কাছে পাঠানো
if user_prompt := st.chat_input("ট্যাক্স বা অ্যাপ সম্পর্কিত যেকোনো প্রশ্ন করুন..."):
    # ইউজার মেসেজ দেখান
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

    # Gemini AI থেকে রেসপন্স জেনারেট করা
    with st.chat_message("assistant"):
        with st.spinner("চিন্তা করছি..."):
            try:
                response = model.generate_content(user_prompt)
                bot_reply = response.text
            except Exception as e:
                bot_reply = f"দুঃখিত, কোনো সমস্যা হয়েছে: {str(e)}"
            
            st.write(bot_reply)
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

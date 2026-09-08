import streamlit as st

# আপনার দেওয়া সম্পূর্ণ কন্টাক্ট ও ট্যাক্স ডিরেক্টরি ডেটা লিস্ট
contacts = [
    # Drive 1
    {"drive": "1", "assessee": "Shaikh Nazrul Islam", "tin": "2886 9380 3054", "circle": "54", "zone": "3", "returnNo": "65", "remarks": "OUT"},
    {"drive": "1", "assessee": "Abu Yousuf Joarder", "tin": "6585 6368 7606", "circle": "158", "zone": "8", "returnNo": "21", "remarks": ""},
    {"drive": "1", "assessee": "G.M. Khorshed Alam", "tin": "5622 2372 1805", "circle": "186", "zone": "9", "returnNo": "13", "remarks": ""},
    {"drive": "1", "assessee": "Rawshan Ara Kabir", "tin": "7603 6977 7389", "circle": "499", "zone": "23", "returnNo": "52", "remarks": ""},
    {"drive": "1", "assessee": "Farooq Ahmed", "tin": "7881 4121 7843", "circle": "41", "zone": "02", "returnNo": "112", "remarks": ""},
    {"drive": "1", "assessee": "Abdullah Al Mahmud", "tin": "6707 8250 6247", "circle": "55", "zone": "03", "returnNo": "36", "remarks": ""},
    {"drive": "1", "assessee": "Towfiq Elahi", "tin": "1288 0833 3865", "circle": "152", "zone": "07", "returnNo": "104", "remarks": ""},
    {"drive": "1", "assessee": "Mohammad Humayun Kabir", "tin": "678822460329", "circle": "130", "zone": "06", "returnNo": "22", "remarks": ""},
    {"drive": "1", "assessee": "Md. Shahjahan Ali", "tin": "6881 1133 8091", "circle": "241", "zone": "11", "returnNo": "62", "remarks": ""},
    {"drive": "1", "assessee": "Saleha Sarwar", "tin": "1686 3877 2479", "circle": "159", "zone": "08", "returnNo": "10", "remarks": ""},
    {"drive": "1", "assessee": "Saida Begum", "tin": "8249 7955 4462", "circle": "276", "zone": "13", "returnNo": "37", "remarks": ""},
    {"drive": "1", "assessee": "Fariha Binte Quayum", "tin": "1840 3722 6881", "circle": "215", "zone": "10", "returnNo": "54", "remarks": ""},
    {"drive": "1", "assessee": "Sabera Belal", "tin": "4770 3972 1039", "circle": "55", "zone": "03", "returnNo": "47", "remarks": ""},
    {"drive": "1", "assessee": "Zakia Binte Quayum", "tin": "3243 3742 7116", "circle": "41", "zone": "02", "returnNo": "51", "remarks": ""},
    {"drive": "1", "assessee": "Gulshan Ara Begum", "tin": "7841 2955 1338", "circle": "215", "zone": "10", "returnNo": "53", "remarks": ""},
    {"drive": "1", "assessee": "A. S. Md Nazmul Huda / Mahmuda Sultana", "tin": "1623 8479 4917 / 8222 5736 0152", "circle": "71 / 122", "zone": "04 / 06", "returnNo": "09 / 93", "remarks": ""},
    {"drive": "1", "assessee": "Jakia Jasmin", "tin": "3950 3125 2471", "circle": "323", "zone": "15", "returnNo": "63", "remarks": ""},
    {"drive": "1", "assessee": "Sharmin Sultana (Neamul 173)", "tin": "2929 4120 2763", "circle": "130", "zone": "06", "returnNo": "39", "remarks": ""},
    {"drive": "1", "assessee": "Ms. Joystna Khatun", "tin": "8231 3539 9302", "circle": "92", "zone": "05", "returnNo": "56", "remarks": ""},
    {"drive": "1", "assessee": "Atiq & Family", "tin": "", "circle": "", "zone": "", "returnNo": "", "remarks": ""},
    {"drive": "1", "assessee": "Sharmin Sultana (Bhabi 165)", "tin": "7525 2655 8124", "circle": "176", "zone": "08", "returnNo": "41", "remarks": ""},
    {"drive": "1", "assessee": "Munshi Darul Islam", "tin": "5670 6736 5297", "circle": "122", "zone": "06", "returnNo": "78", "remarks": ""},
    {"drive": "1", "assessee": "Dipa Chowdhury (Bhabi Munshi Bhai)", "tin": "2455 1782 9010", "circle": "11", "zone": "01", "returnNo": "83", "remarks": ""},
    {"drive": "1", "assessee": "Shaikh Sameen Yasar", "tin": "5814 1936 9401", "circle": "281", "zone": "13", "returnNo": "64", "remarks": "OUT"},
    {"drive": "1", "assessee": "Mohammad Neamul Hasan (173)", "tin": "5864 2013 7641", "circle": "190", "zone": "09", "returnNo": "68", "remarks": ""},
    {"drive": "1", "assessee": "Md. Shafiqul Islam (Sc. Lab)", "tin": "1357 0161 2299", "circle": "131", "zone": "06", "returnNo": "113", "remarks": ""},

    # Drive 2
    {"drive": "2", "assessee": "Azizun Nessa", "tin": "7861 8466 4504", "circle": "10", "zone": "01", "returnNo": "30", "remarks": ""},
    {"drive": "2", "assessee": "Nurani Shams Palash", "tin": "7852 6862 2699", "circle": "131", "zone": "06", "returnNo": "152", "remarks": ""},
    {"drive": "2", "assessee": "Monira Sultana", "tin": "2507 7480 7167", "circle": "234", "zone": "11", "returnNo": "11", "remarks": ""},
    {"drive": "2", "assessee": "Md. Awal", "tin": "1673 2778 4450", "circle": "43", "zone": "02", "returnNo": "108", "remarks": ""},
    {"drive": "2", "assessee": "Sayeda Sabrina Akter", "tin": "1746 3875 4137", "circle": "37", "zone": "02", "returnNo": "107", "remarks": ""},
    {"drive": "22", "assessee": "Rumana Afroz (Wife of Dr. Hadi)", "tin": "1565 6966 7314", "circle": "278", "zone": "10", "returnNo": "151", "remarks": ""},
    {"drive": "2", "assessee": "Shammi Khan", "tin": "5448 9158 9874", "circle": "131", "zone": "06", "returnNo": "", "remarks": "OUT"},
    {"drive": "2", "assessee": "Farzana Noor", "tin": "1762 3115 9220", "circle": "131", "zone": "06", "returnNo": "", "remarks": "OUT"},
    {"drive": "2", "assessee": "Sharmin Islam", "tin": "5124 8978 8108", "circle": "14", "zone": "01", "returnNo": "", "remarks": "OUT"},
    {"drive": "2", "assessee": "Asifur Rahman", "tin": "2624 5954 2999", "circle": "14", "zone": "01", "returnNo": "18", "remarks": ""},
    {"drive": "22", "assessee": "Kaniz Sultana", "tin": "1763 0067 4920", "circle": "215", "zone": "10", "returnNo": "19", "remarks": ""},
    {"drive": "2", "assessee": "Md. Mafidul Hasan", "tin": "1618 8375 0303", "circle": "247", "zone": "12", "returnNo": "20", "remarks": ""},
    {"drive": "2", "assessee": "Sk. Saleq- Uz- Zaman", "tin": "7974 8322 3450", "circle": "153", "zone": "07", "returnNo": "34", "remarks": ""},
    {"drive": "2", "assessee": "Mariam Zamila", "tin": "6241 4926 0808", "circle": "43", "zone": "02", "returnNo": "35", "remarks": ""},
    {"drive": "2", "assessee": "Israt Jahan", "tin": "5846 0244 2299", "circle": "115", "zone": "06", "returnNo": "43", "remarks": "OUT"},
    {"drive": "2", "assessee": "A.Z.M. Shafiqur Hannan (PWD)", "tin": "2532 1414 8538", "circle": "71", "zone": "04", "returnNo": "44", "remarks": "OUT"},
    {"drive": "2", "assessee": "Shams Saad Mahmood Palash", "tin": "5498 0565 2019", "circle": "131", "zone": "06", "returnNo": "71", "remarks": ""},
    {"drive": "2", "assessee": "Suraia Ahmed", "tin": "4703 0198 4406", "circle": "131", "zone": "06", "returnNo": "61", "remarks": ""},
    {"drive": "2", "assessee": "Md. Islam", "tin": "1344 6737 1079", "circle": "126", "zone": "06", "returnNo": "46", "remarks": ""},
    {"drive": "2", "assessee": "Mohammad Mohiuddin", "tin": "6309 7818 5145", "circle": "262", "zone": "12", "returnNo": "", "remarks": ""},
    {"drive": "2", "assessee": "Md. Kabir Hossain", "tin": "6865 6311 8176", "circle": "128", "zone": "06", "returnNo": "27", "remarks": ""},
    {"drive": "2", "assessee": "Sabbir Ahmed", "tin": "1381 2155 2511", "circle": "203", "zone": "10", "returnNo": "", "remarks": "OUT"},
    {"drive": "2", "assessee": "Israt Jahan (Murad)", "tin": "7233 1539 1912", "circle": "131", "zone": "06", "returnNo": "17", "remarks": ""},
    {"drive": "2", "assessee": "Mst. Saleha Ahmed (PWD Hannan Vi)", "tin": "4728 7935 7124", "circle": "148", "zone": "07", "returnNo": "", "remarks": "OUT"},

    # Drive 3
    {"drive": "3", "assessee": "Nilufar Momtaz", "tin": "3943 0220 6562", "circle": "125", "zone": "06", "returnNo": "105", "remarks": ""},
    {"drive": "3", "assessee": "Hosne Ara", "tin": "4140 3212 6598", "circle": "125", "zone": "06", "returnNo": "16", "remarks": ""},
    {"drive": "3", "assessee": "Nishat Subha", "tin": "4469 3486 4499", "circle": "125", "zone": "06", "returnNo": "90", "remarks": ""},
    {"drive": "3", "assessee": "Sanchita Morsalin", "tin": "1906 5111 9313", "circle": "242", "zone": "11", "returnNo": "33", "remarks": ""},
    {"drive": "3", "assessee": "Mohammad Sajibul Alam Morsalin", "tin": "7930 1214 4745", "circle": "63", "zone": "03", "returnNo": "32", "remarks": ""},
    {"drive": "3", "assessee": "Md. Riyed Mosharaf", "tin": "4923 9357 0604", "circle": "125", "zone": "06", "returnNo": "45", "remarks": ""},
    {"drive": "3", "assessee": "Yasmin Ara Khanam", "tin": "6406 1385 6957", "circle": "235", "zone": "11", "returnNo": "129", "remarks": ""},
    {"drive": "3", "assessee": "Nafisa Navall", "tin": "1353 7889 3187", "circle": "252", "zone": "12", "returnNo": "31", "remarks": ""},
    {"drive": "3", "assessee": "Md. Al Hasib Jamal", "tin": "3898 4268 9439", "circle": "122", "zone": "06", "returnNo": "24", "remarks": ""},
    {"drive": "3", "assessee": "Subarna Hoque", "tin": "2354 2674 3069", "circle": "124", "zone": "06", "returnNo": "70", "remarks": ""},
    {"drive": "3", "assessee": "Mohammad Harun Or Rashid", "tin": "2194 9465 3096", "circle": "115", "zone": "06", "returnNo": "80", "remarks": ""},
    {"drive": "3", "assessee": "Thouhidur Rahman Appollo", "tin": "1129 9154 3924", "circle": "214", "zone": "10", "returnNo": "94", "remarks": ""},
    {"drive": "3", "assessee": "Muhammad Yousuf", "tin": "2517 2416 2164", "circle": "76", "zone": "04", "returnNo": "28", "remarks": ""},
    {"drive": "3", "assessee": "Ranu Ara Kutub", "tin": "8497 7579 7273", "circle": "292", "zone": "14", "returnNo": "82", "remarks": ""},
    {"drive": "3", "assessee": "Sayeda Afroza Khanam (PWD)", "tin": "5808 8254 9428", "circle": "97", "zone": "05", "returnNo": "42", "remarks": ""},
    {"drive": "3 / 3", "assessee": "Mohammad Aminul Islam / Md. Bellal Hossan", "tin": "8221 8942 9164 / 5937 2546 1498", "circle": "300 / 261", "zone": "14 / 12", "returnNo": "66", "remarks": "Dead"},
    {"drive": "3", "assessee": "Md. Moksudur Rahman", "tin": "4295 7266 4348", "circle": "278", "zone": "13", "returnNo": "", "remarks": "OUT"},
    {"drive": "3", "assessee": "Mst. Mukta Parvin", "tin": "2154 3634 5602", "circle": "214", "zone": "10", "returnNo": "", "remarks": "OUT"},
    {"drive": "3", "assessee": "Most. Shahanaj Parvin", "tin": "4757 7054 8347", "circle": "215", "zone": "10", "returnNo": "", "remarks": "OUT"},
    {"drive": "3", "assessee": "Md. Mamunur Rashid", "tin": "1997 7082 6318", "circle": "215", "zone": "10", "returnNo": "", "remarks": "OUT"},
    {"drive": "3", "assessee": "Md. Mashikur Rahman", "tin": "1177 1321 2437", "circle": "226", "zone": "11", "returnNo": "88", "remarks": ""},
    {"drive": "3", "assessee": "Sayeda Nasrin Akhter (Wife of Rizvi)", "tin": "6277 2587 2718", "circle": "64", "zone": "03", "returnNo": "69", "remarks": ""},
    {"drive": "3", "assessee": "Md. Shahidur Rahman Bhuiyan", "tin": "4107 1252 3714", "circle": "103", "zone": "05", "returnNo": "102", "remarks": ""},
    {"drive": "3", "assessee": "Md. Mahfujul Alam", "tin": "6233 2717 1582", "circle": "307", "zone": "14", "returnNo": "6", "remarks": ""},
    {"drive": "3", "assessee": "Hasan Mahmudul Huda", "tin": "4186 0520 3944", "circle": "131", "zone": "06", "returnNo": "", "remarks": "USA"},
    {"drive": "3", "assessee": "Md. Monoar Hossain (Zakir 195)", "tin": "8396 6557 6233", "circle": "54", "zone": "03", "returnNo": "38", "remarks": ""},
    {"drive": "3", "assessee": "Afsana Parvin", "tin": "3236 6690 4854", "circle": "131", "zone": "06", "returnNo": "18", "remarks": ""},
    {"drive": "3", "assessee": "Md. Rubaiat Morshed", "tin": "4723 0276 9990", "circle": "160", "zone": "08", "returnNo": "99", "remarks": ""},
    {"drive": "3", "assessee": "Ismat Jahan", "tin": "546259223961", "circle": "366", "zone": "17", "returnNo": "", "remarks": ""},

    # Drive 4
    {"drive": "4", "assessee": "Muminun Nessa", "tin": "4786 4273 0930", "circle": "15", "zone": "01", "returnNo": "29", "remarks": ""},
    {"drive": "4", "assessee": "Md. Monowarul Islam", "tin": "8500 4892 6882", "circle": "54", "zone": "03", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Md. Abul Hasnat Mollah", "tin": "2504 2738 2655", "circle": "131", "zone": "06", "returnNo": "91", "remarks": ""},
    {"drive": "4", "assessee": "Tania Tanzeem", "tin": "1118 2657 8664", "circle": "131", "zone": "06", "returnNo": "92", "remarks": ""},
    {"drive": "4", "assessee": "Ahmed Ali", "tin": "8699 9491 7000", "circle": "202", "zone": "10", "returnNo": "89", "remarks": ""},
    {"drive": "4", "assessee": "Saiful Yakub", "tin": "2215 2524 2786", "circle": "180", "zone": "09", "returnNo": "", "remarks": ""},
    {"drive": "4", "assessee": "Md. Sirajul Islam", "tin": "8263 0794 8671", "circle": "180", "zone": "09", "returnNo": "23", "remarks": ""},
    {"drive": "4", "assessee": "Mohammad Anowarul Islam", "tin": "4451 0388 1221", "circle": "180", "zone": "09", "returnNo": "", "remarks": ""},
    {"drive": "4", "assessee": "Monirul Islam", "tin": "3896 2945 7932", "circle": "180", "zone": "09", "returnNo": "", "remarks": ""},
    {"drive": "4", "assessee": "Md. Jahirul Islam", "tin": "3288 3988 9977", "circle": "180", "zone": "09", "returnNo": "110", "remarks": ""},
    {"drive": "4", "assessee": "Md. Nazrul Islam", "tin": "6409 5925 0521", "circle": "180", "zone": "09", "returnNo": "109", "remarks": ""},
    {"drive": "4", "assessee": "Md. Daudul Islam", "tin": "7290 0224 0109", "circle": "180", "zone": "09", "returnNo": "", "remarks": ""},
    {"drive": "4", "assessee": "Mrs. Srabanti", "tin": "3559 9734 6089", "circle": "115", "zone": "06", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Md. Babul Hawlader", "tin": "1506 7150 4027", "circle": "11", "zone": "01", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Asif Chowdhury", "tin": "5547 2938 1245", "circle": "131", "zone": "06", "returnNo": "60", "remarks": ""},
    {"drive": "4", "assessee": "Din Mohammad", "tin": "2164 0774 0243", "circle": "75", "zone": "04", "returnNo": "11", "remarks": ""},
    {"drive": "4", "assessee": "Meher Abjun Begum", "tin": "6586 7620 3109", "circle": "318", "zone": "15", "returnNo": "12", "remarks": ""},
    {"drive": "4 / 4", "assessee": "Rama Shah / S. A Trading", "tin": "6798 7997 7010", "circle": "303 / Meherpur", "zone": "14", "returnNo": "40", "remarks": ""},
    {"drive": "4", "assessee": "Tryotel Travels Ltd.", "tin": "7351 0880 9611", "circle": "74", "zone": "04", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Saimon Global Ltd.", "tin": "8565 7067 8518", "circle": "23", "zone": "02", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Rowshan Ara Begum", "tin": "6829 4393 7393", "circle": "41", "zone": "02", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Hasina Begum", "tin": "8904 9894 0112", "circle": "97", "zone": "05", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Sharmin Akter", "tin": "3817 6613 4058", "circle": "104", "zone": "05", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Rajkumer Bhattacharya", "tin": "4433 3042 9583", "circle": "222", "zone": "11", "returnNo": "", "remarks": "OUT"},
    {"drive": "4", "assessee": "Yami Bin M. Muhaimin Saleh", "tin": "1660 5076 4632", "circle": "74", "zone": "04", "returnNo": "121", "remarks": "OUT"},

    # Drive 5
    {"drive": "5", "assessee": "Fair Securities & Logistics", "tin": "3976 2966 8244", "circle": "304", "zone": "14", "returnNo": "", "remarks": ""},
    {"drive": "5 / 5", "assessee": "Saimon Global / Arnaz Rahman", "tin": "8565 7067 8518 / 5106 8768 5202", "circle": "02 / 131", "zone": "23 / 06", "returnNo": "127", "remarks": "OUT"},
    {"drive": "5", "assessee": "Naba Habib Belim", "tin": "6742 4896 0396", "circle": "147", "zone": "07", "returnNo": "128", "remarks": ""},
    {"drive": "5", "assessee": "Sugar Shots", "tin": "4879 0197 7395", "circle": "147", "zone": "07", "returnNo": "", "remarks": ""},
    {"drive": "5", "assessee": "Md. Masud Rana", "tin": "5234 0962 9978", "circle": "252", "zone": "12", "returnNo": "81", "remarks": ""},
    {"drive": "5", "assessee": "Hasibul Haque", "tin": "4484 0068 4697", "circle": "300", "zone": "14", "returnNo": "", "remarks": "OUT"},
    {"drive": "5", "assessee": "Bird Place", "tin": "VAT", "circle": "", "zone": "", "returnNo": "", "remarks": "OUT"},
    {"drive": "5", "assessee": "Tareq Masud Enterprise", "tin": "1594 2340 9878", "circle": "180", "zone": "09", "returnNo": "", "remarks": "OUT"},
    {"drive": "5", "assessee": "Nascenia", "tin": "1754 1163 2080", "circle": "311", "zone": "15", "returnNo": "", "remarks": "OUT"},
    {"drive": "5", "assessee": "Mediaider", "tin": "1804 8633 0570", "circle": "311", "zone": "15", "returnNo": "", "remarks": "OUT"},
    {"drive": "5", "assessee": "Pets World", "tin": "", "circle": "", "zone": "", "returnNo": "", "remarks": "OUT"},
    {"drive": "5", "assessee": "Peark Bangla Ltd.", "tin": "", "circle": "", "zone": "", "returnNo": "", "remarks": "OUT"},
    {"drive": "5", "assessee": "Md. Tarequll Islam", "tin": "2139 0516 1246", "circle": "207", "zone": "10", "returnNo": "", "remarks": "OUT"},
    {"drive": "5 / 5", "assessee": "Jannat Jute Bag Industries / Shahruk Hossain", "tin": "1498 6585 6765", "circle": "125", "zone": "06", "returnNo": "135", "remarks": ""},
    {"drive": "5", "assessee": "Alif Hossain Mollah", "tin": "2962 2286 5289", "circle": "04", "zone": "01", "returnNo": "136", "remarks": ""},
    {"drive": "5", "assessee": "Mrs. Shahnaz Sharmin", "tin": "525893785966", "circle": "128", "zone": "06", "returnNo": "137", "remarks": ""},
    {"drive": "5", "assessee": "Md. Badrul Hossain Mollah", "tin": "273173324497", "circle": "127", "zone": "06", "returnNo": "", "remarks": "Dead"},
    {"drive": "5", "assessee": "Md. Azim-Ul-Ahsan", "tin": "2615 0819 7885", "circle": "76", "zone": "04", "returnNo": "26", "remarks": ""},
    {"drive": "5", "assessee": "Ferdosh Ara (Sister in Law OMI)", "tin": "8742 2329 0159", "circle": "248", "zone": "12", "returnNo": "", "remarks": ""},
    {"drive": "5", "assessee": "Abu Muhammad Sadat", "tin": "1295 8127 2250", "circle": "125", "zone": "06", "returnNo": "14", "remarks": ""},
    {"drive": "5", "assessee": "Khandokar Shamsud Tahid", "tin": "112488398070", "circle": "05", "zone": "01", "returnNo": "126", "remarks": ""},

    # Drive 6
    {"drive": "6", "assessee": "Shahriar Rashid (185)", "tin": "881651747845", "circle": "186", "zone": "09", "returnNo": "57", "remarks": ""},
    {"drive": "6", "assessee": "Zakir 195", "tin": "765483350836", "circle": "195", "zone": "09", "returnNo": "97", "remarks": ""},
    {"drive": "6", "assessee": "Ismat Ara Asha (Apa Palash Bhai)", "tin": "1195 3879 9228", "circle": "", "zone": "12", "returnNo": "", "remarks": "Gazipur"},
    {"drive": "6", "assessee": "Nova Tasha (Palash Bhai)", "tin": "1189 1377 6925", "circle": "192", "zone": "09", "returnNo": "98", "remarks": ""},
    {"drive": "6", "assessee": "Tiva Tasha (Palash Bhai)", "tin": "5715 7534 1600", "circle": "192", "zone": "09", "returnNo": "08", "remarks": ""},
    {"drive": "6", "assessee": "Hosne Ara Begum", "tin": "6108 2571 2338", "circle": "215", "zone": "10", "returnNo": "87", "remarks": ""},
    {"drive": "6", "assessee": "Shameem Ara Eti (Zakir 195)", "tin": "3491 5135 0580", "circle": "233", "zone": "11", "returnNo": "95", "remarks": ""},
    {"drive": "6", "assessee": "Zahin Zeima (Zakir 195)", "tin": "3101 5088 7547", "circle": "307", "zone": "14", "returnNo": "96", "remarks": ""},
    {"drive": "6", "assessee": "Md. Ashfaqure Rahman", "tin": "5909 1758 3799", "circle": "77", "zone": "04", "returnNo": "79", "remarks": ""},
    {"drive": "6", "assessee": "Anika Sama", "tin": "6728 2620 2875", "circle": "214", "zone": "10", "returnNo": "142", "remarks": ""},
    {"drive": "6", "assessee": "Md. Abdur Rajib", "tin": "1554 7724 2029", "circle": "215", "zone": "10", "returnNo": "", "remarks": ""},
    {"drive": "6", "assessee": "Kazi Zahidur Rahman", "tin": "1320 4444 6266", "circle": "214", "zone": "10", "returnNo": "72", "remarks": ""},
    {"drive": "6", "assessee": "Kazi Mohammad Ashequr Rahman", "tin": "6793 8220 9247", "circle": "215", "zone": "10", "returnNo": "73", "remarks": ""},
    {"drive": "6", "assessee": "Kazi Mohammad Asifur Rahman", "tin": "4636 5039 1063", "circle": "215", "zone": "10", "returnNo": "74", "remarks": ""},
    {"drive": "6", "assessee": "Ms. Joystna Khatun / Sabrina Jahan(Chumki)", "tin": "823135399302", "circle": "92", "zone": "05", "returnNo": "56", "remarks": "Double"},

    # Drive 7
    {"drive": "7", "assessee": "S. M. Quamrul Islam", "tin": "5442 8097 3859", "circle": "168", "zone": "08", "returnNo": "50", "remarks": ""},
    {"drive": "7", "assessee": "Bithika Hasan", "tin": "6238 9132 0172", "circle": "15", "zone": "01", "returnNo": "49", "remarks": ""},
    {"drive": "7", "assessee": "Feroza Akhter Kazol", "tin": "4944 1051 3391", "circle": "18", "zone": "01", "returnNo": "48", "remarks": ""},
    {"drive": "7", "assessee": "Morjina Begum", "tin": "460344348106", "circle": "115", "zone": "06", "returnNo": "123", "remarks": ""},
    {"drive": "7", "assessee": "Sk. Abdullah", "tin": "837872243719", "circle": "115", "zone": "05", "returnNo": "122", "remarks": ""},
    {"drive": "7", "assessee": "Mohammad Ali", "tin": "513243317102", "circle": "408", "zone": "19", "returnNo": "119", "remarks": ""},
    {"drive": "7 / 7", "assessee": "Md. Asif Ali Zaman / Nasrin", "tin": "437110316084 / 389307745851", "circle": "318 / 121", "zone": "15 / 06", "returnNo": "120 / 118", "remarks": ""},
    {"drive": "7", "assessee": "Saima Islam (Wife Of Mozib)", "tin": "846558265715", "circle": "128", "zone": "06", "returnNo": "", "remarks": ""},
    {"drive": "7", "assessee": "Md. Mozibur Rahman (Sc. Lab)", "tin": "125746976519", "circle": "127", "zone": "06", "returnNo": "", "remarks": ""},
    {"drive": "7 / 7", "assessee": "Mohammad Abdul Hakim Babu / Md. Ziaur Rahman (Mujib Brother)", "tin": "312431119784 / 546254959261", "circle": "128 / 03", "zone": "06 / 01", "returnNo": "153 / 124", "remarks": ""},
    {"drive": "7", "assessee": "Shamsun Naher (Zia, Mujib)", "tin": "241840853004", "circle": "19", "zone": "01", "returnNo": "132", "remarks": ""},
    {"drive": "7", "assessee": "Mia Md. Mortayez Amin", "tin": "779725198592", "circle": "208", "zone": "10", "returnNo": "149", "remarks": ""},
    {"drive": "7", "assessee": "Tamanna Begum", "tin": "788989997801", "circle": "86", "zone": "04", "returnNo": "150", "remarks": ""}
]

# Streamlit UI Configuration
st.set_page_config(page_title="কন্টাক্ট ডিরেক্টরি সার্চ", page_icon="📱", layout="centered")

st.title("📱 কন্টাক্ট ডিরেক্টরি সার্চ")

# Search Input
search_query = st.text_input("🔍 নাম টাইপ করে সার্চ করুন:", placeholder="যেমন: Islam, Sultana, Palash...")

if search_query.strip():
    query = search_query.strip().lower()
    filtered_contacts = [c for c in contacts if query in c["assessee"].lower()]

    if filtered_contacts:
        st.subheader(f"ফলাফল ({len(filtered_contacts)} টি পাওয়া গেছে):")
        for item in filtered_contacts:
            with st.expander(f"👤 {item['assessee']}", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Drive:** {item['drive']}")
                    st.write(f"**TIN:** {item['tin']}")
                    st.write(f"**Circle:** {item['circle']}")
                with col2:
                    st.write(f"**Zone:** {item['zone']}")
                    st.write(f"**Return No:** {item['returnNo']}")
                    st.write(f"**Remarks:** {item['remarks'] if item['remarks'] else 'N/A'}")
    else:
        st.warning("কোনো তথ্য পাওয়া যায়নি।")
else:
    st.info("উপরে সার্চ বক্সে নাম লিখে সার্চ করুন।")

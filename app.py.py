contacts = {
    "রহিম": {"ঠিকানা": "মিরপুর", "ফোন": "01700000000"},
    "করিম": {"ঠিকানা": "উত্তরা", "ফোন": "01700000001"},
}

name_to_search = input("কার তথ্য খুঁজছেন? ")

if name_to_search in contacts:
    print(f"ঠিকানা: {contacts[name_to_search]['ঠিকানা']}")
    print(f"ফোন: {contacts[name_to_search]['ফোন']}")
else:
    print("তথ্য পাওয়া যায়নি।")

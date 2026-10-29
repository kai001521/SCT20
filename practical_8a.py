# Practical 8A: Find Ratios Using Fuzzy Logic
# Source: SCT Shortest code with original output.docx

from fuzzywuzzy import fuzz
print("This is Practical 8A")
a='FuzzyWuzzy is a lifesaver!'; b='fuzzy wuzzy is a LIFESAVER.'
print("Similarity score: {}".format(fuzz.ratio(a.lower(),b.lower())))
a='Chicago Illinois'; b='Chicago'
print("partial_ratio: {}".format(fuzz.partial_ratio(a.lower(),b.lower())))
a='Gunner William Kline'; b='Kline, Gunner William'
print("token_sort_ratio: {}".format(fuzz.token_sort_ratio(a.lower(),b.lower())))
a='The 3000 meter steeplechase winner, Soufiane El Bakkali'; b='Soufiane El Bakkali'
print("token_set_ratio: {}".format(fuzz.token_set_ratio(a.lower(),b.lower())))

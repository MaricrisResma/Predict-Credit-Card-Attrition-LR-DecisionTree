import re
# my_words = "Because it's not Blippi 143 15 9"

# print(my_words)

# reg_list = ["[A-Z]", "[a-z]+", "[^a-z]", "[a-z]+", "^Beca", "9$"]

# for pattern in reg_list:
#     print(re.findall(pattern, my_words))



import re
my_words = "bnd"

print(my_words)

reg_list = ["ba*n", "ba+n", "ba?n"]

for pattern in reg_list:
    print(re.findall(pattern, my_words))
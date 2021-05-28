''' [Question 1157]'''

words = input().upper()
# Alphabet_list shows which alphabet is in the input
Alphabet_list = list(set(words))

# Alphabet_count shows how many same numbers is in the input
Alphabet_count = []
for x in Alphabet_list:
    cnt = words.count(x)
    Alphabet_count.append(cnt)

if Alphabet_count.count(max(Alphabet_count)) > 1:
    print("?")
else:
    find_index = Alphabet_count.index(max(Alphabet_count))
    print(Alphabet_list[find_index])





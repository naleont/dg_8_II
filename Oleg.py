with open('dg_8_II/Oleg.txt', encoding='utf-8') as f:
    text = f.read()

symbols = {}
text = text.lower()

for symb in text:
    if symb in symbols.keys():
        symbols[symb] += 1
    else:
        symbols[symb] = 1

print(symbols)

# words = text.split()

# for word in words:
#     new_word = word.strip('.,?!":;»«— …')
#     print(new_word)
def format_name(name):
    split_name = name.split()
    new_name = []
    for n in split_name:
        if n:
            new_name.append(n)
    l_name = new_name[0]
    f_name = new_name[1]
    new_name[0] = l_name[0].upper() + l_name[1:].lower()
    new_name[1] = f_name[0].upper() + f_name[1:].lower()
    res_name = ' '.join(new_name)
    return res_name

with open('dg_8_II/names.txt', encoding='utf-8') as f:
    text = f.read()

names = text.split('\n')
for name in names:
    if name:
        new_name = format_name(name)
        print(new_name)

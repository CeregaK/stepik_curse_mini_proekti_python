#str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
# Выводит строк типа  A10B31C2XYZD4E3F3
def word_count(str):
    n_str = ""
    for i in str:
        a = str.count(i)
        if i not in n_str:
            if a == 1:
                n_str += f'{i}'
            else:
                n_str += f'{i}{a}'
    return n_str

print(word_count(input("input word:")))

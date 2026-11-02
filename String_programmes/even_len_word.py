def even_len_word(w):
    w=w.split(' ')
    for word in w:
        if len(word)%2==0:
            return word
        else:
            return "enter even length word"
print(even_len_word("mourya"))
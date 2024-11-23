# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1.44
page_count = 100
str_count = 50
sym_count = 25
cap = 4
book_cap = page_count*str_count*sym_count*cap/1024**2
book_count = int(memory//book_cap)
print("Количество книг, помещающихся на дискету:", book_count)

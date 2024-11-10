# TODO Найдите количество книг, которое можно разместить на дискете

pages = 100
lines = 50
symbols = 25
volume_one_symbols = 4 # в байтах

volume_one_book_b = pages * lines * symbols * volume_one_symbols

volume_disk = 1.44 # в мбайтах

volume_one_book_mb = volume_one_book_b / (1024 * 1024)
number_book_disk = volume_disk // volume_one_book_mb

print("Количество книг, помещающихся на дискету:", int (number_book_disk))

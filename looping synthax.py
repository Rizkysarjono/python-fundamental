"""
looping syntax
"""
amount_of_books = 100
print('mom said,"read all your books"')

amount_of_read_books = 0
print(f'amount of read books {amount_of_read_books}')

for amount_of_read_books in range(1,amount_of_books+1):
    print(f'book {amount_of_read_books} have been read')

print(f'amount of read books {amount_of_read_books}')
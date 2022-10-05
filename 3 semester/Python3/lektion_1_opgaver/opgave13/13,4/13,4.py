numbers = [1, 2, 3, 4, 5, 6, 7, 8]
uneven_number_filter = filter(lambda x: (x%2 != 0), numbers)
uneven_numbers = list(uneven_number_filter)
print(uneven_numbers)
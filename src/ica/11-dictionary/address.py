betsy_info = {"name": "Betsy", "city": "Saint Paul", "age": 31}
tom_info = {"name": "Tom", "city": "Saint Paul", "age": 28}

address_book = [betsy_info, tom_info, {"name": "Sue", "city": "Saint Paul", "age": 45}]

print(address_book)

address_book.append({"name": "Henry", "city": "Minneapolis", "age": 22})
address_book.append({"name": "Alice", "city": "Chicago", "age": 35})

def filter_by_city(city, book):
    return [entry for entry in book if entry["city"] == city]

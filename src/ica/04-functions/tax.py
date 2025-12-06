def add_tax(price, tax_rate):
    print('add tax:', price)
    price += tax_rate * price
    print('price:', price)
    return price
    return price
    tax_amt = price * tax_rate
    return price + tax_amt

print(add_tax(25.99, 0.0725))
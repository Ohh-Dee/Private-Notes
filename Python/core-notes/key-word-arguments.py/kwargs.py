# uses 2 unpacking operators

def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

print_address(street="456 Fake Street", city="Detroit", state="Michigan", zip="54231")
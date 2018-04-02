print("Template, (c) Verloka Vadim 2018\n\n\n")

from string import Template

def Main():

    cart = []
    cart.append(dict(name = "Apple", price = 48, count = 64))
    cart.append(dict(name = "Banana", price = 38, count = 164))
    cart.append(dict(name = "Rasbery", price = 148, count = 644))
    cart.append(dict(name = "Tomato", price = 8, count = 14))

    template = Template("$name x $count = $price")

    print("Cart:")
    for item in cart:
        print(template.substitute(item))

if __name__ == "__main__":
    Main()
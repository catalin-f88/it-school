# def product(a, b, *args):
#     """ Calculate the product of two or more numbers. """
#     p = a * b
#     for i in args:
#         p *= i
#     return p

# print(product(1,2,3,4))
def demo(**kwargs):
    return kwargs

def box_price(h, l, w, type=1, p=25, **kwargs):
    """ Calculate the price 
    - kwargs: 
        -cq2 = value if t = 2;
        -cq3 = value if t = 3 """
    
    raw_price = h * l * w * p
    if type == 1:
        return raw_price
    if type == 2:
        return raw_price * kwargs.get("cq2", 1.1)
    if type == 3:
        return raw_price * kwargs.get("cq2", 1.2)

boxes = [
    {
        "h": 2,
        "l": 3,
        "w": 4
    }, 
    {
        "h": 2,
        "l": 3,
        "w": 4,
        "type": 2
    },
    {
        "h": 2,
        "l": 3,
        "w": 4,
        "type": 2,
        "p": 23
    }
]

for box in boxes:
    demo(**box)
    print(f"Pret cutie: {box_price(**box)} RON")


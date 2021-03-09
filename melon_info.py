"""Print out all the melons in our inventory."""


from melons import melon_information


def print_melon(name, price, seeded, flesh, weight, rind):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')
    seeded_or_not = True
    if seeded:
        seeded_or_not = False


    print(f"""{name}
    seedless: {seeded_or_not}
    price: ${price:.2f}
    flesh_color: {flesh}
    weight: {weight}
    rind_color: {rind}
    """)


for i in melon_information:

    print_melon(melon_information[1][i],
    melon_information[2][i], 
    melon_information[3][i], 
    melon_information[4][i], 
    melon_information[5][i], 
    melon_information[6][i])


word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Takes one down")
    print("Pass it around.")
    if beer_num == 1:
        word = "bottle"
        print(f"No more {word} of beer on the wall.")
    else:
        new_num = beer_num - 1
        print(new_num, word, "of beer on the wall left.")
    print()

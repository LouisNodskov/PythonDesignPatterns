def count_to(count):
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf", "sechs", "sieben", "ocht", "neun", "zehn"]

    iterator = zip(range(count), numbers_in_german)



    for position, number in iterator:
        yield number

if __name__ == "__main__":
    for num in count_to(10):
        print("{}".format(num))
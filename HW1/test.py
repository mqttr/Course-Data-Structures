def gen():
    for x in range(5):
        yield x

def main():
    for x in gen():
        print(x)




main()
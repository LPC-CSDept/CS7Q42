
evencnt = 0


def main():
    global evencnt
    number = []
    evencnt = 0

    for i in range(10):
        number.append(int(input()))
    ##################################################
    # Code your program here
    ##################################################
    prev = 0
    on = 0
    for v in number:
        if prev and not v % 2 and not on:
            on = 1
            evencnt += 1
        if v % 2:
            prev = 0
            on = 0
        else:
            prev = 1

    print(evencnt)

##


if __name__ == '__main__':
    main()

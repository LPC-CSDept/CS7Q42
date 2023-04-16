
lognest = ''
shortest = ''


def main():
    global longest, shortest

    ##################################################
    # Code your program here
    ##################################################
    inputval = input()
    shortest = longest = inputval
    minlen = maxlen = len(shortest)
    while inputval != 'stop' and inputval != 'STOP':
        if minlen > len(inputval):
            minlen = len(inputval)
            shortest = inputval
        if maxlen < len(inputval):
            maxlen = len(inputval)
            longest = inputval
        inputval = input()

    print(longest)
    print(shortest)


if __name__ == '__main__':
    main()

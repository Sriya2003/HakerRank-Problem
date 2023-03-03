def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # TOP N lines
    topN = ""
    for i in range(size):
        string = alphabet[(size-1):(size-i-1):-1] + alphabet[(size-i-1):(size)]
        string = "-".join(list(string))
        string = string.center(4*size-3, "-")
        topN += string + "\n"
    for i in range(size-2, -1, -1):
        string = alphabet[(size-1):(size-i-1):-1] + alphabet[(size-i-1):(size)]
        string = "-".join(list(string))
        string = string.center(4*size-3, "-")
        topN += string + "\n"     
    print(topN)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
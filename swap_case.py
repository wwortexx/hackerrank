def swap_case(s):
    ret = ''
    for c in s:
        if c == ' ':
            ret += c
        elif c.islower():
           ret += c.upper()
        elif c.isupper():
            ret += c.lower()
        else:
            ret += c
    return ret

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
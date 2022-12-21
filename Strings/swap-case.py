def swap_case(s):
    t = ''
    for char in s:
        if char.isupper():
            t += char.lower()
        else:
            t += char.upper()
    return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
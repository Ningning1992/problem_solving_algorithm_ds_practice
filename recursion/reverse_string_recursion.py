def reverse(s):
    if len(s) == 1:
        return s
    elif len(s) == 0:
        return ""
    else:
        return reverse(s[1::]) + s[0]

if __name__ == "__main__":
    print(reverse("hello"))
    print(reverse("l"))
    print(reverse("follow"))
    print(reverse(""))


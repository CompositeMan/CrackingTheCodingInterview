
counter = 0

def permutation(s, prefix):
    permutations(s, "")

def permutation(s, prefix):
    global counter
    if len(s) == 0:
        counter +=1
        print(prefix)
    else:
        for i in range(len(s)):
            rem = s[0:i] + s[i+1:]
            print("Calling recursively")
            counter += 1
            permutation(rem, prefix+s[i])


if __name__ == '__main__':
    s, p = "ABC", "12"
    permutation(s, p)
    print(f"Total calls {counter}")


def diff(arr, k):
    if len(arr) <=1:
        return 0,[],[]

    h_set = set()
    counter = 0
    pairs = []

    while len(arr) > 0:
        both = [False, False]
        elm = arr.pop()
        if elm-2 in h_set:
            counter += 1
            pairs.append((elm-2, elm))
            both[0] = True
        if elm+2 in h_set:
            counter += 1
            pairs.append((elm, elm+2))
            both[1] = True
        if not (both[0] and both[1]):
            h_set.add(elm)
    return counter, h_set, pairs

def test(arr =  [1,7,5,9,2,12,3] , k=2):
    print(f"Testing : {arr} with k:{k}")
    res, s, p = diff(arr, k)
    print(f"result : {res}, with pairs {p}")

    #difference_2 = [ (1,3), (3,5), (5,7), (7,9) ]
    #print(f"Correct {difference_2}")
if __name__ == '__main__':
    test()
    test([1], 10)
    test([1,2,3,4,5], 2)

#Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

""" 
[ 1, 2, 3, 4, 5, 6]
[ 1, 2, 3, 4, 5, 6]
[ 1, 2, 3, 4, 5, 6]
[ 1, 2, 3, 4, 5, 6]
[ 1, 2, 3, 4, 5, 6]
[ 1, 2, 3, 4, 5, 6]

iter = 0

lv = 0 -> (0, 0), (5,0), (5,5), (0,5)

lv = 1 -> (1,1), (4,1), (4,4),(1,4)

lv =2 -> (2,2), (3,2), (3,3), (2,3)

iter = 1

lv = 0 -> (0,1), (4,0), (5,4), (1,5)

lv = 1 -> (1,2), (3,1), (4,3), (2,4)
"""




def rotate_corners(m, lv=0):

        end = len(m)-lv-1
        #for i in range(0, len(m)-(lv*2)-1):
        for i in range(1, len(m)-(lv*2)):
                t = m[lv][lv+i]
                print(f"m[{lv}][{lv+i}] ({m[lv][lv+i]}) is changed to m[{end-i}][{lv}] ({m[end-i][lv]})")
                m[lv][lv+i] = m[end-i][lv]
                # m[end-i][lv] = m[end][end-i]
                # m[end][end-i] = m[lv+i][end]
                # m[lv+i][end] = t
        

def print_matrix(m):
        print("-"*100)
        for r in m:
                print(r)
        print("-"*100)
def test():
        d = 4
        m = [None]*4
        for i in range(d):
                v = 4*i
                m[i] = list(range(v, v+4)) 
                # m[i] = [i]*d 

        print_matrix(m)
        rotate_corners(m, 0)
        print_matrix(m)

        

  

test()

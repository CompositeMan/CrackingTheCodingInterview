#You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of ls you could create.
# 1775 (or: 11011101111) -> output:8


# when I first see a 0, I make it one and continue, 
#I remember its index
# if I see another zero, 
# I compare the index of first zero and this one, 
# If the diff is 1, I make the length = 0
#pop the, 
#I check if it max or not, update the max accordingly 


101010111010

length = 0 
i = -1
at = 0

1 010011010
length = 1
i = -1
at = 0
max = -1

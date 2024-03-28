

smallest = None # accumulator variable
sum = 0 # accumulator variable
print('Before:', smallest)
for itervar in [3, 41, 12, 1, 74, 15]:
    if (smallest is None) or (itervar < smallest):
        smallest = itervar # update accumulator variable
        print('Iteration:', itervar, smallest)
        print('Smallest:', smallest)
else:
 print('not found')
    
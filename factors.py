#def factors(n):

#create a function to find factors 

def find_factors(n):
    factors = []
    for number in range(1,n+1):
        if n%number == 0:
            factors.append(number)         
    return factors

print(find_factors(6))

#create a function to find factors of n_factors 
def factors(n):
    factors = find_factors(n)
    myDictionary = {}
    for x in factors:
        myDictionary[x] = find_factors(x)
    return myDictionary

print(factors(6))



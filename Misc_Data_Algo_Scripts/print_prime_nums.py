#print prime numbers () between 100-200

def print_prime_nums():
    for num in range (100,200):
        if all(num%i!=0 for i in range (2,num)):
            print(num)

print(print_prime_nums())

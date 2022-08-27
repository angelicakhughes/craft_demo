from functools import reduce

domain = [1, 2, 3, 4, 5]

our_range = map(lambda num: num * 2, domain)
print(list(our_range))


evens = filter(lambda num: num % 2 ==0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

wordslist = ['Boss', 'a', 'fig', 'Alfred', 'Daemon','dig']

#stringwords = print(str(sorted(words)))

words = (map(lambda words: words.lower(), wordslist))

b = list(sorted(words))

print(b)



#hello = 'hello'
#print(str(hello.lower()))



#print("sorting with a method")
#words.sort(key=str.lower, reverse=True)
#print(words)

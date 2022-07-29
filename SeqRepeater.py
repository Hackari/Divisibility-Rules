n = 10 #Change base here
primes = []#Insert p here
space = []
 
for p in primes:
    count = 0
    div = 1
    
    mod = []
    for i in range(0,p):
        a = n**i
        b = a % p
        if b == 1:
            mod.append('One')
            count += 1
            if count == 2:
                space.append(div)
                print(f'When p = {str(p)}, Sequence repeats every {str(div)} terms')
                break
        else:
            mod.append(b)
            div += 1
            
    print(str(p)+' : '+str(mod))
    print()
#print(space)
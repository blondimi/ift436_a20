from random import choice

def pseudomed(s, k):
    t = []
    
    for _ in range(k):
        t.append(choice(s))

    t.sort()

    return t[len(t) // 2]

if __name__ == "__main__":
    repetitions = 10000
    num_erreurs = 0

    s = [1, 2, 3, 4]
    k = 3
    
    for _ in range(repetitions):
        x = pseudomed(s, k)
        
        if x == 1 or x == 4: # Attention, à changer manuellement si s change
            num_erreurs += 1

    print("{}".format(num_erreurs / repetitions))

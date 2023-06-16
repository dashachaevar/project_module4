

def strcounter(a):
    print(set(a))
    for sym in set(a):
        counter = 0
        for sub_a in a:
            if sym == sub_a:
                counter += 1 
        print(sym, "-", counter)

# strcounter("abbbcc")

def strcounter2(a):
    syma_counter = {}
    for sym in a:
        syma_counter[sym] = syma_counter.get(sym, 0) + 1
        
    for sym, count in syma_counter.items():
        print(sym, "-", count)

strcounter2("abbbcc")
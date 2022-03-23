
def quick_sort(n):
    if len(n) < 2:
        return n
    else:
        pivot = n[0]
        left = [x for x in n[1:] if x <  pivot]
        right = [x for x in n[1:] if x >  pivot]
        return quick_sort(left)+[x for x in n if x==n[0]] +quick_sort(right)

if __name__ =="__main__":    
    test_list = [19,290,10,34,22,9]
    print(quick_sort(test_list))
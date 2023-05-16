def main():
    with open('day1input.txt') as f:
        p=[i.strip() for i in f.readlines()]
    
    sum_lists = []
    current_sum = 0
    for val in p:
        if(val!=''):
            current_sum+=int(val)
        else:
            sum_lists.append(current_sum)
            current_sum = 0 
    sum_lists.sort(reverse=True)
    print(sum_lists[0])

    # part 2 
    print(sum_lists[0]+sum_lists[1]+sum_lists[2])

main()
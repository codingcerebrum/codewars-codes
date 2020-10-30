def sequence(start, n, k):
    result = []
    final = [start]
    for x in range(0,k):
        print('here2')
        numlist = [int(each)**n for each in str(start)]
        start = 0
        
        for each in numlist:
            start += each 

        if(start in final):
            print("here")
            result.append(x)
            result.append(final[final.index(start):(x+1)])
            result.append(len(result[1]))
            result[0] -= (result[2] - 1)
            break

        final.append(start)

    last = (k - result[0]) % result[2]
    result.append(result[1][last])
    return result

print(sequence(420,4,30))
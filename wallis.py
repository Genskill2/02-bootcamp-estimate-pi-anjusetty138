#estimation of pi byy wallis forumla

def wallis(n):
    #assign 1 to a golabal variable pi_walli
    pi_walli = 1

    #keep multiplying the terms in the wallis formula for the given range n
    for i in range(1,n):
        pi_walli *= ((4*pow(i, 2))/((4*pow(i, 2))-1))

    #now multiply the pi_walli with 2 and return the value
    return(pi_walli*2)

if __name__ == '__main__':
    num = int(input('Enter the range: '))
    print('The estimated pi value is: ',wallis(num))
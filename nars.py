def narsis(n):
    if (n <= 999):
        n=str(n)
        panjang = len(n)
        total = 0
        for i in n:
            total+=int(i)**panjang
        if total == int(n):
            print('Narcissitic')
        else:
            print('Bukan')
    else:
        print('Melewati batas maksimal (999)')

# narsis(123)

def pentagon(n):
    if (n==0):
        return 0
    else:
        suku = n*(((3*n)-1)/2)
        pentagon(n-1)
        print(int(suku), end=' ')

    
pentagon(0)
    


def sumsquare():
    odd_sum=0
    even_sum=0
    for i in list:
        if i%2==0:
            even_sum=even_sum+(i**2)
        else:
            odd_sum=odd_sum+(i**2)
    print(odd_sum,even_sum)
list=[1,4,9,12,13,18,30]
sumsquare()

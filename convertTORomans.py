def  convertToRoman(num):
    dec = [1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5,4, 1]
    romans = ["M","CM", "D","CD", "C", "XC", "L","XL", "X", "IX", "V","IV", "I"]
    result = ""
    i=0

    for i in range(len(dec)):
        while (num%dec[i] < num):
            result= result+ romans[i]
            num = num - dec[i]
            print (num)
            print(result)
        
    return result

print (convertToRoman(649))

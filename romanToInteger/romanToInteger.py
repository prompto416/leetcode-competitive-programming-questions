class Solution(object):
    def romanToInt(self,s):
        usin = s
        romanSymbol = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        romanVal = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        #specialRomanSymbol = ["IV","IX","XL","XC",]
        # romanSymbol = ["I","V","X","L","C","D","M"]
        # romanVal = [1,5,10,50,100,500,1000]

    
        tuples = [(key, value) for i, (key, value) in enumerate(zip(romanSymbol,romanVal))]
        romanNum = dict(tuples)
        
        solution = 0
        i = 0
        while i < len(s):
            try:
                print("special case",s[i:i+2],romanNum[s[i:i+2]])
                solution += romanNum[s[i:i+2]]
                i+= 1
            except:
                solution += romanNum[s[i]]
                print("normal case",s[i],romanNum[s[i]])
            i += 1
        return solution
    
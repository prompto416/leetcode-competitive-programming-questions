class Solution:
    def intToRoman(self,num):
        romanSymbol = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        romanVal = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

        # romanSymbol = ["I","V","X","L","C","D","M"]
        # romanVal = [1,5,10,50,100,500,1000]

        n = num
        tuples = [(key, value) for i, (key, value) in enumerate(zip(romanVal, romanSymbol))]
        romanNum = dict(tuples)


        preSolution = []
        solution = ""
        i = 0 
        while n > 0: #Big O = 7n --> n --> linear 
            while i < len(romanVal):
                print("note: ",n,"compare",romanVal[i],"iteration",i)
                if n <= 0:
                    break
                if n == romanVal[i]:
                    print(f"Exact Case: {n}-{romanVal[i]} = {n-romanVal[i]}")
                    #print(romanVal[i])
                    n -= romanVal[i]
                    preSolution.append(romanVal[i])
                    i = 0 
                    
                    #append answer to preSolution
                    
                elif n < romanVal[i]: #main case where n is not exact so we find the nearest value
                    # print(romanVal[i-1])
                    print(f"Nearest Val case: {n}-{romanVal[i-1]} = {n-romanVal[i-1]}")
                    n-= romanVal[i-1]
                    preSolution.append(romanVal[i-1])
                    i = 0 
                    
                elif (n > 1000) :
                    print(f"Special Case: {n}-{1000} = {n-1000}")
                    n -= 1000  #1000 is the max value available for the roman number notation
                    preSolution.append(1000)
                    i = 0
                i += 1
                    
                

        print(preSolution)

        for i in preSolution:
            solution += romanNum[i]
            
        return solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # turn it into number
        num = 0
        for i in range(len(digits)-1,-1,-1): 
            num+=digits[i]*(10**(len(digits)-1-i))
        # +1 
        print(num)
        num +=1 
        # turn it to string 
        num = str(num)
        # turn it into list 
        output_l = []
        for i in range(len(num)): 
            output_l.append(int(num[i])) 
        # return 
        return output_l 
        
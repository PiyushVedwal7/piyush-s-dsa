#Remove Outermost Parentheses
"""Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()"."""


class Parenthesis:
    def outer(string):
        stk=[]
        res=[]

        for char in string:
            if char=='(':
                if len(stk)>0:
                     res.append(char)
                    
               
                stk.append(char)

            elif char==')':
                stk.pop()
                if len(stk)>0:
                    res.append(char)    
        return ''.join(res)




if __name__=='__main__':
    string= "(()())(())"
    print(Parenthesis.outer(string))


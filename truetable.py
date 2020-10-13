from conversion import Conversion
import numpy as np

# This function replace postfix expression by each binary case of each column, for ex. ab+ convert to 00+ in the first column and so one for the others.
def Bin_sustitution(posfix, operands, bin_value):    
    
    bin_expr = posfix
    for i, j in enumerate(operands):
        bin_expr = bin_expr.replace(j, str(bin_value[i]))
    return bin_expr

values = []  

# This function evaluate those resulting expresions from the sustitution.
def Evaluate_expr(t):
    stack = []
    try:
        for num in t:
            # If we find a 0 or a 1 in the expression we add it in the list.
            if num == '0':
                num = int(not bool(num)) 
                stack.append(num)
            elif num == '1':
                num = int(bool(num))
                stack.append(num)
            #when we find a ~ we take the last caracter adding to the list and we 
            # convert it into his negation and then we put it in the list again.
            elif num == '~':
                neg = int(not bool(stack.pop()))
                stack.append(neg)
                
            else: # When we find a + or a * we take 2 succesive caracter in the list an make num1 or num2 or num1 and num2.
                num_1 = stack.pop()
                num_2 = stack.pop()
                if num == '+':
                    stack.append(int(bool(num_1 or num_2)))
                elif num == '*':
                    stack.append(int(bool(num_1 and num_2)))
        return stack[0]
    
    except IndexError:
        return "Invalid input, please try with a valid one (for ex. a+b)"
        

# To determine if the expression is a tautology.
def Is_tautology(t):
    
    for i in t:
        if i==1 and t.count(1)==len(t):
            return "Yes"
            break
        elif i==0 and t.count(0)==len(t): 
            return "No"
            break
        elif i==1 and t.count(1)!=len(t): 
            return "No"
            break
        elif i==0 and t.count(0)!=len(t):
            return "No"
            break
        else:
            return ""
            break

# To determine if the expression is a contradiction.
def Is_contradiction(t):
    for i in t:
       
        if i==0 and t.count(0)==len(t): 
            return "Yes"
            break
        elif i==1 and t.count(1)==len(t):
            return "No"
            break
        elif i==1 and t.count(1)!=len(t): 
            return "No"
            break
        elif i==0 and t.count(0)!=len(t):
            return "No"
            break
        else:
            return ""
            break

# To determine if the expression is a contigency.
def Is_contingency(t):
    for i in t:
        if i==1 and t.count(1)==len(t):
            return "No"
            break
        elif i==0 and t.count(0)==len(t): 
            return "No"
            break
        elif i==1 and t.count(1)!=len(t): 
            return "Yes"
            break
        elif i==0 and t.count(0)!=len(t):
            return "Yes"
            break
        else:
            return ""
            break

# To determine if the expression is satisfiable.
def Is_satisfiable(t):
    for i in t:
        if i==1 and t.count(1)==len(t):
            return "Yes"
            break
        elif i==0 and t.count(0)==len(t): 
            return "No"
            break
        elif i==1 and t.count(1)!= len(t): 
            return "Yes"
            break
        elif i==0 and t.count(0)!=len(t): 
            return "Yes"
            break
        else:
            return ""
            break

# expr = "a+b"
# expression= tuple(expr)

# obj = Conversion(len(expr)).toPostfix(expr)
# print(obj)

# operands = []
# for i in expression:
#     if i.isalpha():
#         operands.append(i)
# operands.sort()        
# len = len(operands)
# row = 2**len
# List = list(range(0, row))

# n = []
# for i in List:
#     n.append(tuple(np.binary_repr(int(i), width=len)))

# result = []
# for b in n:
#     result.append(Bin_sustitution(obj, operands, b))

# print(result)

# for col in result:
#     values.append(Evaluate_expr(col))

# print(values)
# print(" operands: {} and Binary List: {} ".format(operands,  n))

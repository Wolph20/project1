
# This algorithm convert the infix expression to the postfix one.
class Conversion:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack = []
        self.output = []
        self.precedence = {'+':0, '*':1, '~':2}
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False 
    
    def topChar(self):
            return self.stack[-1]
        
    def push(self, item):
        self.top += 1
        self.stack.append(item)
            
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        
    def isOperand(self, c):
        return c >= 'a' and c <= 'z'

    def notGreater(self, char):
        try:
            a = self.precedence[char]
            b = self.precedence[self.topChar]
            return True if a <= b else False
        except KeyError:
            return False

    def toPostfix(self, expression): #Conversion from infix to postfix expression.
        #result = ""
        
        #stack = Stack(15)
        
        for char in expression:
            
            if self.isOperand(char): # If the caracter is an operand, we print it.
                self.output.append(char)
                            
            elif char == '(':
                self.push(char)
                
            elif char == ')': # if we find a right parenthesis, we look the stack and output every character until the left parenthesis.
                while ((not self.isEmpty()) and self.topChar() != '('):
                    cpop = self.pop()
                    self.output.append(cpop)
        
                if (not self.isEmpty() and self.topChar() != '('):
                    return -1
                else:
                    self.pop()
            else: # An operator is finded, we just push it at the stack.
                while (not self.isEmpty() and self.notGreater(char)):
                    self.output.append(char)
                self.push(char)
                
        # Finally, we pop all the operators from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
        return "".join(self.output)
#expression= exp = "(~a+b)*~(c+d)"
#obj = Conversion(len(expression)).toPostfix(expression)
#Postfix= obj.toPostfix(expression)
#print(obj)
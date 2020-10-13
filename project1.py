from flask import Flask, render_template, request
from truetable import Bin_sustitution, Evaluate_expr, Is_tautology, Is_contradiction, Is_contingency, Is_satisfiable
from conversion import Conversion
import numpy as np
app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/program', methods=['POST'])
def program():
    
    if request.method == 'POST':
        expr = request.form['expr']
        # print(expr)
        values = []
        # expr = "(a+~c)*~(b+d)"
        expression= tuple(expr)

        operands = [] # Save the input variables, only letter from english alphabet.
        for i in expression:
            if i.isalpha() and i not in operands:
                operands.append(i)
        operands.sort()        
        lena = len(operands) # Total of variable, this permit us to know how many columns and rows we gonna use.
        row = 2**lena
        
        List = list(range(0, row))

        n = [] # Depends of the length of the variable, we iterate the range of the total variables (form 0 to n) and coonvert them into binary number.
        for i in List:
            n.append(tuple(np.binary_repr(int(i), width=lena)))
        
        obj = Conversion(len(expr)).toPostfix(expr) # This function convert the input expression into postfix expression.

        result = [] # We save a list of 0's an 1's, to use them like the truth and false values of the truth table.
        for b in n:
            result.append(Bin_sustitution(obj, operands, b))

        # We evaluate the truth table column by column.
        for col in result:
            values.append(Evaluate_expr(col))
        
        # The total of row of each index in, is equal to the total of variable.
        total_of_row = len(n[0])

        # Convert the binary array string in an integer binary array in order to facilitate the view of the web interface.
        def toInteger(x):
            return int(x)

        # Get the index of each value.
        def getIndexValue(o):
            def get(array):
                return array[o]
            return get

        # The map función allows us to take a specific object in a specific position in order to manipulate it, in this case we use
        # map to make a list of integer number.
        data = [] # Stores the new list of the truth table values
        for i in range(total_of_row):
            values_str = map(getIndexValue(i), n)
            values_int = list(map(toInteger, values_str))
            data.append(values_int)
        
        prin_data=[] # We save the truth values of each variable in a dictionnary to use later in the view.
        for i, j in enumerate(operands):
            c = dict()
            c['title'] = j
            c['values'] = list(data[i])
            prin_data.append(c)
        
        tauto = Is_tautology(values) # With this function we evaluate if the expression is a tautology.
        contra = Is_contradiction(values)# With this function we evaluate if the expression is a contradiction.
        conti = Is_contingency(values)# With this function we evaluate if the expression is a contingency.
        satis = Is_satisfiable(values)# With this function we evaluate if the expression is satisfiable.
        
    return render_template('result.html', operands=operands, expr=expr, t_val=prin_data, t_result=values, tauto=tauto, contra=contra, conti=conti, satis=satis)



if __name__ == '__main__':
    app.run(port = 3000, debug = True)
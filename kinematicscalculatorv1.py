#Python 3.8
import math
from sympy.solvers import solve

#list set for list comprehension later in the function
symbols = ['Vavg', 'Vo', 'Vf', 'a', 't', 'x']

#start of function
def KineCalc():
    answers = []
    print('\nWelcome to Kinematics Calculator, type "answers" to see answers and "exit" to exit')
    while True:
    #inputs to get the values
        solvent = input("\n\nwhat value are you trying to find(x, t, Vo, Vf, Vavg, a)? ")

        #checks to see if any of the inputs were keywords or if they input an actual option
        if solvent.lower() == 'exit':
            break
        elif solvent.lower() == 'answers':
            for val in answers:
                print(val)
            break
        elif solvent not in symbols:
            print('"{}" is not an option, please try again'.format(solvent))
            continue

        #all values with one input with a statement telling the person what to do
        print('\nAll the values will be asked for, if you do not know the value please write the variable again\n')
        Vavg, Vo, Vf, a, t, x = [input('{}: '.format(symbols[ct])) for ct in range(0,6)]

        #all equations put in string form for sympy and set to 0
        eq7 = '(('+Vo+')+('+Vf+'))/2-('+Vavg+')'
        eq8 = '((('+Vo+')+('+Vf+'))/2)*('+t+ ')-('+x+')'
        eq9 = '('+Vf+')-('+ Vo+ ')-(' +a+')*('+t+')'
        eq10 = '('+Vo+')**2 + 2*('+a+')*('+x+ ')-('+ Vf+')**2'
        eq11 = '(('+a+')*('+t+')**2)/2 +('+ Vo+')*('+t+ ')-('+ x+')'
        equations = [eq7, eq8, eq9, eq10, eq11]

        #first loop finds the best equation
        for ct in range(0,5):
            try:
                #checks if the answer is correct
                ans = float(solve(equations[ct], solvent)[0])
                #prints with correct formatting
                print('\nthe equation is {}'.format(equations[ct]))
                print('the answer is {}'.format(ans))
                #puts the values into the answers list with correct formatting
                if ans in answers:
                    answers.append('{} is a repeat'.format(ans))
                else:
                    answers.append(ans)
            except:
                pass

KineCalc()

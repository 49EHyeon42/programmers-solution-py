import question
import solution

if __name__=="__main__":
    parameter = question.Question(10, 10).createString()
    
    print("1. Input :", parameter)
    if solution.mySolution(parameter) != solution.referenceSolution1(parameter):
        print("error 1")
    elif solution.mySolution(parameter) != solution.referenceSolution2(parameter):
        print("error 2")
    elif solution.mySolution(parameter) != solution.referenceSolution3(parameter):
        print("error 3")
    else:
        print("pass")

    test = "Test C  oDe"
    print("2. Input :", test)
    if solution.mySolution(test) != solution.referenceSolution2(test):
        print("1 :", solution.mySolution(test))
        print("2 :", solution.referenceSolution2(test))
    else:
        print("pass")
import question
import solution

if __name__=="__main__":
    parameter = question.Question(10, 3, 10).createString()
    
    print("Input :", parameter)
    if solution.mySolution(parameter) != solution.referenceSolution1(parameter):
        print("Output : error 1")
    elif solution.mySolution(parameter) != solution.referenceSolution2(parameter):
        print("Output : error 2")
    elif solution.mySolution(parameter) != solution.referenceSolution3(parameter):
        print("Output : error 3")
    else:
        print("Output : pass")
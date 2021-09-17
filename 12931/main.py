import question
import solution

if __name__=="__main__":
    parameter = question.Question().createNaturalNumber()
    
    print("Input :", parameter)
    if solution.mySolution(parameter) != solution.Solution1(parameter):
        print("Output : error 1")
    elif solution.mySolution(parameter) != solution.Solution2(parameter):
        print("Output : error 2")
    elif solution.mySolution(parameter) != solution.Solution3(parameter):
        print("Output : error 3")
    else:
        print("Output : pass")
    
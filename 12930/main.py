import question
import solution

if __name__=="__main__":
    parameter = question.Question(10, 10).createString()
    if solution.mySolution(parameter) != solution.referenceSolution1(parameter):
        print("error 1")
    elif solution.mySolution(parameter) != solution.referenceSolution2(parameter):
        print("error 2")
    elif solution.mySolution(parameter) != solution.referenceSolution3(parameter):
        print("error 3")
    else:
        print("pass")

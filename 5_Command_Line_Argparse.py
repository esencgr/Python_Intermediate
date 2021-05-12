# HOW WE CAN PROCESS COMMAND LINE ARGS USING  ARGPARSE

"""
    We are writing a program that takes 3 inputs,

        1) first number
        2) second number 
        3 operation("add", "substract", "multiply")

    it should return result of operation based on inputs 

"""

import argparse

if __name__ == "__main__":
    """
    there are two kinds of arguments that argparse 
        * positional arguments 
        * optional arguments

    """
    # we initilazes parser object
    parser = argparse.ArgumentParser()

    # add argument to your program when you run it using a command line
    # argument ("name of argument", help paramter)
    
    # # POSITIONAL ARGUMENTS : Should supply all the element as a mandatory 
    # parser.add_argument("number1", help = "first number")
    # parser.add_argument("number2", help = "second number")
    # parser.add_argument("operation", help = "operation", \
    #                     choices = ["add","substract","multiply"])  # when if you try another option for this raise error

    # OPTIONAL ARGUMENTS : If you want to skip any argument 
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation", \
                        choices=["add","subtract","multiply"])  # when if you try another option for this raise error

    # trying the pass arguments
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation )
    
    # whenever you pass an input using command line it always comes to program as a string 
    # so converts all inputs into integer 

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None

    if args.operation == "add":
        result = n1 + n2
    
    elif args.operation == "subtract":
        result = n1 - n2
 
    elif args.operation == "multiply":
        result = n1 * n2
    
    else:
        print("unsopperted operation")
        
    print("result :", result)


    
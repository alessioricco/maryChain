'''


'''

import maryChain.maryChain as mc


def assertion(s, expected):
    """
    Tests the given expression and compares its output to an expected result.
    
    Parameters
    ----------
    s : str
        A string representing the expression to evaluate.
    expected : various types
        The expected result of the evaluated expression. Type depends on the expression.

    Returns
    -------
    None
    """

    # Print the expression and the expected result
    print(f"\nTesting {s} => {expected}")

    # Evaluate the expression
    result = mc.eval(s)

    # Compare the result to the expected output and print the outcome
    if result == expected:
        print(f"PASS: {s} => {result}")
    else:
        print(f"FAIL: {s} => {result}, expected {expected}")



assertion("1",1)  # Integer literal
assertion("1+1",2)  # Integer addition
assertion("(1)",1)  # Integer literal with parentheses
assertion("(1+1)",2)  # Integer addition with parentheses
assertion("1+(1+1)",3)  # More complex integer addition with parentheses
assertion("1+3*2+1",8)  # Addition and multiplication
assertion("1|add(2)",3)  # Using the pipe operator with function call
assertion("'hello' | out","hello")
assertion("add(1)(2)",3)  # Function call with 2 arguments
assertion("add(1,1)",2)  # Function call with 2 arguments
assertion("add(1)(2)",3)  # Integer literal

assertion("add({1})(2)",3)  # Function call with 2 arguments
assertion("add({1},2)",3)  # Function call with 2 arguments
assertion("add({1})(2)",3)  # Integer literal

assertion("add(1)({2})",3)  # Function call with 2 arguments
assertion("add(1,{2})",3)  # Function call with 2 arguments
assertion("add(1)({2})",3)  # Integer literal

assertion("3*add(1,1)",6)  # Mixing arithmetic and function calls
assertion("add(1,add(1,1))",3)  # Nested function calls
assertion("{1}",1)  # Expression in braces
assertion('{"ciao"}','ciao')  # String literal in braces
assertion("{'ciao'}","ciao")  # Single quoted string literal
assertion("'ciao'","ciao")  # Single quoted string literal
assertion('"ciao"',"ciao")  # Double quoted string literal
assertion("lazy 1", 1)  # Lazy evaluation
assertion("lazy 1+1", 2)  # Lazy evaluation with arithmetic
assertion("out('hello')",'hello')  # Print function
assertion('out("hello")','hello')  # Print function with double quotes
assertion("1|out",1)  # Using the pipe operator with print function
assertion('"hello"|out',"hello")  # Printing a string with pipe operator
assertion('true',True)  # Boolean literal
assertion('false',False)  # Boolean literal
assertion('if true then true else false',True)  # If-then-else statement
assertion('if true then out("true") else out("false")',"true")  # If-then-else statement with print function
assertion('if true then false',False)  # If-then statement
assertion("if false then 1 else 2", 2)  # If-then-else statement with false condition
assertion("if true then if false then 1 else 2 else 3", 2)  # Nested if-then-else statements

assertion("1-1", 0)  # Integer subtraction
assertion("4/2", 2)  # Integer division
assertion("2*3+4", 10)  # Mixed multiplication and addition
assertion("2*(3+4)", 14)  # Multiplication and addition with parentheses
assertion("lazy (1+2)*2", 6)  # Lazy evaluation with more complex expression
assertion("lazy if true then 1 else 2", 1)  # Lazy evaluation with if-then-else statement
assertion("out('world')|out", "world")  # Print function piped into another print function

assertion(f"""exec('3')""",3)
assertion(f"""exec('add(1,add(2,3))')""",6)
assertion(f"""
          import math as m
          m.sqrt(9)
          """,3)

assertion("('hello' | out) | out ","hello")
assertion("'hello' | out | out ","hello")
assertion("'hello' | out | out | out","hello")

assertion("lambda (x) x*2 (3)", 6)  # Lambda function application
assertion("while false do 1", None)  # While statement with false condition

assertion("let x = 5 in x", 5)  # Let-in expression
assertion("let x = 5 in x*2", 10)  # Let-in expression with use of defined variable


assertion("let x = 5 in let y = 2 in x*y", 10)  # Nested let-in expressions
assertion("let x = 5 in let x = 2 in x", 2)  # Shadowing in let-in expressions
assertion("let double = lambda (x) x*2 in double(3)", 6)  # Let-in expression with lambda function

assertion("let x = 5 in while x > 0 do x = x - 1", 0)  # Loop decrementing a value until it reaches 0
assertion("let x = 1 in while x < 100 do x = x * 2", 128)  # Loop doubling a value until it reaches or exceeds a certain value



assertion("let x = 0 in let y = 5 in while y > 0 do x = x + (y = y - 1) | out", 10)
assertion("let x = 0 in let y = 5 in (while y > 0 do x = x + (y = y - 1)) | out", 10)
# assertion("let x = 1 in let y = 0 in while x <= 10 do y = y + x; x = x + 1 end end; y", 55)  # Loop calculating the sum of the first ten integers

# # Defining and calling a function
# assertion("let f = \\x -> x + 1 in f(5)", 6)

# # Function that calculates factorial
# assertion("""
# let factorial = \\n ->
#     if n = 0 then 1 else n * factorial(n - 1) end
# in factorial(5)
# """, 120)

# # Function that calculates the nth Fibonacci number
# assertion("""
# let fib = \\n ->
#     if n <= 1 then n else fib(n - 1) + fib(n - 2) end
# in fib(10)
# """, 55)

# # Function that checks if a number is even
# assertion("""
# let is_even = \\n ->
#     if n % 2 = 0 then true else false end
# in is_even(4)
# """, True)

# # Function that takes another function as an argument
# assertion("""
# let apply_twice = \\(f, x) -> f(f(x)) in
# let add_one = \\x -> x + 1 in
# apply_twice(add_one, 0)
# """, 2)

# assertion("add(1)",2)
# assertion("1 | out(_)",1)
# assertion("3|add(_,2)",5)
# assertion("3|add(2,_)",5)
# assertion("'hello'|out(_)",'hello')
# assertion("1|_",1)

# invalid expressions or edge cases
# assertion(f"""import library as core""",None)
# assertion(f"""import Workers.functions as core""",None)
# assertion("lambda (x) x*2", (mc.eval("lambda (x) x*2")))  # Lambda function definition
# assertion("let x = 5 in while x > 0 do let y = x in x = x - 1", 0)  # Similar loop, but uses an extra variable inside the loop
# assertion("let x = 0 in let y = 5 in while y > 0 do x = x + y; y = y - 1", 15)  # Loop calculating the sum of the first few integers
while True:
    """
    Main loop of the program.
    It repeatedly asks for user input and evaluates it using the 'mc' module.

    The loop can be exited by sending an EOF signal (e.g., Ctrl+D on Unix, Ctrl+Z+Enter on Windows).

    If the evaluation of an expression results in a ValueError, it's caught and its message is printed to the console.
    """
    try:
        # Prompt the user for input
        s = input('test > ')

        # Evaluate the user input
        result = mc.eval(s)

        # Print the evaluation result
        print(result)

    # Handle value errors that could occur during the evaluation
    except ValueError as e:
        # Print the error message to the console
        print(e)

    # Handle the EOF error that is raised when the user wants to exit the loop
    except EOFError:
        # Break the loop and end the program
        break

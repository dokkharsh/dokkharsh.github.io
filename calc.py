import math
import sys

problemtype = sys.argv[1]

if problemtype == "combination":
    n = int(sys.argv[2])
    r = int(sys.argv[3])
    if(n < r):
        print("Invalid values for n and r.\n")
        exit(1)

    ans = (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))
    print("The answer for this combination is:", ans , "\n")

if problemtype == "permutation":
    n = int(sys.argv[2])
    r = int(sys.argv[3])
    if(n < r):
        print("Invalid values for n and r.\n")
        exit(1)

    ans = (math.factorial(n))/math.factorial(n-r)
    print("The answer for this permutation is:", ans , "\n")

if problemtype == "truth-table":
    argument = sys.argv[2]
    #argument = "(not(p and q)) xor (p and q)"

    numDashes = 17 + 3 + 4 + len(argument) + 1
    for x in range(numDashes):
        print("-", end="")
    print("\n|   p   |   q   |   ", argument)
    for x in range(numDashes):
        print("-", end="")
    argument = argument.replace("xor", "!=")
    p = False
    q = False
    print("\n|   F   |   F   |   ", eval(argument))
    for x in range(numDashes):
        print("-", end="")
    p = True
    q = True
    print("\n|   T   |   T   |   ", eval(argument))
    for x in range(numDashes):
        print("-", end="")
    p = True
    q = False
    print("\n|   T   |   F   |   ", eval(argument))
    for x in range(numDashes):
        print("-", end="")
    p = False
    q = True
    print("\n|   F   |   T   |   ", eval(argument))
    for x in range(numDashes):
        print("-", end="")
    print("\n")

if problemtype == "bayes-prob":
    pta = int(sys.argv[2])
    pa = int(sys.argv[3])
    pt = int(sys.argv[4])
    ans = (pta*pa)/(pt)
    print("The answer for this bayes probabilty problem is:",ans,"\n")

if problemtype == "big-o":
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    d = int(sys.argv[4])

    if (a/(b ** d) < 1):
        print("O(n) = O(n **",d, ")\n")  
    elif (a/(b ** d) == 1):
        print("O(n) = O((n **",d,") * log(n))\n")
    elif (a/(b ** d) > 1):
        print("O(n) = O(n ** (log(",b,")(",a,")))\n")

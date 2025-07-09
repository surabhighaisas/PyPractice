"""
Use Dynamic programming for problems meeting below criteria
1. Overlapping subproblems i.e. some subproblems repeat
2. Optimized substructure: optimal solution to problem can be derived from optimal solutions to subproblems

Memoization: Store results of subproblems so that when subproblem repeats a single read from memory given answer

Fibonacci series is good example of problem where dynamic programming can be used. 
"""

# bottoms up approach without memoization & recursion
# loop gets invoked n-1 times hence O(n)
# Both best case and worst case are O(n)

ctr = 0
def fib_without_memo(n):
    global ctr
    fib_store = [0,1]
    for i in range(2,n+1):
        ctr+=1
        next_fib = fib_store[i-1] + fib_store[i-2]
        fib_store.append(next_fib)
    return fib_store[n]


# top down approach with memoization
# function gets invoked 2n-1 times, hence O(n)
# Best case O(1), worst case O(n)

fib_store = [0,1] + [None] * 48 # 50 member list
counter = 0 
def fib_with_memo(n):
    global counter
    counter += 1
    if fib_store[n] is not None:
        return fib_store[n]
    else:
        fib_store[n] = fib_with_memo(n-1) + fib_with_memo(n-2)
    return fib_store[n]

print(fib_without_memo(19))
print('ctr without memo=', ctr)
print(fib_with_memo(19))
print('ctr with memo=', counter)


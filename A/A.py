def solve():
    # Read input from file
    with open('input.txt', 'r') as file:
        lines = file.read().strip().split()
    
    # First line is t (number of test cases)
    t = int(lines[0])
    
    results = []
    idx = 1
    
    for _ in range(t):
        x = int(lines[idx])
        n = int(lines[idx + 1])
        idx += 2
        
        # Calculate total energy
        # When n is even, pairs of (x + (-x)) = 0, so total = 0
        # When n is odd, total = x (because last term is x and previous pairs cancel)
        if n % 2 == 0:
            total = 0
        else:
            total = x
        
        results.append(total)
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()

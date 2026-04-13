# ISRO Moon Rover Navigation System

# Plateau size 
maxX, maxY = map(int, input().split()) 

# Direction order 
directions = ['N', 'E', 'S', 'W'] 

while True: 
    try: 
        # Input initial position 
        x, y, dir = input().split() 
        x = int(x) 
        y = int(y) 

        # Input instructions 
        instructions = input().strip() 

        # Get direction index 
        d = directions.index(dir) 

        # Process instructions 
        for cmd in instructions: 
            if cmd == 'L': 
                d = (d - 1) % 4 

            elif cmd == 'R': 
                d = (d + 1) % 4 

            elif cmd == 'M': 
                if directions[d] == 'N' and y < maxY: 
                    y += 1 
                elif directions[d] == 'E' and x < maxX: 
                    x += 1 
                elif directions[d] == 'S' and y > 0: 
                    y -= 1 
                elif directions[d] == 'W' and x > 0: 
                    x -= 1 

        # Output final position 
        print(x, y, directions[d]) 

    except EOFError: 
        break

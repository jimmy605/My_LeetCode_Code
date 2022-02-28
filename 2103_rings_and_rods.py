def countPoints(rings: str) -> int:
    output = 0
    
    # Create a dict rods that stores the rods numbers as keys and a list of the colours as values
    rods = {i:[] for i in range(10)}
    
    # Iterate through the spliced str and add rod/colour to the rods dict
    for i in range(0, len(rings), 2):
        colour = rings[i]
        rod = int(rings[i + 1])
        
        # If colour not in rods key add it in
        if colour not in rods[rod]:
            rods[rod].append(colour)
    
    # Iterate though the dict and check the length of each list value
    for rod, colour in rods.items():
        # If == 3 add 1 to output
        if len(colour) == 3:
            output += 1
    
    return output


print(countPoints("B0B6G0R6R0R6G9"))

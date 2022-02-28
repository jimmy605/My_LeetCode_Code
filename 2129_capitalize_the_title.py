def capitalizeTitle(title: str) -> str:
    # # Create an output string
    # output = []
    
    # # Split the string into a list of strings and iterate through it
    # for word in title.split():
    #     # If len(string) < 3:
    #     if len(word) < 3:
    #         # Append to output in lowercase
    #         output.append(word.lower())
    #     # Else append to output as title case
    #     else:
    #         output.append(word.title())
    
    # # Return the output list as a joined string
    # return ' '.join(output)

    return ' '.join([word.lower() if len(word) < 3 else word.title()
                     for word in title.split()])


print(capitalizeTitle("capiTalIze tHe titLe"))
print(capitalizeTitle("First leTTeR of EACH Word"))
print(capitalizeTitle("i lOve leetcode"))
def mostWordsFound(sentences) -> int:
    # store the highest count
    highest_count = 0
    
    # Iterate through sentences and count the words of each index
    for sentence in sentences:
        # split the string into a list to count the words
        count = len(sentence.split())
        # If length is higher than highest_count update
        if count > highest_count:
            highest_count = count
    
    # Return highest_count
    return highest_count


print(mostWordsFound(["alice and bob love leetcode",
      "i think so too", "this is great thanks very much"]))
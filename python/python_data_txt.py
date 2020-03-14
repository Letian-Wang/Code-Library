
# link: https://www.computerhope.com/issues/ch001721.htm


# iterate on lines and string
    mylines = []                                # list
    with open ('log.txt', 'rt') as myfile:      # Open text. 'rt': read txt data
        for line in myfile:                     # For each line of text,
            mylines.append(line)                # append line to list.
        for element in mylines:                 # For each element in the list,
            print(element, end = '')            # end ='' means no newline character('\n')          

# strip
    line.rstrip('\n')  # \n or \r or \r\n       #  strips characters from the right side
    errors.append("Line "+ line.rstrip('\n'))

# format change
    errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))


# lowercase
    substr = "error".lower()
    if line.lower().find(substr) != -1:

# character in a line
    line[5]

# Get a specific-line data
    import linecache
    line_1 = linecache.getline(directory, 2)

# search a character in a line
    mylines[0].find("e")                        # search character "e" from the beginning, one character at a time.
    mylines[0].find("e", 10, 20)                # Search between 11th and 21th character   

                                                # When found, the search stops and returns the index number of location (index is zero-based)
                                                # When it reaches the end, ti returns -1
                                                # line, string all has find() 
    str = mylines[0]
    substr = "e"
    index = str.find(substr, index)   

    if line.lower().find(substr) != -1:       

    # example of find()
    # search all the occurance 
    # Locate and print all occurences of letter "e"
    index = 0                                       # current index 
    prev = 0                                        # previous index
    str = mylines[0]                                # (first element of mylines)
    substr = "e"                                    # substring to search for
    while index < len(str):                         # While index has not exceeded string length,
        index = str.find(substr, index)             # set index to first occurrence of "e"
        if index == -1:                             
            break                                   
        print(" " * (index - prev) + "e", end='')   # print location of this "e"
        prev = index + len(substr)                  # set previous to index + 1
        index += len(substr)                        # increment the index by the length of substr.                             
    print('\n' + str);                              # Print the original string under the e's       

# read comma-separated values from txt file and write to txt
    with open("test.txt", "r") as filestream:
        with open("answers.txt", "w") as filestreamtwo:     # replace "w" with "a+"
            for line in filestream:
                currentline = line.split(",")
                total = str(int(currentline[0]) + int(currentline[1]) + int(currentline [2])) + "\n"
                filestreamtwo.write(total)

# regular expression search : deal with complex problem
    # search a word according to the first and last character
    import re
    str = "Good morning, doctor."
    # pat = re.compile("error", re.IGNORECASE)                      # search word "error"
    # pat = re.compile(r"\bh\w*pe$", re.IGNORECASE)                 # search word begin with h and end with pe
    # pat = re.compile(r"(\+\d{1,2})?[\s.-]?\d{3}[\s.-]?\d{4}")     # search number
    pat = re.compile(r"\bd\w*r\b", re.IGNORECASE)                   # this is to search for word begin with d and end with r
                                                                    # r means raw text
    with open ('logfile.txt', 'rt') as myfile:    
        for line in myfile:     
            #if pat.search(str) != None:                                              
            if pat.search(line) != None:                            # Search for the pattern. If found,
            print(line)                           


# Split string into word             
    str = 'Hello! I am Robot. This is a Python example.'
    splits = str.split()
    for split in splits:
        print(split)
    print(splits[0])


                                    
                                    

                            


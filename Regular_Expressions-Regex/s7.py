import re
def substitutor():
    S = ["2020 Olympic games have @# been cancelled",
     "Dr Vikram Sarabhai was +%--the ISRO’s first chairman",
     "Dr Abdul            Kalam, the father      of India's missile programme"]
    for i in range(len(S)):
        S[i] = re.sub(r'[@#%+-]+', '', S[i])  # Remove special characters
        S[i] = re.sub(r'\s+', ' ', S[i])  # Replace multiple spaces with a single space
        S[i] = re.sub(r"\W", "",S[i])  # Replace non-word characters with a white space
         # replacing every digit character with a white space
        S[i] = re.sub(r"\d", " ", S[i])
        
        # replacing one or more white space with a single white space
        S[i] = re.sub(r"\s+", " ", S[i])
        
        # replacing alphabetic characters which have one or more 
        # white space before and after them with a white space
        S[i] = re.sub(r"\s+[a-z]\s+", " ", S[i], flags = re.I)
        
        # substituting one or more white space which is at 
        # beginning of the string with an empty string
        S[i] = re.sub(r"^\s+", "", S[i])
        
        # substituting one or more white space which is at
        # end of the string with an empty string
        S[i] = re.sub(r"\s+$", "", S[i])
        print(S[i])

substitutor()        
        
    



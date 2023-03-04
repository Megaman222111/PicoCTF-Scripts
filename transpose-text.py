# For the transposition trail challenge, text turns spaces indo dashes, and then splits the text into sections of 3. It then makes the 3rd letter the first letter, shifting the rest of the letters back.

text = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"
text = text.replace(" ", "-") # remove spaces from the text
sections = [text[i:i+3] for i in range(0, len(text), 3)] # split the text into sections of 3 characters
result = ""

for section in sections:
    if len(section) == 3:
        # transpose the 3rd letter to the 1st position
        transposed_section = section[2] + section[0] + section[1] 
        result += transposed_section
    else:
        result += section # append the remaining characters to the result

result = "".join([result[i:i+3] for i in range(0, len(result), 3)]) # join the sections with underscores
print(result)

def alphabet_position(letter):
    letter = letter.lower()
    return(ord(letter)-97)

def rotate_char(char, rot):

    uppercase = True

    if char.isalpha(): #rotate character if aplha
        if char.islower():
            uppercase = False
        
        position = alphabet_position(char)

        rotated = (position + rot) % 26

        #print("position ", + rotated)

        new_char = chr(rotated + 97)

        #print(position + rotation)
        
    else:
        return char #return unmodified character if non-alpha

    if uppercase:
        return new_char.upper()
    else:
        return new_char
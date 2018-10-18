from helpers import alphabet_position, rotate_char

def encrypt(text, rot):
    encrypted = ''

    for char in text:
        encrypted = encrypted + rotate_char(char, rot)
    
    return encrypted

def main():
    from sys import argv, exit

    if len(argv) == 2:
        if not argv[1].isdigit():
            print('Expected usage: caesar.py n')
            exit()
    else:
        print('Expected usage: caesar.py n')
        exit()

    #print('Command line input:', argv)
    user_string = input("Type a message:\n")
    #rotate = int(input('Rotate by: \n'))
    print(encrypt(user_string, int(argv[1])))

if __name__ == "__main__":
    main()
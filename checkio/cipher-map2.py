"""
Help Sofia write a decrypter for the passwords that Nikola will encrypt through the cipher map. 
A cipher grille is a 4×4 square of paper with four windows cut out. Placing the grille on a paper 
sheet of the same size, the encoder writes down the first four symbols of his password inside the 
windows (see fig. below). After that, the encoder turns the grille 90 degrees clockwise. 
The symbols written earlier become hidden under the grille and clean paper appears inside the 
windows. The encoder then writes down the next four symbols of the password in the windows and 
turns the grille 90 degrees again. Then, they write down the following four symbols and turns 
the grille once more. Lastly, they write down the final four symbols of the password. Without 
the same cipher grille, it is difficult to discern the password from the resulting square comprised 
of 16 symbols. Thus, the encoder can be confident that no hooligan will easily gain access to the locked door.

Write a module that enables the robots to easily recall their passwords through codes when they return home.

The cipher grille and the ciphered password are represented as an array (tuple) of strings.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string.

Example:

recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'icantforgetiddqd'
​
recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqrwsfzxqxzhczy'

How it is used: Here you can learn how to work with 2D arrays. You also get to learn about the ancient Grille Cipher, a technique of encoding messages which has been used for half a millenium. The earliest known description of the grille cipher comes from the Italian mathematician, Girolamo Cardano in 1550.

Precondition: len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)
"""

def recall_password(cipher_grille, ciphered_password):
    final_password = ''
    cipher_grille_list = change_zip_into_list(cipher_grille) 
    ciphered_password_list = [list(item) for item in ciphered_password]

    # rotate the cipher grilles, because python is pass-by-reference
    cipher_grille_rotated_0 = cipher_grille_list
    cipher_grille_rotated_90 = rotate_cipher_grille(cipher_grille_list)
    cipher_grille_rotated_180 = rotate_cipher_grille(cipher_grille_rotated_90)
    cipher_grille_rotated_270 = rotate_cipher_grille(cipher_grille_rotated_180)

    rotated_grille_list = (cipher_grille_rotated_0, cipher_grille_rotated_90, cipher_grille_rotated_180, cipher_grille_rotated_270)

    for rotated_item in rotated_grille_list:
        rotated_item_list = change_zip_into_list(rotated_item)
        final_password += read_from_ciphered_password(rotated_item_list, ciphered_password_list)

    return final_password
    
def change_zip_into_list(cipher_grille):
    cipher_grille_list = [list(grille_item) for grille_item in cipher_grille]
    
    return cipher_grille_list

def rotate_cipher_grille(cipher_grille_list):
    rotated_cipher_grille = list(zip(*cipher_grille_list[::-1]))
    
    return rotated_cipher_grille
    
def read_from_ciphered_password(cipher_grille_list, ciphered_password_list):
    temp_cipher_grille_list = cipher_grille_list
    temp_ciphered_password_list = ciphered_password_list
    password_addition = ''
    zipped = zip(temp_cipher_grille_list, temp_ciphered_password_list)
    for zip_block in zipped:
        for cell in zip_block[0]:
            if cell == 'X':
                password_addition += zip_block[1][zip_block[0].index(cell)]
                zip_block[0][zip_block[0].index(cell)] = 'N'

    return password_addition
                

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...', '..X.', 'X..X', '....'),
        ('itdf', 'gdce', 'aton', 'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

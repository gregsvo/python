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

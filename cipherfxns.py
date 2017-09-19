def monoalphabetic():
    #ask for user input for message and key
    plain = input('Enter the message: ')
    key = input('Enter the key: ')

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ''

    #cipher
    #loop through plaintext
    for x in range(0, len(plain)):
        if plain[x] not in alphabet:
            cipher += plain[x]
        else:
            #find index of plaintext in regular alphabet
            #add the same index of the key to cipher string
            cipher += key[alphabet.index(plain[x])]
    
    print('ciphertext:', cipher)

    decipher = ''
    #decipher
    #loop through ciphertext
    for x in range(0, len(cipher)):
        if cipher[x] not in alphabet:
            decipher += cipher[x]
        else:
            #find index of ciphertext in key
            #add the same index of the regular alphabet to decipher string
            decipher += alphabet[key.index(cipher[x])]

    print('plaintext:', decipher)



def caesar():
    #ask for user input for message and key
    plain = input('Enter the message: ')
    #key = number of places to shift down alphabet
    key = input('Enter the key (# of shifts): ')

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ''

    #cipher
    #loop through plaintext
    for x in range(0, len(plain)):
        if plain[x] not in alphabet:
            cipher += plain[x]
        else:
            #using general caesar algorithm C = E(k,p) = mod 26
            cipher += alphabet[(alphabet.index(plain[x])+ 3)%26]
    
    print('ciphertext:', cipher)

    decipher = ''
    #decipher
    #loop through ciphertext
    for x in range(0, len(cipher)):
        if cipher[x] not in alphabet:
            decipher += cipher[x]
        else:
            #using decryption algorithm p = D(k,C) = (C-k) mod 26
            decipher += alphabet[(alphabet.index(cipher[x])- 3)%26]

    print('plaintext:', decipher)


def playfair():
    #ask for user input for message and key
    plain = input('Enter the message: ')
    key = input('Enter the key: ')

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipherbet = ''

    #create the ciphertext alphabet from the key(word)
    #take out duplicates
    for x in range(0, len(key)):
        if(key[x] not in cipherbet and key[x] != 'i'):
            cipherbet += key[x]
    
    #add rest of the alphabet in alphabetic order
    for x in range(0, len(alphabet)):
        if(alphabet[x] not in cipherbet and alphabet[x] != 'i'):
            cipherbet += alphabet[x]

    #separate repetitive letters with a filler letter x
    for x in range(0, len(plain)):
        if x !=0 and plain[x] == plain [x-1]:
            plain = plain[:x] + 'x' + plain[x:] 

    cipher = ''

    #cipher
    #loop through plaintext
    #plaintext is encrypted two letters at a time
    for x in range(0, len(plain),2):
        #if last letter (single letter), remains same
        if x == len(plain)-1:
            cipher += plain[x]
        elif plain[x] not in cipherbet:
            cipher += plain[x]
        elif cipherbet.index(plain[x])//5 == cipherbet.index(plain[x+1])//5:
            #if in the same row, replaced by the letter to the right
            #if last letter in row, replace with first (couldn't find a general algorithm, so used if cases)
            if cipherbet.index(plain[x])%5 == 4:
                cipher += cipherbet[cipherbet.index(plain[x])-4]
            else:
                cipher += cipherbet[cipherbet.index(plain[x])+1]
            if cipherbet.index(plain[x+1])%5 == 4:
                cipher += cipherbet[cipherbet.index(plain[x+1])-4]
            else:
                cipher += cipherbet[cipherbet.index(plain[x+1])+1]
        elif cipherbet.index(plain[x])%5 == cipherbet.index(plain[x+1])%5:
            #if in the same column, replaced by letter beneath
            cipher += cipherbet[(cipherbet.index(plain[x])+5)%25] + cipherbet[(cipherbet.index(plain[x+1])+5)%25]
        else:
            #otherwise, replaced with letter in its row and column of the other letter
            cipher += cipherbet[cipherbet.index(plain[x]) + (cipherbet.index(plain[x+1])%5)-(cipherbet.index(plain[x])%5)]
            cipher += cipherbet[cipherbet.index(plain[x+1]) + (cipherbet.index(plain[x])%5)-(cipherbet.index(plain[x+1])%5)]

    print('ciphertext:', cipher)

    decipher = ''

    #decipher
    #loop through ciphertext
    #ciphertext is decrypted two letters at a time
    for x in range(0, len(cipher),2):
        #if last letter (single letter), remains same
        if x == len(cipher)-1:
            decipher += cipher[x]
        elif cipher[x] not in cipherbet:
            decipher += cipher[x]            
        elif cipherbet.index(cipher[x])//5 == cipherbet.index(cipher[x+1])//5:
            #if in the same row, replaced by the letter to the left
            #if first letter in row, replace with last (couldn't find a general algorithm, so used if cases)
            if cipherbet.index(cipher[x])%5 == 0:
                decipher += cipherbet[cipherbet.index(cipher[x])+4]
            else:
                decipher += cipherbet[cipherbet.index(cipher[x])-1]
            if cipherbet.index(cipher[x+1])%5 == 0:
                decipher += cipherbet[cipherbet.index(cipher[x+1])+4]
            else:
                decipher += cipherbet[cipherbet.index(cipher[x+1])-1]
        elif cipherbet.index(cipher[x])%5 == cipherbet.index(cipher[x+1])%5:
            #if in the same column, replaced by letter above
            decipher += cipherbet[(cipherbet.index(cipher[x])-5)%25] + cipherbet[(cipherbet.index(cipher[x+1])-5)%25]
        else:
            #otherwise, replaced with letter in its row and column of the other letter
            decipher += cipherbet[cipherbet.index(cipher[x]) + (cipherbet.index(cipher[x+1])%5)-(cipherbet.index(cipher[x])%5)]
            decipher += cipherbet[cipherbet.index(cipher[x+1]) + (cipherbet.index(cipher[x])%5)-(cipherbet.index(cipher[x+1])%5)]

    #remove x's from plaintext
    for x in range(1, len(decipher)-1):
        if decipher[x] == 'x' and decipher[x-1] == decipher[x+1]:
            decipher = decipher[:x] + decipher[x+1:]

    print('plaintext:', decipher)


def vigenere():
    #ask for user input for message and key
    plain = input('Enter the message: ')
    key = input('Enter the key: ')

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ''

    #cipher
    #loop through plaintext
    for x in range(0, len(plain)):
        if plain[x] not in alphabet:
            cipher += plain[x]
        else:
            #find index of plaintext and key in regular alphabet
            #sum indices 
            cipher += alphabet[(alphabet.index(plain[x])+alphabet.index(key[x]))%26]
    
    print('ciphertext:', cipher)

    decipher = ''
    #decipher
    #loop through ciphertext
    for x in range(0, len(cipher)):
        if cipher[x] not in alphabet:
            decipher += cipher[x]
        else:
            #find index of ciphertext and key in regular alphabet
            #subtract key index from cipher 
            decipher += alphabet[(alphabet.index(cipher[x])-alphabet.index(key[x]))%26]

    print('plaintext:', decipher)

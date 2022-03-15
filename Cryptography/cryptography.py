import sys
import string
def welcome():

    #Printing the user guide
    
    print('Welcome to my cryptographic page! \n')
    print('Select 1 to encrypt \n')
    print('Select 2 to decrypt \n')
    print('Select 0 to quit \n')
    prompt1 = input('Select here: \n')

    #catching some errors that could result from user input

    try:
        if int(prompt1) == 1:
            encrypt()
        elif int(prompt1) == 2:
            decrypt()
        elif int(prompt1) == 0:
            sys.exit('Bye and Thanks')
    except TypeError:
        print('Please Select between 1, 2 or 0 \n')
        welcome()
    except ValueError:
        print('Invalid input. Please follow the guide below to make your selection \n')
        welcome()
    except:
        print('You made a wrong entry! Please follow the guide and retry \n')
        welcome()

#function to encrypt string

def encrypt():
    global ascii_string, encrypt_string, encrypt_key, container
    ascii_string = 'abcdefghijklmnopqrstuvwxyz'
    encrypt_string = input('Type word to encrypt:  \n')

    #below blocks try to catch errors due user input

    if encrypt_string.isspace():
        print('Encryption string must not be empty! Please try again')
        encrypt()
        
    encrypt_key = input('Type encryption key between 1-10 here: \n')

    if int(encrypt_key)<1 or int(encrypt_key)>10:
        print('Value out of range, please retry')
        encrypt()


    if encrypt_key.isspace() or encrypt_key == '':
        encrypt_key = 0

   
    #Below code blocks show the encryption algorithm

    encrypt_key = int(encrypt_key)
    encrypt_container = ''
    for i in encrypt_string:
        if (not i.islower() or not i.isalpha()) or (not i.islower() and not i.isalpha()) or i == '':
            encrypt_container += i
        else:
            found_value = ascii_string.find(i)
            new_arr_index = (found_value+encrypt_key)%(len(ascii_string)-1)
            encrypt_container = encrypt_container+ascii_string[new_arr_index]

    #below blocks prrints the result of user operation and prompt for further actions

    print(f'The encoded text is: {encrypt_container} \n')
    print('Select 3 to have another go \n')
    print('Select 4 to decrypt \n')
    print('Select 5 to quit \n')

    option = int(input('Select here: '))
    if option == 3:
        welcome()
    elif option == 4:
        decrypt()
    elif option == 5:
        sys.exit('Thank you')


#Decryption function

def decrypt():
    ascii_string = 'abcdefghijklmnopqrstuvwxyz' 
    global decrypt_string, decryption_container, find_decryption_value, new_decr_arr_index
    decrypt_string = input('Type word to decrypt: \n')

    #Below blocks try to catch possible errors from user

    if decrypt_string.isspace():
        print('Decryption string must not be empty! Please try again')
        decrypt()
    global decrypt_key
    decrypt_key = input('Type decryption key between 1-10 here: \n')

    if int(decrypt_key)<1 or int(decrypt_key)>10:
        print('Value out of range, please retry')
        decrypt()


    if decrypt_key.isspace() or decrypt_key == '':
        decrypt_key = 0

    #Decryption algorthm is writtem below

    decrypt_key = int(decrypt_key)
    decryption_container = ''
    for i in decrypt_string:
        if (not i.islower() or not i.isalpha()) or (not i.islower() and not i.isalpha()) or i == '':
            decryption_container += i
        else:
            found_decryption_value = ascii_string.find(i)
            new_decr_arr_index = (found_decryption_value - decrypt_key)%(len(ascii_string)-1)
            decryption_container = decryption_container+ascii_string[new_decr_arr_index]

    #code blocks below print result and prompts for further action from the user

    print(f'The decoded text is: {decryption_container} \n')
    print('Select 3 to have another go \n')
    print('Select 4 to encrypt \n')
    print('Select 5 to quit \n')

    option = int(input('Select here: '))
    if option == 3:
        decrypt()
    elif option == 4:
        encrypt()
    elif option == 5:
        sys.exit('Thank you')

welcome()

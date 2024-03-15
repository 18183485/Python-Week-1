'''This program hacks messages encrypted with the Ceasar cipher by doing
a brute force attack against every possible key.
'''

print('Ceasar Cipher Hacker')
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    #Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key #Decrypt the number

            #Handle the wrap around if num is less than 0:
            if num < 0:
                num = num +len(SYMBOLS)

            #Add decrypted number's symbol to translated
            translated = translated + SYMBOLS[num]

        else:
            #Just add the symbol without decrypting:
            translated = translated + symbol
    print('key #{}: {}'.format(key, translated))
    
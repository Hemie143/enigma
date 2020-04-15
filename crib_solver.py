import crypto-enigma
import crib_cipher


cpercent = 0
errora = 0

def permute(a, b, c, cyph, crib, ct):
    # TODO: awfully translated from C. Couldn't be worse
    global cpercent
    print('[I]  {}% Completed - Checking wheels {}{}{}'.format(cpercent, a, b, c))
    crib_cipher.test(a, b, c, cyph, crib, ct, errora)
    cpercent += 1.66
    print('[I]  {}% Completed - Checking wheels {}{}{}'.format(cpercent, a, c, b))
    crib_cipher.test(a, c, b, cyph, crib, ct, errora)
    cpercent += 1.66
    print('[I]  {}% Completed - Checking wheels {}{}{}'.format(cpercent, b, a, c))
    crib_cipher.test(b, a, c, cyph, crib, ct, errora)
    cpercent += 1.66
    print('[I]  {}% Completed - Checking wheels {}{}{}'.format(cpercent, b, c, a))
    crib_cipher.test(b, c, a, cyph, crib, ct, errora)
    cpercent += 1.66
    print('[I]  {}% Completed - Checking wheels {}{}{}'.format(cpercent, c, a, b))
    crib_cipher.test(c, a, b, cyph, crib, ct, errora)
    cpercent += 1.66
    print('[I]  {}% Completed - Checking wheels {}{}{}'.format(cpercent, c, b, a))
    crib_cipher.test(c, b, a, cyph, crib, ct, errora)
    cpercent += 1.66
    return


def bombe(cyph, crib):
    ct = 0
    permute(1, 2, 3, cyph, crib, ct)
    permute(1, 2, 4, cyph, crib, ct)
    permute(1, 2, 5, cyph, crib, ct)
    permute(1, 3, 4, cyph, crib, ct)
    permute(1, 3, 5, cyph, crib, ct)
    permute(1, 4, 5, cyph, crib, ct)
    permute(2, 3, 4, cyph, crib, ct)
    permute(2, 3, 5, cyph, crib, ct)
    permute(2, 4, 5, cyph, crib, ct)
    permute(3, 4, 5, cyph, crib, ct)

    print('[I] 100% Completed - Found {} possible solutions.'.format(ct))
    return


if __name__ == '__main__':
    inEncryptedText = input('Encrypted text: ')
    inCribTxt = input('Crib text: ')
    print('[I] This process can take a very long time.')

    inEncryptedText = inEncryptedText.upper()
    inCribTxt = inCribTxt.upper()
    bombe(inEncryptedText, inCribTxt)
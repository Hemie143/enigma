from enigma.machine import EnigmaMachine
import logging

rotors = ["I II III", "I II IV", "I II V", "I III II",
          "I III IV", "I III V", "I IV II", "I IV III",
          "I IV V", "I V II", "I V III", "I V IV",
          "II I III", "II I IV", "II I V", "II III I",
          "II III IV", "II III V", "II IV I", "II IV III",
          "II IV V", "II V I", "II V III", "II V IV",
          "III I II", "III I IV", "III I V", "III II I",
          "III II IV", "III II V", "III IV I", "III IV II",
          "III IV V", "IV I II", "IV I III", "IV I V",
          "IV II I", "IV II III", "IV I V", "IV II I",
          "IV II III", "IV II V", "IV III I", "IV III II",
          "IV III V", "IV V I", "IV V II", "IV V III",
          "V I II", "V I III", "V I IV", "V II I",
          "V II III", "V II IV", "V III I", "V III II",
          "V III IV", "V IV I", "V IV II", "V IV III"]

ring = ["1",  "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9", "10",
		"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
		"21", "22", "23", "24", "25", "26"]

logging.basicConfig(filename='bruteforce.log', level=logging.DEBUG)

def find_rotor_start(rotor_choice, ring_choice, ciphertext, cribtext):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    machine = EnigmaMachine.from_key_sheet(rotors=rotor_choice,
                                           reflector='B',
                                           ring_settings=ring_choice,
                                           plugboard_settings='BU GE VL')

    for rotor1 in alphabet:
        for rotor2 in alphabet:
            for rotor3 in alphabet:
                start_pos = rotor1 + rotor2 + rotor3
                machine.set_display(start_pos)
                plaintext = machine.process_text(ciphertext)
                # print(plaintext)
                if cribtext in plaintext:
                    print('Valid settings found!')
                    logging.info('Valid settings found!')
                    logging.info(plaintext)
                    return rotor_choice, ring_choice, start_pos
    return rotor_choice, ring_choice, "Cannot find settings"


if __name__ == '__main__':
    ciphertext = 'YTTUAGIMHXPWZVBIDZTCHFMMQJWVPNGBXVHAVIKRCGUPRCENDBDFOVLBSDDVRPBRTSOVGDEXHTOVKCARMZQQQNGKUUWWPDSEFXEMSWEOOOADRTUDPDDUDQMZHSPSYKSYUPAKESUWIMAIMENTOVWTZSCRAWLJLEJWFLFFZBFABBWVTVLXJIRVIYTVGOAMPLFPHZOVLREXZVKLQRKSPNPLHITMAJLXAGWFFQESMSVPAVYIUSDRHTGMOBQHLVPMMSBLZACEGGGTMUEPGOLYIPMYOFROGZEYIXHFMMPYRBLLJDHRGKGZZQKZDUJCAKQYAEYGXFOGSGTRMBAMZTPNGLPLMRZTTYLBACOKNCQTHNKTYOJBHCRSJFIYBQRWCXHBAPIGRTHVGUIIKQGNMWYTHNWKYEMBDRVWFHKFPHOIUASGKHYVEENFHXHJOIXHIXZDLDLXQMGFXUAEGKHKPGBEQGQCKXQOZCDSYNJECJMQCRTUDSTXIREXMSLBSE'
    # ciphertext = 'IFPWKYTTUAGIMHXPWZVBIDZTCHFMMQJWVPNGBXVHAVIKRCGUPRCENDBDFOVLBSDDVRPBRTSOVGDEXHTOVKCARMZQQQNGKUUWWPDSEFXEMSWEOOOADRTUDPDDUDQMZHSPSYKSYUPAKESUWIMAIMENTOVWTZSCRAWLJLEJWFLFFZBFABBWVTVLXJIRVIYTVGOAMPLFPHZOVLREXZVKLQRKSPNPLHITMAJLXAGWFFQESMSVPAVYIUSDRHTGMOBQHLVPMMSBLZACEGGGTMUEPGOLYIPMYOFROGZEYIXHFMMPYRBLLJDHRGKGZZQKZDUJCAKQYAEYGXFOGSGTRMBAMZTPNGLPLMRZTTYLBACOKNCQTHNKTYOJBHCRSJFIYBQRWCXHBAPIGRTHVGUIIKQGNMWYTHNWKYEMBDRVWFHKFPHOIUASGKHYVEENFHXHJOIXHIXZDLDLXQMGFXUAEGKHKPGBEQGQCKXQOZCDSYNJECJMQCRTUDSTXIREXMSLBSE'
    cribtext = 'LAISSE'

    print(("Brute force crypt attack on Enigma message %s using crib %s" % (ciphertext, cribtext)))


    # try all rotor settings (choosing three from five)
    found = False
    i = 1
    ring0 = 1
    ring1 = 2
    ring2 = 1
    # Awful code
    # TODO: use range
    while ring0 <= len(ring) and not found:
        while ring1 <= len(ring) and not found:
            while ring2 <= len(ring) and not found:

                ring_choice = "{} {} {}".format(ring0, ring1, ring2)
                rot = 0

                while rot < len(rotors) and not found:
                    rotor_choice = rotors[rot]
                    print('Trying rotor {} with ring {}'.format(rotor_choice, ring_choice))
                    logging.info('Trying rotor {} with ring {}'.format(rotor_choice, ring_choice))
                    rotor_choice, ring_choice, start_pos = find_rotor_start(rotor_choice, ring_choice, ciphertext, cribtext)
                    if start_pos != "Cannot find settings":
                        print('{} - {} - {}'.format(rotor_choice, ring_choice, start_pos))
                        logging.info('{} - {} - {}'.format(rotor_choice, ring_choice, start_pos))

                    rot += 1
                ring2 += 1
            ring2 = 1
            ring1 += 1
        ring1 = 1
        ring0 += 1

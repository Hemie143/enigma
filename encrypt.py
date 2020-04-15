from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(rotors='IV I V',
                                       reflector='B',
                                       ring_settings='20 5 10',
                                       plugboard_settings='SX KU QP VN JG TC LA WM OB ZF')

machine.set_display('FNZ')
msg_key = machine.process_text('BFR')
print(msg_key)

machine.set_display('BFR')
plaintext = 'RASPBERRYPI'
ciphertext = machine.process_text(plaintext)
print(ciphertext)


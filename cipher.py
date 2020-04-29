#!/usr/bin/env python3
import argparse
import subprocess
from pprint import pprint
import time
from alive_progress import alive_bar, config_handler


class Cipher:

    def arguments(self):
        cipher_parse = argparse.ArgumentParser(description='Encrypt and Decrypt words', add_help=True)

        cipher_parse.add_argument('-w', '--word', dest='word', action='store',
                                  help='word to encrypt', required=True)
        cipher_parse.add_argument('-k', '--key', dest='key', action='store',
                                  help='key', required=True)
        group = cipher_parse.add_mutually_exclusive_group(required=True)
        group.add_argument('-e', '--encrypt', dest='type', action='store_true', help='-e to encrypt')
        group.add_argument('-d', '--decrypt', dest='type', action='store_false', help='-d to decrypt')

        args = cipher_parse.parse_args()
        word = str(args.word).lower()
        key = str(args.key).lower()
        # true, Encrypt
        # False, Decrypt
        enter_type = args.type

        if enter_type:
            text_intro = "         +-+-+-+-+-+ +-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+ \n" \
                         +"         |E|n|c|r|y|p|t| |W|o|r|d| |by| |B|4|r|t|\n" \
                         + "        +-+-+-+-+-+ +-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+\n"
            subprocess.run(['echo', text_intro])
            subprocess.run(['echo', 'Processing... \n'])
            final_text = self.cifrar(word, key)
            all_values = final_text['all_values']
            encrypted_list = (" ".join(final_text['encrypted_list']))
            subprocess.run(['echo', "\n Printing values... \n"])
            pprint(all_values)
            subprocess.run(['echo', "\n Original word : " + word.upper()])
            subprocess.run(['echo', "\n Encrypted Word : " + encrypted_list.upper()])
            subprocess.run(['echo', '\n Completed....! \n'])

        else:
            subprocess.run(['echo', 'Decrypt....! \n'])

    def cifrar(self, text_to_enc, key):

        generated_key = self.generate_text_from_pswd(text_to_enc, key)
        group_list = []
        encrypted_list = []
        all_values_group = []
        if len(text_to_enc) == len(generated_key):
            with alive_bar(1, bar='blocks') as bar:
                for i, c in enumerate(text_to_enc):
                    num1 = self.numberxposition(c)
                    num2 = self.numberxposition(generated_key[i])
                    all_values_group.append(str(num1) + ' , ' + str(num2) + ' => ' + str(num1 + num2))
                    sum_numbers = num1 + num2
                    encrypted_list.append(self.positionxnumber(self.encrypted_char(sum_numbers)))
                    group_list.append([num1, num2])
                    bar()
                return {
                    'all_values': all_values_group,
                    'encrypted_list': encrypted_list
                }

        else:
            return 'error'

    def generate_text_from_pswd(self, text_to_enc, password):
        key_text = ''
        count = 0

        for i in range(len(text_to_enc)):
            key_text += password[count]
            count += 1

            if count == len(password):
                count = 0

        return key_text

    def numberxposition(self, letra):
        char = list('abcdefghijklmnopqrstuvwxyzñ0123456789')
        return char.index(letra)

    def positionxnumber(self, number):
        char = list('abcdefghijklmnopqrstuvwxyzñ0123456789')
        return char[number]

    def encrypted_char(self, sum):
        division = divmod(sum, 37)
        if division[0] == 0:
            return sum
        else:
            return division[1]


if __name__ == '__main__':
    Cipher().arguments()

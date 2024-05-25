import awafier_maps
import argparse

def binary_to_awawa(binary: int):
    stringrep = "{0:08b}".format(binary)
    stringrep = stringrep.replace("0", "awa")
    stringrep = stringrep.replace("1", "wa")
    stringrep = stringrep.replace("aa", "a a")
    return stringrep


def awawafy_character(character : chr):
    if character not in awafier_maps.AWASCII_MAP.keys():
        if character not in awafier_maps.SUBSTITUTION_MAP.keys():
            print("Character not supported by AWASCII")
            exit()
        else:
            character = awafier_maps.SUBSTITUTION_MAP[character]

    return binary_to_awawa(awafier_maps.AWASCII_MAP[character])


def awawafy(text: str):
    print("Awawawafying: ", text)
    start_flag = "awa"
    blow_flag = "awa awawa awawa"
    text_terms = []
    print_flag = "awa awa awa awawa"

    for character in text:
        text_terms.append(awawafy_character(character))
        text_terms.append(blow_flag)

    text_section = " ".join(text_terms[::-1])

    result = " ".join([start_flag, text_section] +  [print_flag]*len(text))
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='AwaScript name converter')
    parser.add_argument("input_text")

    args = parser.parse_args()
    awawafy(args.input_text)
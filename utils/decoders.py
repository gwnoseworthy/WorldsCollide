## from https://www.ff6hacking.com/wiki/doku.php?id=ff3:ff3us:doc:asm:fmt:actor_startup
import binascii
from collections import namedtuple
## TODO pull this from data.characters, but need to resolve circular import.
CHARACTER_LIST = (
    'TERRA', 'LOCKE', 'CYAN', 'SHADOW', 'EDGAR', 'SABIN', 'CELES',
    'STRAGO', 'RELM', 'SETZER', 'MOG', 'GAU', 'GOGO', 'UMARO', 'BANON',
    'LEO')



def get_characters(char_hex):
    """
    Unpacks 16bit character Hex with last 2 bits saved for BANNON/LEO
    """

    return  [name for bit, name in zip(format(char_hex, '16b'), CHARACTER_LIST ) if bit == "1"]

if __name__ == "__main__":
    print(get_characters(0x832f))
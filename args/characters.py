from utils.decoders import get_characters


def name():
    return "Characters"

def parse(parser):
    ## NOTE: Used to parse hex input values
    def auto_int(x):
        return int(x, 0)
    characters = parser.add_argument_group("Characters")

    characters.add_argument("-sal", "--start-average-level", action = "store_true",
                            help = "Recruited characters start at the average character level")
    characters.add_argument("-stl", "--start-level", default = 3, type = int, choices = range(3, 100), metavar = "COUNT",
                            help = "Start game at level %(metavar)s.")
    characters.add_argument("-sn", "--start-naked", action = "store_true",
                            help = "Recruited characters start with no equipment")
    characters.add_argument("-eu", "--equipable-umaro", action = "store_true",
                            help = "Umaro can access equipment menu")
    characters.add_argument("-csrp", "--character-stat-random-percent", default = [100, 100], type = int,
                            nargs = 2, metavar = ("MIN", "MAX"), choices = range(201),
                            help = "Each character stat set to random percent of original within given range ")

    characters.add_argument("-clist", '--character-list', type=auto_int)

def process(args):
    args._process_min_max("character_stat_random_percent")

def flags(args):
    flags = ""

    if args.start_average_level:
        flags += " -sal"
    if args.start_level != 3:
        flags += f" -stl {args.start_level}"
    if args.start_naked:
        flags += " -sn"
    if args.equipable_umaro:
        flags += " -eu"
    if args.character_stat_random_percent_min != 100 or args.character_stat_random_percent_max != 100:
        flags += f" -csrp {args.character_stat_random_percent_min} {args.character_stat_random_percent_max}"
    if args.character_list:
        flags +=f" -clist {' '.join(get_characters(args.character_list))}"
    return flags

def options(args):
    character_stats = f"{args.character_stat_random_percent_min}-{args.character_stat_random_percent_max}%"

    return [
        ("Start Average Level", args.start_average_level),
        ("Start Level", args.start_level),
        ("Start Naked", args.start_naked),
        ("Equipable Umaro", args.equipable_umaro),
        ("Character Stats", character_stats),
        ("Character List",  "".join(c[:2].title() for c in get_characters(args.character_list)))
    ]

def menu(args):
    entries = options(args)
    for index, entry in enumerate(entries):
        key, value = entry
        if key == "Character Stats":
            entries[index] = ("Stats", entry[1])
    return (name(), entries)

def log(args):
    from log import format_option
    log = [name()]

    entries = options(args)
    for entry in entries:
        log.append(format_option(*entry))

    return log

import sys

def change_tabs(fileObject, tabsToSpaces=4):
    line: str
    for line in fileObject:
        line = line.replace('\t', ' '*tabsToSpaces)
        yield line

def get_input(args):
    if len(args) == 0:
        sys.exit("Usage: python ./fixindent.py <input_file> OPTIONAL: <output_file> (or piping)")

    try:
        return open(args[0], 'r')
    except FileNotFoundError:
        sys.exit("File not found")

def write_out(object, args):
    if len(args) < 2:
        for line in change_tabs()



if __name__ == "__main__":
    args = sys.argv[1:]
    with get_input(args) as inObj:
        change_tabs(inObj)

    write_out()
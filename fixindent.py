if __name__ == "__main__":
    with open('HW1/hw1.py', 'r') as fin, open('space.hw1.py', 'a') as out:
        lines = fin.readlines()
        for line in lines:
            line = line.replace('\t', '    ')

            out.write(line)
### This is a script to strip all non-human readable characters from a given file

import re

def main():
    with open(input('Please input the filename you would like to strip: '), 'r') as file:
        for line in file:
            line = line.replace("NameProperty", "")
            print(re.sub(r'\W+', '', line))
main()
        

#!/usr/bin/env python3

# Generate all possible permutations with given strings list

import argparse
import itertools
import os
import sys


def build_parser():
    """Add parser arguments and return an instance of ArgumentParser."""
    parser = argparse.ArgumentParser(description=("Generate all possible "
                                                  "permutations with given "
                                                  "strings list"),
                                     formatter_class=argparse.
                                     ArgumentDefaultsHelpFormatter)
    parser.add_argument("separator",
                        metavar="SEPARATOR",
                        type=str,
                        help=("Char to use as separator (e.g.: \" \" - \
                               whitespace)"))

    parser.add_argument("input_file",
                        metavar="INPUT_FILE",
                        type=str,
                        help="File with strings to permutate")
    parser.add_argument("output_file",
                        metavar="OUTPUT_FILE",
                        type=str,
                        help="Where to write the permutated strings")
    return parser


def validate_files(input_file, output_file):
    """Check if input/output files are valid."""
    if not os.path.isfile(input_file):
        print("[-] The file %s does not exist or is not a file!" % input_file)
        sys.exit(1)
    if os.path.isfile(output_file):
        answer = input("[!] The file %s already exists! Overwrite? [y/N] "
                           % output_file)
        if answer.lower() == "y":
            os.remove(output_file)
        else:
            print("[!] Aborted.")
            sys.exit(0)


def write_output(output_file, write_this):
    """Write permutated strings to the output file."""
    try:
        output_file = open(output_file, 'a')
        output_file.writelines(write_this + '\n')
        output_file.close()
    except IOError:
        print("[-] Error writing to file %s" % output_file)
        print("[!] Exiting ...")
        sys.exit(1)


if __name__ == "__main__":
    args = build_parser().parse_args()
    validate_files(args.input_file, args.output_file)

    print("[!] Starting permutations ...")
    written_strings = 0
    with open(args.input_file) as file_words_permutate:
        words_permutate = file_words_permutate.read().splitlines()

        for how_many in range(1, len(words_permutate) + 1):
            this_list = list(itertools.permutations(words_permutate, how_many))

            for permutation in this_list:
                write_output(args.output_file,
                             args.separator.join(list(permutation)))
                written_strings += 1

    print("[!] Strings read: " + str(len(words_permutate)))
    print("[!] Strings written: " + str(written_strings))
    print("[!] All done! exiting ...")
    sys.exit(0)

class ManglingParameters:
    def __init__(self):
        self.num_file = None
        self.sym_file = None
        self.cus_file = None
        self.mutation_mode = None
        self.from_year = None
        self.to_year = None
        self.short_year = None
        self.suffix_pos_swap = False
        self.prefix_pos_swap = False


class Mangler(object):
    def __init__(self, mangling_parameters):
        self.parameters = mangling_parameters

    def mutate(self, some_string):
        mangled = [some_string]

        if (self.parameters.mutation_mode == "suffix-mode" or
                self.parameters.mutation_mode == "dual-mode"):

            for symbol in self.parameters.sym_file:
                # "example!"
                mangled.append(some_string + symbol)

            for year in range(self.parameters.from_year,
                               self.parameters.to_year + 1):
                # "example2018"
                mangled.append(some_string + str(year))
                if (self.parameters.short_year):
                    # "example18"
                    mangled.append(some_string + str(year)[+2:])
                for symbol in self.parameters.sym_file:
                    # "example2018!"
                    mangled.append(some_string + str(year) + symbol)
                    if (self.parameters.short_year):
                        # "example18!"
                        mangled.append(some_string + str(year)[+2:] + symbol)
                    if self.parameters.suffix_pos_swap:
                        # "example!2018"
                        mangled.append(some_string + symbol + str(year))
                        if (self.parameters.short_year):
                            # "example!18"
                            mangled.append(some_string + symbol +
                                           str(year)[+2:])

            for number in self.parameters.num_file:
                # "example123"
                mangled.append(some_string + number)
                for symbol in self.parameters.sym_file:
                    # "example123!"
                    mangled.append(some_string + number + symbol)
                    if self.parameters.suffix_pos_swap:
                        # "example!123"
                        mangled.append(some_string + symbol + number)

            if (self.parameters.cus_file):
                for custom in self.parameters.cus_file:
                    # "examplecustom"
                    mangled.append(some_string + custom)
                    for symbol in self.parameters.sym_file:
                        # "examplecustom!"
                        mangled.append(some_string + custom + symbol)
                        if self.parameters.suffix_pos_swap:
                            # "example!custom"
                            mangled.append(some_string + symbol + custom)

        if (self.parameters.mutation_mode == "prefix-mode" or
                self.parameters.mutation_mode == "dual-mode"):

            for symbol in self.parameters.sym_file:
                # "!example"
                mangled.append(symbol + some_string)

            for year in range(self.parameters.from_year,
                               self.parameters.to_year + 1):
                # "2018example"
                mangled.append(str(year) + some_string)
                if (self.parameters.short_year):
                    # "18example"
                    mangled.append(str(year)[+2:] + some_string)
                for symbol in self.parameters.sym_file:
                    # "!2018example"
                    mangled.append(symbol + str(year) + some_string)
                    if (self.parameters.short_year):
                        # "!18example"
                        mangled.append(symbol + str(year)[+2:] + some_string)
                    if self.parameters.prefix_pos_swap:
                        # "2018!example"
                        mangled.append(str(year) + symbol + some_string)
                        if (self.parameters.short_year):
                            # "18!example"
                            mangled.append(str(year)[+2:] + symbol +
                                           some_string)

            for number in self.parameters.num_file:
                # "123example"
                mangled.append(number + some_string)
                for symbol in self.parameters.sym_file:
                    # "!123example"
                    mangled.append(symbol + number + some_string)
                    if self.parameters.prefix_pos_swap:
                        # "123!example"
                        mangled.append(number + symbol + some_string)

            if (self.parameters.cus_file):
                for custom in self.parameters.cus_file:
                    # "customexample"
                    mangled.append(custom + some_string)
                    for symbol in self.parameters.sym_file:
                        # "!customexample"
                        mangled.append(symbol + custom + some_string)
                        if self.parameters.suffix_pos_swap:
                            # "custom!example"
                            mangled.append(custom + symbol + some_string)

        return mangled

    # "example"
    def normal_mangling(self, line):
        return "Normal-Mangling", self.mutate(line)

    # "EXAMPLE"
    def uppercase_mangling(self, line):
        return "UpperCase-Mangling", self.mutate(line.upper())

    # "Example"
    def firstup_mangling(self, line):
        return "FirstUp-Mangling", self.mutate(line.title())

    # "examplE"
    def lastup_mangling(self, line):
        return "LastUp-Mangling", self.mutate(line[0:-1] + line[-1:].upper())

    # "exampleexample"
    def double_mangling(self, line):
        return "Double-Mangling", self.mutate(line + line)

    # "EXAMPLEEXAMPLE"
    def doubleandupper_mangling(self, line):
        return "DoubleAndUpper-Mangling", self.mutate(line.upper() +
                                                      line.upper())

    # "ExampleExample"
    def doubleandfirstup_mangling(self, line):
        return "DoubleAndFirstUp-Mangling", self.mutate(line.title() +
                                                        line.title())

    # "exampleexampleexample"
    def triple_mangling(self, line):
        return "Triple-Mangling", self.mutate(line + line + line)

    # "elpmaxe"
    def reversed_mangling(self, line):
        return "Reversed-Mangling", self.mutate(line[::-1])

    # "3x4mpl3"
    def replacevowels_mangling(self, line):
        vowels = {'a': '4',
                  'e': '3',
                  'i': '1',
                  'o': '0',
                  'A': '4',
                  'E': '3',
                  'I': '1',
                  'O': '0'}  # 'u' | 'U' are generally not replaced by a number

        for i, j in vowels.items():
            line = line.replace(i, j)

        return "ReplaceVowels-Mangling", self.mutate(line)

    # "l3373x4mpl3"
    def basicleet_mangling(self, line):
        leet = {'a': '4',
                'e': '3',
                'g': '6',
                'i': '1',
                'o': '0',
                's': '5',
                't': '7',
                'A': '4',
                'E': '3',
                'G': '6',
                'I': '1',
                'O': '0',
                'S': '5',
                'T': '7'}

        for i, j in leet.items():
            line = line.replace(i, j)

        return "BasicLeet-Mangling", self.mutate(line)

    # "eXaMPLe"
    def upperminusvowels_mangling(self, line):
        line = line.upper()
        vowels_upper = ('A', 'E', 'I', 'O', 'U')
        for character in line:
            if character in vowels_upper:
                line = line.replace(character, character.lower())
        return "UpperMinusVowels-Mangling", self.mutate(line)

    # "ExAmPLe"
    def upperminusconsonants_mangling(self, line):
        line = line.lower()
        vowels_lower = ('a', 'e', 'i', 'o', 'u')
        for character in line:
            if character in vowels_lower:
                line = line.replace(character, character.upper())
        return "UpperMinusConsonants-Mangling", self.mutate(line)

    # Example + eXample + exAmple + [...]
    def recursivecase_mangling(self, line):
        accumulated = []
        for n in range(0, len(line)):
            accumulated.extend(self.mutate(line[:n] + line[n].upper() + line[n+1:]))
        return "RecursiveCase-Mangling", sorted(set(accumulated))
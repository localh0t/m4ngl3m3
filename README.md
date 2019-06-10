![version 0.1.2](http://img.shields.io/badge/version-v0.1.2-orange.svg) ![python 3](http://img.shields.io/badge/python-3-blue.svg)

# m4ngl3m3!

<p align="center">
  <img src="https://cdn-images-1.medium.com/max/800/1*CE0ChZPVvFMuJ5wXNUMHVg.png">
</p>

## Quick Installation:

    $ git clone https://github.com/localh0t/m4ngl3m3
    $ cd m4ngl3m3
    $ ./main.py

## Basic Help:

    usage: main.py [-h] [-fy FROM_YEAR] [-ty TO_YEAR] [-sy] [-nf NUMBERS_FILE]
                   [-sf SYMBOLS_FILE] [-cf CUSTOM_FILE] [-sbs] [-sap]
                   [-mm MUTATION_METHODS]
                   MUTATION_MODE STRINGS_FILE OUTPUT_FILE

    Common password pattern generator using strings list

    positional arguments:
      MUTATION_MODE         Mutation mode to perform: (prefix-mode | 
                            suffix-mode | dual-mode)
      STRINGS_FILE          File with strings to mutate
      OUTPUT_FILE           Where to write the mutated strings

    optional arguments:
      -h, --help            show this help message and exit
      -fy FROM_YEAR, --from-year FROM_YEAR
                            Year where our iteration starts (default: 
                            2015)
      -ty TO_YEAR, --to-year TO_YEAR
                            Year where our iteration ends (default: 
                            2020)
      -sy, --short-year     Also add shorter year form when iterating 
                            (default: False)
      -nf NUMBERS_FILE, --numbers-file NUMBERS_FILE
                            Numbers prefix/suffix file (default:
                            ./files/numbers/numbers_set2.txt)
      -sf SYMBOLS_FILE, --symbols-file SYMBOLS_FILE
                            Symbols prefix/suffix file (default:
                            ./files/symbols/symbols_set2.txt)
      -cf CUSTOM_FILE, --custom-file CUSTOM_FILE
                            Custom words/dates/initials/etc file 
                            (default: None)
      -sbs, --symbols-before-suffix
                            Insert symbols also before years/numbers/
                            custom (when in suffix-mode or dual-mode)
                            (default: False)
      -sap, --symbols-after-prefix
                            Insert symbols also after years/numbers/
                            custom (when in prefix-mode or dual-mode) 
                            (default: False)
      -mm MUTATION_METHODS, --mutation-methods MUTATION_METHODS
                            Mutation methods to perform (comma
                            separated, no spaces) (valid: see
                            MUTATION_METHODS.md)                  
                            (default:
                            normal,uppercase,firstup,replacevowels)

### --from-year (-fy), --to-year (-ty):

Here we set where we want our script to **start** and **end** iterating over
years. Many times people include the **current year** in an
effort to add some entropy. Because passwords could be **outdated**, or the
years included could be in the (near) **future**, we are going to add them as a
range. For **online** environments, we would be looking at a conservative
approach and only include ranges in the order of **(-1, +1)** or **(-2, +2)**.
For **offline** environments, the range could be wider to **(-20, +5)** or even
**(-50, +10)**. Output example:

    password2017
    [...]
    password2018
    [...]
    password2019

### --short-year (-sy):

When iterating years, also add its shorter **double digit form**. Output
example:

    password17
    [...]
    password18
    [...]
    password19

### --numbers-file (-nf):

In this argument we are going to select a file containing **numbers** that
people frequently add to their passwords. By default I included **6** sets, the
largest being the **6**, and the rest being **subsets** of the previous one. The
numbers included in the first sets **(1,2…)** are more likely to be present that
the ones **only** included in latest sets **(…5,6)**. Again, for **online**
environments, we would be looking at using the first three sets, where in
**offline** environments, we could use the last ones. By default, the script
uses the set number **2**. Output example:

    password1
    [...]
    password123
    [...]
    password1234

### --symbols-file (-sf):

In this argument we are going to select a file  containing **symbols** that
people frequently add to their passwords. Again, set number **1** is the
shortest, set number **6** is the largest. The symbols included in the first
sets **(1,2…)** are more likely to be present that the ones **only** included in
latest sets **(…5,6)**. By default, the script uses the set number **2**. Output
example:

    password123!
    [...]
    password2018?
    [...]
    password1234.

### --custom-file (-cf):

Here we add anything else we **know** about our targets (and it’s not considered
as the “**base**” of the password itself). Let the creativity roll in! It could
be from **company initials**, **birth dates**, **special dates**… to **specific
years**, **short** **keywords**, etc. This custom strings will be treated in the
same way that the years/numbers. Output example:

    passwordABC
    [...]
    password01011980!
    [...]
    password.admin

### MUTATION_MODE (positional argument):

In this parameter we are going to select how the tool will work when shifting
strings. You can choose one of three:

* **suffix-mode:** It will add years, numbers, symbols and custom **after** the
main string. Example: *password***2018!**
* **prefix-mode:** It will add years, numbers, symbols and custom **before** the
main string. Example: **!2018***password*
* **dual-mode:** As the name suggests, it uses both modes (generates both
outputs).

### STRINGS_FILE (positional argument):

File containing **strings to mutate**. If you’re for example, doing a pentest
and don’t know where to start, I would suggest you using a tool like
[CeWL](https://github.com/digininja/CeWL) to spider the company website, and
keep the **most recurring words** (including the company name of course).

### OUTPUT_FILE (positional argument):

Simply, file where we want to write the **mutated strings**.

### --symbols-before-suffix (-sbs):

When this flag is enabled, and we are running the tool either  in **suffix-mode** 
or **dual-mode**, the script will also add the symbols **before**
years/numbers/custom. Output example:

    password2018!
    [...]
    password!2018
    [...]

### --symbols-after-prefix (-sap):

When this flag is enabled, and we are running the tool either in **prefix-mode** 
or **dual-mode**, the script will also add the symbols **after**
years/numbers/custom. Output example:

    !2018password
    [...]
    2018!password
    [...]

### --mutation-methods (-mm):

In this parameter we define which mutation methods are going to be performed.
Mutation methods are **base transformations** made **before** starting iterating
over years/numbers/symbols/custom. You can select as many mutation methods as
you want. For a list of all valid mutation methods, check: [MUTATION_METHODS.md](MUTATION_METHODS.md).  
By default, **m4ngl3m3!** runs with the following: *Normal, UpperCase, FirstUp and
ReplaceVowels.*


## Usage examples:

In order to see some basic usage examples, please take a look at: [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)


## License:

See: [LICENSE.md](LICENSE.md)
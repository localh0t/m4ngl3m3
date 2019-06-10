### Usage example (1):

    $ ./main.py --from-year 2017 --to-year 2018 --symbols-before-suffix suffix-mode strings.txt output.txt
    (or, shorter version)
    $ ./main.py -fy 2017 -ty 2018 -sbs suffix-mode strings.txt output.txt
    [!] Starting...
    [+] Normal-Mangling mutation method done on string: admin
    [+] UpperCase-Mangling mutation method done on string: admin
    [+] FirstUp-Mangling mutation method done on string: admin
    [+] ReplaceVowels-Mangling mutation method done on string: admin
    ---
    [+] Normal-Mangling mutation method done on string: companyname
    [+] UpperCase-Mangling mutation method done on string: companyname
    [+] FirstUp-Mangling mutation method done on string: companyname
    [+] ReplaceVowels-Mangling mutation method done on string: companyname
    ---
    [!] All done!
    [!] Strings read: 2
    [!] Strings written: 888
    [!] Exiting ...

> “Iterate from year 2017 to 2018, default numbers and symbols file, suffix mode
> only,  insert symbols also before suffix, default mutation methods.”

#### Input file:

    admin
    companyname

#### Output file:

    admin
    admin!
    [...]
    Admin2017!
    Admin!2017
    [...]
    COMPANYNAME1234!
    COMPANYNAME!1234
    [...]
    c0mp4nyn4m32018@
    c0mp4nyn4m3@2018
    [...]

### Usage example (2):

    $ ./main.py -fy 2016 -ty 2019 -sy -nf ./files/numbers/numbers_set1.txt -sf ./files/symbols/symbols_set1.txt -sbs -sap -mm normal,firstup,doubleandfirstup,basicleet dual-mode strings.txt output.txt
    [!] Starting...
    [+] Normal-Mangling mutation method done on string: password
    [+] FirstUp-Mangling mutation method done on string: password
    [+] DoubleAndFirstUp-Mangling mutation method done on string: password
    [+] BasicLeet-Mangling mutation method done on string: password
    ---
    [+] Normal-Mangling mutation method done on string: example
    [+] FirstUp-Mangling mutation method done on string: example
    [+] DoubleAndFirstUp-Mangling mutation method done on string: example
    [+] BasicLeet-Mangling mutation method done on string: example
    ---
    [!] All done!
    [!] Strings read: 2
    [!] Strings written: 1288
    [!] Exiting ...

> “Iterate from year 2016 to 2019, with short year form also, use set 1 for
> numbers and symbols, dual-mode (prefix and suffix),  insert symbols also before
suffix, insert symbols also after prefix, mutation methods: Normal, FirstUp,
DoubleAndFirstUp, BasicLeet.”

#### Input file:

    password
    example

#### Output file:

    password
    password!
    password@
    [...]
    !2018PasswordPassword
    !18PasswordPassword
    2018!PasswordPassword
    18!PasswordPassword
    [...]
    p455w0rd$1
    p455w0rd123
    p455w0rd123!
    p455w0rd!123
    [...]
    Example!2019
    Example!19
    [...]
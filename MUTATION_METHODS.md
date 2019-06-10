|             Mutation Method                 |                          Description                                                    |         Example                        |
|---------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------|
| Normal (normal)                             | Does nothing to given string.                                                           | password                               |
| UpperCase (uppercase)                       | Converts the entire string to uppercase.                                                | PASSWORD                               |
| FirstUp (firstup)                           | Capitalizes the first letter of the string.                                             | Password                               |
| LastUp (lastup)                             | Capitalizes the last letter of the string.                                              | passworD                               |
| Double (double)                             | Doubles the given string.                                                               | passwordpassword                       |
| DoubleAndUpper (doubleandupper)             | Combines Double + UpperCase.                                                            | PASSWORDPASSWORD                       |
| DoubleAndFirstUp (doubleandfirstup)         | Combines Double + FirstUp.                                                              | PasswordPassword                       |
| Triple (triple)                             | Triples the given string.                                                               | passwordpasswordpassword               |
| Reversed (reversed)                         | Reverses the given string.                                                              | drowssap                               |
| ReplaceVowels (replacevowels)               | Replaces vowels with it's number equivalent (minus the 'u').                            | p4ssw0rd                               |
| BasicLeet (basicleet)                       | Converts given string to basic leet speak.                                              | p455w0rd                               |
| UpperMinusVowels (upperminusvowels)         | Converts vowels to lowercase and consonants to uppercase.                               | PaSSWoRD                               |
| UpperMinusConsonants (upperminusconsonants) | Converts vowels to uppercase and consonants to lowercase.                               | pAsswOrd                               |
| RecursiveCase (recursivecase)               | Converts one character to uppercase at a time (WARNING: can generate a lot of strings). | Password + pAssword + paSsword + [...] |
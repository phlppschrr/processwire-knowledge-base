# $password->hash($pass): string

Source: `wire/core/Password.php`

Given an unhashed password, generate a hash of the password for database storage and comparison

Note: When blowfish, returns the entire blowfish string which has the salt as the first 28 characters.

## Arguments

- string $pass Raw password

## Return value

string

## Throws

- WireException

# Password

Source: `wire/core/Password.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire Password Fieldtype

Class to hold combined password/salt info. Uses Blowfish when possible.
Specially used by FieldtypePassword.

Methods:
- [`matches(string $pass): bool`](method-matches.md) Does this Password match the given string?
- [`__get(string $name): mixed`](method-__get.md) Get a property via direct access ('salt' or 'hash')
- [`__set(string $key, mixed $value)`](method-__set.md) Set a property
- [`setPass(string $value)`](method-___setpass.md) (hookable) Set the 'pass' to the given value
- [`salt(): string`](method-salt.md) Generate a random salt for the given hashType
- [`randomBase64String(int $requiredLength = 22, array|bool $options = array()): string|array`](method-randombase64string.md) Generate a truly random base64 string of a certain length
- [`isBlowfish(string $str = ''): bool`](method-isblowfish.md) Returns whether the given string is blowfish hashed
- [`supportsBlowfish(): bool`](method-supportsblowfish.md) Returns whether the current system supports Blowfish
- [`hash(string $pass): string`](method-hash.md) Given an unhashed password, generate a hash of the password for database storage and comparison
- [`randomAlpha(int $qty = 1, bool $alphanumeric = false, array $disallow = array()): string`](method-randomalpha.md) Return a pseudo-random alpha or alphanumeric character
- [`randomAlnum(int $length = 0, array $options = array()): string`](method-randomalnum.md) Return cryptographically secure random alphanumeric, alpha or numeric string
- [`randomLetters(int $length = 0, array $options = array()): string`](method-randomletters.md) Return string of random letters
- [`randomDigits(int $length = 0, array $options = array()): string`](method-randomdigits.md) Return string of random digits
- [`randomPass(array $options = array()): string`](method-randompass.md) Generate and return a random password
- [`random(): WireRandom`](method-random.md)

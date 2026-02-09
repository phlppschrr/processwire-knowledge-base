# Password

Source: `wire/core/Password.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire Password Fieldtype

Class to hold combined password/salt info. Uses Blowfish when possible.
Specially used by FieldtypePassword.

Methods:
- [`matches(string $pass): bool`](method-matches.md)
- [`__get(string $name): mixed`](method-__get.md)
- [`__set(string $key, mixed $value)`](method-__set.md)
- [`setPass(string $value)`](method-___setpass.md) (hookable)
- [`salt(): string`](method-salt.md)
- [`randomBase64String(int $requiredLength = 22, array|bool $options = array()): string|array`](method-randombase64string.md)
- [`isBlowfish(string $str = ''): bool`](method-isblowfish.md)
- [`supportsBlowfish(): bool`](method-supportsblowfish.md)
- [`hash(string $pass): string`](method-hash.md)
- [`randomAlpha(int $qty = 1, bool $alphanumeric = false, array $disallow = array()): string`](method-randomalpha.md)
- [`randomAlnum(int $length = 0, array $options = array()): string`](method-randomalnum.md)
- [`randomLetters(int $length = 0, array $options = array()): string`](method-randomletters.md)
- [`randomDigits(int $length = 0, array $options = array()): string`](method-randomdigits.md)
- [`randomPass(array $options = array()): string`](method-randompass.md)
- [`random(): WireRandom`](method-random.md)

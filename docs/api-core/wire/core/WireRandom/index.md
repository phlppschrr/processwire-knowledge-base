# WireRandom

Source: `wire/core/WireRandom.php`

Inherits: `Wire`

## Summary

Random generators for ProcessWire

Common methods:
- [`alphanumeric()`](method-alphanumeric.md)
- [`string1()`](method-string1.md)
- [`string2()`](method-string2.md)
- [`alpha()`](method-alpha.md)
- [`numeric()`](method-numeric.md)

Includes methods for random strings, numbers, arrays and passwords.


@since 3.0.111

Usage example
~~~~~
$random = new WireRandom();
$s = $random->alphanumeric(10);
$i = $random->integer(0, 10);
~~~~~

## Methods
- [`alphanumeric(int $length = 0, array $options = array()): string`](method-alphanumeric.md) Return random alphanumeric, alpha or numeric string
- [`string1(int $length, string $allowed, array $options): string`](method-string1.md) Generate a random string using faster method
- [`string2(int $length, string $allowed, array $options): string`](method-string2.md) Generate random string using method that pulls from the base64 method
- [`alpha(int $length = 0, array $options = array()): string`](method-alpha.md) Return string of random ASCII alphabetical letters
- [`numeric(int $length = 0, array $options = array()): string`](method-numeric.md) Return string of random numbers/digits
- [`string(int $length = 0, string $characters = '', array $options = []): string`](method-string.md) Generate a random string using given characters
- [`integer(int $min = 0, int $max = PHP_INT_MAX, array $options = array()): int|array`](method-integer.md) Get a random integer
- [`arrayItem(array $a, array $options = array()): mixed|array|null`](method-arrayitem.md) Get a random item (or items, key or keys) from the given array
- [`arrayValue(array $a): mixed|null`](method-arrayvalue.md) Get a random value from given array
- [`arrayValues(array $a, int $qty = 0): array`](method-arrayvalues.md) Return a random version of given array or a quantity of random items
- [`arrayKey(array $a): string|int`](method-arraykey.md) Get a random key from given array
- [`arrayKeys(array $a, int $qty = 0): array`](method-arraykeys.md) Get a random version of all keys in given array (or a specified quantity of them)
- [`shuffle(string|array $value): string|array`](method-shuffle.md) Shuffle a string or an array
- [`pass(array $options = array()): string`](method-pass.md) Generate and return a random password
- [`passCreate(array $options): string`](method-passcreate.md) Create a password (for password method)
- [`passTrunc(string $value, array $options): string`](method-passtrunc.md) Truncate password to requested maxLength without removing required options (for password method)
- [`base64(int $requiredLength = 22, array|bool $options = array()): string|array`](method-base64.md) Generate a truly random base64 string of a certain length
- [`randomBufferToSalt(string $buffer, int $requiredLength): string`](method-randombuffertosalt.md) Given random buffer string of bytes return base64 encoded salt
- [`cryptoSecure(): bool`](method-cryptosecure.md) Is a crypto secure method of generating numbers available?
- [`_strlen(string $s): int`](method-_strlen.md) Return string length, using mb_strlen() when available, or strlen() when not

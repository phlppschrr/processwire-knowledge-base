# WireRandom

Source: `wire/core/WireRandom.php`

Inherits: `Wire`

Random generators for ProcessWire

Includes methods for random strings, numbers, arrays and passwords.


@since 3.0.111

Usage example
~~~~~
$random = new WireRandom();
$s = $random->alphanumeric(10);
$i = $random->integer(0, 10);
~~~~~

Methods:
- [`alphanumeric(int $length = 0, array $options = array()): string`](method-alphanumeric.md)
- [`string1(int $length, string $allowed, array $options): string`](method-string1.md)
- [`string2(int $length, string $allowed, array $options): string`](method-string2.md)
- [`alpha(int $length = 0, array $options = array()): string`](method-alpha.md)
- [`numeric(int $length = 0, array $options = array()): string`](method-numeric.md)
- [`string(int $length = 0, string $characters = '', array $options = []): string`](method-string.md)
- [`integer(int $min = 0, int $max = PHP_INT_MAX, array $options = array()): int|array`](method-integer.md)
- [`arrayItem(array $a, array $options = array()): mixed|array|null`](method-arrayitem.md)
- [`arrayValue(array $a): mixed|null`](method-arrayvalue.md)
- [`arrayValues(array $a, int $qty = 0): array`](method-arrayvalues.md)
- [`arrayKey(array $a): string|int`](method-arraykey.md)
- [`arrayKeys(array $a, int $qty = 0): array`](method-arraykeys.md)
- [`shuffle(string|array $value): string|array`](method-shuffle.md)
- [`pass(array $options = array()): string`](method-pass.md)
- [`passCreate(array $options): string`](method-passcreate.md)
- [`passTrunc(string $value, array $options): string`](method-passtrunc.md)
- [`base64(int $requiredLength = 22, array|bool $options = array()): string|array`](method-base64.md)
- [`randomBufferToSalt(string $buffer, int $requiredLength): string`](method-randombuffertosalt.md)
- [`cryptoSecure(): bool`](method-cryptosecure.md)
- [`_strlen(string $s): int`](method-_strlen.md)

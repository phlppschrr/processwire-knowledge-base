# WireNumberTools

Source: `wire/core/WireNumberTools.php`

Inherits: `Wire`

## Summary

Tools for working with numbers

Common methods:
- [`uniqueNumber()`](method-uniquenumber.md)
- [`randomInteger()`](method-randominteger.md)
- [`strToBytes()`](method-strtobytes.md)
- [`bytesToStr()`](method-bytestostr.md)
- [`locale()`](method-locale.md)

@since 3.0.213

## Methods
- [`uniqueNumber(array|string $options = array()): int`](method-uniquenumber.md) Generate and return an installation unique number/ID (integer)
- [`randomInteger(int $min, int $max, bool $throw = false): int`](method-randominteger.md) Return a random integer (cryptographically secure when available)
- [`strToBytes(string|int|float $value, string|null $unit = null): int`](method-strtobytes.md) Given a value like "1M", "2MB", "3 kB", "4 GB", "5tb" etc. return quantity of bytes
- [`bytesToStr(int|string $bytes, array|int $options = array()): string`](method-bytestostr.md) Given a quantity of bytes (int), return readable string that refers to quantity in bytes, kB, MB, GB and TB
- [`locale(string $key = ''): array|string|int|null`](method-locale.md) Get a number formatting property from current locale

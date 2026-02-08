# $wireRandom->randomBufferToSalt($buffer, $requiredLength): string

Source: `wire/core/WireRandom.php`

Given random buffer string of bytes return base64 encoded salt

## Usage

~~~~~
// basic usage
$string = $wireRandom->randomBufferToSalt($buffer, $requiredLength);
~~~~~

## Arguments

- `$buffer` `string`
- `$requiredLength` `int`

## Return value

- `string`

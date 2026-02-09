# $punycode->decode($input): string

Source: `wire/core/Punycode.php`

Decode a Punycode domain name to its Unicode counterpart

## Usage

~~~~~
// basic usage
$string = $punycode->decode($input);
~~~~~

## Arguments

- `$input` `string` Domain name in Punycode

## Return value

- `string` Unicode domain name

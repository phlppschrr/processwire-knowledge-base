# $punycode->decodePart($input): string

Source: `wire/core/Punycode.php`

Decode a part of domain name, such as tld

## Usage

~~~~~
// basic usage
$string = $punycode->decodePart($input);
~~~~~

## Arguments

- `$input` `string` Part of a domain name

## Return value

- `string` Unicode domain part

# $punycode->encodePart($input): string

Source: `wire/core/Punycode.php`

Encode a part of a domain name, such as tld, to its Punycode version

## Usage

~~~~~
// basic usage
$string = $punycode->encodePart($input);
~~~~~

## Arguments

- `$input` `string` Part of a domain name

## Return value

- `string` Punycode representation of a domain part

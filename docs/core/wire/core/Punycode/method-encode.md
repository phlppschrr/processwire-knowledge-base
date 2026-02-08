# $punycode->encode($input): string

Source: `wire/core/Punycode.php`

Encode a domain to its Punycode version

## Usage

~~~~~
// basic usage
$string = $punycode->encode($input);
~~~~~

## Arguments

- `$input` `string` Domain name in Unicode to be encoded

## Return value

- `string` Punycode representation in ASCII

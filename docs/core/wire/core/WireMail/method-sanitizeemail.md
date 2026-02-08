# $wireMail->sanitizeEmail($email): string

Source: `wire/core/WireMail.php`

Sanitize an email address or throw WireException if invalid or in blacklist

## Usage

~~~~~
// basic usage
$string = $wireMail->sanitizeEmail($email);
~~~~~

## Arguments

- `$email` `string`

## Return value

- `string`

## Exceptions

- `WireException`

# $wireMail->quotedPrintableString($text): string

Source: `wire/core/WireMail.php`

Return the text quoted-printable encoded

Uses short notation for charset and encoding suitable for email headers
as laid out in rfc2047.

## Usage

~~~~~
// basic usage
$string = $wireMail->quotedPrintableString($text);
~~~~~

## Arguments

- `$text` `string`

## Return value

- `string`

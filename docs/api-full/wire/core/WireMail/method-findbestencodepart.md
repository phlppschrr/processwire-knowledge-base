# $wireMail->findBestEncodePart($input, $maxlen = 63, $isFirst = false): string

Source: `wire/core/WireMail.php`

Tries to split the passed subject at a whitespace at or before $maxlen,
falling back to a hard substr if none was found, and returns the
left part.

Makes sure that the quoted-printable encoded part is inside the 76 characters
header limit (66 for first line that has the header name, minus a buffer
of 2 characters for whitespace) given in rfc2047.

## Usage

~~~~~
// basic usage
$string = $wireMail->findBestEncodePart($input);

// usage with all arguments
$string = $wireMail->findBestEncodePart($input, $maxlen = 63, $isFirst = false);
~~~~~

## Arguments

- `$input` `string` The subject to encode
- `$maxlen` (optional) `int` Maximum length of unencoded string, defaults to 63
- `$isFirst` (optional) `bool` Set to true for first line to account for the header name

## Return value

- `string`

# $sanitizer->email($value, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Sanitize and validate an email address

Returns valid email address, or blank string if it isn’t valid.

## Arguments

- string $value Email address to sanitize and validate.
- array $options All options require 3.0.208+ - `allowIDN` (bool|int): Allow internationalized domain names? (default=false) Specify int 2 to also allow UTF-8 in local-part of email [SMTPUTF8] (i.e. `bøb`). - `getASCII` (bool): Returns ASCII encoded version of email when host is IDN (default=false) Does not require the allowIDN option since returned email host will be only ASCII. Not meant to be combined with allowIDN=2 option since local-part of email does not ASCII encode. - `getUTF8` (bool): Converts ASCII-encoded IDNs to UTF-8, when present (default=false) - `checkDNS` (bool): Check that host part of email has a valid DNS record? (default=false) Warning: this slows things down a lot and should not be used in time sensitive cases. - `throw` (bool): Throw WireException on fail with details on why it failed (default=false)

## Return value

string Sanitized, valid email address, or blank string on failure.

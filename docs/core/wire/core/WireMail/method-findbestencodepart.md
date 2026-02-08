# WireMail::findBestEncodePart()

Source: `wire/core/WireMail.php`

Tries to split the passed subject at a whitespace at or before $maxlen,
falling back to a hard substr if none was found, and returns the
left part.

Makes sure that the quoted-printable encoded part is inside the 76 characters
header limit (66 for first line that has the header name, minus a buffer
of 2 characters for whitespace) given in rfc2047.

@param string $input The subject to encode

@param int $maxlen Maximum length of unencoded string, defaults to 63

@param bool $isFirst Set to true for first line to account for the header name

@return string

# $wireUpload->validateFilename($value, $extensions = array()): bool|string

Source: `wire/core/WireUpload.php`

Sanitize/validate a given filename

## Arguments

- `$value` `string` Filename
- `$extensions` (optional) `array` Allowed file extensions

## Return value

bool|string Returns boolean false if invalid or string of potentially modified filename if valid

# $wireUpload->validateFilename($value, $extensions = array()): bool|string

Source: `wire/core/WireUpload.php`

Sanitize/validate a given filename

## Usage

~~~~~
// basic usage
$bool = $wireUpload->validateFilename($value);

// usage with all arguments
$bool = $wireUpload->validateFilename($value, $extensions = array());
~~~~~

## Arguments

- `$value` `string` Filename
- `$extensions` (optional) `array` Allowed file extensions

## Return value

- `bool|string` Returns boolean false if invalid or string of potentially modified filename if valid

# $sanitizer->fieldName($value, $beautify = false, $maxLength = 128): string

Source: `wire/core/Sanitizer.php`

Sanitize consistent with names used by ProcessWire fields and/or PHP variables

- Allows upper and lowercase ASCII letters, digits and underscore.
- ProcessWire field names follow the same conventions as PHP variable names, though digits may lead.
- This method is the same as the varName() sanitizer except that it supports beautification and max length.
- Unlike other name formats, hyphen and period are excluded because they aren't allowed characters in PHP variables.

## Example

~~~~~
$test = "Hello world";
echo $sanitizer->fieldName($test); // outputs: Hello_world
~~~~~

## Usage

~~~~~
// basic usage
$string = $sanitizer->fieldName($value);

// usage with all arguments
$string = $sanitizer->fieldName($value, $beautify = false, $maxLength = 128);
~~~~~

## Arguments

- `$value` `string` Value you want to sanitize
- `$beautify` (optional) `bool|int` Should be true when using the name for a new field (default=false). You may also specify constant `Sanitizer::translate` (or number 2) for the $beautify param, which will make it translate letters based on the system page name translation settings.
- `$maxLength` (optional) `int` Maximum number of characters allowed in the name (default=128).

## Return value

- `string` Sanitized string

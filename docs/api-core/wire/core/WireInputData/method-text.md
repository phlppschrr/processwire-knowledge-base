# $wireInputData->text($varName, $options = array()): string

Source: `wire/core/WireInputData.php`

Sanitize to single line of text up to 255 characters (1024 bytes max), HTML markup is removed

## Usage

~~~~~
// basic usage
$string = $wireInputData->text($varName);

// usage with all arguments
$string = $wireInputData->text($varName, $options = array());
~~~~~

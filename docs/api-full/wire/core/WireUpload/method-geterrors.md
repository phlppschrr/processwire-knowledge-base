# $wireUpload->getErrors($clear = false): array

Source: `wire/core/WireUpload.php`

Get error messages

## Usage

~~~~~
// basic usage
$array = $wireUpload->getErrors();

// usage with all arguments
$array = $wireUpload->getErrors($clear = false);
~~~~~

## Arguments

- `$clear` (optional) `bool` Clear the list of error messages? (default=false)

## Return value

- `array` of strings

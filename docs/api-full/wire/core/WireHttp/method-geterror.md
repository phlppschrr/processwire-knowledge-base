# $wireHttp->getError($getArray = false): string|array

Source: `wire/core/WireHttp.php`

Get a string of the last error message

## Usage

~~~~~
// basic usage
$string = $wireHttp->getError();

// usage with all arguments
$string = $wireHttp->getError($getArray = false);
~~~~~

## Arguments

- `$getArray` (optional) `bool` Specify true to receive an array of error messages, or omit for a string.

## Return value

- `string|array`

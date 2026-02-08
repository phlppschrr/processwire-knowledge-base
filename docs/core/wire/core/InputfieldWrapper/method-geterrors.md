# $inputfieldWrapper->getErrors($clear = false): array

Source: `wire/core/InputfieldWrapper.php`

Return an array of errors that occurred on any of the children during input processing.

Should only be called after `InputfieldWrapper::processInput()`.

## Usage

~~~~~
// basic usage
$array = $inputfieldWrapper->getErrors();

// usage with all arguments
$array = $inputfieldWrapper->getErrors($clear = false);
~~~~~

## Arguments

- `$clear` (optional) `bool` Specify true to clear out the errors (default=false).

## Return value

- `array` Array of error strings

# $inputfield->error($text, $flags = 0): $this

Source: `wire/core/Inputfield.php`

Record an error for this Inputfield

The error message will be placed in the context of this Inputfield.
See the `Wire::error()` method for full details on arguments and options.

## Usage

~~~~~
// basic usage
$result = $inputfield->error($text);

// usage with all arguments
$result = $inputfield->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string` Text of error message
- `$flags` (optional) `int` Optional flags

## Return value

- `$this`

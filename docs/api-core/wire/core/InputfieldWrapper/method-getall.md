# $inputfieldWrapper->getAll(array $options = array()): InputfieldsArray

Source: `wire/core/InputfieldWrapper.php`

Get all Inputfields below this recursively in a flat InputfieldWrapper (children, and their children, etc.)

Note that all InputfieldWrapper instances are removed as a result (except for the containing InputfieldWrapper).

## Usage

~~~~~
// basic usage
$inputfieldsArray = $inputfieldWrapper->getAll();

// usage with all arguments
$inputfieldsArray = $inputfieldWrapper->getAll(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` Options to modify behavior (3.0.169+) - `withWrappers` (bool): Also include InputfieldWrapper objects? (default=false) 3.0.169+

## Return value

- `InputfieldsArray`

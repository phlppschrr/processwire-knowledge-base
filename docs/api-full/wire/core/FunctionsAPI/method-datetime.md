# $functionsAPI->datetime($format = '', $value = ''): WireDateTime|string|int

Source: `wire/core/FunctionsAPI.php`

Access date and time related tools ($datetime API variable as a function)

This behaves the same as the `$datetime` API variable except that you can optionally provide
arguments as a shortcut to the `$datetime->formatDate()` method.

## Example

~~~~~
$str = datetime()->relativeTimeStr('2016-10-10');
$str = datetime('Y-m-d');  // shortcut to formatDate method
$str = datetime('Y-m-d', time()); // shortcut to formatDate method
~~~~~

## Usage

~~~~~
// basic usage
$wireDateTime = $functionsAPI->datetime();

// usage with all arguments
$wireDateTime = $functionsAPI->datetime($format = '', $value = '');
~~~~~

## Arguments

- `$format` (optional) `string` Optional date format
- `$value` (optional) `string|int` Optional date to format

## Return value

- `WireDateTime|string|int`

## See Also

- WireDateTime

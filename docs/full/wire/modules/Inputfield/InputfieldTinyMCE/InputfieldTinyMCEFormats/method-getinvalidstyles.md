# $inputfieldTinyMCEFormats->getInvalidStyles($value, $defaultValue, $merge = false): array|string

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEFormats.php`

Get TinyMCE "invalid_styles" setting and prepare as array value

Parses value in space-separated string format (commas optional):
In the above, line-height and color are disabled for all elements,
background and background color are disabled for "a" elements,
and height is disabled for "td" elements.

## Example

~~~~~
line-height, color, a=background|background-color, td=height
~~~~~

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCEFormats->getInvalidStyles($value, $defaultValue);

// usage with all arguments
$array = $inputfieldTinyMCEFormats->getInvalidStyles($value, $defaultValue, $merge = false);
~~~~~

## Arguments

- `$value` `string|array`
- `$defaultValue` `array|string`
- `$merge` (optional) `bool` Merge with given defaultValue?

## Return value

- `array|string`

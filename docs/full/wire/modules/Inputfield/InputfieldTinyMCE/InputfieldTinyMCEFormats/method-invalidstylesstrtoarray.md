# $inputfieldTinyMCEFormats->invalidStylesStrToArray($value, array $a = array()): array

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEFormats.php`

Convert invalid_styles string to array

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCEFormats->invalidStylesStrToArray($value);

// usage with all arguments
$array = $inputfieldTinyMCEFormats->invalidStylesStrToArray($value, array $a = array());
~~~~~

## Arguments

- `$value` `string` i.e. "line-height color a=background|background-color td=height"
- `$a` (optional) `array` Optionally merge with these styles

## Return value

- `array`

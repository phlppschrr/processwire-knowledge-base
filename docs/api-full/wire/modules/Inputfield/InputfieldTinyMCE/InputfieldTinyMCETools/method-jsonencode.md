# $inputfieldTinyMCETools->jsonEncode($a, $propertyName, $pretty = true): string

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCETools.php`

Encode array to JSON

## Usage

~~~~~
// basic usage
$string = $inputfieldTinyMCETools->jsonEncode($a, $propertyName);

// usage with all arguments
$string = $inputfieldTinyMCETools->jsonEncode($a, $propertyName, $pretty = true);
~~~~~

## Arguments

- `$a` `array`
- `$propertyName` `string` Name of property JSON is for
- `$pretty` (optional) `bool`

## Return value

- `string`

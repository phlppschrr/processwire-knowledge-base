# $inputfieldTinyMCEConfigs->getMceToolbars($splitToArray = true): array|string[]

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEConfigs.php`

Get TinyMCE toolbar names and details

Returns array of arrays or array of strings

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCEConfigs->getMceToolbars();

// usage with all arguments
$array = $inputfieldTinyMCEConfigs->getMceToolbars($splitToArray = true);
~~~~~

## Arguments

- `$splitToArray` (optional) `bool` Specify false to return array of strings

## Return value

- `array|string[]`

# $inputfieldTinyMCE->getSettingNames($types): string[]

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Get all configurable setting names

## Usage

~~~~~
// basic usage
$result = $inputfieldTinyMCE->getSettingNames($types);
~~~~~

## Arguments

- `$types` `array|string` Types to get, one or more of: 'tinymce', 'field', 'module', 'optionals'

## Return value

- `string[]`

## Exceptions

- `WireException` if given unknown setting type

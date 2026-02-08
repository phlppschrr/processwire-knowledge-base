# $inputfieldTinyMCESettings->getOriginalDefaults($key = ''): array|mixed|null

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Get original defaults from source JSON, prior to being overriden by module default settings

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCESettings->getOriginalDefaults();

// usage with all arguments
$array = $inputfieldTinyMCESettings->getOriginalDefaults($key = '');
~~~~~

## Arguments

- `$key` (optional) `string`

## Return value

- `array|mixed|null`

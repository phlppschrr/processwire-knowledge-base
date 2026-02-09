# $inputfieldTinyMCESettings->mergeSettings(array $settings1, array $settings2 = array()): array

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Merge all settings in given array and combine those with "add_" prefix

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCESettings->mergeSettings($settings1);

// usage with all arguments
$array = $inputfieldTinyMCESettings->mergeSettings(array $settings1, array $settings2 = array());
~~~~~

## Arguments

- `$settings1` `array`
- `$settings2` (optional) `array` Optionally specify this to merge/combine with those in $settings1

## Return value

- `array`

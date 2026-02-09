# $inputfieldTinyMCESettings->getSettings($defaults = null, $cacheKey = ''): array

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Get settings from Inputfield vary from the $defaults

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCESettings->getSettings();

// usage with all arguments
$array = $inputfieldTinyMCESettings->getSettings($defaults = null, $cacheKey = '');
~~~~~

## Arguments

- `$defaults` (optional) `array|null` Default settings Default settings or omit to pull automatically
- `$cacheKey` (optional) `string` Optionally cache with this key

## Return value

- `array`

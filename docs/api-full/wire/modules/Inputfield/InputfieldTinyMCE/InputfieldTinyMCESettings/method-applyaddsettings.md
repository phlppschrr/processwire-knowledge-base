# $inputfieldTinyMCESettings->applyAddSettings(array &$settings, array &$addSettings, array $defaults)

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Apply 'add_*' settings in $addSettings, plus merge all $addSettings into given $settings

This updates the $settings and $addSettings variables directly

## Usage

~~~~~
// basic usage
$result = $inputfieldTinyMCESettings->applyAddSettings($settings, $addSettings, $defaults);

// usage with all arguments
$result = $inputfieldTinyMCESettings->applyAddSettings(array &$settings, array &$addSettings, array $defaults);
~~~~~

## Arguments

- `$settings` `array`
- `$addSettings` `array`
- `$defaults` `array`

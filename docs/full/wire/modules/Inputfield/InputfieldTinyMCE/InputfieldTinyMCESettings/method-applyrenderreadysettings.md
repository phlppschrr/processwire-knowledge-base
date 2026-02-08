# $inputfieldTinyMCESettings->applyRenderReadySettings(array $addSettings = array())

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Determine which settings go where and apply to Inputfield

## Usage

~~~~~
// basic usage
$result = $inputfieldTinyMCESettings->applyRenderReadySettings();

// usage with all arguments
$result = $inputfieldTinyMCESettings->applyRenderReadySettings(array $addSettings = array());
~~~~~

## Arguments

- `$addSettings` (optional) `array` Optionally add this settings on top of those that would otherwise be used

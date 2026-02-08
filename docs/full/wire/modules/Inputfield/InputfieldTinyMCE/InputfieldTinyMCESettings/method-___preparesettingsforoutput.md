# $inputfieldTinyMCESettings->prepareSettingsForOutput(array $settings): array

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Prepare given settings ready for output

This converts relative URLs to absolute, etc.

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCESettings->prepareSettingsForOutput($settings);

// usage with all arguments
$array = $inputfieldTinyMCESettings->prepareSettingsForOutput(array $settings);
~~~~~

## Hookable

- Hookable method name: `prepareSettingsForOutput`
- Implementation: `___prepareSettingsForOutput`
- Hook with: `$inputfieldTinyMCESettings->prepareSettingsForOutput()`

## Arguments

- `$settings` `array`

## Return value

- `array`

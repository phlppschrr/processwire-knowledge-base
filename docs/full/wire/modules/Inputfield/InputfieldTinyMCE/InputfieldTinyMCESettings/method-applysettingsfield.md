# $inputfieldTinyMCESettings->applySettingsField($fieldName): bool|Field

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Apply settings settings to $this->inputfield to inherit from another field

This is called from the main InputfieldTinyMCE class.

## Usage

~~~~~
// basic usage
$bool = $inputfieldTinyMCESettings->applySettingsField($fieldName);
~~~~~

## Arguments

- `$fieldName` `string` Field name or 'fieldName:id' string

## Return value

- `bool|Field` Returns false or field inherited from

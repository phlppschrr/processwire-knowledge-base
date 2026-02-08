# $inputfieldTinyMCETools->getPasteFiltersForJS(): string

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCETools.php`

Prepare pasteFilters string for JS

This converts the rules to a longer format that is optimized for matching from the
InputfieldTinyMCE.js pasteProcess() function.

## Usage

~~~~~
// basic usage
$string = $inputfieldTinyMCETools->getPasteFiltersForJS();
~~~~~

## Return value

- `string`

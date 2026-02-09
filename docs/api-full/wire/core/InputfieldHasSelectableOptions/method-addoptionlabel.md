# $inputfieldHasSelectableOptions->addOptionLabel($value, $label, $language = null): self|$this

Source: `wire/core/Interfaces.php`

Add selectable option with label, optionally for specific language

## Usage

~~~~~
// basic usage
$result = $inputfieldHasSelectableOptions->addOptionLabel($value, $label);

// usage with all arguments
$result = $inputfieldHasSelectableOptions->addOptionLabel($value, $label, $language = null);
~~~~~

## Arguments

- `$value` `string|int`
- `$label` `string`
- `$language` (optional) `Language|null`

## Return value

- `self|$this`

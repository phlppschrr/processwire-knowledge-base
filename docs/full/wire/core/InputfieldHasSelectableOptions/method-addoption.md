# $inputfieldHasSelectableOptions->addOption($value, $label = null, ?array $attributes = null): self|$this

Source: `wire/core/Interfaces.php`

Add a selectable option

## Usage

~~~~~
// basic usage
$result = $inputfieldHasSelectableOptions->addOption($value);

// usage with all arguments
$result = $inputfieldHasSelectableOptions->addOption($value, $label = null, ?array $attributes = null);
~~~~~

## Arguments

- `$value` `string|int`
- `$label` (optional) `string|null`
- `$attributes` (optional) `array|null`

## Return value

- `self|$this`

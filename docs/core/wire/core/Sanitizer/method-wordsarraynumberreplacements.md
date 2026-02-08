# $sanitizer->wordsArrayNumberReplacements(&$value, $prefix = 'REP'): array

Source: `wire/core/Sanitizer.php`

Identify decimals, minus signs and commas in numbers, replace them, and return the replacements array

## Usage

~~~~~
// basic usage
$array = $sanitizer->wordsArrayNumberReplacements($value);

// usage with all arguments
$array = $sanitizer->wordsArrayNumberReplacements(&$value, $prefix = 'REP');
~~~~~

## Arguments

- `$value` `string`
- `$prefix` (optional) `string`

## Return value

- `array`

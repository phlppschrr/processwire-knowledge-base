# $field->setLabel($text, $language = null)

Source: `wire/core/Field.php`

Set label, optionally for a specific language

## Usage

~~~~~
// basic usage
$result = $field->setLabel($text);

// usage with all arguments
$result = $field->setLabel($text, $language = null);
~~~~~

## Arguments

- `$text` `string` Text to set
- `$language` (optional) `Language|string|int|null` Language to use

## Since

3.0.16 Added for consistency, all versions can still set property directly.

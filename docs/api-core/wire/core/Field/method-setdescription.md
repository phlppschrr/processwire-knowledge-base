# $field->setDescription($text, $language = null)

Source: `wire/core/Field.php`

Set description, optionally for a specific language

## Usage

~~~~~
// basic usage
$result = $field->setDescription($text);

// usage with all arguments
$result = $field->setDescription($text, $language = null);
~~~~~

## Arguments

- `$text` `string` Text to set
- `$language` (optional) `Language|string|int|null` Language to use

## Since

3.0.16 Added for consistency, all versions can still set property directly.

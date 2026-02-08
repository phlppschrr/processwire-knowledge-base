# $field->getLabel($language = null): string

Source: `wire/core/Field.php`

Get field label for current language, or another specified language.

This is different from `$field->label` in that it knows about languages (when installed).

## Usage

~~~~~
// basic usage
$string = $field->getLabel();

// usage with all arguments
$string = $field->getLabel($language = null);
~~~~~

## Arguments

- `$language` (optional) `Page|Language` Optionally specify a language. If not specified user's current language is used.

## Return value

- `string`

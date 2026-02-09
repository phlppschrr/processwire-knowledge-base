# $field->getNotes($language = null): string

Source: `wire/core/Field.php`

Return field notes for current language, or another specified language.

This is different from `$field->notes` in that it knows about languages (when installed).

## Usage

~~~~~
// basic usage
$string = $field->getNotes();

// usage with all arguments
$string = $field->getNotes($language = null);
~~~~~

## Arguments

- `$language` (optional) `Page|Language` Optionally specify a language. If not specified user's current language is used.

## Return value

- `string`

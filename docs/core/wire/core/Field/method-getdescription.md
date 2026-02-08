# $field->getDescription($language = null): string

Source: `wire/core/Field.php`

Return field description for current language, or another specified language.

This is different from `$field->description` in that it knows about languages (when installed).

## Arguments

- `$language` (optional) `Page|Language` Optionally specify a language. If not specified user's current language is used.

## Return value

string

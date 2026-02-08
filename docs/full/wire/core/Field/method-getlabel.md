# Field::getLabel()

Source: `wire/core/Field.php`

Get field label for current language, or another specified language.

This is different from `$field->label` in that it knows about languages (when installed).


@param Page|Language $language Optionally specify a language. If not specified user's current language is used.

@return string

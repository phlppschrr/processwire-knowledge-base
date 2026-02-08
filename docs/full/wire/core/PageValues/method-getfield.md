# PageValues::getField()

Source: `wire/core/PageValues.php`

Get a Field object in context or NULL if not valid for this page

Field in context is only returned when output formatting is on.


@param Page $page

@param string|int|Field $field

@return Field|null

@todo determine if we can always retrieve in context regardless of output formatting.

# Fieldgroup::get()

Source: `wire/core/Fieldgroup.php`

Get a Fieldgroup property or a Field.

It is preferable to use `Fieldgroup::getField()` to retrieve fields from the Fieldgroup because
the scope of this `get()` method means it can return more than just Field object.


@param string|int $key Property name to retrieve, or Field name

@return Field|string|int|null|array

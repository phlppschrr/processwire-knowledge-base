# Fieldgroup::softRemove()

Source: `wire/core/Fieldgroup.php`

Remove a field without queueing it to be removed from database

Removes a field from the fieldgroup without deleting any associated field data when fieldgroup
is saved to the database. This is useful in the API when you want to move a field around within
a fieldgroup, like when moving a field to a Fieldset within the Fieldgroup.


@param Field|string|int $field Field object, name or id.

@return bool|Fieldgroup|WireArray

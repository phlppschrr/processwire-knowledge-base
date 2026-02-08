# $fieldtype->___deleteField(Field $field): bool

Source: `wire/core/Fieldtype.php`

Delete the given field, which implies: drop the table used by the field.

This should only be called by the `Fields` class since `fieldgroups_fields` lookup entries must be
deleted before this method is called.

## Arguments

- `$field` `Field` Field object

## Return value

bool True on success, false on DB delete failure.

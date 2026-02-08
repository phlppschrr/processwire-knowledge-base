# $field->setRoles($type, $roles)

Source: `wire/core/Field.php`

Set the roles that are allowed to view or edit this field on pages.

Applicable only if the `Field::flagAccess` is set to this field's flags.

## Arguments

- `$type` `string` Must be either "view" or "edit"
- `$roles` `PageArray|array|null` May be a PageArray of Role objects or an array of Role IDs.

## Throws

- WireException if given invalid argument

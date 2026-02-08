# Field::setRoles()

Source: `wire/core/Field.php`

Set the roles that are allowed to view or edit this field on pages.

Applicable only if the `Field::flagAccess` is set to this field's flags.


@param string $type Must be either "view" or "edit"

@param PageArray|array|null $roles May be a PageArray of Role objects or an array of Role IDs.

@throws WireException if given invalid argument

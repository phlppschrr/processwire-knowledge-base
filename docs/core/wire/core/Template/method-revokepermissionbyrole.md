# Template::revokePermissionByRole()

Source: `wire/core/Template.php`

Revoke a permission that applies to users having a specific role with pages using this template

Note that the change is not committed until you save() the template.

@param Permission|int|string $permission Permission object, name, or id

@param Role|int|string $role Role object, name or id

@param bool $test Specify true to only test if an update would be made, without changing anything

@return bool Returns true if an update was made (or would be made), false if not

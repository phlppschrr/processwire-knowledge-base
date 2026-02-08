# Role

Source: `wire/core/Role.php`

ProcessWire Role Page

Role is a type of Page used for grouping permissions to users.
Any given User will have one or more roles, each with zero or more permissions assigned to it.
Note that most public API-level access checking is typically performed from the User rather than
the Role(s), as it accounts for the combined roles. Please also see `User`, `Permission` and the
access related methods on `Page`.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property PageArray $permissions PageArray of permissions assigned to Role.

@property string $name Name of role.

@property int $id Numeric page ID of role.

## __construct()

Create a new Role page in memory.

@param Template|null $tpl

## wired()

Wired to API

## getPredefinedTemplate()

Get predefined template (template method)

@return Template

## getPredefinedParent()

Get predefined parent page (template method)

@return Page

## hasPermission()

Does this role have the given permission name, id or object?

@param string|int|Permission $permission Permission object, name, or id.

@param Page|Template|null $context Optional Page or Template context.

@return bool

@see User::hasPermission()

## hasPermissionContext()

Return whether the role has the permission within the context of a Page or Template

@param bool $has Result from the hasPermission() method

@param Permission $permission Permission to check

@param Wire $context Must be a Template or Page

@return bool

## addPermission()

Add the given Permission string, id or object.

This is the same as `$role->permissions->add($permission)` except this one will accept ID or name.

@param string|int|Permission $permission Permission object, name or id.

@return bool Returns false if permission not recognized, true otherwise

## removePermission()

Remove the given permission string, id or object.

This is the same as `$role->permissions->remove($permission)` except this one will accept ID or name.

@param string|int|Permission $permission Permission object, name or id.

@return bool false if permission not recognized, true otherwise

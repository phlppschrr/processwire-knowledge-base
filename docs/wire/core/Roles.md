# Roles

Source: `wire/core/Roles.php`

The Roles class serves as the $roles API variable.

Provides management of all Role pages for access control.

## other

@method PageArray find($selector) Return the Role(s) matching the the given selector.

@method Role add($name) Add new Role with the given name and return it.

@method bool save(Role $role) Save given role.

@method bool delete(Role $role) Delete the given role.

@method array saveReady(Page $page) Hook called just before a Role is saved

@method void saved(Page $page, array $changes = [], $values = []) Hook called after a role has been saved

@method void added(Page $page) Hook called just after a Role is added

@method void deleteReady(Page $page) Hook called before a Role is deleted

@method void deleted(Page $page) Hook called after a Role is deleted

@method Role new($options = []) Create new Role instance in memory (3.0.249+)

## get()

Get a Role by name, numeric ID or selector

@param string $selectorString Role name or selector

@return Role|NullPage|null

## ___save()

Save a Role


@param Role|Page $page

@return bool True on success, false on failure

@throws WireException

## ___delete()

Permanently delete a Role


@param Role|Page $page Permission to delete

@param bool $recursive If set to true, then this will attempt to delete any pages below the Permission too.

@return bool True on success, false on failure

@throws WireException

## ___add()

Add a new Role with the given name and return it


@param string $name Name of role you want to add, i.e. "hello-world"

@return Role|NullPage Returns a Role page on success, or a NullPage on error

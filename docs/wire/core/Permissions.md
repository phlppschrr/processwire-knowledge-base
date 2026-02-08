# Permissions

Source: `wire/core/Permissions.php`

The Permissions class serves as the $permissions API variable.

Provides management of all Permission pages independent of users, for access control.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method PageArray find($selector) Return the permissions(s) matching the the given selector query.

@method Permission|NullPage get($selector) Return permission by given name, numeric ID or a selector string.

@method array saveReady(Page $page) Hook called just before a Permission is saved

@method void saved(Page $page, array $changes = array(), $values = [])

@method void added(Page $page) Hook called just after a Permission is added

@method void deleteReady(Page $page) Hook called before a Permission is deleted

@method void deleted(Page $page) Hook called after a permission is deleted

@method Permission new($options = []) Create new Permission instance in memory (3.0.249+)

## has()

Does the system have a permission with the given name?

~~~~~
// Check if page-publish permission is available
if($permissions->has('page-publish')) {
  // system has the page-publish permission installed
}
~~~~~

@param string $name Name of permission

@return bool True if system has a permission with this name, or false if not.

## ___save()

Save a Permission


@param Permission|Page $page

@return bool True on success, false on failure

@throws WireException

## ___delete()

Permanently delete a Permission


@param Permission|Page $page Permission to delete

@param bool $recursive If set to true, then this will attempt to delete any pages below the Permission too.

@return bool True on success, false on failure

@throws WireException

## ___add()

Add a new Permission with the given name and return it


@param string $name Name of permission you want to add, i.e. "hello-world"

@return Permission|NullPage Returns a Permission page on success, or a NullPage on error

## getReducerPermissions()

Get permission names that can reduce existing access, when installed

Returned permission names that end with a "-" indicate that given permission name is a prefix
that applies for anything that appears after it.

@return array Array of permission names where both index and value are permission name

## getIterator()

Returns all installed Permission pages and enables foreach() iteration of $permissions

~~~~~
// Example of listing all permissions
foreach($permissions as $permission) {
  echo "<li>$permission->name</li>";
}
~~~~~

@return array|PageArray|\Traversable

## ___saved()

Hook called when a permission is saved


@param Page $page Page that was saved

@param array $changes Array of changed field names

@param array $values Array of changed field values indexed by name (when enabled)

@throws WireException

## ___deleted()

Hook called when a permission is deleted


@param Page $page Page that was deleted

@throws WireException

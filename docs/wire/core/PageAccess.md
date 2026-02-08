# PageAccess

Source: `wire/core/PageAccess.php`

ProcessWire Page Access

Provides implementation for Page access functions.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## getType()

Normalize a permission name type

Converts things like 'page-view' to 'view', and more.

@param string|int|Permission $name

@return string

## getAccessParent()

Returns the parent page that has the template from which we get our role/access settings from

@param Page $page

@param string $type Type, one of 'view', 'edit', 'create' or 'add' (default='view')

@param int $level Recursion level for internal use only

@return Page|NullPage Returns NullPage if none found

## getAccessTemplate()

Returns the template from which we get our role/access settings from

@param Page $page

@param string $type Type, one of 'view', 'edit', 'create' or 'add' (default='view')

@return Template|null Returns null if none

## getAccessRoles()

Return the PageArray of roles that have access to this page

This is determined from the page's template. If the page's template has roles turned off,
then it will go down the tree till it finds usable roles to use.

@param Page $page

@param string $type Default is 'view', but you may specify 'edit', 'create' or 'add' to retrieve that type

@return PageArray

## hasAccessRole()

Returns whether this page has the given access role

Given access role may be a role name, role ID or Role object

@param Page $page

@param string|int|Role $role

@param string $type Default is 'view', but you may specify 'create' or 'add' as well

@return bool

## wire()

Get or inject a ProcessWire API variable or fuel a new object instance

See Wire::wire() for explanation of all options.

@param string|WireFuelable $name Name of API variable to retrieve, set, or omit to retrieve entire Fuel object.

@param null|mixed $value Value to set if using this as a setter, otherwise omit.

@param bool $lock When using as a setter, specify true if you want to lock the value from future changes (default=false)

@return mixed|Fuel

@throws WireException

## setWire()

Set the ProcessWire instance

@param ProcessWire $wire

## getWire()

Get the ProcessWire instance

@return ProcessWire

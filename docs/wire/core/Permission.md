# Permission

Source: `wire/core/Permission.php`

ProcessWire Permission Page

Permission is a Page type used for storing an individual permission.
One or more Permission objects are attached to `Role` objects, which are then attached to `User` objects
and `Template` objects, forming ProcessWire's role-based access control system. Outside of roles,
Permission objects are managed with the `$permissions` API variable.


ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property int $id Numeric page ID of the permission.

@property string $name Name of the permission.

@property string $title Short description of what the permission is for.

## __construct()

Create a new Permission page in memory.

@param Template|null $tpl Template object this page should use.

## wired()

Wired to API

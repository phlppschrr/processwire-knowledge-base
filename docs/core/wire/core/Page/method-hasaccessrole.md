# $page->hasAccessRole($role, $type = 'view'): bool

Source: `wire/core/Page.php`

Returns whether this page has the given access role

Given access role may be a role name, role ID or Role object.

## Usage

~~~~~
// basic usage
$bool = $page->hasAccessRole($role);

// usage with all arguments
$bool = $page->hasAccessRole($role, $type = 'view');
~~~~~

## Arguments

- `$role` `string|int|Role`
- `$type` (optional) `string` May be 'view', 'edit', 'create' or 'add' (default is 'view')

## Return value

- `bool`

# $permissions->getReducerPermissions(): array

Source: `wire/core/Permissions.php`

Get permission names that can reduce existing access, when installed

Returned permission names that end with a "-" indicate that given permission name is a prefix
that applies for anything that appears after it.

## Usage

~~~~~
// basic usage
$array = $permissions->getReducerPermissions();
~~~~~

## Return value

- `array` Array of permission names where both index and value are permission name

# $pageAccess->getType($name): string

Source: `wire/core/PageAccess.php`

Normalize a permission name type

Converts things like 'page-view' to 'view', and more.

## Usage

~~~~~
// basic usage
$string = $pageAccess->getType($name);
~~~~~

## Arguments

- `$name` `string|int|Permission`

## Return value

- `string`

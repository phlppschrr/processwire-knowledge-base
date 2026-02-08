# $pageAccess->getAccessParent(Page $page, $type = 'view', $level = 0): Page|NullPage

Source: `wire/core/PageAccess.php`

Returns the parent page that has the template from which we get our role/access settings from

## Usage

~~~~~
// basic usage
$page = $pageAccess->getAccessParent($page);

// usage with all arguments
$page = $pageAccess->getAccessParent(Page $page, $type = 'view', $level = 0);
~~~~~

## Arguments

- `$page` `Page`
- `$type` (optional) `string` Type, one of 'view', 'edit', 'create' or 'add' (default='view')
- `$level` (optional) `int` Recursion level for internal use only

## Return value

- `Page|NullPage` Returns NullPage if none found

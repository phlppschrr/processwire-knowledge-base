# $pageAccess->getAccessParent(Page $page, $type = 'view', $level = 0): Page|NullPage

Source: `wire/core/PageAccess.php`

Returns the parent page that has the template from which we get our role/access settings from

## Arguments

- Page $page
- string $type Type, one of 'view', 'edit', 'create' or 'add' (default='view')
- int $level Recursion level for internal use only

## Return value

Page|NullPage Returns NullPage if none found

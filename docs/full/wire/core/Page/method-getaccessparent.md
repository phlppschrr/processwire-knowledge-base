# $page->getAccessParent($type = 'view'): Page|NullPage

Source: `wire/core/Page.php`

Returns the page from which role/access settings are inherited from

## Arguments

- string $type Optionally specify one of 'view', 'edit', 'add', or 'create' (default='view')

## Return value

Page|NullPage Returns NullPage if none found

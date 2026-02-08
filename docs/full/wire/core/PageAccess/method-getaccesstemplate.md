# $pageAccess->getAccessTemplate(Page $page, $type = 'view'): Template|null

Source: `wire/core/PageAccess.php`

Returns the template from which we get our role/access settings from

## Arguments

- Page $page
- string $type Type, one of 'view', 'edit', 'create' or 'add' (default='view')

## Return value

Template|null Returns null if none

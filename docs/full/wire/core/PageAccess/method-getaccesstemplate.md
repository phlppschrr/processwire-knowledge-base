# $pageAccess->getAccessTemplate(Page $page, $type = 'view'): Template|null

Source: `wire/core/PageAccess.php`

Returns the template from which we get our role/access settings from

## Usage

~~~~~
// basic usage
$template = $pageAccess->getAccessTemplate($page);

// usage with all arguments
$template = $pageAccess->getAccessTemplate(Page $page, $type = 'view');
~~~~~

## Arguments

- `$page` `Page`
- `$type` (optional) `string` Type, one of 'view', 'edit', 'create' or 'add' (default='view')

## Return value

- `Template|null` Returns null if none

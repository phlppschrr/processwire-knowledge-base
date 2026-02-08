# $page->getAccessTemplate($type = 'view'): Template|null

Source: `wire/core/Page.php`

Returns the template from which role/access settings are inherited from

## Usage

~~~~~
// basic usage
$template = $page->getAccessTemplate();

// usage with all arguments
$template = $page->getAccessTemplate($type = 'view');
~~~~~

## Arguments

- `$type` (optional) `string` Optionally specify one of 'view', 'edit', 'add', or 'create' (default='view')

## Return value

- `Template|null` Returns Template object or NULL if none

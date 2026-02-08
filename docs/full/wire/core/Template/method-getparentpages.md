# $template->getParentPages($checkAccess = false): PageArray

Source: `wire/core/Template.php`

Return all defined parent pages for this template

## Usage

~~~~~
// basic usage
$items = $template->getParentPages();

// usage with all arguments
$items = $template->getParentPages($checkAccess = false);
~~~~~

## Arguments

- `$checkAccess` (optional) `bool` Specify true to exclude parents that user doesn't have access to add children to (default=false)

## Return value

- `PageArray`

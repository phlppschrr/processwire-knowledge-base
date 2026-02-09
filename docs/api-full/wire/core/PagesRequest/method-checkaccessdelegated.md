# $pagesRequest->checkAccessDelegated(Page $page): Page|null|bool

Source: `wire/core/PagesRequest.php`

Check access to a delegated page (like a repeater)

Note: this should move to PagePermissions.module or FieldtypeRepeater.module
if a similar check is needed somewhere else in the core.

## Usage

~~~~~
// basic usage
$page = $pagesRequest->checkAccessDelegated($page);

// usage with all arguments
$page = $pagesRequest->checkAccessDelegated(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `Page|null|bool`

# $page->moveable($newParent = null): bool

Source: `wire/core/Page.php`

Returns true if the current user can move this page. Optionally specify the new parent to check if the page is moveable to that parent.

## Usage

~~~~~
// basic usage
$bool = $page->moveable();

// usage with all arguments
$bool = $page->moveable($newParent = null);
~~~~~

# $page->trashable($orDeleteable = false): bool

Source: `wire/core/Page.php`

Returns true if the page is trashable by the current user, false if not.

## Usage

~~~~~
// basic usage
$bool = $page->trashable();

// usage with all arguments
$bool = $page->trashable($orDeleteable = false);
~~~~~

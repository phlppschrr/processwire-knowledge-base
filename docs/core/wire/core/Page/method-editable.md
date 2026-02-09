# $page->editable($field = '', $checkPageEditable = true): bool

Source: `wire/core/Page.php`

Returns true if the page (and optionally field) is editable by the current user, false if not.

## Usage

~~~~~
// basic usage
$bool = $page->editable();

// usage with all arguments
$bool = $page->editable($field = '', $checkPageEditable = true);
~~~~~

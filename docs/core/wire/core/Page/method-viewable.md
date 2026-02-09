# $page->viewable($field = '', $checkTemplateFile = true): bool

Source: `wire/core/Page.php`

Returns true if the page (and optionally field) is viewable by the current user, false if not.

## Usage

~~~~~
// basic usage
$bool = $page->viewable();

// usage with all arguments
$bool = $page->viewable($field = '', $checkTemplateFile = true);
~~~~~

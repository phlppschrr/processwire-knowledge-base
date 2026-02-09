# $page->addable($pageToAdd = null): bool

Source: `wire/core/Page.php`

Returns true if the current user can add children to the page, false if not. Optionally specify the page to be added for additional access checking.

## Usage

~~~~~
// basic usage
$bool = $page->addable();

// usage with all arguments
$bool = $page->addable($pageToAdd = null);
~~~~~

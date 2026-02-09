# $page->cloneable($recursive = null): bool

Source: `wire/core/Page.php`

Can current user clone this page? Specify false for $recursive argument to ignore whether children are cloneable. @since 3.0.239

## Usage

~~~~~
// basic usage
$bool = $page->cloneable();

// usage with all arguments
$bool = $page->cloneable($recursive = null);
~~~~~

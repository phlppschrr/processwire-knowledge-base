# $page->__construct(?Template $tpl = null)

Source: `wire/core/Page.php`

Create a new page in memory.

## Usage

~~~~~
// basic usage
$result = $page->__construct();

// usage with all arguments
$result = $page->__construct(?Template $tpl = null);
~~~~~

## Arguments

- `$tpl` (optional) `Template|null` Template object this page should use.

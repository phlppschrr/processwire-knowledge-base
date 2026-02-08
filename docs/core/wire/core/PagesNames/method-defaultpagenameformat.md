# $pagesNames->defaultPageNameFormat(Page $page, array $options = array()): string

Source: `wire/core/PagesNames.php`

Get the name format string that should be used for given $page if no name was assigned

## Usage

~~~~~
// basic usage
$string = $pagesNames->defaultPageNameFormat($page);

// usage with all arguments
$string = $pagesNames->defaultPageNameFormat(Page $page, array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `fallbackFormat` (string): Fallback format if another cannot be determined (default='untitled-time'). - `parent` (Page|null): Optional parent page to use instead of $page->parent (default=null).

## Return value

- `string`

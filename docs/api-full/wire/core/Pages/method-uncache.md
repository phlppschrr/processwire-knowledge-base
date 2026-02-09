# $pages->uncache($page = null, array $options = array()): int

Source: `wire/core/Pages.php`

Remove the given page(s) from the cache, or uncache all by omitting $page argument

When no $page argument is given, this method behaves the same as `$pages->uncacheAll()`.
When any $page argument is given, this does not remove pages from selectorCache.

## Usage

~~~~~
// basic usage
$int = $pages->uncache();

// usage with all arguments
$int = $pages->uncache($page = null, array $options = array());
~~~~~

## Arguments

- `$page` (optional) `Page|PageArray|int|null` Page to uncache, PageArray of pages to uncache, ID of page to uncache (3.0.153+), or omit to uncache all.
- `$options` (optional) `array` Additional options to modify behavior: - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent that call, set this to true.

## Return value

- `int` Number of pages uncached

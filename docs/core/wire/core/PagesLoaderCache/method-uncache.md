# $pagesLoaderCache->uncache($page, array $options = array()): bool

Source: `wire/core/PagesLoaderCache.php`

Remove the given page from the cache.

Note: does not remove pages from selectorCache. Call uncacheAll to do that.

## Usage

~~~~~
// basic usage
$bool = $pagesLoaderCache->uncache($page);

// usage with all arguments
$bool = $pagesLoaderCache->uncache($page, array $options = array());
~~~~~

## Arguments

- `$page` `Page|int` Page to uncache or ID of page (prior to 3.0.153 only Page object was accepted)
- `$options` (optional) `array` Additional options to modify behavior: - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent call to $page->uncache(), set 'shallow' => true.

## Return value

- `bool` True if page was uncached, false if it didn't need to be

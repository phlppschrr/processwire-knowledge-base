# $pagesLoaderCache->uncache($page, array $options = array()): bool

Source: `wire/core/PagesLoaderCache.php`

Remove the given page from the cache.

Note: does not remove pages from selectorCache. Call uncacheAll to do that.

## Arguments

- Page|int $page Page to uncache or ID of page (prior to 3.0.153 only Page object was accepted)
- array $options Additional options to modify behavior: - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent call to $page->uncache(), set 'shallow' => true.

## Return value

bool True if page was uncached, false if it didn't need to be

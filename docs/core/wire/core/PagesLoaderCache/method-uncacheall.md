# $pagesLoaderCache->uncacheAll(?Page $page = null, array $options = array()): int

Source: `wire/core/PagesLoaderCache.php`

Remove all pages from the cache

## Arguments

- Page|null $page Optional Page that initiated the uncacheAll
- array $options Additional options to modify behavior: - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent call to $page->uncache(), set 'shallow' => true.

## Return value

int Number of pages uncached

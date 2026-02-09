# PagesLoaderCache

Source: `wire/core/PagesLoaderCache.php`

Inherits: `Wire`

ProcessWire Pages Loader Cache

Pages Loader Cache
$pages->cacher
Implements page caching of loaded pages and PageArrays for $pages API variable

Methods:
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`getCacheStatus(bool|null $verbose = null): array|string`](method-getcachestatus.md) Get cache status
- [`getCache(int|string|null $id = null): Page|array|null`](method-getcache.md) Given a Page ID, return it if it's cached, or NULL of it's not.
- [`hasCache($id): bool`](method-hascache.md) Is given page ID in the cache?
- [`cache(Page $page): void`](method-cache.md) Cache the given page in memory
- [`cacheGroup(Page $page, string $groupName)`](method-cachegroup.md) Cache given page into a named group that it can be uncached with
- [`uncache(Page|int $page, array $options = array()): bool`](method-uncache.md) Remove the given page from the cache.
- [`uncacheAll(?Page $page = null, array $options = array()): int`](method-uncacheall.md) Remove all pages from the cache
- [`uncacheGroup(string $groupName, array $options = array()): int`](method-uncachegroup.md) Uncache pages that were cached with given group name
- [`selectorCache(string $selector, array $options, PageArray $pages): bool`](method-selectorcache.md) Cache the given selector string and options with the given PageArray
- [`optionsArrayToString(array $options): string`](method-optionsarraytostring.md) Convert an options array to a string
- [`getSelectorCache(string $selector, array $options, bool $returnSelector = false): array|null|string|PageArray`](method-getselectorcache.md) Retrieve any cached page IDs for the given selector and options OR false if none found.

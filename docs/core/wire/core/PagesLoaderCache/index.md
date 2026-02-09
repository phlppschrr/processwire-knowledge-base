# PagesLoaderCache

Source: `wire/core/PagesLoaderCache.php`

Inherits: `Wire`

ProcessWire Pages Loader Cache

Pages Loader Cache
$pages->cacher
Implements page caching of loaded pages and PageArrays for $pages API variable

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`getCacheStatus(bool|null $verbose = null): array|string`](method-getcachestatus.md)
- [`getCache(int|string|null $id = null): Page|array|null`](method-getcache.md)
- [`hasCache($id): bool`](method-hascache.md)
- [`cache(Page $page): void`](method-cache.md)
- [`cacheGroup(Page $page, string $groupName)`](method-cachegroup.md)
- [`uncache(Page|int $page, array $options = array()): bool`](method-uncache.md)
- [`uncacheAll(?Page $page = null, array $options = array()): int`](method-uncacheall.md)
- [`uncacheGroup(string $groupName, array $options = array()): int`](method-uncachegroup.md)
- [`selectorCache(string $selector, array $options, PageArray $pages): bool`](method-selectorcache.md)
- [`optionsArrayToString(array $options): string`](method-optionsarraytostring.md)
- [`getSelectorCache(string $selector, array $options, bool $returnSelector = false): array|null|string|PageArray`](method-getselectorcache.md)

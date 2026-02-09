# WireCache

Source: `wire/core/WireCache.php`

Inherits: `Wire`

ProcessWire WireCache

Simple cache for storing strings (encoded or otherwise) and serves as $cache API var


Provides easy, persistent caching of markup, strings, arrays or PageArray objects.
~~~~~
// Get a cache named 'foo' that lasts for 1 hour (aka 3600 seconds)
$value = $cache->get('foo', 3600, function() {
  // this is called if cache expired or does not exist,
  // so generate a new cache value here and return it
  return "This is the cached value";
});
~~~~~

Methods:
- [`cacher(): WireCacheInterface`](method-cacher.md) Get the current WireClassInterface instance
- [`preload(array $names, int|string|null $expire = null)`](method-preload.md) Preload the given caches, so that they will be returned without query on the next get() call
- [`preloadFor(object|string $ns, int|string|null $expire = null)`](method-preloadfor.md) Preload all caches for the given object or namespace
- [`get(string|array $name, int|string|null|false $expire = null, callable $func = null): string|array|PageArray|mixed|null`](method-get.md) Get data from cache with given name
- [`renderCacheValue(string $name, int|string|null $expire, callable $func): bool|string`](method-rendercachevalue.md) Render and save a cache value, when given a function to do so
- [`getFor(string|object $ns, string $name, null|int|string $expire = null, callable|null $func = null): string|array|PageArray|mixed|null`](method-getfor.md) Same as get() but with namespace
- [`save(string $name, string|array|PageArray $data, int|string|Page $expire = self::expireDaily): bool`](method-save.md) Save data to cache with given name
- [`saveFor(string|object $ns, string $name, string|array|PageArray $data, int|Page $expire = self::expireDaily): bool`](method-savefor.md) Same as save() except with namespace
- [`delete(string $name): bool`](method-delete.md) Delete/clear the cache(s) identified by given name or wildcard
- [`deleteAll(): int`](method-deleteall.md) Delete all caches (where allowed)
- [`expireAll(): int`](method-expireall.md) Deletes all caches that have expiration dates (only)
- [`deleteFor(string $ns, string $name = ''): bool`](method-deletefor.md) Delete one or more caches in a given namespace
- [`maintenance($obj = null): bool`](method-maintenance.md) Cache maintenance removes expired caches
- [`maintenanceGeneral(): bool`](method-maintenancegeneral.md) General maintenance removes expired caches
- [`maintenancePage(Page $page): bool`](method-maintenancepage.md) Run maintenance for a page that was just saved or deleted
- [`maintenanceTemplate(Template $template): bool`](method-maintenancetemplate.md) Run maintenance for a template that was just saved or deleted
- [`arrayToPageArray(array $data): PageArray`](method-arraytopagearray.md) Convert a cacheable array to a PageArray
- [`pageArrayToArray(PageArray $items): array`](method-pagearraytoarray.md) Given a PageArray, convert it to a cachable array
- [`getInfo(bool $verbose = true, array|string $names = array(), array|string $exclude = array(), array $cols = array()): array`](method-getinfo.md) Get information about all the caches in this WireCache
- [`renderFile(string $filename, int|Page|string|null $expire = null, array $options = array()): string|bool`](method-renderfile.md) Render a file as a ProcessWire template file and cache the output
- [`setCacheModule(WireCacheInterface $module)`](method-setcachemodule.md) Set WireCache module to use for caching
- [`getCacheModule(): WireCacheInterface`](method-getcachemodule.md) Get WireCache module that is currently being used

Constants:
- [`defaultCacheClass`](const-defaultcacheclass.md)
- [`expireNever`](const-expirenever.md)
- [`expireNever`](const-expirenever.md)
- [`expireReserved`](const-expirereserved.md)
- [`expireSave`](const-expiresave.md)
- [`expireNow`](const-expirenow.md)
- [`expireHourly`](const-expirehourly.md)
- [`expireDaily`](const-expiredaily.md)
- [`expireWeekly`](const-expireweekly.md)
- [`expireMonthly`](const-expiremonthly.md)
- [`expireIgnore`](const-expireignore.md)

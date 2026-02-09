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
- [`cacher(): WireCacheInterface`](method-cacher.md)
- [`preload(array $names, int|string|null $expire = null)`](method-preload.md)
- [`preloadFor(object|string $ns, int|string|null $expire = null)`](method-preloadfor.md)
- [`get(string|array $name, int|string|null|false $expire = null, callable $func = null): string|array|PageArray|mixed|null`](method-get.md)
- [`renderCacheValue(string $name, int|string|null $expire, callable $func): bool|string`](method-rendercachevalue.md)
- [`getFor(string|object $ns, string $name, null|int|string $expire = null, callable|null $func = null): string|array|PageArray|mixed|null`](method-getfor.md)
- [`save(string $name, string|array|PageArray $data, int|string|Page $expire = self::expireDaily): bool`](method-save.md)
- [`saveFor(string|object $ns, string $name, string|array|PageArray $data, int|Page $expire = self::expireDaily): bool`](method-savefor.md)
- [`delete(string $name): bool`](method-delete.md)
- [`deleteAll(): int`](method-deleteall.md)
- [`expireAll(): int`](method-expireall.md)
- [`deleteFor(string $ns, string $name = ''): bool`](method-deletefor.md)
- [`maintenance($obj = null): bool`](method-maintenance.md)
- [`maintenanceGeneral(): bool`](method-maintenancegeneral.md)
- [`maintenancePage(Page $page): bool`](method-maintenancepage.md)
- [`maintenanceTemplate(Template $template): bool`](method-maintenancetemplate.md)
- [`arrayToPageArray(array $data): PageArray`](method-arraytopagearray.md)
- [`pageArrayToArray(PageArray $items): array`](method-pagearraytoarray.md)
- [`getInfo(bool $verbose = true, array|string $names = array(), array|string $exclude = array(), array $cols = array()): array`](method-getinfo.md)
- [`renderFile(string $filename, int|Page|string|null $expire = null, array $options = array()): string|bool`](method-renderfile.md)
- [`setCacheModule(WireCacheInterface $module)`](method-setcachemodule.md)
- [`getCacheModule(): WireCacheInterface`](method-getcachemodule.md)

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

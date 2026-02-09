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
Method: [cacher()](method-cacher.md)
Method: [preload()](method-preload.md)
Method: [preloadFor()](method-preloadfor.md)
Method: [get()](method-get.md)
Method: [renderCacheValue()](method-rendercachevalue.md)
Method: [getFor()](method-getfor.md)
Method: [save()](method-save.md)
Method: [saveFor()](method-savefor.md)
Method: [delete()](method-delete.md)
Method: [deleteAll()](method-deleteall.md)
Method: [expireAll()](method-expireall.md)
Method: [deleteFor()](method-deletefor.md)
Method: [maintenance()](method-maintenance.md)
Method: [maintenanceGeneral()](method-maintenancegeneral.md)
Method: [maintenancePage()](method-maintenancepage.md)
Method: [maintenanceTemplate()](method-maintenancetemplate.md)
Method: [arrayToPageArray()](method-arraytopagearray.md)
Method: [pageArrayToArray()](method-pagearraytoarray.md)
Method: [getInfo()](method-getinfo.md)
Method: [renderFile()](method-renderfile.md)
Method: [setCacheModule()](method-setcachemodule.md)
Method: [getCacheModule()](method-getcachemodule.md)

Constants:
Const: [defaultCacheClass](const-defaultcacheclass.md)
Const: [expireNever](const-expirenever.md)
Const: [expireNever](const-expirenever.md)
Const: [expireReserved](const-expirereserved.md)
Const: [expireSave](const-expiresave.md)
Const: [expireNow](const-expirenow.md)
Const: [expireHourly](const-expirehourly.md)
Const: [expireDaily](const-expiredaily.md)
Const: [expireWeekly](const-expireweekly.md)
Const: [expireMonthly](const-expiremonthly.md)
Const: [expireIgnore](const-expireignore.md)

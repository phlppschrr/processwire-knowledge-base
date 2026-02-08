# WireCache

Source: `wire/core/WireCache.php`

ProcessWire WireCache

Simple cache for storing strings (encoded or otherwise) and serves as $cache API var

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

Provides easy, persistent caching of markup, strings, arrays or PageArray objects.
These constants are used for the `$expire` argument of get() and save() cache methods.
~~~~~
// Get a cache named 'foo' that lasts for 1 hour (aka 3600 seconds)
$value = $cache->get('foo', 3600, function() {
  // this is called if cache expired or does not exist,
  // so generate a new cache value here and return it
  return "This is the cached value";
});
~~~~~

## defaultCacheClass

Default cache class

## expireNever

Expiration constants that may be supplied to WireCache::save $seconds argument.

## expireNever

Cache should never expire (unless manually cleared).

## expireReserved

Cache should never expire and should not be deleted during deleteAll() calls (for PW internal system use)
Can only be deleted by delete() calls that specify it directly or match it specifically with a wildcard.

## expireSave

Cache should expire when a given resource (Page or Template) is saved.

## expireNow

Cache should expire now

## expireHourly

Cache should expire once per hour

## expireDaily

Cache should expire once per day

## expireWeekly

Cache should expire once per week

## expireMonthly

Cache should expire once per month

## expireIgnore

Ignore expiration (skips expiration check) 3.0.218+

## cacher()

Get the current WireClassInterface instance

@return WireCacheInterface

## preload()

Preload the given caches, so that they will be returned without query on the next get() call

After a preloaded cache is returned from a get() call, it is removed from local storage.


@param array $names

@param int|string|null $expire

@deprecated

## preloadFor()

Preload all caches for the given object or namespace


@param object|string $ns

@param int|string|null $expire

@deprecated

## get()

Get data from cache with given name

Optionally specify expiration time and/or a cache generation function to use when cache needs to be created.

Cached value can be a string, an array of non-object values, or a PageArray.

~~~~~
// get single cache value
$str = $cache->get('foo');

// get 3 cached values, returns associative array with foo, bar, baz indexes
$array = $cache->get([ 'foo', 'bar', 'baz' ]);

// get all cache values with names starting with “hello”
$array = $cache->get('hello*');

// get cache only if it’s less than or equal to 1 hour old (3600 seconds)
$str = $cache->get('foo', 3600);

// same as above, but also generates the cache value with function when expired
$str = $cache->get('foo', 3600, function() {
  return "This is the cached value";
});
~~~~~

@param string|array $name Provide a single cache name, an array of cache names, or an asterisk cache name.
- If given a single cache name (string) just the contents of that cache will be returned.
- If given an array of names, multiple caches will be returned, indexed by cache name.
- If given a cache name with an asterisk in it, it will return an array of all matching caches.

@param int|string|null|false $expire Optionally specify max age (in seconds) OR oldest date string, or false to ignore.
- If cache exists and is older, then null returned. You may omit this to divert to whatever expiration
  was specified at save() time. Note: The $expire and $func arguments may optionally be reversed.
- If using a $func, the behavior of $expire becomes the same as that of save().

@param callable $func Optionally provide a function/closure that generates the cache value and it
	will be used when needed. This option requires that only one cache is being retrieved (not an array of caches).
	Note: The $expire and $func arguments may optionally be reversed.

@return string|array|PageArray|mixed|null Returns null if cache doesn’t exist and no generation function provided.

@throws WireException if given invalid arguments

## renderCacheValue()

Render and save a cache value, when given a function to do so

Provided $func may specify any arguments that correspond with the names of API vars
and it will be sent those arguments.

Provided $func may either echo or return it's output. If any value is returned by
the function it will be used as the cache value. If no value is returned, then
the output buffer will be used as the cache value.

@param string $name

@param int|string|null $expire

@param callable $func

@return bool|string

@since 2.5.28

## getFor()

Same as get() but with namespace

Namespace is useful to avoid cache name collisions. The ProcessWire core commonly uses cache
namespace to bind cache values to the object class, which often make a good namespace.

Please see the `$cache->get()` method for usage of all arguments.

~~~~~
// specify namespace as a string
$value = $cache->getFor('my-namespace', 'my-cache-name');

// or specify namespace is an object instance
$value = $cache->get($this, 'my-cache-name');
~~~~~

@param string|object $ns Namespace

@param string $name Cache name

@param null|int|string $expire Optional expiration

@param callable|null $func Optional cache generation function

@return string|array|PageArray|mixed|null Returns null if cache doesn’t exist and no generation function provided.

@see WireCache::get()

## save()

Save data to cache with given name

~~~~~
$value = "This is the value that will be cached.";

// cache the value, using default expiration (daily)
$cache->save("my-cache-name", $value);

// cache the value, and expire after 1 hour (3600 seconds)
$cache->save("my-cache-name", $value, 3600);
~~~~~

@param string $name Name of cache, can be any string up to 255 chars

@param string|array|PageArray $data Data that you want to cache. May be string, array of non-object values, or PageArray.

@param int|string|Page $expire Lifetime of this cache, in seconds, OR one of the following:
 - Specify one of the `WireCache::expire*` constants.
 - Specify the future date you want it to expire (as unix timestamp or any `strtotime()` compatible date format)
 - Provide a `Page` object to expire when any page using that template is saved.
 - Specify `WireCache::expireNever` to prevent expiration.
 - Specify `WireCache::expireSave` to expire when any page or template is saved.
 - Specify selector string matching pages that–when saved–expire the cache.

@return bool Returns true if cache was successful, false if not

@throws WireException if given data that cannot be cached

## saveFor()

Same as save() except with namespace

Namespace is useful to avoid cache name collisions. The ProcessWire core commonly uses cache
namespace to bind cache values to the object class, which often make a good namespace.

~~~~~
// save cache using manually specified namespace
$cache->save("my-namespace", "my-cache-name", $value);

// save cache using namespace of current object
$cache->save($this, "my-cache-name", $value);
~~~~~

@param string|object $ns Namespace for cache

@param string $name Name of cache, can be any string up to 255 chars

@param string|array|PageArray $data Data that you want to cache

@param int|Page $expire Lifetime of this cache, in seconds, OR one of the following:
 - Specify one of the `WireCache::expire*` constants.
 - Specify the future date you want it to expire (as unix timestamp or any strtotime compatible date format)
 - Provide a `Page` object to expire when any page using that template is saved.
 - Specify `WireCache::expireNever` to prevent expiration.
 - Specify `WireCache::expireSave` to expire when any page or template is saved.
 - Specify selector string matching pages that, when saved, expire the cache.

@return bool Returns true if cache was successful, false if not

## delete()

Delete/clear the cache(s) identified by given name or wildcard

~~~~~
// Delete cache named "my-cache-name"
$cache->delete("my-cache-name");

// Delete all caches starting with "my-"
$cache->delete("my-*");
~~~~~

@param string $name Name of cache, or partial name with wildcard (i.e. "MyCache*") to clear multiple caches.

@return bool True on success, false if no cache was cleared

## deleteAll()

Delete all caches (where allowed)

This method deletes all caches other than those with `WireCache::expireReserved` status.

@return int Quantity of caches deleted

@since 3.0.130

## expireAll()

Deletes all caches that have expiration dates (only)

This method does not delete caches that are expired by saving of resources or matching selectors.

@return int

@since 3.0.130

## deleteFor()

Delete one or more caches in a given namespace

~~~~~
// Delete all in namespace
$cache->deleteFor("my-namespace");

// Delete one cache in namespace
$cache->deleteFor("my-namespace", "my-cache-name");
~~~~~

@param string $ns Namespace of cache.

@param string $name Name of cache. If none specified, all for namespace are deleted.

@return bool True on success, false on failure

## maintenance()

Cache maintenance removes expired caches

Should be called as part of a regular maintenance routine and after page/template save/deletion.
ProcessWire already calls this automatically, so you don’t typically need to call this method on your own.


@param Template|Page|null|bool Item to run maintenance for or, if not specified, general maintenance is performed.
	General maintenance only runs once per request. Specify boolean true to force general maintenance to run.

@return bool

## maintenanceGeneral()

General maintenance removes expired caches

@return bool

## maintenancePage()

Run maintenance for a page that was just saved or deleted

@param Page $page

@return bool

## maintenanceTemplate()

Run maintenance for a template that was just saved or deleted

@param Template $template

@return bool Returns true if any caches were deleted, false if not

## arrayToPageArray()

Convert a cacheable array to a PageArray

@param array $data

@return PageArray

@since 2.5.28

## pageArrayToArray()

Given a PageArray, convert it to a cachable array

@param PageArray $items

@return array

@throws WireException

@since 2.5.28

## getInfo()

Get information about all the caches in this WireCache


@param bool $verbose Whether to be more verbose for human readability

@param array|string $names Optionally specify name(s) of cache to get info. If omitted, all caches are included.

@param array|string $exclude Exclude any caches that begin with any of these namespaces (default=[])

@param array $cols Columns to get, default = [ 'name', 'expires', 'data', 'size' ]

@return array of arrays of cache info

## renderFile()

Render a file as a ProcessWire template file and cache the output

This method is similar to the `$files->render()` method and actually delegates the file
rendering to that method (when creating the cache). The important difference is that this
method caches the output according to WireCache rules for the `$expire` argument, rather
than re-rendering the file on every call.

If there are any changes to the source file `$filename` the cache will be automatically
re-created, regardless of what is specified for the `$expire` argument.

~~~~~~
// render primary nav from site/templates/partials/primary-nav.php
// and cache for 3600 seconds (1 hour)
echo $cache->renderFile('partials/primary-nav.php', 3600);
~~~~~~

@param string $filename Filename to render (typically PHP file).
  Can be full path/file, or dir/file relative to current work directory (which is typically /site/templates/).
  If providing a file relative to current dir, it should not start with "/".
  File must be somewhere within site/templates/, site/modules/ or wire/modules/, or provide your own `allowedPaths` option.
  Please note that $filename receives API variables already (you don’t have to provide them).

@param int|Page|string|null $expire Lifetime of this cache, in seconds, OR one of the following:
 - Specify one of the `WireCache::expire*` constants.
 - Specify the future date you want it to expire (as unix timestamp or any `strtotime()` compatible date format)
 - Provide a `Page` object to expire when any page using that template is saved.
 - Specify `WireCache::expireNever` to prevent expiration.
 - Specify `WireCache::expireSave` to expire when any page or template is saved.
 - Specify selector string matching pages that–when saved–expire the cache.
 - Omit for default value, which is `WireCache::expireDaily`.

@param array $options Accepts all options for the `WireFileTools::render()` method, plus these additional ones:
 - `name` (string): Optionally specify a unique name for this cache, otherwise $filename will be used as the unique name. (default='')
 - `vars` (array): Optional associative array of extra variables to send to template file. (default=[])
 - `allowedPaths` (array): Array of paths that are allowed (default is anywhere within templates, core modules and site modules)
 - `throwExceptions` (bool): Throw exceptions when fatal error occurs? (default=true)

@return string|bool Rendered template file or boolean false on fatal error (and throwExceptions disabled)

@throws WireException if given file doesn’t exist

@see WireFileTools::render()

@since 3.0.130

## setCacheModule()

Set WireCache module to use for caching

@param WireCacheInterface $module

@since 3.0.218

## getCacheModule()

Get WireCache module that is currently being used

@return WireCacheInterface

@since 3.0.218

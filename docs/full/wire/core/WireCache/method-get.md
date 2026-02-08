# WireCache::get()

Source: `wire/core/WireCache.php`

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

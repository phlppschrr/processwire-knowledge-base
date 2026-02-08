# WireCacheInterface

Source: `wire/core/Interfaces.php`

Interface for WireCache handler classes

For example implementations of this interface see
WireCacheDatabase (core) and WireCacheFilesystem (module)

@since 3.0.218

## find()

Find caches by names and/or expirations and return requested values

~~~~~
// Default options
$defaults = [
 'names' => [],
 'expires' => [],
 'expiresMode' => 'OR',
 'get' => [ 'name', 'expires', 'data' ],
];

// Example options
$options['names'] = [ 'my-cache', 'your-cache', 'hello-*' ];
$options['expires'] => [
 '<= ' . WireCache::expiresNever,
 '>= ' . date('Y-m-d H:i:s')
];
~~~~~

@param array $options
 - `get` (array): Properties to get in return value, one or more of [ `name`, `expires`, `data`, `size` ] (default=all)
 - `names` (array): Names of caches to find (OR condition), optionally appended with wildcard `*`.
 - `expires` (array): Expirations of caches to match in ISO-8601 date format, prefixed with operator and space (see expiresMode mode below).
 - `expiresMode` (string): Whether it should match any one condition 'OR', or all conditions 'AND' (default='OR')

@return array Returns array of associative arrays, each containing requested properties

## save()

Save a cache

@param string $name

@param string $data

@param string $expire

@return bool

## delete()

Delete cache by name

@param string $name

@return bool

## deleteAll()

Delete all caches (except those reserved by the system)

@return int

## expireAll()

Expire all caches (except those that should never expire)

@return int

# $wireCacheInterface->find(array $options): array

Source: `wire/core/Interfaces.php`

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

## Arguments

- `$options` `array` - `get` (array): Properties to get in return value, one or more of [ `name`, `expires`, `data`, `size` ] (default=all) - `names` (array): Names of caches to find (OR condition), optionally appended with wildcard `*`. - `expires` (array): Expirations of caches to match in ISO-8601 date format, prefixed with operator and space (see expiresMode mode below). - `expiresMode` (string): Whether it should match any one condition 'OR', or all conditions 'AND' (default='OR')

## Return value

array Returns array of associative arrays, each containing requested properties

# $wire->cache($name = '', $expire = null, $func = null): WireCache|string|array|PageArray|null

Source: `wire/core/Wire.php`

Access the $cache API variable as a function.

## Usage

~~~~~
// basic usage
$wireCache = $wire->cache();

// usage with all arguments
$wireCache = $wire->cache($name = '', $expire = null, $func = null);
~~~~~

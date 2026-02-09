# $modules->memcache($name, $setValue = null): bool|array|mixed|null

Source: `wire/core/Modules.php`

Set a runtime memory cache

## Usage

~~~~~
// basic usage
$bool = $modules->memcache($name);

// usage with all arguments
$bool = $modules->memcache($name, $setValue = null);
~~~~~

## Arguments

- `$name` `string`
- `$setValue` (optional) `mixed`

## Return value

- `bool|array|mixed|null`

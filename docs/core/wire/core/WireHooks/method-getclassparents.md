# $wireHooks->getClassParents($object, $cache = true): array

Source: `wire/core/WireHooks.php`

Get an array of parent classes and interfaces for the given object

## Usage

~~~~~
// basic usage
$array = $wireHooks->getClassParents($object);

// usage with all arguments
$array = $wireHooks->getClassParents($object, $cache = true);
~~~~~

## Arguments

- `$object` `Wire|string` Maybe either object instance or class name
- `$cache` (optional) `bool` Allow use of cache for getting or storing? (default=true)

## Return value

- `array`

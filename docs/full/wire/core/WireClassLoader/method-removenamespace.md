# $wireClassLoader->removeNamespace($namespace, $path = '')

Source: `wire/core/WireClassLoader.php`

Remove defined paths (or single path) for given namespace

## Usage

~~~~~
// basic usage
$result = $wireClassLoader->removeNamespace($namespace);

// usage with all arguments
$result = $wireClassLoader->removeNamespace($namespace, $path = '');
~~~~~

## Arguments

- `$namespace` `string`
- `$path` (optional) `string` Optionally specify path to remove (default=remove all)

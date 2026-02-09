# $wireClassLoader->addPrefix($prefix, $path)

Source: `wire/core/WireClassLoader.php`

Map a class prefix to a path

This is used as a helper/fallback and class is not required to be in given path,
but the path will be added as another to check when not found in namespace path(s).

## Usage

~~~~~
// basic usage
$result = $wireClassLoader->addPrefix($prefix, $path);
~~~~~

## Arguments

- `$prefix` `string` Case sensitive prefix specific to class name (not namespace).
- `$path` `string`

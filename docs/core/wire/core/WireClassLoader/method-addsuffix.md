# $wireClassLoader->addSuffix($suffix, $path)

Source: `wire/core/WireClassLoader.php`

Map a class suffix to a path

This is used as a helper/fallback and class is not required to be in given path,
but the path will be added as another to check when not found in namespace path(s).

## Usage

~~~~~
// basic usage
$result = $wireClassLoader->addSuffix($suffix, $path);
~~~~~

## Arguments

- `$suffix` `string` Case sensitive suffix specific to class name (not namespace).
- `$path` `string`

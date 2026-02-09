# $wireClassLoader->findClassFile($className): bool|string

Source: `wire/core/WireClassLoader.php`

Find filename for given class name (primarily for API testing/debugging purposes)

## Usage

~~~~~
// basic usage
$bool = $wireClassLoader->findClassFile($className);
~~~~~

## Arguments

- `$className` `string` Class name with namespace

## Return value

- `bool|string` Returns file on success or boolean false when not found

## Since

3.0.152

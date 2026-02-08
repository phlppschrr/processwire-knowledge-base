# $wireClassLoader->addNamespace($namespace, $path)

Source: `wire/core/WireClassLoader.php`

Add a namespace to point to a path root

Multiple root paths may be specified for a single namespace by calling this method more than once.

## Example

~~~~~
$classLoader->addNamespace('HelloWorld', '/path/to/that/');
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireClassLoader->addNamespace($namespace, $path);
~~~~~

## Arguments

- `$namespace` `string`
- `$path` `string` Full system path

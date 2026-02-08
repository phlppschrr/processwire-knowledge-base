# $functions->wireInstanceOf($instance, $className, $autoload = true): bool|string

Source: `wire/core/Functions.php`

Does given instance (or class) represent an instance of the given className (or class names)?

Since version 3.0.108 the $className argument may also represent an interface,
array of interfaces, or mixed array of interfaces and class names. Previous versions did
not support interfaces unless the $instance argument was an object.

## Usage

~~~~~
// basic usage
$bool = $functions->wireInstanceOf($instance, $className);

// usage with all arguments
$bool = $functions->wireInstanceOf($instance, $className, $autoload = true);
~~~~~

## Arguments

- `$instance` `object|string` Object instance to test (or string of its class name).
- `$className` `string|array` Class/interface name or array of class/interface names to test against.
- `$autoload` (optional) `bool` Allow PHP to autoload the class? (default=true)

## Return value

- `bool|string` Returns one of the following: - `false` (bool): if not an instance (whether $className argument is string or array). - `true` (bool): if given a single $className (string) and $instance is an instance of it. - `ClassName` (string): first matching class/interface name if $className was an array of classes to test.

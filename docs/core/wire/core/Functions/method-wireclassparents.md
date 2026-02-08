# $functions->wireClassParents($className, $autoload = true): array

Source: `wire/core/Functions.php`

Return array of all parent classes for given class/object

ProcessWire namespace aware version of PHP’s class_parents() function

Returns associative array where array keys are full namespaced class name, and
values are the non-namespaced classname.

## Arguments

- string|object $className
- bool $autoload

## Return value

array

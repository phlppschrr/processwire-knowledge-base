# $functions->wireClassExists($className, $autoload = true): bool

Source: `wire/core/Functions.php`

Does the given class name exist?

ProcessWire namespace aware version of PHP’s class_exists() function

If given a class name that does not include a namespace, the `\ProcessWire` namespace is assumed.

## Arguments

- string $className
- bool $autoload

## Return value

bool

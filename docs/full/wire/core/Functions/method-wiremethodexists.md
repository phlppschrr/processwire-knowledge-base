# $functions->wireMethodExists($className, $method, $hookable = false): bool

Source: `wire/core/Functions.php`

Does the given class have the given method?

ProcessWire namespace aware version of PHP’s method_exists() function

If given a class name that does not include a namespace, the `\ProcessWire` namespace is assumed.

## Arguments

- `$className` `string` Class name or object
- `$method` `string` Method name
- `$hookable` (optional) `bool` Also return true if "method" exists in a hookable format "___method"? (default=false) 3.0.204+

## Return value

bool

# $functions->wireMethodExists($className, $method, $hookable = false): bool

Source: `wire/core/Functions.php`

Does the given class have the given method?

ProcessWire namespace aware version of PHP’s method_exists() function

If given a class name that does not include a namespace, the `\ProcessWire` namespace is assumed.

## Usage

~~~~~
// basic usage
$bool = $functions->wireMethodExists($className, $method);

// usage with all arguments
$bool = $functions->wireMethodExists($className, $method, $hookable = false);
~~~~~

## Arguments

- `$className` `string` Class name or object
- `$method` `string` Method name
- `$hookable` (optional) `bool` Also return true if "method" exists in a hookable format "___method"? (default=false) 3.0.204+

## Return value

- `bool`

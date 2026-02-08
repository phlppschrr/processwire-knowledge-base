# Functions::wireMethodExists()

Source: `wire/core/Functions.php`

Does the given class have the given method?

ProcessWire namespace aware version of PHP’s method_exists() function

If given a class name that does not include a namespace, the `\ProcessWire` namespace is assumed.


@param string $className Class name or object

@param string $method Method name

@param bool $hookable Also return true if "method" exists in a hookable format "___method"? (default=false) 3.0.204+

@return bool

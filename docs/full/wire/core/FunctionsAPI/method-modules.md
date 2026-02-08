# $functionsAPI->modules($name = ''): Modules|Module|ConfigurableModule|null

Source: `wire/core/FunctionsAPI.php`

Get a module, get module information, and much more ($modules API variable as a function)

This function behaves the same as the `$modules` API variable, though does support
an optional shortcut argument for getting a module.

~~~~~
$modules = modules(); // Simply get $modules API var
$module = modules()->get('ModuleName'); // Get a module
$module = modules('ModuleName'); // Shortcut to get a module
~~~~~

## Arguments

- `$name` (optional) `string` Optionally retrieve the given module name

## Return value

Modules|Module|ConfigurableModule|null

## See also

- Modules

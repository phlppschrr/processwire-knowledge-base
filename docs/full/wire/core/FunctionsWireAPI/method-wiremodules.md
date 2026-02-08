# $functionsWireAPI->wireModules($name = ''): Modules|Module|ConfigurableModule|null

Source: `wire/core/FunctionsWireAPI.php`

Access the $modules API variable as a function

~~~~~
$modules = modules(); // Simply get $modules API var
$module = modules()->get('ModuleName'); // Get a module
$module = modules('ModuleName'); // Shortcut to get a module
~~~~~

## Arguments

- string $name Optionally retrieve the given module name

## Return value

Modules|Module|ConfigurableModule|null

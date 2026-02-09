# $functionsWireAPI->wireModules($name = ''): Modules|Module|ConfigurableModule|null

Source: `wire/core/FunctionsWireAPI.php`

Access the $modules API variable as a function

## Example

~~~~~
$modules = modules(); // Simply get $modules API var
$module = modules()->get('ModuleName'); // Get a module
$module = modules('ModuleName'); // Shortcut to get a module
~~~~~

## Usage

~~~~~
// basic usage
$modules = $functionsWireAPI->wireModules();

// usage with all arguments
$modules = $functionsWireAPI->wireModules($name = '');
~~~~~

## Arguments

- `$name` (optional) `string` Optionally retrieve the given module name

## Return value

- `Modules|Module|ConfigurableModule|null`

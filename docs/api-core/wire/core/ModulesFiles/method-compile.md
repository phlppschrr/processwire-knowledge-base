# $modulesFiles->compile($moduleName, $file = '', $namespace = null): string|bool

Source: `wire/core/ModulesFiles.php`

Compile and return the given file for module, if allowed to do so

## Usage

~~~~~
// basic usage
$string = $modulesFiles->compile($moduleName);

// usage with all arguments
$string = $modulesFiles->compile($moduleName, $file = '', $namespace = null);
~~~~~

## Arguments

- `$moduleName` `Module|string`
- `$file` (optional) `string` Optionally specify the module filename as an optimization
- `$namespace` (optional) `string|null` Optionally specify namespace as an optimization

## Return value

- `string|bool`

# $modulesFiles->moduleFileExt($class, $setValue = null): int

Source: `wire/core/ModulesFiles.php`

Get or set module file extension type (1 or 2)

## Usage

~~~~~
// basic usage
$int = $modulesFiles->moduleFileExt($class);

// usage with all arguments
$int = $modulesFiles->moduleFileExt($class, $setValue = null);
~~~~~

## Arguments

- `$class` `string` Module class name
- `$setValue` (optional) `int` 1 for '.module' or 2 for '.module.php', or omit to get current value

## Return value

- `int`

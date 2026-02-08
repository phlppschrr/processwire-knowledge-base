# $modules->getModuleID($class): int

Source: `wire/core/Modules.php`

Returns the database ID of a given module class, or 0 if not found

## Usage

~~~~~
// basic usage
$int = $modules->getModuleID($class);
~~~~~

## Arguments

- `$class` `string|int|Module` Module, module name or ID

## Return value

- `int`

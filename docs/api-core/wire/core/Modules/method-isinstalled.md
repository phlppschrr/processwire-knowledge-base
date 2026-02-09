# $modules->isInstalled($class): bool

Source: `wire/core/Modules.php`

Is the given module name installed?

## Usage

~~~~~
// basic usage
$bool = $modules->isInstalled($class);
~~~~~

## Arguments

- `$class` `string` Just a module class name, or optionally: `ModuleClassName>=1.2.3` (operator and version)

## Return value

- `bool` True if installed, false if not

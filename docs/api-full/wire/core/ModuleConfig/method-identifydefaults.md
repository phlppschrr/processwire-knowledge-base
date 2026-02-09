# $moduleConfig->identifyDefaults($a): array

Source: `wire/core/ModuleConfig.php`

Identify defaults from the given Inputfield definition array (internal use)

This is used only when getDefaults() is not implemented by descending class,
and inputfields use an array definition.

## Usage

~~~~~
// basic usage
$array = $moduleConfig->identifyDefaults($a);
~~~~~

## Arguments

- `$a` `array`

## Return value

- `array`

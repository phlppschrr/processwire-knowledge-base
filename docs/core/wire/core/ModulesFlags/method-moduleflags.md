# $modulesFlags->moduleFlags($moduleID = null, $setValue = null): array|mixed|null

Source: `wire/core/ModulesFlags.php`

Get or set flags for module by module ID

Omit all arguments to get flags for all modules indexed by module ID.

Returns null if given module ID not found.

## Usage

~~~~~
// basic usage
$array = $modulesFlags->moduleFlags();

// usage with all arguments
$array = $modulesFlags->moduleFlags($moduleID = null, $setValue = null);
~~~~~

## Arguments

- `$moduleID` (optional) `int` This method only accepts module ID
- `$setValue` (optional) `int` Flag(s) to set

## Return value

- `array|mixed|null`

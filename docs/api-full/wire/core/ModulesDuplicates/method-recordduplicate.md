# $modulesDuplicates->recordDuplicate($basename, $pathname, $pathname2, &$installed)

Source: `wire/core/ModulesDuplicates.php`

Record a duplicate at runtime

## Usage

~~~~~
// basic usage
$result = $modulesDuplicates->recordDuplicate($basename, $pathname, $pathname2, $installed);

// usage with all arguments
$result = $modulesDuplicates->recordDuplicate($basename, $pathname, $pathname2, &$installed);
~~~~~

## Arguments

- `$basename` `string` Name of module
- `$pathname` `string` Path of module
- `$pathname2` `string` Second path of module
- `$installed` `array` Installed module info array

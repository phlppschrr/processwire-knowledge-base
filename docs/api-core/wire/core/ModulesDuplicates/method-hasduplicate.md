# $modulesDuplicates->hasDuplicate($className, $pathname = ''): bool

Source: `wire/core/ModulesDuplicates.php`

Does the given module class have a duplicate?

## Usage

~~~~~
// basic usage
$bool = $modulesDuplicates->hasDuplicate($className);

// usage with all arguments
$bool = $modulesDuplicates->hasDuplicate($className, $pathname = '');
~~~~~

## Arguments

- `$className` `string`
- `$pathname` (optional) `string` Optionally specify the duplicate to check

## Return value

- `bool`

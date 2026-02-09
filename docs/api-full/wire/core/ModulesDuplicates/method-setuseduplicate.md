# $modulesDuplicates->setUseDuplicate($className, $pathname)

Source: `wire/core/ModulesDuplicates.php`

For a module that has duplicates, tell it which file to use

## Usage

~~~~~
// basic usage
$result = $modulesDuplicates->setUseDuplicate($className, $pathname);
~~~~~

## Arguments

- `$className` `string`
- `$pathname` `string` Full path and filename to module file

## Exceptions

- `WireException` if given information that can't be resolved

# $modulesDuplicates->addDuplicate($className, $pathname, $current = false)

Source: `wire/core/ModulesDuplicates.php`

Add a duplicate to the list

## Usage

~~~~~
// basic usage
$result = $modulesDuplicates->addDuplicate($className, $pathname);

// usage with all arguments
$result = $modulesDuplicates->addDuplicate($className, $pathname, $current = false);
~~~~~

## Arguments

- $className
- $pathname
- `$current` (optional) `bool` Is this the current one in use?

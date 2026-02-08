# $modulesDuplicates->getDuplicatesConfigData($className, array $configData = array()): array

Source: `wire/core/ModulesDuplicates.php`

Populate duplicates info into config data, when applicable

## Usage

~~~~~
// basic usage
$array = $modulesDuplicates->getDuplicatesConfigData($className);

// usage with all arguments
$array = $modulesDuplicates->getDuplicatesConfigData($className, array $configData = array());
~~~~~

## Arguments

- $className
- `$configData` (optional) `array`

## Return value

- `array` Updated configData

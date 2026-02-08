# $exportable->setImportData(array $data): array

Source: `wire/core/Interfaces.php`

Given an export data array, import it back to the class and return what happened

## Usage

~~~~~
// basic usage
$array = $exportable->setImportData($data);

// usage with all arguments
$array = $exportable->setImportData(array $data);
~~~~~

## Arguments

- `$data` `array`

## Return value

- `array` Returns array( [property_name] => array( 'old' => 'old value',	// old value, always a string 'new' => 'new value',	// new value, always a string 'error' => 'error message or blank if no error' )

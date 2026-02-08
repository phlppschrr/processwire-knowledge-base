# $templates->___setImportData(Template $template, array $data): array

Source: `wire/core/Templates.php`

Given an array of Template export data, import it to the given Template

## Example

~~~~~~
// Example of return value
$returnValue = array(
  'property_name' => array(
    'old' => 'old value', // old value (in string comparison format)
    'new' => 'new value', // new value (in string comparison format)
    'error' => 'error message or blank if no error' // error message (string) or messages (array)
  ),
  'another_property_name' => array(
    // ...
  )
);
~~~~~~

## Usage

~~~~~
// basic usage
$array = $templates->___setImportData($template, $data);

// usage with all arguments
$array = $templates->___setImportData(Template $template, array $data);
~~~~~

## Arguments

- `$template` `Template` Template you want to import to
- `$data` `array` Import data array (must have been exported from getExportData() method).

## Return value

- `array` Returns array with list of changes (see example in method description)

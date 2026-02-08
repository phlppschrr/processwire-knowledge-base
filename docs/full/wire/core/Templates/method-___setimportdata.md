# Templates::___setImportData()

Source: `wire/core/Templates.php`

Given an array of Template export data, import it to the given Template

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


@param Template $template Template you want to import to

@param array $data Import data array (must have been exported from getExportData() method).

@return array Returns array with list of changes (see example in method description)

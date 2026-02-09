# $templates->setImportData(Template $template, array $data): array

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
$array = $templates->setImportData($template, $data);

// usage with all arguments
$array = $templates->setImportData(Template $template, array $data);
~~~~~

## Hookable

- Hookable method name: `setImportData`
- Implementation: `___setImportData`
- Hook with: `$templates->setImportData()`

## Hooking Before

~~~~~
$this->addHookBefore('Templates::setImportData', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $template = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $template);
  $event->arguments(1, $data);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Templates::setImportData', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $template = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$template` `Template` Template you want to import to
- `$data` `array` Import data array (must have been exported from getExportData() method).

## Return value

- `array` Returns array with list of changes (see example in method description)

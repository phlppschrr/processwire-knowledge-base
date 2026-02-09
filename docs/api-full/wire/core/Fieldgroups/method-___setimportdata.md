# $fieldgroups->setImportData(Fieldgroup $fieldgroup, array $data): array

Source: `wire/core/Fieldgroups.php`

Given an export data array, import it back to the class and return what happened

Changes are not committed until the item is saved

## Usage

~~~~~
// basic usage
$array = $fieldgroups->setImportData($fieldgroup, $data);

// usage with all arguments
$array = $fieldgroups->setImportData(Fieldgroup $fieldgroup, array $data);
~~~~~

## Arguments

- `$fieldgroup` `Fieldgroup`
- `$data` `array`

## Return value

- `array` Returns array( [property_name] => array( 'old' => 'old value',	// old value, always a string 'new' => 'new value',	// new value, always a string 'error' => 'error message or blank if no error' )

## Hooking

- Hookable method name: `setImportData`
- Implementation: `___setImportData`
- Hook with: `Fieldgroups::setImportData`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::setImportData', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fieldgroup);
  $event->arguments(1, $data);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldgroups::setImportData', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if given invalid data

# $fieldtype->importConfigData(Field $field, array $data): array

Source: `wire/core/Fieldtype.php`

Convert an array of exported data to a format that will be understood internally

This is the opposite of the exportConfigData() method.
Most modules can use the default implementation provided here.

## Usage

~~~~~
// basic usage
$array = $fieldtype->importConfigData($field, $data);

// usage with all arguments
$array = $fieldtype->importConfigData(Field $field, array $data);
~~~~~

## Arguments

- `$field` `Field`
- `$data` `array`

## Return value

- `array` Data as given and modified as needed. Also included is $data[errors], an associative array indexed by property name containing errors that occurred during import of config data.

## Hooking

- Hookable method name: `importConfigData`
- Implementation: `___importConfigData`
- Hook with: `Fieldtype::importConfigData`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::importConfigData', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
  $event->arguments(1, $data);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::importConfigData', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

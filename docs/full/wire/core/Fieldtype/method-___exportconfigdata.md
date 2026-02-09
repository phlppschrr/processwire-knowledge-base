# $fieldtype->exportConfigData(Field $field, array $data): array

Source: `wire/core/Fieldtype.php`

Export configuration values for external consumption

Use this method to externalize any config values when necessary.
For example, internal IDs should be converted to GUIDs where possible.
Most Fieldtype modules can use the default implementation already provided here.

## Usage

~~~~~
// basic usage
$array = $fieldtype->exportConfigData($field, $data);

// usage with all arguments
$array = $fieldtype->exportConfigData(Field $field, array $data);
~~~~~

## Hookable

- Hookable method name: `exportConfigData`
- Implementation: `___exportConfigData`
- Hook with: `$fieldtype->exportConfigData()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::exportConfigData', function(HookEvent $event) {
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

## Hooking After

~~~~~
$this->addHookAfter('Fieldtype::exportConfigData', function(HookEvent $event) {
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

## Arguments

- `$field` `Field`
- `$data` `array`

## Return value

- `array`

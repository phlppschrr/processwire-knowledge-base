# $fieldtypeMulti->getSelectorInfo(Field $field, array $data = array()): array

Source: `wire/core/FieldtypeMulti.php`

Return array with information about what properties and operators can be used with this field

## Usage

~~~~~
// basic usage
$array = $fieldtypeMulti->getSelectorInfo($field);

// usage with all arguments
$array = $fieldtypeMulti->getSelectorInfo(Field $field, array $data = array());
~~~~~

## Hookable

- Hookable method name: `getSelectorInfo`
- Implementation: `___getSelectorInfo`
- Hook with: `$fieldtypeMulti->getSelectorInfo()`

## Hooking Before

~~~~~
$this->addHookBefore('FieldtypeMulti::getSelectorInfo', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

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
$this->addHookAfter('FieldtypeMulti::getSelectorInfo', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

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
- `$data` (optional) `array` Array of extra data, when/if needed

## Return value

- `array`

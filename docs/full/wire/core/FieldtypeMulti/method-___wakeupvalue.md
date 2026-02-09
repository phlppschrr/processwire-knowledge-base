# $fieldtypeMulti->wakeupValue(Page $page, Field $field, $value): WireArray

Source: `wire/core/FieldtypeMulti.php`

Process the value to convert it from array to whatever object it needs to be

## Usage

~~~~~
// basic usage
$items = $fieldtypeMulti->wakeupValue($page, $field, $value);

// usage with all arguments
$items = $fieldtypeMulti->wakeupValue(Page $page, Field $field, $value);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `array`

## Return value

- `WireArray`

## Hooking

- Hookable method name: `wakeupValue`
- Implementation: `___wakeupValue`
- Hook with: `FieldtypeMulti::wakeupValue`

### Hooking Before

~~~~~
$this->addHookBefore('FieldtypeMulti::wakeupValue', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $value = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
  $event->arguments(2, $value);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('FieldtypeMulti::wakeupValue', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $value = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

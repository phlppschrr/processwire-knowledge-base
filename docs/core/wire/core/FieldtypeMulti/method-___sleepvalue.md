# $fieldtypeMulti->sleepValue(Page $page, Field $field, $value): array

Source: `wire/core/FieldtypeMulti.php`

Given an 'awake' value, as set by wakeupValue, convert the value back to a basic type for storage in DB.

FieldtypeMulti::savePageField expects values as an array, so we convert the $value object to an array

Note that FieldtypeMulti is designed around potentially supporting more than just the 'data' field in
the table, so other fieldtypes may want to override this and return an array of associative arrays containing a 'data' field
and any other fields that map to the table. i.e. $values[] = array('data' => $data, 'description' => $description), etc.
See FieldtypePagefiles module class for an example of this.

## Usage

~~~~~
// basic usage
$array = $fieldtypeMulti->sleepValue($page, $field, $value);

// usage with all arguments
$array = $fieldtypeMulti->sleepValue(Page $page, Field $field, $value);
~~~~~

## Hookable

- Hookable method name: `sleepValue`
- Implementation: `___sleepValue`
- Hook with: `$fieldtypeMulti->sleepValue()`

## Hooking Before

~~~~~
$this->addHookBefore('FieldtypeMulti::sleepValue', function(HookEvent $event) {
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

## Hooking After

~~~~~
$this->addHookAfter('FieldtypeMulti::sleepValue', function(HookEvent $event) {
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

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `WireArray`

## Return value

- `array`

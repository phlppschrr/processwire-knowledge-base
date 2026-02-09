# $fieldtype->sleepValue(Page $page, Field $field, $value): string|int|float|array

Source: `wire/core/Fieldtype.php`

Given an 'awake' value, as set by wakeupValue(), convert the value back to a basic type for storage in database.

In many cases, this may mean no change to the value, which is why the default here just returns the value.
But for values that are stored with pages as objects (for instance) this method would take that object
and convert it to an array, int or string (serialized or otherwise).

Returned value must be either an array, number, or string.

## Usage

~~~~~
// basic usage
$string = $fieldtype->sleepValue($page, $field, $value);

// usage with all arguments
$string = $fieldtype->sleepValue(Page $page, Field $field, $value);
~~~~~

## Hookable

- Hookable method name: `sleepValue`
- Implementation: `___sleepValue`
- Hook with: `$fieldtype->sleepValue()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::sleepValue', function(HookEvent $event) {
  $fieldtype = $event->object;

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
$this->addHookAfter('Fieldtype::sleepValue', function(HookEvent $event) {
  $fieldtype = $event->object;

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
- `$value` `string|int|float|array|object`

## Return value

- `string|int|float|array`

## See Also

- [Fieldtype::wakeupValue()](method-___wakeupvalue.md)

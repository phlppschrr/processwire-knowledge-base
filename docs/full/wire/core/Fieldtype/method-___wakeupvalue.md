# $fieldtype->wakeupValue(Page $page, Field $field, $value): string|int|array|object

Source: `wire/core/Fieldtype.php`

Given a raw value (value as stored in database), return the value as it would appear in a Page object.

In many cases, no change to the value may be necessary, but if a Page expects this value as an object (for instance)
then this would be the method that converts that value to an object and returns it.

This method is called by the Page class, which takes the value provided by `Fieldtype::loadPageField()` and sends
it to this method before making it a part of the Page.

## Usage

~~~~~
// basic usage
$string = $fieldtype->wakeupValue($page, $field, $value);

// usage with all arguments
$string = $fieldtype->wakeupValue(Page $page, Field $field, $value);
~~~~~

## Hookable

- Hookable method name: `wakeupValue`
- Implementation: `___wakeupValue`
- Hook with: `$fieldtype->wakeupValue()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::wakeupValue', function(HookEvent $event) {
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
$this->addHookAfter('Fieldtype::wakeupValue', function(HookEvent $event) {
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
- `$value` `string|int|array`

## Return value

- `string|int|array|object` $value

## See Also

- [Fieldtype::sleepValue()](method-___sleepvalue.md)

# $fieldtype->exportValue(Page $page, Field $field, $value, array $options = array()): string|float|int|array

Source: `wire/core/Fieldtype.php`

Given a value, return an portable version of it as either a string, int, float or array

If an array is returned, it should only contain: strings, ints, floats or more arrays of those types.
This is intended for web service exports.

When applicable, this method should map things like internal IDs to named equivalents (name, path, etc.).

If not overridden, this takes on the same behavior as `Fieldtype::sleepValue()`. However, if overridden,
it is intended to be more verbose than wakeupValue, where applicable.

## Usage

~~~~~
// basic usage
$string = $fieldtype->exportValue($page, $field, $value);

// usage with all arguments
$string = $fieldtype->exportValue(Page $page, Field $field, $value, array $options = array());
~~~~~

## Hookable

- Hookable method name: `exportValue`
- Implementation: `___exportValue`
- Hook with: `$fieldtype->exportValue()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::exportValue', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $value = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
  $event->arguments(2, $value);
  $event->arguments(3, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldtype::exportValue', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $value = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `string|int|float|array|object|null`
- `$options` (optional) `array` Optional settings to shape the exported value, if needed: - `system` (boolean): Indicates value is being used for a system export via $pages->export() call (default=false). - `human` (boolean): When true, Fieldtype may optionally emphasize human readability over importability (default=false).

## Return value

- `string|float|int|array`

# $fieldtype->formatValue(Page $page, Field $field, $value): mixed

Source: `wire/core/Fieldtype.php`

Format the given value for output and return a string of the formatted value

Page instances call upon this method to do any necessary formatting of a value in preparation for output,
but only if output formatting `$page->of()` is enabled. The most common use of this method is for text-only fields that
need to have some text formatting applied to them, like Markdown, SmartyPants, Textile, etc. As a result,
Fieldtype modules don't need to implement this unless it's applicable.

## Usage

~~~~~
// basic usage
$result = $fieldtype->formatValue($page, $field, $value);

// usage with all arguments
$result = $fieldtype->formatValue(Page $page, Field $field, $value);
~~~~~

## Hookable

- Hookable method name: `formatValue`
- Implementation: `___formatValue`
- Hook with: `$fieldtype->formatValue()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::formatValue', function(HookEvent $event) {
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
$this->addHookAfter('Fieldtype::formatValue', function(HookEvent $event) {
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

- `$page` `Page` Page that the value lives on
- `$field` `Field` Field that represents the value
- `$value` `string|int|object` The value to format

## Return value

- `mixed`

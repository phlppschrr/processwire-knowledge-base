# $fieldtype->getConfigAllowContext(Field $field): array

Source: `wire/core/Fieldtype.php`

Return an array of configuration field names from that are allowed in fieldgroup/template context

These field names are those that would be used for Inputfields like those returned from getConfigInputfields()
or getConfigArray().

Inputfield field names returned from here are allowed to have unique values per Fieldgroup assignment, rather
than sharing the same setting globally.

## Usage

~~~~~
// basic usage
$array = $fieldtype->getConfigAllowContext($field);

// usage with all arguments
$array = $fieldtype->getConfigAllowContext(Field $field);
~~~~~

## Hookable

- Hookable method name: `getConfigAllowContext`
- Implementation: `___getConfigAllowContext`
- Hook with: `$fieldtype->getConfigAllowContext()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::getConfigAllowContext', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldtype::getConfigAllowContext', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `array` of Inputfield names

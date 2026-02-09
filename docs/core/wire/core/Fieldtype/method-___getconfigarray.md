# $fieldtype->getConfigArray(Field $field): array

Source: `wire/core/Fieldtype.php`

Same as getConfigInputfields but with definition as an array instead

If both getConfigInputfields and getConfigInputfieldsArray are implemented then
definitions from both will be used. It's probably simplest just to implement one
or the other.

## Usage

~~~~~
// basic usage
$array = $fieldtype->getConfigArray($field);

// usage with all arguments
$array = $fieldtype->getConfigArray(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `array`

## Hooking

- Hookable method name: `getConfigArray`
- Implementation: `___getConfigArray`
- Hook with: `Fieldtype::getConfigArray`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::getConfigArray', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::getConfigArray', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

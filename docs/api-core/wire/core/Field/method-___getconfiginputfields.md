# $field->getConfigInputfields(): InputfieldWrapper

Source: `wire/core/Field.php`

Get any Inputfields needed to configure the field in the admin.

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $field->getConfigInputfields();
~~~~~

## Return value

- `InputfieldWrapper`

## Hooking

- Hookable method name: `getConfigInputfields`
- Implementation: `___getConfigInputfields`
- Hook with: `Field::getConfigInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('Field::getConfigInputfields', function(HookEvent $event) {
  $field = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Field::getConfigInputfields', function(HookEvent $event) {
  $field = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

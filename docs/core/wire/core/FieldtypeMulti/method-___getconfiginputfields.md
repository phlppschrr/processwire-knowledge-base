# $fieldtypeMulti->getConfigInputfields(Field $field): InputfieldWrapper

Source: `wire/core/FieldtypeMulti.php`

Get Inputfields for advanced settings of the Field and Fieldtype

Inputfields returned from this appear under the "Advanced" tab rather than the "Details" tab,
in the Field editor.

In most cases, you will want to implement the getConfigInputfields() or getConfigArray() rather than this method.

NOTE: Inputfields with a name that starts with an underscore, i.e. "_myname" are assumed to be for runtime
use and are NOT stored in the database.

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $fieldtypeMulti->getConfigInputfields($field);

// usage with all arguments
$inputfieldWrapper = $fieldtypeMulti->getConfigInputfields(Field $field);
~~~~~

## Hookable

- Hookable method name: `getConfigInputfields`
- Implementation: `___getConfigInputfields`
- Hook with: `$fieldtypeMulti->getConfigInputfields()`

## Hooking Before

~~~~~
$this->addHookBefore('FieldtypeMulti::getConfigInputfields', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('FieldtypeMulti::getConfigInputfields', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

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

- `InputfieldWrapper`

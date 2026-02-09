# $fieldtypeMulti->getCompatibleFieldtypes(Field $field): Fieldtypes|null

Source: `wire/core/FieldtypeMulti.php`

Get an array of Fieldtypes that are compatible with this one (i.e. ones the user may change the type to)

## Usage

~~~~~
// basic usage
$fieldtypes = $fieldtypeMulti->getCompatibleFieldtypes($field);

// usage with all arguments
$fieldtypes = $fieldtypeMulti->getCompatibleFieldtypes(Field $field);
~~~~~

## Arguments

- `$field` `Field` Just in case it's needed

## Return value

- `Fieldtypes|null`

## Hooking

- Hookable method name: `getCompatibleFieldtypes`
- Implementation: `___getCompatibleFieldtypes`
- Hook with: `FieldtypeMulti::getCompatibleFieldtypes`

### Hooking Before

~~~~~
$this->addHookBefore('FieldtypeMulti::getCompatibleFieldtypes', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('FieldtypeMulti::getCompatibleFieldtypes', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

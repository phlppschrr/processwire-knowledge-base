# $fieldtype->getCompatibleFieldtypes(Field $field): Fieldtypes|null

Source: `wire/core/Fieldtype.php`

Get an array of Fieldtypes that are compatible with this one

This represents the list of Fieldtype modules that the user is allowed to change to from this one.

## Usage

~~~~~
// basic usage
$fieldtypes = $fieldtype->getCompatibleFieldtypes($field);

// usage with all arguments
$fieldtypes = $fieldtype->getCompatibleFieldtypes(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `Fieldtypes|null`

## Hooking

- Hookable method name: `getCompatibleFieldtypes`
- Implementation: `___getCompatibleFieldtypes`
- Hook with: `Fieldtype::getCompatibleFieldtypes`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::getCompatibleFieldtypes', function(HookEvent $event) {
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
$this->addHookAfter('Fieldtype::getCompatibleFieldtypes', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

# $fields->changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

Source: `wire/core/Fields.php`

Hook called when a field has changed type

## Usage

~~~~~
// basic usage
$result = $fields->changedType($item, $fromType, $toType);

// usage with all arguments
$result = $fields->changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType);
~~~~~

## Hookable

- Hookable method name: `changedType`
- Implementation: `___changedType`
- Hook with: `$fields->changedType()`

## Hooking Before

~~~~~
$this->addHookBefore('Fields::changedType', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $fromType = $event->arguments(1);
  $toType = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $fromType);
  $event->arguments(2, $toType);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fields::changedType', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $fromType = $event->arguments(1);
  $toType = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Field`
- `$fromType` `Fieldtype`
- `$toType` `Fieldtype`

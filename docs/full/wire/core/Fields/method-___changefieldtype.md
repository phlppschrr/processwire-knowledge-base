# $fields->changeFieldtype(Field $field1, $keepSettings = false): bool

Source: `wire/core/Fields.php`

Change a field's type

## Usage

~~~~~
// basic usage
$bool = $fields->changeFieldtype($field1);

// usage with all arguments
$bool = $fields->changeFieldtype(Field $field1, $keepSettings = false);
~~~~~

## Hookable

- Hookable method name: `changeFieldtype`
- Implementation: `___changeFieldtype`
- Hook with: `$fields->changeFieldtype()`

## Hooking Before

~~~~~
$this->addHookBefore('Fields::changeFieldtype', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field1 = $event->arguments(0);
  $keepSettings = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field1);
  $event->arguments(1, $keepSettings);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fields::changeFieldtype', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field1 = $event->arguments(0);
  $keepSettings = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$field1` `Field` Field with the new type already assigned
- `$keepSettings` (optional) `bool` Whether or not to keep custom $data settings (default=false)

## Return value

- `bool`

## Exceptions

- `WireException`

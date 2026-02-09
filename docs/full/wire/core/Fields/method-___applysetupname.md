# $fields->applySetupName(Field $field, $setupName = ''): bool

Source: `wire/core/Fields.php`

Setup a new field using predefined setup name(s) from the Field’s fieldtype

If no setupName is provided then this method doesn’t do anything, but hooks to it might.

## Usage

~~~~~
// basic usage
$bool = $fields->applySetupName($field);

// usage with all arguments
$bool = $fields->applySetupName(Field $field, $setupName = '');
~~~~~

## Arguments

- `$field` `Field` Newly created field
- `$setupName` (optional) `string` Setup name to apply

## Return value

- `bool` True if setup was appled, false if not

## Hooking

- Hookable method name: `applySetupName`
- Implementation: `___applySetupName`
- Hook with: `Fields::applySetupName`

### Hooking Before

~~~~~
$this->addHookBefore('Fields::applySetupName', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $setupName = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
  $event->arguments(1, $setupName);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fields::applySetupName', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $setupName = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.213

# $fieldtype->upgrade($fromVersion, $toVersion)

Source: `wire/core/Fieldtype.php`

Called when module version changes

## Usage

~~~~~
// basic usage
$result = $fieldtype->upgrade($fromVersion, $toVersion);
~~~~~

## Arguments

- $fromVersion
- $toVersion

## Hooking

- Hookable method name: `upgrade`
- Implementation: `___upgrade`
- Hook with: `Fieldtype::upgrade`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::upgrade', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $fromVersion = $event->arguments(0);
  $toVersion = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fromVersion);
  $event->arguments(1, $toVersion);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::upgrade', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $fromVersion = $event->arguments(0);
  $toVersion = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if upgrade fails

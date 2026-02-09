# $fieldtype->uninstall()

Source: `wire/core/Fieldtype.php`

Uninstall this Fieldtype, consistent with optional Module interface

- Checks to make sure it's safe to uninstall this Fieldtype. If not, throw an Exception indicating such.
- It's safe to uninstall a Fieldtype only if it's not being used by any Fields.
- If a Fieldtype overrides this to perform additional uninstall functions, it would be good to call this
  parent uninstall method first to make sure uninstall is okay.

## Usage

~~~~~
// basic usage
$result = $fieldtype->uninstall();
~~~~~

## Hooking

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `Fieldtype::uninstall`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::uninstall', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::uninstall', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` Should throw an Exception if uninstall can't be completed.

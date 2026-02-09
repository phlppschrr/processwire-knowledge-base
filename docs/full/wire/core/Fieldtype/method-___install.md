# $fieldtype->install()

Source: `wire/core/Fieldtype.php`

Install this Fieldtype, consistent with optional Module interface

- Called once at time of installation by Modules::install().
- If custom Fieldtype classes need to perform any setup beyond that performed in ___createTable(),
  this method is where they should do it. This is not required, and probably not applicable to most.

## Usage

~~~~~
// basic usage
$result = $fieldtype->install();
~~~~~

## Hooking

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `Fieldtype::install`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::install', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::install', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` Should throw an Exception on failure to install

# $adminThemeFramework->getUserNavArray(): array

Source: `wire/core/AdminThemeFramework.php`

Get navigation items for the “user” menu

This is hookable so that something else could add stuff to it.
See the method body for details on format used.

Supported properties/attributes as of 3.0.248:

- url (href)
- title (label text)
- target (html attr)
- icon (name of icon)
- permission (required permission)
- id (html attr)
- class (html attr)
- onclick (html attr)
- data-* (html attr)

## Usage

~~~~~
// basic usage
$array = $adminThemeFramework->getUserNavArray();
~~~~~

## Return value

- `array`

## Hooking

- Hookable method name: `getUserNavArray`
- Implementation: `___getUserNavArray`
- Hook with: `AdminThemeFramework::getUserNavArray`

### Hooking Before

~~~~~
$this->addHookBefore('AdminThemeFramework::getUserNavArray', function(HookEvent $event) {
  $adminThemeFramework = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('AdminThemeFramework::getUserNavArray', function(HookEvent $event) {
  $adminThemeFramework = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

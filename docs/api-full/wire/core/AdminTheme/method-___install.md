# $adminTheme->install()

Source: `wire/core/AdminTheme.php`

Install the admin theme

Other admin themes using an install() method must call this install before their own.

## Usage

~~~~~
// basic usage
$result = $adminTheme->install();
~~~~~

## Hooking

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `AdminTheme::install`

### Hooking Before

~~~~~
$this->addHookBefore('AdminTheme::install', function(HookEvent $event) {
  $adminTheme = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('AdminTheme::install', function(HookEvent $event) {
  $adminTheme = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

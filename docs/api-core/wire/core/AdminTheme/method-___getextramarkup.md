# $adminTheme->getExtraMarkup(): array

Source: `wire/core/AdminTheme.php`

Enables hooks to append extra markup to various sections of the admin page

## Usage

~~~~~
// basic usage
$array = $adminTheme->getExtraMarkup();
~~~~~

## Return value

- `array` Associative array containing the following properties, any of which may be populated or empty: - head - body - masthead - content - footer - sidebar

## Hooking

- Hookable method name: `getExtraMarkup`
- Implementation: `___getExtraMarkup`
- Hook with: `AdminTheme::getExtraMarkup`

### Hooking Before

~~~~~
$this->addHookBefore('AdminTheme::getExtraMarkup', function(HookEvent $event) {
  $adminTheme = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('AdminTheme::getExtraMarkup', function(HookEvent $event) {
  $adminTheme = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

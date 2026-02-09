# $adminThemeRenoHelpers->topNavItems(array $items): string

Source: `wire/modules/AdminTheme/AdminThemeReno/AdminThemeRenoHelpers.php`

Render top navigation items (hookable)

## Usage

~~~~~
// basic usage
$string = $adminThemeRenoHelpers->topNavItems($items);

// usage with all arguments
$string = $adminThemeRenoHelpers->topNavItems(array $items);
~~~~~

## Return value

- `string`

## Hooking

- Hookable method name: `topNavItems`
- Implementation: `___topNavItems`
- Hook with: `AdminThemeRenoHelpers::topNavItems`

### Hooking Before

~~~~~
$this->addHookBefore('AdminThemeRenoHelpers::topNavItems', function(HookEvent $event) {
  $adminThemeRenoHelpers = $event->object;

  // Get arguments
  $items = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $items);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('AdminThemeRenoHelpers::topNavItems', function(HookEvent $event) {
  $adminThemeRenoHelpers = $event->object;

  // Get arguments
  $items = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

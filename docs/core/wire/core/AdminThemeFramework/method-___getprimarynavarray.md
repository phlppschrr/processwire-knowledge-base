# $adminThemeFramework->getPrimaryNavArray(): array

Source: `wire/core/AdminThemeFramework.php`

Return nav array of primary navigation

## Usage

~~~~~
// basic usage
$array = $adminThemeFramework->getPrimaryNavArray();
~~~~~

## Hookable

- Hookable method name: `getPrimaryNavArray`
- Implementation: `___getPrimaryNavArray`
- Hook with: `$adminThemeFramework->getPrimaryNavArray()`

## Hooking Before

~~~~~
$this->addHookBefore('AdminThemeFramework::getPrimaryNavArray', function(HookEvent $event) {
  $adminThemeFramework = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('AdminThemeFramework::getPrimaryNavArray', function(HookEvent $event) {
  $adminThemeFramework = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `array`

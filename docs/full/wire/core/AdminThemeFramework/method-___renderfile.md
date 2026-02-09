# $adminThemeFramework->renderFile($file, array $vars = array()): string

Source: `wire/core/AdminThemeFramework.php`

Render a admin theme template file

This method is only used if it is hooked

## Usage

~~~~~
// basic usage
$string = $adminThemeFramework->renderFile($file);

// usage with all arguments
$string = $adminThemeFramework->renderFile($file, array $vars = array());
~~~~~

## Hookable

- Hookable method name: `renderFile`
- Implementation: `___renderFile`
- Hook with: `$adminThemeFramework->renderFile()`

## Hooking Before

~~~~~
$this->addHookBefore('AdminThemeFramework::renderFile', function(HookEvent $event) {
  $adminThemeFramework = $event->object;

  // Get arguments
  $file = $event->arguments(0);
  $vars = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $file);
  $event->arguments(1, $vars);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('AdminThemeFramework::renderFile', function(HookEvent $event) {
  $adminThemeFramework = $event->object;

  // Get arguments
  $file = $event->arguments(0);
  $vars = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$file` `string` Full path and filename
- `$vars` (optional) `array` Associative array of variables to populate in rendered file

## Return value

- `string` Returns blank string when $echo is true

## Since

3.0.196

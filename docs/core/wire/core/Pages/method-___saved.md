# $pages->saved(Page $page, array $changes = array(), $values = array())

Source: `wire/core/Pages.php`

Hook called after a page is successfully saved

This is the same as hooking after `Pages::save`, except that it occurs before other save-related hooks.
Whereas `Pages::save` hooks occur after. In most cases, the distinction does not matter.

## Usage

~~~~~
// basic usage
$result = $pages->saved($page);

// usage with all arguments
$result = $pages->saved(Page $page, array $changes = array(), $values = array());
~~~~~

## Hookable

- Hookable method name: `saved`
- Implementation: `___saved`
- Hook with: `$pages->saved()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::saved', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $changes = $event->arguments(1);
  $values = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $changes);
  $event->arguments(2, $values);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::saved', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $changes = $event->arguments(1);
  $values = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` The page that was saved
- `$changes` (optional) `array` Array of field names that changed
- `$values` (optional) `array` Array of values that changed, if values were being recorded, see Wire::getChanges(true) for details.

## See Also

- [Pages::savedPageOrField()](method-___savedpageorfield.md)
- [Pages::savedField()](method-___savedfield.md)

# $pagesType->saved(Page $page, array $changes = array(), $values = array())

Source: `wire/core/PagesType.php`

Hook called after a page of this type is successfully saved

## Usage

~~~~~
// basic usage
$result = $pagesType->saved($page);

// usage with all arguments
$result = $pagesType->saved(Page $page, array $changes = array(), $values = array());
~~~~~

## Arguments

- `$page` `Page` The page that was saved
- `$changes` (optional) `array` Array of field names that changed
- `$values` (optional) `array` Array of values that changed, if values were being recorded, see Wire::getChanges(true) for details.

## Hooking

- Hookable method name: `saved`
- Implementation: `___saved`
- Hook with: `PagesType::saved`

### Hooking Before

~~~~~
$this->addHookBefore('PagesType::saved', function(HookEvent $event) {
  $pagesType = $event->object;

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

### Hooking After

~~~~~
$this->addHookAfter('PagesType::saved', function(HookEvent $event) {
  $pagesType = $event->object;

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

## Since

3.0.128

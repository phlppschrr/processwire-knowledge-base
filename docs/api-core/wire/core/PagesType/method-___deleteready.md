# $pagesType->deleteReady(Page $page)

Source: `wire/core/PagesType.php`

Hook called when a page is about to be deleted, but before data has been touched

## Usage

~~~~~
// basic usage
$result = $pagesType->deleteReady($page);

// usage with all arguments
$result = $pagesType->deleteReady(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Hooking

- Hookable method name: `deleteReady`
- Implementation: `___deleteReady`
- Hook with: `PagesType::deleteReady`

### Hooking Before

~~~~~
$this->addHookBefore('PagesType::deleteReady', function(HookEvent $event) {
  $pagesType = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PagesType::deleteReady', function(HookEvent $event) {
  $pagesType = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.128

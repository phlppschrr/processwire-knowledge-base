# $pages->deleteReady(Page $page, array $options = array())

Source: `wire/core/Pages.php`

Hook called when a page is about to be deleted, but before data has been touched

This is different from a before `Pages::delete` hook because this hook is called once it has
been confirmed that the page is deleteable and *will* be deleted.

## Usage

~~~~~
// basic usage
$result = $pages->deleteReady($page);

// usage with all arguments
$result = $pages->deleteReady(Page $page, array $options = array());
~~~~~

## Hookable

- Hookable method name: `deleteReady`
- Implementation: `___deleteReady`
- Hook with: `$pages->deleteReady()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::deleteReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::deleteReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page that is about to be deleted.
- `$options` (optional) `array` Options passed to delete method (since 3.0.163)

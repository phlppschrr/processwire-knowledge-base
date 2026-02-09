# $pages->moveReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page is about to be moved to another parent

Note the previous parent is accessible in the `$page->parentPrevious` property.

## Usage

~~~~~
// basic usage
$result = $pages->moveReady($page);

// usage with all arguments
$result = $pages->moveReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `moveReady`
- Implementation: `___moveReady`
- Hook with: `$pages->moveReady()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::moveReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::moveReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page that is about to be moved.

## Since

3.0.235

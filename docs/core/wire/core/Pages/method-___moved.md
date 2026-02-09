# $pages->moved(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page has been moved from one parent to another

Note the previous parent is accessible in the `$page->parentPrevious` property.

## Usage

~~~~~
// basic usage
$result = $pages->moved($page);

// usage with all arguments
$result = $pages->moved(Page $page);
~~~~~

## Hookable

- Hookable method name: `moved`
- Implementation: `___moved`
- Hook with: `$pages->moved()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::moved', function(HookEvent $event) {
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
$this->addHookAfter('Pages::moved', function(HookEvent $event) {
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

- `$page` `Page` Page that was moved.

# $pages->added(Page $page)

Source: `wire/core/Pages.php`

Hook called after a new page has been added

## Usage

~~~~~
// basic usage
$result = $pages->added($page);

// usage with all arguments
$result = $pages->added(Page $page);
~~~~~

## Hookable

- Hookable method name: `added`
- Implementation: `___added`
- Hook with: `$pages->added()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::added', function(HookEvent $event) {
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
$this->addHookAfter('Pages::added', function(HookEvent $event) {
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

- `$page` `Page` Page that was added.

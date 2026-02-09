# $pages->sorted(Page $page, $children = false, $total = 0)

Source: `wire/core/Pages.php`

Hook called after a page has been sorted, or had its children re-sorted

## Usage

~~~~~
// basic usage
$result = $pages->sorted($page);

// usage with all arguments
$result = $pages->sorted(Page $page, $children = false, $total = 0);
~~~~~

## Hookable

- Hookable method name: `sorted`
- Implementation: `___sorted`
- Hook with: `$pages->sorted()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::sorted', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $children = $event->arguments(1);
  $total = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $children);
  $event->arguments(2, $total);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::sorted', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $children = $event->arguments(1);
  $total = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page given to have sort adjusted
- `$children` (optional) `bool` If true, children of $page have been all been re-sorted
- `$total` (optional) `int` Total number of pages that had sort adjusted as a result

# $pages->insertAfter(Page $page, Page $afterPage)

Source: `wire/core/Pages.php`

Sort/move one page after another (for manually sorted pages)

## Usage

~~~~~
// basic usage
$result = $pages->insertAfter($page, $afterPage);

// usage with all arguments
$result = $pages->insertAfter(Page $page, Page $afterPage);
~~~~~

## Arguments

- `$page` `Page` Page you want to move/sort
- `$afterPage` `Page` Page you want to insert after

## Hooking

- Hookable method name: `insertAfter`
- Implementation: `___insertAfter`
- Hook with: `Pages::insertAfter`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::insertAfter', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $afterPage = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $afterPage);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::insertAfter', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $afterPage = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException`

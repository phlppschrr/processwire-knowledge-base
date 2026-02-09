# $pages->insertBefore(Page $page, Page $beforePage)

Source: `wire/core/Pages.php`

Sort/move one page above another (for manually sorted pages)

## Usage

~~~~~
// basic usage
$result = $pages->insertBefore($page, $beforePage);

// usage with all arguments
$result = $pages->insertBefore(Page $page, Page $beforePage);
~~~~~

## Hookable

- Hookable method name: `insertBefore`
- Implementation: `___insertBefore`
- Hook with: `$pages->insertBefore()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::insertBefore', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $beforePage = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $beforePage);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::insertBefore', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $beforePage = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page you want to move/sort
- `$beforePage` `Page` Page you want to insert before

## Exceptions

- `WireException`

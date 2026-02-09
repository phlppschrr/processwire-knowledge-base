# $pages->restored(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page has been moved OUT of the trash (restored)

## Usage

~~~~~
// basic usage
$result = $pages->restored($page);

// usage with all arguments
$result = $pages->restored(Page $page);
~~~~~

## Hookable

- Hookable method name: `restored`
- Implementation: `___restored`
- Hook with: `$pages->restored()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::restored', function(HookEvent $event) {
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
$this->addHookAfter('Pages::restored', function(HookEvent $event) {
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

- `$page` `Page` Page that was restored

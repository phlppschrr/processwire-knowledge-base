# $pages->restoreReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page is about to be moved OUT of the trash (restored)

## Usage

~~~~~
// basic usage
$result = $pages->restoreReady($page);

// usage with all arguments
$result = $pages->restoreReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `restoreReady`
- Implementation: `___restoreReady`
- Hook with: `$pages->restoreReady()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::restoreReady', function(HookEvent $event) {
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
$this->addHookAfter('Pages::restoreReady', function(HookEvent $event) {
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

- `$page` `Page` Page that is about to be restored

## Since

3.0.235

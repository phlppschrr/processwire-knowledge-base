# $pages->statusChangeReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page's status is about to be changed and saved

Previous status may be accessed at `$page->statusPrevious`.

## Usage

~~~~~
// basic usage
$result = $pages->statusChangeReady($page);

// usage with all arguments
$result = $pages->statusChangeReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `statusChangeReady`
- Implementation: `___statusChangeReady`
- Hook with: `$pages->statusChangeReady()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::statusChangeReady', function(HookEvent $event) {
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
$this->addHookAfter('Pages::statusChangeReady', function(HookEvent $event) {
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

- `$page` `Page`

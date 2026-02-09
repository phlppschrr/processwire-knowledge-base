# $pages->addReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a new page is about to be added and saved to the database

## Usage

~~~~~
// basic usage
$result = $pages->addReady($page);

// usage with all arguments
$result = $pages->addReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `addReady`
- Implementation: `___addReady`
- Hook with: `$pages->addReady()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::addReady', function(HookEvent $event) {
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
$this->addHookAfter('Pages::addReady', function(HookEvent $event) {
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

## Since

3.0.253

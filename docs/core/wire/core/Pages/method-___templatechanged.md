# $pages->templateChanged(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page's template has been changed

Note the previous template is available in the `$page->templatePrevious` property.

## Usage

~~~~~
// basic usage
$result = $pages->templateChanged($page);

// usage with all arguments
$result = $pages->templateChanged(Page $page);
~~~~~

## Hookable

- Hookable method name: `templateChanged`
- Implementation: `___templateChanged`
- Hook with: `$pages->templateChanged()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::templateChanged', function(HookEvent $event) {
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
$this->addHookAfter('Pages::templateChanged', function(HookEvent $event) {
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

- `$page` `Page` Page that had its template changed.

# $pagesAccess->updatePage(Page $page)

Source: `wire/core/PagesAccess.php`

Save to pages_access table to indicate what template each page is getting its access from

This should be called when a page has been saved and its parent or template has changed.
Or, when a new page is added.

If there is no entry in this table, then the page is getting its access from its existing template.

This is used by PageFinder to determine what pages to include in a find() operation based on user access.

## Usage

~~~~~
// basic usage
$result = $pagesAccess->updatePage($page);

// usage with all arguments
$result = $pagesAccess->updatePage(Page $page);
~~~~~

## Hookable

- Hookable method name: `updatePage`
- Implementation: `___updatePage`
- Hook with: `$pagesAccess->updatePage()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesAccess::updatePage', function(HookEvent $event) {
  $pagesAccess = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PagesAccess::updatePage', function(HookEvent $event) {
  $pagesAccess = $event->object;

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

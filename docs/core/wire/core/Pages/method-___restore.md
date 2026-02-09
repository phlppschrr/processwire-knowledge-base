# $pages->restore(Page $page, $save = true): bool

Source: `wire/core/Pages.php`

Restore a page in the trash back to its original location and state

If you want to restore the page to some location other than its original location, set the `$page->parent` property
of the page to contain the location you want it to restore to. Otherwise the page will restore to its original location,
when possible to do so.

## Example

~~~~~
// Grab a page from the trash and restore it
$trashedPage = $pages->get(1234);
$pages->restore($trashedPage);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $pages->restore($page);

// usage with all arguments
$bool = $pages->restore(Page $page, $save = true);
~~~~~

## Hookable

- Hookable method name: `restore`
- Implementation: `___restore`
- Hook with: `$pages->restore()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::restore', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $save = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $save);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::restore', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $save = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page that is in the trash that you want to restore
- `$save` (optional) `bool` Set to false if you only want to prep the page for restore (i.e. you will save the page yourself later). Primarily for internal use.

## Return value

- `bool` True on success, false on failure.

## See Also

- [Pages::trash()](method-___trash.md)

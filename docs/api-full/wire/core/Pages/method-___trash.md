# $pages->trash(Page $page, $save = true): bool

Source: `wire/core/Pages.php`

Move a page to the trash

When a page is moved to the trash, it is in a "delete pending" state. Once trashed, the page can be either restored
to its original location, or permanently deleted (when the trash is emptied).

## Example

~~~~~
// Trash a product page
$product = $pages->get('/products/foo-bar-widget/');
$pages->trash($product);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $pages->trash($page);

// usage with all arguments
$bool = $pages->trash(Page $page, $save = true);
~~~~~

## Arguments

- `$page` `Page` Page to trash
- `$save` (optional) `bool` Set to false if you will perform your own save() call afterwards to complete the operation. Omit otherwise. Primarily for internal use.

## Return value

- `bool` Returns true on success, false on failure.

## Hooking

- Hookable method name: `trash`
- Implementation: `___trash`
- Hook with: `Pages::trash`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::trash', function(HookEvent $event) {
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

### Hooking After

~~~~~
$this->addHookAfter('Pages::trash', function(HookEvent $event) {
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

## Exceptions

- `WireException`

## See Also

- [Pages::restore()](method-___restore.md)
- [Pages::emptyTrash()](method-___emptytrash.md)
- [Pages::delete()](method-___delete.md)

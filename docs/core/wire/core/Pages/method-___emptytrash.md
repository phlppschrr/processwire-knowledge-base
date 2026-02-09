# $pages->emptyTrash(array $options = array()): int|array

Source: `wire/core/Pages.php`

Delete all pages in the trash

Note that once the trash is emptied, pages in the trash are permanently deleted.
This method populates error notices when there are errors deleting specific pages.

## Example

~~~~~
// Empty the trash
$pages->emptyTrash();
~~~~~

## Usage

~~~~~
// basic usage
$int = $pages->emptyTrash();

// usage with all arguments
$int = $pages->emptyTrash(array $options = array());
~~~~~

## Hookable

- Hookable method name: `emptyTrash`
- Implementation: `___emptyTrash`
- Hook with: `$pages->emptyTrash()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::emptyTrash', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::emptyTrash', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$options` (optional) `array` See PagesTrash::emptyTrash() for advanced options

## Return value

- `int|array` Returns total number of pages deleted from trash, or array if verbose option specified. This number is negative or 0 if not all pages could be deleted and error notices may be present.

## See Also

- [Pages::trash()](method-___trash.md)
- [Pages::restore()](method-___restore.md)

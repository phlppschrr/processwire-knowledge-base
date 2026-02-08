# $page->moveReady($oldParent, $newParent)

Source: `wire/core/Page.php`

Called when this Page is about to be moved to another parent

## Example

~~~~~
$wire->addHook('Page::moveReady', function($e) {
  $page = $e->object;
  list($oldParent, $newParent) = $e->arguments;
  $e->log->message("Moving page $page from $oldParent->path into $newParent->path");
  if($newParent->isTrash()) $e->log->save("trash", "Trashing page $page");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->moveReady($oldParent, $newParent);
~~~~~

## Hookable

- Hookable method name: `moveReady`
- Implementation: `___moveReady`
- Hook with: `$page->moveReady()`

## Arguments

- `$oldParent` `Page`
- `$newParent` `Page`

## Since

3.0.253

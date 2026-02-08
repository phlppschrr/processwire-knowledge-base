# $page->renamed($oldName, $newName)

Source: `wire/core/Page.php`

Called right after this page has been renamed (i.e. had its name property changed)

## Example

~~~~~
$wire->addHook('Page::renamed', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page renamed: $oldName => $newName");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->renamed($oldName, $newName);
~~~~~

## Hookable

- Hookable method name: `renamed`
- Implementation: `___renamed`
- Hook with: `$page->renamed()`

## Arguments

- `$oldName` `string` The old name
- `$newName` `string` The new name

## Since

3.0.253

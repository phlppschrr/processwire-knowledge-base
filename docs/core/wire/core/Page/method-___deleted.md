# $page->deleted()

Source: `wire/core/Page.php`

Called after this page and its data has been deleted

## Example

~~~~~
$wire->addHook('Page::deleted', function($e) {
  $page = $e->object;
  $e->warning("Page $page has been deleted");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->deleted();
~~~~~

## Hookable

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `$page->deleted()`

## Since

3.0.253

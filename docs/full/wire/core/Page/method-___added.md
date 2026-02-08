# $page->added()

Source: `wire/core/Page.php`

Called after this new Page has been added

## Example

~~~~~
$wire->addHook('Page::added', function($e) {
  $page = $e->object;
  $e->message("Added new $page->template page: $page->path");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->added();
~~~~~

## Hookable

- Hookable method name: `added`
- Implementation: `___added`
- Hook with: `$page->added()`

## Since

3.0.253

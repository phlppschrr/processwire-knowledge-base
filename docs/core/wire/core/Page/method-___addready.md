# $page->addReady()

Source: `wire/core/Page.php`

Called when this new Page about to be added and saved to the database

## Example

~~~~~
$wire->addHook('Page::addReady', function($e) {
  $page = $e->object;
  $e->message("Ready to add new $page->template page");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->addReady();
~~~~~

## Hookable

- Hookable method name: `addReady`
- Implementation: `___addReady`
- Hook with: `$page->addReady()`

## Since

3.0.253

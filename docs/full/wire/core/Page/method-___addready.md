# $page->___addReady()

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
$result = $page->___addReady();
~~~~~

## Since

3.0.253

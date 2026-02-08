# $page->___loaded()

Source: `wire/core/Page.php`

Called when this page has been loaded and is now ready and use

## Example

~~~~~
$wire->addHook('Page::loaded', function($e) {
  $e->message("Loaded page $e->object");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->___loaded();
~~~~~

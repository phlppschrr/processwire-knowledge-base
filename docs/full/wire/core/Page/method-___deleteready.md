# $page->___deleteReady()

Source: `wire/core/Page.php`

Called right before this page is deleted (and before any of its data is touched)

~~~~~
$wire->addHook('Page::deleteReady', function($e) {
  $page = $e->object;
  $e->warning("Page $page WILL be deleted");
});
~~~~~

## Since

3.0.253

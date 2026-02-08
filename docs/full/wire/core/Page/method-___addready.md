# Page::___addReady()

Source: `wire/core/Page.php`

Called when this new Page about to be added and saved to the database

~~~~~
$wire->addHook('Page::addReady', function($e) {
  $page = $e->object;
  $e->message("Ready to add new $page->template page");
});
~~~~~


@since 3.0.253

# $page->___added()

Source: `wire/core/Page.php`

Called after this new Page has been added

~~~~~
$wire->addHook('Page::added', function($e) {
  $page = $e->object;
  $e->message("Added new $page->template page: $page->path");
});
~~~~~

## Since

3.0.253

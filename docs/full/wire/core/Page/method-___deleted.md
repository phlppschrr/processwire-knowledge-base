# Page::___deleted()

Source: `wire/core/Page.php`

Called after this page and its data has been deleted

~~~~~
$wire->addHook('Page::deleted', function($e) {
  $page = $e->object;
  $e->warning("Page $page has been deleted");
});
~~~~~


@since 3.0.253

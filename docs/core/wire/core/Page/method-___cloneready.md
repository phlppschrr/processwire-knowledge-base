# Page::___cloneReady()

Source: `wire/core/Page.php`

Called right before this page is cloned

~~~~~
$wire->addHook('Page::cloneReady', function($e) {
 $page = $e->object;
 $e->log->message("Page $page is ready to be cloned");
});
~~~~~


@param Page $copy The copy of this page that it will be cloned to

@since 3.0.253

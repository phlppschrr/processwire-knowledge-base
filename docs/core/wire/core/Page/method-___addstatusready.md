# Page::___addStatusReady()

Source: `wire/core/Page.php`

Called when new status flag about to be added to page but not yet saved

~~~~~
$wire->addHook('Page::addStatusReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  if($name === 'unpublished' && $page->id === 1) {
    $page->removeStatus($name);
    $e->error("We do not allow unpublish of homepage");
  }
});
~~~~~


@param string $name Name of the status flag to be added, i.e. unpublished, hidden, trash, locked

@param int $value Value of the status flag to be added, a `Page::status*` constant

@since 3.0.253

# ProcessPageListRender::___getNumChildren()

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Hook this method if you want to manipulate the numChildren count for pages

~~~~~
$wire->addHookAfter('ProcessPageListRender::getNumChildren', function($event) {
  $page = $event->arguments(0);
  $selector = $event->arguments(1);
  $event->return = $page->numChildren($selector); // your implementation here
});
~~~~~

See Page::numChildren() for details on arguments


@param Page $page

@param string|int|bool|null $selector

@return int

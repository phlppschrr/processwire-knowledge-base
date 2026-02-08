# $processPageListRender->___getNumChildren(Page $page, $selector = null): int

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Hook this method if you want to manipulate the numChildren count for pages


See Page::numChildren() for details on arguments

## Example

~~~~~
$wire->addHookAfter('ProcessPageListRender::getNumChildren', function($event) {
  $page = $event->arguments(0);
  $selector = $event->arguments(1);
  $event->return = $page->numChildren($selector); // your implementation here
});
~~~~~

## Usage

~~~~~
// basic usage
$int = $processPageListRender->___getNumChildren($page);

// usage with all arguments
$int = $processPageListRender->___getNumChildren(Page $page, $selector = null);
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|int|bool|null`

## Return value

- `int`

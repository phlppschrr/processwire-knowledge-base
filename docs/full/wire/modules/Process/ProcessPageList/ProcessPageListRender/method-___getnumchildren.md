# $processPageListRender->getNumChildren(Page $page, $selector = null): int

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
$int = $processPageListRender->getNumChildren($page);

// usage with all arguments
$int = $processPageListRender->getNumChildren(Page $page, $selector = null);
~~~~~

## Hookable

- Hookable method name: `getNumChildren`
- Implementation: `___getNumChildren`
- Hook with: `$processPageListRender->getNumChildren()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessPageListRender::getNumChildren', function(HookEvent $event) {
  $processPageListRender = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $selector = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $selector);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessPageListRender::getNumChildren', function(HookEvent $event) {
  $processPageListRender = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $selector = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|int|bool|null`

## Return value

- `int`

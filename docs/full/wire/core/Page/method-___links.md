# $page->links($selector = '', $field = ''): PageArray

Source: `wire/core/Page.php`

Return pages linking to this one (in Textarea/HTML fields)

Applies only to Textarea fields with “html” content-type and link abstraction enabled.

## Usage

~~~~~
// basic usage
$items = $page->links();

// usage with all arguments
$items = $page->links($selector = '', $field = '');
~~~~~

## Hookable

- Hookable method name: `links`
- Implementation: `___links`
- Hook with: `$page->links()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::links', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $selector = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $selector);
  $event->arguments(1, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Page::links', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $selector = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$selector` (optional) `string|bool` Optional selector to filter by or boolean true for “include=all”. (default='')
- `$field` (optional) `string|Field` Optionally limit results to specified field. (default=all applicable Textarea fields)

## Return value

- `PageArray`

## Since

3.0.107

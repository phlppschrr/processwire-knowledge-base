# $page->references($selector = '', $field = ''): PageArray|array

Source: `wire/core/Page.php`

Return pages that have Page reference fields pointing to this one (references)

By default this excludes pages that are hidden, unpublished and pages excluded due to access control for the current user.
To prevent these exclusions specify an include mode in the selector, i.e. `include=all`, or you can use
boolean `true` as a shortcut to specify that you do not want any exclusions.

## Usage

~~~~~
// basic usage
$items = $page->references();

// usage with all arguments
$items = $page->references($selector = '', $field = '');
~~~~~

## Hookable

- Hookable method name: `references`
- Implementation: `___references`
- Hook with: `$page->references()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::references', function(HookEvent $event) {
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
$this->addHookAfter('Page::references', function(HookEvent $event) {
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

- `$selector` (optional) `string|bool` Optional selector to filter results by, or boolean true as shortcut for `include=all`.
- `$field` (optional) `Field|string|bool` Optionally limit to pages using specified field (name or Field object), - OR specify boolean TRUE to return array of PageArrays indexed by field names. - If $field argument not specified, it searches all applicable Page fields.

## Return value

- `PageArray|array`

## Since

3.0.107

# $page->getMarkup($key): string

Source: `wire/core/Page.php`

Return the markup value for a given field name or {tag} string

1. If given a field name (or `name.subname` or `name1|name2|name3`) it will return the
   markup value as defined by the fieldtype.
2. If given a string with field names referenced in `{tags}`, it will populate those
   tags and return the populated string.

## Usage

~~~~~
// basic usage
$string = $page->getMarkup($key);
~~~~~

## Hookable

- Hookable method name: `getMarkup`
- Implementation: `___getMarkup`
- Hook with: `$page->getMarkup()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::getMarkup', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $key = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $key);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Page::getMarkup', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $key = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$key` `string` Field name or markup string with field {name} tags in it

## Return value

- `string`

## See Also

- [Page::getText()](method-gettext.md)

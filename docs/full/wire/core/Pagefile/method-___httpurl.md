# $pagefile->httpUrl(): string

Source: `wire/core/Pagefile.php`

Return the web accessible URL (with scheme and hostname) to this Pagefile.

## Usage

~~~~~
// basic usage
$string = $pagefile->httpUrl();
~~~~~

## Hookable

- Hookable method name: `httpUrl`
- Implementation: `___httpUrl`
- Hook with: `$pagefile->httpUrl()`

## Hooking Before

~~~~~
$this->addHookBefore('Pagefile::httpUrl', function(HookEvent $event) {
  $pagefile = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pagefile::httpUrl', function(HookEvent $event) {
  $pagefile = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `string`

## See Also

- [Pagefile::url()](method-url.md)

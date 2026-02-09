# $pagefile->url(): string

Source: `wire/core/Pagefile.php`

Hookable version of url() method

## Usage

~~~~~
// basic usage
$string = $pagefile->url();
~~~~~

## Return value

- `string`

## Hooking

- Hookable method name: `url`
- Implementation: `___url`
- Hook with: `Pagefile::url`

### Hooking Before

~~~~~
$this->addHookBefore('Pagefile::url', function(HookEvent $event) {
  $pagefile = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pagefile::url', function(HookEvent $event) {
  $pagefile = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

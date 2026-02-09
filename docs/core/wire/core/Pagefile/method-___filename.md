# $pagefile->filename()

Source: `wire/core/Pagefile.php`

Hookable version of filename() method

## Usage

~~~~~
// basic usage
$result = $pagefile->filename();
~~~~~

## Hooking

- Hookable method name: `filename`
- Implementation: `___filename`
- Hook with: `Pagefile::filename`

### Hooking Before

~~~~~
$this->addHookBefore('Pagefile::filename', function(HookEvent $event) {
  $pagefile = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pagefile::filename', function(HookEvent $event) {
  $pagefile = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

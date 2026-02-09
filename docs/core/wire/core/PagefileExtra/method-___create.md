# $pagefileExtra->create(): bool

Source: `wire/core/PagefileExtra.php`

Create the extra file

Must be implemented by a hook or by descending class

## Usage

~~~~~
// basic usage
$bool = $pagefileExtra->create();
~~~~~

## Hookable

- Hookable method name: `create`
- Implementation: `___create`
- Hook with: `$pagefileExtra->create()`

## Hooking Before

~~~~~
$this->addHookBefore('PagefileExtra::create', function(HookEvent $event) {
  $pagefileExtra = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PagefileExtra::create', function(HookEvent $event) {
  $pagefileExtra = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `bool` Returns true on success, false on fail

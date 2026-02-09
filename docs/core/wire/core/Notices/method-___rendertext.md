# $notices->renderText(): string

Source: `wire/core/Notices.php`

Render these Notices as plain text

Note: if this ends up in HTML, such as in a `<pre>`, you should pass the returned text
through `$sanitizer->entities()` or `htmlspecialchars()` before outputting.

## Usage

~~~~~
// basic usage
$string = $notices->renderText();
~~~~~

## Return value

- `string`

## Hooking

- Hookable method name: `renderText`
- Implementation: `___renderText`
- Hook with: `Notices::renderText`

### Hooking Before

~~~~~
$this->addHookBefore('Notices::renderText', function(HookEvent $event) {
  $notices = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Notices::renderText', function(HookEvent $event) {
  $notices = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.254

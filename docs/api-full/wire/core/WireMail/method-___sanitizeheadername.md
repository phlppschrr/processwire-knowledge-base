# $wireMail->sanitizeHeaderName($name): string

Source: `wire/core/WireMail.php`

Sanitize and normalize a header name

## Usage

~~~~~
// basic usage
$string = $wireMail->sanitizeHeaderName($name);
~~~~~

## Arguments

- `$name` `string`

## Return value

- `string`

## Hooking

- Hookable method name: `sanitizeHeaderName`
- Implementation: `___sanitizeHeaderName`
- Hook with: `WireMail::sanitizeHeaderName`

### Hooking Before

~~~~~
$this->addHookBefore('WireMail::sanitizeHeaderName', function(HookEvent $event) {
  $wireMail = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireMail::sanitizeHeaderName', function(HookEvent $event) {
  $wireMail = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.132

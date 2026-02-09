# $wireMail->sanitizeHeaderValue($value): string

Source: `wire/core/WireMail.php`

Sanitize an email header header value

## Usage

~~~~~
// basic usage
$string = $wireMail->sanitizeHeaderValue($value);
~~~~~

## Hookable

- Hookable method name: `sanitizeHeaderValue`
- Implementation: `___sanitizeHeaderValue`
- Hook with: `$wireMail->sanitizeHeaderValue()`

## Hooking Before

~~~~~
$this->addHookBefore('WireMail::sanitizeHeaderValue', function(HookEvent $event) {
  $wireMail = $event->object;

  // Get arguments
  $value = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $value);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireMail::sanitizeHeaderValue', function(HookEvent $event) {
  $wireMail = $event->object;

  // Get arguments
  $value = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$value` `string`

## Return value

- `string`

## Since

3.0.132

# $wireMail->send(): int

Source: `wire/core/WireMail.php`

Send the email

Call this method only after you have specified at least the `subject`, `to` and `body`.

## Usage

~~~~~
// basic usage
$int = $wireMail->send();
~~~~~

## Return value

- `int` Returns a positive number (indicating number of addresses emailed) or 0 on failure.

## Hooking

- Hookable method name: `send`
- Implementation: `___send`
- Hook with: `WireMail::send`

### Hooking Before

~~~~~
$this->addHookBefore('WireMail::send', function(HookEvent $event) {
  $wireMail = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireMail::send', function(HookEvent $event) {
  $wireMail = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

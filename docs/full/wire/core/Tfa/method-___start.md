# $tfa->start($name, $pass): bool

Source: `wire/core/Tfa.php`

Start 2-factor authentication

On successful authentication of user, this method performs a redirect to the next step.
If user does not exist, they are not allowed to login, or fails to authenticate, this method
returns a boolean false. If user does not have 2FA enabled, or is remembered from a previous
TFA login, then this method returns true, but user still needs to be authenticated.

If preferred, you can ignore the return value, as this method will perform redirects whenever
it needs to move on to the next 2FA step.

## Usage

~~~~~
// basic usage
$bool = $tfa->start($name, $pass);
~~~~~

## Arguments

- `$name` `string`
- `$pass` `string`

## Return value

- `bool`

## Hooking

- Hookable method name: `start`
- Implementation: `___start`
- Hook with: `Tfa::start`

### Hooking Before

~~~~~
$this->addHookBefore('Tfa::start', function(HookEvent $event) {
  $tfa = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $pass = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $pass);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Tfa::start', function(HookEvent $event) {
  $tfa = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $pass = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

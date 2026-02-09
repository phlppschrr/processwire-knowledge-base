# $session->redirect($url, $status = 301)

Source: `wire/core/Session.php`

Redirect this session to another URL.

Execution halts within this function after redirect has been issued.

## Example

~~~~~
// redirect to homepage
$session->redirect('/');
~~~~~

## Usage

~~~~~
// basic usage
$result = $session->redirect($url);

// usage with all arguments
$result = $session->redirect($url, $status = 301);
~~~~~

## Arguments

- `$url` `string` URL to redirect to
- `$status` (optional) `bool|int` One of the following (or omit for 301): - `true` (bool): Permanent redirect (same as 301). - `false` (bool): Temporary redirect (same as 302). - `301` (int): Permanent redirect using GET. (3.0.166+) - `302` (int): “Found”, Temporary redirect using GET. (3.0.166+) - `303` (int): “See other”, Temporary redirect using GET. (3.0.166+) - `307` (int): Temporary redirect using current request method such as POST (repeat that request). (3.0.166+)

## Hooking

- Hookable method name: `redirect`
- Implementation: `___redirect`
- Hook with: `Session::redirect`

### Hooking Before

~~~~~
$this->addHookBefore('Session::redirect', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $url = $event->arguments(0);
  $status = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $url);
  $event->arguments(1, $status);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Session::redirect', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $url = $event->arguments(0);
  $status = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## See Also

- [Session::location()](method-location.md)

# $wire->trackException($e, $severe = true, $text = null): $this

Source: `wire/core/Wire.php`

Hookable method called when an Exception (or Error) occurs

- It will log Exception to `exceptions.txt` log if 'exceptions' is in `$config->logs`.
- It will log Error to `errors.txt` log if 'errors' is in `$config->logs`.
- It will re-throw Exception or Error if `$config->allowExceptions` is true.
- If additional `$text` is provided, it will be sent to notice method call.

Please note that if your root /index.php version is less than 302 it will only receive
Exception (and not Error) objects.

## Usage

~~~~~
// basic usage
$result = $wire->trackException($e);

// usage with all arguments
$result = $wire->trackException($e, $severe = true, $text = null);
~~~~~

## Arguments

- `$e` `\Throwable` Exception or Error object that was thrown.
- `$severe` (optional) `bool|int` Whether or not it should be considered severe (default=true).
- `$text` (optional) `string|array|object|true` Additional details (optional): - When provided, it will be sent to `$this->error($text)` if $severe is true, or `$this->warning($text)` if $severe is false. - Specify boolean `true` to just send the `$e->getMessage()` to `$this->error()` or `$this->warning()`.

## Return value

- `$this`

## Hooking

- Hookable method name: `trackException`
- Implementation: `___trackException`
- Hook with: `Wire::trackException`

### Hooking Before

~~~~~
$this->addHookBefore('Wire::trackException', function(HookEvent $event) {
  $wire = $event->object;

  // Get arguments
  $e = $event->arguments(0);
  $severe = $event->arguments(1);
  $text = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $e);
  $event->arguments(1, $severe);
  $event->arguments(2, $text);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Wire::trackException', function(HookEvent $event) {
  $wire = $event->object;

  // Get arguments
  $e = $event->arguments(0);
  $severe = $event->arguments(1);
  $text = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `\Exception|\Error` If `$severe==true` and `$config->allowExceptions==true`

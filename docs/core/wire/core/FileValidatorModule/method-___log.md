# $fileValidatorModule->log($str = '', array $options = array()): WireLog|null

Source: `wire/core/FileValidatorModule.php`

Log a message for this class

Message is saved to a log file in ProcessWire's logs path to a file with
the same name as the class, converted to hyphenated lowercase.

## Usage

~~~~~
// basic usage
$wireLog = $fileValidatorModule->log();

// usage with all arguments
$wireLog = $fileValidatorModule->log($str = '', array $options = array());
~~~~~

## Arguments

- `$str` (optional) `string` Text to log, or omit to just return the name of the log
- `$options` (optional) `array` Optional extras to include: - url (string): URL to record the with the log entry (default=auto-detect) - name (string): Name of log to use (default=auto-detect)

## Return value

- `WireLog|null`

## Hooking

- Hookable method name: `log`
- Implementation: `___log`
- Hook with: `FileValidatorModule::log`

### Hooking Before

~~~~~
$this->addHookBefore('FileValidatorModule::log', function(HookEvent $event) {
  $fileValidatorModule = $event->object;

  // Get arguments
  $str = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $str);
  $event->arguments(1, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('FileValidatorModule::log', function(HookEvent $event) {
  $fileValidatorModule = $event->object;

  // Get arguments
  $str = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

# $templateFile->fileFailed($filename, \Exception $e): bool

Source: `wire/core/TemplateFile.php`

Called when render of specific file failed with Exception

## Usage

~~~~~
// basic usage
$bool = $templateFile->fileFailed($filename, $e);

// usage with all arguments
$bool = $templateFile->fileFailed($filename, \Exception $e);
~~~~~

## Arguments

- `$filename` `string`
- `$e` `\Exception`

## Return value

- `bool` True if Exception $e should be thrown, false if it should be ignored

## Hooking

- Hookable method name: `fileFailed`
- Implementation: `___fileFailed`
- Hook with: `TemplateFile::fileFailed`

### Hooking Before

~~~~~
$this->addHookBefore('TemplateFile::fileFailed', function(HookEvent $event) {
  $templateFile = $event->object;

  // Get arguments
  $filename = $event->arguments(0);
  $e = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $filename);
  $event->arguments(1, $e);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('TemplateFile::fileFailed', function(HookEvent $event) {
  $templateFile = $event->object;

  // Get arguments
  $filename = $event->arguments(0);
  $e = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.154

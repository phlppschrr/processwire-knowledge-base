# $fileCompiler->compile($sourceFile): string

Source: `wire/core/FileCompiler.php`

Compile given source file and return compiled destination file

## Usage

~~~~~
// basic usage
$string = $fileCompiler->compile($sourceFile);
~~~~~

## Arguments

- `$sourceFile` `string` Source file to compile (relative to sourcePath given in constructor)

## Return value

- `string` Full path and filename of compiled file. Returns sourceFile is compilation is not necessary.

## Hooking

- Hookable method name: `compile`
- Implementation: `___compile`
- Hook with: `FileCompiler::compile`

### Hooking Before

~~~~~
$this->addHookBefore('FileCompiler::compile', function(HookEvent $event) {
  $fileCompiler = $event->object;

  // Get arguments
  $sourceFile = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $sourceFile);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('FileCompiler::compile', function(HookEvent $event) {
  $fileCompiler = $event->object;

  // Get arguments
  $sourceFile = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if given invalid sourceFile

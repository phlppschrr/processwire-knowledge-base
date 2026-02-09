# $fileCompiler->compileData($data, $sourceFile): string

Source: `wire/core/FileCompiler.php`

Compile the given string of data

## Usage

~~~~~
// basic usage
$string = $fileCompiler->compileData($data, $sourceFile);
~~~~~

## Hookable

- Hookable method name: `compileData`
- Implementation: `___compileData`
- Hook with: `$fileCompiler->compileData()`

## Hooking Before

~~~~~
$this->addHookBefore('FileCompiler::compileData', function(HookEvent $event) {
  $fileCompiler = $event->object;

  // Get arguments
  $data = $event->arguments(0);
  $sourceFile = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $data);
  $event->arguments(1, $sourceFile);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('FileCompiler::compileData', function(HookEvent $event) {
  $fileCompiler = $event->object;

  // Get arguments
  $data = $event->arguments(0);
  $sourceFile = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$data` `string`
- `$sourceFile` `string`

## Return value

- `string`

# $processFieldExportImport->processImport()

Source: `wire/modules/Process/ProcessField/ProcessFieldExportImport.php`

Commit changed field data

## Usage

~~~~~
// basic usage
$result = $processFieldExportImport->processImport();
~~~~~

## Hookable

- Hookable method name: `processImport`
- Implementation: `___processImport`
- Hook with: `$processFieldExportImport->processImport()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessFieldExportImport::processImport', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessFieldExportImport::processImport', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

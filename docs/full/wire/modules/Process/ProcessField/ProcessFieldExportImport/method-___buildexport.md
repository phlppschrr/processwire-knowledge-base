# $processFieldExportImport->buildExport(): InputfieldForm

Source: `wire/modules/Process/ProcessField/ProcessFieldExportImport.php`

Execute export

## Usage

~~~~~
// basic usage
$inputfieldForm = $processFieldExportImport->buildExport();
~~~~~

## Hookable

- Hookable method name: `buildExport`
- Implementation: `___buildExport`
- Hook with: `$processFieldExportImport->buildExport()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessFieldExportImport::buildExport', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessFieldExportImport::buildExport', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `InputfieldForm`

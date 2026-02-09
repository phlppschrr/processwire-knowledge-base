# $processTemplateExportImport->processImport()

Source: `wire/modules/Process/ProcessTemplate/ProcessTemplateExportImport.php`

Commit changed field data

## Usage

~~~~~
// basic usage
$result = $processTemplateExportImport->processImport();
~~~~~

## Hookable

- Hookable method name: `processImport`
- Implementation: `___processImport`
- Hook with: `$processTemplateExportImport->processImport()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessTemplateExportImport::processImport', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessTemplateExportImport::processImport', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

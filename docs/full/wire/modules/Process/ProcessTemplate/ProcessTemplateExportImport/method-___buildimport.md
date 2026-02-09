# $processTemplateExportImport->buildImport(): string

Source: `wire/modules/Process/ProcessTemplate/ProcessTemplateExportImport.php`

Execute import

## Usage

~~~~~
// basic usage
$string = $processTemplateExportImport->buildImport();
~~~~~

## Hookable

- Hookable method name: `buildImport`
- Implementation: `___buildImport`
- Hook with: `$processTemplateExportImport->buildImport()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessTemplateExportImport::buildImport', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessTemplateExportImport::buildImport', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `string`

## Exceptions

- `WireException` if given invalid import data

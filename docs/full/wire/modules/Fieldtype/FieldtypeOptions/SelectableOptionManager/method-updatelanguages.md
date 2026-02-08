# $selectableOptionManager->updateLanguages(?HookEvent $event = null)

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Hook method called when a language is added or deleted

Also called when module is installed

## Usage

~~~~~
// basic usage
$result = $selectableOptionManager->updateLanguages();

// usage with all arguments
$result = $selectableOptionManager->updateLanguages(?HookEvent $event = null);
~~~~~

## Arguments

- `$event` (optional) `HookEvent|null`

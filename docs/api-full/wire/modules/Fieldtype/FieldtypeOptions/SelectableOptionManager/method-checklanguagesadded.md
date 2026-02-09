# $selectableOptionManager->checkLanguagesAdded($languageAdded = null): array

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Check for added languages

## Usage

~~~~~
// basic usage
$array = $selectableOptionManager->checkLanguagesAdded();

// usage with all arguments
$array = $selectableOptionManager->checkLanguagesAdded($languageAdded = null);
~~~~~

## Arguments

- `$languageAdded` (optional) `Language|null`

## Return value

- `array` SQL statements to add language when appropriate

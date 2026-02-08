# $selectableOptionManager->checkLanguagesDeleted($languageDeleted = null): array

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Check for deleted languages

## Usage

~~~~~
// basic usage
$array = $selectableOptionManager->checkLanguagesDeleted();

// usage with all arguments
$array = $selectableOptionManager->checkLanguagesDeleted($languageDeleted = null);
~~~~~

## Arguments

- `$languageDeleted` (optional) `Language|null`

## Return value

- `array` SQL statements to delete language when appropriate

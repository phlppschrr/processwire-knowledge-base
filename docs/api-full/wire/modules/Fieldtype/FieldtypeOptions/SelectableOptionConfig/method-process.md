# $selectableOptionConfig->process(Inputfield $inputfield)

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionConfig.php`

Custom processing for the options string in getConfigInputfields

Detects and confirms option deletions.

## Usage

~~~~~
// basic usage
$result = $selectableOptionConfig->process($inputfield);

// usage with all arguments
$result = $selectableOptionConfig->process(Inputfield $inputfield);
~~~~~

## Arguments

- `$inputfield` `Inputfield` For the _options inputfield

## Exceptions

- `WireException`

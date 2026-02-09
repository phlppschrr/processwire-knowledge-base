# $inputfieldDatetimeType->processInput(WireInputData $input): int|string|bool

Source: `wire/modules/Inputfield/InputfieldDatetime/InputfieldDatetimeType.php`

Process input

## Usage

~~~~~
// basic usage
$int = $inputfieldDatetimeType->processInput($input);

// usage with all arguments
$int = $inputfieldDatetimeType->processInput(WireInputData $input);
~~~~~

## Arguments

- `$input` `WireInputData`

## Return value

- `int|string|bool` Int for UNIX timestamp date, blank string for no date, or boolean false if InputfieldDatetime should process input

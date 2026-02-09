# $wireDateTime->getTimeFormats(): array

Source: `wire/core/WireDateTime.php`

Return all predefined PHP date() formats for use as times

## Example

~~~~~
// output all time formats
$formats = $datetime->getTimeFormats();
echo "<pre>" . print_r($formats, true) . "</pre>";
~~~~~

## Usage

~~~~~
// basic usage
$array = $wireDateTime->getTimeFormats();
~~~~~

## Return value

- `array` Returns an array of strings containing recognized time formats

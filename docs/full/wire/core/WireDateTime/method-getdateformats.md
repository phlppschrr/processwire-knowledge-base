# $wireDateTime->getDateFormats(): array

Source: `wire/core/WireDateTime.php`

Return all predefined PHP date() formats for use as dates

## Example

~~~~~
// output all date formats
$formats = $datetime->getDateFormats();
echo "<pre>" . print_r($formats, true) . "</pre>";
~~~~~

## Usage

~~~~~
// basic usage
$array = $wireDateTime->getDateFormats();
~~~~~

## Return value

- `array` Returns an array of strings containing recognized date formats

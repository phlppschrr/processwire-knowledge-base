# $wireDateTime->getTimeFormats(): array

Source: `wire/core/WireDateTime.php`

Return all predefined PHP date() formats for use as times

~~~~~
// output all time formats
$formats = $datetime->getTimeFormats();
echo "<pre>" . print_r($formats, true) . "</pre>";
~~~~~

## Return value

array Returns an array of strings containing recognized time formats

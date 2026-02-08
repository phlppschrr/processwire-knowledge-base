# WireDateTime::getDateFormats()

Source: `wire/core/WireDateTime.php`

Return all predefined PHP date() formats for use as dates

~~~~~
// output all date formats
$formats = $datetime->getDateFormats();
echo "<pre>" . print_r($formats, true) . "</pre>";
~~~~~


@return array Returns an array of strings containing recognized date formats

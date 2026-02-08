# WireFileTools::getAllCSV()

Source: `wire/core/WireFileTools.php`

Get all rows from a CSV file

This simplifies the reading of a CSV file by abstracting file-open, get-header, get-rows and file-close
operations into a single method call, where all those operations are handled internally. All you have to
do is call the `$files->getAllCSV($filename)` method once and it will return an array of arrays (one per row).
This method will also skip over blank rows by default, unlike PHP’s fgetcsv() which will return a 1-column row
with null value.

This method is limited by available memory, so when working with potentially large files, you should use the
`$files->getCSV()` method instead, which reads the CSV file row-by-row rather than all at once.

Note for the method `$options` argument that the `length`, `separator`, `enclosure` and `escape` options
all correspond to the identically named PHP [fgetcsv](https://www.php.net/manual/en/function.fgetcsv.php)
arguments.

Example foods.csv file (first row is header):
~~~~~
Food,Type,Color
Apple,Fruit,Red
Banana,Fruit,Yellow
Spinach,Vegetable,Green
~~~~~
Example of reading the foods.csv file above:
~~~~~
$rows = $files->getAllCSV('/path/to/foods.csv');
foreach($rows as $row) {
  echo "Food: $row[Food] ";
  echo "Type: $row[Type] ";
  echo "Color: $row[Color] ";
}
~~~~~


@param string $filename CSV filename to read from

@param array $options
 - `header` (bool|array): Indicate whether CSV has header and how it should be used (default=true):
    True to treat first line as header and return rows as associative arrays indexed by the header values.
    False to indicate there is no header and/or to indicate it should return regular non-associative PHP arrays for rows.
    Array to use it as the header and return rows as associative arrays indexed by your values.
 - `length` (int): Optional. When specified, must be greater than the longest line (in characters) to be found in the CSV file
    (allowing for trailing line-end characters). Otherwise the line is split in chunks of length characters, unless the split
    would occur inside an enclosure. Omitting this parameter (or setting it to 0, or null in PHP 8.0.0 or later) the maximum
    line length is not limited, which is slightly slower. (default=0)
 - `separator` (string): The field separator/delimiter, one single-byte character only. (default=',')
 - `enclosure` (string): The field enclosure character, one single-byte character only. (default='"')
 - `escape` (string): The escape character, at most one single-byte character. An empty string ("") disables the proprietary
    escape mechanism. (default="\\")
 - `convert` (bool): Convert digit-only strings to integers? (default=false)
 - `blanks` (bool): Allow blank rows? (default=false)

@return array

@see https://www.php.net/manual/en/function.fgetcsv.php

@see getCSV()

@since 3.0.197

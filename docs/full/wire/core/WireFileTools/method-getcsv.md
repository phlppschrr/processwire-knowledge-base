# $wireFileTools->getCSV($filename, array $options = array()): array|false

Source: `wire/core/WireFileTools.php`

Get next row from a CSV file

This simplifies the reading of a CSV file by abstracting file-open, get-header, get-rows and file-close
operations into a single method call, where all those operations are handled internally. All you have to
do is keep calling the `$files->getCSV($filename)` method until it returns false. This method will also
skip over blank rows by default, unlike PHP’s fgetcsv() which will return a 1-column row with null value.

This method should always be used in a loop, meaning you must keep calling it until it returns false.
Otherwise a CSV file may be unintentionally left open. If you can't do that then use getAllCSV() instead.

For the method `$options` argument note that the `length`, `separator`, `enclosure` and `escape` options
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
while($row = $files->getCSV('/path/to/foods.csv')) {
  echo "Food: $row[Food] ";
  echo "Type: $row[Type] ";
  echo "Color: $row[Color] ";
}
~~~~~

## Arguments

- `$filename` `string` CSV filename to read from
- `$options` (optional) `array` - `header` (bool|array): Indicate whether CSV has header and how it should be used (default=true): True to treat first line as header and return rows as associative arrays indexed by the header values. False to indicate there is no header and/or to indicate it should return regular non-associative PHP arrays for rows. Array to use it as the header and return rows as associative arrays indexed by your values. - `length` (int): Optional. When specified, must be greater than the longest line (in characters) to be found in the CSV file (allowing for trailing line-end characters). Otherwise the line is split in chunks of length characters, unless the split would occur inside an enclosure. Omitting this parameter (or setting it to 0, or null in PHP 8.0.0 or later) the maximum line length is not limited, which is slightly slower. (default=0) - `separator` (string): The field separator/delimiter, one single-byte character only. (default=',') - `enclosure` (string): The field enclosure character, one single-byte character only. (default='"') - `escape` (string): The escape character, at most one single-byte character. An empty string ("") disables the proprietary escape mechanism. (default="\\") - `blanks` (bool): Allow blank rows? (default=false) - `convert` (bool): Convert digit-only strings to integers? (default=false)

## Return value

array|false Returns array for next row or boolean false when there are no more rows.

## See also

- [https://www.php.net/manual/en/function.fgetcsv.php](https://www.php.net/manual/en/function.fgetcsv.php)
- getAllCSV()

## Since

3.0.197

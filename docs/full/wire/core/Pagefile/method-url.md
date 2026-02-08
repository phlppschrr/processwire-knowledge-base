# $pagefile->url(): string

Source: `wire/core/Pagefile.php`

Return the web accessible URL to this Pagefile.

## Example

~~~~~
// Example of using the url method/property
foreach($page->files as $file) {
  echo "<li><a href='$file->url'>$file->description</a></li>";
}
~~~~~

## Usage

~~~~~
// basic usage
$string = $pagefile->url();
~~~~~

## Return value

- `string`

## See Also

- Pagefile:httpUrl()

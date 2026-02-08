# $pagefile->url(): string

Source: `wire/core/Pagefile.php`

Return the web accessible URL to this Pagefile.

~~~~~
// Example of using the url method/property
foreach($page->files as $file) {
  echo "<li><a href='$file->url'>$file->description</a></li>";
}
~~~~~

## Return value

string

## See also

- Pagefile:httpUrl()

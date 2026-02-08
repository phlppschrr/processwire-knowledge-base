# $pagesVersions->getPageVersionInfos(Page $page, array $options = []): PageVersionInfo[]

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get just PageVersionInfo objects for all versions of given page

This is the same as using the getPageVersions() method with the `getInfo` option.


~~~~~
$page = $pages->get(1234);
$infos = $pagesVersions->getPageVersionInfos($page);
foreach($infos as $info) {
  echo "<li>$info->version: $descriptionHtml</li>"; // i.e. "2: Hello world"
}
~~~~~

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `sort`: Sort by property, one of: 'created', '-created', 'version', '-version' (default='-created')

## Return value

PageVersionInfo[]

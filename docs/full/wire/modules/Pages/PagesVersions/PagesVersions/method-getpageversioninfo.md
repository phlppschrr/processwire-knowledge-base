# PagesVersions::getPageVersionInfo()

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get info for given page and version

~~~~~
// get info for version 2
$info = $pagesVersions->getPageVersionInfo($page, 2);
if($info) {
  echo "Version: $info->version <br />";
  echo "Created: $info->createdStr by {$info->createdUser->name} <br />";
  echo "Description: $info->descriptionHtml";
} else {
  echo "Version does not exist";
}
~~~~~


@param Page $page

@param int $version

@return PageVersionInfo|null

# $pagefilesManager->getFile($name): Pagefile|Pageimage|null

Source: `wire/core/PagefilesManager.php`

Get the Pagefile object containing the given filename.

## Arguments

- string $name Name of file to get: - If given a URL or path, this will traverse to other pages. - If given a basename, it will stay with current page.

## Return value

Pagefile|Pageimage|null Returns Pagefile or Pageimage object if found, or null if not.

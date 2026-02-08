# Pages::getByPath()

Source: `wire/core/Pages.php`

Get a page by its path, similar to $pages->get('/path/to/page/') but with more options

1. There are no exclusions for page status or access. If needed, you should validate access
   on any page returned from this method.
2. In a multi-language environment, you must specify the `$useLanguages` option to be true, if you
   want a result for a $path that is (or might be) a multi-language path. Otherwise, multi-language
   paths will make this method return a NullPage (or 0 if getID option is true).
3. Partial paths may also match, so long as the partial path is completely unique in the site.
   If you don't want that behavior, double check the path of the returned page.

~~~~~
// Get a page by path
$p = $pages->getByPath('/skyscrapers/atlanta/191-peachtree/');

// Now validate that the page we retrieved is valid
if($p->id && $p->viewable()) {
  // Page is valid to display
}

// Get a page by path with options
$p = $pages->getByPath('/products/widget/', [
  'useLanguages' => true,
  'useHistory' => true
]);
~~~~~


@param string $path Path of page you want to retrieve.

@param array|bool $options array of options (below), or specify boolean for $useLanguages option only.
 - `getID` (int): Specify true to just return the page ID (default=false).
 - `useLanguages` (bool): Specify true to allow retrieval by language-specific paths (default=false).
 - `useHistory` (bool): Allow use of previous paths used by the page, if PagePathHistory module is installed (default=false).
 - `allowUrl` (bool): Allow getting page by path OR url? Specify false to find only by path. This option only applies if
    the site happens to run from a subdirectory. (default=true) 3.0.184+
 - `allowPartial` (bool): Allow partial paths to match? (default=true) 3.0.184+
 - `allowUrlSegments` (bool): Allow paths with URL segments to match? When true and page match cannot be found, the closest
    parent page that allows URL segments will be returned. Found URL segments are populated to a `_urlSegments` array
    property on the returned page object. This also cancels the allowPartial setting. (default=false) 3.0.184+

@return Page|int

@since 3.0.6

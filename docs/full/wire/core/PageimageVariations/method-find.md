# $pageimageVariations->find(array $options = array()): Pageimages|array|int

Source: `wire/core/PageimageVariations.php`

Get all size variations of this image

This is useful after a delete of an image (for example). This method can be used to track down all the
child files that also need to be deleted.

## Arguments

- array $options Optional, one or more options in an associative array of the following: - `info` (bool): when true, method returns variation info arrays rather than Pageimage objects (default=false). - `count` (bool): when true, only a count of variations is returned (default=false). - `verbose` (bool|int): Return verbose array of info. If false, returns only filenames (default=true). This option does nothing unless the `info` option is true. Also note that if verbose is false, then all options following this one no longer apply (since it is no longer returning width/height info). When integer 1, returned info array also includes Pageimage variation options in 'pageimage' index of returned arrays (since 3.0.137). - `width` (int): only variations with given width will be returned - `height` (int): only variations with given height will be returned - `width>=` (int): only variations with width greater than or equal to given will be returned - `height>=` (int): only variations with height greater than or equal to given will be returned - `width<=` (int): only variations with width less than or equal to given will be returned - `height<=` (int): only variations with height less than or equal to given will be returned - `suffix` (string): only variations having the given suffix will be returned - `suffixes` (array): only variations having one of the given suffixes will be returned - `noSuffix` (string): exclude variations having this suffix - `noSuffixes` (array): exclude variations having any of these suffixes - `name` (string): only variations containing this text in filename will be returned (case insensitive) - `noName` (string): only variations NOT containing this text in filename will be returned (case insensitive) - `regexName` (string): only variations that match this PCRE regex will be returned

## Return value

Pageimages|array|int Returns Pageimages array of Pageimage instances. Only returns regular array if provided `$options['info']` is true. Returns integer if count option is specified.

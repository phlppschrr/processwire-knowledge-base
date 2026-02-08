# PageimageVariations

Source: `wire/core/PageimageVariations.php`

ProcessWire PageimageVariations

Helper class for Pageimage that handles variation collection methods

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

@since 3.0.137

## __construct()

Construct

@param Pageimage $pageimage

## count()

Return a total or filtered count of variations

This method is also here to implement the Countable interface.

@param array $options See options for find() method

@return int

## getInfo()

Given a file name (basename), return array of info if this is a variation for this instance’s file, or false if not.

Returned array includes the following indexes:

- `original` (string): Original basename
- `url` (string): URL to image
- `path` (string): Full path + filename to image
- `width` (int): Specified width in filename
- `height` (int): Specified height in filename
- `actualWidth` (int): Actual width when checked manually
- `actualHeight` (int): Acual height when checked manually
- `crop` (string): Cropping info string or blank if none
- `suffix` (array): Array of suffixes

The following are only present if variation is based on another variation, and thus has a parent variation
image between it and the original:

- `suffixAll` (array): Contains all suffixes including among parent variations
- `parent` (array): Variation info array of direct parent variation file

@param string $basename Filename to check (basename, which excludes path)

@param array|bool $options Array of options to modify behavior, or boolean to only specify `allowSelf` option.
 - `allowSelf` (bool): When true, it will return variation info even if same as current Pageimage. (default=false)
 - `verbose` (bool): Return verbose array of info? If false, just returns basename (string) or false. (default=true)

@return bool|string|array Returns false if not a variation, or array (verbose) or string (non-verbose) of info if it is.

## find()

Get all size variations of this image

This is useful after a delete of an image (for example). This method can be used to track down all the
child files that also need to be deleted.

@param array $options Optional, one or more options in an associative array of the following:
	- `info` (bool): when true, method returns variation info arrays rather than Pageimage objects (default=false).
 - `count` (bool): when true, only a count of variations is returned (default=false).
 - `verbose` (bool|int): Return verbose array of info. If false, returns only filenames (default=true).
    This option does nothing unless the `info` option is true. Also note that if verbose is false, then all options
    following this one no longer apply (since it is no longer returning width/height info).
    When integer 1, returned info array also includes Pageimage variation options in 'pageimage' index of
    returned arrays (since 3.0.137).
	- `width` (int): only variations with given width will be returned
	- `height` (int): only variations with given height will be returned
	- `width>=` (int): only variations with width greater than or equal to given will be returned
	- `height>=` (int): only variations with height greater than or equal to given will be returned
	- `width<=` (int): only variations with width less than or equal to given will be returned
	- `height<=` (int): only variations with height less than or equal to given will be returned
	- `suffix` (string): only variations having the given suffix will be returned
 - `suffixes` (array): only variations having one of the given suffixes will be returned
 - `noSuffix` (string): exclude variations having this suffix
 - `noSuffixes` (array): exclude variations having any of these suffixes
 - `name` (string): only variations containing this text in filename will be returned (case insensitive)
 - `noName` (string): only variations NOT containing this text in filename will be returned (case insensitive)
 - `regexName` (string): only variations that match this PCRE regex will be returned

@return Pageimages|array|int Returns Pageimages array of Pageimage instances.
 Only returns regular array if provided `$options['info']` is true.
 Returns integer if count option is specified.

## rebuild()

Rebuilds variations of this image

By default, this excludes crops and images with suffixes, but can be overridden with the `$mode` and `$suffix` arguments.

**Options for $mode argument**

- `0` (int): Rebuild only non-suffix, non-crop variations, and those w/suffix specified in $suffix argument. ($suffix is INCLUSION list)
- `1` (int): Rebuild all non-suffix variations, and those w/suffix specifed in $suffix argument. ($suffix is INCLUSION list)
- `2` (int): Rebuild all variations, except those with suffix specified in $suffix argument. ($suffix is EXCLUSION list)
- `3` (int): Rebuild only variations specified in the $suffix argument. ($suffix is ONLY-INCLUSION list)
- `4` (int): Rebuild only non-proportional, non-crop variations (variations that specify both width and height)

Mode 0 is the only truly safe mode, as in any other mode there are possibilities that the resulting
rebuild of the variation may not be exactly what was intended. The issues with other modes primarily
arise when the suffix means something about the technical details of the produced image, or when
rebuilding variations that include crops from an original image that has since changed dimensions or crops.

@param int $mode See the options for $mode argument above (default=0).

@param array $suffix Optional argument to specify suffixes to include or exclude (according to $mode).

@param array $options See $options for `Pageimage::size()` for details.

@return array Returns an associative array with with the following indexes:
 - `rebuilt` (array): Names of files that were rebuilt.
 - `skipped` (array): Names of files that were skipped.
 - `errors` (array): Names of files that had errors.
 - `reasons` (array): Reasons why files were skipped or had errors, associative array indexed by file name.

## remove()

Delete all the alternate sizes associated with this Pageimage

@param array $options See options for getVariations() method to limit what variations are removed, plus these:
 - `dryRun` (bool): Do not remove now and instead only return the filenames of variations that would be deleted (default=false).
 - `getFiles` (bool): Return deleted filenames? Also assumed if the test option is used (default=false).

@return $this|array Returns $this by default, or array of deleted filenames if the `getFiles` option is specified

## removeExtras()

Remove extras

@param Pageimage $pageimage

@param array $deletedFiles

@param array $options See options for remove() method

# PagefileExtra

Source: `wire/core/PagefileExtra.php`

Extra extension for Pagefile or Pageimage objects

Properties
==========

@property string $url Local URL/path to file

@property string $httpUrl Full HTTP URL with scheme and host

@property string $URL No-cache version of url

@property string $HTTPURL No-cache version of httpUrl

@property string $filename Full disk path/file

@property string $pathname Alias of filename

@property string $basename Just the basename without path

@property string $extension File extension

@property string $ext Alias of extension

@property bool $exists Does the file exist?

@property int $filesize Size of file in bytes

@property string $filesizeStr Human readable size of file

@property Pagefile|Pageimage $pagefile Source Pageimage object

@property int $savings Bytes saved by this extra

@property string $savingsStr Human readable savings by this extra

@property string $savingsPct Percent savings by this extra

The following properties affect the behavior of the URL-related methods
=======================================================================

@property bool $useSrcUrlOnFail Use source Pagefile URL if extra image does not exist and cannot be created? (default=false)

@property bool $useSrcUrlOnSize Use source Pagefile URL if extra file is larger than source file? (default=false)

@property bool $useSrcExt Use longer filenames that also include the Pagefile’s extension? (default=false)

Hookable methods
================

@method bool create()

@method string noCacheURL($http = false)

## __construct()

Construct

@param Pagefile|Pageimage $pagefile

@param $extension

## setPagefile()

Set Pagefile instance this extra is connected to

@param Pagefile $pagefile

## setExtension()

Set extension for this extra

@param $extension

## exists()

Does the extra file currently exist?

@param bool $clear Clear stat cache before checking? (default=false)

@return bool

## filesize()

Return the file size in bytes

@return int

## filesizeStr()

Return human readable file size string

@return string

## filename()

Return the full server disk path to the extra file, whether it exists or not

@return string

## basename()

Return just the basename (no path)

@return string

## url()

Return the URL to the extra file, creating it if it does not already exist

@param bool $fallback Allow falling back to source Pagefile URL when appropriate?

@return string

## httpUrl()

Return the HTTP URL to the extra file

@return string

## ___noCacheURL()

Get cache busted URL

@param bool $http

@return string

@since 3.0.194

## unlink()

Unlink/delete the extra file

@return bool

## rename()

Rename the extra file to be consistent with Pagefile name

@return bool

## ___create()

Create the extra file

Must be implemented by a hook or by descending class

@return bool Returns true on success, false on fail

## get()

Get property

@param string $key

@return bool|int|mixed|null|string

## __toString()

@return string

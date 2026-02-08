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

Methods:
Method: [__construct()](method-__construct.md)
Method: [setPagefile()](method-setpagefile.md)
Method: [setExtension()](method-setextension.md)
Method: [exists()](method-exists.md)
Method: [filesize()](method-filesize.md)
Method: [filesizeStr()](method-filesizestr.md)
Method: [filename()](method-filename.md)
Method: [basename()](method-basename.md)
Method: [url()](method-url.md)
Method: [httpUrl()](method-httpurl.md)
Method: [___noCacheURL()](method-___nocacheurl.md)
Method: [unlink()](method-unlink.md)
Method: [rename()](method-rename.md)
Method: [___create()](method-___create.md)
Method: [get()](method-get.md)
Method: [__toString()](method-__tostring.md)

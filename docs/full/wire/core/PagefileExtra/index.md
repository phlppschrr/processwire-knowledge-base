# PagefileExtra

Source: `wire/core/PagefileExtra.php`

Inherits: `WireData`

Extra extension for Pagefile or Pageimage objects

Properties
==========

- [$url: string](method-url.md) Local URL/path to file
- [$httpUrl: string](method-httpurl.md) Full HTTP URL with scheme and host
- $URL: string No-cache version of url
- $HTTPURL: string No-cache version of httpUrl
- [$filename: string](method-filename.md) Full disk path/file
- $pathname: string Alias of filename
- [$basename: string](method-basename.md) Just the basename without path
- $extension: string File extension
- $ext: string Alias of extension
- [$exists: bool](method-exists.md) Does the file exist?
- [$filesize: int](method-filesize.md) Size of file in bytes
- [$filesizeStr: string](method-filesizestr.md) Human readable size of file
- $pagefile: Pagefile|Pageimage Source Pageimage object
- $savings: int Bytes saved by this extra
- $savingsStr: string Human readable savings by this extra
- $savingsPct: string Percent savings by this extra

The following properties affect the behavior of the URL-related methods
=======================================================================

- $useSrcUrlOnFail: bool Use source Pagefile URL if extra image does not exist and cannot be created? (default=false)
- $useSrcUrlOnSize: bool Use source Pagefile URL if extra file is larger than source file? (default=false)
- $useSrcExt: bool Use longer filenames that also include the Pagefile’s extension? (default=false)

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
Method: [noCacheURL()](method-___nocacheurl.md) (hookable)
Method: [unlink()](method-unlink.md)
Method: [rename()](method-rename.md)
Method: [create()](method-___create.md) (hookable)
Method: [get()](method-get.md)
Method: [__toString()](method-__tostring.md)

Hookable methods
================

- [create(): bool](method-___create.md)
- [noCacheURL($http = false): string](method-___nocacheurl.md)

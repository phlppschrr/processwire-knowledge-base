# PagefileExtra

Source: `wire/core/PagefileExtra.php`

Inherits: `WireData`

## Summary

Extra extension for Pagefile or Pageimage objects

Common methods:
- [`setPagefile()`](method-setpagefile.md)
- [`setExtension()`](method-setextension.md)
- [`exists()`](method-exists.md)
- [`filesize()`](method-filesize.md)
- [`filesizeStr()`](method-filesizestr.md)

## Properties

- [`$url: string`](method-url.md) Local URL/path to file
- [`$httpUrl: string`](method-httpurl.md) Full HTTP URL with scheme and host
- `$URL: string` No-cache version of url
- `$HTTPURL: string` No-cache version of httpUrl
- [`$filename: string`](method-filename.md) Full disk path/file
- `$pathname: string` Alias of filename
- [`$basename: string`](method-basename.md) Just the basename without path
- `$extension: string` File extension
- `$ext: string` Alias of extension
- [`$exists: bool`](method-exists.md) Does the file exist?
- [`$filesize: int`](method-filesize.md) Size of file in bytes
- [`$filesizeStr: string`](method-filesizestr.md) Human readable size of file
- `$pagefile: Pagefile|Pageimage` Source Pageimage object
- `$savings: int` Bytes saved by this extra
- `$savingsStr: string` Human readable savings by this extra
- `$savingsPct: string` Percent savings by this extra

## The Following Properties Affect The Behavior Of The Url-Related Methods

- `$useSrcUrlOnFail: bool` Use source Pagefile URL if extra image does not exist and cannot be created? (default=false)
- `$useSrcUrlOnSize: bool` Use source Pagefile URL if extra file is larger than source file? (default=false)
- `$useSrcExt: bool` Use longer filenames that also include the Pagefile’s extension? (default=false)

## Hookable Methods

- [`create(): bool`](method-___create.md)
- [`noCacheURL($http = false): string`](method-___nocacheurl.md)

## Methods
- [`__construct(Pagefile $pagefile, $extension)`](method-__construct.md) Construct
- [`setPagefile(Pagefile $pagefile)`](method-setpagefile.md) Set Pagefile instance this extra is connected to
- [`setExtension($extension)`](method-setextension.md) Set extension for this extra
- [`exists(bool $clear = false): bool`](method-exists.md) Does the extra file currently exist?
- [`filesize(): int`](method-filesize.md) Return the file size in bytes
- [`filesizeStr(): string`](method-filesizestr.md) Return human readable file size string
- [`filename(): string`](method-filename.md) Return the full server disk path to the extra file, whether it exists or not
- [`basename(): string`](method-basename.md) Return just the basename (no path)
- [`url(bool $fallback = true): string`](method-url.md) Return the URL to the extra file, creating it if it does not already exist
- [`httpUrl(): string`](method-httpurl.md) Return the HTTP URL to the extra file
- [`noCacheURL(bool $http = false): string`](method-___nocacheurl.md) (hookable) Get cache busted URL
- [`unlink(): bool`](method-unlink.md) Unlink/delete the extra file
- [`rename(): bool`](method-rename.md) Rename the extra file to be consistent with Pagefile name
- [`create(): bool`](method-___create.md) (hookable) Create the extra file
- [`get(string $key): bool|int|mixed|null|string`](method-get.md) Get property
- [`__toString(): string`](method-__tostring.md)

# Pagefile: other

Source: `wire/core/Pagefile.php`

- [`$url: string`](method-url.md) URL to the file on the server.
- [`$httpUrl: string`](method-___httpurl.md) URL to the file on the server including scheme and hostname.
- `$URL: string` Same as $url property but with browser cache busting query string appended.
- `$HTTPURL: string` Same as the cache-busting uppercase “URL” property, but includes scheme and hostname.
- [`$filename: string`](method-filename.md) full disk path to the file on the server.
- `$name: string` Returns the filename without the path, same as the "basename" property.
- [`$hash: string`](method-hash.md) Get a unique hash (for the page) representing this Pagefile.
- [`$basename: string`](method-basename.md) Returns the filename without the path.
- [`$description: string`](method-description.md) Value of the file’s description field (string), if enabled. Note you can also set this property directly.
- [`$ext: string`](method-ext.md) File’s extension (i.e. last 3 or so characters)
- [`$filesize: int`](method-filesize.md) File size (number of bytes).
- [`$filesizeStr: string`](method-filesizestr.md) File size as a formatted string, i.e. “123 Kb”.
- `$pagefiles: Pagefiles` The Pagefiles WireArray that contains this file.
- `$page: Page` The Page object that this file is part of.
- `$field: Field` The Field object that this file is part of.
- [`$filedata: array`](method-filedata.md)
- `$created_users_id: int` ID of user that added/uploaded the file or 0 if not known (3.0.154+).
- `$modified_users_id: int` ID of user that last modified the file or 0 if not known (3.0.154+).
- `$createdUser: User|NullPage` User that added/uploaded the file or NullPage if not known (3.0.154)+.
- `$modifiedUser: User|NullPage` User that last modified the file or NullPage if not known (3.0.154)+.
- [`$uploadName: string`](method-uploadname.md) Original unsanitized filename at upload, see notes for uploadName() method (3.0.212+).
- [`install($filename): void`](method-___install.md)
- [`httpUrl(): string`](method-___httpurl.md)
- `noCacheURL($http = false): string`

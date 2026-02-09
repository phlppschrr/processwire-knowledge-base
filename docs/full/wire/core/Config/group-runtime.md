# Config: runtime

Source: `wire/core/Config.php`

- `$ajax: bool` If the current request is an ajax (asynchronous javascript) request, this is set to true.
- `$modal: bool|int` If the current request is in a modal window, this is set to a positive number. False if not.
- `$admin: bool|int` Is current request for logged-in user in admin? True, false, or 0 if not yet known. @since 3.0.142
- `$https: bool` If the current request is an HTTPS request, this is set to true.
- [`$version: string`](method-version.md) Current ProcessWire version string (i.e. "2.2.3")
- `$systemVersion: int` System version, used by SystemUpdater to determine when updates must be applied.
- `$styles: FilenameArray` Array used by ProcessWire admin to keep track of what stylesheet files its template should load. It will be blank otherwise. Feel free to use it for the same purpose in your own sites.
- `$scripts: FilenameArray` Array used by ProcessWire admin to keep track of what javascript files its template should load. It will be blank otherwise. Feel free to use it for the same purpose in your own sites.
- [`$urls: Paths`](method-urls.md) Items from $config->urls reflect the http path one would use to load a given location in the web browser. URLs retrieved from $config->urls always end with a trailing slash. This is the same as the $urls API variable.
- [`$paths: Paths`](method-paths.md) All of what can be accessed from $config->urls can also be accessed from $config->paths, with one important difference: the returned value is the full disk path on the server. There are also a few items in $config->paths that aren't in $config->urls. All entries in $config->paths always end with a trailing slash.
- `$internal: bool` This is automatically set to FALSE when PW is externally bootstrapped.
- `$cli: bool` This is automatically set to TRUE when PW is booted as a command line (non HTTP) script.
- [`$serverProtocol: string`](method-serverprotocol.md) Current server protocol, one of: HTTP/1.1, HTTP/1.0, HTTP/2, or HTTP/2.0. @since 3.0.166
- `$versionName: string` This is automatically populated with the current PW version name (i.e. 2.5.0 dev)
- `$pagerHeadTags: string|null` Populated at runtime to contain `<link rel=prev|next />` tags for document head, after pagination has been rendered by MarkupPagerNav module.

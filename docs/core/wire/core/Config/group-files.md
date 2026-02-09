# Config: files

Source: `wire/core/Config.php`

- $pagefileSecure: bool When used, files in /site/assets/files/ will be protected with the same access as the page. Routes files through a passthrough script. Note if applying to existing site it may not affect existing pages and file/image fields until they are accessed or saved.

- $pagefileSecurePathPrefix: string One or more characters prefixed to the pathname of protected file dirs. This should be some prefix that the .htaccess file knows to block requests for.

- $fileContentTypes: array Array of extensions and the associated MIME type for each (for file output). See /wire/config.php for details and defaults.

- $fileCompilerOptions: array Array of options for FileCompiler class. See /wire/config.php for details and defaults.

- $chmodDir: string Octal string permissions assigned to directories created by ProcessWire

- $chmodFile: string Octal string permissions assigned to files created by ProcessWire

- $chmodWarn: bool Set to false to suppress warnings about 0666/0777 file permissions that are potentially too loose

- $uploadTmpDir: string Optionally override PHP's upload_tmp_dir with your own. Should include a trailing slash.

- $uploadBadExtensions: string Space separated list of file extensions that are always disallowed from uploads.

- $pagefileExtendedPaths: bool Use extended file mapping?

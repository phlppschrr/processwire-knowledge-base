# Config: files

Source: `wire/core/Config.php`

@property bool $pagefileSecure When used, files in /site/assets/files/ will be protected with the same access as the page. Routes files through a passthrough script. Note if applying to existing site it may not affect existing pages and file/image fields until they are accessed or saved.

@property string $pagefileSecurePathPrefix One or more characters prefixed to the pathname of protected file dirs. This should be some prefix that the .htaccess file knows to block requests for.

@property array $fileContentTypes Array of extensions and the associated MIME type for each (for file output). See /wire/config.php for details and defaults.

@property array $fileCompilerOptions Array of options for FileCompiler class. See /wire/config.php for details and defaults.

@property string $chmodDir Octal string permissions assigned to directories created by ProcessWire

@property string $chmodFile Octal string permissions assigned to files created by ProcessWire

@property bool $chmodWarn Set to false to suppress warnings about 0666/0777 file permissions that are potentially too loose

@property string $uploadTmpDir Optionally override PHP's upload_tmp_dir with your own. Should include a trailing slash.

@property string $uploadBadExtensions Space separated list of file extensions that are always disallowed from uploads.

@property bool $pagefileExtendedPaths Use extended file mapping?

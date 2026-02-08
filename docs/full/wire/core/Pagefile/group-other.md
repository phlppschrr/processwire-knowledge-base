# Pagefile: other

Source: `wire/core/Pagefile.php`

@property-read string $url URL to the file on the server.

@property-read string $httpUrl URL to the file on the server including scheme and hostname.

@property-read string $URL Same as $url property but with browser cache busting query string appended.

@property-read string $HTTPURL Same as the cache-busting uppercase “URL” property, but includes scheme and hostname.

@property-read string $filename full disk path to the file on the server.

@property-read string $name Returns the filename without the path, same as the "basename" property.

@property-read string $hash Get a unique hash (for the page) representing this Pagefile.

@property string $basename Returns the filename without the path.

@property string $description Value of the file’s description field (string), if enabled. Note you can also set this property directly.

@property string $ext File’s extension (i.e. last 3 or so characters)

@property-read int $filesize File size (number of bytes).

@property string $filesizeStr File size as a formatted string, i.e. “123 Kb”.

@property Pagefiles $pagefiles The Pagefiles WireArray that contains this file.

@property Page $page The Page object that this file is part of.

@property Field $field The Field object that this file is part of.

@property array $filedata

@property int $created_users_id ID of user that added/uploaded the file or 0 if not known (3.0.154+).

@property int $modified_users_id ID of user that last modified the file or 0 if not known (3.0.154+).

@property User|NullPage $createdUser User that added/uploaded the file or NullPage if not known (3.0.154)+.

@property User|NullPage $modifiedUser User that last modified the file or NullPage if not known (3.0.154)+.

@property string $uploadName Original unsanitized filename at upload, see notes for uploadName() method (3.0.212+).

@method void install($filename)

@method string httpUrl()

@method string noCacheURL($http = false)

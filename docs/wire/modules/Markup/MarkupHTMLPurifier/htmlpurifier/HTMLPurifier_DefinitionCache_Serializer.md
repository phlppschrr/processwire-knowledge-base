# HTMLPurifier_DefinitionCache_Serializer

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## add()

@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
@return int|bool

## set()

@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
@return int|bool

## replace()

@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
@return int|bool

## get()

@param HTMLPurifier_Config $config
@return bool|HTMLPurifier_Config

## remove()

@param HTMLPurifier_Config $config
@return bool

## flush()

@param HTMLPurifier_Config $config
@return bool

## cleanup()

@param HTMLPurifier_Config $config
@return bool

## generateFilePath()

Generates the file path to the serial file corresponding to
the configuration and definition name
@param HTMLPurifier_Config $config
@return string
@todo Make protected

## generateDirectoryPath()

Generates the path to the directory contain this cache's serial files
@param HTMLPurifier_Config $config
@return string
@note No trailing slash
@todo Make protected

## generateBaseDirectoryPath()

Generates path to base directory that contains all definition type
serials
@param HTMLPurifier_Config $config
@return mixed|string
@todo Make protected

## _write()

Convenience wrapper function for file_put_contents
@param string $file File name to write to
@param string $data Data to write into file
@param HTMLPurifier_Config $config
@return int|bool Number of bytes written if success, or false if failure.

## _prepareDir()

Prepares the directory that this type stores the serials in
@param HTMLPurifier_Config $config
@return bool True if successful

## _testPermissions()

Tests permissions on a directory and throws out friendly
error messages and attempts to chmod it itself if possible
@param string $dir Directory path
@param int $chmod Permissions
@return bool True if directory is writable

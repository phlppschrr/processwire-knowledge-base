# Functions::wireUnzipFile()

Source: `wire/core/Functions.php`

Unzips the given ZIP file to the destination directory

This is procedural version of the `$files->unzip()` method. See that method for more details.


@param string $file ZIP file to extract

@param string $dst Directory where files should be unzipped into. Directory is created if it doesn’t exist.

@param array $options See `WireFileTools::unzip()` for options.

@return array Returns an array of filenames (excluding $dst) that were unzipped.

@throws WireException All error conditions result in WireException being thrown.

@see WireFileTools::unzip()

# FileValidatorModule

Source: `wire/core/FileValidatorModule.php`

Base class for FileValidator modules

Base class for FileValidator modules, which validate uploaded files.
To create a FileValidator module:

1. Create a class that extends this and follow the naming convention: `FileValidator[Something]`.
2. Place in file: /site/modules/FileValidator[Something].module (or in module-specific directory).
3. Copy the `getModuleInfo()` method out of this class and update as appropriate.
4. Implement an `isValidFile($filename)` method, and you are done.

Example: /site/modules/FileValidatorHTML.module
~~~~~~
class FileValidatorHTML extends FileValidatorModule {
    public static function getModuleInfo() {
      return array(
        'title' => 'Validate HTML files',
        'version' => 1,
        'validates' => array('html', 'htm'),
      );
    }
    protected function isValidFile($filename) {
        $valid = false;
        // some code to validate $filename and set $valid
        return $valid;
    }
}
~~~~~~

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## getModuleInfo()

Get module information

FileValidator modules should provide their own getModuleInfo() with the
key part being the 'validates' property (see below).

@return array

## isValidFile()

Is the given file valid? (this is the method modules should implement)

This method should return:
	- boolean TRUE if file is valid
	- boolean FALSE if file is not valid
	- integer 1 if file is valid as a result of sanitization performed by this method (if supported by module)

If the file can be made valid by sanitization, this method may also choose to do that (perhaps if configured
to do so) and return integer 1 after doing so.

If method wants to explain why the file is not valid, it should call $this->error('reason why not valid').

@param string $filename Full path and filename to the file

@return bool|int

## isValid()

Is the given file valid?

FileValidator modules should not implement this method, as it only serves as a front-end to isValid()
for logging purposes.

@param string $filename

@return bool|int Returns TRUE if valid, FALSE if not, or integer 1 if valid as a result of sanitization.

## getPage()

Get the Page associated with any isValid() calls

If not applicable, it will be a NullPage()

@return NullPage|Page

## getField()

Get the Field object associated with any isValid() calls

If not applicable, it will be null.

@return null|Field

## getPagefile()

Get the Pagefile or Pageimage object associated with any isValid() calls

If not applicable, it will be null.

@return Pagefile|null

## ___log()

Log a message for this class

Message is saved to a log file in ProcessWire's logs path to a file with
the same name as the class, converted to hyphenated lowercase.

@param string $str Text to log, or omit to just return the name of the log

@param array $options Optional extras to include:
	- url (string): URL to record the with the log entry (default=auto-detect)
	- name (string): Name of log to use (default=auto-detect)

@return WireLog|null

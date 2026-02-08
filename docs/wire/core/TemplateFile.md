# TemplateFile

Source: `wire/core/TemplateFile.php`

ProcessWire TemplateFile

A template file that will be loaded and executed as PHP and its output returned.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property bool $halt Set to true to halt during render, or use method $this->halt();

@property-read string $filename Primary file to render.

@property-read array $prependFilename Optional file name(s) used for prepend.

@property-read array $appendFilename Optional file name(s) used for append.

@property-read string $currentFilename Current file being rendered (whether primary, prepend, append).

@property-read bool $trim Whether or not leading/trailing whitespace is trimmed from output (3.0.154+).

@method string render()

@method bool fileFailed($filename, \Exception $e)

## __construct()

Construct the template file

@param string $filename Full path and filename to the PHP template file

## setFilename()

Sets the template file name, replacing whatever was set in the constructor

@param string $filename Full path and filename to the PHP template file

@return bool true on success, false if file doesn't exist

@throws WireException if file doesn't exist (unless throwExceptions is disabled)

## setPrependFilename()

Set a file to prepend to the template file at render time

@param string $filename

@return bool Returns true on success, false if file doesn't exist.

@throws WireException if file doesn't exist (unless throwExceptions is disabled)

## setAppendFilename()

Set a file to append to the template file at render time

@param string $filename

@return bool Returns true on success false if file doesn't exist.

@throws WireException if file doesn't exist (unless throwExceptions is disabled)

## setThrowExceptions()

Call this with boolean false to disable exceptions when file doesn’t exist

@param bool $throwExceptions

## setTrim()

Set whether rendered output should have leading/trailing whitespace trimmed

By default whitespace is trimmed so you would call `$templateFile->setTrim(false);` to disable.

@param bool $trim

@since 3.0.154

## setChdir()

Set the directory to temporarily change to during rendering

If not set, it changes to the directory that $filename is in.
To disable TemplateFile from changing any directories, set to false (3.0.154+).

@param string|bool $chdir

## ___render()

Render the template: execute it and return its output

@return string|array The output of the Template File

@throws WireException|\Exception Throws WireException if file not exist + any exceptions thrown by included file(s)

## fileReady()

Prepare to nclude specific file (whether prepend, main or append)

@param string $filename

@since 3.0.154

## fileFinished()

Clean up after include specific file

@since 3.0.154

## ___fileFailed()

Called when render of specific file failed with Exception


@param string $filename

@param \Exception $e

@return bool True if Exception $e should be thrown, false if it should be ignored

@since 3.0.154

## renderReady()

Prepare to render

Called right before render about to start

@since 3.0.154

## renderFinished()

Cleanup after render

@since 3.0.154

## renderFailed()

Called when overall render failed

@param \Exception $e

@return \Exception

@since 3.0.154

## setCurrentFilename()

Set the current filename being rendered

@param string $filename

@deprecated Moved to fileReady() and fileFinished()

## getArray()

Get an array of all variables accessible (locally scoped) to the PHP template file

@return array

## get()

Get a set property from the template file, typically to check if a template has access to a given variable

@param string $key

@return mixed Returns the value of the requested property, or NULL if it doesn't exist

## set()

Set a property

@param string $key

@param mixed $value

@return $this|WireData

## getRenderStack()

Get the current render stack

This contains the files currently being rendered from first to last

@return array

## clearAll()

Clear out all pending output buffers

@since 3.0.175

@return int Number of output buffers cleaned

## __toString()

The string value of a TemplateFile is its PHP template filename OR its class name if no filename is set

@return string

## halt()

This method can be called by any template file to stop further render inclusions

This is preferable to doing an exit; or die() from your template file(s), as it only halts the rendering
of output and doesn't halt the rest of ProcessWire.

Can be called from prepend/append files as well.

USAGE from template file is: return $this->halt();

@param bool|string $halt
 If given boolean, it will set the halt status.
 If given string, it will be output (3.0.239+)

@return $this

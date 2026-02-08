# SystemUpdaterChecks

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Class to check for potential issues in the system that may require updates from the admin

All check* methods in this class return true if the check was a success and there are no problem,
or they return false if the check failed and there is a potential issue to resolve.

## setShowNotices()

Set whether or not to show verbose notices

@param bool $showNotices

## setTestAll()

Set whether or not to test all checks (as if all checks failed)

@param bool $testAll

## execute()

Run all system checks and return array of results

@return array

## checkIndexFile()

Check that index.php file is the correct version

@return bool

## checkHtaccessFile()

Check that main htaccess file is the correct version

@return bool

@throws WireException

## checkOtherHtaccessFiles()

Check that other useful htaccess files are present

@return bool

## checkWelcome()

Check if this is the first call to checkWelcome and show a welcome message and add an active.php file if so

@return bool Returns false if active.php does not yet exist or true if it does

## checkInstallerFiles()

Check if unnecessary installer files are present

@return bool

## checkFilePermissions()

Check for insecure file permissions

@return bool

## checkPublishedField()

Check if there is a field named 'published' that should not be present

@return bool

## checkLocale()

Check locale setting

Warning about servers with locales that break UTF-8 strings called by basename
and other file functions, due to a long running PHP bug

@return bool

## checkDebugMode()

Check for debug mode

return bool Always returns true, as there is no way to fail this test

## checkMemoryLimit()

Check PHP memory_limit setting

@return bool Always returns true as memory_limit errors not considered fatal

@since 3.0.206

## getMemoryLimit()

Get memory limit

@param string $getInUnit Get value in 'K' [kilobytes], 'M' [megabytes], 'G' [gigabytes] (default='M')

@return int|float

@since 3.0.206

## checkSystemTimes()

Check that database time and PHP time match

@return bool

@since 3.0.241

## warning()

*****************************************************************************************

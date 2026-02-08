# WireSessionHandler

Source: `wire/core/WireSessionHandler.php`

ProcessWire Session Handler

This is an abstract class for a session handler module to extend from.
It provides the interface and some basic functions. For an example, see:
/wire/modules/Session/SessionHandlerDB/SessionHandlerDB.module

ProcessWire 3.x, Copyright 2026 by Ryan Cramer
https://processwire.com

## wired()

Initialize the save handler when $modules sets the current instance

## init()

Initailize, called when module configuration has been populated

## hookSessionInit()

Hook before Session::init

@param HookEvent $event

## attach()

Attach this as the session handler

## open()

Open the session

@param string $path Save path

@param string $name Name of session

@return bool True on success, false on failure

## close()

Close the session

@return bool True on success, false on failure

## read()

Read and return data for session indicated by $id

@param string $id Session ID

@return string|false Serialized data string, blank string if none, or false on fail

## write()

Write the given $data for the given session ID

@param string $id Session ID

@param string Serialized data to write

@return bool

## destroy()

Destroy the session indicated by the given session ID

@param string $id Session ID

@return bool True on success, false on failure

## gc()

Garbage collection: remove stale sessions

@param int $seconds Max lifetime of a session

@return bool True on success, false on failure

## sessionExists()

Does a session currently exist? (i.e. already one started)

@return bool

@since 3.0.158

## isSingular()

Tells the Modules API to only instantiate one instance of this module

## isAutoload()

Tells the Modules API to automatically load this module at boot

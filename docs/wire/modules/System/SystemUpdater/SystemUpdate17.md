# SystemUpdate17

Source: `wire/modules/System/SystemUpdater/SystemUpdate17.php`

Apply secondary layer of .htaccess protections for various site directories
as a fallback in case root .htaccess ever becomes corrupted or goes missing

## update()

Apply the update

@return bool

@throws WireException

## isApache()

Are we running under Apache?

@return bool

## isUseful()

Is this update useful for this installation?

@return bool

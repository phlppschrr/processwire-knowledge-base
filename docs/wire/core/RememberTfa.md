# RememberTfa

Source: `wire/core/Tfa.php`

Manages the “remember me” feature for Tfa class

Accessed from $tfaInstance->remember($user, $settings)->method().
This class is kept in Tfa.php because it cannot be instantiated without
a Tfa instance.

@method array getFingerprintArray($getLabels = false)

## setDays()

Set days to remember between logins

@param int $days

## setFingerprints()

Fingerprints to use for newly created "remember" items

@param array $fingerprints

## saveRemember()

Save Tfa 'remember' settings

@return bool

## enable()

Set combination of user/browser/host/page as remembered and allowed to skip TFA

@return bool

## remembered()

Is current user/browser/host/URL one that is remembered and TFA can be skipped?

@param bool $getName Return remembered cookie name rather than true? (default=false)
@return bool|string

## disable()

Disable one or more cookie/remembered client by name(s)

@param array|string $names
@return int

## disableAll()

Disable all stored "remember me" data for user

@return bool

## getCookie()

Get a "remember me" cookie value

@param string $name
@return string|null

## setCookie()

Set the "remember me" cookie

@param string $cookieName
@param string $cookieValue
@return WireInputData

## cookiePrefix()

Get cookie prefix

@return string

## cookieName()

Given name return cookie name

@param string $name
@return string

## clearCookie()

Clear cookie

@param string $name
@return bool

## serverValue()

Given a cookie value return equivalent expected server value

@param string $cookieValue
@param User|null $user
@return string

## ___getFingerprintArray()

Get fingerprint of current browser, host and URL

Note that this is not guaranted unique, so is only a secondary security measure to
ensure that remember-me record is married to an agent, scheme, and http host.

@return array

## getFingerprintString()

Get fingerprint string

@param array|null $types Fingerprints to use, or omit when creating new
@return string

## fingerprintStringMatches()

Does given fingerprint match one determined from current request?

@param string $fpstr Fingerprint to compare
@return bool

## getFingerprintTypes()

Get the types used in given fingerprint string

@param string $fpstr
@return array|bool

## debugNote()

Display debug note

@param string|array $note

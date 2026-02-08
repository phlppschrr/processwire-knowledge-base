# Tfa::isValidUserCode()

Source: `wire/core/Tfa.php`

Return true if code is valid or false if not

Modules MUST implement this method.

@param User $user

@param string|int $code

@param array $settings User configured TFA settings

@return bool|int Returns true if valid, false if not, or optionally integer 0 if code was valid but is now expired

@throws WireException

# User::hasTfa()

Source: `wire/core/User.php`

Does user have two-factor authentication (Tfa) enabled? (and what type?)

- Returns boolean false if not enabled.
- Returns string with Tfa module name (string) if enabled.
- When `$getInstance` argument is true, returns Tfa module instance rather than module name.

The benefit of using this method is that it can identify if Tfa is enabled without fully
initializing a Tfa module that would attach hooks, etc. So when you only need to know if
Tfa is enabled for a user, this method is more efficient than accessing `$user->tfa_type`.

When using `$getInstance` to return module instance, note that the module instance might not
be initialized (hooks not added, etc.). To retrieve an initialized instance, you can get it
from `$user->tfa_type` rather than calling this method.


@param bool $getInstance Get Tfa module instance when available? (default=false)

@return bool|string|Tfa

@since 3.0.162

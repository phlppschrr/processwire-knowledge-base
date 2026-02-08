# 2-factor authentication

Source: https://processwire.com/docs/security/two-factor-authentication/

## Summary

Two-factor (or multi-factor) authentication gives you an extra layer of account security relative to just using a password. ProcessWire versions 3.0.109 and newer include core support for two-factor authentication.

## Key Points

- [TfaTotp](/docs/security/two-factor-authentication/totp/) for TOTP 2-factor authentication (time-based one time protocol)
- [TfaEmail](/docs/security/two-factor-authentication/email/) for Email/SMS 2-factor authentication

## Sections


## Two-factor (or multi-factor) authentication

Two-factor (or multi-factor) authentication gives you an extra layer of account security relative to just using a password. ProcessWire versions 3.0.109 and newer include core support for two-factor authentication.

The ProcessWire core provides the API, interface and flow control for the two-factor authentication process. But the actual implementation is handled by modules that extend the `Tfa` base module class. In this section we'll cover details on two different modules for implementation of two-factor authentication. To begin using two-factor authentication, you'll want to install one of these modules:

- [TfaTotp](/docs/security/two-factor-authentication/totp/) for TOTP 2-factor authentication (time-based one time protocol)
- [TfaEmail](/docs/security/two-factor-authentication/email/) for Email/SMS 2-factor authentication


### Which two-factor authentication module should you use?

The addition of any two-factor authentication to your login process is going to be a nice security improvement. The more options you provide, the more likely your users will adopt it. So at this stage, unless you are wanting to stick with a specific standard or application, it makes sense to install multiple two-factor authentication modules.


### How it works

When you install one or more `Tfa` modules, the ProcessWire core automatically adds a new field to your user template, called `tfa_type`. This field is editable from the user profile screen, and enables the user to select what two-factor authentication type they want to use:

After making a selection, it will ask you to enter your current password for security purposes. Save your profile, and 2-factor authentication is ready to configure. In this case, I've selected the TOTP two-factor authentication:

Open an Authenticator application on your phone, tap "add account" and it'll ask you to hold your phone up to the QR code so that it can record it and save it. Once it's in the authenticator application, it starts generating new codes for it every 30 seconds. Enter the first code that it generates for you and hit Save. Now your account has two-factor authentication enabled.

If you need a backup of your secret/private-key: technically you could copy the "Secret" string and store it somewhere securely. Or I suppose you could copy/paste the QR code if you preferred. I'm not saying you should, just saying you can. Keeping copies of these things ultimately makes it more convenient if you lose access to your phone/application, though having copies also makes it less secure.

With two-factor authentication now enabled, the next time you login, you'll get the following second-step after completing your username/password login:

You'll have about 90 seconds to get it right, as it'll accept the current, previous, or next 30-second codes, to account for any time differences or delays between the server and client. If you can't get the code right in a few tries (not likely), it'll abort and make you re-authenticate with your username and password.

To begin using two-factor authentication in ProcessWire, install one of the “Tfa” modules:

- [TOTP 2-factor authentication (TfaTotp)](/docs/security/two-factor-authentication/totp/)TOTP standards for “Time-based One-Time Password”, which is an algorithm that computes a one-time password. It does this with a…
- [Email/SMS 2-factor authentication (TfaEmail)](/docs/security/two-factor-authentication/email/)This is a push-based two-factor authentication method, where it sends out an email or SMS message to you with your authentication…

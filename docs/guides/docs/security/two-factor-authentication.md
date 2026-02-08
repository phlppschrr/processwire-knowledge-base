# Two-factor (or multi-factor) authentication

Source: https://processwire.com/docs/security/two-factor-authentication/

## Summary

Two-factor (or multi-factor) authentication gives you an extra layer of account security relative to just using a password. ProcessWire versions 3.0.109 and newer include core support for two-factor authentication.

## Key Points

- Two-factor (or multi-factor) authentication gives you an extra layer of account security relative to just using a password. ProcessWire versions 3.0.109 and newer include core support for two-factor authentication.
- The ProcessWire core provides the API, interface and flow control for the two-factor authentication process. But the actual implementation is handled by modules that extend the Tfa base module class. In this section we'll cover details on two different modules for implementation of two-factor authentication. To begin using two-factor authentication, you'll want to install one of these modules:
- The addition of any two-factor authentication to your login process is going to be a nice security improvement. The more options you provide, the more likely your users will adopt it. So at this stage, unless you are wanting to stick with a specific standard or application, it makes sense to install multiple two-factor authentication modules.

## Sections


### Which two-factor authentication module should you use?

The addition of any two-factor authentication to your login process is going to be a nice security improvement. The more options you provide, the more likely your users will adopt it. So at this stage, unless you are wanting to stick with a specific standard or application, it makes sense to install multiple two-factor authentication modules.


### How it works

When you install one or more Tfa modules, the ProcessWire core automatically adds a new field to your user template, called tfa_type. This field is editable from the user profile screen, and enables the user to select what two-factor authentication type they want to use:


### TOTP 2-factor authentication (TfaTotp)


### Email/SMS 2-factor authentication (TfaEmail)

# ProcessWire 3.0.109 adds two-factor authentication

Source: https://processwire.com/blog/posts/processwire-3.0.109-adds-two-factor-authentication/

## Sections


## ProcessWire 3.0.109 adds two-factor authentication

3 August 2018 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-3.0.109-adds-two-factor-authentication/#comments)


## ProcessWire 3.0.109

In the [last blog post](/blog/posts/2-factor-authentication-coming-to-processwire/) I told you about how two-factor authentication was coming to the core and what our plans were. This week it's ready to use in ProcessWire 3.0.109, so we'll take a closer look at all the details and how to use it.


### Two-factor auth in the core with implementation in modules

The core now comes with the base for 2-factor modules in a class called [Tfa](https://github.com/processwire/processwire/blob/dev/wire/core/Tfa.php). It provides the API, interface and flow control for the two-factor authentication process. But the actual implementation is handled by modules that extend the Tfa base module class. I've built two of these modules to get things started. One or both of these may end up in the core at some point, but for the moment they are non-core modules that you can install:

- [TfaTotp](https://github.com/ryancramerdesign/TfaTotp) for TOTP 2-factor authentication
- [TfaEmail](https://github.com/ryancramerdesign/TfaEmail) for Email/SMS 2-factor authentication

Below are more details about these:


### TOTP 2-factor authentication (TfaTotp)

TOTP standards for “Time-based One-Time Password”, which is an algorithm that computes a one-time password. It does this with a shared secret key and the current time. [More about TOTP](https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm)

My experience with TOTP thus far is that it is implemented by many mobile authenticator applications, and thus widely available and in widespread use. Google Authenticator (mentioned in the previous post) just happens to be the simplest and apparently most widely used of them. But TOTP is supported by all of these authenticator applications, which you can also now use with ProcessWire too:

- Google Authenticator (Android, iOS)
- Microsoft Authenticator (Android, iOS)
- 1Password (Android, iOS, Windows, Mac)
- Authy (Android, iOS, Windows, Mac, cloud-sync)
- LastPass Authenticator (Android, iOS, Windows, Mac, Linux, cloud-sync)
- And several others

One of the nice things about TOTP is that they are all implementing the same algorithm (described in [RFC 6238](https://tools.ietf.org/html/rfc6238)), and thus all appear to be compatible with each other (though someone correct me if I'm wrong). I used the same QR code (secret) in both Google Authenticator and Authy and found I could use them interchangeably on the same site.

TOTP relies upon a long string of characters called a "secret", which is a private key that is stored server-side with the user account when enabling two-factor auth. When you use your phone and authenticator app to scan a QR code, it is sharing that secret with your phone. From that point forward, the website and phone can confirm identity with a 6-digit code that changes every 30 seconds.

What if your phone dies or gets lost? Since the private key (secret) is stored on your phone, you'd no longer have the ability to generate authentication codes. So this could be a problem, unless you've got a backup of your private key. Applications like Authy and LastPass keep that backup for you (cloud-sync). If you are using another application like Google Authenticator, you could always keep your own backup of the QR code/secret, so that you could plug it into any other phone or authentication app and continue to generate codes with it. But if you were to do that, you'd want to do so very securely, as the more copies of that secret that there are, the less secure it is.

The new [TfaTotp](https://github.com/ryancramerdesign/TfaTotp) module uses the excellent [TwoFactorAuth](https://github.com/RobThree/TwoFactorAuth) library by RobThree on GitHub.


### Email/SMS 2-factor authentication (TfaEmail)

This is a push-based two-factor authentication method, where it sends out an email or SMS message to you with your authentication code. Unlike TOTP, it doesn't rely on shared secrets/keys or algorithms, and instead verifies your identity based on your access to a particular email address or phone number. Whether that's beneficial or not depends on how secure that access is.

As I understand it, relying upon email or SMS for two-factor authentication is less secure than using a TOTP application. Though regardless of what two-factor auth method you use, it's going to be a lot more secure than relying on just a username and password alone.

In the case of our [TfaEmail](https://github.com/ryancramerdesign/TfaEmail) module, it actually just relies upon email. But because phone numbers you can send an SMS/text to generally have a corresponding email address, this enables you to use it as an SMS delivery method as well. For instance, here's how you can send an SMS/text to various different phone companies (let's say your phone number was 123-456-7890, below are the email addresses you would use):

- AT&T: 1234567890@txt.att.net
- Project Fi: 1234567890@msg.fi.google.com
- Sprint: 1234567890@messaging.sprintpcs.com
- T-Mobile: 1234567890@tmomail.net
- Verizon: 1234567890@vtext.com

Those are just examples. If you don't see your provider, just google "email to SMS [provider]" and it should be easy to find. Whether using email-to-SMS is ideal for this purpose, I don't really know—I only became familiar with the universality of email-to-SMS within the last week. But I do know that I want to make a lot of two-factor authentication methods available for ProcessWire, and that any authentication that adds two-factor on top of username/password requirements is going to be a nice security improvement over authentication that lacks it.

One benefit of this push-based approach is that if someone manages to get your username and password, you'll likely find out about it pretty quickly as you'll get an email or text about it immediately. Meanwhile, the attacker won't be able to login, unless they've already managed to break into your email (or SMS if using that).


### Which two-factor module should you use?

Like mentioned earlier, the addition of any two-factor authentication to your login process is going to be a nice security improvement. The more options you provide, the more likely your users will adopt it. So at this stage, unless you are wanting to stick with a specific standard or application, then it makes sense to install both the [TfaTotp](https://github.com/ryancramerdesign/TfaTotp) and [TfaEmail](https://github.com/ryancramerdesign/TfaEmail) modules. Though these are brand new at this stage, so maybe better to experiment with on development sites before applying to production sites.


### How it works (screenshots)

When you install one or more Tfa modules, the ProcessWire core automatically adds a new field to your user template, called tfa_type. This field is editable from the user profile screen, and enables the user to select what two-factor authentication type they want to use:

After making a selection, it will ask you to enter your current password for security purposes. Save your profile, and 2-factor authentication is ready to configure. In this case, I've selected the TOTP two-factor authentication:

Open an Authenticator application on your phone, tap "add account" and it'll ask you to hold your phone up to the QR code so that it can record it and save it. Once it's in the authenticator application, it starts generating new codes for it every 30 seconds. Enter the first code that it generates for you and hit Save. Now your account has two-factor authentication enabled.

If you need a backup of your secret/private-key: technically you could copy the "Secret" string and store it somewhere securely. Or I suppose you could copy/paste the QR code if you preferred. I'm not saying you should, just saying you can. Keeping copies of these things ultimately makes it more convenient if you lose access to your phone/application, though having copies also makes it less secure.

With two-factor authentication now enabled, the next time you login, you'll get the following second-step after completing your username/password login:

You'll have about 90 seconds to get it right, as it'll accept the current, previous, or next 30-second codes, to account for any time differences or delays between the server and client. If you can't get the code right in a few tries (not likely), it'll abort and make you re-authenticate with your username and password.

I realize not everyone is ready to adopt two-factor authentication in their ProcessWire installations just yet. And I know that there are also installations where it's really not necessary. But I think it's really important that we have it for those that do want it and those that need it. Core support also is consistent with our long standing tradition of making security a first priority in ProcessWire. It's a major security benefit for ProcessWire and our users. While I've not yet experimented much with implementing it on the front-end (like with the LoginRegister module or others), it has been designed to work as well on the front-end as the admin, so I'll be spending more time with that soon—stay tuned. Thanks for reading, have a great weekend, and check in at the [ProcessWire Weekly](http://weekly.pw) the latest ProcessWire news and updates!

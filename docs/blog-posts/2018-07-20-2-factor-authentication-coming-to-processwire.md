# 2-factor authentication coming to ProcessWire

Source: https://processwire.com/blog/posts/2-factor-authentication-coming-to-processwire/

## Sections


## 2-factor authentication coming to ProcessWire

20 July 2018 by Ryan Cramer [ 7 Comments](/blog/posts/2-factor-authentication-coming-to-processwire/#comments)

This week we're going to talk about a new feature that’s currently in development on the dev branch: 2-factor authentication.

This will likely be introduced in version 3.0.109 or 3.0.110). The development branch remains on version 3.0.108 this week, though it does have several updates relative to this time last week, mostly for resolution of GitHub issue reports.


### About 2-factor authentication

A new security feature coming soon to the ProcessWire dev branch is the addition of optional 2-factor authentication (also known as two-step verification, multi-factor authentication, 2FA, TFA, etc). Just in case you aren't already familiar with this, two-factor implies an authentication system where you login with your username and password as usual, but with a second step that protects your account, even if someone were to ever get a hold of your password. The second step consists of a unique and usually random code to verify your identity, and it is most commonly sent to you via an app on your phone or SMS.


### Why 2-factor authentication?

These days I'm using two factor authentication on just about every online account that I have, anywhere that it's available. With every online service being under pretty much constant attack, our increasing reliance upon these services, and the companies behind them seemingly not being so careful with our data, 2FA is reaching a point of becoming essential.

With ProcessWire's emphasis on security, it just seems like it should be built into the PW core too. It really adds a lot of security, it sets a good example, and it's something that is becoming increasingly important when it comes to online application security. It's not just about you and me, but even more so about our clients and the people that we work with—people that sometimes don't know or use best practices when it comes to passwords. 2-factor authentication is a great way to add even more protection and security for our clients and the sites that we develop for them.


### How we are implementing it

Two factor authentication is being built directly into our admin login module (ProcessLogin), but it will use separate modules as the actual providers for two factor authentication. This will enable us to support different types 2-factor authentication and different providers. Much in the same way that we support different types of email providers with WireMail modules. The module approach will also enable people to more easily utilize 2FA on the front-end, like with the LoginRegister module.


### Google Authenticator (to start)

The first provider module will be for [Google Authenticator](https://en.wikipedia.org/wiki/Google_Authenticator), which I've already been using, and am guessing some of you might already be using elsewhere (like Google, Amazon, Facebook, GitHub, etc). Google Authenticator is an app that you can install on your phone (Android and iPhone), and it provides random codes that can be used as a second step to authenticate your login identity. It's also free for both user and client at any scale, doesn't rely on SMS (or fees associated with text messages), and is generally very simple, and it seemed like a good default implementation to start with. Though there are a lot of other options too (some more powerful and full featured), so this is just where we'll start our implementation.


### 2-factor authentication process

In ProcessWire, 2-factor authentication has to first be enabled in the ProcessLogin module settings. Once enabled, individual users can enable 2-factor authentication for their account in the ProcessWire user profile editor.

ProcessWire asks the user to take a photo of a QR code on the screen with the Google Authenticator app. This QR code represents a user-unique secret that is shared this one time between Google Authenticator and ProcessWire, enabling Google Authenticator to generate codes that correspond to the user in ProcessWire. Once the secret (represented by a QR code) has been read, Google Authenticator gives the user a 6-digit code to type back into ProcessWire, just to make sure it works. The user hits save, and then they are done.

In the future, when the user logs in, they'll type in their username and password as usual, but the next screen asks them for a 6-digit code that appears on their phone. These codes are randomly generated every 30 seconds.


### Other 2-factor authentication methods

The WireMail-like module approach will likely result in more two-factor authentication methods becoming available, services like Authy, SMS-based and others. I also want to mention that Netcarver (from the forum) was on top of this back in 2012 when he developed the [PPP 2-factor authentication module](https://modules.processwire.com/modules/auth2-factor-ppp/) for ProcessWire. While it's a different kind of 2-factor authentication (utilizing email delivered and/or printed codes), I'm hopeful that it will be one that becomes available in the new module format as well.

The 2-factor authentication in ProcessWire is in the early stages of development, and it'll likely be another 1-2 weeks before the initial version is committed to the dev branch. There's a lot more to write about it, so look for more details in future blog posts here.


### Start using 2FA now in the ProcessWire forums

While we're on the subject, I also wanted to mention that I've enabled Google Authenticator-based 2FA in the ProcessWire forums. If you'd like to enable it for your account, do the following:

- Login to the [forums](https://processwire.com/talk/).
- Click your name in the top right (dropdown) and click on “Account Settings”.
- Click “Account Security” in the sidebar on the left.
- From here, you can setup Google Authenticator 2-factor authentication.

Next week I'm scheduled to work with another ProcessWire user on PW-based development project on a quick timeline, so there might not be a blog post next week, depending on how quickly we finish the project. I hope that you all have a great weekend, and enjoy reading the [ProcessWire Weekly](http://weekly.pw) for the latest ProcessWire news and updates.

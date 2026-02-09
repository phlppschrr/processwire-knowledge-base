# Timing attacks and how to prevent them

Source: https://processwire.com/blog/posts/timing-attacks-and-how-to-prevent-them/

## Sections


## Timing attacks and how to prevent them

20 October 2023 by Ryan Cramer [ 0 Comments](/blog/posts/timing-attacks-and-how-to-prevent-them/#comments)

This week we’ll take a look at a new (but simple) module available for ProcessWire that helps to prevent timing attacks. We’ll cover what timing attacks are, how they work, and how to prevent them.

The [LoginTimer](/modules/login-timer/) module for ProcessWire helps to prevent timing attacks by enabling normalization of login times so that a failed login is no faster than a successful login.

This prevents timing attacks from discovering any information about good vs. bad user names or passwords based on the time taken to process the login request. It does this by remembering how long successful logins take and applying that same amount of time to failed logins.

This module works with ProcessWire's admin login form, the login form from the [LoginRegisterPro](/store/login-register-pro/) Pro module, and any login form that uses ProcessWire's [$session](../api-full/wire/core/Session/index.md) login functions. The module also includes an API for using in your own login implementations.


### How timing attacks work

Timing attacks take advantage of the fact that different inputs to login forms can take differing amounts of time to process. Timing how long different input takes over repeated attempts begins to reveal patterns that an attacker may extrapolate and build from.

There are a few different time consuming parts of a login process. The longest is typically the hashing of the password before comparison with an existing stored hash. Other parts of the process may also take measurable amounts of time, such as validating username, identifying it as matching a valid user, etc. Password hashing in particular is an intentionally slow task, so it is quite easy to tell the difference between a login request that hashes a password to match, versus one that skips it.

When a failed login occurs, it can happen much faster than a successful one due to the non-presence of a user with the given name, or the password hash being skipped, or not matching. By simply measuring the time it takes with different login attempts, potential information about logins can be leaked.

This is the nature of login systems and not specifically related to ProcessWire.


### Compare the following theoretical cases:

- Login fail with bad username and bad password (15ms).
- Login fail with good username and invalid password (150ms).
- Login fail with good username and valid but incorrect password (300ms).
- Successful login (500ms).

The milliseconds (ms) times are made up here but represent the fact that some types of login fails consume more time than others, and successful logins often consume more time than failed logins.

A motivated attacker can measure the time it takes for login requests and begin to identify what may be successful user names. They may also be able to identify what the system accepts as valid for passwords based on attempting different lengths and characters (see case 2 above). Once they identify longer requests that appear to proceed with password hashing, they may gain additional information by attempting different passwords through the hashing and matching process.

The cases described above are just an introduction to timing attacks and not all aspects are necessarily applicable to ProcessWire. In the wild, timing attacks may go much further in attempting to catch leaks about password lengths or complexity and more. [More about timing attacks](https://en.wikipedia.org/wiki/Timing_attack).


### How to protect against timing attacks

One way to protect against timing attacks is to normalize the amount of time it takes for login requests. Meaning that cases like the 4 mentioned above all take the same amount of time. This effectively makes it useless to attempt a timing attack because there is no information to be gained in doing so.

If a successful login takes 500ms, then we make the unsuccessful attempts also take 500ms. This ensures that one can't measure the time a login attempt takes to gain any information about it. This is the approach this module takes.


### How common or likely are timing attacks?

In reality, timing attacks don't seem to be all that common on most websites because it's a lot of work for a little information. And the liklihood of that information ever translating to an actual usable login may still be rare. So my guess is that a target has to be a relatively high value target, though you never know. Automation and AI may take a lot of the work out of it and make such attacks more common.

I suspect this type of attack is rare on ProcessWire-powered sites, especially since login attempts are throttled, making it a lot more difficult to pound with login attempts. And ProcessWire is not a target the way something like WordPress is. Nevertheless, timing attacks are a real thing, they can and do occur. It's something to be aware of and something that I suspect may increase in the future on all platforms, especially given greater automation resources and the fact that it seems to be a lesser known attack among website owners. Depending on the nature of your site, it may be worth defending against.

I've always considered security to be at the top of my list for ProcessWire, so it's one of those things I wanted to account for. Though since it is likely rare among ProcessWire-powered sites, I don't think it belongs in the core at this time, but wanted it at least available as a module.


### One downside to consider

One downside to preventing timing attacks is that it increases the potential for denial-of-service (DOS) attacks. If a particular form is known to always take 500ms, then it becomes a potential target for DOS attacks. However, in the case of ProcessWire, this is less an issue since we throttle login requests.


### Using the LoginTimer API

Since LoginTimer automatically applies to all logins using ProcessWire’s [$session](../api-full/wire/core/Session/index.md) login functions, it's unlikely you will need to use its API. But there may be cases where you want more included in the timing of your login. This was the case with LoginRegisterPro, which translates email addresses to user names, and that aspect had to be included in the timing. (The LoginTimer already hooks the LoginRegisterPro module directly, when it is installed).

The process to apply LoginTimer starts when a login form has been submitted, and then proceeds as follows:

**Get an instance of the LoginTimer module:**

```
$loginTimer = $modules->get('LoginTimer');
```

**Start a named timer (i.e. 'my-login-timer'):**

```
$loginTimer->start('my-login-timer');
```

**Process the login form.**

**On successful login, save the timer:**

```
$loginTimer->save();
```

**On failed login, apply a delay that matches the time of a successful login:**

```
$loginTimer->apply();
```

Putting it all together in one code block (with a little pseudocode as well), it might look like this:

```
if('login form is submitted') {
  $loginTimer = $modules->get('LoginTimer');
  $loginTimer->start('my-login-form');
  // …your code to test for login success goes here…
  if('login success') {
    // remember time of successful login
    $loginTimer->save();
  } else {
    // apply delay for failed login
    $loginTimer->apply();
  }
}
```


### Get the Login Timer module

I recommend using ProcessWire 3.0.227 or newer, though it may work fine in older versions as well.

- [LoginTimer on GitHub](https://github.com/ryancramerdesign/LoginTimer)
- [LoginTimer in the ProcessWire modules directory](/modules/login-timer/)

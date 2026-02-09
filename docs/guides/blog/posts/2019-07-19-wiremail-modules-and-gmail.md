# Two new WireMail modules and using Gmail with PW

Source: https://processwire.com/blog/posts/wiremail-modules-and-gmail/

## Sections


## Two new WireMail modules plus how to use Gmail with ProcessWire

19 July 2019 by Ryan Cramer [ 0 Comments](/blog/posts/wiremail-modules-and-gmail/#comments)

A look at two new WireMail modules for sending email, plus details on how you can configure ProcessWire to use Gmail for sending email.

This week I was catching up with client work after traveling last week, but a good part of that work overlapped with a focus on WireMail modules. As a result, this week I’ve released two new WireMail modules, and also have information here on how you can configure two existing WireMail modules (WireMailSmtp and WireMailPHPMailer) to use Gmail as the SMTP sender.


## WireMail: Mail Router

This is a WireMail module that sends email through other WireMail modules based upon configurable rules.

It was built in part because I was having trouble with some mailer services (Mailgun primarily) sometimes getting temporary blocked by Yahoo.com, Hotmail.com and others, resulting in large amounts of non-delivered email. This module enables you to route such mails to other services when you want to, ensuring they can still be delivered.

The module also enables you to control delivery based upon any other values in the email or email headers, as well as designate primary and secondary WireMail modules to handle email delivery when one or another fails.

The module was built as part of the [ProMailer](/store/pro-mailer/) package but seems like it could be useful in a lot of other situations too, so has been released on its own. For this module to be useful, you should ideally have at least one other WireMail module installed so that there is more than one way to send email in your system.

[ WireMail: Mail Router](https://modules.processwire.com/modules/wire-mail-router/)


### How to install

```
$config->wireMail('module', 'WireMailRouter');
```

The module is now installed and ready for sending email. To configure the rules that determine which mailer to use for any given email, move on to the Configuration section below:


### Configuration

The WireMailRouter module configuration screen lets you specify text-matching rules for each WireMail module that you have installed. It also lets you specify rules for when to use the core WireMail (PHP mail) and when an email should automatically fail or be skipped.

For each input in the Rules section, you should specify one rule per line. The rule can either be plain text to match or it can be a regular expression for more powerful matching options.

By default all rules are matching the “to” email address of a given message. However you can also match other email properties when needed (details further below).

If rules for multiple mailers match, only the first matched mailer will be used (in the order shown on the configuration screen).


### Basic text matching rules

For most use cases, the basic text matching rules are likely to be adequate. So if this section serves your needs, then you likely don't need to get into regular expressions.

Each rule may be any text to match, anywhere in the email address. Rules are not case sensitive. The rule `@yahoo.com` matches any email address at yahoo.com and the rule `bob` would match any email address that contains the letters “bob”, anywhere.

Because basic text matching matches anywhere in the email address, if you want to match a specific domain, it is good to ensure there is a `@` in your rule. For example, `@hotmail.com` would be what you'd want to use if your rule intends to route emails addressed to hotmail.com emails because a rule of just `hotmail.com` (without the @) would also match myhotmail.com.

Some domains might have multiple possible TLDs. For instance, Yahoo email addresses come in many flavors, like yahoo.com, yahoo.co.uk, yahoo.ca, yahoo.es, and so on. So if you wanted to match all of those, you'd want to use the rule without specifying the TLD, like this: `@yahoo.` (trailing period intentional). Of course, this would also match any email address using “yahoo” as the subdomain, but such cases seem unlikely.

If you need more powerful matching capabilities, then you'd want to use the regular expression matching rules discussed below.


### Regular expression matching rules

To perform more specific matches, or to match multiple domains, TLDs or subdomains in a single rule, you might find this best achieved with a regular expression (regex).

A regex is assumed whenever the rule contains certain characters that never appear in email addresses (regex start/end delimiters are optional). Matching is done with PCRE compatible regular expressions, except that ours are NOT case sensitive unless you specify your own starting/ending delimiters. Behind the scenes, the match is performed with PHP’s preg_match function.

Below are some examples of regular-expression based matching rules:

`^bob@domain\.com$` Matches only the exact email “bob@domain.com”.

`@gmail\.com$` Matches all email addresses ending with “gmail.com”.

`@(hotmail|outlook|live)\.com$` Matches “hotmail.com”, “outlook.com” and “live.com” email addresses.

`(@|\.)(yahoo|aol)\.[.a-z]+$` Matches yahoo and aol emails with optional subdomain and any TLD/extension.


### Matching other email properties

For more advanced or specific use cases, you can match email properties other than the email “to” address. To do so, specify your matching rule in the format: `property:rule`.

For instance, you can match any email with a subject containing the word “receipt” with: `subject:receipt`. To match emails where the subject BEGINS with the word “receipt” you would want to use a regular expression for the rule part: `subject:^receipt`.

To match emails where the FROM email (rather than TO email) contains “@mydomain.com” you would use: `from:@mydomain.com`.

To match emails where the BODY contains “booking request” you would use: `body:booking request`, or for the HTML body you would use: `bodyHTML:booking request`.

Non-default properties that you can match include the following:

- toName
- from
- fromName
- replyTo
- replyToName
- subject
- body
- bodyHTML
- header

If matching the “header” property, note that it performs the match upon all of the email headers where each header string is in the format `header-name: header-value`.


## WireMail: Gmail

This WireMail module enables using the Google OAuth2 API for sending email in ProcessWire. Once installed and configured, any email sent by ProcessWire is sent by Gmail.

[ WireMail: Gmail](https://modules.processwire.com/modules/wire-mail-gmail/)


### Benefits

The benefits of using Gmail are likely not a mystery—it’s about as reliable as it gets when it comes to sending email, for starters. We’ll instead focus on the benefits of using this particular module relative to using SMTP.

The OAuth2 API is the way Google would prefer that you send email through Gmail. Gmail also supports sending via SMTP, but only if you turn on the setting in your Google account for “enable access for insecure apps”. Since doing that isn’t ideal (and Google recommends against it), this module provides a way to send email the way Google prefers that you do. Presumably this is more safe, secure and reliable as a long term solution.


### Drawbacks

Most of the Google services use the OAuth2 API, and the biggest drawback is just that it requires more setup on your part. It’s not as simple as copying/pasting a few email server settings into the field. Though it can still all be done from the browser, but just takes a few extra steps. In particular, you’ll need the ProcessWire [GoogleClientAPI](https://github.com/ryancramerdesign/GoogleClientAPI) module installed and configured before you can use this WireMailGmail module. This is Step 1 in our installation instructions below.


### Other considerations

When using Gmail for sending your website’s email, consider that it requires the Gmail account to be the “from” email address for any messages sent. You cannot use it to send emails with a “from” address that is something you are not authenticated for. Meaning, you can’t spoof addresses. Though that’s both a benefit and a drawback, depending on what your expectations are. However, you do have full control over the from “name” and “reply-to”. So the actual “from” email address may never actually be seen by the email recipients.

You probably don’t want to use a Gmail account for sending thousands of bulk messages. I don't know what Gmail's policies are regarding this, but I'm guessing they don't want you doing this. I personally think of Gmail as an excellent and reliable solution primarily for for transactional email, but maybe also for small scale newsletters (though I've not personally used it for that purpose).


### Installation

**Step 1:**

Please read all of step 1 before proceeding. You must first install and configure the [GoogleClientAPI](https://github.com/ryancramerdesign/GoogleClientAPI) module. It has its own installation instructions. In the section where it asks for “scopes”, one of them should be this:

`https://www.googleapis.com/auth/gmail.send`

Note that when sending email with this module, it will send from whatever Gmail account you authenticated it with. Gmail requires that that account be in the “from” header of any message sent with it. As a result, if you are a web developer, you probably want this to be setup with your client’s account, rather than your own. Or you may want to setup a new Google/Gmail account specifically for this purpose.

**Step 2:**

- Copy this module’s files into /site/modules/WireMailGmail/.
- In your admin, click to Modules > Refresh.
- On the “Site” tab of your Modules screen, click “Install” for WireMailGmail
- Review and optionally populate the “from” email and name fields. Save.

**Step 3:**

Test that everything is working by entering an email address in the last field on the configuration screen. It will send a test message to whatever email you enter there. If it encounters errors, they will appear as error notifications in the admin and they will be recorded in Setup > Logs > wire-mail-gmail. If you receieve the test email, then that confirms that everything is working. I also recommend testing in live scenarios on your website if/when possible.

**Step 4: (optional)**

If WireMailGmail is the only WireMail module you have installed, then you can skip this step. However, if you have multiple WireMail modules installed, and you want WireMailGmail to be the default one used by ProcessWire, then you should add the following to your /site/config.php file:

```
$config->wireMail('module', 'WireMailGmail');
```

If using Google’s API for Gmail seems more involved than you'd like, there's another option: you can use Gmail as an SMTP server, if you don't mind the potential security tradeoffs…


## Using Gmail as an SMTP server


### Enabling “less secure app access”

Google will let you use SMTP with your Gmail account if you enable “Less secure app access”. Though Google recommends that you avoid this, so if you go this route you might create a burner account for the purpose rather than using your regular Gmail account.

To enable “less secure app access” go to [myaccount.google.com/security](https://myaccount.google.com/security), scroll to the bottom and click the link to enable less secure apps (SMTP presumably being less secure than using their OAuth2 API). Once enabled it should look like this:


### WireMailPHPMailer with Gmail

I was able to get [WireMailPHPMailer](https://modules.processwire.com/modules/altivebirit/) sending through Gmail with these settings below (all other settings left at defaults).


### WireMailSmtp with Gmail

For [WireMailSmtp](https://modules.processwire.com/modules/wire-mail-smtp/), I couldn’t get TLS working, but I was able to get it working with SSL using these settings below. Of course in both instances, you should replace the you@gmail.com with your Gmail account and populate the password as appropriate.

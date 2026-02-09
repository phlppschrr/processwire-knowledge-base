# Introducing IftRunner and the story behind it

Source: https://processwire.com/blog/posts/introducing-iftrunner-and-the-story-behind-it/

## Sections


## Introducing IftRunner and the story behind it

18 September 2015 by Ryan Cramer [ 22 Comments](/blog/posts/introducing-iftrunner-and-the-story-behind-it/#comments)

This week is a different week here on the ProcessWire blog. Ryan is on holidays and he asked me to write this blog post. It's a great honor and I wanted to use this as an opportunity to tell you a little bit of our company's background with ProcessWire. There is also a surprise module release for you all.

Before we start, let me quickly introduce myself. My name is Antti Peisa, also known as apeisa at the [forums](/talk/) and [twitter](https://twitter.com/apeisa). I work as a production manager at [Avoine](https://www.avoine.fi/), which is a web company from Finland.


### Collaboration between Avoine and ProcessWire

If you follow ProcessWire development (as most of you who read this blog do), you might remember seeing Avoine mentioned every now and then. We started using ProcessWire to build websites for our customers around 2012 and back then one of the first obstacles was the lack of multi-language support. Most of the Finns do understand English, but many still prefer to use the software in our own language. So the lack of multi-language support was definitely a big issue for us. After a few emails with Ryan, I felt very confident in future of ProcessWire. It was also clear that multi-language support was coming, but we needed it as fast as possible. We decided to boost the development with a sponsorship deal. That turned out great: soon we had the ability to translate the PW admin interface, but also a good foundation to manage content in multiple languages. Every year all aspects of ProcessWire have improved and so has multi-language support. Today ProcessWire has the [strongest multi-language support](/api/multi-language-support/) I know (at least on the php cms/f space).

Multi-language support was just the beginning of a collaboration between Avoine and Ryan. After that we needed [inputfield dependencies](/api/selectors/inputfield-dependencies/) in one of our projects. This was second project where Avoine gave some money and ideas so that Ryan could build fantastic features. I think inputfield dependencies are a brilliant feature that is rarely seen and in ProcessWire it is done very well. Today the ProcessWire admin itself uses inputfield dependencies here and there and they really boost the usability.

Last year Avoine started a huge software development project to create our next generation member management platform (pretty close to CRM software) called *Avoine Sense*. Earlier collaboration with Ryan was a great foundation and gave us confidence boost to start building Sense on top of ProcessWire. During product development, we ended up sponsoring quite a many features that ended up either in PW-core or as separate modules. Here is a list of features that we have sponsored and have all ended as part of ProcessWire core:

- [PageTable](/blog/posts/processwire-2.5-changelog/#featured-additions)
- [Notification system](/blog/posts/processwire-2.5.3-master-2.5.4-dev/)
- [Selector fieldtype and inputfield](/blog/posts/processwire-2.5-changelog/#fields)
- [Selector string to support API-variables (user, session, page)](/blog/posts/processwire-2.5-changelog/#selectors-and-finding-pages)
- [Advanced selectors: subselectors and or-groups](/blog/posts/processwire-2.5-changelog/#selectors-and-finding-pages)
- [Possibility to allow other templates than user to login](/blog/posts/processwire-core-updates-2.5.14/#multiple-templates-or-parents-for-users)


### Building complex web application with ProcessWire

Sense is quite a large application, if we compare it to projects that are usually built on top of ProcessWire. We are not ready yet (first client projects will start in month or two), but here are the current stats:

- 1750 commits from 8 developers (currently 4 working on)
- 1½ years in development

We decided to build Sense on top of ProcessWire for two main reasons:

- most of our new software had already been built using ProcessWire (and all our developers loved it)
- featurewise PW included much more we could use compared to more traditional frameworks (like Zend, Laravel or Yii)

Of course many features of ProcessWire are website specific and were not required (like page urls for example) and some features worked in way that didn't help us at all (like user access). That was a small price compared to what we got out of the box. I am not saying that there hasn't been any moments when we would have wished PW to behave more like traditional web application framework and less like a content management framework - but I think much less than we originally feared. In our application we use PW admin as a backend for our staff (customer service, project managers, programmers - all use PW admin to manage our client's application), while our customers have 100% unique admin UI for their usage. For the UI we hired Ville Saarivaara (aka Fokke from forums) to help us build something totally unique in boring sea of registry applications:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1094/sense.png)

What might be interesting for most of you considering ProcessWire for bigger projects or as a platform for SaaS application are the technical decisions we made with Avoine Sense:

- it is 100% cloud based and load balanced, running on top of AWS (Elastic Beanstalk, S3, SQS, ELB)
- all persistent data is stored in S3
- sessions and other cached data are stored in ElastiCache
- ProcessWire databases are running as RDS-instances
- API and workers (which process time consuming tasks) are running as separate applications
- we built REST-API with OAuth2 authentication that allows read/write access into our PW instances
- all instances are handled through the same PW application, instance specific configuration is loaded from DynamoDB in realtime

We are living very exciting times at Avoine since we can finally start showing our customers what we have been building. It is also rewarding to start sharing many of the technical aspects of our project with the ProcessWire community. Please do ask us here in the comments if you are interested hearing more about these themes.


### IftRunner release

During Sense development Ryan built us two big modules that we have open sourced together. First one was [Dynamic Roles, which we released over year ago](/talk/topic/6822-module-dynamic-roles-for-pw-246/). Dynamic Roles allows a very flexible way to define user groups and their view/edit access (both based on selectors). While we finally ended up not using Dynamic Roles in our project, I feel it is great module and definitely something you should consider if PW's default access management doesn't suit your needs.

The second module is the surprise I mentioned in the first paragraph. This beauty has a bizarre name, called [IftRunner](https://github.com/ryancramerdesign/IftRunner), which could be translated: "If this happens, then do that". It is basically a visual GUI for defining hooks and launching actions based on those hooks.

What this really means is that you can define triggers like:

- "each time page with news-item template is created"

then do these actions:

- "send this email to allcompany@example.com"
- "tell my newsletter application that it can send update to list x"

The most common use case for us is quite simple: we use IftRunner to update title fields based on other fields. For example, when pages with "member"-template are saved, we make sure that title stays as "<firstname> <lastname>". What is really cool in our case is that some of our customers want more information into their titles than others. Usually this would require a custom changes in code or client specific module - now we can just make the changes through the IftRunner's admin interface.

IftRunner is not a tool that all websites need. In fact very rare websites actually do make a good use of it (this is the reason it is separate module and not a core feature). But if you are building something more complex (like some sort of web application) or you are afraid of module development (don't be, it's easy!), then IftRunner might be an enormous help to you. The real power comes from the fact that you can build more actions yourself that IftRunner is able to launch.

There isn't readme or proper instructions yet, but most adventurous of you might enjoy diving into IftRunner (you can [find it on GitHub](https://github.com/ryancramerdesign/IftRunner)). Together with Lister Pro, you can achieve quite a complex logic and processes just by using ProcessWire admin, without any coding. The problem is that there are quite few actions currently, so if you don't build the ones you need, there isn't too many options yet. Here are few screenshots though to get sneak peak without installing it.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1094/ift1.png)

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1094/ift2.png)

Thanks for reading! Please ask any guestions you might have below, I will follow comments section actively for the next week.

-Antti

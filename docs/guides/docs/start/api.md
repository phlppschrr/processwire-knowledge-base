# Unknown

Source: https://processwire.com/docs/start/api/

What the API is, why we think you'll like it, and how it makes ProcessWire a unique platform in the CMS landscape.

- [Introduction to the API](#introduction-to-the-api)
  - [What is an API in a CMS?](#what-is-an-api-in-a-cms)
  - [Why is the API so important?](#why-is-the-api-so-important)
  - [What’s unique about ProcessWire’s API?](#whats-unique-about-processwires-api)

- [What makes up the API?](#what-makes-up-the-api)
  - [API Variables](#api-variables)
  - [Selectors](#selectors)
  - [Fluent Interfaces](#fluent-interfaces)
  - [Module Plugin Architecture](#module-plugin-architecture)

- [How is the API similar to jQuery?](#how-is-the-api-similar-to-jquery)
  - [DOM / Site Map](#dom-site-map)
  - [Methods](#methods)
  - [Chaining](#chaining)
  - [Traversing](#traversing)

---

[#](#)

## Introduction to the API

[#](#)

### What is an API in a CMS?

API means application programming interface. In our context, it most commonly refers to the clearly defined interface (or tools) that the web developer uses to interact with content managed by the CMS. This interaction is most commonly used to produce output (like markup for the front-end of a site). In our case, the interactions can also be to manipulate content, create new content, and so on.

ProcessWire is entirely built around the API, and its admin panel is actually a website built using this API. ProcessWire was a headless CMS before there was a term for it. ProcessWire's easy-to-use API can do everything that you can do interactively in the admin, and more.

[#](#)

### Why is the API so important?

When it comes to a CMS, the API is the primary interface and set of tools that the web developer uses is developing a CMS-driven website/application. The web developer most commonly works within the context of output, like HTML, CSS and perhaps Javascript. But when it comes to retrieving or manipulating the actual content, it's between the CMS API and the developer.

 The quality, consistency and simplicity of using that API, and how well it works in the context of the front-end output, either makes or breaks the development experience.

This is where ProcessWire's API comes into play. It focuses on making the development experience a joy while being simple, productive and powerful. It's about working the way you do, getting more done with less time, and having fun in the process.

[#](#)

### What’s unique about ProcessWire’s API?

The ProcessWire API may already be comfortable and familiar for you, even if you've never used it before. To explain why it's both unique and familiar, lets first look at where it came from.

When it was originally released, the [jQuery](https://jquery.com/) javascript library was a paradigm shift. It took what was kind of a tricky and technical (Javascript) and turned it into something that was a joy to use. jQuery could be picked up quickly, and using it made my job fun. Its syntax was so simple, fast and powerful, that it was pure enjoyment for me, a web developer.

Prior to jQuery, I knew some Javascript but couldn't do very much with it (PHP was really my focus). jQuery came along and changed all that. To my clients, it made me look like a pro on the front-end. It enabled me to build things I never could have before, and have fun doing it. I could produce a whole lot of results without a lot of time. While it's now more than a decade ago, jQuery changed my world as a web developer.

It wasn't long after discovering and learning jQuery that I started longing for a similar experience in a CMS. There were a lot of open source CMSs out there, and I tried them all, but nothing approached the powerful and simple joy of jQuery when it came to web development. I had already been developing custom CMS platforms for many years, and I thought it was time to pursue this project.

After more than a year of planning and development, the first open source version of ProcessWire was born.** **First came the design and planning of the API, then the CMS was built around it. Like jQuery, it's fun, fast, powerful, and a joy to use. It has also proven to be a secure platform for websites and applications, and every bit as sought after of a tool for clients as it is for developers. It's pure enjoyment in a CMS.

Now more than eight years since the original open souce release of ProcessWire, this original concept is still our foundation and guide.

---

[#](#)

## What makes up the API?

ProcessWire’s API consists of a few different components:

[#](#)

### API Variables

The API consists of a few variables (via PHP objects) which are provided to your site's template files. These variables enable you to get or modify anything from your content, much in the same way that jQuery enables you to get and modify anything from the DOM.

The two most common API variables are [$page](/api/variables/page/) and [$pages](/docs/start/variables/pages/). For some sites, this is all that you will ever use. The $page API variables represents the current page being viewed, and $pages represents all the other pages in your site. These can be thought of like the `$()` object in jQuery.

ProcessWire's API variables provide access to all the components in ProcessWire, including all the site's pages, users, templates and fields. They provide a means of finding, getting, creating, modifying, saving and deleting these types of data.

You don't even need to build a site or application in ProcessWire in order to use the API. That's because the API can also be accessed by [bootstrapping ProcessWire](/docs/front-end/include/) from another PHP script. [More about API variables](/docs/start/variables/)

[#](#)[#](#)

### Selectors

Another major component of ProcessWire's API are selectors. Like in jQuery, selectors are simple strings of text that specify fields and values. For example, "name=ryan" is a simple selector that says: "find items that have the name ryan." These selectors are used throughout ProcessWire to get and find pages (and other types of data). ProcessWire selectors resemble jQuery selectors in many instances, but are also quite different. [More about ProcessWire selectors](/docs/selectors/)

[#](#)

### Fluent Interfaces

Most of the API objects in ProcessWire are chainable, using a fluent interface. This enables you to accomplish multiple operations on one line, for example:

```
echo $pages->get("/products/2010/")
  ->find("template=faq, body*=Tobiko")
  ->first()
  ->url;
```

Might print something like this:

```

/products/2010/sushi-knives/faq/
```

Of course, you don't have to chain statements like that unless you want to.

[#](#)

### Module Plugin Architecture

ProcessWire is built around a modular architecture. Modules exist to enable a high level of extensibility and customization to an installation of ProcessWire. Nearly every component and action in ProcessWire is hookable. Much of ProcessWire itself is a collection of plugin modules. [More about Modules](/docs/modules/)

---

[#](#)

## How is the API similar to jQuery?

ProcessWire's API is inspired by jQuery and its style and syntax. You'll find a lot of similarities, and you'll also find some differences. The goal behind the ProcessWire API is to provide the level of accessibility and control to your site's pages that jQuery provides to the DOM.

There are fundamental differences in the way that PHP and Javascript work, not to mention even greater fundamental differences between an SQL database and the DOM. ProcessWire's API is inspired by jQuery, but it's on a completely different platform and there are as many differences as similarities. Nevertheless, my hope is that if you use jQuery, you'll find ProcessWire's API familiar and surprisingly easy to work with relative to other platforms. Even if you haven't worked with jQuery, the API is designed to be easy and approachable. Its scope is similar than that of jQuery from an API standpoint, though perhaps even easier to learn. Below are a few similarities you'll find between ProcessWire's API and jQuery.

[#](#)

### DOM / Site Map

You interact with your site's structure via ProcessWire's API in a manner similar to working with the DOM in jQuery. The hierarchy of your site can be thought of like a DOM hierarchy, where every node (page) has a parent and every node may have children, and so on. Likewise, every node (page) can have its own attributes (fields). Depending on the type of node (template) the attributes (fields) will be different.

[#](#)

### Methods

For the most part, ProcessWire's API attempts to use the same method naming conventions as jQuery. For example, you may use the find(), children(), siblings(), parent() and parents() methods on any page (aka node) and optionally supply a selector.

[#](#)[#](#)

### Selectors

ProcessWire takes the idea of attribute selectors from jQuery and lets you apply that methodology to getting and finding pages in your site based on values in their attributes (aka fields). These selectors are a simplified version of what you find in jQuery, but the intention, experience and results are the same. For the most part, the operators used in a selector are the same as the operators used in jQuery selectors. [More about Selectors](/docs/selectors/)

[#](#)

### Chaining

Like in jQuery, you can chain method calls in ProcessWire if you want to. This is what's called a fluent interface. Sometimes this is convenient and sometimes not, but the option is always there. For example, the following bit of code of grabs the first file from a field named *images* on the current `$page`, resizes it to 200px width, and outputs the URL in an `<img>` tag:

```
<img src='<?=$page->images->first->width(200)->url?>' alt='Example'>
```

[#](#)

### Traversing

Like in jQuery, most traversing methods return values that can themselves be traversed and compared. For instance, a call to `$page->find(...)` or `$page->children(...)` returns an array type that also has its own methods for find(), filter(), first(), has(), add(), filter() and so on.

- [Getting started](/docs/start/)
- [Installation](/docs/start/install/)
- [Structure](/docs/start/structure/)
- [About the API](/docs/start/api/)
- [Template files](/docs/start/templates/)
- [API variables](/docs/start/variables/)
- [API access](/docs/start/api-access/)
- [Output strategies](/docs/front-end/output/)

- See also
- [API Reference](/api/ref/)
- [API variables](/docs/start/variables/)
- [Selectors](/docs/selectors/)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)

[Structure](/docs/start/structure/)[Template files](/docs/start/templates/)

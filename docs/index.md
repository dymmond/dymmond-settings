# Dymmond Lazy Settings

<p align="center">
    <em>🚀 Generic settings system applied to any application. 🚀</em>
</p>

<p align="center">
<a href="https://github.com/dymmond/dymmond-settings/actions/workflows/test-suite.yml/badge.svg?event=push&branch=main" target="_blank">
    <img src="https://github.com/dymmond/dymmond-settings/actions/workflows/test-suite.yml/badge.svg?event=push&branch=main" alt="Test Suite">
</a>

<a href="https://pypi.org/project/dymmond-settings" target="_blank">
    <img src="https://img.shields.io/pypi/v/dymmond-settings?color=%2334D058&label=pypi%20package" alt="Package version">
</a>

<a href="https://pypi.org/project/dymmond-settings" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/dymmond-settings.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: [https://settings.dymmond.com](https://settings.dymmond.com) 📚

**Source Code**: [https://github.com/dymmond/dymmond-settings](https://github.com/dymmond/dymmond-settings)

**The official supported version is always the latest released**.

---

## Motivation

**Not overcomplicating what it should be easy by default.**

In the current technological environment almost for certain, every system needs some sort of settings.
These settings are often inside a `settings.py` file or similar and then internally is called everywhere
needed.

The problem encountered is the fact that those are not considered `lazy`.

What does that mean? Means that you often face issues when trying to get your application up and running
and those settings need be loaded beforehand but not evaluated until the time "comes".

The `dymmond-settings` was created with the purpose of addressing those same `lazy` settings problems.

The current Dymmond ecosystem uses a similar system an it was where this package came from.

No hard dependencies, just pure Python using `dataclasses`. Yes, you read properly, the settings
system is built on top of the default Python dataclasses, which means, you can take full advantage
of the built-in in your favour.

Of course some defaults are provided and some extra functionality on top to make sure you can use
it without too much hassle.

## Installation

To install, you can simply run.

```shell
$ pip install dymmond-settings
```

## How to use it

This is the best part. Inspired by the way the Dymmond ecosystem
([Esmerald][esmerald], [Edgy][edgy], [Saffier][saffier], [Mongoz][mongoz]) operates, these settings
aim to mimic exactly the same behaviour.

You can simply import the global `Settings` object and extend and then call the `settings` lazy
object anywhere in your code without the risk of blowing up beforehand.

## Defaults

The settings system provides some defaults for you that usually are common in every application
but **you are not entitled to use them**.

These defaults can be overridden at any given time, of course.

### Attributes

* **debug** - Boolean flag generally used to indicate if the application should be in debug mode
or not. This is particularly useful if you want to separate some settings by environment.

    <sup>Default: `False`</sup>

* **environment** - String value indicating the the environment of the `settings`. This can be
particularly useful if you want to show specific settings by the given environment. You can use
the provided values from `dymmond_settings.enums.EnvironmentType` or create your own.

    <sup>Default: `production`</sup>

* **version** - A value indicating a possible the `version` of your application running the settings.
It defaults to the current version of `dymmond_settings` if nothing is provided.

    <sup>Default: `dymmond_settings.__version__`</sup>

### Functions

Although Python `dataclasses` also provides that same functionality for you, `dymmond_settings`
makes it easier for you to use it.

All `dymmond_settings` objects can be used with any of the normal `dataclasses` functionalities
and applications.

#### dict()

This simply converts your settings module into a python dictionary. This provides the same level
of functionality of `asdict` from the Python `dataclasses` module when `exclude_none` is set
to `False` (default).

**Parameters**:

- **exclude_none** - Excludes the values containing `None`.
- **upper** - Boolean flag indicating if the keys should be in upper case.

```python
from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class AppSettings(Settings):
    ...


my_settings = AppSettings()
my_settings.dict()
```

Or if you want to exclude the `None` values.

```python
from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class AppSettings(Settings):
    ...


my_settings = AppSettings()
my_settings.dict(exclude_none=True)
```

Or if you want the keys to be upper case.

```python
from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class AppSettings(Settings):
    ...


my_settings = AppSettings()
my_settings.dict(upper=True)
```

#### tuple()

This simply converts your settings module into a python tuple but is slightly different from the
`astuple` from Python `dataclasses` module.

The default from `dataclasses` provides a tuple with all the values of the object provided `astuple`
whereas `dymmond_settings` tuple function provides **a list of tuples key/pair valued**.

As per [dict](#dict) functionality, the `tuple()` also provides a `exclude_none` in case you want
a list attributes with the values set.

**Parameters**:

- **exclude_none** - Excludes the values containing `None`.
- **upper** - Boolean flag indicating if the keys should be in upper case.

```python
from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class AppSettings(Settings):
    ...


my_settings = AppSettings()
my_settings.tuple()
```

Or if you want to exclude the `None` values.

```python
from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class AppSettings(Settings):
    ...


my_settings = AppSettings()
my_settings.tuple(exclude_none=True)
```

Or if you want the tuple to contain the *keys* in upper case.

```python
from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class AppSettings(Settings):
    ...


my_settings = AppSettings()
my_settings.tuple(upper=True)
```

## How to use it

There are many ways you can use the settings and all of them valid. Here we show just a few examples
how to use it.

### The auto detection

When using the settings system, you kinda need to be able to tell your application where to look up
for the settings when loading, right?

Well yes and no, if you don't want to rely of the auto-load
of the settings for you and you want to take charge of if, you can simply skip this but if you don't,
well, this is the way.

As mentioned before, to make sure you use the automatic detection of the settings in your application
**you need to set an environment variable**, called `SETTINGS_MODULE`.

When the `SETTINGS_MODULE` is set and pointing to your settings, this will make the `settings`
object from `dymmond_settings` aware of it and make it available globally and in lazy mode.

Confusing? Well, let us see an example.

Let us imagine we have a `settings.py` file somewhere in the code, example: `myapp/config/settings.py`.

Let us also create our custom application settings and provide some values, like this:

```python
from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class AppSettings(Settings):
    debug: bool = False
    my_setting: str = field(default="works")
```

Simple so far, right? Ok, no we need to make sure our system is aware of these new settings and for
that we will set the `SETTINGS_MODULE` to point it out to our custom settings. Like this:

```shell
$ SETTINGS_MODULE='myapp.config.settings.AppSettings' python ...
```

And that is it, really! Although looking very simple, there is a lot of magic happening behind the scenes
that you don't need to worry about.

Now, because we made the application aware, we are also able to use the `settings` object provided
by the `dymmond_settings` anywhere in your code base by simply importing it.

Like this:

```python
from dymmond_settings import settings


def get_my_settings() -> str:
    return settings.my_setting
```

This simple `settings` is very powerful and `lazy`, which makes it perfect if you want to use it
anywhere in your codebase without those annoying imports happening all over the place.

[esmerald]: https://esmerald.dev
[edgy]: https://edgy.tarsild.io
[saffier]: https://saffier.tarsild.io
[mongoz]: https://mongoz.tarsild.io

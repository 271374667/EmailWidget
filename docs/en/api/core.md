# Core Modules

The core modules provide the foundational architecture for EmailWidget, including the Widget base class, template engine, cache system, and other core components.

## BaseWidget

::: email_widget.core.base.BaseWidget
    options:
        show_root_heading: true
        show_source: false
        heading_level: 3
        filters:
          - "!^_"
          - "!^.*args$"
          - "!^.*kwargs$"

## TemplateEngine

::: email_widget.core.template_engine.TemplateEngine
    options:
        show_root_heading: true
        show_source: false
        heading_level: 3
        filters:
          - "!^_"
          - "!^.*args$"
          - "!^.*kwargs$"

## ImageCache

::: email_widget.core.cache.ImageCache
    options:
        show_root_heading: true
        show_source: false
        heading_level: 3
        filters:
          - "!^_"
          - "!^.*args$"
          - "!^.*kwargs$"

## Logger

::: email_widget.core.logger.EmailWidgetLogger
    options:
        show_root_heading: true
        show_source: false
        heading_level: 3
        filters:
          - "!^_"
          - "!^.*args$"
          - "!^.*kwargs$"
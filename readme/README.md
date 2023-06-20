# Crisp Minimal Résumé

<p align="center">
  <img src="screenshots/resume-desktop.png" width="578" />
  <img src="screenshots/resume-mobile.png" width="220" />
</p>

<p align="center">
  <img src="https://github.com/crispgm/resume/workflows/build/badge.svg" alt="GitHub CI" />
  <a href="https://badge.fury.io/rb/jekyll-theme-minimal-resume">
    <img src="https://badge.fury.io/rb/jekyll-theme-minimal-resume.svg" alt="Gem Version" />
  </a>
  <a href="https://badge.fury.io/js/hexo-theme-crisp-minimal-resume">
    <img src="https://badge.fury.io/js/hexo-theme-crisp-minimal-resume.svg" alt="npm version" />
  </a>
</p>

## Introduction

[English](/README.md) [简体中文](/README_zh-CN.md)

This is a responsive minimal résumé template made by Crisp, powered by [Jekyll](http://jekyllrb.com/). And we also provide an official [Hexo port](/port-hexo/README.md) for Hexo users.

You may config all the data in `yaml` and make it your own résumé. Then, you might use on GitHub Pages, your website, or wherever you want.

[DEMO](https://crispgm.github.io/resume/resume.html)

## Features

- Simple, elegant, and minimal design
- PC and mobile friendly, but it looks better on PC
- PDF supports and print friendly
- Flexible and extensible

## Usage

### Local Mode

1. Clone the repo

   ```shell
   git clone https://github.com/crispgm/resume.git
   ```

2. Install Jekyll

   ```shell
   gem install jekyll
   ```

3. Config your résumé data

   The `baseurl` is required in `_config.yml` if you serve this page as part of your website. And your contact information, **EDUCATION**, **SKILLS**, **EXPERIENCE**, and **PROJECTS** data will be set in `_data/resume.yml`.

4. Run and Debug

   ```shell
   jekyll serve
   ```

5. Build

   ```shell
   jekyll build
   ```

### Gem-based Theme

1. Create a `Gemfile`

   ```shell
   source "https://rubygems.org"

   gem "jekyll-theme-minimal-resume"
   ```

   And then,

   ```shell
   bundle install
   ```

2. Init `_config.yml`

   ```yaml
   title: Résumé Title
   baseurl: "/resume/"
   theme: "jekyll-theme-minimal-resume"
   ```

3. Create a `index.html`

   ```yaml
   ---
   layout: resume
   ---

   ```

4. Create `_data/resume.yml` and fill in your resume data. [Example data is available here](/_data/resume.ytml).

## Data Format

### Contact

```yaml
contact:
  - icon: fa-envelope
    text: youremail@example.com
  - icon: fa-phone-square
    text: your-phone-num
  - icon: fa-globe
    text: your-website.com
    link: https://crispgm.github.io/resume/resume.html
```

FontAwesome iconfont is embedded, so use the `fa-` class name as icon. `link` is optional, present if you want a link for your web version.

## Colors

There are a set of colorscheme. `color` may be specified in `_config.yml`. The default colorscheme is gray.

```yaml
color: gray
```

Colors powered by [Open-Color](https://yeun.github.io/open-color/):

- red
- pink
- grape
- violet
- indigo
- blue
- cyan
- teal
- green
- lime
- yellow
- orange

Colors powered by [Nord](https://www.nordtheme.com/):

- nord

<img src="screenshots/resume-with-color.png" width="578" />

## Extending Sections

1. Add new section in `_data/resume.yml`

   ```yaml
   languages:
     - name: English
       proficiency: Professional working proficiency
     - name: Mandarin Chinese
       proficiency: Native or bilingual proficiency
   ```

2. Add section to `_layouts/resume.html`:

   ```html
   <section id="languages">
     <div class="section-title">Language</div>
     <div class="section-content">
       {% for lang in site.data.resume.languages %}
       <div class="block">
         <div class="block-title">{{ lang.name }}</div>
         <div class="block-content">{{ lang.proficiency }}</div>
       </div>
       {% endfor %}
     </div>
   </section>
   ```
## Maintaining publication list

All you have to do is to maintain the `.bib` files under `_data/bibtex` directory.

Remember that to use the following format for `author` field of each bib entry.

```
first_name, last_name and first_name2, last_name2 and ...
```

`_includes/foot.html` contains the Javascript that highlights your name in the publication list.

## Modifying the page layout

Go to `_layouts/resume.html` and look for the Liquid macros. 

## Publish this on Github pages

Make sure to use Github actions for publishing Github pages. 

`.github/workflows/jekyll.yml` is the file that specifies the steps running when publishing the site.

`script/cibuild` is the script that will be run by the steps defined in `.github/workflows/jekyll.yml`. It will also run the 
`script/publication_generator.py` which can generate the `_data/publications.yml` for you during `Jekyll` build process.

## Showcases

Feel free to add yours here.

- [David Zhang](https://crispgm.com/resume/)
- [Wei Zhang](https://zhangwei217245.github.io/OnlineCV)

## Donation

- [Buy Me A Coffee](https://www.buymeacoffee.com/crispgm)

## License

[![license](https://img.shields.io/github/license/crispgm/resume.svg)](/LICENSE)

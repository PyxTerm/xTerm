<img src="https://raw.githubusercontent.com/PyxTerm/xTerm/main/.github/workflows/Typographic.png" title="xterm Python Package" alt="python Package xTerm" width="auto" height="auto"> 

# xTerm
## Install

Windows Install with `pip`

```bash
pip install xTerm
```

Linux Install with `pip3`

```bash
pip3 install xTerm
```

Upgrade xterm Python Package : `pip install --upgrade xTerm` or `pip3 install --upgrade xTerm`

```python
from xTerm import Maths
# class shortcut
maths = Maths(font_type="Sans_Serif")
# or
maths = Maths(font_type="Sans_Serif_bold")
# or
maths = Maths(font_type="Sans_Serif_italic")
# or
maths = Maths(font_type="Sans_Serif_bold_italic")
# or
maths = Maths(font_type="Mathematical_bold")
# or
maths = Maths(font_type="Mathematical_italic")
# or
maths = Maths(font_type="Mathematical_Fraktur")
# or
maths = Maths(font_type="Mathematical_bold_Fraktur")
# or
maths = Maths(font_type="Mathematical_double_struck")
# or
maths = Maths(font_type="Mathematical_monospace")
# converet string model to any unicode font ,
converted_text = maths.Convert("Hello World")
print(converted_text)
```

---
## Alpha Mode (Convert Font String)

Convert String Text To Unicode Font Display

```python
from xTerm import Alpha
# shortcut class
alpha = Alpha.Maths(font_type="Sans_Serif_bold_italic")
# text string for convert
converted_text = alpha.Convert("Hello World")
# Print Output
print(converted_text)
# Hello World
```

## Table Mode (Create Table Data on Terminal)

Draw Table Data On Any Terminal

```python
from xTerm import Table
table = Table([["User01", "34"], ["User02", "56"]], ["User", "ID"], "simple_grid")
print(table)
```
Output:

```
┌────────┬──────┐
│ User   │   ID │
├────────┼──────┤
│ User01 │   34 │
├────────┼──────┤
│ User02 │   56 │
└────────┴──────┘
```

---

```python
from xTerm import Table
# Create Table Data List
table = Table([
    ["File 01", 233345],
    ["File 02", 545660],
    ["File 03", 100057],
    ["File 04", 438103]],
    ["File Name", "Download"]
    , "simple_grid")
# Output:
# ┌─────────────┬────────────┐
# │ File Name   │   Download │
# ├─────────────┼────────────┤
# │ File 01     │     233345 │
# ├─────────────┼────────────┤
# │ File 02     │     545660 │
# ├─────────────┼────────────┤
# │ File 03     │     100057 │
# ├─────────────┼────────────┤
# │ File 04     │     438103 │
# └─────────────┴────────────┘
```

---

## Table Funcation


- `table_data`: Any,
- `headers`: tuple = (),
- `tablefmt`: str = "simple",
- `floatfmt`: str = _DEFAULT_FLOATFMT,
- `intfmt`: str = _DEFAULT_INTFMT,
- `numalign`: str = _DEFAULT_ALIGN,
- `stralign`: str = _DEFAULT_ALIGN,
- `missingval`: str = _DEFAULT_MISSINGVAL,
- `showindex`: str = "default",
- `disable_numparse`: bool = False,
- `colglobalalign`: Any = None,
- `colalign`: Any = None,
- `maxcolwidths`: Any = None,
- `headersglobalalign`: Any = None,
- `headersalign`: Any = None,
- `rowalign`: Any = None,
- `maxheadercolwidths`: Any = None) -> JupyterHTMLStr | LiteralString | str

---

### Table formatting

There is more than one way to format a table in plain text. The third optional argument named tablefmt defines how the
table is formatted.

Supported table formats are:

| Parameter    |   Type   | Value             | Parameter    |   Type   | Value             |
|:-------------|:--------:|:------------------|--------------:|:--------:|:------------------|
| **tablefmt** | _string_ | `plain`           | **tablefmt** | _string_ | `orgtbl`          |   
| **tablefmt** | _string_ | `simple`          | **tablefmt** | _string_ | `asciidoc`        |   
| **tablefmt** | _string_ | `github`          | **tablefmt** | _string_ | `jira`            |   
| **tablefmt** | _string_ | `grid`            | **tablefmt** | _string_ | `presto`          |   
| **tablefmt** | _string_ | `simple_grid`     | **tablefmt** | _string_ | `pretty`          |   
| **tablefmt** | _string_ | `rounded_grid`    | **tablefmt** | _string_ | `psql`            |   
| **tablefmt** | _string_ | `heavy_grid`      | **tablefmt** | _string_ | `rst`             |   
| **tablefmt** | _string_ | `mixed_grid`      | **tablefmt** | _string_ | `mediawiki`       |   
| **tablefmt** | _string_ | `double_grid`     | **tablefmt** | _string_ | `moinmoin`        |   
| **tablefmt** | _string_ | `fancy_grid`      | **tablefmt** | _string_ | `youtrack`        |   
| **tablefmt** | _string_ | `outline`         | **tablefmt** | _string_ | `html`            |   
| **tablefmt** | _string_ | `simple_outline`  | **tablefmt** | _string_ | `unsafehtml`      |   
| **tablefmt** | _string_ | `rounded_outline` | **tablefmt** | _string_ | `latex`           |   
| **tablefmt** | _string_ | `heavy_outline`   | **tablefmt** | _string_ | `latex_raw`       |   
| **tablefmt** | _string_ | `mixed_outline`   | **tablefmt** | _string_ | `latex_booktabs`  |   
| **tablefmt** | _string_ | `double_outline`  | **tablefmt** | _string_ | `latex_longtable` |   
| **tablefmt** | _string_ | `fancy_outline`   | **tablefmt** | _string_ | `textile`         |   
| **tablefmt** | _string_ | `pipe`            | **tablefmt** | _string_ | `tsv`             |   

More details : [table](https://xterm.readthedocs.io/en/latest/table/ 'xTerm Table Terminal') | [Notebook Example](https://deepnote.com/app/vector3/xTerm-5a0d16cf-d30e-4373-8564-4b5f7b2d0ed3)

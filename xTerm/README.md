![](https://avatars.githubusercontent.com/u/180863253?s=128)
# xTerm

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

More details : [table](https://github.com/PyxTerm/xTerm/blob/main/docs/table.md)

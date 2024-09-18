Format a fixed width table for pretty printing.

```python
print(Table([[1, 2.34], [-56, "8.999"], ["2", "10001"]]))
```

Output:

```
    ---  ---------
      1      2.34
    -56      8.999
      2  10001
    ---  ---------
```

The first required argument (`table_data`) can be a
list-of-lists (or another iterable of iterables), a list of named
tuples, a dictionary of iterables, an iterable of dictionaries,
an iterable of dataclasses (Python 3.7+), a two-dimensional NumPy array,
NumPy record array, or a Pandas' dataframe.

## Table headers

To print nice column headers, supply the second argument (`headers`):

- `headers` can be an explicit list of column headers
- if `headers="firstrow"`, then the first row of data is used
- if `headers="keys"`, then dictionary keys or column indices are used

Otherwise, a headerless table is produced.

If the number of headers is less than the number of columns, they
are supposed to be names of the last columns. This is consistent
with the plain-text format of R and Pandas' dataframes.

```python
print(Table([["sex", "age"], ["Alice", "F", 24], ["Bob", "M", 19]],
            headers="firstrow"))
```

Output:

```
           sex      age
    -----  -----  -----
    Alice  F         24
    Bob    M         19
```

By default, pandas.DataFrame data have an additional column called
row index. To add a similar column to all other types of data,
use `showindex="always"` or `showindex=True`. To suppress row indices
for all types of data, pass `showindex="never" or `showindex=False`.
To add a custom row index column, pass `showindex=some_iterable`.

```python
print(Table([["F", 24], ["M", 19]], showindex="always"))
```

Output:

```
    -  -  --
    0  F  24
    1  M  19
    -  -  --
```

## Column and Headers alignment

`Table` tries to detect column types automatically, and aligns
the values properly. By default, it aligns decimal points of the
numbers (or flushes integer numbers to the right), and flushes
everything else to the left. Possible column alignments
(`numalign`, `stralign`) are: "right", "center", "left", "decimal"
(only for `numalign`), and None (to disable alignment).

`colglobalalign` allows for global alignment of columns, before any
specific override from `colalign`. Possible values are: None
(defaults according to coltype), "right", "center", "decimal", "left".
`colalign` allows for column-wise override starting from left-most .
column. Possible values are: "global" (no override), "right",
"center", "decimal", "left".
`headersglobalalign` allows for global headers alignment, before any
specific override from `headersalign`. Possible values are: None
(follow columns alignment), "right", "center", "left".
`headersalign` allows for header-wise override starting from left-most
given header. Possible values are: "global" (no override), "same"
(follow column alignment), "right", "center", "left".

Note on intended behaviour: If there is no `table_data`, any column
alignment argument is ignored. Hence, in this case, header
alignment cannot be inferred from column alignment.

## Table formats

`intfmt` is a format specification used for columns which
contain numeric data without a decimal point. This can also be
a list or tuple of format strings, one per column.

`floatfmt` is a format specification used for columns which
contain numeric data with a decimal point. This can also be
a list or tuple of format strings, one per column.

`None` values are replaced with a `missingval` string (like
`floatfmt`, this can also be a list of values for different
columns):

```python
print(Table([["spam", 1, None],
             ...["eggs", 42, 3.14],
             ...["other", None, 2.7]], missingval="?"))
```

Output:

```
    -----  --  ----
    spam    1  ?
    eggs   42  3.14
    other   ?  2.7
    -----  --  ----
```

Various plain-text table formats (`tablefmt`) are supported:
'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
'latex', 'latex_raw', 'latex_booktabs', 'latex_longtable' and tsv.
Variable `Table_formats`contains the list of currently supported formats.

"plain" format doesn't use any pseudographics to draw tables,
it separates columns with a double space:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "plain"))

# strings      numbers
#     spam         41.9999
#     eggs        451
```

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="plain"))

#    spam   41.9999
#    eggs  451
```

"simple" format is like Pandoc simple_tables:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "simple"))
# strings      numbers
# ---------  ---------
# spam         41.9999
# eggs        451
```

---

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="simple"))

# ----  --------
# spam   41.9999
# eggs  451
# ----  --------
```

---
"grid" is similar to tables produced by Emacs table. It uses the package or
Pandoc grid_tables:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "grid"))
# +-----------+-----------+
# | strings   |   numbers |
# +===========+===========+
# | spam      |   41.9999 |
# +-----------+-----------+
# | eggs      |  451      |
# +-----------+-----------+
```

---

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="grid"))
# +------+----------+
# | spam |  41.9999 |
# +------+----------+
# | eggs | 451      |
# +------+----------+
```

---

"simple_grid" draws a grid using single-line box-drawing
characters:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "simple_grid"))
# ┌───────────┬───────────┐
# │ strings   │   numbers │
# ├───────────┼───────────┤
# │ spam      │   41.9999 │
# ├───────────┼───────────┤
# │ eggs      │  451      │
# └───────────┴───────────┘
```

---

"rounded_grid" draws a grid using single-line box-drawing
characters with rounded corners:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "rounded_grid"))
# ╭───────────┬───────────╮
# │ strings   │   numbers │
# ├───────────┼───────────┤
# │ spam      │   41.9999 │
# ├───────────┼───────────┤
# │ eggs      │  451      │
# ╰───────────┴───────────╯
```

---
"heavy_grid" draws a grid using bold (thick) single-line box-drawing
characters:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "heavy_grid"))
# ┏━━━━━━━━━━━┳━━━━━━━━━━━┓
# ┃ strings   ┃   numbers ┃
# ┣━━━━━━━━━━━╋━━━━━━━━━━━┫
# ┃ spam      ┃   41.9999 ┃
# ┣━━━━━━━━━━━╋━━━━━━━━━━━┫
# ┃ eggs      ┃  451      ┃
# ┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

---

"mixed_grid" draws a grid using a mix of light (thin) and heavy (thick) lines
box-drawing characters:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "mixed_grid"))
# ┍━━━━━━━━━━━┯━━━━━━━━━━━┑
# │ strings   │   numbers │
# ┝━━━━━━━━━━━┿━━━━━━━━━━━┥
# │ spam      │   41.9999 │
# ├───────────┼───────────┤
# │ eggs      │  451      │
# ┕━━━━━━━━━━━┷━━━━━━━━━━━┙
```

---

"double_grid" draws a grid using double-line box-drawing
characters:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
# ...                ["strings", "numbers"], "double_grid"))
# ╔═══════════╦═══════════╗
# ║ strings   ║   numbers ║
# ╠═══════════╬═══════════╣
# ║ spam      ║   41.9999 ║
# ╠═══════════╬═══════════╣
# ║ eggs      ║  451      ║
# ╚═══════════╩═══════════╝
```

"fancy_grid" draws a grid using a mix of single and
double-line box-drawing characters:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "fancy_grid"))
# ╒═══════════╤═══════════╕
# │ strings   │   numbers │
# ╞═══════════╪═══════════╡
# │ spam      │   41.9999 │
# ├───────────┼───────────┤
# │ eggs      │  451      │
# ╘═══════════╧═══════════╛
```

---

"outline" is the same as the "grid" format but doesn't draw lines between rows:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "outline"))
# +-----------+-----------+
# | strings   |   numbers |
# +===========+===========+
# | spam      |   41.9999 |
# | eggs      |  451      |
# +-----------+-----------+
print(Table([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="outline"))
# +------+----------+
# | spam |  41.9999 |
# | eggs | 451      |
# +------+----------+
```

"simple_outline" is the same as the "simple_grid" format but doesn't draw lines between rows:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "simple_outline"))
# ┌───────────┬───────────┐
# │ strings   │   numbers │
# ├───────────┼───────────┤
# │ spam      │   41.9999 │
# │ eggs      │  451      │
# └───────────┴───────────┘
```

"rounded_outline" is the same as the "rounded_grid" format but doesn't draw lines between rows:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "rounded_outline"))
# ╭───────────┬───────────╮
# │ strings   │   numbers │
# ├───────────┼───────────┤
# │ spam      │   41.9999 │
# │ eggs      │  451      │
# ╰───────────┴───────────╯
```

---

"heavy_outline" is the same as the "heavy_grid" format but doesn't draw lines between rows:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "heavy_outline"))
# ┏━━━━━━━━━━━┳━━━━━━━━━━━┓
# ┃ strings   ┃   numbers ┃
# ┣━━━━━━━━━━━╋━━━━━━━━━━━┫
# ┃ spam      ┃   41.9999 ┃
# ┃ eggs      ┃  451      ┃
# ┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

"mixed_outline" is the same as the "mixed_grid" format but doesn't draw lines between rows:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "mixed_outline"))
# ┍━━━━━━━━━━━┯━━━━━━━━━━━┑
# │ strings   │   numbers │
# ┝━━━━━━━━━━━┿━━━━━━━━━━━┥
# │ spam      │   41.9999 │
# │ eggs      │  451      │
# ┕━━━━━━━━━━━┷━━━━━━━━━━━┙
```

---

"double_outline" is the same as the "double_grid" format but doesn't draw lines between rows:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "double_outline"))
# ╔═══════════╦═══════════╗
# ║ strings   ║   numbers ║
# ╠═══════════╬═══════════╣
# ║ spam      ║   41.9999 ║
# ║ eggs      ║  451      ║
# ╚═══════════╩═══════════╝
```

---

"fancy_outline" is the same as the "fancy_grid" format but doesn't draw lines between rows:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "fancy_outline"))
# ╒═══════════╤═══════════╕
# │ strings   │   numbers │
# ╞═══════════╪═══════════╡
# │ spam      │   41.9999 │
# │ eggs      │  451      │
# ╘═══════════╧═══════════╛
```

"pipe" is like tables in PHP Markdown Extra extension or Pandoc
pipe_tables:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "pipe"))
# | strings   |   numbers |
# |:----------|----------:|
# | spam      |   41.9999 |
# | eggs      |  451      |
```

---
"presto" is like tables produce by the Presto CLI:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "presto"))
#  strings   |   numbers
# -----------+-----------
#  spam      |   41.9999
#  eggs      |  451

print(Table([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="pipe"))
# |:-----|---------:|
# | spam |  41.9999 |
# | eggs | 451      |
```

"orgtbl" is like tables in Emacs org-mode and orgtbl-mode. They
are slightly different from "pipe" format by not using colons to
define column alignment, and using a "+" sign to indicate line
intersections:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "orgtbl"))
# | strings   |   numbers |
# |-----------+-----------|
# | spam      |   41.9999 |
# | eggs      |  451      |

print(Table([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="orgtbl"))
# | spam |  41.9999 |
# | eggs | 451      |
```

"rst" is like a simple table format from reStructuredText; please
note that reStructuredText accepts also "grid" tables:

```python
print(Table([["spam", 41.9999], ["eggs", "451.0"]],
            ...["strings", "numbers"], "rst"))
# =========  =========
# strings      numbers
# =========  =========
# spam         41.9999
# eggs        451
# =========  =========

print(Table([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="rst"))
# ====  ========
# spam  41.9999
# eggs  451
# ====  ========
```

Number parsing
--------------
By default, anything which can be parsed as a number is a number.
This ensures numbers represented as strings are aligned properly.
This can lead to weird results for particular strings such as
specific git SHAs e.g. "42992e1" will be parsed into the number
429920 and aligned as such.

To completely disable number parsing (and alignment), use
`disable_numparse=True`. For more fine grained control, a list column
indices is used to disable number parsing only on those columns
e.g. `disable_numparse=[0, 2]` would disable number parsing only on the
first and third columns.

Column Widths and Auto Line Wrapping
------------------------------------
xTerm will, by default, set the width of each column to the length of the
longest element in that column. However, in situations where fields are expected
to reasonably be too long to look good as a single line, Table can help automate
word wrapping long fields for you. Use the parameter `maxcolwidth` to provide a
list of maximal column widths

```python
print(Table(
    [('1', 'John Smith',
      'This is a rather long description that might look better if it is wrapped a bit')],
    headers=("Issue Id", "Author", "Description"),
    maxcolwidths=[None, None, 30],
    tablefmt="grid"
    ))
# +------------+------------+-------------------------------+
# |  Issue ID  | Author     | Description                   |
# +============+============+===============================+
# |          1 | John Smith | This is a rather long         |
# |            |            | description that might look   |
# |            |            | better if it is wrapped a bit |
# +------------+------------+-------------------------------+
```

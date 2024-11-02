### Table formatting

There is more than one way to format a table in plain text. The third optional argument named tablefmt defines how the
table is formatted.

Supported table formats are:

| Parameter    |   Type   | Value             | Parameter    |   Type   | Value             |
|:-------------|:--------:|:------------------|--------------|:--------:|:------------------|
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

---

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


---

```python
products = [
    ["Laptop", 1299.99],
    ["Smartphone", 799.99],
    ["Tablet", 499.49],
    ["Headphones", 199.95],
    ["Smartwatch", 249.90],
]

print(Table(
    [[item[0], f"${item[1]:,.2f}"] for item in products],
    headers=["Product", "Price (USD)"],
    tablefmt="fancy_grid"
))
╒════════════╤═══════════════╕
│ Product    │ Price (USD)   │
╞════════════╪═══════════════╡
│ Laptop     │ $1,299.99     │
├────────────┼───────────────┤
│ Smartphone │ $799.99       │
├────────────┼───────────────┤
│ Tablet     │ $499.49       │
├────────────┼───────────────┤
│ Headphones │ $199.95       │
├────────────┼───────────────┤
│ Smartwatch │ $249.90       │
╘════════════╧═══════════════╛

```

---

```python
employees = [
    ["John Doe", 56000, 4],
    ["Jane Smith", 78000, 5],
    ["Emily Davis", 62000, 3],
    ["Michael Johnson", 85000, 4],
    ["Sarah Lee", 50000, 2],
]

print(Table(
    [[emp[0], f"${emp[1]:,}", "★" * emp[2]] for emp in employees],
    headers=["Employee", "Salary", "Rating"],
    tablefmt="rounded_outline"
))
╭─────────────────┬──────────┬──────────╮
│ Employee        │ Salary   │ Rating   │
├─────────────────┼──────────┼──────────┤
│ John Doe        │ $56,000  │ ★★★★     │
│ Jane Smith      │ $78,000  │ ★★★★★    │
│ Emily Davis     │ $62,000  │ ★★★      │
│ Michael Johnson │ $85,000  │ ★★★★     │
│ Sarah Lee       │ $50,000  │ ★★       │
╰─────────────────┴──────────┴──────────╯
```

---

```python
sensors = [
    ["Sensor A", 23.5, "Normal"],
    ["Sensor B", 28.1, "Alert"],
    ["Sensor C", 21.3, "Normal"],
    ["Sensor D", 30.7, "Critical"],
    ["Sensor E", 25.0, "Normal"],
]

print(Table(
    [[sensor[0], f"{sensor[1]}°C", sensor[2]] for sensor in sensors],
    headers=["Sensor", "Temperature", "Status"],
    tablefmt="grid"
))
+----------+---------------+----------+
| Sensor   | Temperature   | Status   |
+==========+===============+==========+
| Sensor A | 23.5°C        | Normal   |
+----------+---------------+----------+
| Sensor B | 28.1°C        | Alert    |
+----------+---------------+----------+
| Sensor C | 21.3°C        | Normal   |
+----------+---------------+----------+
| Sensor D | 30.7°C        | Critical |
+----------+---------------+----------+
| Sensor E | 25.0°C        | Normal   |
+----------+---------------+----------+

```

---

```python
tasks = [
    ["Database Migration", "In Progress", 45],
    ["API Development", "Completed", 100],
    ["Frontend Design", "In Progress", 60],
    ["Backend Optimization", "Not Started", 0],
    ["Testing & QA", "Pending", 20],
]

print(Table(
    [[task[0], task[1], f"{task[2]}%"] for task in tasks],
    headers=["Task", "Status", "Progress"],
    tablefmt="pipe"
))

| Task                 | Status      | Progress   |
|:---------------------|:------------|:-----------|
| Database Migration   | In Progress | 45%        |
| API Development      | Completed   | 100%       |
| Frontend Design      | In Progress | 60%        |
| Backend Optimization | Not Started | 0%         |
| Testing & QA         | Pending     | 20%        |

```

---

```python
students = [
    ["Ali", [85, 90, 78], 84.33],
    ["Sara", [92, 88, 95], 91.67],
    ["Reza", [70, 65, 75], 70.00],
    ["Mina", [88, 80, 82], 83.33],
    ["Hassan", [60, 55, 65], 60.00],
]

print(Table(
    [[
        student[0],
        ", ".join(map(str, student[1])),
        f"{student[2]:.2f}",
        f"{student[2] * 100 / 100:.1f}%"
    ] for student in students],
    headers=["Student", "Scores", "Average", "Percentage"],
    tablefmt="psql"
))

+-----------+------------+-----------+--------------+
| Student   | Scores     |   Average | Percentage   |
|-----------+------------+-----------+--------------|
| Ali       | 85, 90, 78 |     84.33 | 84.3%        |
| Sara      | 92, 88, 95 |     91.67 | 91.7%        |
| Reza      | 70, 65, 75 |     70    | 70.0%        |
| Mina      | 88, 80, 82 |     83.33 | 83.3%        |
| Hassan    | 60, 55, 65 |     60    | 60.0%        |
+-----------+------------+-----------+--------------+

```


---

```python
devices = [
    ["Router", "Online", "2024-10-31 14:30"],
    ["Switch", "Offline", "2024-10-31 08:15"],
    ["Firewall", "Online", "2024-10-30 23:45"],
    ["Access Point", "Maintenance", "2024-10-31 12:20"],
    ["Server", "Online", "2024-10-31 13:55"],
]

print(Table(
    devices,
    headers=["Device", "Status", "Last Update"],
    tablefmt="github"
))

| Device       | Status      | Last Update      |
|--------------|-------------|------------------|
| Router       | Online      | 2024-10-31 14:30 |
| Switch       | Offline     | 2024-10-31 08:15 |
| Firewall     | Online      | 2024-10-30 23:45 |
| Access Point | Maintenance | 2024-10-31 12:20 |
| Server       | Online      | 2024-10-31 13:55 |

```

---

```python
financial_report = [
    ["2020", "$1,200,000", "$800,000", "$400,000", "12.5%"],
    ["2021", "$1,350,000", "$900,000", "$450,000", "13.2%"],
    ["2022", "$1,500,000", "$950,000", "$550,000", "15.3%"],
    ["2023", "$1,800,000", "$1,000,000", "$800,000", "18.2%"],
]

print(Table(
    financial_report,
    headers=["Year", "Revenue", "Expenses", "Net Profit", "Growth Rate"],
    tablefmt="fancy_grid",
    stralign="center",
    numalign="right"
))

╒════════╤════════════╤════════════╤══════════════╤═══════════════╕
│   Year │  Revenue   │  Expenses  │  Net Profit  │  Growth Rate  │
╞════════╪════════════╪════════════╪══════════════╪═══════════════╡
│   2020 │ $1,200,000 │  $800,000  │   $400,000   │     12.5%     │
├────────┼────────────┼────────────┼──────────────┼───────────────┤
│   2021 │ $1,350,000 │  $900,000  │   $450,000   │     13.2%     │
├────────┼────────────┼────────────┼──────────────┼───────────────┤
│   2022 │ $1,500,000 │  $950,000  │   $550,000   │     15.3%     │
├────────┼────────────┼────────────┼──────────────┼───────────────┤
│   2023 │ $1,800,000 │ $1,000,000 │   $800,000   │     18.2%     │
╘════════╧════════════╧════════════╧══════════════╧═══════════════╛

```

---

```python
projects = [
    ["Website Redesign", "2024-09-01", "12 days", "In Progress"],
    ["Mobile App", "2024-08-15", "5 days", "Completed"],
    ["Backend API", "2024-10-10", "3 days", "Testing"],
    ["Cloud Migration", "2024-07-30", "18 days", "Pending"],
    ["Security Update", "2024-08-25", "15 days", "In Progress"],
]

print(Table(
    projects,
    headers=["Project", "Start Date", "Time Remaining", "Status"],
    tablefmt="rounded_outline",
    stralign="center"
))

╭──────────────────┬──────────────┬──────────────────┬─────────────╮
│     Project      │  Start Date  │  Time Remaining  │   Status    │
├──────────────────┼──────────────┼──────────────────┼─────────────┤
│ Website Redesign │  2024-09-01  │     12 days      │ In Progress │
│    Mobile App    │  2024-08-15  │      5 days      │  Completed  │
│   Backend API    │  2024-10-10  │      3 days      │   Testing   │
│ Cloud Migration  │  2024-07-30  │     18 days      │   Pending   │
│ Security Update  │  2024-08-25  │     15 days      │ In Progress │
╰──────────────────┴──────────────┴──────────────────┴─────────────╯

```

---

```python
students = [
    ["Ali", [85, 90, 78, 88], 85.25, "Passed"],
    ["Sara", [92, 88, 95, 96], 92.75, "Passed"],
    ["Reza", [70, 65, 75, 68], 69.5, "Failed"],
    ["Mina", [88, 80, 82, 86], 84.0, "Passed"],
    ["Hassan", [60, 55, 65, 59], 59.75, "Failed"],
]

print(Table(
    [[student[0], ", ".join(map(str, student[1])), f"{student[2]:.2f}", student[3]] for student in students],
    headers=["Student", "Scores", "Average", "Status"],
    tablefmt="psql",
    stralign="center",
    numalign="right"
))

+-----------+----------------+-----------+----------+
|  Student  |     Scores     |   Average |  Status  |
|-----------+----------------+-----------+----------|
|    Ali    | 85, 90, 78, 88 |     85.25 |  Passed  |
|   Sara    | 92, 88, 95, 96 |     92.75 |  Passed  |
|   Reza    | 70, 65, 75, 68 |      69.5 |  Failed  |
|   Mina    | 88, 80, 82, 86 |        84 |  Passed  |
|  Hassan   | 60, 55, 65, 59 |     59.75 |  Failed  |
+-----------+----------------+-----------+----------+

```

---

```python
servers = [
    ["Server 1", "192.168.1.10", "Online", "75%", "65%"],
    ["Server 2", "192.168.1.20", "Offline", "-", "-"],
    ["Server 3", "192.168.1.30", "Maintenance", "40%", "50%"],
    ["Server 4", "192.168.1.40", "Online", "60%", "70%"],
    ["Server 5", "192.168.1.50", "Online", "85%", "90%"],
]

print(Table(
    servers,
    headers=["Server", "IP Address", "Status", "CPU Usage", "Memory Usage"],
    tablefmt="github",
    stralign="center"
))

|  Server  |  IP Address  |   Status    |  CPU Usage  |  Memory Usage  |
|----------|--------------|-------------|-------------|----------------|
| Server 1 | 192.168.1.10 |   Online    |     75%     |      65%       |
| Server 2 | 192.168.1.20 |   Offline   |      -      |       -        |
| Server 3 | 192.168.1.30 | Maintenance |     40%     |      50%       |
| Server 4 | 192.168.1.40 |   Online    |     60%     |      70%       |
| Server 5 | 192.168.1.50 |   Online    |     85%     |      90%       |

```

---

```python
employees = [
    ["John Doe", 5, "$70,000", "★★★★☆", "Excellent"],
    ["Jane Smith", 2, "$50,000", "★★★☆☆", "Good"],
    ["Emily Davis", 7, "$85,000", "★★★★★", "Outstanding"],
    ["Michael Brown", 4, "$60,000", "★★★☆☆", "Average"],
    ["Sarah Lee", 3, "$55,000", "★★★☆☆", "Good"],
]

print(Table(
    employees,
    headers=["Employee", "Experience (Years)", "Salary", "Rating", "Evaluation"],
    tablefmt="pipe",
    stralign="center"
))

|   Employee    |   Experience (Years) |  Salary  |  Rating  |  Evaluation  |
|:-------------:|---------------------:|:--------:|:--------:|:------------:|
|   John Doe    |                    5 | $70,000  |  ★★★★☆   |  Excellent   |
|  Jane Smith   |                    2 | $50,000  |  ★★★☆☆   |     Good     |
|  Emily Davis  |                    7 | $85,000  |  ★★★★★   | Outstanding  |
| Michael Brown |                    4 | $60,000  |  ★★★☆☆   |   Average    |
|   Sarah Lee   |                    3 | $55,000  |  ★★★☆☆   |     Good     |

```
---

```python
crypto_assets = [
    ["Bitcoin", 2.5, "$60,000", "$150,000"],
    ["Ethereum", 10, "$4,000", "$40,000"],
    ["Ripple", 5000, "$0.50", "$2,500"],
    ["Litecoin", 15, "$150", "$2,250"],
    ["Cardano", 2000, "$2.10", "$4,200"],
]

print(Table(
    crypto_assets,
    headers=["Asset", "Quantity", "Price per Unit", "Total Value"],
    tablefmt="fancy_grid",
    numalign="right"
))

╒══════════╤════════════╤══════════════════╤═══════════════╕
│ Asset    │   Quantity │ Price per Unit   │ Total Value   │
╞══════════╪════════════╪══════════════════╪═══════════════╡
│ Bitcoin  │        2.5 │ $60,000          │ $150,000      │
├──────────┼────────────┼──────────────────┼───────────────┤
│ Ethereum │         10 │ $4,000           │ $40,000       │
├──────────┼────────────┼──────────────────┼───────────────┤
│ Ripple   │       5000 │ $0.50            │ $2,500        │
├──────────┼────────────┼──────────────────┼───────────────┤
│ Litecoin │         15 │ $150             │ $2,250        │
├──────────┼────────────┼──────────────────┼───────────────┤
│ Cardano  │       2000 │ $2.10            │ $4,200        │
╘══════════╧════════════╧══════════════════╧═══════════════╛

```

---

```python
matches = [
    ["Team A", "Team B", 3, 2, "Team A"],
    ["Team C", "Team D", 1, 1, "Draw"],
    ["Team E", "Team F", 0, 2, "Team F"],
    ["Team G", "Team H", 4, 1, "Team G"],
    ["Team I", "Team J", 2, 2, "Draw"],
]

print(Table(
    matches,
    headers=["Home Team", "Away Team", "Home Score", "Away Score", "Result"],
    tablefmt="grid",
    stralign="center",
    numalign="right"
))

+-------------+-------------+--------------+--------------+----------+
|  Home Team  |  Away Team  |   Home Score |   Away Score |  Result  |
+=============+=============+==============+==============+==========+
|   Team A    |   Team B    |            3 |            2 |  Team A  |
+-------------+-------------+--------------+--------------+----------+
|   Team C    |   Team D    |            1 |            1 |   Draw   |
+-------------+-------------+--------------+--------------+----------+
|   Team E    |   Team F    |            0 |            2 |  Team F  |
+-------------+-------------+--------------+--------------+----------+
|   Team G    |   Team H    |            4 |            1 |  Team G  |
+-------------+-------------+--------------+--------------+----------+
|   Team I    |   Team J    |            2 |            2 |   Draw   |
+-------------+-------------+--------------+--------------+----------+

```


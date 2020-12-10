
# Table of Contents

1.  [Dataset](#org0d21a5d)
    1.  [Variables](#org7feb939)
    2.  [Data sources](#orgf83378e)
2.  [Prototyping](#org39f0f68)
    1.  [Features](#org850f2ea)
    2.  [Wireframe](#org00cb457)
3.  [Development](#org909a422)
    1.  [Why did we pick Dash?](#org274dca1)
    2.  [Architecture](#orgbfbe61b)
        1.  [Structure of `app.py`](#org3834c0b)
            -   [Globals](#org1a561f9)
            -   [Layout](#orgc060127)
            -   [Callbacks functions](#org084a2c5)
    3.  [Visual identity guidelines](#orgc6f66d4)
        1.  [Colors](#orgb4c6f8a)
            -   [Primary colors](#org2a17b83)
            -   [Secondary colors](#org32f3529)
        2.  [Fonts](#orgb2a2e6d)
            -   [Primary fonts](#orgd254b8f)
            -   [Secondary fonts](#org02fe1e6)
        3.  [Logo](#orge02fe30)
            -   [Symbol](#org12fabfa)
            -   [Logotype](#org697a356)
    4.  [How to contribute](#orgd249d81)
        1.  [Setting up a new Git repository](#org72c565e)
        2.  [Adding or modifying owned files (`push`)](#org8f4a35d)
        3.  [Submit proposed changes to review (`pull-request`)](#orgcc58583)
4.  [Tools that we used](#orgc53a177)



<a id="org0d21a5d"></a>

# Dataset


<a id="org7feb939"></a>

## Variables


<a id="orgf83378e"></a>

## Data sources


<a id="org39f0f68"></a>

# Prototyping


<a id="org850f2ea"></a>

## Features


<a id="org00cb457"></a>

## Wireframe


<a id="org909a422"></a>

# Development


<a id="org274dca1"></a>

## Why did we pick [Dash](https://plotly.com/dash/)?

As we wanted to use Python to build the Dashboard we had to pick among [Python dashboard libraries](https://pyviz.org/tools.html) :

![img](./Pics/dashboardlibraries.png "Python dashboarding libraries")

According to following benchmarck the team decided to develop the PoC with ****Dash****

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Maturity</th>
<th scope="col" class="org-left">Popularity</th>
<th scope="col" class="org-left">Simplicity</th>
<th scope="col" class="org-left">Adaptability</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Streamlit</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>


<tr>
<td class="org-left">Dash</td>
<td class="org-left">B</td>
<td class="org-left">A</td>
<td class="org-left">B</td>
<td class="org-left">B</td>
</tr>


<tr>
<td class="org-left">Voila</td>
<td class="org-left">C</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>
</tbody>
</table>

****Maturity****: Based on the age of the project and how stable it is.

****Popularity****: Based on adoption and GitHub stars.

****Simplicity****: Based on how easy it is to get started using the library.

****Adaptability****: Based on how flexible and opinionated the library is.


<a id="orgbfbe61b"></a>

## Architecture


<a id="org3834c0b"></a>

### Structure of `app.py`


<a id="org1a561f9"></a>

#### Globals


##### Loading libraries, style, and data

-   Libraries

-   Style

-   Pandas DataFrame


##### Data prep


##### Global functions


<a id="orgc060127"></a>

#### Layout


<a id="org084a2c5"></a>

#### Callbacks functions


<a id="orgc6f66d4"></a>

## Visual identity guidelines


<a id="orgb4c6f8a"></a>

### Colors


<a id="org2a17b83"></a>

#### Primary colors


<a id="org32f3529"></a>

#### Secondary colors


<a id="orgb2a2e6d"></a>

### Fonts


<a id="orgd254b8f"></a>

#### Primary fonts


<a id="org02fe1e6"></a>

#### Secondary fonts


<a id="orge02fe30"></a>

### Logo


<a id="org12fabfa"></a>

#### Symbol


<a id="org697a356"></a>

#### Logotype


<a id="orgd249d81"></a>

## How to contribute


<a id="org72c565e"></a>

### Setting up a new Git repository

-   Clone project locally

```sh
git init
git clone https://github.com/dataforgoodfr/batch8_carbon4/tree/master/plateforme
```
-   Ask to join our GitHub


<a id="org8f4a35d"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

```sh
git add filename
git commit
git push
```

Where `filename` is the name of the file


<a id="orgcc58583"></a>

### Submit proposed changes to review (`pull-request`)

When modifying an existing file, if you're not its owner, you have to submit the modifications to its owner (i.e. reviewer). Ownership is distributed as follow :

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Owner GitHub name</th>
<th scope="col" class="org-left">File</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">linetonthat</td>
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">j-back</td>
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">morgandavidson</td>
<td class="org-left">`README.md`</td>
</tr>
</tbody>
</table>

To submit changes reviewees have to do :

```sh
git branch new-branch        #Creates a new branch nammed "new-branch"
git checkout new-branch   #Switch to "new-branch"
# alternatively these two commands can be condensed to "git checkout -b new-branch"
git add filename
git commit
git push origin new-branch
git checkout master          #Switch back to master
```

Then go on our [GitHub](https://github.com/dataforgoodfr/batch8_worldbank), and simply click on `compare & pull request` and pick a reviewer. Or do

-   cilck on `Pull requests`,
-   then on `New Pull Request`,
-   click on `compare across forks`,
-   select : `dataforgoodfr/batch8_carbon4 | =base: master` <- `revieweename/batch8_carbon4` | `new-branch`,
-   click on `create pull request`
-   enter GitHub reviewer name in `reviewers`, add title and comment,
-   click on `create pull request`


<a id="orgc53a177"></a>

# Tools that we used

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Tools</th>
<th scope="col" class="org-left">Usage</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Slack</td>
<td class="org-left">Chat</td>
</tr>


<tr>
<td class="org-left">Pycharm, Jupyter</td>
<td class="org-left">Code editing</td>
</tr>


<tr>
<td class="org-left">Git, GitHub</td>
<td class="org-left">Code storage/versioning</td>
</tr>


<tr>
<td class="org-left">Python, CSS</td>
<td class="org-left">Coding languages</td>
</tr>


<tr>
<td class="org-left">Org-mode, Github, Notion</td>
<td class="org-left">Documentation</td>
</tr>


<tr>
<td class="org-left">Zoom</td>
<td class="org-left">Meetings</td>
</tr>


<tr>
<td class="org-left">dash, pandas</td>
<td class="org-left">Python librairies</td>
</tr>


<tr>
<td class="org-left">Google Slides</td>
<td class="org-left">Wireframing</td>
</tr>
</tbody>
</table>

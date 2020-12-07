
# Table of Contents

1.  [Dataset](#org49fb2c2)
    1.  [Variables](#orgd6bc55f)
    2.  [Data sources](#org98031a7)
2.  [Prototyping](#org7227fc6)
    1.  [Features](#org8f3b227)
    2.  [Wireframe](#org80c763d)
3.  [Development](#orgf13c97b)
    1.  [Why did we pick Dash?](#orgf31be37)
    2.  [Architecture](#orgc99d593)
        1.  [Structure of `app.py`](#org0a2a5eb)
            -   [Globals](#org6735779)
            -   [Layout](#org4e06c70)
            -   [Callbacks functions](#orgae95974)
    3.  [Visual identity guidelines](#orgfeefe86)
        1.  [Colors](#org188f030)
            -   [Primary colors](#orgbd6a26b)
            -   [Secondary colors](#orgeb3d231)
        2.  [Fonts](#orgcd04d00)
            -   [Primary fonts](#org3b3bc84)
            -   [Secondary fonts](#org00c6f82)
        3.  [Logo](#orge7a0dc5)
            -   [Symbol](#orgd91d81d)
            -   [Logotype](#orgf1bc2c0)
    4.  [How to contribute](#org99a8352)
        1.  [Setting up a new Git repository](#org960c680)
        2.  [Adding or modifying owned files (`push`)](#org632c11d)
        3.  [Submit proposed changes to review](#orgb63dfe2)
4.  [Tools that we used](#org4a48c28)



<a id="org49fb2c2"></a>

# Dataset


<a id="orgd6bc55f"></a>

## Variables


<a id="org98031a7"></a>

## Data sources


<a id="org7227fc6"></a>

# Prototyping


<a id="org8f3b227"></a>

## Features


<a id="org80c763d"></a>

## Wireframe


<a id="orgf13c97b"></a>

# Development


<a id="orgf31be37"></a>

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


<a id="orgc99d593"></a>

## Architecture


<a id="org0a2a5eb"></a>

### Structure of `app.py`


<a id="org6735779"></a>

#### Globals


##### Loading libraries, style, and data

-   Libraries

-   Style

-   Pandas DataFrame


##### Data prep


##### Global functions


<a id="org4e06c70"></a>

#### Layout


<a id="orgae95974"></a>

#### Callbacks functions


<a id="orgfeefe86"></a>

## Visual identity guidelines


<a id="org188f030"></a>

### Colors


<a id="orgbd6a26b"></a>

#### Primary colors


<a id="orgeb3d231"></a>

#### Secondary colors


<a id="orgcd04d00"></a>

### Fonts


<a id="org3b3bc84"></a>

#### Primary fonts


<a id="org00c6f82"></a>

#### Secondary fonts


<a id="orge7a0dc5"></a>

### Logo


<a id="orgd91d81d"></a>

#### Symbol


<a id="orgf1bc2c0"></a>

#### Logotype


<a id="org99a8352"></a>

## How to contribute


<a id="org960c680"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub


<a id="org632c11d"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="orgb63dfe2"></a>

### Submit proposed changes to review

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
<td class="org-left">line</td>
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">j-back</td>
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">morgandavidson</td>
<td class="org-left">??</td>
</tr>
</tbody>
</table>

To submit changes reviewees have to do: 

    $ git add filename
    $ git commit
    $ git push https://github.com/revieweename/batch8_worldbank

Where `revieweename` is the GitHub name of the reviewee.
Then go on our [GitHub](https://github.com/dataforgoodfr/batch8_worldbank), 

-   cilck on `Pull requests`,
-   then on `New Pull Request`,
-   click on `compare across forks`,
-   select : `dataforgoodfr/batch8_worldbank` | `base: master` <- `revieweename/batch8_worldbank` | `master`,
-   click on `create pull request`
-   enter GitHub reviewer name in `reviewers`, add title and comment,
-   click on `create pull request`


<a id="org4a48c28"></a>

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




# Table of Contents

1.  [Dataset](#org6af3af6)
    1.  [Variables](#org59f4cd8)
    2.  [Data sources](#org199aa20)
2.  [Prototyping](#orga475819)
    1.  [Features](#org0126bdc)
    2.  [Wireframe](#org229a195)
3.  [Development](#orgd46f015)
    1.  [Why did we pick Dash?](#org0c44cfe)
    2.  [Architecture](#org9b7c9c3)
        1.  [Structure of `app.py`](#orgd72ab21)
            -   [Globals](#org1140793)
            -   [Layout](#org93311b5)
            -   [Callbacks functions](#orge434711)
    3.  [Visual identity guidelines](#orgf1cc28b)
        1.  [Colors](#orgc120995)
            -   [Primary colors](#org1973bbb)
            -   [Secondary colors](#org3ccd105)
        2.  [Fonts](#orgc8b665f)
            -   [Primary fonts](#org4142988)
            -   [Secondary fonts](#org437d963)
        3.  [Logo](#org87449ce)
            -   [Symbol](#org897bf7d)
            -   [Logotype](#org9b3e358)
    4.  [How to contribute](#org8f552ec)
        1.  [Setting up a new Git repository](#org5f151fb)
        2.  [Adding or modifying owned files (`push`)](#orgf8e69c2)
        3.  [Submit proposed changes to review](#org8f79e20)
4.  [Tools that we used](#orgb969a81)



<a id="org6af3af6"></a>

# Dataset


<a id="org59f4cd8"></a>

## Variables


<a id="org199aa20"></a>

## Data sources


<a id="orga475819"></a>

# Prototyping


<a id="org0126bdc"></a>

## Features


<a id="org229a195"></a>

## Wireframe


<a id="orgd46f015"></a>

# Development


<a id="org0c44cfe"></a>

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


<a id="org9b7c9c3"></a>

## Architecture


<a id="orgd72ab21"></a>

### Structure of `app.py`


<a id="org1140793"></a>

#### Globals


##### Loading libraries, style, and data

-   Libraries

-   Style

-   Pandas DataFrame


##### Data prep


##### Global functions


<a id="org93311b5"></a>

#### Layout


<a id="orge434711"></a>

#### Callbacks functions


<a id="orgf1cc28b"></a>

## Visual identity guidelines


<a id="orgc120995"></a>

### Colors


<a id="org1973bbb"></a>

#### Primary colors


<a id="org3ccd105"></a>

#### Secondary colors


<a id="orgc8b665f"></a>

### Fonts


<a id="org4142988"></a>

#### Primary fonts


<a id="org437d963"></a>

#### Secondary fonts


<a id="org87449ce"></a>

### Logo


<a id="org897bf7d"></a>

#### Symbol


<a id="org9b3e358"></a>

#### Logotype


<a id="org8f552ec"></a>

## How to contribute


<a id="org5f151fb"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub


<a id="orgf8e69c2"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="org8f79e20"></a>

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
<td class="org-left">linetonthat</td>
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


<a id="orgb969a81"></a>

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



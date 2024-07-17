\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ucph-handout}[2019/12/26 ucph-handout]

\PassOptionsToClass{a4paper}{memoir}
\PassOptionsToClass{oneside}{memoir}
\PassOptionsToClass{10pts}{memoir}
\PassOptionsToClass{article}{memoir}
\ProcessOptions
\LoadClass{memoir}

%%%%%%%%% DEFAULT PACKAGES %%%%%%%%%
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{palatino}
\RequirePackage[scaled]{beramono}
\RequirePackage{lato}
\RequirePackage{graphicx}
\RequirePackage[table]{xcolor}
\RequirePackage{url}
\RequirePackage[hidelinks,hyperindex]{hyperref}
\RequirePackage{listings}
\RequirePackage{tikz}
\usetikzlibrary{positioning,arrows}
\RequirePackage{datetime}
\RequirePackage[most]{tcolorbox}
\RequirePackage{textcomp}
\RequirePackage{microtype}
\RequirePackage{todonotes}
\RequirePackage{soul}
\presetkeys{todonotes}{inline}{}

%%%%%%%% DIMENSIONS %%%%%%%%
\setlrmarginsandblock{35mm}{*}{1}

% Distance between header and content
\setlength{\headsep}{1cm}
\checkandfixthelayout

%%%%%%%%% COLORS   %%%%%%%%%
\definecolor{kugrey}{RGB}{102,102,102}

%%%%%%%%% HEADINGS %%%%%%%%%
% Bold face section headings and figure captions
\setsecheadstyle{\bfseries\large}
\captionnamefont{\bfseries}

% No chapter and section numbers
\setsecnumdepth{part}

%%%%%%% UCPH LOGO %%%%%%%
\providecommand*{\ucphlogo}{\includegraphics[width=30mm]{ucphlogo-mini-da.pdf}}

% Change logo if language is changed using babel
\AtBeginDocument{
  \@ifpackagewith{babel}{english}{%
    \renewcommand*\ucphlogo{\includegraphics[width=30mm]{ucphlogo-mini-en.pdf}}
  }{}
}

% Allow changing logo by passing english as classoption
\DeclareOption{english}{
    \renewcommand*\ucphlogo{\includegraphics[width=30mm]{ucphlogo-mini-en.pdf}}
}
\ProcessOptions\relax

%%%%%%%%% HEADER & FOOTER %%%%%%%%%
\newcommand{\HeadFootStyle}{\sffamily\color{kugrey}}
\newcommand{\Title}{}
\newcommand{\Author}{}
\newcommand{\AuthorEmail}{}
\newcommand{\TimeAndLocation}{\monthname, \the\year}
\makepagestyle{ucph-handout}
\makeoddhead{ucph-handout}
  {\Large\HeadFootStyle \Title \vspace{0.01mm} }
  {}
  {\ucphlogo}
\makeoddfoot{ucph-handout}
  {}
  {\small\HeadFootStyle\thepage}
  {\small\HeadFootStyle\Author\hfill\\\vspace{-0.5mm} \AuthorEmail}
% Horizontal ruler below header
\makeheadfootruleprefix{ucph-handout}{\HeadFootStyle}{}
\makeheadrule{ucph-handout}{\textwidth}{\normalrulethickness}
\pagestyle{ucph-handout}

%%%%%%%% CONTENT BOXES %%%%%%%%
\newtcolorbox{exercisebox}[1][]{
  fonttitle=\bfseries\large,
  colback=white,
  coltitle=black,
  colbacktitle=black!10,
  boxrule=0.25pt,
  before upper=\renewcommand\thempfootnote{\fnsymbol{mpfootnote}},
  #1
}

%%%%%%%%% CODE BLOCKS %%%%%%%%%
\lstset{
    basicstyle=\ttfamily\footnotesize,
    literate=%
{æ}{{\ae}}{1}
{å}{{\aa}}{1}
{ø}{{\o}}{1}
{Æ}{{\AE}}{1}
{Å}{{\AA}}{1}
{Ø}{{\O}}{1}
}

\lstdefinelanguage{JavaScript}{
  keywords={typeof, new, true, false, catch, function, return, null, catch, switch, var, if, in, while, do, else, case, break},
  ndkeywords={class, export, boolean, throw, implements, import, this},
  sensitive=false,
  comment=[l]{//},
  morecomment=[s]{/*}{*/},
  morestring=[b]',
  morestring=[b]"
}

\lstdefinestyle{myjavascript}{
  keywordstyle=\bfseries,
  captionpos=b,
  language=JavaScript,
  keywordstyle=\bfseries,
  identifierstyle=\color{black},
  ndkeywordstyle=\color{darkgray}\bfseries,
  commentstyle=\color{gray}\ttfamily,
  stringstyle=\color{red}\ttfamily,
  showstringspaces=false
}
\lstdefinestyle{mypython}{
  keywordstyle=\bfseries,
  captionpos=b,
  language=Python,
  keywordstyle=\bfseries,
  identifierstyle=\color{black},
  ndkeywordstyle=\color{darkgray}\bfseries,
  commentstyle=\color{gray}\ttfamily,
  % stringstyle=\color{red}\ttfamily,
  stringstyle=\color{gray}\ttfamily,%\colorbox{black!10},
  showstringspaces=false
}


\lstnewenvironment{code}[1][]{}{}
\lstnewenvironment{python}[1][]{\lstset{style=mypython, xleftmargin=4mm}}{}
\lstnewenvironment{javascript}[1][]{\lstset{style=myjavascript, xleftmargin=4mm}}{}

\def\inlinepython{\lstinline[style=mypython]}
\def\ttpy{\lstinline[style=mypython]}
\def\ttjs{\lstinline[style=myjavascript]}
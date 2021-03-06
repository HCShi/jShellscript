% The swfcthesis class is for producing senior year theses and dissertations
% that meet the SWFU requirements.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{swfcthesis} % [TeX Live 2016/Debian SWFU Theses and Dissertations]
% pass unknown options to book
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\LoadClass[a4paper,12pt,oneside]{book}
\RequirePackage{ifxetex} % This class can only be processed with XeTeX
\RequirePackage[top=3cm,bottom=2.5cm,left=3cm,right=2.5cm,
nomarginpar,headheight=15pt, % to avoid "headheight too small"
%showframe,showcrop,
]{geometry}
\RequirePackage{indentfirst}
\RequirePackage{tabu,longtable,multicol,multirow,array}
% graphicx
\RequirePackage[xetex]{graphicx} % before xltxtra
\graphicspath{{./figs/}{../figs/}{./img/}{../img/}{./}{../}} %mind the trailing “ / ”
% titlesec
\RequirePackage{titlesec} % \titleformat, \titlespacing
\titleformat{\chapter}{\centering\LARGE\bfseries}{\thechapter}{1em}{}
\titlespacing{\chapter}{0pt}{*0}{*4}
\RequirePackage[bottom]{footmisc} % stick footnote at bottom of page
% fancyhdr
\RequirePackage{fancyhdr}
\fancypagestyle{plain}{%
\fancyhf{} % clear all header and footer fields
\fancyfoot[C]{\fontsize{8}{8}\selectfont -- \thepage\ --}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
}
\fancyhf{}
\fancyfoot[C]{\fontsize{8}{8}\selectfont -- \thepage\ --}
\fancyhead[C]{\slshape \leftmark}
\RequirePackage{enumitem} % \setlist
\setlist{nosep} % kills all vertical spacing
\RequirePackage[backend=biber,url=true,hyperref=true,
doi=false,isbn=false,style=caspervector,utf8,sorting=centy]{biblatex}
\renewcommand*{\bibfont}{\small} % 11pt
\DeclareFieldFormat*{year}{#1}
%%%% caspervector provides \supercite already.
% \DeclareCiteCommand{\supercite}[\mkbibsuperscript]
% {\iffieldundef{prenote}
%
{}
%
{\BibliographyWarning{Ignoring prenote argument}}%
%
\iffieldundef{postnote}
%
{}
%
{\BibliographyWarning{Ignoring postnote argument}}}
% {\usebibmacro{citeindex}%
%
\bibopenbracket\usebibmacro{cite}\bibclosebracket}
% {\supercitedelim}
% {}
\let\cite=\supercite
% caption
\RequirePackage{caption} % \captionsetup
\RequirePackage{subcaption}
\captionsetup{labelsep=quad}
\RequirePackage{xcolor}
\RequirePackage{hyperref}
\hypersetup{%
bookmarksnumbered,pdfpagelabels=true,plainpages=false,breaklinks=true,
colorlinks=false,
pdfborderstyle={/S/U/W .3},% border style will be underline of width .3pt
linkbordercolor=red,
% internal links
citebordercolor=cyan,
% links to bibliography
filebordercolor=magenta,
% file links
urlbordercolor=blue,
% external links
%linkcolor=black,citecolor=black,urlcolor=blue
}
% before xunicode!
\RequirePackage{amsmath,amsfonts,amssymb,latexsym,marvosym,pifont}
\RequirePackage[tt=false]{libertine} % keyboard symbol
\RequirePackage{xltxtra} %fontspec,xunicode are loaded here.
\RequirePackage[CJKmath=true,AutoFakeSlant=true]{xeCJK} % slant header
% \singlespacing, \onehalfspacing, \doublespacing
\RequirePackage[doublespacing]{setspace}
\renewcommand{\doublespacing}{\setstretch{1.6}}
%%% Obsolete! setspace package is perfered to setting baselinestretch directly.
% \newcommand{\normalspace}
%
{\par\renewcommand{\baselinestretch}{1}\small\normalsize\par}
% \newcommand{\singlespace}
%
{\par\renewcommand{\baselinestretch}{1.2}\small\normalsize\par}
% \newcommand{\doublespace}% 30 lines per page
%
{\par\renewcommand{\baselinestretch}{1.6}\small\normalsize\par}
\defaultfontfeatures{Mapping=tex-text}
\setmainfont{Liberation Serif}
\setsansfont{Liberation Sans}
\setCJKmainfont[BoldFont={Adobe Heiti Std}]{Adobe Song Std}
\setCJKsansfont[BoldFont={Adobe Heiti Std}]{Adobe Song Std}
\setCJKmonofont{Noto Sans Mono CJK SC Regular}
\setCJKfamilyfont{hei}{Adobe Heiti Std}
\setCJKfamilyfont{song}{Adobe Song Std}
\newCJKfontfamily\quotefont{Adobt Kaiti Std}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
\pagenumbering{arabic}
\renewcommand{\headrulewidth}{.4pt}
\urlstyle{rm}
\raggedbottom
\pagestyle{fancy}
% Must go after the first call of \pagestyle{fancy} !!!
\renewcommand{\chaptermark}[1]{\markboth{\thechapter \ \ #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection \ \ #1}}
\newcommand{\Appendix}[1]{%
\renewcommand{\chaptermark}[1]%
{\markboth{附录\ \thechapter \ \ #1}{}}
\titleformat{\chapter}%
{\centering\LARGE\bfseries}{附录\ \thechapter}{1em}{}
\appendix
}
% set caption label style to, e.g. 3-2.
\renewcommand{\thefigure}{\thechapter{}-\arabic{figure}}
\renewcommand{\thetable}{\thechapter{}-\arabic{table}}
\renewcommand{\thesubfigure}{\thechapter{}-\arabic{subfigure}}
\renewcommand{\thesubtable}{\thechapter{}-\arabic{subtable}}
% not used. use \makebox instead.
\newcommand{\ziju}[1]{\renewcommand{\CJKglue}{\hskip #1}}
%\renewcommand{\bibname}{ 参考文献 } % only for bibtex. Obsolete!
\renewcommand{\contentsname}{目\hspace{1em} 录}
\renewcommand{\listfigurename}{插图目录}
\renewcommand{\listtablename}{表格目录}
\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}
% Variables to hold the text fields for the preliminary pages
\newcommand{\Title}[1]{\gdef\SWFCField@Title{#1}}
\newcommand{\enTitle}[1]{\gdef\SWFCField@enTitle{#1}}
\newcommand{\Author}[1]{\gdef\SWFCField@Author{#1}}
\newcommand{\enAuthor}[1]{\gdef\SWFCField@enAuthor{#1}}
\newcommand{\Docname}[1]{\gdef\SWFCField@Docname{#1}}
\newcommand{\Degree}[1]{\gdef\SWFCField@Degree{#1}}
\newcommand{\Advisor}[1]{\gdef\SWFCField@Advisor{#1}}
\newcommand{\AdvisorTitle}[1]{\gdef\SWFCField@AdvisorTitle{#1}}
\newcommand{\AdvisorInfo}[1]{\gdef\SWFCField@AdvisorInfo{#1}}
\newcommand{\Month}[1]{\gdef\SWFCField@Month{#1}}
\newcommand{\Year}[1]{\gdef\SWFCField@Year{#1}}
\newcommand{\Abstract}[1]{\gdef\SWFCField@Abstract{#1}}
\newcommand{\enAbstract}[1]{\gdef\SWFCField@enAbstract{#1}}
\newcommand{\Keywords}[1]{\gdef\SWFCField@Keywords{#1}}
\newcommand{\enKeywords}[1]{\gdef\SWFCField@enKeywords{#1}}
\newcommand{\Acknowledgments}[1]{\gdef\SWFCField@Acknowledgments{#1}}
\newcommand{\School}[1]{\gdef\SWFCField@School{#1}}
\newcommand{\enSchool}[1]{\gdef\SWFCField@enSchool{#1}}
\newcommand{\Univ}[1]{\gdef\SWFCField@Univ{#1}}
\newcommand{\enUniv}[1]{\gdef\SWFCField@enUniv{#1}}
\newcommand{\Subject}[1]{\gdef\SWFCField@Subject{#1}}
\newcommand{\SWFCtitlepage}{% Title page layout
\thispagestyle{empty}
\begin{center}
\makebox[14.7em][s]{{\huge\SWFCField@Univ}}\\[5mm]
\makebox[25.75em][s]{\Huge\textbf{\SWFCField@Docname}}\\[5mm]
\makebox[12em][s]{\hspace{.5em}\LARGE(\SWFCField@Year\, 届)}\\[60pt]
\begin{minipage}{.8\linewidth}
\begin{Large}
\extrarowsep=^8mm
\extrarowsep=_-7pt
\begin{tabu}spread\textwidth{@{}X[r]X[3.3,c]@{}}
\textbf{题\hspace{2em} 目:}&\SWFCField@Title\\\tabucline{2-2}
\textbf{分院系部:} &\SWFCField@School\\\tabucline{2-2}
\textbf{专\hspace{2em} 业:}&\SWFCField@Subject\\\tabucline{2-2}
\textbf{姓\hspace{2em} 名:}&\SWFCField@Author\\\tabucline{2-2}
\textbf{导师姓名:} &\SWFCField@Advisor\\\tabucline{2-2}
\textbf{导师职称:} &\SWFCField@AdvisorTitle\\\tabucline{2-2}
\end{tabu}
\end{Large}
\end{minipage}
\vfill
{\Large\textbf{\SWFCField@Year\ 年\ \SWFCField@Month\ 月}}\\[1cm]
\end{center}
\clearpage
}
\newcommand{\abstractpage}{% Abstract page
\providecommand\pdfbookmark[3][]{} \pdfbookmark[0]{摘要}{bm:cnAbstract}
\thispagestyle{empty}
\begin{center}
{\singlespacing \Large{\textbf{\SWFCField@Title}}}\\[5mm]
\large{\SWFCField@Author}\\
\large{(\SWFCField@Univ\,\SWFCField@School,云南\, 昆明\,650224)}
\end{center}
\vskip 3ex
\noindent \textbf{摘\hspace{1em} 要:}~\SWFCField@Abstract
\vskip 2ex
\noindent \textbf{关键词:}~\SWFCField@Keywords
\clearpage
}
\newcommand{\enabstractpage}{% English abstract page
\providecommand\pdfbookmark[3][]{}%
\pdfbookmark[0]{Abstract}{bm:Abstract}
\thispagestyle{empty}
\begin{center}
{\singlespacing {\Large\textbf{\SWFCField@enTitle}}}\\[5mm]
{\large\SWFCField@enAuthor}\\[3mm]
{\singlespacing {\large\SWFCField@enSchool\\\SWFCField@enUniv\\%
Kunming 650224, Yunnan, China}}
\end{center}
\vskip 2em
\noindent\textbf{Abstract: }~\SWFCField@enAbstract
\vskip 1em
\noindent\textbf{Key words: }~\SWFCField@enKeywords
\clearpage
}
\newcommand{\acknowledgmentspage}{% Acknowledgments page
\phantomsection
\addcontentsline{toc}{chapter}{致\hspace{1em} 谢}
\chapter*{致\hspace{1em} 谢}
\SWFCField@Acknowledgments
}
\newcommand{\advisorinfopage}{% Advisor info page
\phantomsection
\addcontentsline{toc}{chapter}{指导教师简介}
\chapter*{指导教师简介}
\SWFCField@AdvisorInfo
\clearpage
}
\newcommand{\makepreliminarypages}{% preliminary pages
\SWFCtitlepage
\doublespacing % global line spacing
\abstractpage
\enabstractpage
}
\RequirePackage{minted} % minted has to be loaded at last!!!
\usemintedstyle{bw}
\renewcommand{\listingscaption}{程序} % used by minted
\renewcommand{\listoflistingscaption}{程序目录}
\setlength{\parindent}{2em}
% Initialize the variables to their default values
\Title{}
\Author{}
\Docname{}
\Advisor{}
\AdvisorTitle{}
\AdvisorInfo{}
\Month{}
\Year{}
\Univ{}
\School{}
\Subject{}
\Abstract{}
\Keywords{}
\Acknowledgments{}
% The followings are for the English Abstract.
\enTitle{}
\enAuthor{}
\enUniv{}
\enSchool{}
\enAbstract{}
\enKeywords{}

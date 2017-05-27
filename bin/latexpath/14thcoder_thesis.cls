%%================================================================
%% 下面 5 行是通用的
%%================================================================
% The 14thcoder_article class is for producing senior year theses and dissertations that meet the SWFU requirements.
\NeedsTeXFormat{LaTeX2e}[1999/12/01]
% specifies which version of TeX or LaTeX is required at least to run your package.
% The optional date may be used to specify the version more precisely.
\ProvidesClass{14thcoder_thesis}[2017/03/30] % 发布日期
% it has to have the same name of the file without the extension.
% It tells LaTeX the name of the package and will allow it to issue a sensible error message when you try to include a package twice.
% The date is important since it can be used by other package to specify the minimum version requirement they need to use your package.
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}} % book 功能比较多
% it are end-user parameters. Each option is declared by one such command.
% pass unknown options to book
% \PassOptionsToClass and \PassOptionsToPackage are used to automatically invoke the corresponding options when the class or the package is loaded.
\ProcessOptions\relax % terminates the option processing.
\LoadClass[a4paper, 12pt, oneside]{book} % specifies the unique parent class, if any

%%================================================================
%% 引入各种第三方包
%%================================================================
% \RequirePackage{ifxetex, indentfirst, longtable, multicol, multirow, array} % 没用到的
% \RequirePackage[bottom]{footmisc} % stick footnote at bottom of page
% \RequirePackage{amsmath, amsfonts, amssymb, latexsym, marvosym, pifont}
\RequirePackage{tabu} % begin{tabu}
% layout
\RequirePackage[top = 3cm, bottom = 2.5cm, left = 3cm, right = 2.5cm,
    nomarginpar, headheight = 15pt, % to avoid "headheight too small"
    %showframe, showcrop,
]{geometry} % can be changed with \newgeometry
% fancyhdr
\RequirePackage{fancyhdr}
\fancypagestyle{plain}{ %
    \fancyhf{} % clear all header and footer fields
    \fancyfoot[C]{\fontsize{8}{8}\selectfont -- \thepage\ --}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancyhf{}
\fancyfoot[C]{\fontsize{8}{8}\selectfont -- \thepage\ --}
\fancyhead[C]{\slshape \leftmark}
% enumitem
\RequirePackage{enumitem} % \setlist
\setlist{nosep} % kills all vertical spacing
% graphicx
\RequirePackage[xetex]{graphicx} % before xltxtra, 加载图片要用这个, 以后要把这些功能单独分离出去, 搞一个适合自己的, 否则加载这么多太慢
\graphicspath{{/home/coder352/github/jImage/}{./img/}{../img/}{./}{../}} % mind the trailing "/"
% titlesec
\RequirePackage{titlesec} % \titleformat, \titlespacing
\titleformat{\chapter}{\centering\LARGE\bfseries}{\thechapter}{1em}{}
\titlespacing{\chapter}{0pt}{*0}{*4}
% biblatex, 好多注释删掉了
\RequirePackage[backend = biber, url = true, hyperref = true,
    doi = false, isbn = false, style = caspervector, utf8, sorting = centy]{biblatex}
\renewcommand*{\bibfont}{\small} % 11pt
\DeclareFieldFormat*{year}{#1}
\let\cite = \supercite
% caption
\RequirePackage{caption} % \captionsetup
\RequirePackage{subcaption}
\captionsetup{labelsep = quad}
% hyperref
\RequirePackage{hyperref}
\RequirePackage{xcolor}
\hypersetup{ %
  bookmarksnumbered, pdfpagelabels = true, plainpages = false, breaklinks = true,
  colorlinks = false,
  pdfborderstyle = {/S/U/W .3}, % border style will be underline of width .3pt
  linkbordercolor = red, % internal links
  citebordercolor = cyan, % links to bibliography
  filebordercolor = magenta, % file links
  urlbordercolor = blue, % external links
  % linkcolor = black, citecolor = black, urlcolor = blue
}
% before xunicode! % 这几行不能删, 否则无法正常显示汉字
\RequirePackage[tt = false]{libertine} % keyboard symbol
\RequirePackage{xltxtra} % fontspec, xunicode are loaded here.
\RequirePackage[CJKmath = true, AutoFakeSlant = true]{xeCJK} % slant header
% setspace
\RequirePackage[doublespacing]{setspace} % \singlespacing, \onehalfspacing, \doublespacing
\renewcommand{\doublespacing}{\setstretch{1.6}}
%%% Obsolete! setspace package is perfered to setting baselinestretch directly.
% \newcommand{\normalspace}
{\par\renewcommand{\baselinestretch}{1}\small\normalsize\par}
% \newcommand{\singlespace}
{\par\renewcommand{\baselinestretch}{1.2}\small\normalsize\par}
% \newcommand{\doublespace}% 30 lines per page
{\par\renewcommand{\baselinestretch}{1.6}\small\normalsize\par}

%%================================================================
%% 自定义设置
%%================================================================
% 设置字体, 需要的时候再取消注释
% \defaultfontfeatures{Mapping = tex-text}
% \setmainfont{Liberation Serif}
% \setsansfont{Liberation Sans}
% \setCJKmainfont[BoldFont = {Adobe Heiti Std}]{Adobe Song Std}
% \setCJKsansfont[BoldFont = {Adobe Heiti Std}]{Adobe Song Std}
% \setCJKmonofont{Noto Sans Mono CJK SC Regular}
% \setCJKfamilyfont{hei}{Adobe Heiti Std}
% \setCJKfamilyfont{song}{Adobe Song Std}
% \newCJKfontfamily\quotefont{Adobt Kaiti Std}
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
\newcommand{\Appendix}[1]{
  \renewcommand{\chaptermark}[1]{\markboth{附录\ \thechapter \ \ #1}{}}
  \titleformat{\chapter}{\centering\LARGE\bfseries}{附录\ \thechapter}{1em}{}
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

%%================================================================
% Variables to hold the text fields for the preliminary pages
%%================================================================
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

%%================================================================
%% 实现各种样式的 Page
%%================================================================
% \SWFCtitlepage 就可以在 .tex 文件中渲染出一个页面
\newcommand{\SWFCtitlepage}{ % Title page layout
  \thispagestyle{empty}
  \begin{center}
    \makebox[14.7em][s]{{\huge\SWFCField@Univ}}\\[5mm]
    \makebox[25.75em][s]{\Huge\textbf{\SWFCField@Docname}}\\[5mm]
    \makebox[12em][s]{\hspace{.5em}\LARGE(\SWFCField@Year\, 届)}\\[60pt]
    \begin{minipage}{.8\linewidth}
      \begin{Large}
        \extrarowsep = ^8mm
        \extrarowsep = _-7pt
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
\newcommand{\abstractpage}{ % Abstract page
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
\newcommand{\enabstractpage}{ % English abstract page
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
\newcommand{\makepreliminarypages}{ % preliminary pages
    \SWFCtitlepage % custom command
    \doublespacing % global line spacing
    \abstractpage % custom command
    \enabstractpage % custom command
    \acknowledgmentspage
    \advisorinfopage
}
\RequirePackage{minted} % minted has to be loaded at last!!!
\usemintedstyle{bw}
\renewcommand{\listingscaption}{程序} % used by minted
\renewcommand{\listoflistingscaption}{程序目录}
\setlength{\parindent}{2em}

%%================================================================
%% Initialize the variables to their default values
%%================================================================
\Title{人生--理想--学习--朋友--童年}
\Author{贾瑞鹏}
\Advisor{肖军弼}
\AdvisorTitle{副教授}
\AdvisorInfo{一个对我一生影响很大的老师}
\Month{四}
\Year{二〇一七}
\Univ{中国石油大学(华东)}
\School{计算机与通信工程学院}
\Subject{计算机科学与技术专业}
\Docname{贾先生的世界}
\Abstract{有时候回头, 看自己曾经的说的话, 发现我丢了对我来说最宝贵的东西...}
\Keywords{自我 利益 追求 民主 梦 国家 书生 名和利}
\Acknowledgments{感谢一路走来, 所有的人, 这一生很短暂, 我不想太盲目, 这个世界需要我}
% The followings are for the English Abstract.
\enTitle{The World of Mr.Jia}
\enAuthor{14thcoder}
\enUniv{China University of Petroleum}
\enSchool{Computer Science and Technology}
\enAbstract{I have some dreams when I was about twenty years old, and I want to achieve them!}
\enKeywords{Childhood Game Human-Nature Old-Man Flower}

\endinput % this must be the last command. [unnecessary]

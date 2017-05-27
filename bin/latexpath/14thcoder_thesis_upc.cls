%% ================================================================
%% 下面 5 行是通用的
%% ================================================================
% The 14thcoder_article class is for producing senior year theses and dissertations that meet the SWFU requirements.
\NeedsTeXFormat{LaTeX2e}[1999/12/01]
% specifies which version of TeX or LaTeX is required at least to run your package.
% The optional date may be used to specify the version more precisely.
\ProvidesClass{14thcoder_thesis_upc}[2017/03/30]  % 发布日期, 这里的名字必须和文件名相同, 真别扭
% it has to have the same name of the file without the extension.
% It tells LaTeX the name of the package and will allow it to issue a sensible error message when you try to include a package twice.
% The date is important since it can be used by other package to specify the minimum version requirement they need to use your package.
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}  % book 功能比较多
% it are end-user parameters. Each option is declared by one such command.
% pass unknown options to book
% \PassOptionsToClass and \PassOptionsToPackage are used to automatically invoke the corresponding options when the class or the package is loaded.
\ProcessOptions\relax  % terminates the option processing.
\LoadClass[a4paper, 12pt, oneside]{book} % specifies the unique parent class, if any

%% ================================================================
%% 引入各种第三方包, 这种模板中用 RequirePackage, 包中用 usepackage
%% ================================================================
% \RequirePackage{ifxetex, indentfirst, longtable, multicol, multirow, array}  % 没用到的
% \RequirePackage[bottom]{footmisc}  % stick footnote at bottom of page
% \RequirePackage{amsmath, amsfonts, amssymb, latexsym, marvosym, pifont}
\RequirePackage{tabu}  % begin{tabu}, 更厉害的表格
%% ================================================================
%% Geometry (layout)
%% ================================================================
\RequirePackage[top = 2cm, bottom = 1.5cm, left = 2cm, right = 1.5cm,
    nomarginpar, headheight = 15pt,  % to avoid "headheight too small"
    % showframe, showcrop,
]{geometry}  % can be changed with \newgeometry
%% ================================================================
%% Fancyhdr 页眉, 页脚, geometry 先设置了页眉, 页脚到页边的距离
%% ================================================================
\RequirePackage{fancyhdr}
\pagestyle{fancy} % Set default style for all content pages (not TOC, etc), \pagestyle 这个命令是 Latex 自带的, {fancy} 实现初步调用
\fancyhf{}  % 清空所有的页眉页脚, 然后开始设置
\fancyfoot[C]{\fontsize{8}{8}\selectfont -- \thepage\ --}
\fancyhead[C]{\slshape \leftmark}
\renewcommand{\headrulewidth}{.4pt}  % 页眉用 0.4pt 的分隔符
\pagenumbering{arabic}  % 页码编号用阿拉伯数字
\fancypagestyle{plain}{  % 针对空白页进行设置
    \fancyhf{}  % clear all header and footer fields
    \fancyfoot[C]{\fontsize{8}{8}\selectfont -- \thepage\ --}
    \renewcommand{\headrulewidth}{0pt}  % 顶部线宽为 0
    \renewcommand{\footrulewidth}{0pt}
}
%% ================================================================
%% enumitem
%% ================================================================
\RequirePackage{enumitem}  % \setlist
\setlist{nosep}  % kills all vertical spacing
%% ================================================================
%% graphicx
%% ================================================================
\RequirePackage[xetex]{graphicx} % before xltxtra, 加载图片要用这个, 以后要把这些功能单独分离出去, 搞一个适合自己的, 否则加载这么多太慢
\graphicspath{{/home/coder352/github/jImage/UPC/}{./img/}{../img/}{./}{../}}  % mind the trailing "/", 最后也要加 /, 好坑...
%% ================================================================
%% titlesec
%% ================================================================
\RequirePackage{titlesec}  % \titleformat, \titlespacing
\titleformat{\chapter}{\centering\LARGE\bfseries}{\thechapter}{1em}{}
\titlespacing{\chapter}{0pt}{*0}{*4}
%% ================================================================
%% biblatex, 好多注释删掉了
%% ================================================================
\RequirePackage[backend = biber, url = true, hyperref = true,
    doi = false, isbn = false, style = caspervector, utf8, sorting = centy]{biblatex}
\renewcommand*{\bibfont}{\small}  % 11pt
\DeclareFieldFormat*{year}{#1}
\let\cite = \supercite
%% ================================================================
%% caption, 标题
%% ================================================================
\RequirePackage{caption}  % \captionsetup
\RequirePackage{subcaption}
\captionsetup{labelsep = quad}
%% ================================================================
%% hyperref, xcolor
%% ================================================================
\RequirePackage{hyperref}
\RequirePackage{xcolor}
\hypersetup{  %
  bookmarksnumbered, pdfpagelabels = true, plainpages = false, breaklinks = true,
  colorlinks = false,
  pdfborderstyle = {/S/U/W .3},  % border style will be underline of width .3pt
  linkbordercolor = red,  % internal links
  citebordercolor = cyan,  % links to bibliography
  filebordercolor = magenta,  % file links
  urlbordercolor = blue,  % external links
  % linkcolor = black, citecolor = black, urlcolor = blue
}
%% ================================================================
%% libertine, xltxtra, xeCJK, setspace
%% ================================================================
% before xunicode! % 这几行不能删, 否则无法正常显示汉字
\RequirePackage[tt = false]{libertine}  % keyboard symbol
\RequirePackage{xltxtra}  % fontspec, xunicode are loaded here.
\RequirePackage[CJKmath = true, AutoFakeSlant = true]{xeCJK}  % slant header
% setspace
\RequirePackage[doublespacing]{setspace}  % \singlespacing, \onehalfspacing, \doublespacing
\renewcommand{\doublespacing}{\setstretch{1.6}}
%%% Obsolete! setspace package is perfered to setting baselinestretch directly.
% \newcommand{\normalspace}
{\par\renewcommand{\baselinestretch}{1}\small\normalsize\par}
% \newcommand{\singlespace}
{\par\renewcommand{\baselinestretch}{1.2}\small\normalsize\par}
% \newcommand{\doublespace}% 30 lines per page
{\par\renewcommand{\baselinestretch}{1.6}\small\normalsize\par}

%% ================================================================
%% 自定义设置
%% ================================================================
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
\urlstyle{rm}
\raggedbottom  % 针对 book 模板, 短行自动占据整行
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

%% ================================================================
%% Variables to hold the text fields for the preliminary pages
%% ================================================================
\usepackage{14thcoder_thesis_variables}

%% ================================================================
%% 实现各种样式的 Page
%% ================================================================
\usepackage{14thcoder_thesis_pages}

\RequirePackage{minted}  % minted has to be loaded at last!!!
\usemintedstyle{bw}
\renewcommand{\listingscaption}{程序}  % used by minted
\renewcommand{\listoflistingscaption}{程序目录}
\setlength{\parindent}{2em}

\endinput % this must be the last command. [unnecessary]

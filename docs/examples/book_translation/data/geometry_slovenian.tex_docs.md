# Documentation: geometry_slovenian.tex

## File Metadata
- **Path**: `examples/book_translation/data/geometry_slovenian.tex`
- **Type**: .tex file
- **Size**: 1,539,257 bytes (1503.18 KB)
- **Lines**: 32,858
- **Words**: 171,332
- **Characters**: 1,485,565

## Original Source

```
\documentclass[11pt]{book}

%PAPIR - US TRADE
\paperwidth 15.24cm
\paperheight 22.86cm

%TEKST
\textwidth 11.9cm \textheight 19.4cm
\oddsidemargin=-0.5cm
\evensidemargin=-1.2cm
\topmargin=-15mm

\headheight=13.86pt

%\usepackage[slovene]{babel}
\usepackage[english]{babel}

%\usepackage[cp1250]{inputenc}
\usepackage[utf8]{inputenc}


\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{color}
\usepackage{amsfonts}
\usepackage{makeidx}
\usepackage{calc}
\usepackage{gclc}
%\usepackage[dvips]{hyperref}
\usepackage{amssymb}
\usepackage[dvips]{graphicx}
\usepackage{fancyhdr}

%za slike
\usepackage{caption}
\DeclareCaptionFormat{empty}

\def\contentsname{Vsebina}

\makeindex

\newcommand{\ch}{\mathop {\mathrm{ch}}}
\newcommand{\sh}{\mathop {\mathrm{sh}}}
\newcommand{\tgh}{\mathop {\mathrm{th}}}
\newcommand{\tg}{\mathop {\mathrm{tg}}}
\newcommand{\ctg}{\mathop {\mathrm{ctg}}}
\newcommand{\arctg}{\mathop {\mathrm{arctg}}}
\newcommand{\arctgh}{\mathop {\mathrm{arcth}}}

\def\indexname{Indeks}

\definecolor{green1}{rgb}{0,0.5,0}
\definecolor{viol}{rgb}{0.5,0,0.5}
\definecolor{viol1}{rgb}{0.2,0,0.9}
\definecolor{viol3}{rgb}{0.3,0,0.6}
\definecolor{viol4}{rgb}{0.6,0,0.6}
\definecolor{grey}{rgb}{0.5,0.5,0.5}

 \def\qed{$\hfill\Box$}
\newcommand{\kdokaz}{\color{red}\qed\vspace*{2mm}\normalcolor}

\newcommand{\res}[1]{\color{green1}\textit{#1}\normalcolor}

\newtheorem{izrek}{Theorem}[section]
\newtheorem{lema}{Lemma}[section]
\newtheorem{definicija}{Definition}[section]
\newtheorem{aksiom}{Axiom}[section]
\newtheorem{zgled}{Exercise}[section]
\newtheorem{naloga}{Problem}
\newtheorem{trditev}{Proposition}[section]
\newtheorem{postulat}{Postulate}
\newtheorem{ekv}{E}


%BARVA

\newcommand{\pojem}[1]{\color{viol4}\textit{#1}\normalcolor}

%\newcommand{\pojemFN}[1]{\textit{#1}}

\newcommand{\blema}{\color{blue}\begin{lema}}
\newcommand{\elema}{\end{lema}\normalcolor}

\newcommand{\bizrek}{\color{blue}\begin{izrek}}
\newcommand{\eizrek}{\end{izrek}\normalcolor}

\newcommand{\bdefinicija}{\begin{definicija}}
\newcommand{\edefinicija}{\end{definicija}}

\newcommand{\baksiom}{\color{viol3}\begin{aksiom}}
\newcommand{\eaksiom}{\end{aksiom}\normalcolor}

\newcommand{\bzgled}{\color{green1}\begin{zgled}}
\newcommand{\ezgled}{\end{zgled}\normalcolor}

\newcommand{\bnaloga}{\color{red}\begin{naloga}}
\newcommand{\enaloga}{\end{naloga}\normalcolor}

\newcommand{\btrditev}{\color{blue}\begin{trditev}}
\newcommand{\etrditev}{\end{trditev}\normalcolor}


\newcommand{\del}[1]{\chapter{#1}}
\newcommand{\poglavje}[1]{\section{#1}}
%\newcommand{\naloge}[1]{\color{red}\section*{#1}\normalcolor}
\newcommand{\naloge}[1]{\section{#1}}
\newcommand{\ppoglavje}[1]{\subsection{#1}}

\setlength\arraycolsep{2pt}

\author{Milan Mitrovi\'c}
\title{\textsl{\Huge{\textbf{Euclidean Plane Geometry}}}}

\date{}

%_________________________________________________________________________________________

\begin{document}
\pagestyle{fancy}
\lhead[\thepage]{\textsl{\nouppercase{\rightmark}}}
\rhead[\textsl{\nouppercase{\leftmark}}]{\thepage}
\cfoot[]{}


 \vspace*{-12mm}

\hspace*{24mm} \textsl{\Huge{\textbf{Euclidean }}}\\

\hspace*{24mm} \textsl{\Huge{\textbf{Plane}}}\\

\hspace*{24mm} \textsl{\Huge{\textbf{Geometry}}}

 \vspace*{8mm}\hspace*{60mm}Milan Mitrovi\'c
% \normalcolor

 \vspace*{0mm}

\hspace*{-21mm}
\input{sl.NASL2A4.pic}

%\color{viol1}
 \hspace*{48mm}Sevnica

 \hspace*{49mm}
2013
% \normalcolor
  %slikaNova0-1-1
%\includegraphics[width=120mm]{slikaNaslov.pdf}

 \setcounter{section}{0}
 \thispagestyle{empty}
 \newpage


%\pagecolor{white}

%\color{viol1}
\vspace*{17mm}
 \hspace*{77mm} \textit{To Boris and Jasmina}
%\normalcolor
  %slikaNova0-1-1
%\includegraphics[width=120mm]{slikaNaslov.pdf}


 \thispagestyle{empty}
\newpage

%________________________________________________________________________

%PREDGOVOR
%{\hypertarget{Vsebina}\tableofcontents}
 %\printindex
\thispagestyle{empty}


%_______________________________________________________________________


\chapter*{Preface}

\thispagestyle{empty}


\thispagestyle{empty}

The present book is the result of the experience I gained as a professor in teaching geometry at the Mathematical Gymnasium in Belgrade for many years and preparing students in Slovenia for the International Mathematical Olympiad (IMO).

Formally, the substance is presented in such a way that it does not rely on prior knowledge of geometry. In the book, we will deal only with planar Euclidean geometry - all definitions and statements refer to the plane.

The first two chapters deal with the history and axiomatic design of geometry.
The consequences of the axioms of incidence,  congruence and parallelism are discussed in detail, while in the other two groups (axioms of order and continuity) the consequences are mostly not proven.
Chapters three and four deal with the relation of the congruence of figures, the use of the triangle congruence theorems, and a circle.
In the fifth chapter, a vectors are defined. Thales's theorem of proportion is proven.
Chapter six deals with isometries and their use. Their classification has been performed.
Chapters 7 and 8 deal with similarity transformations, figure similarity relation, and area of figures. The ninth chapter presents the inversion.
At the end of each chapter (except the introductory one) are exercises. Solutions and instructions can be found in the last, tenth chapter.


The book contains 341 theorems, 247 examples and 418 solved problems (28 of them from the IMO). In this sense, the book in front of you is at the same time a preparing guide for the IMO.

For some well-known theorems and problems, are given brief historical remarks. That can help high school and college students to better understand the development of geometry over the centuries.

A lot of help in writing the book was selflessly offered to me by Prof. Roman Drstvenšek, who read the manuscript in its entirety. With his professional and linguistic comments, he made a great contribution to the final version of the book.
In that work, he was assisted by Prof. Ana Kretič Mamič. I kindly thank both of them for the effort and time they have generously devoted to this book.

I would especially like to thank Prof. Kristjan Kocbek, who read the partial manuscript
 and with his critical remarks contributed to
 significant improvement of the book.

%I sincerely thank prof. Gordana Kenda Kozinc, who read and proofread the introductory chapter, and thanks also to prof. Alenka Brilej, who helped Roman with the language test with quite a few useful tips.

I also thank Prof. Dr Predrag Janiči\'c, who wrote the wonderful software package \textit {GCLC} for \ LaTeX {}. Almost all pictures in this book were made with this package.

Last but not least, I would like to thank the students of the Bežigrad Grammar School, the 1st Grammar School in Celje and the Brežice Grammar School for their inspiration and support. Students from these schools attended the renewed course of geometry which I have already taken before
years in Belgrade.

\thispagestyle{empty}

\vspace*{12mm} Sevnica, December 2013 \hfill Milan
Mitrovi\'c
%\newpage

%________________________________________________________________________

 \tableofcontents

 %\thispagestyle{empty}

%\newpage



% DEL 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
% O DEDUKTIVNI IN INDUKTIVNI METODI
%________________________________________________________________________________

 \del{Introduction} \label{pogUVOD}

%________________________________________________________________________________
\poglavje{Deductive and Inductive Method} \label{odd1DEDUKT}

Že v osnovni šoli spoznamo veliko geometrijskih pojmov, kot so:
trikotnik, krožnica, pravi kot itd. Kasneje se naučimo tudi
nekaj izrekov: izreki o skladnosti trikotnikov, Pitagorov in
Talesov izrek. V začetku izrekov ne dokazujemo, ampak dejstva
ugotavljamo na osnovi večih posameznih primerov. Ta način
sklepanja se imenuje induktivna metoda. Induktivna metoda (lat.
inductio -- uvajanje) je torej način sklepanja, pri katerem od
posameznih pridemo do splošnih zaključkov. Kasneje začnemo
posamezne izreke dokazovati. Skozi te dokaze se prvič srečamo s
t. i. deduktivnim načinom sklepanja oz. z dedukcijo. Dedukcija
(lat. deductio -- izvajanje) je način sklepanja, pri katerem se od
splošnih pride do posameznih zaključkov. Ideja pri tej
metodi torej je, da z dokazovanjem izpeljemo splošni zaključek in ga
potem uporabljamo v posameznih primerih. Ker pri induktivni
metodi ne moremo preveriti vseh primerov, saj je njihovo število
najpogosteje neskončno, lahko s to metodo  pridemo tudi do
napačnih zaključkov. Z deduktivno metodo dobimo vedno pravilne
zaključke, če so le predpostavke, ki jih v dokazu uporabljamo,
pravilne. Na naslednjem primeru analizirajmo obe omenjeni metodi.
Poskusimo priti do ugotovitve:
 \btrditev \label{TalesUvod}
 The diameter of a circle subtends a right angle to any point on the circle.
 \etrditev


\begin{figure}[!htb]
\centering
\input{sl.1.2.1.6.pic}
\caption{} \label{sl.sl.1.2.1.6.pic}
\end{figure}

  %slikaNova0-1-1
%\includegraphics[width=50mm]{slikaNova0-1-1.pdf}

Če bi uporabljali induktivno metodo, bi preverjali, ali ta trditev
velja v nekih posameznih primerih; npr.  v primeru, ko je  vrh
kota središče polkrožnice in podobno (Figure
\ref{sl.sl.1.2.1.6.pic}). Če bi le iz teh posameznih
primerov izpeljali splošno ugotovitev, seveda ne bi mogli biti
prepričani, da v katerem od primerov, ki ga nismo preverili, ta
trditev ne drži.

Uporabimo sedaj deduktivno metodo. Naj bo $AB$ polmer krožnice s
središčem $O$ in $L$ poljubna točka te krožnice, različna od
točk $A$ in $B$ (Figure \ref{sl.sl.1.2.1.6.pic}). Dokažimo, da je
kot $ALB$ pravi kot. Ker je
 $OA\cong OB\cong OL$, sledi,
da sta trikotnika $AOL$ in $BOL$ enakokraka, zato je
 $\angle ALO\cong\angle LAO=\alpha$ in $\angle BLO\cong\angle LBO=\beta$.
Tedaj je $\angle ALB=\alpha+\beta$.
 Vsota notranjih kotov v
trikotniku $ALB$ je enaka $180^0$,  torej je
$2\alpha+2\beta=180^0$. Iz tega sledi:
 $$\angle ALB=\alpha+\beta=90^0$$

Opazimo, da v primeru uporabe deduktivne metode oz. pri dokazovanju
trditve nismo obravnavali neke določene točke $L$ na krožnici,
ampak poljubno točko (v splošni legi). To pomeni, da trditev
velja za vsako točko krožnice (razen $A$ in $B$), če je seveda
dokaz pravilen. Toda ali je dokaz pravilen? V tem dokazu smo
uporabljali naslednji dve trditvi:
 \btrditev
 If two sides in a triangle are congruent, then the angles opposite the congruent sides are congruent angles.
 \etrditev
 \btrditev
  The sum of the interior angles of a triangle is equal to $180^0$.
   \etrditev
Uporabili smo tudi pojme, kot so: enakokraki trikotnik, skladnost
kotov; v sami trditvi pa tudi pojme: premer, krožnica, kot nad
premerom in pravi kot. Da smo prepričani, ali je trditev, ki
smo jo dokazovali, točna, moramo biti gotovi, da sta tudi trditvi,
ki smo ju uporabili v dokazu, točni. V našem primeru
predpostavljamo, da smo  omenjeni dve trditvi že dokazali in da
smo vpeljali vse omenjene pojme. Jasno je, da se ta problem pojavi
pri vsaki trditvi -- tudi pri dveh, na kateri smo se sklicevali v
dokazu. To  zahteva določeno sistematizacijo cele geometrije.
Zastavlja se vprašanje, kako začeti, če se v dokazu vsake
trditve zopet sklicujemo na prej dokazane. Ta proces bi se potem
lahko nadaljeval v neskončnost. Tako pridemo do potrebe po
začetnih trditvah -- \index{aksiomi} \pojem{aksiomih}. Isto velja
za pojme -- potrebujemo t. i. \pojem{začetne pojme}.\index{začetni
pojmi} Na ta način je vsaka geometrija (lahko jih je torej več),
ki jo obravnavamo, odvisna od izbire začetnih pojmov in aksiomov.
Ta pristop izgrajevanja neke geometrije imenujemo
\pojem{sintetični postopek}, sami geometriji pa pravimo, da je
\pojem{sintetična geometrija}\index{geometrija!sinteti\v{c}na}.


%________________________________________________________________________________
\poglavje{Basic Terms and Basic Theorems} \label{odd1POJMI}

V neki teoriji  (kot je geometrija) vsako vpeljavo novega
pojma naredimo z \index{definicija} \pojem{definicijo}, s katero ta pojem
opišemo s pomočjo
 nekih začetnih ali že definiranih pojmov.
 Povezave med pojmi in tudi njihove ustrezne lastnosti so dane z izjavami,
  ki jih imenujemo
\pojem{trditve teorije}. Kot smo že omenili, začetne trditve
imenujemo \index{aksiomi} \pojem{aksiomi}, trditve, ki so
iz njih izpeljane, pa  \pojem{izreki} te teorije. Formalno je
\pojem{dokaz} \index{dokaz izreka} nekega izreka $\tau$ zaporedje
trditev, ki logično sledijo ena iz druge, od katerih je vsaka
ali aksiom ali iz aksiomov izpeljana trditev (izrek), zadnja v tem
zaporedju pa je ravno trditev $\tau$.

 Čeprav izbira aksiomov ni enolično določena, ta ne more biti poljubna.
 Pri tej izbiri je
treba paziti, da aksiomi ne pripeljejo do protislovnih trditev
oziroma da ne pride do protislovja. To pomeni, da pri neki izbiri
aksiomov ne obstaja takšna trditev, da sta ta trditev in hkrati njena
negacija izreka v tej teoriji. Potrebno je imeti tudi dovolj
aksiomov, da bi za vsako trditev, ki jo lahko formuliramo v tej
teoriji, lahko ugotovili, ali velja ali ne. To pomeni, da je
bodisi trditev bodisi njena negacija izrek v tej teoriji. Za
sistem aksiomov, ki izpolnjuje prvo zahtevo, pravimo, da je
\index{sistem aksiomov!neprotisloven} \pojem{neprotisloven}, za
tistega, ki izpolnjuje drugo zahtevo, pa pravimo, da je \index{sistem
aksiomov!popoln} \pojem{popoln}. Pri izbiri aksiomov obstaja tudi
tretja zahteva -- da je sistem aksiomov \index{sistem
aksiomov!minimalen} \pojem{minimalen}, kar pomeni, da se noben od
aksiomov ne da izpeljati iz ostalih. Omenimo, da zadnja
 zahteva ni  tako pomembna, kot sta prvi dve.

Dodati moramo še, da evklidske geometrije ne gradimo
neodvisno od algebre in logike. Uporabljali bomo namreč pojme, kot
so npr. množica, funkcija, relacija z lastnostmi, ki za njih
veljajo. Uporabljali bomo tudi t. i. pravila sklepanja, kot je
npr. metoda protislovja. Za matematične discipline, ki jih na ta
način uporabljamo pri gradnji geometrije, pravimo, da so
\pojem{predpostavljene teorije}.



%________________________________________________________________________________
\poglavje{A Brief Historical Overview of the Development of Geometry}
\label{odd1ZGOD}

Z geometrijo so se ljudje začeli ukvarjati  že v rani zgodovini.
 V začetku je bilo to le opazovanje karakterističnih oblik, kot sta
 krožnica ali kvadrat. Po risbah, ki so bile odkrite na stenah starih jam, sklepamo,
 da so se ljudje že v prazgodovini  zanimali za simetrijo likov.

V nadaljnjem razvoju je človek ugotavljal razne lastnosti
geometrijskih likov. To je bilo zaradi praktičnih potreb, npr.
merjenja površine zemljišč -- tako je tudi nastala beseda
‘‘geometrija’’. V tem obdobju se je geometrija razvijala kot
induktivna znanost. To pomeni, da so do geometrijskih trditev
prihajali z izkušnjami -- s pomočjo meritev in s preverjanjem na
posameznih primerih. V tem smislu je bila geometrija razvita pri
vseh starih civilizacijah: kitajski, indijski in še posebej
egipčanski.

V Egiptu se je geometrija razvijala predvsem kot učenje o
meritvah. Ker je reka Nil večkrat poplavila, je
bilo potrebno zemljišča zelo pogosto znova premeriti. Razen tega so
znanje geometrije uporabljali tudi v gradbeništvu. Poznali so
npr. formulo za izračunavanje prostornine piramide in prisekane
piramide, čeprav so do nje prišli empirično. Tako je bila geometrija za
Egipčane predvsem pragmatična disciplina.
Najstarejši zapisi o tem segajo približno v leto 1700 pr. n. š.

Tudi v Mezopotamiji so imeli razvito geometrijo merjenja
ploščin. Geometrija trirazsežnega prostora ni bila
toliko obravnavana kot pri Egipčanih.

O kitajski geometriji ni toliko podatkov kot o egipčanski,
čeprav vemo, da je bila tudi ta  zelo razvita. V
najstarejših ohranjenih zapisih najdemo opis računanja
prostornin prizme, piramide, valja, stožca, prisekane piramide in
prisekanega stožca.

Indijska geometrija je precej mlajša od prejšnjih treh. Datira
približno v peto stoletje pr. n. š. V njej že vidimo prve
poskuse dokazovanja. Kasneje se je razvijala vzporedno s
starogrško geometrijo.

Preobrat v razvoju geometrije se je zgodil v Stari Grčiji. Tedaj
se je prvič v zgodovini pričela v geometriji uporabljati deduktivna metoda.
Prvi geometrijski dokazi so povezani s
Talesom\footnote{Starogrški filozof in matematik \textit{Tales}
\index{Tales} iz Mileta (640--546 pr. n. š.).}. Z njegovim imenom
povezujemo znani izrek o sorazmerju odsekov pri vzporednicah.
Dokazal je tudi izrek, da so koti nad premerom krožnice pravi,
čeprav je bila ta trditev brez dokaza znana že Babiloncem 1000 let
pred tem. Ta način razvoja geometrije so nadaljevali tudi drugi
starogrški filozofi, od katerih je bil Pitagora\footnote{Starogrški
filozof in matematik \textit{Pitagora} \index{Pitagora} z otoka
Samosa (ok. 580--490 pr. n. š.).} eden najpomembnejših.
Znamenit je seveda njegov  \index{izrek!Pitagorov}\pojem{Pitagorov
izrek}. Toda ta izrek so kot dejstvo poznali že Egipčani 3000 let
pr. n. š. (mogoče je bil izrek znan celo pred tem), pač pa je
Pitagora podal prvi znani dokaz. Arhimed\footnote{Starogrški filozof
in matematik \textit{Arhimed} \index{Arhimed} iz Sirakuze (287--212 pr. n. š.).}
je prvi predstavil teoretičen izračun števila $\pi$, tako da
je obravnaval v krožnico včrtane in očrtane večkotnike s $96$
stranicami. Dokazani so bili tudi izreki o skladnosti trikotnikov.
Ob hitrem napredku geometrije, ki se je odražal v velikem številu
dokazanih izrekov, se je pokazala potreba po sistematizaciji in s
tem po vpeljavi aksiomov. Potrebo po aksiomah sta prva opisala
Platon\footnote{Starogrški filozof in matematik \textit{Platon}
\index{Platon} (427--347 pr. n. š.).} in
Aristotel\footnote{Starogrški filozof in matematik
\textit{Aristotel} \index{Aristotel} iz Aten (384--322 pr. n. š.).}.
 Platon je v matematiki znan tudi po tem, da je raziskoval pravilne poliedre:
 tetraeder, kocko, oktaeder, dodekaeder in ikozaeder, zato jih po njem
 imenujemo tudi platonska telesa.

Enega  prvih poskusov aksiomatične zasnove geometrije -- in iz tega
časa edinega ohranjenega -- je dal najznamenitejši geometer tega časa,
Platonov učenec Evklid\footnote{Starogrški filozof in matematik
\textit{Evklid} \index{Evklid} iz Aleksandrije (ok. 330--270 pr. n. š.).}, v svojem znanem delu \textit{Elementi}, ki je sestavljeno iz
13 knjig. V njem je sistematiziral vse dotedanje znanje
geometrije. Začetne trditve je razdelil na aksiome in t. i.
postulate, od katerih so slednji čisto geometrične vsebine (danes
tudi njih imenujemo aksiomi). \textit{Elementi} so postali ena od
najpomembnejših in najvplivnejših knjig v zgodovini matematike.
Geometrija, ki jo je na ta način razvil, z manjšimi nepomembnimi
spremembami, je tista, ki se v šolah uči še danes. Dokazi, kot je
npr. ta o središčnem in obodnem kotu, so se obdržali v praktično
nespremenjeni obliki. Navedimo postulate, kot jih je podal Evklid
(Figure \ref{sl.sl.1.3.1.9.pic}):
\color{viol3}
\begin{postulat}
  We can draw a straight line from any point to any point.
 \end{postulat}
 \begin{postulat}
We can produce a finite straight line continuously in a straight line.
 \end{postulat}
 \begin{postulat}
We can describe a circle with any center and distance.
 \end{postulat}
  \begin{postulat}
All right angles are equal to one another.
 \end{postulat}
 \begin{postulat}
If a straight line falling on two straight lines makes the interior angles on the same side less than two right angles, the straight lines, if produced indefinitely, will meet on that side on which the angles are less that two right angles.
 \end{postulat}
\normalcolor

\begin{figure}[!htb]
\centering
\input{sl.1.3.1.9.pic}
\caption{} \label{sl.sl.1.3.1.9.pic}
\end{figure}

  %slikaNova1-3-3
%\includegraphics[width=100mm]{slikaNova1-3-3.pdf}


Vendar sistem aksiomov, ki jih je podal Evklid, ni bil popoln. V
nekaterih dokazih je določene dele sprejel kot očitne in jih ni
dokazoval. Seveda ne smemo biti preveč kritični, saj je bilo to delo za tiste
čase revolucionarno. \textit{Elementi} so bili stoletja
zgled in inspiracija matematikom in so začrtali nadaljnji razvoj
geometrije vse do danes. Za nadaljnji razvoj geometrije je bil posebej
pomemben zadnji aksiom, t. i. \index{aksiom!peti Evklidov}
\pojem{peti Evklidov aksiom}. Problem njegove neodvisnosti od
ostalih aksiomov je bil odprt naslednjih 2000 let!

Zadnji v nizu velikih starogrških matematikov so bili
Apolonij\footnote{Starogrški matematik \textit{Apolonij}
\index{Apolonij} iz Perge (262--190 pr. n. š.).},
Menelaj\footnote{Starogrški matematik \textit{Menelaj}
\index{Menelaj} iz Aleksandrije
  (ok. 70--130).} in Pappus\footnote{Starogrški matematik \textit{Pappus}
  \index{Pappus}
  iz
  Aleksandrije (ok. 290--350).}. Apolonij je v svoji knjigi \textit{Razprava
  o presekih stožca} definiral elipso, parabolo in hiperbolo kot
  preseke ravnine in krožnega (neskončnega) stožca. Tako je lahko določene
  njihove
  lastnosti  obravnaval hkrati, kar je bil za tisti čas precej
  sodoben pristop. Menelaj in Pappus sta dokazala določene izreke,
  ki so postali aktualni šele v 19.~stoletju z razvojem  projektivne geometrije.
  Torej so bile ideje teh treh matematikov zelo sodobne in na nek način
  lahko rečemo, da so bili na pragu odkritja prve neevklidske geometrije.

Po dokončnem padcu Stare Grčije pod Rimsko cesarstvo se je
obdobje slavne starogrške geometrije končalo. Čeprav so Stari Rimljani
prevzeli velik del starogrške kulture in so gradili ceste,
vodovode in tako dalje,  je zanimivo, da se nikoli niso preveč zanimali za
starogrško teoretično matematiko. Tako je njihov prispevek k razvoju
geometrije zelo skromen.

Pomembno vlogo v nadaljnjem razvoju geometrije so prevzeli Arabci.
Najprej je treba povedati, da so nam vsa dela Starih Grkov
vključno z Evklidovimi \textit{Elementi} danes znana zato, ker so jih
takrat prevedli in tako ohranili ravno Arabci. Od ustanovitve
Bagdada leta 762 so v naslednjih 100-tih letih prevedli večino del
starogrške in indijske matematike. Naredili so tudi sintezo
starogrškega pretežno geometričnega in indijskega pretežno
algebričnega pristopa. Omenimo, da je sama beseda \pojem{algebra}
arabskega izvora. Poleg tega so Arabci nadaljevali razvoj
\pojem{trigonometrije}, ki so jo zasnovali že Stari Grki. A. R. al-Biruni\footnote{Arabski matematik \textit{ A. R. al-Biruni} \index{al-Biruni, A. R.} (973--1048).} je dokazal danes znani \pojem{sinusni izrek}.

V Evropi se je razvoj geometrije začel v 12. stoletju, ko so preko
Španije in Sicilije znanja prinašali arabski in judovski matematiki.
(Evklidovi \textit{Elementi} so bili prevedeni iz arabskega jezika
približno leta 1200); toda pravi razcvet je Evropa doživela šele v
16. stoletju. V srednjeveškem obdobju se je namreč matematika zelo
počasi razvijala. V srednjem veku so se zahodnoevropski matematiki
šele učili starogrško geometrično dediščino iz arabskih prevodov,
vendar ta proces ni bil hiter. Ko se je to znanje akumuliralo in so
se družbeno-politični pogoji spremenili, se je v
razvoju geometrije začelo novo obdobje. Prve nove rezultate so dali italijanski
matematiki tistega časa, ki so veliko pozornosti posvetili
konstrukcijam s pomočjo ravnila in šestila.

Kot smo že prej omenili, je imel peti Evklidov aksiom zelo velik vpliv na
nadaljnji razvoj geometrije. Zaradi svoje
formulacije, ki ni tako enostavna kot pri prejšnjih aksiomih, in
tudi zaradi pomena je veliko matematikov v tistem obdobju menilo,
da ga ni potrebno obravnavati kot aksiom, ampak se ga lahko z ostalimi aksiomi dokaže kot
izrek. Če preberemo druge Evklidove začetne trditve, zares drži, da je
peti aksiom bolj zapleten.
 Problem neodvisnosti petega aksioma od ostalih je v naslednjih stoletjih okupiral mnoge
 matematike. Vse do druge polovice 19.
 stoletja problem ni bil rešen. V mnogih poskusih dokazovanja petega
 aksioma iz preostalih so bile uporabljene trditve, katerih dokaz
 je bil izpuščen.
Kasneje se je pokazalo, da se teh trditev niti ne da dokazati iz
ostalih aksiomov, če se iz njihovega seznama izpusti peti aksiom.
Podobno kot iz njih sledi peti aksiom, tudi te trditve
sledijo iz petega aksioma (seveda z uporabo ostalih aksiomov).
Zato jih imenujemo \pojem{ekvivalenti petega Evklidovega aksioma}.
Navedimo nekaj primerov teh ekvivalentov (Figure
\ref{sl.sl.1.3.1.9a.pic}):

\color{blue}
\begin{ekv}
If $ ABCD $ is a quadrilateral with two right angles on the side $BC$
and the sides $AB$ and $CD$ are congurent, then the two remain angles
of this quadrilateral are also right angles.\footnote{Ta ekvivalent je postavil
italijanski matematik \index{Saccheri, G. G.} \textit{G. G.
Saccheri} (1667--1733).}
\end{ekv}
\begin{ekv}
A line perpendicular to one arm of an acute angle intersects
his other arm.
\end{ekv}
\begin{ekv}
Every triangle can be circumscribed.
\end{ekv}
\begin{ekv}
If three angles of a quadrilateral are right angles, then the fourth angle is also a right angle.\footnote{\index{Lambert, J. H.}\textit{J.
H. Lambert} (1728--1777), francoski matematik.}
\end{ekv}
\begin{ekv}
The sum of the interior angles in every triangle is $180^0$.\footnote{\index{Legendre, A. M.} \textit{A. M. Legendre}
(1752--1833), francoski matematik.}
\end{ekv}
\begin{ekv}
For any given line $p$ and point $A$ not on $p$, in the plane containing both line $p$ and point $A$ there is just one line
 through point $A$ that do not intersect line $p$\footnote{\index{Playfair, J.} \textit{J. Playfair}
(1748--1819), škotski matematik.}.
 \end{ekv}
\normalcolor


\begin{figure}[!htb]
\centering
\input{sl.1.3.1.9a.pic}
\caption{} \label{sl.sl.1.3.1.9a.pic}
\end{figure}

Matematikom je torej uspelo dokazati peti Evklidov aksiom s
pomočjo vsake od teh trditev, toda sčasoma se je pokazalo, da se
 nobene od njih brez petega aksioma sploh ne da dokazati. Zato
so te trditve, kot smo že omenili, petemu aksiomu ekvivalentne.
Danes se najpogosteje uporablja Playfairjev ekvivalent, ki je bil kasneje
namesto petega aksioma dodan k Evklidovim aksiomom.

Toda kako so matematiki ugotovili, da se peti Evklidov aksiom ne
more izpeljati iz ostalih aksiomov? Samo dejstvo, da ga niso
uspeli dokazati, še ni pomenilo, da to ni mogoče. Odgovor na to
vprašanje je prišel konec 19. stoletja in je, kot bomo videli,
za razvoj geometrije prinesel veliko več kot samo dejstvo o
nedokazljivosti petega aksioma.

Naslednja prelomnica v razvoju geometrije je bilo odkritje
\index{geometrija!neevklidska}\pojem{neevklidskih geometrij} v 19. stoletju. Za začetnika tega razvoja
štejemo N.~I.~Lobačevskega\footnote{\index{Lobačevski, N.
I.}\textit{N. I. Lobačevski} (1792--1856), ruski matematik.}. Tudi on
je obravnaval problem neodvisnosti petega Evklidovega aksioma.
Izhajajoč iz njegove negacije oz. iz negacije Playfairjeve
ekvivalentne trditve je Lobačevski postavil predpostavko, da skozi
točko, ki ne leži na neki premici, obstajata vsaj dve premici, ki se s
to premico ne sekata, in sta komplanarni. V želji, da bi prišel do
protislovja (tako bi bil peti aksiom dokazan), je zgradil celo
zaporedje novih trditev. Ena med njimi je na primer ta, da je vsota notranjih kotov
trikotnika vedno manjša od iztegnjenega kota. Toda nobena teh trditev
ni bila v protislovju z ostalimi aksiomi, če seveda s seznama izključimo
peti Evklidov aksiom. Iz tega je dobil idejo, da je mogoče zgraditi
popolnoma novo geometrijo, ki je neprotislovna in temelji na vseh
Evklidovih aksiomih z izjemo petega, ki ga zamenjamo z njegovo
negacijo. Danes to geometrijo imenujemo
\index{geometrija!hiperbolična} \pojem{hiperbolična geometrija}
ali \pojem{geometrija Lobačevskega}.

Neodvisno od Lobačevskega je do istih rezultatov prišel tudi J.
Bolyai\footnote{\index{Bolyai, J.} \textit{J. Bolyai} (1802--1860),
madžarski matematik.}. Kot se to pogosto dogaja, ideje Lobačevskega v času njegovega življenja žal
niso bile sprejete. Popolno potrditev teh idej
oziroma dokaz neprotislovja te nove geometrije je konec 19. stoletja, tj. šele po smrti Lobačevskega, predstavil A.
Poincar\'{e}\footnote{\index{Poincar\'{e}, J. H.} \textit{J. H.
Poincar\'{e}} (1854--1912), francoski matematik.}.
Poincar\'{e} je zgradil model, na
osnovi katerega je pokazal, da bi morebitno protislovje geometrije
Lobačevskega pomenilo hkrati protislovje Evklidove geometrije.
Kasneje je prišlo do odkritja tudi drugih neevklidskih geometrij.

Čeprav je bil konec 19. in
v začetku 20. stoletja sistem aksiomov Evklidove geometrije že skoraj popolnoma zgrajen, je prvi
pravilen popolni sistem dal D. Hilbert\footnote{\index{Hilbert, D.}
\textit{D. Hilbert} (1862--1943), nemški matematik.} v svoji znani
knjigi \textit{Osnove geometrije}, objavljeni leta 1899. Zelo podoben
sistem aksiomov uporabljamo v skoraj nespremenjeni
obliki tudi danes.

Vzporedno z raziskovanjem problema petega Evklidovega aksioma in
razvojem neevklidskih geometrij so se v obravnavi geometrije razvile
tudi druge pomembne
metode. Že okoli leta 1637 je R.
Descartes\footnote{\index{Descartes, R.} \textit{R. Descartes}
(1596--1650) francoski matematik.} v svoji knjigi
\textit{Geometrija} pokazal, da lahko vsako točko v ravnini opišemo z
ustreznim parom dveh realnih števil in podobno v prostoru kot
trojico treh realnih števil. To je povezal s pojmom koordinatne
predstavitve odvisnosti ene količine (funkcije) od druge
(spremenljivke), ki je bil znan že prej. Danes takšen
način določanja točk v prostoru po njem imenujemo \pojem{kartezični
koordinatni sistem}. Premice in ravnine potem lahko opisujemo kot
množice rešitev ustreznih linearnih enačb, kjer so neznanke
koordinate točk.

Tako sta se pod vplivom idej F.
Vi\'{e}teja\footnote{\index{Vi\'{e}te, F.} \textit{F. Vi\'{e}te}
(1540--1603), francoski matematik.}, Descartesa in P.
Fermata\footnote{\index{Fermat, P.} \textit{P. Fermat} (1601--1665),
francoski matematik.} začeli razvijati dve zelo pomembni matematični
disciplini - najprej \index{geometrija!analitična}
\pojem{analitična geometrija}, nato še \index{linearna algebra}
\pojem{linearna algebra}, ki predstavljata povezavo med algebro in
geometrijo. Nadaljnji razvoj teh dveh disciplin je omogočal razvoj
\index{geometrija!večdimenzionalna} \pojem{večdimenzionalne
geometrije}, v kateri se lahko obravnavajo prostori, dimenzije, večje
od tri, saj v algebri ni takšnih omejitev, kot jih imamo v
geometrični percepciji prostora. Tako lahko definiramo t. i.
\pojem{politope} -- objekte večdimenzionalnega prostora, ki so analogija
dvodimenzionalnih večkotnikov in tridimenzionalnih poliedrov.

Kasneje je prišlo tudi do odkritja drugih neevklidskih geometrij.
V 19. stoletju se je razvila še t. i. \index{geometrija!projektivna}\pojem{projektivna geometrija}, vendar
njen razvoj ni potekal aksiomatično kot pri hiperbolični
geometriji, ustrezen sistem aksiomov je bil postavljen šele
kasneje. V tej geometriji v ravnini ni premic, ki se ne sekata.

Eden od prvih motivov za začetek razvoja
 projektivne geometrije izvira iz slikarstva oziroma iz želje, da se
 občutek trirazsežnega prostora prenese v ravnino. Že v zelo
 zgodnjem slikarstvu srečamo zelo pomembno lastnost -- da sta
 vzporednici na sliki predstavljeni kot premici, ki se sekata.

 V 15. stoletju so se italijanski umetniki zelo zanimali za
 geometrijo prostora. Teorijo perspektive je prvi obravnaval F.
 Brunellechi\footnote{\index{Brunellechi, F.} \textit{F.
 Brunellechi} (1377--1446), italijanski arhitekt.} leta 1425.
   Njegovo delo sta
nadaljevala L. B. Alberti\footnote{\index{Alberti, L. B.}
  \textit{L. B.
 Alberti} (1404--1472), italijanski matematik in slikar.} in A.
 D\"{u}rer\footnote{\index{D\"{u}rer, A.} \textit{A.
 D\"{u}rer} (1471--1528), nemški slikar.}. Albertijeva knjiga iz
 leta
 1435 predstavlja prvo predstavitev središčne projekcije.

 Za začetek razvoja projektivne geometrije kot matematične
 discipline smatramo obdobje, ko sta
 J. Kepler\footnote{\index{Kepler, J.} \textit{J. Kepler} (1571--1630),
  nemški astronom.}  in G. Desargues\footnote{\index{Desargues, G.}
  \textit{G. Desargues}
 (1591--1661), francoski arhitekt.}
 neodvisno drug od drugega
  vpeljala pojem točk v neskončnosti.
  Kepler je pokazal, da ima parabola dve gorišči, od katerih je eno
   točka v neskončnosti. Desargues
 je leta 1639 pisal: ‘‘Dve vzporednici imata skupni konec na
 neizmerni oddaljenosti.’’ Leta 1636 je napisal knjigo o perspektivi,
 in leta 1639 še o stožnicah. Znameniti \textit{Desarguesov izrek}
 je objavil  leta 1648.

  Z nadaljnjim razvojem projektivne geometrije povezujemo francoske matematike.
  Genialni B. Pascal\footnote{\index{Pascal, B.} \textit{B. Pascal} (1623--1662),
  francoski filozof in matematik.} je
  že kot šestnajstletnik dokazal pomemben izrek o
  stožnicah, ki ga danes po njem imenujemo \textit{Pascalov izrek}.
  Ta izrek, ki je eden izmed osnovnih izrekov
  projektivne geometrije, je bil objavljen leta 1640.
  G. Monge\footnote{\index{Monge, G.} \textit{G. Monge}
  (1746--1818), francoski matematik.}
  je bil med prvimi matematiki, ki ga lahko smatramo za specialista; je
  namreč prvi pravi geometer. \pojem{Opisno geometrijo}je razvil kot
  posebno disciplino. V njegovem raziskovanju v opisni geometriji
  najdemo veliko idej projektivne geometrije.
  Najbolj originalen Mongeov učenec je
  bil J. V. Poncelet\footnote{\index{Poncelet, J. V.}
  \textit{J. V. Poncelet} (1788--1867), francoski matematik.}.
  Čeprav je že Pappus\footnote{\index{Pappus} \textit{Pappus iz Aleksandrije} (3. stol.), starogrški matematik.}
  odkril prve projektivne izreke, jih je Poncelet
  s popolnoma  projektivnim načinom sklepanja dokazal šele v 19. stoletju.
  Leta 1822 je
  Poncelet objavil svoj znani ‘‘Traktat o projektivnih lastnostih likov’’,
  v katerem se pojavljajo vsi pomembni pojmi, karakteristični za
  projektivno
  geometrijo: harmonična četverica, perspektivnost, projektivnost,
  involucija itd. Poncelet je vpeljal premico v neskončnosti za vse
  ravnine, ki so vzporedne dani ravnini. Poncelet in J. D.
  Gergonne\footnote{\index{Gergonne, J. D.} \textit{J. D. Gergonne} (1771--1859), francoski matematik.} sta
  neodvisno
  drug od drugega proučevala dualnost v projektivni geometriji,
  C.~J.~Brianchon\footnote{\index{Brianchon, C. J.} \textit{C. J. Brianchon}
   (1783--1864), francoski matematik.} pa
 je dokazal izrek, ki je dualen Pascalovem izreku.
 M.~Chasles\footnote{\index{Chasles, M.} \textit{M. Chasles} (1793--1880), francoski matematik.} je bil zadnji iz
  velike šole
 francoskih projektivnih  geometrov tistega časa.

 Tipičen predstavnik t. i. čiste geometrije
 (danes bi rekli sintetične geometrije) je bil
 J. Steiner\footnote{\index{Steiner, J.} \textit{J. Steiner}
 (1796--1863),
 švicarski geometer.}.
 Steiner je razvijal projektivno geometrijo zelo sistematično,
  od perspektivnosti do projektivnosti in potem do stožnic.

 Sredi 19. stoletja so primat v razvoju projektivne geometrije
 prevzeli nemški matematiki.  Negovali so sintetični pristop
 h geometriji. Vsi matematiki do tedaj so projektivno geometrijo
  zasnovali na evklidski metrični geometriji -- z dodajanjem
  točk v neskončnosti. Toda C.~G.~C.~Staudt
  \footnote{\index{Staudt, K. G. C.} \textit{C. G. C. Staudt} (1798--1867),
  nemški matematik.}
   je bil prvi, ki jo je poskusil osamosvojiti ter
    zasnovati samo na incidenčnih aksiomih, brez pomoči metrike.
    Tako je prišlo do ukinitve razlike med točkami v neskončnosti in navadnimi
     točkami
    oziroma prehoda z razširjenega evklidskega na projektivni prostor.

  F. Klein\footnote{\index{Klein, F. C.} \textit{F. C. Klein} (1849--1925), nemški matematik.} je leta 1871
   projektivni geometriji postavil algebraične temelje s pomočjo
    t. i. \pojem{homogenih koordinat}, ki sta jih leta 1827 neodvisno drug od drugega,
     odkrila K. W. Feuerbach\footnote{\index{Feuerbach, K. W.} \textit{K. W. Feuerbach}
      (1800--1834), nemški matematik.}
      in A. F. M\"{o}bius\footnote{\index{M\"{o}bius, A. F.} \textit{A. F. M\"{o}bius}
       (1790--1868), nemški matematik.}.
     A. Cayley\footnote{\index{Cayley, A.} \textit{A. Cayley} (1821--1895), angleški matematik.} in
     Klein
     najdeta uporabo projektivne geometrije v drugih neevklidskih geometrijah.
     Odkrila sta model hiperbolične geometrije in modele drugih geometrij
     v projektivni.

   Prva, ki sta popolnoma aksiomatično zasnovala projektivno geometrijo, sta
    bila G. Fano\footnote{\index{Fano, G.} \textit{G. Fano} (1871--1952), italijanski matematik.}
     leta 1892 in M. Pieri\footnote{\index{Pieri, M.} \textit{M. Pieri} (1860--1913), italijanski matematik.}
      leta 1899.

Zaradi svoje relativne enostavnosti je bil razvoj klasične
(sintetične) projektivne geometrije konec 19. stoletja že skoraj
popolnoma zaključen. Njen razvoj se danes nadaljuje v okviru
drugih teorij -- posebej v algebri in algebraični geometriji kot
$n$-razsežna projektivna geometrija.



G. F. B. Riemann\footnote{\index{Riemann, G. F. B.} \textit{G. F.
B. Riemann} (1828--1866), nemški matematik.} je že v svoji knjigi
\textit{O domnevah, ki ležijo v osnovi geometrije} definiral
prostor poljubne dimenzije, ki ni vedno konstantne ukrivljenosti.
Po njem ga danes imenujemo \pojem{Riemannov metrični
prostor}\index{Riemannovi prostori}. Evklidovo geometrijo potem
dobimo kot poseben primer: če je ukrivljenost konstantna in enaka
0; hiperbolično geometrijo dobimo, če izberemo, da je
ukrivljenost konstantna in negativna. Če je ukrivljenost
konstantna in pozitivna, dobimo t. i.
\index{geometrija!eliptična} \pojem{eliptično geometrijo}.
Slednja geometrija je pravzaprav projektivna geometrija, če ji
dodamo metriko. To raziskovanje je bilo hkrati začetek razvoja
nove discipline v matematiki, t. i. \index{geometrija!diferencialna} \pojem{diferencialne geometrije}.

Če razmišljamo o neevklidskih geometrijah, se nam mogoče zdi čudno,
da se v matematiki sploh lahko obravnava več različnih teorij, kot
so npr. evklidska geometrija in hiperbolična geometrija, ki sta v
nasprotju druga z drugo. Za sodobno matematiko je največjega pomena,
da sta obe geometriji določeni s sistemoma aksiomov, ki sta (vsak zase) neprotislovna in popolna. Na vprašanje, katera od teh
dveh geometrij velja, je nesmiselno iskati odgovor v okviru
matematike. To je namreč odvisno od tega, za katere aksiome smo se
odločili. Takšno vprašanje bi bilo enako vprašanju, kateri aksiomi
veljajo. Toda aksiome po definiciji privzamemo brez dokaza. Seveda
lahko zastavimo vprašanje, kakšna je geometrija prostora v fizičnem
smislu in kako jo lahko opišemo z aksiomi.

Za odgovor na to vprašanje je potrebna fizikalna interpretacija
osnovnih geometričnih pojmov. Na primer, premico je najbolj naravno
interpretirati kot svetlobni žarek. V tem smislu se izkaže, da
fizični prostor ni evklidski. Določen ni niti s hiperbolično
geometrijo. S pojavom Einsteinove\footnote{\index{Einstein, A.}
\textit{A. Einstein} (1879--1955), slaven nemški fizik.} teorije
relativinosti v začetku 20. stoletja se je izkazalo, da je v
prostoru vesoljskih razsežnosti bolj ugodno uporabljati neevklidsko
geometrijo s spremenljivo ukrivljenostjo (Riemannovi metrični
prostori!). Lahko rečemo, da je geometrija vesolja lokalno različna
v vsaki točki, odvisno od bližine in velikosti neke mase.
Einsteinova teorija nam tudi pove, da sta prostor in čas medsebojno
povezana in da niti čas (kar je seveda presenetljivo) ne poteka
enako v vsaki točki vesolja. V zvezi z omenjeno povezavo prostora in
časa je pomemben t. i. \pojem{štirirazsežni prostor
Minkowskyega}\footnote{Ta prostor je odkril \index{Minkowsky, H.}
\textit{H. Minkowsky} (1864--1909), nemški matematik.}.

 Že od 20-ih let 20. stoletja in razvoja teorije prapoka vemo,
 da vesolje ni statično in da se širi. Od tega, kakšna
 je njegova usoda, je odvisno, katera geometrija ga globalno najbolje
 opisuje. Toda še vedno ne vemo dokončno, kakšna je oblika
 vesolja niti kakšna je njegova usoda. Niti ne vemo, ali je vesolje
 končno ali neskončno. Kot piše S.
 Hawking\footnote{\index{Hawking, S.} \textit{S. Hawking} (1942),
 angleški fizik.
 Eden najbolj značilnih teoretičnih fizikov našega časa,
 ki je največ vplival na sodobno predstavo o vesolju.}
 v svoji znani popularni knjigi iz leta 1988
 \textit{Kratka zgodovina časa} (\cite{KratkaZgodCasa}), je celo vesolje
 morda končno in neomejeno. Slednje se zdi paradoksalno,
 čeprav si lahko to predstavljamo ako, de si namesto trirazsežnega zamišljamo
 ‘‘dvorazsežno vesolje’’.
 Tako bi bitja tega dvorazsežnega vesolja lahko
 enkrat ugotovila, da njihovo vesolje pravzaprav ni
 ravnina ampak sfera, ki je končna, toda neomejena.
 Sfera je del trirazsežnega prostora. Tako si teoretično
 lahko predstavljamo vesolje kot trirazsežno sfero v
 štirirazsežnem prostoru. Trirazsežna sfera je ena od 3-mnogoterosti.
 V tem primeru bi bila geometrija vesolja globalno eliptična.


Čeprav je samo vprašanje oblike in usode vesolja vprašanje
teoretične fizike in kozmologije, vidimo, kako je sodobna
geometrija (neevklidske geometrije, geometrija večrazsežnih
prostorov itd.) tesno povezana s tem problemom (\cite{Oblika}).
Pomembno je razumeti, da se geometrija (in vsaka druga matematična
disciplina) razvija in obravnava kot abstraktna disciplina, v kateri
so nam fizične interpretacije le inspiracija -- v tem smislu nam
ostajajo le aksiomi in začetni pojmi, na katerih potem izgrajujemo
matematično teorijo.


Na koncu omenimo še enega najpomembnejših geometrov 20.
stoletja H. S. M. Coxeterja\footnote{\index{Coxeter, H. S. M.}
\textit{H. S. M. Coxeter} (1907--2003), kanadski matematik. Eden
največjih geometrov 20. stoletja.}. Coxeter je naprej raziskoval politope
v poljubnih razsežnostih, predvsem pravilne politope. Razen tega se
je veliko ukvarjal z grupami izometrij v hiperbolični geometriji in
z večrazsežno hiperbolično geometrijo.

Potrebno je dodati, da z vsem tem, kar smo
povedali, razvoj geometrije še zdaleč ni končan. Ravno obratno -- nasprotno običajni
predstavi -- geometrija in na splošno matematika se sedaj  razvijata
še hitreje kot kadar koli prej. Tudi danes obstaja v matematiki (v geometriji posebej iz neevklidskih
geometrij) veliko
problemov, ki so še vedno nerešeni.







% DEL 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
%  AKSIOMI RAVNINSKE EVKLIDSKE GEOMETRIJE
%________________________________________________________________________________


\del{Axioms of Planar Euclidean Geometry} \label{pogAKS}

V nadaljevanju bomo ilustrirali aksiomatično zasnovo ravninske
evklidske geometrije. Navedli bomo začetne pojme in začetne izreke -
aksiome, potem pa izpeljali še nekaj novih pojmov in izrekov.
Omenimo, da smo izbrali ravninske aksiome, ker se bomo v tej knjigi
ukvarjali le z geometrijo evklidske ravnine.

Naj bo $\mathcal{S}$ neprazna množica. Njene elemente imenujemo
\index{točka} \pojem{točke} in jih označujemo z $A, B, C, \ldots$
Določene podmnožice množice $\mathcal{S}$ imenujemo \index{premica}
\pojem{premice} in jih označujemo z $a, b, c, \ldots$ Množico
$\mathcal{S}$ (množico vseh točk) imenujemo tudi \index{ravnina}
\pojem{ravnina}. Razen teh sta začetna pojma tudi dve relaciji na
množici $\mathcal{S}$. Prva je \index{relacija!$\mathcal{B}$}
\pojem{relacija $\mathcal{B}$} in se nanaša na tri točke. Dejstvo,
da so točke $A$, $B$ in $C$ v tej relaciji, bomo označevali z
$\mathcal{B}(A,B,C)$ in brali: Točka $B$ je med točkama $A$ in $C$.
Druga je \index{relacija!skladnosti parov točk} \pojem{relacija
skladnosti parov točk}; dejstvo, da so pari točk $A, B$ in $C, D$ v
tej relaciji, bomo označevali z $(A,B) \cong (C,D)$ in brali: Par
točk $(A,B)$ je skladen s parom točk $(C,D)$.

 S pomočjo omenjenih začetnih pojmov lahko
definiramo tudi naslednje izpeljane pojme:

Če točka $A$ pripada premici $p$ ($A\in p$), oz. premica $p$
vsebuje točko $A$ ($p\ni A$), bomo rekli, da
 točka $A$\index{relacija!leži na premici} \pojem{leži na} premici $p$, oz. da premica $p$ \index{relacija!poteka skozi točko}\pojem{poteka
 skozi} točko $A$.
 Za tri ali
več točk pravimo, da so \index{kolinearne točke}\pojem{kolinearne},
če ležijo na isti premici, sicer so
\index{nekolinearne točke}\pojem{nekolinearne}. Dve
različni premici se \pojem{sekata}, če njun presek (presek dveh podmnožic)
ni prazna množica. Njun presek imenujemo \index{presečišče
dveh premic} \pojem{presečišče} dveh premic. Poljubno neprazno
podmnožico $\Phi$ množice $\mathcal{S}$ ($\Phi\subset\mathcal{S}$) imenujemo \index{lik} \pojem{lik}. Pravimo, da lika $\Phi_1$ in $\Phi_2$ \index{lika!sovpadata}\pojem{sovpadata} (oz. sta \index{lika!identična}\pojem{identična}), če je $\Phi_1=\Phi_2$.

 Sedaj bomo
navedli tudi osnovne trditve - aksiome. Po svoji naravi so
razdeljeni v pet skupin:

\begin{enumerate}
  \item incidence axioms (three axioms),
  \item ordering axioms (four axioms),
  \item congruence axioms (four axioms),
  \item continuity axiom (one axiom),
  \item Playfair's axiom (one axiom).
\end{enumerate}



%________________________________________________________________________________
 \poglavje{Incidence Axioms}
  \label{odd2AKSINC}

 Ker premice kot začetni pojmi predstavljajo določene množice točk,
 lahko za
točke in premice obravnavamo ustrezne relacije med elementi
in množicami: $\in$ in $\ni$ - relaciji imenujemo tudi
\index{relacija!incidencije}\pojem{relaciji incidence}. Aksiomi te
skupine opisujejo ravno osnovne lastnosti teh relacij  (Figure
\ref{sl.aks.2.1.1.pic}):

\vspace*{3mm}

        \baksiom \label{AksI1} For every pair of distinct points $A$ and $B$
        there is exactly one line $p$ such that $A$ and $B$  lie on $p$.
        \eaksiom

        \baksiom \label{AksI2}
        For every line there exist at least two distinct points such that both  lie on.
         \eaksiom

        \baksiom \label{AksI3} There exist three points that do not all lie on any one line.
        \eaksiom

\vspace*{3mm}


\begin{figure}[!htb]
\centering
\input{sl.aks.2.1.1.pic}
\caption{} \label{sl.aks.2.1.1.pic}
\end{figure}



 Iz prvih dveh aksiomov \ref{AksI1} in \ref{AksI2} sledi, da je vsaka premica določena s
 svojima dvema različnima točkama. Zato
premico $p$, ki je določena s točkama $A$ in $B$, imenujemo tudi
premica $AB$.

 Iz prvega aksioma \ref{AksI1} sledi, da je presečišče dveh
 premic, ki se sekata, ena sama točka. Če bi namreč dve premici
 imeli še eno skupno točko, bi po tem aksiomu sovpadali (bili bi identični),
 pri definiciji premic, ki se sekata, pa smo zahtevali, da
 sta različni.
 Dejstvo, da se premici $p$ in $q$ sekata v točki $A$, bomo
 zapisali $p\cap q=\{A\}$ ali krajše $p\cap q=A$ (Figure \ref{sl.aks.2.1.2.pic}).



\begin{figure}[!htb]
\centering
\input{sl.aks.2.1.2.pic}
\caption{} \label{sl.aks.2.1.2.pic}
\end{figure}



Tretji aksiom \ref{AksI3} lahko povemo tudi takole: Obstajajo
vsaj tri  točke, ki so nekolinearne.

 Tako smo izpeljali prve posledice aksiomov incidence;
 zaradi enostavnosti jih nismo izrazili v obliki izrekov. To so skoraj vse posledice, ki izhajajo iz prve skupine aksiomov.
 Zaradi tega je geometrija, ki  temelji le na aksiomih incidence,
 preveč enostavna. V njej bi lahko dokazali le obstoj treh točk in treh
 premic. Torej potrebujemo nove aksiome.



%________________________________________________________________________________
 \poglavje{Ordering Axioms}
 \label{odd2AKSURJ}

Aksiomi v tej skupini opisujejo osnovne karakteristike relacije
$\mathcal{B}$, ki smo jo navedli kot osnovni pojem.
\vspace*{3mm}


        \baksiom \label{AksII1} If $\mathcal{B} (A, B, C)$, then $A$, $B$
         and $C$ are three  distinct collinear points, and also
         $\mathcal{B} (C, B, A)$ (Figure \ref{sl.aks.2.2.1.pic}).
        \eaksiom


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.1.pic}
\caption{} \label{sl.aks.2.2.1.pic}
\end{figure}


        \baksiom \label{AksII2} If $A$, $B$ and $C$ are three distinct
         collinear points,
          exactly one of the relations holds: $\mathcal{B}(A,B,C)$,
        $\mathcal{B}(A,C,B)$, $\mathcal{B}(C,A,B)$
        (Figure \ref{sl.aks.2.2.2.pic}).
        \eaksiom


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.2.pic}
\caption{} \label{sl.aks.2.2.2.pic}
\end{figure}



        \baksiom \label{AksII3} Given a pair of distinct points $A$ and $B$ there is a point $C$ on line $AB$, so that
        is $\mathcal{B}(A,B,C)$
        (Figure \ref{sl.aks.2.2.3.pic}).
        \eaksiom

\vspace*{-1mm}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.3.pic}
\caption{} \label{sl.aks.2.2.3.pic}
\end{figure}

        \baksiom \label{AksPascheva}\index{aksiom!Paschev}
        (Pasch's\footnote{\index{Pasch, M.}
         \textit{M. Pasch}
        (1843--1930), nemški matematik, ki je vpeljal pojem urejenosti točk
        v svojih ‘‘Predavanjih o novejši geometriji’’ iz leta 1882.  Te
        aksiome sta kasneje dopolnila italijanski matematik \index{Peano, G.} \textit{G. Peano}
        (1858--1932), v ‘‘Načelih geometrije’’, nato pa še nemški matematik
        \index{Hilbert, D.}\textit{D. Hilbert} (1862--1943) v svoji znani knjigi
         ‘‘Osnove geometrije’’ iz leta
        1899.} axiom)
        Let $A$, $B$ and $C$ be three noncollinear points and $l$ be a line that does not contain point $A$.
        If there is a point $P$ on $l$ that is $\mathcal{B}(B,P,C)$ then either $l$ contains a point $Q$ that is  $\mathcal{B}(A,Q,C)$ or $l$ contains a point $R$ that is $\mathcal{B}(A,R,B)$ (Figure \ref{sl.aks.2.2.4.pic}).
        \eaksiom


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.4.pic}
\caption{} \label{sl.aks.2.2.4.pic}
\end{figure}


V prejšnjem aksiomu nismo posebej poudarili, da premica $l$ leži v ravnini $ABC$, ker gradimo ravninsko evklidsko geometrijo, kjer vse točke ležijo v isti ravnini.

 Na tem mestu ne bomo dokazali vseh posledic aksiomov urejenosti.
Formalna izpeljava vseh dejstev namreč ni tako enostavna in bi vzela veliko prostora. Večino dokazov lahko bralec poišče v \cite{Lucic}.

Dokažimo prvo posledico aksiomov urejenosti.


        \bizrek \label{izrekAksUrACB}
        Given a pair of distinct points $A$ and $B$ there is a point $C$, so that
        is $\mathcal{B}(A,C,B)$.
        \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.5.pic}
\caption{} \label{sl.aks.2.2.5.pic}
\end{figure}


\textbf{\textit{Proof.}} Po aksiomu \ref{AksI1} obstaja natanko ena premica, ki poteka skozi točki $A$ in $B$ - označimo jo z $AB$.
Po aksiomu \ref{AksI3} obstajajo vsaj tri nekolinearne točke.
Obstaja torej vsaj ena točka izven premice $AB$ - označimo jo z $D$
  (Figure \ref{sl.aks.2.2.5.pic}). Naprej po
aksiomu \ref{AksII3} obstaja  takšna točka $E$, da velja
$\mathcal{B}(B,D,E)$, nato pa še takšna točka $F$, da velja
$\mathcal{B}(A,E,F)$. $A$, $B$ in $E$ so nekolinearne točke,
saj bi sicer točka $D$ ležala na premici $AB$ (aksiom \ref{AksI1}).
Premica $FD$ ne poteka skozi točko $A$, ker bi bile po aksiomu \ref{AksI1} točke $F$, $D$, $A$ in $E$
kolinearne, z njimi pa tudi točka $B$. To pa ni možno, ker bi iz tega sledilo,  da točka $D$ leži na premici $AB$.
Uporabimo sedaj Paschev aksiom \ref{AksPascheva} na
točkah $A$, $B$ in $E$ ter premici $FD$. Premica $FD$ namreč seka premico $EB$ v takšni točki $D$,
da je $\mathcal{B}(B,D,E)$, zato seka bodisi premico $AE$ v takšni točki $F$, da je $\mathcal{B}(A,F,E)$ bodisi
premico $AB$ v takšni točki $C$, da je $\mathcal{B}(A,C,B)$. Ker je že $\mathcal{B}(A,E,F)$, po aksiomu \ref{AksII2} ne more biti tudi $\mathcal{B}(A,F,E)$. Torej premica $FD$ seka
premico $AB$ v taki točki $C$, za katero velja $\mathcal{B}(A,C,B)$.
\kdokaz

Relacija $\mathcal{B}$ in aksiomi urejenosti, ki se nanašajo nanjo, nam omogočajo definiranje novih pojmov.


 Naj bosta $A$ in $B$ poljubni različni točki.
  \index{daljica!odprta}\pojem{Odprta daljica} $AB$ z oznako $(AB)$ je množica vseh točk
  $X$, za
  katere velja $\mathcal{B}(A,X,C)$ (Figure \ref{sl.aks.2.2.6.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6.pic}
\caption{} \label{sl.aks.2.2.6.pic}
\end{figure}


  Če odprti daljici $AB$
  dodamo točki $A$ in $B$, dobimo \index{daljica}\pojem{daljico}
  (ali \index{daljica!zaprta} \pojem{zaprto daljico}) $AB$,
  ki jo označimo tudi z $[AB]$.
  Točki $A$ in $B$
  sta njeni \index{krajišče daljice}\pojem{krajišči}, ostale njene točke pa so \pojem{notranje točke} te daljice (Figure \ref{sl.aks.2.2.6.pic}). Še bolj formalno: daljica (oz. zaprta daljica) je unija odprte daljice in množice $\{A,B\}$ oz. $[AB]=(AB)\cup \{A,B\}$.

Na podoben način definiramo tudi
 \index{daljica!polodprta} \pojem{polodprto daljico}: $(AB]=(AB)\cup \{B\}$, oz.   $[AB)=(AB)\cup \{A\}$ (Figure \ref{sl.aks.2.2.6a.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6a.pic}
\caption{} \label{sl.aks.2.2.6a.pic}
\end{figure}

  Iz aksioma \ref{AksII1} neposrednono sledi, da sta daljici $AB$ in $BA$ isti. Iz istega aksioma sledi tudi, da je daljica $AB$ podmnožica premice $AB$. Zato pravimo, da daljica $AB$ \pojem{leži na premici} $AB$,
  premico $AB$
  pa imenujemo \index{nosilka!daljice}  \pojem{nosilka daljice} $AB$  (Figure \ref{sl.aks.2.2.6b.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6b.pic}
\caption{} \label{sl.aks.2.2.6b.pic}
\end{figure}

Po izreku \ref{izrekAksUrACB} ima daljica $AB$ razen svojih krajišč $A$ in $B$ vsaj še eno točko $C_1$. Na ta način lahko dobimo neskončno zaporedje točk $C_1$, $C_2$, ..., za katere velja $\mathcal{B}(A, C_n, C_{n-1})$ ($n\in \{2,3,\cdots\}$)  (Figure \ref{sl.aks.2.2.6c.pic}). Na tem mestu ne bomo formalno dokazovali dejstva, da so vse točke iz zaporedja različne in vse ležijo na daljici $AB$. Iz te trditve pa sledi, da ima vsaka daljica (posledično tudi premica) neskončno mnogo točk.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6c.pic}
\caption{} \label{sl.aks.2.2.6c.pic}
\end{figure}

Definirajmo še relacijo $\mathcal{B}$, ki se nanaša na več kot tri kolinearne točke. Pravimo, da je $\mathcal{B}(A_1,A_2,\ldots,A_n)$ ($n\in\{4,5,\ldots\}$), če za vsak $k\in\{1,2,\ldots,n-2\}$ velja $\mathcal{B}(A_k,A_{k+1},A_{k+2})$ (Figure \ref{sl.aks.2.2.6d.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6d.pic}
\caption{} \label{sl.aks.2.2.6d.pic}
\end{figure}

 Naj bo $S$ točka, ki leži na premici $p$. Na množici $p\setminus \{S\}$ (vseh točk premice $p$ brez točke $S$) definirajmo dve relaciji.
Pravimo, da sta točki $A$ in $B$ ($A,B\in p\setminus \{S\}$) \index{relacija!na različnih straneh točke} \pojem{na različnih straneh  točke} $S$ (kar označimo z $A,B\div S$), če je $B(A,S,B)$, sicer sta  točki $A$ in $B$ ($A,B\in p\setminus \{S\}$) \index{relacija!na isti strani točke} \pojem{na isti strani  točke} $S$ (kar označimo z $A,B\ddot{-} S$). Torej za točki $A,B\in p\setminus \{S\}$ velja $A,B\ddot{-} S$, če ni $A,B\div S$  (Figure \ref{sl.aks.2.2.7.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.7.pic}
\caption{} \label{sl.aks.2.2.7.pic}
\end{figure}


Naj bosta $A$ in $B$ različni točki. Množico vseh takšnih točk $X$, za katere je $B,X\ddot{-} A$ vključno s točko $A$, imenujemo \index{poltrak}\pojem{poltrak} $AB$ z \pojem{začetno točko} ali \pojem{izhodiščem} $A$. Premica $AB$ je
\index{nosilka!poltraka}  \pojem{nosilka poltraka} $AB$ (Figure \ref{sl.aks.2.2.8.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.8.pic}
\caption{} \label{sl.aks.2.2.8.pic}
\end{figure}

Že iz same definicije sledi, da je poltrak podmnožica svoje nosilke oz. da leži na svoji nosilki. Iz relacije $B,X\ddot{-} A$ sledi, da so $B$, $X$ in $A$ kolinearne točke, zato točka $X$ leži na premici $AB$.

Drugih pomembnih lastnosti daljice in poltraka, ki jih bomo kasneje uporabljali, na tem mestu ne bomo dokazovali. Povejmo nekaj teh lastnosti.

If $C$ is the an interior point of the line segment $AB$, then that line segment can be expressed as the union
the line segments $AC$ and $CB$.

            \bizrek \label{izrekAksIIDaljica}
            If $C$ is an interior point of the line segment $AB$, then that line segment can be expressed as the union
            the line segments $AC$ and $CB$ (Figure \ref{sl.aks.2.2.9.pic}).
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.9.pic}
\caption{} \label{sl.aks.2.2.9.pic}
\end{figure}


            \bizrek \label{izrekAksIIPoltrak}
            Each point lying on the line determines exactly
            two rays on it. The union of these rays is equal to that line  (Figure \ref{sl.aks.2.2.9.pic}).
            \eizrek

Dokaz prejšnjega izreka temelji na dejstvu, da je relacija $\ddot{-} A$ ekvivalenčna relacija, ki ima dva razreda. Vsak od razredov je ustrezen odprti poltrak.

Poltraka iz prejšnjega izreka, ki sta določena z isto začetno točko na premici, imenujemo \index{poltrak!komplementarni}\pojem{komplementarna poltraka}.

Pojma daljica in poltrak nam omogočata definiranje novih pojmov.

Naj bodo $A_1$, $A_2$, ... $A_n$ takšne točke v ravnini, da nobene tri v zaporedju niso kolinearne. Unijo daljic $A_1A_2$, $A_2A_3$,... $A_{n-1}A_n$ imenujemo \index{lomljenka} \pojem{lomljenka} $A_1A_2\cdots A_n$ ali \index{poligonska
črta}\pojem{poligonska črta} $A_1A_2\cdots A_n$ (Figure \ref{sl.aks.2.2.10.pic}). Točke  $A_1$, $A_2$, ... $A_n$ so \index{oglišče!lomljenke} \pojem{oglišča lomljenke},
daljice $A_1A_2$, $A_2A_3$,... $A_{n-1}A_n$ pa \index{stranica!lomljenke} \pojem{stranice lomljenke}. Stranici lomljenke s skupnim ogliščem sta \index{sosednji stranici!lomljenke} \pojem{sosednji stranici lomljenke}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10.pic}
\caption{} \label{sl.aks.2.2.10.pic}
\end{figure}

Če stranice lomljenke nimajo skupnih točk, razen sosednjih stranic, ki imata skupno oglišče, takšno lomljenko imenujemo \index{lomljenka!enostavna} \pojem{enostavna lomljenka} (Figure \ref{sl.aks.2.2.10a.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10a.pic}
\caption{} \label{sl.aks.2.2.10a.pic}
\end{figure}

Lomljenka $A_1A_2\cdots A_nA_{n+1}$, pri kateri je $A_{n+1}=A_1$ in so $A_n$, $A_1$ in $A_2$ nekolinearne točke, se imenuje \index{lomljenka!sklenjena} \pojem{sklenjena lomljenka} $A_1A_2\cdots A_n$ (Figure \ref{sl.aks.2.2.10b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10b.pic}
\caption{} \label{sl.aks.2.2.10b.pic}
\end{figure}

Posebej nas bodo zanimale \pojem{enostavne sklenjene lomljenke} (Figure \ref{sl.aks.2.2.10b.pic}).

Naj bosta $p$ in $q$ dva poltraka s skupnim izhodiščem $O$ (Figure \ref{sl.aks.2.2.10c.pic}). Unijo teh dveh poltrakov imenujemo \index{kotna lomljenka} \pojem{kotna lomljenka} $pq$ (ali $pOq$).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10c.pic}
\caption{} \label{sl.aks.2.2.10c.pic}
\end{figure}


Za nek lik $\Phi$ pravimo, da je \index{lik!konveksen}\pojem{konveksen}, če je za poljubni njegovi točki $A,B\in \Phi$ daljica $AB$ podmnožica tega lika oz. če velja naslednje (Figure \ref{sl.aks.2.2.10d.pic}):
 $$(\forall A)(\forall B)\hspace*{1mm} (A,B\in \Phi \Rightarrow [AB]\subseteq \Phi).$$
Za lik, ki ni konveksen, pravimo, da je \index{lik!nekonveksen}\pojem{nekonveksen} (Figure \ref{sl.aks.2.2.10d.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10d.pic}
\caption{} \label{sl.aks.2.2.10d.pic}
\end{figure}

Neposredno iz definicije sledi, da je premica konveksen lik. Kot posledico aksiomov te skupine je mogoče dokazati, da sta tudi daljica in poltrak konveksna lika.


Za nek lik $\Phi$ pravimo, da je
\index{lik!povezan}\pojem{povezan lik}, če za vsaki njegovi točki $A,B\in \Phi$ obstaja lomljenka $AT_1T_2\cdots T_nB$, ki je podmnožica tega lika oz. če velja naslednje (Figure \ref{sl.aks.2.2.10e.pic}):
 $$(\forall A\in \Phi)(\forall B\in \Phi)(\exists T_1,T_2,\cdots , T_n)\hspace*{1mm}  AT_1T_2\cdots T_nB\subseteq \Phi.$$


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10e.pic}
\caption{} \label{sl.aks.2.2.10e.pic}
\end{figure}

 Za lik, ki ni povezan, pravimo, da je \index{lik!nepovezan}\pojem{nepovezan}.

 Jasno je, da je vsak konveksen lik tudi povezan. Za lomljenko je dovolj vzeti kar daljico $AB$. Obratno seveda ne velja. Obstajajo liki, ki so povezani, niso pa konveksni, kar bomo ugotovili kasneje.



Sedaj bomo definirali dve relaciji, ki sta analogni z relacijama $\ddot{-} S$ in $\div S$.
 Naj bo $p$ premica, ki leži v ravnini $\alpha$ (ker aksiomatsko gradimo le evklidsko geometrijo ravnine, so pravzaprav vse točke, ki za nas obstajajo, v tej ravnini). Na množici $\alpha\setminus p$ (vseh točk razen točk premice $p$) definirajmo dve relaciji.
Pravimo, da sta točki $A$ in $B$ ($A,B\in \alpha\setminus p$) \index{relacija!na različnih bregovih premice} \pojem{na različnih bregovih  premice} $p$ (kar označimo z $A,B\div p$), če ima daljica $AB$ s premico $p$ skupno točko, sicer sta  točki $A$ in $B$ ($A,B\in \alpha\setminus p$) \index{relacija!na istem bregu premice} \pojem{na istem bregu  premice} $p$ (kar označimo z $A,B\ddot{-} p$). Torej za točki $A,B\in \alpha\setminus p$ je $A,B\ddot{-} p$, če ni $A,B\div p$ (Figure \ref{sl.aks.2.2.11.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.11.pic}
\caption{} \label{sl.aks.2.2.11.pic}
\end{figure}


Naj bo $A$ točka, ki ne leži na premici $p$. Množico vseh takšnih točk $X$, za katere je $A,X\ddot{-} p$, imenujemo
\index{polravnina!odprta}\pojem{odprta polravnina} $pA$. Unija odprte polravnine $pA$ in premice $p$ je \index{polravnina!zaprta}\pojem{zaprta polravnina} oz. kar
\index{polravnina}\pojem{polravnina} $pA$. Premica $p$ je \index{rob!polravnine} \pojem{rob} te polravnine (Figure \ref{sl.aks.2.2.11a.pic}). Če točki $B$ in $C$ ležita na robu $p$ polravnine $pA$, bomo to ravnino imenovali tudi polravnina $BCA$. Razen tega bomo polravnine označevali tudi z grškimi črkami $\alpha$, $\beta$, $\gamma$,...

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.11a.pic}
\caption{} \label{sl.aks.2.2.11a.pic}
\end{figure}

Podobno kot pri poltraku je mogoče dokazati (kot posledico aksiomov te skupine), da vsaka premica $p$ v ravnini določa dve polravnini $\alpha$ in $\alpha'$, ki imata premico $p$ za rob (Figure \ref{sl.aks.2.2.11a.pic}). Pravimo, da sta si v tem primeru $\alpha$ in $\alpha'$ \index{polravnina!komplementarna}\pojem{komplementarni polravnini}.
Izkaže se, da je unija dveh komplementarnih polravnin cela ravnina. Podobno kot pri poltraku, tudi dokaz omenjenih trditev temelji na dejstvu, da je relacija $\ddot{-} p$ ekvivalenčna relacija z dvema razredoma. Vsak od razredov je ustrezna odprta polravnina.

Naj bo $pq$ oz. $pOq$ kotna lomljenka. Definirajmo novo relacijo na množici vseh točk ravnine razen točk, ki ležijo na lomljenki. Pravimo, da sta točki $A$ in $B$ na isti strani kotne lomljenke $pq$ (kar označimo z $A,B\ddot{-} pq$), če obstaja lomljenka $AT_1T_2\cdots T_nB$, ki kotne lomljenke $pq$ ne seka oz. z njo nima skupnih točk (Figure \ref{sl.aks.2.2.12.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12.pic}
\caption{} \label{sl.aks.2.2.12.pic}
\end{figure}

 Tudi relacija $\ddot{-} pq$ je ekvivalenčna relacija, ki ima dva razreda. Unijo vsakega od teh dveh razredov s kotno lomljenko $pq$ imenujemo
 \index{kot}\pojem{kot} $pq$, ki ga označimo z $\angle pq$, oz. $\angle pOq$.
  Kotna lomljenka torej določa dva kota. Dilemo, za katerega od kotov gre pri oznaki  $\angle pOq$, bomo kmalu odpravili.
 Poltraka $p$ in $q$ sta
\index{krak!kota}\pojem{kraka kota} in točka $O$ \index{vrh kota}\pojem{vrh kota}.
Če sta $P\in p$ in $Q\in q$ točki, ki ležita na krakih kota $pOq$ in se razlikujeta od njegovega vrha $O$, bomo kot imenovali tudi kot $POQ$ in označili z $\angle POQ$ (Figure \ref{sl.aks.2.2.12a.pic}). Če vemo, za kateri kot gre, ga bomo označevali kar z njegovim vrhom: $\angle O$. Razen tega bomo kote označevali tudi z grškimi črkami $\alpha$, $\beta$, $\gamma$,...

Vse točke kota $pOq$, ki ne ležijo na nobenem od obeh krakov $p$ in $q$, imenujemo \index{notranje točke!kota} \pojem{notranje točke kota}, množico vseh teh točk pa \index{notranjost!kota}\pojem{notranjost kota}. Jasno je, da gre za točke ustreznega razreda, ki jih določa relacija $\ddot{-} pq$. Točke drugega razreda so \index{zunanje!točke kota}\pojem{zunanje točke kota}, cel razred pa \index{zunanjost!kota}\pojem{zunanjost kota}. Točke, ki ležijo na krakih, oz. na kotni lomljenki $pOq$, ki kot $pOq$ določa, so \index{robne točke!kota}\pojem{robne točke kota}, cela lomljenka pa je \index{rob!kota}\pojem{rob kota}.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12a.pic}
\caption{} \label{sl.aks.2.2.12a.pic}
\end{figure}

Če sta kraka kota komplementarna poltraka, takšen kot imenujemo
\index{kot!iztegnjeni}\pojem{iztegnjeni kot} (Figure \ref{sl.aks.2.2.12b.pic}). Kot množica točk je ta kot v bistvu enak polravnini z robom, ki je nosilka obeh krakov.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12b.pic}
\caption{} \label{sl.aks.2.2.12b.pic}
\end{figure}

Če kotna lomljenka $pOq$ ne določa iztegnjenenega kota oz. ni enaka premici, se izkaže, da $pOq$ določa dva kota, ki predstavljata konveksen in nekonveknen lik - imenujemo ju \index{kot!konveksen}\pojem{konveksen (izbočeni) kot} in \index{kot!nekonveksen}\pojem{nekonveksen (vdrti) kot}. Formalen dokaz tega dejstva bomo na tem mestu izpustili. Če ne poudarimo drugače, bomo pod oznako $\angle pOq$ (oz. $\angle pq$ ali $\angle POQ$) vedno mislili na konveksen kot (Figure \ref{sl.aks.2.2.12b.pic}). V tem smislu je že iz definicije kota jasno, da (konveksna) kota $pOq$ in $qOp$ predstavljata isti kot.

Kota $pOq$ in $qOr$, ki imata skupen krak $q$, ki je hkrati njun presek (kot množice točk), sta \index{kot!sosednji}\pojem{sosednja kota} (Figure \ref{sl.aks.2.2.12c.pic}).  Če sta pri tem poltraka $p$ in $r$ še komplementarna (oz. določata iztegnjeni kot), pravimo, da sta $pOq$ in $qOr$ \index{kota!sokota}\pojem{sokota}  (Figure \ref{sl.aks.2.2.12c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12c.pic}
\caption{} \label{sl.aks.2.2.12c.pic}
\end{figure}

Kota $pOq$ in $rOs$ sta \index{kota!sovršna}\pojem{sovršna kota}, če sta $p$ in $r$ oz. $q$ in $s$ para komplementarnih (dopolnilnih) poltrakov (Figure \ref{sl.aks.2.2.12d.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12d.pic}
\caption{} \label{sl.aks.2.2.12d.pic}
\end{figure}

 Naj bo $A_1A_2\cdots A_n$ ($n\in \{3,4,5,\cdots\}$) enostavna sklenjena lomljenka.
 Podobno kot pri kotni lomljenki, lahko na množici vseh točk ravnine razen točk, ki ležijo na lomljenki $A_1A_2\cdots A_n$, definiramo naslednjo relacijo: pravimo, da sta točki $B$ in $C$ na isti strani enostavne sklenjene lomljenke $A_1A_2\cdots A_n$ (kar označimo z $B,C\ddot{-} A_1A_2\cdots A_n$), če obstaja lomljenka $BT_1T_2\cdots T_nC$, ki enostavne sklenjene lomljenke $A_1A_2\cdots A_n$ ne seka oz. z njo nima skupnih točk (Figure \ref{sl.aks.2.2.13.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13.pic}
\caption{} \label{sl.aks.2.2.13.pic}
\end{figure}

 Tudi v tem primeru je mogoče dokazati, da gre za ekvivalenčno relacijo z dvema razredoma - pri tem za en razred obstaja premica, ki cela leži v njem, za drugi pa takšne premice ni. Unijo tistega razreda, ki ne vsebuje nobene premice (intuitivno - tistega, ki je omejen) in enostavne sklenjene lomljenke, $A_1A_2\cdots A_n$ imenujemo
\index{večkotnik}\pojem{večkotnik} $A_1A_2\cdots A_n$ ali
\index{$n$-kotnik}\pojem{$n$-kotnik} $A_1A_2\cdots A_n$ (Figure \ref{sl.aks.2.2.13a.pic}). Vse točke omenjenega razreda, ki ne vsebuje nobene premice, imenujemo \index{notranje točke!večkotnika} \pojem{notranje točke večkotnika}, cel razred pa \index{notranjost!večkotnika}\pojem{notranjost večkotnika}. Točke drugega razreda so \index{zunanje!točke večkotnika}\pojem{zunanje točke večkotnika}, cel razred pa \index{zunanjost!večkotnika}\pojem{zunanjost večkotnika}. Točke, ki ležijo na lomljenki $A_1A_2\cdots A_n$, ki določa večkotnik, so \index{robne točke!večkotnika}\pojem{robne točke večkotnika}, cela lomljenka pa je \index{rob!večkotnika}\pojem{rob večkotnika}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13a.pic}
\caption{} \label{sl.aks.2.2.13a.pic}
\end{figure}


Za notranje točke večkotnika velja izrek, ki je pravzaprav ekvivalenten njihovi definiciji. Izrek bomo podali brez dokaza.

            \bizrek
            A point $N$ is an interior point of a polygon if and only
            if any ray from the point $N$, that does not contain the vertices of the
            polygon, intersects an odd number of sides of the polygon (Figure \ref{sl.aks.2.2.13b.pic}).
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13b.pic}
\caption{} \label{sl.aks.2.2.13b.pic}
\end{figure}

Točke $A_1$, $A_2$,..., $A_n$ (oglišča lomljenke) so \index{oglišče!večkotnika}\pojem{oglišča večkotnika}, daljice $A_1A_2$, $A_2A_3$, ... $A_{n-1}A_n$, $A_nA_1$ pa
\index{stranica!večkotnika}\pojem{stranice večkotnika}. Premice $A_1A_2$, $A_2A_3$, ... $A_{n-1}A_n$, $A_nA_1$ so \index{nosilka!stranice}\pojem{nosilke stranic} $A_1A_2$, $A_2A_3$, ... $A_{n-1}A_n$, $A_nA_1$. Stranici, ki vsebujeta skupno oglišče, sta \index{stranica!sosednja}\pojem{sosednji stranici}, sicer sta stranici  \index{stranica!nesosednja}\pojem{nesosednji}. Če sta oglišči hkrati krajišči iste stranice, pravimo, da sta oglišči \index{oglišče!sosednje}\pojem{sosednji}, sicer sta oglišči \index{oglišče!nesosednje}\pojem{nesosednji}.
Iz definicije je jasno, da ima vsako oglišče natanko dve sosednji oglišči. Prav tako ima vsaka starnica natanko dve sosednji stranici.
 Daljica, ki ju določata nesosednji oglišči, se imenuje
\index{diagonala!večkotnika}\pojem{diagonala večkotnika} (Figure \ref{sl.aks.2.2.13c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13c.pic}
\caption{} \label{sl.aks.2.2.13c.pic}
\end{figure}

O diagonalah večkotnika govori naslednji izrek.

            \bizrek
            The number of diagonals of an $n$-gon is $\frac{n(n-3)}{2}$.
            \eizrek

Dokaz tega izreka bomo podali v razdelku \ref{odd3Helly}, kjer bomo posebej obravnavali kombinatorne lastnosti množic točk v ravnini.

Definirajmo še kote večkotnika. Naj bo $O$ poljubno oglišče večkotnika ter $P$ in $Q$ njegovi sosednji oglišči. Poltraka $OP$ in $OQ$ označimo s $p$ in $q$. V tem primeru kotna lomljenka $pOq$ določa dva kota. Tisti kot, za katerega velja, da vsak poltrak z začetno točko $O$, ki pripada temu kotu in ne vsebuje drugih oglišč večkotnika, seka rob večkotnika razen v točki $O$ še v lihem številu točk, imenujemo \index{kot!notranji večkotnika}\pojem{notranji kot večkotnika} ali krajše \index{kot!notranji}\pojem{kot večkotnika} ob oglišču $O$ (Figure \ref{sl.aks.2.2.13d.pic}). Če je notranji kot večkotnika konveksen, njegov sokot imenujemo \index{kot!zunanji večkotnika}\pojem{zunanji kot večkotnika} (Figure \ref{sl.aks.2.2.13d.pic}).
  Kota večkotnika sta
  \index{kot!sosednji}\pojem{sosednja kota}, če sta njuna vrha sosednji oglišči večkotnika, sicer sta kota \index{kot!nesosednji}\pojem{nesosednja}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13d.pic}
\caption{} \label{sl.aks.2.2.13d.pic}
\end{figure}

Najbolj enostaven $n$-kotnik in hkrati eden najpogosteje uporabljenih likov v geometriji ravnine dobimo v primeru $n=3$ - \index{trikotnik}\pojem{trikotnik}.
V primeru trikotnika $ABC$ (označevali ga bomo z $\triangle ABC$) so torej točke $A$, $B$ in $C$ njegova \pojem{oglišča}, daljice $AB$, $BC$ in $CA$ pa njegove
\index{stranica!trikotnika}\pojem{stranice} (Figure \ref{sl.aks.2.2.14.pic}). Očitno sta vsaki dve stranici trikotnika sosednji. Prav tako sta sosednji tudi vsaki dve oglišči. Trikotnik torej nima nobene diagonale. Pravimo, da sta oglišče $A$ ($B$ in $C$) oz. kot $BAC$ ($ABC$ in $ACB$) \index{oglišče!nasprotno trikotnika}\pojem{nasprotno oglišče} oz. \index{kot!nasprotni trikotnika}\pojem{nasprotni kot} stranice $BC$ ($AC$ in $AB$) trikotnika $ABC$. In tudi stranica $BC$ ($AC$ in $AB$) je \index{stranica!nasprotna trikotnika}\pojem{nasprotna stranica} oglišča $A$ ($B$ in $C$) oz. kota $BAC$ ($ABC$ in $ACB$) trikotnika $ABC$. Kote (notranje) trikotnika $ABC$ ob ogliščih $A$, $B$ in $C$ pogosto označimo z $\alpha$, $\beta$ in $\gamma$, ustrezne zunanje pa z $\alpha_1$, $\beta_1$ in $\gamma_1$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14.pic}
\caption{} \label{sl.aks.2.2.14.pic}
\end{figure}

Trikotnik $ABC$ lahko definiramo tudi kot presek polravnin $ABC$, $ACB$ in $BCA$. Na tem mestu ekvivalentnosti dveh definicij ne bomo dokazovali.

 Paschev aksiom v terminih trikotnikov lahko sedaj izrazimo v krajši obliki:

If a line in the plane of a triangle intersects one of its sides
and does not pass through any of its vertices, then intersects exactly one more side of this triangle



             \bizrek \label{PaschIzrek}
           If a line, not passing through any vertex of a triangle, intersects one side of the triangle
           then the line intersects exactly one more side of this triangle (Figure \ref{sl.aks.2.2.14a.pic}).
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14a.pic}
\caption{} \label{sl.aks.2.2.14a.pic}
\end{figure}

  V primeru $n=4$ za $n$-kotnik dobimo
\index{štirikotnik}\pojem{štirikotnik}. Ker ima vsako oglišče štirikotnika natanko eno nesosednje oglišče, bomo to oglišče imenovali tudi \index{oglišče!nasprotno štirikotnika}\pojem{nasprotno oglišče} štirikotnika. Podobno bosta nesosednji stranici \index{stranica!nasprotna štirikotnika}\pojem{nasprotni stranici} štirikotnika. Diagonalo štirikotnika torej določata nasprotni oglišči.
 Iz same definicije je jasno, da ima štirikotnik dve diagonali\index{diagonala!štirikotnika} (Figure \ref{sl.aks.2.2.14b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14b.pic}
\caption{} \label{sl.aks.2.2.14b.pic}
\end{figure}

Za nesosednja kota štirikotnika pravimo tudi, da sta
 \index{kot!nasprotni štirikotnika}\pojem{nasprotna kota} štirikotnika. Kote (notranje) štirikotnika $ABCD$ ob ogliščih $A$, $B$, $C$ in $D$ ponavadi označimo z $\alpha$, $\beta$, $\gamma$ in $\delta$, ustrezne zunanje (tiste, ki obstajajo) pa z $\alpha_1$, $\beta_1$, $\gamma_1$ in $\delta_1$ (Figure \ref{sl.aks.2.2.14c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14c.pic}
\caption{} \label{sl.aks.2.2.14c.pic}
\end{figure}



Kot posledico aksiomov urejenosti bomo na koncu tega razdelka vpeljali še pojma orientacije trikotnika in orientacije kota.

Trikotnik $ABC$, pri katerem so oglišča urejena trojica $(A,B,C)$, imenujemo
  \index{orientacija!trikotnika} \pojem{orientirani trikotnik}.
Pravimo, da sta orientirana trikotnika $ABC$ in $BCA'$ \pojem{iste orientacije}, če velja $A,A'\ddot{-} BC$, in nasprotne orientacije, če je $A,A'\div BC$
 (Figure \ref{sl.aks.2.2.15.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.15.pic}
\caption{} \label{sl.aks.2.2.15.pic}
\end{figure}

Ko govorimo o orientaciji dveh trikotnikov, bomo v bodoče vedno mislili na orientirana trikotnika (besedo orientirana bomo pogosto izpustili). Trikotnika $ABC$ in $A'B'C'$ sta \pojem{iste orientacije} oz. sta \pojem{enako orientirana}, če obstaja takšno zaporedje trikotnikov: $\triangle ABC=\triangle P_1P_2P_3$, $\triangle P_2P_3P_4$, $\triangle P_3P_4P_5$, ..., $\triangle P_{n-2}P_{n-1}P_n=\triangle A'B'C'$, da je v tem zaporedju število sprememb orientacije dveh sosednjih trikotnikov sodo
 (Figure \ref{sl.aks.2.2.15a.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.15a.pic}
\caption{} \label{sl.aks.2.2.15a.pic}
\end{figure}

Mogoče je dokazati, da je relacija iste orientacije dveh trikotnikov ekvivalenčna relacija, ki ima dva razreda. Za dva trikotnika, ki nista v istem razredu, pravimo, da sta \pojem{različne orientacije} oz. \pojem{različno orientirana}. Vsak od dveh razredov določa \index{orientacija!ravnine}\pojem{orientacijo ravnine}. Imenujemo ju \pojem{pozitivna orientacija} in \pojem{negativna orientacija}. Za lažjo predstavo se dogovorimo, naj bo orientacija, ki ustreza smeri vrtenja urinega kazalca, negativna, njej nasprotna pa pozitivna orientacija.
 Če ne bomo drugače poudarili, bomo vedno uporabljali pozitivno orientacijo ravnine oz. trikotnikov
 (Figure \ref{sl.aks.2.2.15b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.15b.pic}
\caption{} \label{sl.aks.2.2.15b.pic}
\end{figure}


Definirajmo še orientacijo kotov. Kota $ASB$ in $A'S'B'$, od katerih nobeden ni iztegnjeni kot, sta \pojem{iste orientacije}, če:
\begin{itemize}
  \item sta oba konveksna ali oba nekonveksna, trikotnika $ASB$ in $A'S'B'$ pa sta iste orientacije (Figure \ref{sl.aks.2.2.16.pic}),
  \item je en kot konveksen in drugi nekonveksen, tikotnika $ASB$ in $A'S'B'$ pa sta nasprotne orientacije (Figure \ref{sl.aks.2.2.16c.pic}).
\end{itemize}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.16.pic}
\caption{} \label{sl.aks.2.2.16.pic}
\end{figure}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.16c.pic}
\caption{} \label{sl.aks.2.2.16c.pic}
\end{figure}

 Če je $\angle ASB$ iztegnjeni kot, $\angle A'S'B'$ pa konveksen kot, sta kota $ASB$ in $A'S'B'$ iste orientacije, če obstaja takšna točka $C$ v notranjosti kota $ASB$, da sta kota $ASC$ in $A'S'B'$ iste orientacije (Figure \ref{sl.aks.2.2.16d.pic}). Podobno naredimo tudi, če je kot $A'S'B'$ nekonveksen ali če sta oba kota $ASB$ in $A'S'B'$ iztegnjena.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.16d.pic}
\caption{} \label{sl.aks.2.2.16d.pic}
\end{figure}


Tudi v tem primeru se izkaže, da je relacija iste orientacije kotov ekvivalenčna relacija, ki ima dva razreda. Pri tem pozitivno orientacijo kota predstavlja tisti razred, pri katerem ima trikotnik $ASB$ za konveksni kot
 $ASB$ iz tega razreda  negativno orientacijo
 (Figure \ref{sl.aks.2.2.16a.pic}).
V tem smislu sta kota $ASB$ in $BSA$ nasprotno orientirana.
   \index{orientacija!kota} \pojem{Orientirani kot} $ASB$  bomo označili z $\measuredangle ASB$.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.16a.pic}
\caption{} \label{sl.aks.2.2.16a.pic}
\end{figure}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.16b.pic}
\caption{} \label{sl.aks.2.2.16b.pic}
\end{figure}

Če je $C$ poljubna točka, ki ne leži na robu kota $ASB$, bomo definirali vsoto orientiranih kotov $\measuredangle ASC$ in $\measuredangle CSB$
 (Figure \ref{sl.aks.2.2.16b.pic}):
 \begin{eqnarray}
 \measuredangle ASC+\measuredangle CSB = \measuredangle ASB.
 \label{orientKotVsota}
 \end{eqnarray}


%________________________________________________________________________________
 \poglavje{Congruence Axioms}
 \label{odd2AKSSKL}


Naslednji aksiomi so potrebni, da lahko vpeljemo pojem in lastnosti
skladnosti likov. S prejšnjimi aksiomi smo namreč lahko vpeljali in
obravnavali pojme: daljica, poltrak, kot, večkotnik, ... ne pa
še pojmov, ki so povezani s skladnostjo: krožnica, pravi kot,
skladnost trikotnikov,~...

Intuitivna ideja skladnosti likov, ki smo jo uporabljali že v
osnovni šoli, je povezana z gibanjem, ki prvi lik preslika v
drugega. To idejo bomo sedaj uporabili, da bi formalno definirali
pojem skladnosti in njene lastnosti.
 Najprej bomo začeli z osnovnim, že omenjenim, pojmom skladnosti
 parov točk $(A,B)\cong (C,D)$ (Figure \ref{sl.aks.2.3.1.pic})
 ter formalno definirali pojem
 ‘‘gibanja’’.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.1.pic}
\caption{} \label{sl.aks.2.3.1.pic}
\end{figure}

 S pomočjo skladnosti parov točk najprej definirajmo skladnost $n$-terice točk.
 Pravimo, da
sta dve $n$-terici točk skladni (Figure \ref{sl.aks.2.3.2.pic}) oz.
$$(A_1 , A_2,\ldots ,A_n ) \cong ( A'_1 , A'_2 ,\ldots , A'_n ),$$
če je: $(A_i,A_j)\cong (A'_i,A'_j)$ za vsako $i,j\in \{1,2,\ldots,
n\}$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.2.pic}
\caption{} \label{sl.aks.2.3.2.pic}
\end{figure}


Bijektivna preslikava ravnine v ravnino
$\mathcal{I}:\mathcal{S}\rightarrow \mathcal{S}$ je
\index{izometrija}\pojem{izometrija} ali \pojem{izometrijska
transformacija}, če ohranja relacijo skladnosti parov točk
(Figure \ref{sl.aks.2.3.3.pic}) oz. če za vsaki dve točki $A$ in
$B$ velja:
 $$(\mathcal{I}(A),\mathcal{I}(B))\cong (A,B).$$

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.3.pic}
\caption{} \label{sl.aks.2.3.3.pic}
\end{figure}


Z naslednjimi aksiomi bomo vpeljali lastnosti na novo definirane
preslikave.


\vspace*{3mm}


            \baksiom \label{aksIII1} Isometries preserve the relation
            $\mathcal{B}$  (Figure \ref{sl.aks.2.3.4.pic}), which means that for every
              isometry $\mathcal{I} $ holds:
            $$\mathcal{I}: A, B,C\mapsto A',B',C'\hspace*{2mm}\wedge \hspace*{2mm}
            \mathcal{B}(A,B,C)
             \hspace*{1mm}\Rightarrow\hspace*{1mm} \mathcal{B}(A',B',C').$$
             \eaksiom


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.4.pic}
\caption{} \label{sl.aks.2.3.4.pic}
\end{figure}


            \baksiom  \label{aksIII2} If $ABC$ and $A'B'C'$ are two half-planes
             (Figure \ref {asl.aks.2.3.5.pic}), then there is a single isometry
             $\mathcal{I}$, which maps:

            \begin{itemize}
            \item point $A$ to point $A'$,
               \item half-line $AB$ in half-line $A'B'$,
              \item half-plane $ABC$ to half-plane $A'B'C'$.
            \end{itemize}
            If $(A,B)\cong (A',B')$ holds,
            then it is $\mathcal{I}(B)=B'$.
            \\ If in addition
            $(A,B,C)\cong (A',B',C')$ also holds,
             then it is $\mathcal{I}(B)=B'$ and $\mathcal{I}(C)=C'$.
            \eaksiom


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.5.pic}
\caption{} \label{asl.aks.2.3.5.pic}
\end{figure}

            \baksiom  \label{aksIII3} For every two points $A$ and $B$ there exists
             isometry such that holds $$\mathcal{I}: A, B\mapsto B,A.$$
             If $(S,A)\cong (S,B)$ and $S\in AB$, then for each isometry $\mathcal{I}$ with this property  holds $\mathcal{I}(S)=S$ (Figure \ref{sl.aks.2.3.6.pic}).
            \eaksiom

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.6.pic}
\caption{} \label{sl.aks.2.3.6.pic}
\end{figure}

            \baksiom  \label{aksIII4} The set of all isometries with respect to the composition of mappings form a group, which means that:
            \begin{itemize}
            \item composition of two isometries  $\mathcal{I}_2\circ \mathcal{I}_1$ is isometry,
            \item identity map $\mathcal{E}$ is isometry,
            \item if $\mathcal{I}$ is  isometry, then its inverse transformation
            $\mathcal{I}^{-1}$ is also isometry.
            \end{itemize}
             \eaksiom

\vspace*{3mm}

 Omenimo, da je pri strukturi grupe zahtevana tudi lastnost
 asociativnosti oz. $\mathcal{I}_1\circ (\mathcal{I}_2\circ \mathcal{I}_3)=
  (\mathcal{I}_1\circ \mathcal{I}_2)\circ \mathcal{I}_3$ (za poljubne izometrije
  $\mathcal{I}_1$, $\mathcal{I}_2$ in $\mathcal{I}_3$), ki pa je pri
  operaciji kompozituma funkcij
 avtomatično izpolnjena. Omenimo še, da je \pojem{identiteta} \index{identiteta}
 $\mathcal{E}$ iz prejšnjega aksioma preslikava, za katero je
 $\mathcal{E}(A)=A$ za vsako točko ravnine. Preslikava
 $\mathcal{I}^{-1}$ je \pojem{inverzna preslikava} za izometrijo
 $\mathcal{I}$, če velja $\mathcal{I}^{-1}\circ \mathcal{I}
 =\mathcal{I}\circ\mathcal{I}^{-1}=\mathcal{E}$. Po prejšnjem
 aksiomu sta torej identiteta in inverzna preslikava vsake izometrije tudi
  izometriji.



Dokažimo prve posledice aksiomov skladnosti. Najprej bomo
obravnavali naslednje lastnosti izometrij.



            \bizrek \label{izrekIzoB} Isometry maps a line to a line, a line segment to a line segment, a ray to a ray,
            a half-plane to a half-plane, an angle to an angle and an $n$-gon to an $n$-gon.
             \eizrek

\textbf{\textit{Proof.}}
 Po aksiomu \ref{aksIII1} izometrije ohranjajo relacijo
 $\mathcal{B}$. Zato se vse točke daljice $AB$ pri izometriji $I$ preslikajo
  v točke, ki ležijo na daljici $A'B'$, kjer je $A'=\mathcal{I}(A)$ in
  $B'=\mathcal{I}(B)$. Ker je tudi inverzna preslikava $\mathcal{I}^{-1}$
  izometrija (aksiom \ref{aksIII4}), je vsaka točka daljice
  $A'B'$ slika neke točke, ki leži na daljici $AB$. Torej se z
  izometrijo $\mathcal{I}$
  daljica $AB$ preslika v daljico $A'B'$.

 Tudi preostale like iz izreka smo definirali s pomočjo relacije
 $\mathcal{B}$, tako da je dokaz podoben kot za daljico.
 \kdokaz

Iz dokaza prejšnjega izreka sledi, da se krajišči daljice $AB$
z izometrijo preslikata v krajišči slike $A'B'$. Na podoben
način se z izometrijo izhodišče poltraka preslika v izhodišče
poltraka, rob polravnine v rob polravnine, vrh kota v vrh kota in
oglišče večkotnika v oglišče večkotnika.

Izometrije so definirane kot bijektivne preslikave, ki ohranjajo
skladnost parov točk. Ali velja tudi, da za skladne pare točk
obstaja izometrija, ki prvi par preslika v drugega? Odgovor podajmo
z naslednjim izrekom.


            \bizrek \label{izrekAB} If $(A,B)\cong (A',B')$, then there is an isometry
             $\mathcal{I}$, which maps the points $A$ and $B$ to the points
            $A'$ and $B'$,
             i.e.:
            $$\mathcal{I}: A, B\mapsto A',B'.$$
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.7.pic}
\caption{} \label{sl.aks.2.3.7.pic}
\end{figure}


\textbf{\textit{Proof.}}
 Naj bo $C$ točka, ki ne leži na premici $AB$, in $C'$ točka,
 ki ne leži na premici $A'B'$ (Figure \ref{sl.aks.2.3.7.pic}).
 Po aksiomu \ref{aksIII2} obstaja ena sama izometrija $\mathcal{I}$, ki
 preslika točko $A$ v točko $A'$, poltrak $AB$ v poltrak $A'B'$
 in polravnino $ABC$ v polravnino $A'B'C'$. Ker je po predpostavki
 $(A,B)\cong (A',B')$ iz istega aksioma \ref{aksIII2}, sledi še
 $\mathcal{I}(B)=B'$.
 \kdokaz

Podoben je dokaz naslednjega izreka, ki bo kasneje v drugačni obliki
podan kot prvi izrek o skladnosti trikotnikov.



            \bizrek \label{IizrekABC} Let $(A,B,C)$ and $(A',B',C')$ be
            triplets of non-collinear points such that $$(A,B,C)\cong (A',B',C'),$$
            then there is a single isometry  $\mathcal{I}$, that maps the points
             $A$, $B$ and $C$ into the points $A'$, $B'$ and $C'$, i.e.:
            $$\mathcal{I}: A, B,C\mapsto A',B',C'.$$
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.5.pic}
\caption{} \label{sl.aks.2.3.5.pic}
\end{figure}


 \textbf{\textit{Proof.}}
 Po aksiomu \ref{aksIII2} obstaja ena sama izometrija $\mathcal{I}$, ki
 preslika točko $A$ v točko $A'$, poltrak $AB$ v poltrak $A'B'$
 in polravnino $ABC$ v polravnino $A'B'C'$ (Figure \ref{sl.aks.2.3.5.pic}).
  Ker je po predpostavki
 $(A,B,C)\cong (A',B',C')$ iz istega aksioma \ref{aksIII2}, sledi še
 $\mathcal{I}(B)=B'$ in $\mathcal{I}(C)=C'$.

  Potrebno je dokazati, da je $\mathcal{I}$ edina takšna izometrija.
  Predpostavimo, da obstaja takšna izometrija $\mathcal{\widehat{I}}$, da
  velja $\mathcal{\widehat{I}}: A, B,C\mapsto A',B',C'$. Po
  izreku \ref{izrekIzoB} izometrija $\mathcal{\widehat{I}}$
  tudi poltrak $AB$ preslika v poltrak $A'B'$ in polravnino $ABC$
  v polravnino $A'B'C'$. Iz aksioma \ref{aksIII2} sledi
   $\mathcal{\widehat{I}}=\mathcal{I}$.
 \kdokaz

Direktna posledica je naslednji izrek.


                \bizrek \label{IizrekABCident} Let $A$, $B$ and $C$ be three non-collinear points, then the identity map
                 $\mathcal{E}$ is the only isometry that maps points $A$, $B$, and $C$ to the same points
                $A$, $B$ and $C$.
                \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.5a.pic}
\caption{} \label{sl.aks.2.3.5a.pic}
\end{figure}


\textbf{\textit{Proof.}} (Figure \ref{sl.aks.2.3.5a.pic})

Najprej je identična preslikava $\mathcal{E}$, ki točke $A$, $B$
in $C$ preslika v  točke $A$, $B$ in $C$, izometrija po aksiomu
\ref{aksIII4}. Iz prejšnjega izreka \ref{IizrekABC} sledi, da je
takšna izometrija ena sama.
 \kdokaz

Za točko $A$ pravimo, da je \index{točka!fiksna} \pojem{fiksna
točka} (ali \index{točka!negibna} \pojem{negibna
točka}) izometrije $\mathcal{I}$, če velja $\mathcal{I}(A)=A$.
Prejšnji izrek nam pove, da so edine izometrije, ki imajo fiksne tri
nekolinearne točke, identitete.


 Izometrije bomo podrobneje obravnavali v poglavju
 \ref{pogIZO}, na tem mestu pa jih bomo uporabili predvsem za pomoč
 pri vpeljavi skladnosti likov. Dva lika $\Phi$ in $\Phi'$ sta
 \index{lika!skladna}\pojem{skladna}
 (označimo
 $\Phi\cong \Phi'$),
 če obstaja izometrija $I$, ki lik $\Phi$ preslika v lik $\Phi'$.

 Direktna posledica aksioma \ref{aksIII4} je naslednji izrek.


            \bizrek
             Congruence of figures is an equivalence relation. \label{sklRelEkv}
            \eizrek

\textbf{\textit{Proof.}}

\textit{Refleksivnost.} Za vsak lik $\Phi$ velja $\Phi \cong
\Phi$, ker je identična preslikava $\mathcal{E}$ izometrija
(aksiom \ref{aksIII4}) in $\mathcal{E}:\Phi\rightarrow\Phi$.

\textit{Simetričnost.} Iz $\Phi \cong \Phi_1$ sledi,  da obstaja
izometrija $\mathcal{I}$, ki preslika lik $\Phi$ v lik $\Phi_1$.
Inverzna preslikava $\mathcal{I}^{-1}$, ki je po aksiomu
\ref{aksIII4} izometrija, preslika lik $\Phi_1$ v lik $\Phi$,
zato velja $\Phi_1 \cong \Phi$.

\textit{Tranzitivnost.} Iz $\Phi \cong \Phi_1$ in $\Phi_1 \cong
\Phi_2$ sledi,  da obstajata takšni izometriji $\mathcal{I}$ in
$\mathcal{I}'$, da velja $\mathcal{I}:\Phi\rightarrow\Phi_1$ in
$\mathcal{I}':\Phi_1\rightarrow\Phi_2$.
 Potem  kompozitum $\mathcal{I}'\circ\mathcal{I}$,
  ki je po aksiomu \ref{aksIII4} izometrija, preslika lik $\Phi$
v lik $\Phi_2$, zato velja $\Phi \cong \Phi_2$.
\kdokaz



  Pojem skladnosti likov se nanaša tudi na daljice. Intuitivno
  smo skladnost daljic povezovali s skladnostjo parov točk.
  Sedaj bomo dokazali ekvivalentnost obeh relacij.

            \bizrek  \label{izrek(A,B)} $AB \cong A'B' \Leftrightarrow
            (A,B)\cong (A',B')$
             \eizrek

\textbf{\textit{Proof.}}

 ($\Rightarrow$) Če je $(A,B)\cong
(A',B')$, po izreku \ref{izrekAB} obstaja izometrija
$\mathcal{I}$, ki preslika točki $A$ in $B$ v točki $A'$ in
$B'$. Iz izreka \ref{izrekIzoB} sledi, da izometrija $\mathcal{I}$
preslika daljico $AB$ v daljico $A'B'$ oz. $AB \cong A'B'$.

($\Leftarrow$) Če je $AB \cong A'B'$, obstaja izometrija
$\mathcal{I}$, ki preslika daljico $AB$ v daljico $A'B'$. Po
posledici izreka \ref{izrekIzoB} se krajišče daljice preslika v
krajišče daljice. To pomeni, da velja bodisi
$\mathcal{I}:A,B\mapsto A',B'$ bodisi $\mathcal{I}:A,B\mapsto
B',A'$. Iz prve relacije sledi $(A,B)\cong (A',B')$ iz druge pa
$(A,B)\cong (B',A')$. Toda tudi iz drugega primera dobimo
$(A,B)\cong (A',B')$, kar je posledica aksiomov \ref{aksIII3} in
\ref{aksIII4}.
\kdokaz

 Zaradi prejšnjega izreka bomo v nadaljevanju namesto
  relacije $(A,B)\cong (A',B')$ vedno pisali $AB\cong
 A'B'$.


            \bizrek \label{ABnaPoltrakCX}
            For each line segment $AB$ and each ray $CX$, there is exactly
            one point $D$ on the ray
            $CX$ that $AB\cong CD$ holds.
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.5b.pic}
\caption{} \label{sl.aks.2.3.5b.pic}
\end{figure}



 \textbf{\textit{Proof.}} Naj bo $P$ točka, ki ne leži na premici $AB$,
 in $Q$ točka,
 ki ne leži na premici $CX$ (Figure \ref{sl.aks.2.3.5b.pic}).
  Po aksiomu \ref{aksIII2} obstaja ena sama
 izometrija $\mathcal{I}$, ki
 preslika točko $A$ v točko $C$, poltrak $AB$ v poltrak $CX$
 in polravnino $ABP$ v polravnino $CXQ$.
 Naj bo $D=\mathcal{I}(C)$, potem je $AB \cong CD$.

 Predpostavimo,
 da na poltraku $CX$ obstaja še ena točka $\widehat{D}$, za
 katero
 velja $AB \cong C\widehat{D}$. Ker poltraka
 $CX$ in $CD$ sovpadata, izometrija $\mathcal{I}$ pa preslika točko
 $A$ v točko $C$, poltrak $AB$ v poltrak $CD$
 in polravnino $ABP$ v polravnino $CDQ$,
 iz aksioma \ref{aksIII2} sledi $\mathcal{I}(C)=\widehat{D}$ oz.
 $\widehat{D}=D$.
 \kdokaz


                \bizrek \label{izomEnaC'} Let $A$, $B$, $C$ be three non-collinear points
                 and $A'$, $B'$ points of the edge of a half-plane $\pi$ such that $AB \cong A'B'$.
                  Then there is exactly one point $C'$ in the half-plane $\pi$ such that $AC \cong A'C'$ and $BC \cong B'C'$.
                 \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.11a.pic}
\caption{} \label{sl.aks.2.3.11a.pic}
\end{figure}


 \textbf{\textit{Proof.}} (Figure \ref{sl.aks.2.3.11a.pic})

 Po aksiomu \ref{aksIII2} obstaja ena sama
 izometrija $\mathcal{I}$, ki
 preslika točko $A$ v točko $A'$, poltrak $AB$ v poltrak $A'B'$
 in polravnino $ABC$ v polravnino $\pi$ ter velja $\mathcal{I}(B)=B'$.
 Naj bo $C'=\mathcal{I}(C)$, potem velja $AC \cong A'C'$ in
 $BC \cong B'C'$. Predpostavimo, da obstaja takšna točka
 $\widehat{C}'$, ki leži v polravnini $\pi$ ter velja $AC \cong A'\widehat{C}'$ in
 $BC \cong B'\widehat{C}'$. Ker je še $AB \cong
A'B'$, po izreku \ref{IizrekABC} obstaja ena sama izometrija
$\mathcal{\widehat{I}}$, ki preslika točke $A$, $B$ in $C$ v
točke $A'$, $B'$ in $\widehat{C}'$. Toda le-ta preslika tudi
poltrak $AB$ v poltrak $A'B'$ in polravnino $ABC$ v polravnino
$A'B'\widehat{C}'=\pi$. Po aksiomu \ref{aksIII2} je
$\mathcal{\widehat{I}}=\mathcal{I}$ in zato tudi
$\widehat{C}'=\mathcal{\widehat{I}}(C)=\mathcal{I}(C)=C'$.
 \kdokaz


            \bizrek \label{izoABAB} If $\mathcal{I}$ is an isometry that maps a points $A$ and $B$ into the same points
            $A$ and $B$ (i.e. $\mathcal{I}(A)=A$ and $\mathcal{I}(B)=B$), then it also holds for each point $X$ on the line
            $AB$ (i.e. $\mathcal{I}(X)=X$).
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.8.pic}
\caption{} \label{sl.aks.2.3.8.pic}
\end{figure}


%

\textbf{\textit{Proof.}} Označimo z $X$ poljubno točko premice
$AB$. Brez škode za splošnost predpostavimo, da točka $X$ leži
na poltraku $AB$ (Figure \ref{sl.aks.2.3.8.pic}).  Dokažimo, da
velja $\mathcal{I}(X)=X$.

Naj bo $P$ točka, ki ne leži na premici $AB$ in
$P'=\mathcal{I}(P)$. Izometrija $\mathcal{I}$
 preslika točko $A$ v točko $A$, poltrak $AB$ v poltrak $AB$
 (oz. poltrak $AX$ v poltrak $AX$)
 in polravnino $ABP$ v polravnino $ABP'$
 (oz. polravnino $AXP$ v polravnino $AXP'$).
 Po aksiomu \ref{aksIII2}
 iz $AX\cong AX$ sledi $\mathcal{I}(X)=X$.
 \kdokaz

 Vpeljimo nove pojme, ki se nanašajo na daljice.

Pravimo, da je daljica $EF$ \index{vsota!daljic}\pojem{vsota daljic}
$AB$ in $CD$, kar označimo $EF=AB+CD$, če obstaja takšna točka $P$
na daljici $EF$, da velja $AB \cong EP$ in $CD \cong PF$ (Figure
\ref{sl.aks.2.3.9.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.9.pic}
\caption{} \label{sl.aks.2.3.9.pic}
\end{figure}


Daljica $EF$ je \index{razlika!daljic}\pojem{razlika daljic} $AB$
in $CD$, kar označimo $EF=AB-CD$, če je $AB=EF+CD$ (Figure
\ref{sl.aks.2.3.9.pic}).

 Na podoben način lahko definiramo tudi
  množenje daljice z naravnim in s pozitivnim racionalnim
  številom. Za daljici $AB$ in $CD$ je $AB=n\cdot CD$
  ($n\in \mathbb{N}$), če  obstajajo takšne točke
  $X_1$, $X_2$,..., $X_{n-1}$, da je
  $\mathcal{B}(X_1,X_2,\ldots,X_{n-1})$ in
  $AX_1 \cong X_1X_2 \cong X_{n-1}B \cong CD$ (Figure
\ref{sl.aks.2.3.10.pic}).
  V tem primeru je tudi $CD=\frac{1}{n}\cdot AB$.

  Na tem mestu ne bomo formalno dokazovali dejstva, da za vsako daljico $PQ$ in vsako naravno število $n$ obstaja daljica $AB$, za katero je $AB=n\cdot PQ$, ter daljica $CD$, za katero je $CD=\frac{1}{n}\cdot PQ$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.10.pic}
\caption{} \label{sl.aks.2.3.10.pic}
\end{figure}


  Množenje daljice s pozitivnim
  racionalnim številom vpeljemo na naslednji način. Za
  $q=\frac{n}{m} \in \mathbb{Q^+}$ je:
$$q\cdot AB=\frac{n}{m}\cdot AB = n\cdot\left(\frac{1}{m}\cdot AB\right)$$

Če za točko $P$ daljice $AB$ velja $AP=\frac{n}{m}\cdot PB$,
pravimo, da točka $P$ deli daljico $AB$ v \index{razmerje}
\pojem{razmerju} $n:m$, kar zapišemo $AP:PB=n:m$.

Daljica $AB$ je \index{relacija!urejenosti daljic}\pojem{daljša}
od daljice $CD$, kar označimo $AB>CD$, če obstaja takšna točka
$P\neq B$ na daljici $AB$, da velja $CD \cong AP$ (Figure
\ref{sl.aks.2.3.11.pic}). V tem primeru pravimo tudi, da je
daljica $CD$ \pojem{krajša} od daljice $AB$ (oznaka $CD<AB$).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.11.pic}
\caption{} \label{sl.aks.2.3.11.pic}
\end{figure}

Ni težko dokazati, da za daljici $AB$ in $CD$ velja natanko ena
od relacij $AB>CD$ ali $AB<CD$ ali $AB \cong CD$. To je posledica
izreka \ref{ABnaPoltrakCX}.

Točka $S$ je \index{središče!daljice} \pojem{središče (razpolovišče) daljice} $AB$,
če leži na tej daljici in velja $AS \cong SB$ (Figure
\ref{sl.aks.2.3.12.pic}). Jasno je, da središče deli daljico v
razmerju $1:1$. Potrebno je še dokazati, da takšna točka vedno
obstaja.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.12.pic}
\caption{} \label{sl.aks.2.3.12.pic}
\end{figure}

                \bizrek
              For every line segment, there is exactly one midpoint.
                 \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.13.pic}
\caption{} \label{sl.aks.2.3.13.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bo $AB$ daljica in $C$ poljubna točka, ki ne leži na
 premici $AB$
(Figure \ref{sl.aks.2.3.13.pic}). Označimo s $\pi$ polravnino
$ABC$ in s $\pi'$ komplementarno polravnino polravnine $\pi$. Po
aksiomu \ref{aksIII2} obstaja ena sama
 izometrija $\mathcal{I}$, ki
 preslika točko $A$ v točko $B$, poltrak $AB$ v poltrak $BA$
 in polravnino $\pi$ v polravnino $\pi'$. Iz $AB\cong BA$ (posledica
 aksioma \ref{aksIII3}) po istem
 aksiomu sledi $\mathcal{I}(B)=A$.

 Naj bo $C'=\mathcal{I}(C)$, potem velja $AC \cong B'C'$ in
 $BC \cong A'C'$. Ker sta $C$ in $C'$ na različnih straneh premice
 $AB$, premica $CC'$ seka premico $AB$ v neki točki $S$.
 Če je $\widehat{C}=\mathcal{I}(C')$, velja $A'C' \cong B\widehat{C}$ in
 $B'C' \cong A\widehat{C}$. Ker je tudi $AC \cong B'C'$ in
 $BC \cong A'C'$, po izreku \ref{izomEnaC'} je $\widehat{C}=C$ oz.
 $\mathcal{I}(C')=C$. Torej izometrija $\mathcal{I}$ preslika premici $AB$
 in $CC'$ sami vase, zato je:
 $$\mathcal{I}(S)=\mathcal{I}(AB\cap CC')=
 \mathcal{I}(AB)\cap \mathcal{I}(CC')=
 AB\cap CC'=S.$$
 Sedaj iz $\mathcal{I}:A,S\mapsto B,S$ sledi $AS\cong SB$.

 Da bi dokazali, da je točka $S$ res središče daljice $AB$, je potrebno
 dokazati še, da točka $S$ leži na daljici $AB$. Predpostavimo
 nasprotno. Brez škode za splošnost naj bo $\mathcal{B}(A,B,S)$. Toda v
 tem primeru na poltraku $SA$ obstajata dve takšni točki $A$ in $B$,
 da velja $SA\cong SB$, kar nasprotuje izreku \ref{ABnaPoltrakCX}.

  Dokažimo še, da ima daljica eno samo središče. Naj bo
  $\widehat{S}\neq S$ točka daljice $AB$ in  $A\widehat{S}\cong
  \widehat{S}B$. Iz aksioma \ref{aksIII3} sledi
  $\mathcal{I}(A\widehat{S})=A\widehat{S}$. To pomeni (izrek
  \ref{izoABAB}), da  za vsako točko $X\in AB$ velja
  $\mathcal{I}(X)=X$ in tudi $\mathcal{I}(A)=A$, kar pa ni mogoče.
  Torej je $\widehat{S}= S$.
 \kdokaz

Pravimo, da je točka $A$ \index{simetričnost!glede na točko}\pojem{simetrična} točki $B$ glede na točko $S$, če je $S$ središče daljice $AB$. Simetričnost glede na preslikavo čez točko (t. i. središčno zrcaljenje) bomo
podrobneje obravnavali v razdelku \ref{odd6SredZrc}.

 Sedaj bomo vpeljali pojme in izpeljali lastnosti, ki se nanašajo
 na kote in so analogni tistim, ki smo jih vpeljali za daljice.
 Če se izrek \ref{ABnaPoltrakCX} intuitivno nanaša na prenos daljice s šestilom
  na
 poltrak, bo naslednji izrek predstavljal prenos kota k danemu
 poltraku.



                 \bizrek \label{KotNaPoltrak}
                 For each angle $\alpha$ and each ray $Sp$ lies on a line $p$,
                there is exactly one ray $Sq$ in one of the half-planes determined by the line $p$, such that
                $\alpha \cong \angle pSq$.
                \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.14.pic}
\caption{} \label{sl.aks.2.3.14.pic}
\end{figure}

 \textbf{\textit{Proof.}}
 Naj bo $\alpha=\angle BAC$ in $\pi'$ ena od polravnin, ki
  jo določa nosilka poltraka $Sp$ (Figure \ref{sl.aks.2.3.14.pic}).

 Po izreku \ref{ABnaPoltrakCX} obstaja
 ena sama točka $P$ na poltraku $Sp$, da velja $AB \cong SP$.
 Po aksiomu \ref{aksIII2} obstaja ena sama izometrija $\mathcal{I}$, ki
 preslika točko $A$ v točko $S$, poltrak $AB$ v poltrak $Sp$
 in polravnino $ABC$ v polravnino $\pi'$.
  Če je $Q=\mathcal{I}(C)$, se poltrak $AC$ s to izometrijo
  preslika v poltrak $SQ$. Zato poltrak $SQ=Sq$ leži v polravnini
  $\pi'$ in velja $\angle BAC\cong pSq$.

 Predpostavimo, da je tudi $S\widehat{q}$ poltrak, ki leži v polravnini
  $\pi'$ in velja $\angle BAC\cong pS\widehat{q}$. Iz definicije skladnosti
   sledi, da obstaja neka izometrija $\mathcal{\widehat{I}}$, ki
   preslika kot $BAC$ v kot $\angle BAC\cong pS\widehat{q}$. Ker
   tudi
   izometrija $\mathcal{\widehat{I}}$
 preslika točko $A$ v točko $S$, poltrak $AB$ v poltrak $Sp$
 in polravnino $ABC$ v polravnino $\pi'$, je po aksiomu
 \ref{aksIII2} $\mathcal{\widehat{I}}=\mathcal{I}$. Torej je
  $$S\widehat{q}=\mathcal{\widehat{I}}(AB)=\mathcal{I}(AB)=Sq,$$ kar je bilo potrebno dokazati. \kdokaz

 Ker nosilka poltraka $Sp$ iz prejšnjega izreka določa dve
 polravnini, obstajata dva kota s krakom $Sp$, ki sta skladna kotu
 $\alpha$. Omenjena kota sta različno orientirana. To pomeni, da ima
  za orientirani kot $\alpha$  le eden izmed teh dveh kotov isto
 orientacijo kot $\alpha$ (Figure \ref{sl.aks.2.3.15.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.15.pic}
\caption{} \label{sl.aks.2.3.15.pic}
\end{figure}


Podobno kot pri daljicah definiramo določene operacije in
relacije tudi med koti.

 Kot $pq$ z vrhom $S$ je \index{vsota!kotov}\pojem{vsota kotov} $ab$ in $cd$ oz.
 $\angle pq = \angle ab + \angle cd$, če obstaja poltrak
 $s=SX$, ki leži v kotu $pq$ ter velja $\angle ps \cong \angle ab$
 in $\angle sq \cong \angle cd$ (Figure \ref{sl.aks.2.3.16.pic}).
  V tem primeru pravimo tudi, da je
 kot $ab$ \index{razlika!kotov}\pojem{razlika kotov} $pq$ in $cd$, oz.
  $ \angle ab= \angle pq - \angle cd$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.16.pic}
\caption{} \label{sl.aks.2.3.16.pic}
\end{figure}

Analogno kot pri daljicah za kot $ab$ definiramo kote
$n\cdot \angle ab$ in  $\frac{1}{n}\cdot \angle ab$ ($n\in
\mathbb{N}$) ter $q\cdot \angle ab$ ($q\in \mathbb{Q}$).

Pravimo, da je kot $ab$ z vrhom $S$ \index{relacija!urejenosti
kotov}\pojem{večji} od kota $cd$ ($\angle ab > \angle cd$), če
obstaja v kotu $ab$ poltrak $s=SX$, da velja $\angle as \cong
\angle cd$ (Figure \ref{sl.aks.2.3.17.pic}). V tem primeru je tudi
kot $cd$ \pojem{manjši} od kota $ab$ ($\angle cd< \angle ab$). Ni
težko dokazati, da za dva kota $ab$ in $cd$ velja natanko ena od
relacij: $\angle ab > \angle cd$, $\angle ab < \angle cd$ ali
$\angle ab \cong \angle cd$.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.17.pic}
\caption{} \label{sl.aks.2.3.17.pic}
\end{figure}


Kota sta \index{kota!suplementarna}\pojem{suplementarna}, če je
njuna vsota enaka iztegnjenem kotu  (Figure
\ref{sl.aks.2.3.18.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.18.pic}
\caption{} \label{sl.aks.2.3.18.pic}
\end{figure}


Poltrak $s=SX$ je \index{bisektrisa kota}\pojem{bisektrisa kota}
$\angle pSq=\alpha$ (Figure \ref{sl.aks.2.3.19.pic}), če leži v tem kotu in
velja $\angle ps \cong \angle sq$. Nosilka te bisektrise  je \index{simetrala!kota}\pojem{simetrala kota} $pSq$ (premica $s_{\alpha}$).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.19.pic}
\caption{} \label{sl.aks.2.3.19.pic}
\end{figure}



Podobno kot za središče daljice velja za bisektriso kota naslednji izrek.

            \bizrek \label{izrekSimetralaKota}
             An angle has exactly one bisector.
             %(oz. eno samo simetralo).
            \eizrek

\textbf{\textit{Proof.}}
 Naj bo $\alpha=pSq$ poljubni kot, $P$ poljubna točka, ki leži na kraku
 $Sp$ ($P\neq S$) ter $Q$ točka, ki leži na kraku $Sq$ in velja
 $SP\cong SQ$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.20.pic}
\caption{} \label{sl.aks.2.3.20.pic}
\end{figure}



 Predpostavimo, da je kot $\alpha$ iztegnjeni kot
 (Figure \ref{sl.aks.2.3.20.pic}), ki določa
 polravnino $\pi$. Naj bo $A$ njena poljubna točka. Po izreku
 \ref{izomEnaC'} v polravnini $\pi$ obstaja ena sama točka $B$,
 da velja $(P,Q,A)\cong (Q,P,B)$. Iz izreka \ref{IizrekABC} sledi,
 da obstaja ena sama izometrija $\mathcal{I}$, ki točke $P$, $Q$ in
 $A$ preslika v točke $Q$, $P$ in $B$. Naj bo
 $\mathcal{I}(B)=\widehat{A}$. Ker je
 $(Q,P,B)\cong(P,Q,\widehat{A})$, je po izreku \ref{izomEnaC'}
 $\widehat{A}=A$. Torej:
  $$\mathcal{I}:P,Q,A,B\mapsto Q,P,B,A.$$
Zato se središči $S$ in $L$ daljic $PQ$ in $AB$ preslikata vase
(aksiom \ref{aksIII4}), kar potem velja tudi za poltrak $s=SL$ in
vsako njegovo točko (izrek \ref{izoABAB}). Torej izometrija
$\mathcal{I}$ preslika kot $pSs$ v kot $sSq$, zato
  je $pSs\cong sSq$ oz. poltrak $s$ je bisektrisa kota $pSq$.

  Dokažimo, da je $s$ edina bisektrisa kota $\alpha$. Naj bo
  $\widehat{s}=S\widehat{L}$
  poltrak, ki leži v kotu $\alpha$ in velja $pS\widehat{s}\cong
  \widehat{s}Sq$. Potem obstaja izometrija $\mathcal{\widehat{I}}$, ki
  preslika kot $pS\widehat{s}$ v kot $\widehat{s}Sq$. Ta izometrija
  preslika točko $S$ v točko $S$, poltrak $p$ v poltrak $q$ in
  polravnino $\pi$ v polravnino $\pi$, zato je po aksiomu
  \ref{aksIII2} $\mathcal{\widehat{I}}=\mathcal{I}$. Torej
  $\mathcal{I}(\widehat{s})=
  \mathcal{\widehat{I}}(\widehat{s})=\widehat{s}$. Če $\widehat{L} \notin
  s$, izometrija $\mathcal{I}$ preslika tri nekolinearne točke
  $S$, $L$ in $\widehat{L}$ vase in je $\mathcal{I}$ identična preslikava
  (izrek \ref{IizrekABCident}), kar ni mogoče. Torej $\widehat{L} \in
  s$ oz. $\widehat{s}=s$.


 Če je $\alpha$ neiztegnjeni konveksni kot  (Figure \ref{sl.aks.2.3.20.pic}),
  so točke $S$, $P$ in $Q$
 nekolinearne, zato po izreku \ref{IizrekABC} obstaja ena sama
 izometrija $\mathcal{I}$, ki  točke $P$, $S$ in $Q$ preslika v
 točke $Q$, $S$ in $P$. Z $L$ označimo središče daljice $PQ$.
 Po aksiomu \ref{aksIII3} je $\mathcal{I}(L)=L$. Potem se tudi vse
 točke poltraka $s=SL$ preslikajo vase (izrek \ref{izoABAB}). Kot
$\alpha$ je konveksni kot, kar pomeni, da točka $L$ in potem tudi
poltrak $s$ ležita v tem kotu.
 Torej izometrija $\mathcal{I}$ preslika kot $pSs$ v kot $sSq$, zato
  je $pSs\cong sSq$ oz. poltrak $s$ je bisektrisa kota $pSq$.

Na podoben način kot v prejšnjem primeru dokažemo, da kot
$\alpha$ nima drugih bisektris.

Če je $\alpha$ nekonveksni kot, bisektriso dobimo kot
komplementarni (dopolnilni) poltrak poltraka $s$.
 \kdokaz

Dokažimo dva izreka, ki se nanašata na sokote in sovršne kote.\index{kota!sokota} \index{kota!sovršna}



               \bizrek
              The adjacent supplementary angles  of two congruent angles are also congruent. \label{sokota}
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.20a.pic}
\caption{} \label{sl.aks.2.3.20a.pic}
\end{figure}



\textbf{\textit{Proof.}} Naj bosta $\alpha'=\angle P'OQ$ in $\alpha_1'=\angle P_1'O_1Q_1$ sokota
 dveh skladnih kotov $\alpha=\angle POQ$ in $\alpha_1=\angle P_1O_1Q_1$ (Figure \ref{sl.aks.2.3.20a.pic}). Po aksiomu \ref{aksIII2} obstaja ena sama izometrija $\mathcal{I}$, ki preslika točko $O$ v točko $O_1$, poltrak $OP$ v poltrak $O_1P_1$ in polravnino $POQ$ v polravnino $P_1O_1Q_1$. Naj bo $Q_2=\mathcal{I}(Q)$. Potem je $\angle P_1O_1Q_2\cong \angle POQ$. Izometrija $\mathcal{I}$ preslika polravnino $POQ$ v polravnino $P_1O_1Q_1$, zato točka $Q_2$ (in tudi poltrak $O_1Q_2$) leži v polravnini $P_1O_1Q_1$. Ker je po predpostavki še  $\angle POQ\cong\angle P_1O_1Q_1$, po izreku  \ref{KotNaPoltrak} $OQ_1$ in $OQ_2$ predstavljata isti poltrak. Torej točka $Q_2$ leži na poltraku $O_1Q_1$. Naj bo $P_2'=\mathcal{I}(P')$. Ker izometrije poltrak preslikajo v poltrak (izrek \ref{izrekIzoB}), leži točka $P_2'$ na poltraku $O_1P_1'$. Iz $\mathcal{I}:P',O,Q\mapsto P_2',O_1,Q_2$ sledi, da izometrija $\mathcal{I}$ preslika kot $P'OQ$ v kot $P_2'O_1Q_2$  (izrek \ref{izrekIzoB}), zato je
 $\angle P'OQ\cong \angle P_2'O_1Q_2=\angle P_1'O_1Q_1$.
\kdokaz


                \bizrek \label{sovrsnaSkladna}
               Vertical angles are congruent.
                \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.20b.pic}
\caption{} \label{sl.aks.2.3.20b.pic}
\end{figure}


\textbf{\textit{Proof.}} Naj bosta $\alpha=\angle POQ$ in $\alpha'=\angle P'OQ'$ sovršna kota, kjer so točke $P$, $O$, $P'$ (oz. $Q$, $O$, $Q'$) kolinearne (Figure \ref{sl.aks.2.3.20b.pic}). Kot $\beta=\angle QOP'$ je sokot za oba kota $\alpha$ in $\alpha'$. Ker je še $\beta\cong\beta$, je po prejšnjem izreku \ref{sokota} tudi $\alpha\cong\alpha'$.
\kdokaz



            \bizrek \label{sredZrcObstoj}
            For each point $S$ there exists an isometry $\mathcal{I}$ such that $\mathcal{I}(S)=S$.
            In addition, for each point $X\neq S$ the following holds:\\ if $\mathcal{I}(X)=X'$, then $S$ is the midpoint of the line segment $XX'$.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.20c.pic}
\caption{} \label{sl.aks.2.3.20c.pic}
\end{figure}


\textbf{\textit{Proof.}} Naj bo $P$ poljubna točka različna od $S$  (Figure \ref{sl.aks.2.3.20c.pic}). Po aksiomu \ref{AksII3} obstaja na premici $SP$ takšna točka $Q$, da velja $\mathcal{B}(P,S,Q)$. Označimo polravnini, ki ju določa rob $SP$ z $\alpha$ in $\alpha'$. Po aksiomu \ref{aksIII2} obstaja (ena sama) izometrija $\mathcal{I}$, ki preslika točko $S$ v točko $S$, poltrak $SP$ v poltrak $SQ$ in polravnino $\alpha$ v polravnino $\alpha'$.

Označimo s $p$ premico $SP$.
Točka $P'=\mathcal{I}(P)$ leži na poltraku $SQ$ oz. premici $p$. Ker je torej  $\mathcal{I}:S,P \mapsto S,P'$, se po aksiomu \ref{aksIII1} premica $SP$ preslika v premico $SP'$ oz. $\mathcal{I}:p\rightarrow p$.
Slika polravnine $\alpha'$ z robom $p$ je torej polravnina z istim robom (izrek \ref{izrekIzoB}). Ta polravnina ne more biti $\alpha'$, saj je izometrija  $\mathcal{I}$ bijektivna preslikavain po predpostavki  preslika polravnino  $\alpha$ v polravnino $\alpha'$.  Torej je $\mathcal{I}:\alpha'\rightarrow \alpha$.

Sedaj je jasno, da je brez škode za splošnost dovolj, če izpeljemo dokaz le za točke, ki ležijo v polravnini $\alpha$ (brez roba oz. le poltraka $SP$).

Naj bo $X\in \alpha\setminus p$ in $X'=\mathcal{I}(X)$. Takoj vidimo,da je $X'\in \alpha'\setminus p$. Po aksiomu \ref{AksII3} obstaja na premici $SX$ takšna točka $X_1$, da velja $\mathcal{B}(X,S,X_1)$. Ker sta $\angle PSX$ in $\angle P'SX_1$ sovršna kota, sta po izreku \ref{sovrsnaSkladna} tudi skladna. Toda iz $\mathcal{I}:S,P,X \mapsto S,P',X'$ sledi tudi
 $\angle PSX \cong \angle P'SX'$. Torej velja $\angle P'SX_1\cong \angle P'SX'$ (izrek \ref{sklRelEkv})), zato sta po izreku \ref{KotNaPoltrak} poltraka $SX_1$ in $SX'$ identična. To pomeni, da točka $X'$ leži na poltraku $SX_1$ oz. velja $\mathcal{B}(X,S,X')$. Ker je zaradi $\mathcal{I}:S,X \mapsto S,X'$ še $SX\cong SX'$, je po definiciji točka $S$ središče daljice $XX'$.

 Naj bo na koncu $Y$ poljubna točka poltraka $SP$, ki se razlikuje od točke $S$, in $Y'=\mathcal{I}(Y)$. Točka $Y'$ leži na poltraku $SQ$, zato je $\mathcal{B}(Y,S,Y')$. Ker je zaradi $\mathcal{I}:S,Y \mapsto S,Y'$ še $SY\cong SY'$, je po definiciji točka $S$ središče daljice $YY'$.
\kdokaz

V razdelku \ref{odd6SredZrc} bomo izometrijo, ki je omenjena v prejšnjem izreku \ref{sredZrcObstoj}, posebej obravnavali.


 Definirajmo nove vrste kotov.
 Konveksni kot je \index{kot!ostri}\pojem{ostri kot}, \index{kot!pravi}
 \pojem{pravi kot} oz.
 \index{kot!topi}\pojem{topi kot}, če je
 manjši, enak oz. večji od svojega sokota (Figure \ref{sl.aks.2.3.21.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.21.pic}
\caption{} \label{sl.aks.2.3.21.pic}
\end{figure}



Iz definicije sledi, da so ostri (oz. topi) koti tisti konveksni
koti, ki so manjši (oz. večji) od pravega kota.

Iz izreka \ref{izrekSimetralaKota} sledi, da pravi kot
obstaja, saj bisektrisa iztegnjeni kot razdeli na dva skladna
sokota.

Ni težko dokazati, da sta vsaka dva prava kota skladna ter da je
kot, ki je skladen s pravim kotom, tudi pravi kot.

Če je vsota dveh kotov  pravi kot, pravimo, da sta kota
\index{kota!komplementarna}\pojem{komplementarna} (Figure
\ref{sl.aks.2.3.22.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.22.pic}
\caption{} \label{sl.aks.2.3.22.pic}
\end{figure}



Sedaj bomo vpeljali izjemno pomembno relacijo med premicama. Če
premici $p$ in $q$ vsebujeta kraka pravega kota, pravimo, da sta
$p$ in $q$ \pojem{pravokotni}, kar označimo $p \perp q$ (Figure
\ref{sl.aks.2.3.23.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.23.pic}
\caption{} \label{sl.aks.2.3.23.pic}
\end{figure}

Iz same definicije je jasno, da je pravokotnost simetrična relacija
oz. iz $p \perp q$ sledi $q \perp p$. Če je $p \perp q$ in $p \cap q=S$,
pravimo, da je premica $p$
\index{pravokotni!premici}\pojem{pravokotna} na premico $q$ v točki
$S$ oz. da je $p$ \index{pravokotnica}\pojem{pravokotnica}
premice $q$ v tej točki.



Naslednji izrek je najpomembnejši izrek, ki karakterizira relacijo
pravokotnosti.



                \bizrek \label{enaSamaPravokotnica}
                For each point $A$ and each line $p$, there is a unique line $n$
            going through the point $A$, which is perpendicular on the line $p$.
                \eizrek

\textbf{\textit{Proof.}}
Predpostavimo, da točka $A$ ne leži na premici $p$. Naj bosta
$B$ in $C$ poljubni točki, ki ležita na premici $p$
 (Figure \ref{sl.aks.2.3.24.pic}). S $\pi$ označimo polravnino $BCA$,
komplementarno polravnino pa s $\pi_1$. Po izreku \ref{izomEnaC'}
obstaja ena sama točka $A_1\in \pi_1$, za katero velja $(A,B,C)
\cong (A_1,B,C)$. Iz izreka \ref{IizrekABC} sledi, da obstaja ena
sama izometrija $\mathcal{I}$, ki preslika točke $A$, $B$ in $C$
v točke $A_1$, $B$ in $C$. Premico $AA_1$ označimo z $n$. Ker
sta $A$ in $A_1$ na različnih bregovih premice $p$, premica $n$
seka premico $p$ v neki točki $S$. Iz $\mathcal{I}:B,C \mapsto
B,C$ sledi $\mathcal{I}(S)=S$ (izrek \ref{izoABAB}). Torej
izometrija $\mathcal{I}$ preslika kot $ASB$ v kot $A_1SB$. Sledi,
da sta $\angle ASB$ in $\angle A_1SB$ skladna sokota, zato sta
tudi prava kota. Torej je $n \perp p$.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.24.pic}
\caption{} \label{sl.aks.2.3.24.pic}
\end{figure}

Dokažimo, da je $n$ edina pravokotnica premice $p$ skozi točko
$A$. Naj bo $\widehat{n}$ premica, za katero je tudi $A\in
\widehat{n}$ in $\widehat{n} \perp p$. Naj bo točka $\widehat{S}$
presečišče premic $\widehat{n}$ in $p$. Po predpostavki je
$\angle A\widehat{S}B$ pravi kot in je skladen s svojim sokotom
$\angle B\widehat{S}A_2$ ($A_2$ je takšna točka, da velja
$\mathcal{B}(A,\widehat{S},A_2)$), ki je tudi pravi kot.

Iz $\mathcal{I}:B,C \mapsto B,C$ sledi
$\mathcal{I}(\widehat{S})=\widehat{S}$ (izrek \ref{izoABAB}).
Torej izometrija $\mathcal{I}$ preslika kot $A\widehat{S}B$ v kot
$A_1\widehat{S}B$. Sledi, da sta $\angle A\widehat{S}B$ in $\angle
A_1\widehat{S}B$ skladna, zato je tudi $\angle A_1\widehat{S}B$
pravi kot. Torej sta kota $A_1\widehat{S}B$ in $A_2\widehat{S}B$
prava kota in sta zato skladna. Iz tega sledi, da sta poltraka
$\widehat{S}A_1$ in $\widehat{S}A_2$ ista, zato je $A_1 \in
\widehat{S}A_2=\widehat{n}$ oz. $\widehat{n}=AA_1=n$.

 V primeru, ko točka $A$ leži na premici $p$, je pravokotnica $n$
 simetrala pripadajočega iztegnjenega kota (izrek \ref{izrekSimetralaKota}).
\kdokaz


Prejšnji izrek ima za posledico zelo pomembno dejstvo - obstoj parov disjunktnih premic v ravnini - oz. takšnih, ki nimata skupnih točk. To je vsebina naslednjih dveh izrekov.


            \bizrek \label{absolGeom1}
             Let $p$ and $q$ be a lines perpendicular on a line $PQ$ in the points $P$ and $Q$.
            Then the lines $p$ and $q$ do not have a common points i.e. $p\cap q=\emptyset$.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.25b.pic}
\caption{} \label{sl.aks.2.3.25b.pic}
\end{figure}

\textbf{\textit{Proof.}} Izrek je direktna posledica prejšnjega izreka \ref{enaSamaPravokotnica}. Če bi se namreč premici $p$ in $q$ sekali v neki točki $S$, bi iz točke $S$ imeli dve pravokotnici na premico $PQ$ (Figure \ref{sl.aks.2.3.25b.pic}), kar je v protislovju z omenjenim izrekom.
 \kdokaz



            \bizrek \label{absolGeom}
            If $A$ is a point that does not lie on a line $p$, then there exists at least
            one line (in the same plane) passing through the point $A$ and not intersecting the line
            $p$ (Figure \ref{sl.aks.2.3.25a.pic}).
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.25a.pic}
\caption{} \label{sl.aks.2.3.25a.pic}
\end{figure}


\textbf{\textit{Proof.}} Po izreku \ref{enaSamaPravokotnica} obstaja (natanko ena) pravokotnica $n$ premice $p$, ki poteka skozi točko $A$. Označimo z $A'$ presečišče premic $p$ in $n$. Iz istega izreka sledi, da obstaja še pravokotnica $q$ premice $n$ v točki $A$. Po prejšnjem izreku \ref{absolGeom1} je $q$ premica, ki poteka skozi točko $A$ in nima skupnih točk s premico $p$.
 \kdokaz


Točka $A'$ je \index{nožišče}\pojem{nožišče} ali
\index{pravokotna projekcija}\pojem{pravokotna projekcija} točke
$A$ na premico $p$, če pravokotnica premice $p$ skozi točko $A$
seka to premico v točki $A'$. Označili jo bomo  z $A'=pr_{\perp
p}(A)$ (Figure \ref{sl.aks.2.3.25.pic}).
 Iz prejšnjega izreka sledi, da za vsako točko in premico
 obstaja ena sama pravokotna projekcija.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.25.pic}
\caption{} \label{sl.aks.2.3.25.pic}
\end{figure}

Premico, ki poteka skozi središče $S$ daljice $AB$ in je pravokotna
na premico $AB$, imenujemo \index{simetrala!daljice}\pojem{simetrala daljice} $AB$ in jo označimo s $s_{AB}$
(Figure \ref{sl.aks.2.3.26.pic}). Lastnosti simetrale daljice bomo
obravnavali v naslednjem poglavju.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.26.pic}
\caption{} \label{sl.aks.2.3.26.pic}
\end{figure}


Pravimo, da je točka $A$ \index{simetričnost!glede na premico}\pojem{simetrična} točki $B$ glede na premico $s$, če je $s$ simetrala daljice $AB$. Simetričnost glede na premico (kot preslikavo - t. i. osno zrcaljenje) bomo podrobneje obravnavali v razdelku \ref{odd6OsnZrc}.

Naj bo $S$ točka in $AB$ daljica. Množico vseh točk $X$, za
katere velja $SX \cong AB$, imenujemo
\index{krožnica}\pojem{krožnica} s
\index{središče!krožnice}\pojem{središčem} $S$ in \index{polmer
krožnice}\pojem{polmerom} $AB$; označimo jo s $k(S,AB)$ (Figure
\ref{sl.aks.2.3.27.pic})  oz.:
 $$k(S,AB)=\{X;\hspace*{1mm}SX \cong AB\}.$$


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.27.pic}
\caption{} \label{sl.aks.2.3.27.pic}
\end{figure}

 Seveda je krožnica množica
 točk v ravnini, ker v tej knjigi obravnavamo le ravninsko
 geometrijo (vse točke in vsi liki pripadajo isti ravnini).

 Iz definicije je jasno, da za polmer lahko izberemo poljubno daljico,
 ki je skladna z
daljico $AB$, torej katerokoli daljico $SP$, kjer je $P$ poljubna
točka na krožnici. Ker polmer ni vezan na
določeno daljico, ga običajno označujemo z malo črko $r$. Torej lahko krožnico zapišemo tudi takole:
 $$k(S,r)=\{X;\hspace*{1mm}SX \cong r\}.$$
 Množico

$$\{X;\hspace*{1mm}SX \leq r\}$$
imenujemo \index{krog}\pojem{krog} s središčem $S$ in polmerom $r$ (Figure \ref{sl.aks.2.3.28.pic}) označimo ga s $\mathcal{K}(S,r)$.
Množica
 $$\{X;\hspace*{1mm}SX < r\}$$
 je \index{notranjost!kroga}
 \pojem{notranjost kroga} $\mathcal{K}(S, r)$, njene točke so pa
 \pojem{notranje točke kroga}.
 To pomeni, da je krog pravzaprav unija svoje notranjosti in pripadajoče krožnice.

Množico
 $$\{X;\hspace*{1mm}SX > r\}$$
 imenujemo \index{zunanjost!kroga}\pojem{zunanjost kroga} $\mathcal{K}(S, r)$
  in njene točke \pojem{zunanje točke kroga}.

 Iz praktičnih razlogov bomo notranjost kroga $\mathcal{K}(S, r)$ imenovali tudi \index{notranjost!krožnice}\pojem{notranjost} pripadajoče krožnice $k(S,r)$, zunanjost kroga $\mathcal{K}(S, r)$ pa  \index{zunanjost!krožnice}\pojem{zunanjost} pripadajoče krožnice $k(S,r)$. Enako definiramo tudi \pojem{notranje} oz. \pojem{zunanje} točke krožnice.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.28.pic}
\caption{} \label{sl.aks.2.3.28.pic}
\end{figure}

  Če sta $P$ in $Q$ dve točki krožnice $k(S, r)$, daljico $PQ$
   imenujemo \index{tetiva krožnice} \pojem{tetiva} te
  krožnice. Če
tetiva vsebuje središče krožnice, jo imenujemo
\index{premer krožnice}\pojem{premer} ali \index{diameter
krožnice}\pojem{diameter} te krožnice (Figure
\ref{sl.aks.2.3.29.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.29.pic}
\caption{} \label{sl.aks.2.3.29.pic}
\end{figure}

Dokažimo naslednji izrek.


             \bizrek \label{premerInS}
            The centre $S$ of the circle $k(S, r)$ is at the same time the midpoint of each
            diameter of that circle.
            \eizrek

\textbf{\textit{Proof.}}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.30.pic}
\caption{} \label{sl.aks.2.3.30.pic}
\end{figure}

 Če je $PQ$ premer  krožnice $k(S, r)$, točki $P$ in $Q$ ležita na
krožnici, kar pomeni: $SP \cong SQ \cong r$ (Figure
\ref{sl.aks.2.3.30.pic}). Ker točka $S$ leži na daljici $PQ$,
sledi, da je točka $S$ središče te daljice.
 \kdokaz

 Iz prejšnjega izreka sledi, da je premer enak dvema polmeroma, ker je:
$PQ = PS + SQ = 2\cdot PS = 2\cdot r$. To pa pomeni,
da so vsi premeri neke krožnice med seboj skladni.


Naj bosta $P$ in $Q$ poljubni točki krožnice  $k(S, r)$. Presek
krožnice $k$ z eno od polravnin (v ravnini te krožnice) z robom
$s=PQ$ imenujemo \index{krožni!lok} \pojem{krožni lok} $PQ$ (ali
krajše \pojem{lok}) s krajiščema $P$ in $Q$.

Torej vsaka tetiva $PQ$ na neki krožnici $k$ določa dva loka. Predpostavimo, da središče $S$ ne leži na robu polravnine, ki generira krožni lok.
Če ta polravnina
vsebuje središče $S$ krožnice $k$,
gre za \pojem{veliki lok} $PQ$, sicer je to \pojem{mali
lok} $PQ$.
 Če pa je
  središče $S$ na samem robu $PQ$ polravnine, potem je vsak od obeh lokov $PQ$
 \index{polkrožnica}\pojem{polkrožnica} $PQ$ (Figure
\ref{sl.skk.4.2.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.1.pic}
\caption{} \label{sl.skk.4.2.1.pic}
\end{figure}

Ker lok le s svojima krajiščema ni enolično določen, moramo na krožnici poznati še
vsaj eno točko, ki temu loku pripada oz. ne pripada.

Na podoben način definiramo tudi določene dele kroga.

Naj bosta $P$ in $Q$ poljubni točki krožnice  $k(S, r)$. Presek
kroga $\mathcal{K}(S, r)$ z eno od polravnin (v ravnini te krožnice) z robom
$s=PQ$ imenujemo
\index{krožni!odsek} \pojem{krožni odsek}.
 Torej vsaka tetiva $PQ$ na neki krožnici $k(S, r)$ določa na krogu $\mathcal{K}(S, r)$ dva krožna odseka. Predpostavimo, da središče $S$ ne leži na robu polravnine, ki generira krožni odsek.
Če ta polravnina
vsebuje  središče $S$ krožnice $k$,
gre za \pojem{večji krožni odsek} $PQ$, sicer pa za \pojem{manjši
krožni odsek} $PQ$.
 Če je
  središče $S$ na samem robu $PQ$ polravnine, potem je vsak od obeh krožnih odsekov
\index{polkrog}\pojem{polkrog}.
 Iz definicije je jasno, da je rob krožnega odseka unija tetive $PQ$ in ustreznega loka (Figure
\ref{sl.skk.4.2.1b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.1b.pic}
\caption{} \label{sl.skk.4.2.1b.pic}
\end{figure}


Definirajmo še en pojem, ki je povezan s krogom.
Naj bosta $P$ in $Q$ poljubni točki krožnice  $k(S, r)$. Presek
kroga $\mathcal{K}(S, r)$ z enim od kotov $PSQ$ imenujemo
\index{krožni!izsek} \pojem{krožni izsek}. Tudi v tem primeru imamo dva krožna izseka. Če je kot $PSQ$ iztegnjeni kot, dobimo dva polkroga, sicer pa konveksni in nekonveksni krožni izsek, odvisno od tega, ali je kot $PSQ$ konveksen ali nekonveksen (Figure
\ref{sl.skk.4.2.1c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.1c.pic}
\caption{} \label{sl.skk.4.2.1c.pic}
\end{figure}





%________________________________________________________________________________
 \poglavje{Continuity Axiom} \label{odd2AKSZVE}

 Že v osnovni šoli smo pri uvajanju številske premice in
 koordinatnega sistema izvedeli,
 da je možno
vzpostaviti povezavo, pri kateri vsaki točki neke premice pripada
določeno realno število in obratno, vsakemu realnemu številu lahko
priredimo točko, ki leži na tej premici. S tem je povezan naslednji
aksiom.

 \baksiom \label{aksDed}\index{aksiom!Dedekindov}
  (Dedekind’s\footnote{\index{Dedekind, R.}
 \textit{R. Dedekind} (1831--1916),
 nemški matematik.}
  axiom)
  Suppose that all points on open line segment $AB$ are divided into the union of two nonempty disjoint sets $\mathcal{U}$ and
$\mathcal{V}$ such that no point of $\mathcal{U}$ is
  between two points of  $\mathcal{V}$ and vice versa: no point of $\mathcal{V}$ is
  between two points of  $\mathcal{U}$. Then there is a unique point $C$ on open line segment $AB$ such that
  $B(A',C,B')$ for any two points $A'\in
\mathcal{U}\setminus{C}$ and $B'\in \mathcal{V} \setminus {C}$
(Figure \ref{sl.aks.2.4.1.pic}).
 \eaksiom


\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.1.pic}
\caption{} \label{sl.aks.2.4.1.pic}
\end{figure}

Povejmo brez dokazov dve pomembni posledici aksioma
zveznosti\footnote{Vse do 19. stoletja matematiki niso
čutili potrebe, da bi dokazali ti dve trditvi, oz. potrebe za
uvajanjem aksioma zveznosti. Celo \index{Evklid} Evklid iz
Aleksandrije (3. stol. pr. n. š.) v svojem znanem delu
‘‘Elementi’’, navaja konstrukcijo enakostraničnega trikotnika, pri kateri ne
dokazuje, da se določeni krožnici sekata.}.



             \bizrek \label{DedPoslKrozPrem} Let $k$ be a circle and $P$ a point inside that circle.
            Then any line $p$ passing through the point $P$ and the circle $k$ has exactly two common points (Figure
            \ref{sl.aks.2.4.2.pic}).
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.2.pic}
\caption{} \label{sl.aks.2.4.2.pic}
\end{figure}



            \bizrek \label{DedPoslKrozKroz} If $k$ and $l$ are circles such that $l$ contains at least one point inside and one point outside $k$,
             then the circles has exactly two points (Figure \ref{sl.aks.2.4.3.pic}).
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.3.pic}
\caption{} \label{sl.aks.2.4.3.pic}
\end{figure}

Dedekindov aksiom se v nekoliko drugačni obliki uporablja pri
zasnovi množice realnih števil. To nas spominja na že omenjeno
povezavo med množico točk neke premice in množico realnih števil.

Operacijo množenja daljice $AB$ s poljubnim
pozitivnim racionalnim številom $q$ smo že definirali. Sedaj lahko razširimo pojem
množenja za poljubno pozitivno realno število $\lambda$. Definicija daljice
$\lambda\cdot AB$, ($\lambda \in \mathbb{R}^+$), ki jo tu formalno ne
bomo izpeljali do konca, je povezana z dvema množicama točk
na poltraku $CD$:
 \begin{eqnarray*}
&& \{X\in CD;\hspace*{1mm}CX=q\cdot
AB,\hspace*{1mm}q\leq\lambda,\hspace*{1mm}q\in
\mathbb{Q}^+ \} \hspace*{1mm}\textrm{ in}\\
&& \{X\in CD;\hspace*{1mm}CX=q\cdot
AB,\hspace*{1mm}q>\lambda,\hspace*{1mm}q\in \mathbb{Q}^+ \}
 \end{eqnarray*}
 ter
Dedekindovim aksiomom \ref{aksDed}.

 S pomočjo aksioma zveznosti \ref{aksDed} lahko vpeljemo tudi
 pojme merjenja daljic in kotov.

 Pri merjenju daljic bomo vsaki daljici $AB$ priredili
 pozitivno realno  število $\textsl{m}(AB)$ na naslednji način.
  Naj bo $\mathcal{D}$ množica vseh daljic in $\mathbb{R}^+$ množica vseh pozitivnih realnih števil. Preslikavo $\textsl{m}:\mathcal{D}\rightarrow\mathbb{R}^+$, ki izpolnjuje naslednje lastnosti:
  \begin{itemize}
    \item $(\exists A_0B_0\in\mathcal{D})\hspace*{1mm}\textsl{m}(A_0B_0)=1$,
    \item $(\forall AB, CD\in\mathcal{D})\hspace*{1mm}(AB\cong CD \Rightarrow\textsl{m}(AB)=\textsl{m}(CD))$,
    \item $(\forall AB, CD, EF\in\mathcal{D})\hspace*{1mm}(AB+CD=EF\Rightarrow \textsl{m}(AB)+\textsl{m}(CD)=\textsl{m}(EF))$,
  \end{itemize}
  imenujemo \index{dolžina!daljice}\pojem{dolžina daljice} ali \index{mera!daljice}\pojem{mera daljice}, trojico $\textsl{M}=(\mathcal{D},\mathbb{R}^+,\textsl{m})$ pa \index{sistem merjenja!daljic}\pojem{sistem merjenja daljic}.

  Dolžino daljice $AB$ (oz. $\textsl{m}(AB)$) bomo navadno označevali z $|AB|$.

  Intuitivno je jasno, da obstaja neskončno mnogo sistemov merjenja, ki pa so odvisni od izbire enotske daljice $A_0B_0$ - tiste, ki ima dolžino enako 1, oz. $\textsl{m}(A_0B_0)=1$. V nekem sistemu merjenja je torej dolžina poljubne daljice $AB$ predstavljena s pozitivnim realnim  številom $x$, za katerega je $AB=x\cdot A_0B_0$. Torej je $\textsl{m}(AB)=x$ natanko tedaj, ko je $AB=x\cdot A_0B_0$ (Figure \ref{sl.aks.2.4.4.pic}). Sedaj je jasno, zakaj potrebujemo aksiom zveznosti - brez njega bi imeli težave z definicijo dolžine diagonale kvadrata, ki ima za stranico enotsko daljico (dolžine 1)\footnote{Stari Grki so si dolžino vedno predstavljali kot  racionalno število, zato so stranico
in diagonalo kvadrata imenovali \pojem{neprimerljivi daljici}.}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.4.pic}
\caption{} \label{sl.aks.2.4.4.pic}
\end{figure}


        \bizrek \label{meraDalj1}
        Za poljuben sistem merjenja daljic velja:

          (\textit{i}) $AB<CD\Rightarrow |AB|<|CD|$;

          (\textit{ii}) $|AB|=|CD|\Rightarrow AB\cong CD$.
        \eizrek

    \textbf{\textit{Proof.}}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.5.pic}
\caption{} \label{sl.aks.2.4.5.pic}
\end{figure}

          (\textit{i}) Iz $AB<CD$ sledi, da na daljici $CD$ obstaja takšna točka $T$, da velja $CT\cong AB$. Ker je $\mathcal{B}(C,T,D)$, je jasno $CD=CT+TD$ (Figure \ref{sl.aks.2.4.5.pic}). Iz definicije mere je potem: $|CD|=|CT|+|TD|=|AB|+|TD|>|AB|$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.6.pic}
\caption{} \label{sl.aks.2.4.6.pic}
\end{figure}

    (\textit{ii}) Predpostavimo, da ni $AB\cong CD$. Brez škode za splošnost naj bo $AB<CD$. Toda v tem primeru iz dokazanega (\textit{i}) sledi $|AB|<|CD|$, kar je v protislovju s predpostavko $|AB|=|CD|$. Torej velja $AB\cong CD$ (Figure \ref{sl.aks.2.4.6.pic}).
    \kdokaz

Ker sta po definiciji dolžine in prejšnjem izreku \ref{meraDalj1} daljici skladni natanko tedaj, ko imata enako dolžino, bomo pri krožnici $k(S,r)$  na njen \index{polmer krožnice}polmer $r$ pogosto gledali kot na dolžino tega polmera.

Naslednji izrek bomo podali brez dokaza.

            \bizrek \label{meraDaljice}
            Naj bo $\textsl{m}:\mathcal{D}\rightarrow\mathbb{R}^+$ mera daljice. Preslikava $\textsl{m}_1:\mathcal{D}\rightarrow\mathbb{R}^+$ tudi predstavlja  mero natanko tedaj, ko obstaja takšno pozitivno realno število $\mu$, da za vsako daljico $AB$ velja:
            $$\textsl{m}_1(AB)=\mu\cdot\textsl{m}(AB).$$
            \eizrek

Mera daljice nam omogoča definicijo novega pojma.
 \index{razmerje!daljic}\pojem{Razmerje daljic} $AB$ in $CD$ z oznakama $AB:CD$ oz. $\frac{AB}{CD}$ je količnik dolžin teh dveh daljic (Figure \ref{sl.aks.2.4.7a.pic}). Torej:
  $$AB:CD=\frac{AB}{CD}=\frac{|AB|}{|CD|}.$$

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.7a.pic}
\caption{} \label{sl.aks.2.4.7a.pic}
\end{figure}

  Jasno je, da mora biti razmerje dveh daljic vedno isto število, neodvisno od sistema merjenja.

 Korektnost prejšnje definicije bomo torej potrdili z naslednjim izrekom.

            \bizrek
            Razmerje dveh daljic ni odvisno od sistema merjenja.
            \eizrek


    \textbf{\textit{Proof.}} Naj bosta $(\mathcal{D},\mathbb{R}^+,\textsl{m})$ in $(\mathcal{D},\mathbb{R}^+,\textsl{m}_1)$ dva sistema merjenja. Po prejšnjem izreku \ref{meraDaljice} obstaja nek $\mu\in\mathbb{R}^+$, da je $\textsl{m}_1(PQ)=\mu\cdot\textsl{m}(PQ)$ za poljubno daljico $PQ$. Za poljubni daljici $AB$ in $CD$ zato velja:
     $$\frac{\textsl{m}_1(AB)}{\textsl{m}_1(CD)}=
     \frac{\mu\cdot\textsl{m}(AB)}{\mu\cdot\textsl{m}(CD)}=
     \frac{\textsl{m}(AB)}{\textsl{m}(CD)},$$ kar je bilo treba dokazati. \kdokaz


 Pojem delitve daljice v danem razmerju lako razširimo, tako da bo razmerje pozitivno realno število.
  Pravimo, da točka $T$ deli daljico $AB$ v \index{delitev daljice!v razmerju}\pojem{razmerju} $\lambda \in \mathbb{R}^+$, če je $\mathcal{B}(A,T,B)$ in $\frac{AT}{TB}=\lambda$ (Figure \ref{sl.aks.2.4.7.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.7.pic}
\caption{} \label{sl.aks.2.4.7.pic}
\end{figure}

 Enakost dveh razmerij bomo imenovali \pojem{sorazmerje}. Torej so daljice $AB$, $CD$, $EF$ in $GH$ (v tem vrstnem redu)  sorazmerne, če je:
  $$\frac{AB}{CD}=\frac{EF}{GH}.$$


Na podoben način definiramo tudi mero kota.

  Naj bo $\mathcal{K}$ množica vseh kotov in $\mathbb{R}^+$ množica vseh realnih pozitivnih števil. Preslikavo $\textsl{l}:\mathcal{K}\rightarrow\mathbb{R}^+$, ki izpolnjuje naslednje lastnosti:
  \begin{itemize}
    \item $(\exists \alpha_0\in\mathcal{K})\hspace*{1mm}\textsl{l}(\alpha_0)=1$,
    \item $(\forall \alpha, \beta\in\mathcal{K})\hspace*{1mm}(\alpha\cong \beta \Rightarrow\textsl{l}(\alpha)=\textsl{l}(\beta))$,
    \item $(\forall \alpha, \beta, \gamma\in\mathcal{K})\hspace*{1mm}(\alpha+\beta=\gamma\Rightarrow \textsl{l}(\alpha)+\textsl{l}(\beta)=\textsl{l}(\gamma))$.
  \end{itemize}
  imenujemo \index{mera!kota}\pojem{mera kota}, trojico $\textsl{L}=(\mathcal{K},\mathbb{R}^+,\textsl{l})$ pa \index{sistem merjenja!kotov}\pojem{sistem merjenja kotov}.

  Dejstvo, da je mera kota $\alpha$ enaka $x$ (oz. $\textsl{l}(\alpha)=x$) bomo bolj pogosto zapisali v obliki $\alpha=x$.


  Podobno kot pri merjenju daljic obstaja neskončno mnogo sistemov merjenja kotov, ki pa so odvisni od enotskega kota $\alpha_0$ - tistega, za katerega je mera enaka 1, oz. $\textsl{l}(\alpha_0)=1$. Tako je v nekem sistemu merjenja mera poljubnega kota $\alpha$  pozitivno realno  število $x$, za katero je $\alpha=x\cdot \alpha_0$. Torej je $\textsl{l}(\alpha)=x$ natanko tedaj, ko je $\alpha=x\cdot \alpha_0$. Seveda moramo tudi v tem primeru  uporabiti aksiom zveznosti, da lahko vpeljemo množenje kota s pozitivnim realnim številom.

  Od vseh sistemov merjenja bomo izpostavili dva.
  \begin{itemize}
    \item Pri prvem sistemu, ki ga bomo uporabljali najpogosteje, je enotski kot 180-ti del iztegnjenega kota. Za ta kot bomo rekli, da meri \pojem{eno kotno stopinjo} in to mero označili z $1^0$ (Figure \ref{sl.aks.2.4.8.pic}). Če torej uporabimo lastnosti funkcije mere $\textsl{l}$,  v tem sistemu iztegnjeni kot meri $180^0$, pravi kot pa $90^0$.
    \item V drugem sistemu merjenja z \pojem{radiani}, z oznako $[\textrm{rad}]$, meri iztegnjeni kot $\pi$ (kjer je $\pi$ iracionalno število - $\pi\doteq 3,14$), pravi kot pa $\frac{\pi}{2}$. V tem sistemu merjenja kotov oznake $[\textrm{rad}]$ ponavadi ne pišemo.
  \end{itemize}


\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.8.pic}
\caption{} \label{sl.aks.2.4.8.pic}
\end{figure}

  Torej lahko v obeh sistemih mero iztegnjenega kota $\alpha$  zapišemo  $\alpha=180^0=\pi$, pravega kota $\beta$ pa $\beta=90^0=\frac{\pi}{2}$ (Figure \ref{sl.aks.2.4.8a.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.8a.pic}
\caption{} \label{sl.aks.2.4.8a.pic}
\end{figure}

Splošno zvezo med obema sistemoma merjenja kotov lahko zapišemo s formulama:

$$1\hspace*{1mm}\textrm{rad}=\frac{180^0}{\pi}, \textrm{ oz. }
1^0=\frac{\pi}{180^0}\hspace*{1mm}\textrm{rad}.$$



%________________________________________________________________________________
 \poglavje{Playfair's Axiom} \label{odd2AKSVZP}


Kot posledico aksiomov prejšnjih štirih skupin smo že dokazali (izrek \ref{absolGeom}), da za točko $A$, ki ne leži na premici $p$, obstaja (v tej ravnini) vsaj ena premica $q$, ki poteka skozi točko $A$ in ne seka premice $p$ (Figure \ref{sl.aks.2.5.0.pic}).
 Toda ali je takšna premica ena sama? Intuitivno je odgovor pritrdilen. Toda ali lahko to dokažemo z dosedanjimi aksiomi?\footnote{To vprašanje je povezano z že omenjenim problemom petega evklidovega postulata in je bilo odprto skoraj 2000 let.} Izkaže se,  da na to vprašanje ne moremo odgovoriti, če ostanemo le pri prvih štirih skupinah aksiomov.\footnote{Tega dejstva sta se prva začela zavedati ruski matematik \textit{N. I. Lobačevski} (1792--1856) in madžarski matematik  \textit{J. Bolyai} (1802--1860). Prvi, ki je to formalno dokazal, je bil francoski matematik \index{Poincar\'{e}, J. H.} \textit{J. H.
Poincar\'{e}} (1854--1912).}  Dosedanji aksiomi tvorijo en nepopoln sistem aksiomov, ker obstaja trditev, ki jo v tej
teoriji lahko formuliramo, ne moremo pa ugotoviti, če velja ali ne velja.
  Torej je potrebno dodati nov aksiom, s katerim se bomo odločili, ali obstaja le ena takšna premica $q$ ali pa je takšnih premic več.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.0.pic}
\caption{} \label{sl.aks.2.5.0.pic}
\end{figure}


        \baksiom \label{Playfair}\index{aksiom!Playfairjev}
         (Playfair's\footnote{
        \index{Playfair, J.}
        \textit{J. Playfair}
        (1748--1819), škotski matematik je predlagal to trditev kot ekvivalent petega evklidovega postulata.} axiom)
        For any given line $p$ and point $A$ not on $p$ (in the plane containing both line $p$ and point $A$), there is
        just one line  through the point $A$ that do not intersect the line $p$
         (Figure \ref{sl.aks.2.5.1.pic}).
        \eaksiom

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.1.pic}
\caption{} \label{sl.aks.2.5.1.pic}
\end{figure}

Drugo možnost ponuja naslednji aksiom.


        \baksiom \label{Lobac}\index{aksiom!Lobačevskega}
         (Lobachevsky's\footnote{Ruski matematik \textit{N. I. Lobačevski} (1792--1856) in madžarski matematik  \textit{J. Bolyai} (1802--1860) sta neodvisno drug od drugega zgradila prvo neevklidsko geometrijo, ki temelji na
         tem aksiomu in  aksiomih prvih štirih skupin.} axiom)
        For any given line $p$ and point $A$ not on $p$ (in the plane containing both line $p$ and point $A$), there are
        at least two lines  through the point $A$ that do not intersect the line $p$
         (Figure \ref{sl.aks.2.5.1.pic}).
        \eaksiom




Na ta način dobimo dve geometriji, od katerih je vsaka zase neprotislovna.
Prvo geometrijo, ki je določena z aksiomi prvih štirih skupin in s Playfairjevim aksiomom \ref{Playfair}, imenujemo
\index{geometrija!evklidska}\pojem{ravninska evklidska geometrija}. Drugo geometrijo, ki je določena z aksiomi prvih štirih skupin in
aksiomom Lobačevskega \ref{Lobac}, imenujemo \index{geometrija!hiperbolična}\pojem{ravninska hiperbolična
geometrija}.

Čeprav sta očitno različni, imata omenjeni geometriji veliko skupnega. To je jasno že zaradi tega, ker imata  prve štiri skupine aksiomov enake - razlikujeta se le v petem. Posledice prvih štirih
skupin aksiomov, ki smo jih do sedaj obravnavali, veljajo tako v
evklidski geometriji kot tudi v hiperbolični geometriji.
Geometrijo, ki temelji
 samo na  prvih štirih skupinah aksiomov, imenujemo
\index{geometrija!absolutna}\pojem{ravninska absolutna geometrija}. Le-ta določa skupne lastnosti evklidske in hiperbolične geometrije. Ker je sistem aksiomov, ki jo določa, nepopoln, pravimo, da je absolutna geometrija \pojem{nepopolna teorija}.

 Kljub podobnosti veljajo v
hiperbolični geometriji  na prvi pogled nenavadne trditve, kar je seveda posledica aksioma Lobačevskega \ref{Lobac} oz. negacija Playfairjevega aksioma \ref{Playfair}. Vsota notranjih kotov trikotnika je v hiperbolični geometriji
vedno manjša od $180^0$ in ni konstantna; pravokotnica enega kraka ostrega kota ne seka vedno drugega kraka, obstajajo celo trikotniki, za katere ne obstaja včrtana krožnica itd.
 Seveda se nam te trditve zdijo protislovne, toda protislovne so le v evklidski geometriji, v hiperbolični pa ne. Izkaže se, da je hiperbolična geometrija - enako kot evklidska  - neprotislovna teorija\footnote{Neprotislovnost hiperbolične geometrije je prvi dokazal francoski matematik \index{Poincar\'{e}, J. H.} \textit{J. H.
Poincar\'{e}} (1854--1912), ki je zgradil model hiperbolične geometrije v evklidski geometriji. Tako bi protislovje hiperbolične geometrije pomenilo protislovje tudi v evklidski geometriji.}.

Razen omenjenih geometrij obstajajo tudi druge neevklidske geometrije. Geometrija, v kateri se vsaki dve premici ravnine sekata, je t. i. \index{geometrija!eliptična}\pojem{eliptična geometrija\footnote{To geometrijo je razvijal nemški matematik \index{Riemann, G. F. B.} \textit{G. F.
B. Riemann} (1828--1866).}}. Iz že omenjenega izreka \ref{absolGeom} je jasno, da  eliptične geometrije ni možno graditi na aksiomih prvih štirih skupin oz. absolutne geometrije. V tem smislu se ta geometrija bolj razlikuje od evklidske in hiperbolične geometrije.

Omenimo še \index{geometrija!projektivna}\pojem{projektivno geometrijo}. Na določen način je ta od vseh omenjenih geometrij najbolj enostavna, saj temelji samo na treh skupinah aksiomov. Tudi v tej geometriji se vsaki dve premici sekata, toda za razliko od eliptične geometrije v njej nimamo definirane metrike oz. ni relacije skladnosti. V projektivni geometriji je mogoče narediti modele vseh treh geometrij: evklidske, hiperbolične in eliptične.


Še enkrat poudarimo, da v tej knjigi gradimo le ravninsko evklidsko geometrijo. Tako  smo že v začetku množico vseh točk $\mathcal{S}$ imenovali ravnina. V nadaljevanju  jo bomo označevali še z $\mathbb{E}^2$ (oz. $\mathbb{E}^2=\mathcal{S}$). Izbrali smo samo ravninske aksiome in tako dobili sistem aksiomov ravninske evklidske geometrije. Z nekoliko drugačno izbiro osnovnih pojmov (osnovno množico vseh točk $\mathcal{S}$ imenujemo prostor, določene podmnožice so premice in ravnine) in z dodajanjem novih aksiomov (potrebno bi jih bilo dodati že v prvi skupini) bi dobili \pojem{evklidsko geometrijo prostora} ali krajše \index{geometrija!evklidska}\pojem{evklidsko geometrijo}. Na podoben način bi dobili tudi \pojem{hiperbolično geometrijo}\index{geometrija!hiperbolična} in
\index{geometrija!absolutna}\pojem{absolutno geometrijo}.

Obravnavali bomo le evklidsko geometrijo ravnine, zato bomo vedno predpostavljali, da vse točke, premice in liki ležijo v isti ravnini (ker v tej geometriji drugih pravzaprav niti ni). Zaradi razumljivosti pa bomo  to dejstvo občasno ponovno poudarili.


V evklidski geometriji ravnine je sedaj možno vpeljati nov pojem. Pravimo, da sta premici $p$ in $q$ \index{vzporednost!premic}\pojem{vzporedni}, kar označimo $p\parallel q$, če sovpadata ali pa nimata skupnih točk.
 $$p\parallel q \hspace*{2mm} \Leftrightarrow \hspace*{2mm}p=q \hspace*{1mm}\vee \hspace*{1mm} p\cap q=\emptyset .$$

Seveda bi v evklidski geometriji (prostora) morali dodati še pogoj, da $p$ in $q$ ležita v isti ravnini.

Sedaj lahko Playfairjev aksiom  izrazimo tudi v naslednji obliki.



                \bizrek \label{Playfair1}
                For any given line $p$ and point $A$ not on $p$, there is
                just one line  through the point $A$ that is parallel to the line $p$
                (Figure \ref{sl.aks.2.5.1a.pic}).
                \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.1a.pic}
\caption{} \label{sl.aks.2.5.1a.pic}
\end{figure}

 Dokažimo pomembno lastnost definirane relacije vzporednosti.



        \bizrek
        The relation of being parallel is an equivalence relation.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.2.pic}
\caption{} \label{sl.aks.2.5.2.pic}
\end{figure}

 \textbf{\textit{Proof.}} Potrebno  (in dovolj) je dokazati, da je relacija refleksivna, simetrična in tranzitivna (Figure \ref{sl.aks.2.5.2.pic}).


 (\textit{R}) Relacija je refleksivna že po sami definiciji, ker za vsako premico $p$ velja $p\parallel p$.

 (\textit{S}) Če je $p\parallel q$, je direktno po definiciji tudi $q\parallel p$, kar pomeni, da je relacija simetrična.

 (\textit{T}) Predpostavimo, da velja $p\parallel q$ in $q\parallel r$ (vse tri premice so v isti ravnini). Dokažimo, da velja tudi $p\parallel r$. Če vsaj dve od treh premic sovpadata, je dokaz trivialen. Predpostavimo, da se premici $p$ in $r$ sekata v neki točki $A$. V tem primeru potekata skozi točko $A$  vsaj dve premici, ki ne sekata premice $q$, kar je v nasprotju s Playfairjevim aksiomom \ref{Playfair}. Torej velja
 $p\parallel r$, kar pomeni, da je relacija tranzitivna.
\kdokaz

Relacijo vzporednosti bomo definirali tudi za poltrake in daljice.  Poltraka (oz. daljici) sta \index{vzporednost!poltrakov}\index{vzporednost!daljic}\pojem{vzporedna}, če sta njuni nosilki vzporedni premici.

Dokažimo pomemben izrek evklidske geometrije.



        \bizrek \label{KotiTransverzala}
        Let $l$ be a line intersecting two distant lines $a$ and $b$ in points $A$ and $B$, respectively.
        If $X\in a$ and $Y\in b$ are points such that $X,Y\div l$, then:
         $$\angle XAB\cong\angle YBA\hspace*{1mm} \Leftrightarrow \hspace*{1mm}  a\parallel b.$$
        \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.3.pic}
\caption{} \label{sl.aks.2.5.3.pic}
\end{figure}

 \textbf{\textit{Proof.}}

 ($\Rightarrow$) Predpostavimo najprej, da je $\angle XAB\cong\angle YBA$. Označimo s $S$ središče daljice $AB$ in z $N$ pravokotno projekcijo točke $S$ na premico $a$ (Figure \ref{sl.aks.2.5.3.pic}).


 Po izreku \ref{sredZrcObstoj} obstaja takšna izometrija $\mathcal{I}$, ki preslika točko $S$ v točko $S$, za vsako točko $T\neq S$ in njeno sliko $T'=\mathcal{I}(T)$ pa velja, da je $S$ središče daljice $TT'$. Torej je najprej $\mathcal{I}:A,B\mapsto B,A$.
  Naj bo $\mathcal{I}(X)=X'$ in $\mathcal{I}(N)=M$. Označimo z $n$ premico $NM$. Dokažimo, da je $n$ skupna pravokotnica premic $a$ in $b$.

 Dokažimo najprej $\mathcal{I}:a\rightarrow b$ in $M\in b$. Ker je $S$ središče daljice $XX'$, je $X,X'\div S$ oz. $X,X'\div l$ in $X',Y\ddot{-} l$. Iz $\mathcal{I}:B,A,X\mapsto A,B,X'$ sledi $\angle XAB\cong \angle X'BA$. Ker je po predpostavki $\angle XAB\cong\angle YBA$, je tudi $\angle X'BA\cong\angle YBA$. Ker sta še točki $Y$ in $X'$  v isti polravnini $ABY$, po izreku \ref{KotNaPoltrak} poltraka $BX'$ in $BY$ sovpadata. To pomeni, da točka $X'$ leži na poltraku $BY$, zato je tudi $X'\in b$. Iz $\mathcal{I}:A,X\mapsto B,X'$ sedaj sledi (aksiom \ref{aksIII1}) $\mathcal{I}:a\rightarrow b$.
Ker je $N\in a$, je potem tudi $\mathcal{I}(N)\in \mathcal{I}(a)$ oz. $M\in b$.

Iz $\mathcal{I}:S,N\mapsto S,M$ po aksiomu \ref{aksIII1} sledi $\mathcal{I}:n\rightarrow n$.
Torej  velja $\mathcal{I}:a,n\rightarrow b,n$, zato je $\angle b,n\cong a,n=90^0$ oz. $b\perp n$.
Ker je $n$ skupna pravokotnica različnih premic $a$ in $b$, po izreku  \ref{absolGeom} premici $a$ in $b$ nimata skupnih točk, kar pomeni, da je $a\parallel b$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.3a.pic}
\caption{} \label{sl.aks.2.5.3a.pic}
\end{figure}

 ($\Leftarrow$) Naj bo sedaj $a\parallel b$ (Figure \ref{sl.aks.2.5.3a.pic}). Predpostavimo nasprotno - torej, da ni $\angle XAB\cong\angle YBA$. Po izreku \ref{KotNaPoltrak} obstaja tak poltrak $BZ$ v polravnini $ABY$, da velja $\angle ZBA\cong\angle XAB$. Premico $ZB$ označimo z $b'$. Iz prvega dela dokaza ($\Rightarrow$) sledi, da je $b'\parallel a$. Torej $b$ in $b'$ obe potekata skozi točko $B$ in sta vzporedni s premico $a$ oz. z njo nimata skupnih točk (ker je $a\neq b$). Po Playfairovem aksiomu to ni mogoče, kar pomeni, da je $b=b'$. Torej točka $Z$ leži na poltraku $BY$, zato je
 $\angle YBA=\angle ZBA \cong\angle XAB$.
  \kdokaz


Premico $l$, ki seka premici $a$ in $b$, imenujemo njuna \pojem{transverzala}. Kote, ki jih določa premica $l$ s premicama $a$ in $b$, pa imenujemo \index{koti!ob transverzali}\pojem{koti ob transverzali}. Iz prejšnjega izreka \ref{KotiTransverzala} in izreka \ref{sovrsnaSkladna} sledi, da sta vsaka dva kota ob transverzali $l$ vzporednih premic $a$ in $b$  bodisi skladna bodisi suplementarna (Figure \ref{sl.aks.2.5.3b.pic}).
Torej velja naslednja trditev.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.3b.pic}
\caption{} \label{sl.aks.2.5.3b.pic}
\end{figure}


            \bizrek \label{KotiTransverzala1}
            If two parallel lines $a$ and $b$  are cut by a transversal $l$,
            then the angles on the transversal are either congruent or supplementary.
             \index{kota!z vzporednimi kraki}
             \eizrek



 Let's prove a generalization of the previous theorem.



            \bizrek \label{KotaVzporKraki}
            Angles with parallel sides are either congruent or supplementary.
             \index{kota!z vzporednimi kraki}
             \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.4.pic}
\caption{} \label{sl.aks.2.5.4.pic}
\end{figure}


 \textbf{\textit{Proof.}} Naj bosta $\angle aSb$ in $\angle a'S'b'$ takšna kota, da velja $a\parallel a'$ in $b\parallel b'$ (Figure \ref{sl.aks.2.5.4.pic}).
  Če je $b'\parallel a$, po Playfairjevem aksiomu nosilki krakov $a'$ in $b'$ sovpadata. Iz tega enako sledi tudi za kraka $a$ in $b$, kar pomeni, da sta kota $\angle aSb$ in $\angle a'S'b'$ oba iztegnjena in skladna.
  S $S_1$ označimo presečišče nosilk krakov $a$ in $b'$. Po prejšnjem izreku \ref{KotiTransverzala1} sta vsaka dva kota ob transverzali $SS_1$ vzporednic, ki sta nosilki krakov $b$ in $b'$, ali skladna ali suplementarna. Enako velja tudi za poljubna kota ob transverzali $S_1S'$ vzporednic, ki sta nosilki krakov $a$ in $a'$. Iz tega sledi, da sta tudi kota $\angle aSb$ in $\angle a'S'b'$  ali skladna ali suplementarna.
 \kdokaz


V nadaljevanju se bomo ukvarjali z notranjimi in zunanjimi koti večkotnika. Začnimo s trikotnikom.


         \bizrek \label{VsotKotTrik} The sum of the interior angles of a triangle is equal to
         $180^0$.
          \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.7.pic}
\caption{} \label{sl.aks.2.5.7.pic}
\end{figure}

 \textbf{\textit{Proof.}} Naj bo $ABC$ poljubni trikotnik  (Figure \ref{sl.aks.2.5.7.pic}). Po posledici Playfairjevega aksioma \ref{Playfair1} obstaja ena sama premica $l$, ki je vzporedna s premico $BC$. Naj bosta $Y$ in $Z$ takšni točki premice $l$, da velja $Y,B\div AC$ in $Z,C\div AB$. Premica $AB$ je transverzala vzporednic $BC$ in $l$. Ker je še  $Z,C\div AB$, je po izreku \ref{KotiTransverzala}
 $\angle ABC\cong\angle ZAB$. Podobno je premica $AC$ transverzala vzporednic $BC$ in $l$, zato iz  $Y,B\div AC$ in izreka \ref{KotiTransverzala} sledi $\angle BCA\cong\angle YAC$. Na koncu je:
  $$\angle ABC +\angle BAC +\angle BCA = \angle ZAB +\angle BAC +\angle CAY=\angle ZAY=180^0,$$ kar je bilo treba dokazati. \kdokaz

 Zelo koristna sta naslednja izreka.


          \bizrek \label{zunanjiNotrNotr}
          An exterior angle of a triangle is equal to the sum of the two opposite interior angles.
           \eizrek

 \textbf{\textit{Proof.}}  Naj bo $ABC$ poljubni trikotnik  (Figure \ref{sl.aks.2.5.6.pic}). Označimo njegove notranje kote ob ogliščih $A$, $B$ in $C$ z $\alpha$, $\beta$ in $\gamma$, ustrezne zunanje kote pa z  $\alpha'$, $\beta'$ in $\gamma'$. Brez škode za splošnost je dovolj dokazati, da velja $\alpha+\beta=\gamma'$.
 Iz prejšnjega izreka \ref{VsotKotTrik} sledi: $$\alpha+\beta+\gamma=180^0.$$ Ker za sta  zunanji in njemu priležni notranji kot po definiciji sokota, je tudi $$\gamma'+\gamma=180^0.$$ Iz prejšnjih dveh relacij dobimo:
  $$\alpha+\beta=\gamma',$$ kar je bilo treba dokazati. \kdokaz

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.6.pic}
\caption{} \label{sl.aks.2.5.6.pic}
\end{figure}

A direct consequence is the following theorem.


       \bizrek \label{zunanjiNotrNotrVecji}
       An exterior angle of a triangle is greater than either opposite interior angle.
        \eizrek

\textbf{\textit{Proof.}} Vpeljimo iste oznake kot v prejšnjem izreku \ref{zunanjiNotrNotr} (Figure \ref{sl.aks.2.5.6.pic}). Brez škode za splošnost  je dovolj dokazati, da velja $\gamma'>\alpha$ in $\gamma'>\beta$. Relaciji pa sta direktna posledica dokazane neenakosti $\alpha+\beta=\gamma'$ iz prejšnjega izreka \ref{zunanjiNotrNotr}.
 \kdokaz

 Glede na notranje kote lahko obravnavamo tri vrste trikotnikov.
 Dokazali smo že,
  da je v poljubnem trikotniku vsota notranjih kotov enaka $180^0$
  (izrek  \ref{VsotKotTrik}).
To pomeni, da je največ eden od teh kotov topi kot ali pravi kot,
oz. sta vsaj dva ostra. Torej imamo tri možnosti (Figure
\ref{sl.aks.2.6.4a.pic}):
\begin{itemize}
  \item Trikotnik je \index{trikotnik!ostrokotni}
  \pojem{ostrokotni}, če ima vse notranje kote ostre.
  \item Trikotnik je \index{trikotnik!pravokotni}\pojem{pravokotni},
    če ima en notranji kot pravi. Stranico, ki je nasproti
pravemu kotu pravokotnega trikotnika, imenujemo
\index{hipotenuza}\pojem{hipotenuza}, ostali dve stranici sta
\index{kateta}\pojem{kateti}. Ker je vsota notranjih kotov v vsakem
  trikotniku enaka $180^0$, sta
kota pri hipotenuzi pravokotnega trikotnika komplementarna.
  \item Trikotnik je \index{trikotnik!topokotni}\pojem{topokotni},
  če ima en notranji kot topi.
  Ostala dva notranja kota sta potem ostra.
\end{itemize}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.6.4a.pic}
\caption{} \label{sl.aks.2.6.4a.pic}
\end{figure}

%slika 33.1

 Dokažimo še izreka, ki se nanašata na poljubne večkotnike.



         \bizrek \label{VsotKotVeck}
         The sum of the interior angles of any $n$-gon is equal to
         $(n - 2) \cdot 180^0$.
          \eizrek




\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5c.pic}
\caption{} \label{sl.aks.2.5.5c.pic}
\end{figure}


 \textbf{\textit{Proof.}} Predpostavimo najprej, da je $A_1A_2\ldots A_n$ konveksen $n $-kotnik (Figure \ref{sl.aks.2.5.5c.pic}). Njegovih $n-3$ diagonal $A_1A_3$, $A_1A_4$, ... $A_1A_{n-1}$ razdeli ta večkotnik na $n-2$ trikotnikov $\triangle_1$, $\triangle_2$, ..., $\triangle_{n-2}$. Ker se pri tem tudi vsak notranji kot $n $-kotnika  $A_1A_2\ldots A_n$ razdeli na ustrezne notranje kote omenjenih trikotnikov, je vsota vseh notranjih kotov
 $n $-kotnika  $A_1A_2\ldots A_n$ enaka vsoti vseh kotov trikotnikov  $\triangle_1$, $\triangle_2$, ..., $\triangle_{n-2}$. Po izreku \ref{VsotKotTrik} je na koncu ta vsota enaka ravno $(n - 2) \cdot 180^0$.

 Na tem mestu ne bomo dokazovali dejstva, da se tudi v primeru nekonveksnega $n $-kotnika  $A_1A_2\ldots A_n$ le-ta lahko razdeli na $n-2$ trikotnikov.
 \kdokaz


         \bizrek \label{VsotKotVeckZuna}
         The sum of the exterior angles of any $n$-gon is equal to
         $360^0$.
          \eizrek



\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5b.pic}
\caption{} \label{sl.aks.2.5.5b.pic}
\end{figure}


 \textbf{\textit{Proof.}} Označimo z $\alpha_1$, $\alpha_2$,..., $\alpha_n$ notranje in $\alpha'_1$, $\alpha'_2$, ..., $\alpha'_n$ pripadajoče zunanje kote ob ogliščih $A_1$, $A_2$,...,$A_n$ konveksnega $n $-kotnika  $A_1A_2\ldots A_n$. (Figure \ref{sl.aks.2.5.5b.pic}). Za ustrezni notranji in zunanji kot velja:

 \begin{eqnarray*}
 & & \alpha_1+\alpha'_1=180^0\\
 & & \alpha_2+\alpha'_2=180^0\\
 & & \vdots\\
 & & \alpha_n+\alpha'_n=180^0
 \end{eqnarray*}

 Če seštejemo vse enakosti in upoštevamo dokazano enakost iz prejšnjega izreka \ref{VsotKotVeck} $$\alpha_1+\alpha_2+\cdots + \alpha_n=(n - 2) \cdot 180^0,$$
  dobimo $(n - 2) \cdot 180^0+\alpha'_1+\alpha'_2+\cdots + \alpha'_n=n\cdot 180^0$ oz.
  $$\alpha'_1+\alpha'_2+\cdots + \alpha'_n=2 \cdot 180^0=360^0,$$ kar je bilo treba dokazati. \kdokaz

 Iz izreka \ref{VsotKotVeck}  sledi, da je vsota vseh notranjih kotov poljubnega štirikotnika enaka $360^0$, iz izreka \ref{VsotKotVeckZuna} pa, da je tudi vsota vseh zunanjih kotov konveksnega štirikotnika enaka $360^0$ (Figure \ref{sl.aks.2.5.5a.pic}).



\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5a.pic}
\caption{} \label{sl.aks.2.5.5a.pic}
\end{figure}



 Ker je trikotnik (kot presek treh polravnin) konveksen lik, je vsota  vseh zunanjih kotov poljubnega trikotnika enaka $360^0$ (Figure \ref{sl.aks.2.5.5d.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5d.pic}
\caption{} \label{sl.aks.2.5.5d.pic}
\end{figure}


Podobna trditev glede na izrek \ref{KotaVzporKraki}, ki se nanaša na kota z vzporednimi kraki, velja tudi za kota s pravokotnimi kraki.



        \bizrek \label{KotaPravokKraki}
        Angles with perpendicular sides are either congruent or supplementary.
         \index{kota!s pravokotnimi kraki}
        \eizrek



\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5.pic}
\caption{} \label{sl.aks.2.5.5.pic}
\end{figure}


 \textbf{\textit{Proof.}} Naj bosta $\angle aSb$ in $\angle a'S'b'$ takšna kota, da velja $a\perp a'$ in $b\perp b'$ (Figure \ref{sl.aks.2.5.5.pic}). Naj bo $A$ presečišče nosilk krakov $a$ in $a'$ ter $B$  presečišče nosilk krakov $b$ in $b'$. V štirikotniku $SAS'B$ merita notranja kota ob ogliščih $A$ in $B$ vsak $90^0$. Po izreku \ref{VsotKotVeck} je vsota vseh notranjih kotov tega štirikotnika enaka $360^0$. Zato notranja kota $BSA$ in $AS'B$ tega štirikotnika merita skupaj $180^0$, kar pomeni, da sta dva kota, ki ju določata nosilki poltrakov $a$ in $b$ oz. $a'$ in $b'$ suplementarna. Če pa enega od teh kotov zamenjamo z njegovim sokotom, sta ustrezna kota skladna.
 \kdokaz


%________________________________________________________________________________
\naloge{Exercises}
\begin{enumerate}

\item Naj bodo $P$, $Q$ in $R$ notranje točke stranic trikotnika
$ABC$. Dokaži, da so $P$, $Q$ in $R$ nekolinearne.

\item Naj bosta $P$ in $Q$ točki stranic $BC$ in $AC$ trikotnika $ABC$ in hkrati
različni od njegovih oglišč. Dokaži, da se daljici $AP$ in $BQ$
sekata v eni točki.

\item  Točke $P$, $Q$ in $R$ ležijo po vrsti na stranicah $BC$, $AC$ in $AB$ trikotnika
 $ABC$ in so različne od njegovih oglišč. Dokaži, da se daljici $AP$
in $QR$ sekata v eni točki.

\item Premica $p$, ki leži v ravnini štirikotnika, seka njegovo
diagonalo $AC$ in ne poteka skozi nobeno oglišče tega štirikotnika.
Dokaži, da premica $p$ seka natanko dve stranici tega
štirikotnika.

\item Dokaži, da je polravnina konveksen lik.

\item  Dokaži, da je presek dveh konveksnih likov
konveksen lik.

\item  Dokaži, da je poljuben trikotnik konveksen lik.

\item  Če je $\mathcal{B}(A,B,C)$ in $\mathcal{B}(D,A,C)$, je tudi
$\mathcal{B}(B,A,D)$. Dokaži.

\item  Naj bodo $A$, $B$, $C$ in $D$ takšne kolinearne točke, da je
$\neg\mathcal{B}(B,A,C)$ in $\neg\mathcal{B}(B,A,D)$. Dokaži, da
velja $\neg\mathcal{B}(C,A,D)$.

\item Naj bo $A_1A_2\ldots,A_{2k+1}$ poljubni večkotnik z lihim
številom oglišč. Dokaži, da ne obstaja premica, ki seka vse
njegove stranice.

\item Če izometrija $\mathcal{I}$ preslika lika $\Phi_1$ in $\Phi_2$
v lika  $\Phi'_1$ in $\Phi'_2$, potem se  presek
$\Phi_1\cap\Phi_2$ s to izometrijo preslika v presek
$\Phi'_1\cap\Phi'_2$. Dokaži.

\item  Dokaži, da sta poljubna poltraka neke
ravnine med seboj skladna.

\item  Dokaži, da sta poljubni premici neke
ravnine med seboj skladni.


\item  Naj bosta $k$ in $k'$ dve krožnici
neke ravnine s središčema $O$ in $O'$ ter polmeroma $AB$ in $A'B'$.
Dokaži ekvivalenco: $k\cong k' \Leftrightarrow AB\cong A'B'$.

\item  Naj bo $\mathcal{I}$
neidentična izometrija ravnine z dvema negibnima točkama $A$ in
$B$. Če je $p$ premica te ravnine, ki je vzporedna s premico
$AB$ in $A\notin p$. Dokaži, da na premici $p$ ni negibnih točk
izometrije $\mathcal{I}$.

\item   Naj bo $S$ edina negibna točka
izometrije $\mathcal{I}$ v neki ravnini. Dokaži, da če ta izometrija
preslika  premico $p$ vase, je $S\in p$.

\item  Dokaži, da se poljubni dve premici
neke ravnine ali sekata ali sta vzporedni.

\item  Če neka
premica v ravnini seka eno od dveh vzporednic iste ravnine,
 potem  seka tudi drugo vzporednico. Dokaži.

\item  Dokaži, da vsaka izometrija preslika vzporednici v vzporednici.

\item  Naj bodo $p$, $q$ in $r$ takšne premice neke ravnine, tako da velja
$p\parallel q$ in $r\perp p$. Dokaži, da je $r\perp q$.

\item Dokaži, da konveksen $n$-kotnik ne more imeti več kot treh
ostrih kotov.

\end{enumerate}



% DEL 3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
% SKLADNOST TRIKOTNIKOV. VEČKOTNIKI
%________________________________________________________________________________

 \del{Congruence. Triangles and Polygons} \label{pogSKL}

%________________________________________________________________________________
 \poglavje{Triangle Congruence Theorems} \label{odd3IzrSkl}

Iz splošne definicije skladnosti likov sledi, da sta trikotnika
skladna, če obstaja izometrija, ki preslika prvi trikotnik v
drugega. Jasno je, da iz skladnosti dveh trikotnikov sledi
skladnost pripadajočih stranic in notranjih kotov. Nas pa zanima obraten problem:
Kdaj iz skladnosti nekaterih od
pripadajočih stranic in kotov sledi skladnost dveh trikotnikov? O
tem govorijo naslednji \index{izrek!o skladnosti
trikotnikov}\pojem{triangle congruence theorems}\footnote{Prvi, tretji in četrti izrek o skladnosti
trikotnikov pripisujejo \index{Pitagora} \textit{Pitagori z otoka
Samosa} (6. stol. pr. n. š.), za drugi izrek pa se
predpostavlja, da je bil znan že \index{Tales} \textit{Talesu iz
Mileta} (7.--6. stol. pr. n. š.). Vse štiri
navaja \index{Evklid} \textit{Evklid iz Aleksandrije}
(3. stol. pr. n. š.) v prvi knjigi svojih ‘‘Elementov’’.}:

                \bizrek \label{SSS} (\textit{SSS})
                 Triangles are congruent if three sides of one triangle are congruent
                 to the corresponding sides of the other triangle,
                i.e. (Figure
                \ref{sl.skl.3.1.1.pic}):
           \begin{eqnarray*}
            \left.
             \begin{array}{l}
              AB \cong A'B'\\
             BC \cong B'C'\\
             AC \cong A'C'
            \end{array}
            \right\}\hspace*{1mm}\hspace*{1mm}\Rightarrow\triangle ABC \cong \triangle A'B'C'
            \end{eqnarray*}
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.1.pic}
\caption{} \label{sl.skl.3.1.1.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Iz skladnosti daljic po izreku \ref{izrek(A,B)} je tudi $(A,B)
 \cong (A',B')$, $(B,C) \cong (B',C')$
 in $(A,C)
 \cong (A',C')$ oz $(A,B,C) \cong (A',B',C')$. Iz izreka
 \ref{IizrekABC} sledi, da obstaja izometrija $\mathcal{I}$, ki
 preslika točke $A$, $B$ in $C$ v točke $A'$, $B'$ in $C'$.
 Le-ta preslika trikotnik $ABC$ v trikotnik $A'B'C'$, kar je
 posledica izreka \ref{izrekIzoB}. Torej sta trikotnika $ABC$ in
 $A'B'C'$ skladna.
 \kdokaz



                \bizrek \label{SKS} (\textit{SAS})
                Triangles are congruent if two pairs of sides and the included angle of one triangle
                 are congruent to the corresponding sides and angle of the other triangle,
           i.e. (Figure
         \ref{sl.skl.3.1.2.pic}):
           \begin{eqnarray*}
            \left.
             \begin{array}{l}
              AB \cong A'B'\\
             AC \cong A'C'\\
             \angle BAC \cong \angle B'A'C'
            \end{array}
            \right\}\hspace*{1mm}\hspace*{1mm}\Rightarrow\triangle ABC \cong \triangle A'B'C'
            \end{eqnarray*}
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.2.pic}
\caption{} \label{sl.skl.3.1.2.pic}
\end{figure}

\textbf{\textit{Proof.}}
  Ker sta kota $BAC$ in $B'A'C'$ skladna,
  obstaja izometrija $\mathcal{I}$, ki preslika kot $BAC$ v kot $B'A'C'$.
  Ta izometrija preslika vrh $A$ v vrh $A'$ ter kraka $AB$ in $AC$ v $A'B'$ in $A'C'$.
  Naj bo $\mathcal{I}(B)=\widehat{B}'$ in  $\mathcal{I}(C)=\widehat{C}'$.
  Iz tega
  sledi $AB \cong A'\widehat{B}'$ in $AC \cong A'\widehat{C}'$,
  toda po izreku \ref{ABnaPoltrakCX} je $\widehat{B}'=B'$ in
  $\widehat{C}'=C'$.
 Torej izometrija $\mathcal{I}$
 preslika točke $A$, $B$ in $C$ v točke $A'$, $B'$ in $C'$,
 oz. trikotnik $ABC$ v trikotnik $A'B'C'$, kar pomeni, da sta trikotnika $ABC$ in
 $A'B'C'$ skladna.
\kdokaz



                \bizrek \label{KSK} (\textit{ASA})
                Triangles are congruent if two pairs of angles and the included side of one triangle
                 are congruent to the corresponding angles and side of the other triangle
                i.e. (Figure
                \ref{sl.skl.3.1.3.pic}):
           \begin{eqnarray*}
            \left.
             \begin{array}{l}
             AB \cong A'B'\\
             \angle BAC \cong \angle B'A'C'\\
             \angle ABC \cong \angle A'B'C'
            \end{array}
            \right\}\hspace*{1mm}\hspace*{1mm}\Rightarrow\triangle ABC \cong \triangle A'B'C'
            \end{eqnarray*}
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.3.pic}
\caption{} \label{sl.skl.3.1.3.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Iz aksioma \ref{aksIII2} sledi, da obstaja izometrija  $\mathcal{I}$,
  ki preslika
 točko $A$ v točko $A'$, poltrak $AB$ v poltrak $A'B'$ in
 polravnino $ABC$ v polravnino $A'B'C'$.
 Ker je $AB \cong A'B'$, iz istega aksioma sledi
 $\mathcal{I}(B)=B'$. Naj bo $\mathcal{I}(C)=\widehat{C}'$.
 Potem je $\angle BAC \cong \angle B'A'\widehat{C}'$ in
   $\angle ABC \cong \angle A'B'\widehat{C}'$.
  Ker je po predpostavki tudi $\angle BAC \cong \angle B'A'C'$ in
   $\angle ABC \cong \angle A'B'C'$, iz izreka
   \ref{KotNaPoltrak} sledi, da sta poltraka $A'\widehat{C}'$ in
   $A'\widehat{C}'$ (oz. $B'C'$ in
   $B'\widehat{C}'$) enaka. Zato je $\widehat{C}'=A'\widehat{C}'\cap
   A'\widehat{C}'=A'C'\cap
   A'C'=C'$. Torej $\mathcal{I}:A,B,C \mapsto A',B',C'$, zato sta
   trikotnika $ABC$ in $A'B'C'$ skladna.
 \kdokaz

Dokaz četrtega izreka o skladnosti trikotnikov bomo izpustili.



            \bizrek \label{SSK} (\textit{SSA})
            Triangles are congruent if two pairs of sides and the angle opposite to the longer side of one triangle
                 are congruent to the corresponding sides and angle of the other triangle.
            (Figure \ref{sl.skl.3.1.4.pic}).
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.4.pic}
\caption{} \label{sl.skl.3.1.4.pic}
\end{figure}


Ena od pomembnejših posledic izrekov o skladnosti trikotnikov je
naslednja trditev.



             \bizrek \label{enakokraki}
             If two sides of a triangle are congruent, then angles opposite those sides are congruent.\\
             And vice versa:\\
            If angles opposite those sides are congruent, then two sides of a triangle are congruent.
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.5.pic}
\caption{} \label{sl.skl.3.1.5.pic}
\end{figure}


 \textbf{\textit{Proof.}}
 Naj bo $ABC$ takšen trikotnik, da je $AB \cong AC$
 (Figure \ref{sl.skl.3.1.5.pic}). Ker velja
še $AC \cong AB$ in $BC \cong CB$, iz izreka \textit{SSS} sledi, da
sta trikotnika $ABC$ in $ACB$ skladna (ta dva trikotnika imata
različno orientacijo). Zato je $\angle ABC \cong \angle CBA$. Na
enak način bi lahko dokazali tudi obratno trditev. V tem primeru bi
uporabljali izrek \textit{ASA}.
 \kdokaz

 Trikotnik (kot je trikotnik $ABC$ iz prejšnjega izreka),
 ki ima vsaj dve
stranici skladni, imenujemo
\index{trikotnik!enakokraki}\pojem{enakokraki trikotnik}. Vsaka od
dveh skladnih stranic je \index{krak!enakokrakega
trikotnika}\pojem{krak}, tretja stranica pa je
\index{osnovnica!enakokrakega trikotnika}\pojem{osnovnica} tega
trikotnika. Torej sta po prejšnjem izreku notranja kota ob
osnovnici enakokrakega trikotnika skladna. In obratno - če sta dva
notranja kota trikotnika skladna, je ta trikotnik enakokrak.



             \bzgled
            Let the $E$ and $F$ be a points lies on the line containing  the hypotenuse $AB$ of a perpendicular
            triangle $ABC$ and let $B(E,A,B,F)$, $EA\cong AC$ and
              $FB\cong BC$. What is the measure of the angle $ACB$?
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.6.pic}
\caption{} \label{sl.skl.3.1.6.pic}
\end{figure}


 \textbf{\textit{Solution.}} (Figure \ref{sl.skl.3.1.6.pic})

 Notranja kota trikotnika $ABC$ ob ogliščih
 $A$ in $B$ označimo z $\alpha$ in
  $\beta$.
 Trikotnika $EAC$ in $CBF$ sta
 enakokraka trikotnika z osnovnicama $CE$ in $CF$, zato je $\angle CEA \cong \angle ACE$ in
 $\angle CFB \cong \angle BFC$ (izrek \ref{enakokraki}). Kot
 $\alpha$ je zunanji kot trikotnika $EAC$, zato je po izreku \ref{zunanjiNotrNotr}:
  $\alpha = 2\angle ECA$ oz.  $\angle ECA = \frac{1}{2} \alpha$.
  Podobno je tudi $\angle FCB = \frac{1}{2} \beta$. Torej:
\begin{eqnarray*}
   \angle ECF&=&\angle ECA+\angle ACB+\angle BCF=\\
   &=&\frac{1}{2}
   \cdot\alpha+90^0+
    \frac{1}{2} \cdot\beta=90^0+
    \frac{1}{2} \cdot\left(\alpha+\beta\right)=\\
    &=&90^0+
    \frac{1}{2}\cdot 90^0=135^0,
    \end{eqnarray*}
oz. $\angle ECF=135^0$. \kdokaz

Trikotnik, pri katerem so vse stranice enake, imenujemo
\index{trikotnik!enakostranični}\pojem{enakostranični trikotnik}
(Figure \ref{sl.skl.3.1.7.pic}), ki  je poseben primer
enakokrakega trikotnika. Zato iz omenjenega izreka sledi,
da so vsi notranji koti enakostraničnega trikotnika enaki. Ker je
njihova vsota enaka $180^0$, vsak od teh kotov meri $60^0$. Velja
tudi obratno: če sta vsaj dva kota trikotnika enaka $60^0$ (in
zaradi tega tudi tretji), potem je ta trikotnik enakostraničen.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.7.pic}
\caption{} \label{sl.skl.3.1.7.pic}
\end{figure}




            \bzgled
              Let $ABC$ be an equilateral triangle and $P$, $Q$ and $R$
            points such that $\mathcal{B}(A,B,R)$, $\mathcal{B}(B,C,Q)$, $\mathcal{B}(C,A,P)$ and
            $BR\cong CQ\cong AP$. Prove that $PQR$ is also an equilateral triangle.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.8.pic}
\caption{} \label{sl.skl.3.1.8.pic}
\end{figure}


 \textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.1.8.pic})

 Iz danih pogojev je najprej
  $AR\cong BQ\cong CP$. Trikotnik $ABC$ je  enakostranični trikotnik,
  zato vsi trije notranji koti merijo $60^0$. Iz tega sledi
  $\angle PAR\cong \angle RBQ\cong QCP$. Po izreku \textit{SAS} so
  trikotniki $PAR$, $RBQ$ in $QCP$ skladni in je $PR\cong RQ\cong QP$.
  To pomeni, da je tudi $PQR$  enakostranični trikotnik.
 \kdokaz


V prejšnjem poglavju smo definirali simetralo daljice kot premico,
ki je pravokotnica daljice  in poteka skozi njeno središče. Dokažimo
sedaj ekvivalentno definicijo simetrale daljice, ki bo zelo
pomembna v nadaljevanju. \index{simetrala!daljice}


             \bizrek \label{simetrala}
             The perpendicular bisector of a line segment $AB$ is the set of all points $X$
              that are equidistant from its endpoints, i.e. $AX \cong BX$.
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.9.pic}
\caption{} \label{sl.skl.3.1.9.pic}
\end{figure}


 \textbf{\textit{Proof.}}
   Naj bo premica $s$ simetrala daljice
$AB$ v neki ravnini. Po definiciji je $s$ pravokotnica na  daljico
$AB$ skozi njeno središče – točko $S$. Označimo z $\mathcal{M}$
množico vseh točk $X$ te ravnine, za katere velja $AX \cong BX$.
Potrebno je dokazati, da je $s =\mathcal{M}$. To bomo dokazali z
dvema inkluzijama (Figure \ref{sl.skl.3.1.9.pic}).

($s\subseteq \mathcal{M}$). Naj bo $X \in s$. Dokažimo, da potem
velja $X \in \mathcal{M}$. Iz relacij $AS \cong BS$, $XS \cong XS$
in $\angle ASX \cong \angle BSX = 90^0$ sledi, da sta trikotnika
$ASX$ in $BSX$ skladna (izrek \textit{SAS}). Zato je $AX \cong BX$
oz. $X \in \mathcal{M}$.

($\mathcal{M}\subseteq s$). Naj bo sedaj $X \in \mathcal{M}$.
Dokažimo, da velja $X \in s$. Iz $X \in \mathcal{M}$ sledi $AX \cong BX$.
Sedaj iz $AS \cong BS$, $XS \cong XS$ in $AX \cong BX$ sledi,
da sta trikotnika $ASX$ in $BSX$ skladna (izrek \textit{SSS}). Zato sta kota
$ASX$ in $BSX$ skladna in kot sokota sta oba prava kota. To pomeni,
da je premica $XS$ pravokotnica daljice $AB$ v njenem središču.
Torej, premica $XS$ je simetrala $s$ oz. $X \in s$.
 \kdokaz

The next problem is an example of multiple use of the theorem of an isosceles triangle (\ref{enakokraki}).

      \bnaloga\footnote{42. IMO USA - 2001, Problem 5.}
      In a triangle $ABC$, let $AP$ bisect $\angle BAC$, with $P$ on $BC$, and let $BQ$ bisect $\angle ABC$, with $Q$ on $CA$.
It is known that $\angle BAC=60^0$ and that $|AB|+|BP|=|AQ|+|QB|$.
What are the possible measures of  interior angles of triangle $ABC$?
        \enaloga


\begin{figure}[!htb]
\centering
\input{sl.skk.4.9.IMO1.pic}
\caption{} \label{sl.skk.4.9.IMO1.pic}
\end{figure}

\textbf{\textit{Solution.}} Označimo notranje kote trikotnika $ABC$ z
$\alpha=60^0$, $\beta$ in $\gamma$. Naj bosta $D$ in $E$ takšni
točki, da velja: $BD\cong BP$, $\mathcal{B}(A,B,D)$, $QE \cong QB$
in $\mathcal{B}(A,Q,E)$ (Figure \ref{sl.skk.4.9.IMO1.pic}). Iz teh
pogojev sledi, da sta $DBP$ in $BQE$ enakokraka trikotnika z
osnovnicama $DP$ in $BE$. Iz danega pogoja $|AB|+|BP|=|AQ|+|QB|$
sledi še $AD\cong AE$, kar pomeni, da je tudi $ADE$ enakokraki
trikotnik z osnovnico $DE$.

Ker je $DBP$ enakokraki trikotnik, iz izrekov \ref{enakokraki} in
\ref{zunanjiNotrNotr} sledi: $\angle BDP\cong \angle BPD
=\frac{1}{2}\angle ABC=\frac{1}{2}\beta$.
Ker je tudi $BQE$ enakokraki trikotnik, je $\angle QBE\cong\angle QEB$.
 Iz skladnosti trikotnikov $ADP$ in $AEP$ (izrek \textit{SAS}
\ref{SKS}) sledi $\angle ADP\cong\angle AEP$ in $PD\cong PE$.

Če povežemo dokazane relacije, velja:
 \begin{eqnarray*}
&& \angle AEP\cong \angle BDP
=\frac{1}{2}\beta\cong \angle QBP\\
&&\textrm{ in } \angle AEB\cong\angle QBE
 \end{eqnarray*}

 Predpostavimo najprej, da velja $QB>QC$ oz.
 $\mathcal{B}(Q,C,E)$. V tem primeru je:
 \begin{eqnarray*}
 \angle PEB &=&\angle AEB-\angle AEP=\\
 &=&\angle QBE-\angle QBP=\\
 &=&\angle PBE.
 \end{eqnarray*}
To pomeni, da je $PBE$ enakokraki trikotnik z osnovnico $BE$ oz.
$PE\cong PB$. Toda iz že dokazanega $PE\cong PD$ in predpostavke
$PB\cong BD$ sledi $PD\cong PB\cong BD$, zatorej je $BDP$ enakostranični
trikotnik. Iz tega sledi $\beta=2\angle BDP=2\cdot 60^0=120^0$, oz. $\alpha+\beta=60^0+120^0=180^0$, kar ni možno (izrek
\ref{VsotKotTrik}). Zato relacija $QB>QC$ ni mogoča.

Na podoben način pripelje do protislovja tudi relacija $QB>QC$. To
pomeni, da je možno le $QB\cong QC$. V tem primeru je $C=E$ in
velja $\gamma=\angle ACB=\angle AEB\cong AEP=\frac{1}{2}\beta$. Iz
$\alpha+\beta+\gamma=180^0$, sledi
$60^0+\beta+\frac{1}{2}\beta=180^0$ oz. $\beta=80^0$.

Dokazali smo, da iz pogojev iz naloge sledi $\beta=80^0$. Torej je
edina možna rešitev  $\beta=80^0$. Potrebno je še dokazati, da
$\beta=80^0$ je rešitev, oz. da iz $\alpha=60^0$, $\beta=80^0$
sledi $|AB|+|BP|=|AQ|+|QB|$.
 Najprej iz $\angle QCB=\gamma=\frac{1}{2}\beta=40^0=\angle QBC$ sledi
 (izrek \ref{enakokraki}) $QC\cong QB$ oz.
 $|AQ|+|QB|=|AQ|+|QC|=|AC|$.
Če točko $D$ definiramo na isti način kot v prvem delu, spet
dobimo $\angle ADP\cong \angle BPD=\frac{1}{2}\angle ABC=40^0=\angle ACB=\angle ACP$.
To pomeni, da sta trikotnika
$ADP$ in $ACP$ skladna (izrek \textit{ASA} \ref{KSK}) oz.
$AD\cong AC$. Zato je na koncu:
 $$|AB|+|BP|=|AB|+|BD|=|AD|=|AC|=|AQ|+|QB|,$$ kar je bilo treba dokazati. \kdokaz



%________________________________________________________________________________
 \poglavje{Constructions in Geometry} \label{odd3NacrtNaloge}

Ob naslednjem zgledu bomo opisali t. i. načrtovalne naloge.


             \bzgled \label{načrt1odd3}
              Two congruent line segments $AB$ and $A'B'$ in a plane are given.
              Construct a point $C$ such that $\triangle ABC \cong \triangle A'B'C$.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.10.pic}
\caption{} \label{sl.skl.3.1.10.pic}
\end{figure}

 \textbf{\textit{Solution.}} Predpostavimo, da je $C$ točka v ravnini daljic, za
 katero je $\triangle ABC \cong \triangle A'B'C$. Potem je $AC\cong A'C$
 in  $BC\cong B'C$ oz. točka $C$ leži na simetralah daljic $AA'$
 in $BB'$ (izrek  \ref{simetrala}). To dejstvo nam omogoča konstrukcijo
  (Figure \ref{sl.skl.3.1.10.pic}).

 Načrtajmo simetrali daljic $AA'$
 in $BB'$. Točko $C$ dobimo v njunem presečišču.

 Dokažimo, da je $C$ iskana točka oz. da izpolnjuje pogoje iz
 naloge. Po predpostavki je že $AB\cong A'B'$. Ker smo točko $C$ dobili kot
 presečišče simetral daljic $AA'$
 in $BB'$, je  $AC\cong A'C$ in $BC\cong B'C$. Iz izreka \ref{SSS} (SSS) sledi,
 da sta trikotnika $ABC$ in $A'B'C$
 skladna.

  Naloga ima rešitev (eno) natanko tedaj, ko se simetrali daljic
  $AA'$
 in $BB'$ sekata, oz. ko premici $AA'$
 in $BB'$ nista vzporedni.
  \kdokaz

  Prejšnji zgled je torej t. i. \index{načrtovalna naloga}
   \pojem{načrtovalna naloga}, pri kateri
  je za dane podatke potrebno načrtati oz. konstruirati nek novi element ali lik,
  ki v zvezi z danimi podatki
  izpolnjuje določene pogoje. \pojem{Načrtovanje} oz. \index{konstrukcije}
  \pojem{konstrukcija}
   pomeni
  uporabo ravnila in šestila oz. uporabo
  \index{konstrukcije!elementarne}
  \pojem{elementarne konstrukcije}:\label{elementarneKonstrukcije}
\begin{itemize}
  \item za dani točki $A$ in $B$ narišemo:
 \begin{itemize}
  \item premico $AB$,
  \item daljico $AB$,
  \item poltrak $AB$;
\end{itemize}
 \item narišemo krožnico $k$:
\begin{itemize}
  \item s središčem $S$, ki poteka skozi dano točko $A$,
  \item s središčem $S$ in polmerom, ki je skladen z dano
  daljico;
\end{itemize}
\item narišemo krožni lok z danima središčem in polmerom,
\item narišemo presečišče (oz. presečišči):
\begin{itemize}
  \item dveh premic,
  \item premice in krožnice,
  \item dveh krožnic.
\end{itemize}
\end{itemize}

  Rešitev načrtovalne naloge (nariši lik $\Phi$, ki izpolnjuje pogoje
  $\mathcal{A}$) je formalno sestavljena iz štirih korakov:
\begin{itemize}
  \item \textit{analysis} - pri kateri predpostavimo, da je
  lik $\Phi$ že načrtan in izpolnjuje pogoje $\mathcal{A}$, nato
  pa iščemo nove pogoje $\mathcal{B}$, ki jih lik izpolnjuje.
  Ti sledijo iz pogojev $\mathcal{A}$ in so bolj ugodni za
  konstrukcijo lika $\Phi$. Dokažemo
  $\mathcal{A}\Rightarrow \mathcal{B}$.
  \item \textit{construction} - načrtamo lik $\Phi'$, ki izpolnjuje pogoje
   $\mathcal{B}$. Natanko opišemo potek načrtovanja.
  \item \textit{proof} - dokažemo, da je $\Phi' = \Phi$ oz.
  $\mathcal{B}\Rightarrow \mathcal{A}$.
  \item \textit{discussion} - raziščemo
  število rešitev naloge, odvisno od pogojev  $\mathcal{A}$.
\end{itemize}


        \bzgled \label{konstrTrik1}
        Line segments $a$, $l$ and an angle $\alpha$ are given. Construct a triangle
            $ABC$, such that the side $BC$ is congruent to the line segment $a$, the sum of the sides $AB + AC$
             equal to the line segment $l$ and the interior angle $BAC$ congruent to the angle $\alpha$  ($a$, $b+c$, $\alpha$).
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.10a.pic}
\caption{} \label{sl.skl.3.1.10a.pic}
\end{figure}


 \textbf{\textit{Analysis.}} Naj bo $ABC$ trikotnik, pri katerem je $BC \cong a$, vsota $AB+AC$ enaka dani daljici $l$ in
$\angle BAC\cong \alpha$ (Figure \ref{sl.skl.3.1.10a.pic}). Naj bo $D$ takšna točka na poltraku $BA$, da je $AD\cong AC$ in točki $B$ in $D$ na različnih straneh
točke $A$. Torej velja $BD=BA+AD=AB+AC=l$ oz. $BD\cong l$. Trikotnik $ACD$ je enakokrak, zato sta  kota $ADC$ in $ACD$
po izreku \ref{enakokraki} skladna. Ker sta hkrati notranja
kota trikotnika $CAD$, sta oba enaka polovici zunanjega kota $BAC$ tega trikotnika (izrek  \ref{zunanjiNotrNotr}), oz.
 $\angle BDC=\angle ADC\cong \angle ACD=\frac{1}{2}\angle BAC=\frac{1}{2}\alpha$.
 To dejstvo nam omogoča
konstrukcijo trikotnika $BCD$.

\textbf{\textit{Construction.}} Načrtajmo najprej trikotnik $BCD$, kjer je
$\angle BDC=\frac{1}{2}\alpha$,
 $BC\cong a$ in $BD\cong l$,
nato pa točko $A$ kot presečišče simetrale daljice $CD$ z daljico $BD$. Dokažimo da je $ABC$
iskani trikotnik.

\textbf{\textit{Proof.}} Najprej je $BC\cong a$, že po konstrukciji. Po konstrukciji točka $A$ leži na simetrali daljice
$CD$, zato je $AD\cong AC$ (izrek \ref{simetrala}). Torej $CAD$ je enakokraki trikotnik z osnovnico $CD$, zato je (izrek \ref{enakokraki}) tudi $\angle ADC\cong \angle ACD$. Zaradi tega je (izrek \ref{zunanjiNotrNotr}) $\angle BAC = 2 \cdot \angle BDC= 2\cdot\frac{1}{2}\alpha=\alpha$. Iz $AD\cong AC$  pa sledi
 $AB + AC = AB + AD = BD \cong l$
.

\textbf{\textit{Discussion.}} Naloga ima rešitev (in sicer eno ali dve) natanko tedaj,
ko poltrak $DC$ seka krožnico $k(B,a)$
in simetrala daljice $CD$ seka daljico $BD$.
 \kdokaz

V bodoče ne bomo pri vsaki načrtovalni nalogi izpeljevali vseh korakov.
V večini primerov bomo naredili le prvi korak in s tem nakazali
potek reševanja.




%________________________________________________________________________________
 \poglavje{Triangle inequality} \label{odd3NeenTrik}

Najprej bomo dokazali  dva pomembna izreka, ki sta posledici
izrekov o skladnosti trikotnikov.

            \bizrek \label{vecstrveckot}
            One side of a triangle is longer than another side of a triangle if and only if
            the measure of the angle opposite the longer side is greater than the angle opposite the shorter side.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.1.pic}
\caption{} \label{sl.skl.3.2.1.pic}
\end{figure}

 \textbf{\textit{Proof.}} Naj bo $ABC$ trikotnik, v katerem je $AC > AB$ (Figure \ref{sl.skl.3.2.1.pic}).
 Dokažimo, da je tedaj tudi $\angle ABC > \angle ACB$. Ker je $AC > AB$, obstaja
takšna točka $B'$ med točkama $A$ in $C$, za katero velja $AB \cong AB'$.
Tedaj je trikotnik $BAB’$ enakokrak in velja
$\angle ABB' \cong \angle AB'B$ (izrek \ref{enakokraki}).
Poltrak $BB'$ je znotraj kota $ABC$, zato je $\angle ABC > \angle ABB '$.
Potem je $\angle AB'B$ zunanji kot trikotnika $BCB'$. Po
 izreku  \ref{zunanjiNotrNotrVecji} je ta kot večji od njegovega nesosednjega
notranjega kota $B'CB$. Če uporabimo doslej dokazano, dobimo:
 $$\angle ABC >
\angle ABB ' \cong \angle AB'B > \angle B'CB \cong \angle ACB.$$
 Torej velja $\angle ABC
> \angle ACB$. Na podoben način dokažemo, da velja tudi obratno.
\kdokaz

 Če  z $a$, $b$ in $c$ označimo dolžine stranic $BC$, $AC$ in
 $AB$ trikotnika $ABC$ ter z $\alpha$, $\beta$ in $\gamma$
 mere nasprotnih kotov ob ogliščih $A$, $B$ in $C$, lahko prejšnji izrek
 zapišemo v obliki:
  $$a > b \Leftrightarrow \alpha > \beta,$$
  izrek o enakokrakem trikotniku \ref{enakokraki} pa v obliki:
 $$a = b \Leftrightarrow \alpha = \beta.$$


 To pomeni, da sta izraza $a-b$ in $\alpha-\beta$ oba pozitivna,
 oba negativna ali oba enaka nič. Tako smo dokazali naslednjo
 lastnost:

             \bzgled \label{vecstrveckotAlgeb}
            For each triangle $ABC$ is:
             $$(a-b)(\alpha-\beta)\geq 0, \hspace*{4mm}
             (b-c)(\beta-\gamma)\geq 0, \hspace*{4mm}
             (c-a)(\gamma-\alpha)\geq 0$$
            \ezgled

Iz izreka \ref{vecstrveckot} direktno sledi naslednja
trditev:


            \bizrek \label{vecstrveckotHipot}
            The hypotenuse of a right-angled triangle is longer than its
            two legs.
            The longest side of an obtuse triangle is the one opposite to the obtuse angle.
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.2.pic}
\caption{} \label{sl.skl.3.2.2.pic}
\end{figure}


\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.2.2.pic})

 Vsota notranjih kotov trikotnika je enaka $180^0$. Zato je v
pravokotnem trikotniku največji kot ravno pravi kot. Hipotenuza
pravokotnega trikotnika je po prejšnjem izreku najdaljša stranica
tega trikotnika. Podobno dokažemo tudi v primeru topokotnega
trikotnika.
 \kdokaz


Daljica $AA'$ je \index{višina!trikotnika}\pojem{višina}
trikotnika $ABC$, če je $AA'\perp BC$ in $A'\in BC$. Zadnja od
dveh relacij pomeni, da točka $A'$ leži na premici $BC$, ne pa
nujno na daljici $BC$. Relacija $\mathcal{B}(B,A',C)$ velja
natanko tedaj, ko sta notranja kota pri ogliščih $B$ in $C$ oba
ostra (Figure \ref{sl.skl.3.2.3.pic}). To je posledica izreka o
vsoti notranjih kotov poljubnega trikotnika (izrek
\ref{VsotKotTrik}). V primeru, da je  $\angle ABC\geq 90^0$ in
$\mathcal{B}(B,A',C)$, bi bila vsota notranjih kotov v trikotniku $ABA'$
večja od $180^0$.
 Torej
 višina trikotnika ni vedno v notranjosti trikotnika.
 Pri pravokotnem trikotniku sta višini iz
dveh oglišč ob ostrih kotih enaki ustreznima katetama. Višine,
ki potekajo iz oglišč $A$, $B$ in $C$ ponavadi označimo z $v_a$,
$v_b$ in $v_c$. Iz prejšnjega izreka \ref{vecstrveckotHipot}
sledi, da je dolžina višina poljubnega trikotnika manjša ali enaka dolžini
nepripadajoče stranice tega trikotnika, npr.: $v_a\leq b$, $v_a\leq c$, ...


\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.3.pic}
\caption{} \label{sl.skl.3.2.3.pic}
\end{figure}


Sedaj bomo rešili načrtovalno nalogo, v kateri kot podatek nastopa višina trikotnika.


        \bzgled
        	 Construct a triangle $ABC$ such that the sides $AB$,
            $AC$ and the altitude  from the vertex $B$ are congruent to the three given line segments $c$, $b$ and $v_b$.
        \ezgled



\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.4a.pic}
\caption{} \label{sl.skl.3.2.4a.pic}
\end{figure}



\textbf{\textit{Analysis.}} Naj bo $ABC$ trikotnik, za katerega velja $AB\cong c$,
 $AC\cong b$ in $AD\cong v_b$ (kjer je $BD$ višina tega trikotnika iz oglišča $B$).
 V pravokotnem trikotniku $ABD$
sta torej znani hipotenuza $AB\cong c$ in kateta
$AD\cong v_b$, kar pomeni, da ga lahko načrtamo. Tretje oglišče $C$ trikotnika $ABC$ leži na premici $AD$ (Figure \ref{sl.skl.3.2.4a.pic}).

\textbf{\textit{Construction.}} Načrtajmo najprej pravokotni trikotnik
$ABD$ (s pogoji: $AB\cong c$, $\angle ADB=90^0$ in $BD\cong v_b$). Na premici $AD$ nato določimo  takšno točko $C$,
da velja $AC\cong b$. Dokažimo, da je $ABC$ iskani trikotnik.


\textbf{\textit{Proof.}} Najprej je $AB\cong c$ in
 $AC\cong b$ že po konstrukciji. Ker je še $\angle ADB=90^0$, je $BD$ višina trikotnika $ABC$ iz oglišča $B$ in je po konstrukciji skladna z daljico $v_b$.


\textbf{\textit{Discussion.}} Naloga ima rešitev natanko tedaj, ko je možna
konstrukcija trikotnika $ABD$ oz. $hb\leq c$. Pri konstrukciji točke $C$
obstajata dve možnosti - na različnih straneh točke $A$, kar pomeni, da imamo dve rešitvi za trikotnik $ABC$. V primeru  $hb\cong c$ sta rešitvi pravokotna in skladna trikotnika.
 \kdokaz



        \bzgled
        If $v_a$, $v_b$ and $v_c$ are altitudes corresponding
        to the sides $a$, $b$ and $c$ of a triangle, then:
        $$\frac{v_a}{b+c}+\frac{v_b}{a+c}+\frac{v_c}{a+b}<\frac{3}{2}.$$
        \ezgled

\textbf{\textit{Proof.}}
Če seštejemo neenakosti $v_a\leq b$,
$v_a\leq c$
 dobimo $2v_a\leq b+c$ oz. $\frac{v_a}{b+c}\leq\frac{1}{2}$.
 Analogno dobimo $\frac{v_b}{a+c}\leq\frac{1}{2}$ in
 $\frac{v_c}{a+b}\leq\frac{1}{2}$. Ker vse enakosti ne morejo veljati hkrati,
  s seštevanjem dobimo iskano neenakost.
 \kdokaz

Naslednjo lastnost trikotnika bomo imenovali \index{trikotniška
neenakost} \pojem{trikotniška neenakost}.


             \bizrek \label{neenaktrik}
             The sum of any two sides of a triangle is greater than the third side.
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.4.pic}
\caption{} \label{sl.skl.3.2.4.pic}
\end{figure}


\textbf{\textit{Proof.}} Naj bo $ABC$ poljuben trikotnik.
Dokažimo, da velja \\ $AB + AC > BC$. Z $D$ označimo takšno točko,
da je $\mathcal{B}(B,A,D)$ in $AD \cong  AC$ (Figure
\ref{sl.skl.3.2.4.pic}). Po izreku \ref{enakokraki}
($\triangle CAD$ je enakokraki trikotnik z osnovnico $CD$) je  tudi  $\angle BDC=\angle ADC  \cong  \angle ACD$. Poltrak $CA$ je
znotraj kota $DCB$, zato je
 $\angle ACD <  \angle DCB$. Tedaj je tudi  $\angle BDC <  \angle DCB$.
 Iz izreka
 \ref{vecstrveckot} (glede na trikotnik $BCD$) sledi:
$$BC < BD = AB + AD = AB + AC,$$ kar je bilo treba dokazati. \kdokaz

Iz trikotniške neenakosti dobimo kriterij za obstoj takšnega
trikotnika, da so njegove stranice skladne s tremi danimi daljicami.


             \bzgled
            Let $a$, $b$ and $c$ be three line segments. A triangle with sides $a$,
            $b$ and $c$ exist if and only if:
             $$b + c > a,\hspace*{2mm}
             a + c > b \hspace*{1mm}\textrm{ in }\hspace*{1mm}
             a + b > c.$$
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.5.pic}
\caption{} \label{sl.skl.3.2.5.pic}
\end{figure}

\textbf{\textit{Proof.}}  Če takšen trikotnik obstaja, potem so tri
relacije direktna posledice izreka o trikotniški neenakosti
\ref{neenaktrik}. Predpostavimo torej, da veljajo vse tri relacije.
Brez škode za splošnost naj bo npr. $a$ najdaljša stranica tega
trikotnika (dovolj je, da ni krajša od neke druge stranice) ter $B$
in $C$ poljubni točki, za kateri je $BC \cong a$ (Figure
\ref{sl.skl.3.2.5.pic}). Ker je po predpostavki $b + c > a$,
to pomeni, da se krožnici $k(B,c)$ in $k(C,b)$ sekata v neki točki
$A$ (posledica Dedekindovega aksioma - izrek
\ref{DedPoslKrozKroz}, ker vsaka od njiju vsebuje notranje točke
druge), ki ni na daljici $BC$. Trikotnik $ABC$ je potem iskani
trikotnik. \kdokaz

 Če vemo, katera od treh stranic je najdaljša,
 je dovolj preveriti le eno neenakost, saj
sta drugi dve avtomatično izpolnjeni. Dokaz
prejšnjega izreka lahko uporabimo tudi za naslednji, ekvivalenten
kriterij.

             \bzgled \label{neenaktrik1}
               Let $a$, $b$ and $c$ be three line segments, such that $a \geq b,c$. A triangle with sides $a$,
            $b$ and $c$ exist if and only if $b + c > a$.
              \ezgled

Tako npr. lahko ugotovimo, da obstaja trikotnik s stranicami, ki
imajo dolžine 7, 5 in 3 (ker je $5+3>7$), trikotnik s stranicami, ki imajo dolžine 9, 6 in 2,
pa ne obstaja (ker ni $6+2>9$).

 Oglejmo si še nekatere posledice prejšnjih izrekov.


             \bzgled
              If $X$ is an arbitrary point of the side $BC$ of a triangle $ABC$,
                then:
               $$AX < AB + AC.$$
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.6.pic}
\caption{} \label{sl.skl.3.2.6.pic}
\end{figure}

\textbf{\textit{Proof.}} Če uporabimo trikotniško neenakost za
trikotnike $ABX$ in $AXC$ (Figure \ref{sl.skl.3.2.6.pic}), dobimo:
 $$AX < AB + BX \hspace*{1mm} \textrm{ in }\hspace*{1mm}  AX < AC + CX.$$
Po seštevanju teh dveh neenakosti in uporabi trikotniške
neenakosti  za trikotnik $ABC$ dobimo:
 $$2AX < AB + AC +
BC < 2(AB + AC),$$ kar je bilo treba dokazati. \kdokaz

%%  !!! Dosegel magično stran - 100!!! Wow Bravo!!!

Naslednja neenakost je posplošitev prejšnje. V tem smislu je
prejšnja trditev njena posledica in je ni bilo potrebno posebej
dokazovati.


            \bzgled
            Let $X$ be an arbitrary point of the side $BC$, different from the vertices $B$ and $C$ of a triangle $ABC$.
            Then the line segment $AX$ is shorter than at least one of the two line segments $AB$ and $AC$ i.e.:
            $$AX < \max\{AB, AC\}.$$
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.7.pic}
\caption{} \label{sl.skl.3.2.7.pic}
\end{figure}

\textbf{\textit{Proof.}} Ker za točko $X$ velja $\mathcal{B}(B, X, C)$,
eden od sokotov $AXB$ in $AXC$ ni oster. Brez škode za
splošnost naj bo to kot $AXC$ (Figure \ref{sl.skl.3.2.7.pic}). Potem
je le-ta največji kot v trikotniku $AXB$, kar pomeni, da je \\
$AX < AC$ (izrek \ref{vecstrveckot}). Podobno, če kot $AXB$ ni oster,
velja $AX < AB$.
 \kdokaz

Posebej bomo obravnavali primer daljice $AX$, če je točka $X$ iz
prejšnjih dveh izrekov središče stranice $BC$ (Figure
\ref{sl.skl.3.2.8.pic}). Takšno daljico, ki je določena z ogliščem
in središčem nasprotne stranice trikotnika, imenujemo
\index{težiščnica trikotnika} \pojem{težiščnica} trikotnika.
Težiščnice, ki ustrezajo ogliščem $A$, $B$ in $C$ trikotnika $ABC$,
običajno označujemo s $t_a$, $t_b$ in $t_c$. Zadnji
dve trditvi lahko uporabimo tudi za težiščnice. Toda za težiščnice
velja še dodatna lastnost, ki jo bomo sedaj dokazali.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.8.pic}
\caption{} \label{sl.skl.3.2.8.pic}
\end{figure}



             \bzgled \label{neenTezisZgl}  If $a$, $b$, $c$ are the sides and $t_a$
             the corresponding median of a triangle $ABC$, then:
            $$\frac{b+c-a}{2}<t_a<\frac{b+c}{2}.$$
              \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.9.pic}
\caption{} \label{sl.skl.3.2.9.pic}
\end{figure}

\textbf{\textit{Proof.}} Označimo z $A_1$ središče stranice $BC$
trikotnika $ABC$. Tedaj je $t_a  =AA_1$  (Figure
\ref{sl.skl.3.2.9.pic}).

Če za trikotnika $ABX$ in $ACX$ uporabimo trikotniško
neenakost (izrek \ref{neenaktrik}), dobimo: $AA_1 + A_1B > AB$ in
$AA_1 + A_1C > AC$  oz.:
$$t_a+\frac{a}{2}>c \hspace*{2mm} \textrm{ in } \hspace*{2mm}
 t_a+\frac{a}{2}>b.$$
Če seštejemo te dve neenakosti, dobimo $\frac{b+c-a}{2}<t_a$.
Dokažimo še $t_a<\frac{b+c}{2}$.
 Naj bo $D$ točka, za katero je
 $A_1D \cong AA_1$ in $\mathcal{B}(A,A_1,D)$. Trikotnika $AA_1B$ in $DA_1C$
  sta
skladna (izrek \textit{SAS} \ref{SKS}), kar pomeni, da je tudi $AB \cong DC$. Če
uporabimo še trikotniško neenakost (izrek \ref{neenaktrik}) za
trikotnik $ACD$, dobimo:
$$b+c = AC + AB = AC + CD > AD = 2AA_1 = 2t_a,$$ kar je bilo treba dokazati. \kdokaz

 Pokažimo še nekaj primerov uporabe trikotniške neenakosti.


             \bzgled
             Let $M$ be an arbitrary point of the bisector of the exterior angle at
            the vertex $C$ of a triangle $ABC$. Then
            $$MA + MB \geq CA + CB.$$
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.10.pic}
\caption{} \label{sl.skl.3.2.10.pic}
\end{figure}


 \textbf{\textit{Proof.}} Naj bo $D$ takšna točka poltraka $BC$, da je $AC \cong CD$
 in $\mathcal{B}(A,C,D)$ (Figure
\ref{sl.skl.3.2.10.pic}). Trikotnika $ACM$ in $DCM$ sta skladna,
po izreku \textit{SAS}  \ref{SKS} ($AC \cong DC$, $CM \cong CM$, $\angle ACM \cong
\angle DCM$). Zato je tudi $MA \cong MD$. Če sedaj uporabimo
trikotniško neenakost, dobimo: $$MA + MB = MD + MB \geq BD = DC +
CB = CA + CB.$$
 Seveda enakost velja v primeru,
kadar so točke $B$, $M$ in $D$ kolinearne oziroma $M = C$.
 \kdokaz



             \bzgled
            If the bisector of the interior angle at
            the vertex $A$ of a triangle $ABC$ intersects the side $BC$ in the point $E$, then
            $$AB > BE \hspace*{2mm} \textrm{ in }\hspace*{2mm}  AC > CE .$$
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.11.pic}
\caption{} \label{sl.skl.3.2.11.pic}
\end{figure}

 \textbf{\textit{Proof.}}  Ker je $\mathcal{B}(B,E,C)$, je kot
 $AEB$ zunanji kot  trikotnika $AEC$ (Figure
\ref{sl.skl.3.2.11.pic}). Zato je $\angle BEA > \angle EAC \cong
\angle BAE$ (izrek \ref{zunanjiNotrNotrVecji}). Nasproti večjega
kota v trikotniku $BAE$ je večja stranica, oziroma velja $AB > BE$
(izrek \ref{vecstrveckot}). Podobno dokazujemo, da velja tudi
druga od dveh relacij.
 \kdokaz


             \bzgled \label{zgled3.2.9}
            If $M$ is the interior point of a triangle $ABC$, then \\
            $BA + AC > BM + MC.$
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.12.pic}
\caption{} \label{sl.skl.3.2.12.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $N$ presečišče premic $BM$ in
$CA$ (Figure \ref{sl.skl.3.2.12.pic}). Ker je $M$ notranja točka
trikotnika $ABC$, velja $\mathcal{B}(B,M,N)$ in
$\mathcal{B}(A,N,C)$. Če sedaj dvakrat uporabimo trikotniško
neenakost (izrek \ref{neenaktrik}), dobimo:
 \begin{eqnarray*}
\hspace*{-4mm}BM + MC &<& BM + (MN + NC) = (BM + MN) + NC = BN + NC\\
 \hspace*{-4mm}&<& (BA +
AN) + NC = BA + (AN + NC) = BA + AC.
  \end{eqnarray*}

Definirajmo dva nova pojma. Vsoto vseh stranic nekega večkotnika
imenujemo njegov \index{obseg!večkotnika} \pojem{obseg}. Polovica
te vsote pa je \pojem{polobseg} tega večkotnika.



             \bzgled
            If $M$ is the interior point and $s$ the semiperimeter of a triangle $ABC$, then
             $$s < AM + BM + CM < 2s.$$
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.13.pic}
\caption{} \label{sl.skl.3.2.13.pic}
\end{figure}

 \textbf{\textit{Proof.}}
  Prvo neenakost dobimo, če
trikrat uporabimo trikotniško neenakost za trikotnike $MAB$,
$MBC$ in $MCA$ in jih potem seštejemo. Drugo neenakost pa dobimo,
če trikrat uporabimo prejšnjo trditev (zgled \ref{zgled3.2.9})
in seštejemo ustrezne neenakosti (Figure \ref{sl.skl.3.2.13.pic}).
 \kdokaz


             \bzgled
             In each convex pentagon there exist three diagonals,
             which are congruent to the sides of a triangle.
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.14.pic}
\caption{} \label{sl.skl.3.2.14.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bo $AD$ najdaljša diagonala
petkotnika $ABCDE$ (naj ne bo krajša od nobene druge
diagonale). Dokažimo, da so $AD$, $AC$ in $BD$ iskane diagonale,
torej tiste, za katere obstaja trikotnik, čigar stranice so
 s temi diagonalami skladne (Figure \ref{sl.skl.3.2.14.pic}). Ker je
 $AD\geq AC$ in $AD\geq BD$, je dovolj dokazati (zgled \ref{neenaktrik1}),
da velja $AC + BD > AD$. Petkotnik $ABCDE$ je konveksen,
zato se njegovi diagonali $AC$ in
$BD$ sekata v neki točki $S$. Tedaj je: $$AC + BD > AS + SD > AD,$$ kar je bilo treba dokazati. \kdokaz

Zelo pomembna je naslednja posledica izrekov o skladnosti
trikotnikov. Tudi v tem dokazu bomo potrebovali trikotniško
neenakost.


             \bizrek \label{SkladTrikLema}
             Let $ABC$ and $A'B'C'$ triangles such that $AB \cong A'B'$
              and $AC \cong A'C'$. Then $BC > B'C'$ if and only if
             $\angle BAC > \angle B' A'C'$ i.e.
             $$BC > B'C' \Leftrightarrow \angle BAC > \angle B'
            A'C'.$$
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.15.pic}
\caption{} \label{sl.skl.3.2.15.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.2.15.pic})

 ($\Leftarrow$) Naj bo $\angle BAC > \angle B' A'C'$. Tedaj obstaja
znotraj kota $BAC$ takšen poltrak $l$, da je $\angle BA,l \cong \angle B'A'C'$.
S $C''$ označimo točko poltraka $l$, za katero je
$AC'' \cong A'C'$. Tedaj sta (po izreku $SKS$) trikotnika $ABC''$ in
$A'B'C'$ skladna in je $BC'' \cong B'C'$. Dovolj je dokazati, da
velja $BC > BC''$. Če  $C''$ leži na stranici $BC$, je to trivialno
izpolnjeno. Predpostavimo, da točka $C''$ ne leži na stranici $BC$.
Naj bo točka $E$ presečišče simetrale kota $CAC''$ in stranice $BC$.
Po izreku \textit{SAS} sta skladna tudi trikotnika $ACE$ in $AC''E$, zato
je $CE \cong C''E$. Sedaj je:
$$BC = BE + EC = BE + EC'' \hspace{0.1mm} > BC'' = B'C'.$$
 ($\Rightarrow$) Naj bo $BC > B'C'$. Relacija $\angle BAC \cong
  \angle B' A'C'$ ne velja,
  ker bi bila tedaj (po izreku \textit{SAS}) trikotnika
$ABC$ in $A'B'C'$  skladna in potem tudi $BC \cong B'C'$. Če
bi pa veljalo $\angle BAC < \angle B' A'C'$,  bi iz že dokazanega
sledilo $BC < B'C'$. Torej velja $\angle BAC > \angle B' A'C'$.
 \kdokaz

             \bizrek \label{neenakIzlLin}
             If $A_1A_2\ldots A_n$ ($n\in \mathbb{N}$, $n\geq 3$) is polygonal chain, then
             $$|A_1A_2|+|A_2A_2|+\cdots +|A_{n-1}A_n|\geq |A_1A_n|.$$
             \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.16.pic}
\caption{} \label{sl.skl.3.2.16.pic}
\end{figure}

\textbf{\textit{Proof.}} Dokaz bomo izpeljali z indukcijo po $n$
(Figure \ref{sl.skl.3.2.16.pic}).

 V primeru $n=3$ dobimo trikotniško neenakost - izrek
 \ref{neenaktrik}.

 Predpostavimo, da neenakost velja za $n=k$ ($k\in \mathbb{N}$, $k> 3$) oz.
  $|A_1A_2|+|A_2A_2|+\cdots +|A_{k-1}A_k|\geq |A_1A_k|.$ Dokažimo,
  da potem neenakost velja tudi za $n=k+1$ oz.
  $|A_1A_2|+|A_2A_2|+\cdots +|A_kA_{k+1}|\geq |A_1A_{k+1}|.$ Če
  uporabimo najprej indukcijsko
  predpostavko, nato pa trikotniško neenakost, dobimo:
  \begin{eqnarray*}
   && |A_1A_2|+|A_2A_2|+\cdots +|A_{k-1}A_k|+|A_kA_{k+1}|\geq\\
   && \geq|A_1A_k|+|A_kA_{k+1}|\geq |A_1A_{k+1}|,
  \end{eqnarray*}
 kar je bilo treba dokazati. \kdokaz

Dokažimo še eno neenakost, ki velja v poljubnem trikotniku.


             \bzgled
             If $a$, $b$, $c$ are the sides and $\alpha$, $\beta$, $\gamma$
              the opposite interior angles of a triangle, then
              $$60^0\leq \frac{a\alpha+b\beta +c\gamma}{a+b+c} < 90^0.$$
               \ezgled

\textbf{\textit{Proof.}} Dokazali bomo vsako od neenakosti
posebej. Pri tem bomo uporabili izrek o vsoti notranjih kotov
trikotnika (izrek \ref{VsotKotTrik}) Najprej bomo dokazali drugo
neenakost:
 \begin{eqnarray*}
  \frac{a\alpha+b\beta +c\gamma}{a+b+c} < 90^0
  &\Leftrightarrow& a\alpha+b\beta +c\gamma - 90^0(a+b+c)<0\\
  &\Leftrightarrow& a(\alpha-90^0)+b(\beta-90^0) +c(\gamma-90^0)<0\\
  &\Leftrightarrow& a(180^0-2\alpha)+b(180^0-2\beta) +c(180^0-2\gamma)>0\\
  &\Leftrightarrow& a(\beta+\gamma-\alpha)+b(\alpha+\gamma-\beta) +
  c(\alpha+\beta-\gamma)>0\\
  &\Leftrightarrow& \alpha(b+c-a)+\beta(a+c-b) +
  \gamma(a+b-c)>0
 \end{eqnarray*}
 Zadnja neenakost je izpolnjena, zato ker po trikotniški neenakosti (izrek
 \ref{neenaktrik}) velja $b+c-a>0$, $a+c-b>0$ in  $a+b-c>0$.
 Dokažimo še prvo neenakost:
 \begin{eqnarray*}
  && \frac{a\alpha+b\beta +c\gamma}{a+b+c} \geq 60^0\Leftrightarrow\\
  &\Leftrightarrow& a\alpha+b\beta +c\gamma - 60^0(a+b+c)\geq 0\\
  &\Leftrightarrow& a(\alpha-60^0)+b(\beta-60^0) +c(\gamma-60^0)\geq 0\\
  &\Leftrightarrow& a(3\alpha-180^0)+b(3\beta-180^0) +c(3\gamma-180^0)\geq 0\\
  &\Leftrightarrow& a(2\alpha-\beta-\gamma)+b(2\beta-\alpha-\gamma) +
  c(2\gamma-\alpha-\beta)\geq 0\\
  &\Leftrightarrow& a(\alpha-\beta+\alpha-\gamma)+b(\beta-\alpha+\beta-\gamma) +
  c(\gamma-\alpha+\gamma-\beta)\geq 0\\
  &\Leftrightarrow& a(\alpha-\beta)+a(\alpha-\gamma)+
  b(\beta-\alpha)+b(\beta-\gamma) +
  c(\gamma-\alpha)+c(\gamma-\beta)\geq 0\\
  &\Leftrightarrow& (a-b)(\alpha-\beta)+(a-c)(\alpha-\gamma)+
  (b-c)(\beta-\gamma) \geq 0
 \end{eqnarray*}
 Zadnja neenakost je posledica trditve \ref{vecstrveckotAlgeb}.
 \kdokaz

 Naslednji izrek bo motivacija za definiranje razdalje točke od
 premice.

             \bizrek Let $A'=pr_{\perp p}(A)$ be the foot of the perpendicular from a point  $A$ on a line $p$.
            If $X\in p$ and $X\neq A'$, then $AX>AA'$.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.17.pic}
\caption{} \label{sl.skl.3.2.17.pic}
\end{figure}

  \textbf{\textit{Proof.}}
 Po definiciji je $AA'\perp p$
(Figure \ref{sl.skl.3.2.17.pic}), kar pomeni, da je $AA'X$
 pravokotni trikotnik s hipotenuzo $AX$. Iz izreka
 \ref{vecstrveckotHipot} sledi $AX>AA'$.
 \kdokaz

 Če je $A'=pr_{\perp
p}(A)$, pravimo, da je dolžina daljice $AA'$ \index{razdalja!točke
 od premice} \pojem{razdalja točke $A$ od premice $p$}.
Označimo jo z $d(A,p)$. Torej $d(A,p)=|AA'|$.




%________________________________________________________________________________
 \poglavje{Circle and Line} \label{odd3KrozPrem}

V nadaljevanju se bomo ukvarjali s krožnico ter z medsebojno lego
krožnice in premice. Dokažimo najprej eno lastnost premera
krožnice, ki je enostavna posledica trikotniške neenakosti.


            \bizrek \label{premerNajdTetiva}
               The longest chord of a circle is its diameter.
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.1.pic}
\caption{} \label{sl.skl.3.3.1.pic}
\end{figure}

 \textbf{\textit{Proof.}}  Naj bosta
$AB$ poljubna tetiva krožnice, ki ni premer, in $C$ točka na
premici $AS$, za katero velja $CS\cong SA$ in $\mathcal{B}(A,S,C)$
(Figure \ref{sl.skl.3.3.1.pic}). Tedaj točka $C$ leži na
krožnici $k$ in je $AC$ njen premer. Dokazali smo že (posledica
izreka \ref{premerInS}), da so vsi premeri neke krožnice
medsebojno skladni. Zato je dovolj dokazati, da je $AC>AB$. To pa
sledi iz trikotniške neenakosti (trikotnik $ASB$). Velja:
 $$AC=AS+SC=AS+SB>AB,$$ kar je bilo treba dokazati. \kdokaz

Sledi še ena lastnost tetive krožnice, kot posledica izreka
\ref{vecstrveckotHipot}.


         \bzgled \label{tetivaNotrTocke}
        Every point that lies on a chord of a circle, except its endpoints,
         is an interior point of the circle.
         \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.2.pic}
\caption{} \label{sl.skl.3.3.2.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $X$ notranja točka tetive $AB$
s krajščema na krožnici $k(S,r)$ (Figure \ref{sl.skl.3.3.2.pic}). Kota $AXS$ in
$BXS$ sta sokota, kar pomeni, da nista oba ostra kota. Brez škode
za splošnost predpostavimo, da kot $BXS$ ni ostri kot. Tedaj je v
trikotniku $SXB$ stranica $SB$ najdaljša  (izrek
\ref{vecstrveckotHipot}), kar pomeni, da je:
 $$SX<SB=r.$$
Zaradi tega je $X$ notranja točka krožnice  $k(S,r)$.
 \kdokaz

Na podoben način bomo dokazali naslednji pomemben izrek.


        \bizrek \label{KrogKonv}
         A circular disc is a convex set.
          \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.3.pic}
\caption{} \label{sl.skl.3.3.3.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bosta $A$ in $B$ dve točki kroga
$\mathcal{K}(S,r)$ (Figure \ref{sl.skl.3.3.3.pic}). Potrebno je dokazati, da
cela daljica $AB$ leži v tem krogu, oz. da to velja za poljubno
točko $X$, za katero je $\mathcal{B}(A,X,B)$. Ker točki $A$ in $B$
ležita v krogu $\mathcal{K}$, potem velja
 $SA, SB\leq r$.
Podobno kot pri dokazu prejšnjega izreka zapišemo: ker je
$\mathcal{B}(A,X,B)$, potem vsaj eden izmed sokotov $AXS$ in $BXS$ ni
oster. Brez škode za splošnost naj bo $\angle BXS\geq 90^0$. Če
uporabimo izrek \ref{vecstrveckotHipot} za trikotnik $SXB$, dobimo:
$$SX<SB\leq r.$$
 Torej točka $X$ leži v krogu $\mathcal{K}$, kar pomeni, da je $\mathcal{K}$
konveksen lik.
 \kdokaz

Intuitivno je jasno, da imata lahko premica in krožnica  največ
dve skupni točki. To dejstvo sedaj lahko tudi dokažemo.

        \bizrek \label{KroznPremPresek}
        A line and a circle can have at most two common points.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.4.pic}
\caption{} \label{sl.skl.3.3.4.pic}
\end{figure}

\textbf{\textit{Proof.}} Predpostavimo nasprotno, da imata  krožnica
$k(S,r)$ in premica $p$ vsaj tri različne skupne točke: $A$,
$B$ in $C$, oz. $A,B,C\in p\cap k$ (Figure \ref{sl.skl.3.3.4.pic}). Če središče $S$ leži na premici $p$, potem na tej premici obstajata
le dve točki, ki sta od točke $S$ oddaljeni za polmer $r$ (izrek
\ref{ABnaPoltrakCX}). Naj bo $S\notin p$.
Iz pogoja $A,B,C\in p\cap k$ sledi  $SA=SB=SC=r$,
kar pomeni, da so trikotniki $ASC$, $ASB$ in $BSC$ enakokraki.
Brez škode za splošnost predpostavimo, da je
$\mathcal{B}(A,C,B)$. Iz tega sledi (izrek \ref{enakokraki}), da
so skladni tudi koti:
 $$\angle  SCA\cong \angle SAC \cong \angle SBC \cong \angle SCB.$$
Torej sta sokota $SCA$ in $SCB$ skladna in sta zaradi tega hkrati
prava kota. Potem je  tudi kot $SAC$ pravi kot. To pa ni mogoče,
ker bi v tem primeru trikotnik $SAC$ imel dva  prava notranja kota.
To pomeni, da predpostavka $A,B,C\in p\cap k$ odpade. \kdokaz

 Iz izreka \ref{KroznPremPresek} torej sledi, da imata lahko premica in krožnica  dve, eno ali pa
nobene skupne točke. V prvem primeru pravimo, da se premica
 in krožnica
 \pojem{sekata}, v drugem primeru se \pojem{dotikata}, v tretjem
 primeru pa sta
 \pojem{mimobežni} (Figure
\ref{sl.skl.3.3.5.pic}). Premica je v prvem primeru \index{sekanta
krožnice}\pojem{sekanta} ali \pojem{sečnica}, v drugem primeru
\index{tangenta krožnice}\pojem{tangenta} ali \pojem{dotikalnica}
in v tretjem primeru \index{mimobežnica
krožnice}\pojem{mimobežnica}. Točko, v kateri se tangenta dotika krožnice, imenujemo \index{dotikališče}
\pojem{dotikališče}.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.5.pic}
\caption{} \label{sl.skl.3.3.5.pic}
\end{figure}

Za tangento pogosto uporabljamo naslednji kriterij, ki je
pravzaprav potreben in zadosten pogoj, da je neka premica tangenta
krožnice.


        \bizrek \label{TangPogoj}
        Let $T$ be a point lying on the circle $k(S, r)$. A line
        $PT$ (lying in the plane of the circle) is a tangent of the circle at the point $T$ if and only if $PT \perp TS$.
        \eizrek


\textbf{\textit{Proof.}}  ($\Rightarrow$) Naj bo $PT$ tangenta
krožnice $k$ v točki $T$. Če kot $PTS$ ni pravi kot, je  eden
izmed kotov, ki ga določata premici $PT$ in $TS$ oster. Brez škode za
splošnost naj bo $\angle STX =w < 90°$ (Figure
\ref{sl.skl.3.3.6.pic}). Z $l$ označimo
 poltrak z izhodiščem $S$, ki leži v polravnini $STX$, tako da je
 $\angle ST,l = 180° - 2w $. Če je $Y$ presečišče poltrakov $TX$ in $l$, je
trikotnik $STY$ enakokrak ($\angle STY = \angle SYT =w$ ) in je
$ST = SY = r$. To pa ni možno, ker je $PT$ tangenta krožnice $k$
in imata eno samo skupno točko. Torej je  $\angle PTS$ pravi
kot oz. $PT \perp TS$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.6.pic}
\caption{} \label{sl.skl.3.3.6.pic}
\end{figure}

($\Leftarrow$) Naj bo sedaj $PT \perp TS$ (Figure
\ref{sl.skl.3.3.6.pic}). Za vsako točko $T_1\in PT$  ($T_1 \neq T$)
je $STT_1$ pravokotni trikotnik s hipotenuzo $ST_1$ in potem
velja (izrek \ref{vecstrveckotHipot}):
 $$ST_1 > ST = r.$$
 Torej nobena od točk $T_1$ ($T_1 \neq T$), ki ležijo na
premici $PT$, ne leži na krožnici $k$. To pomeni, da je premica
$PT$ tangenta te krožnice.
 \kdokaz

Iz dokaza prejšnjega izreka ($\Leftarrow$) sledi, da so vse
točke, ki ležijo na tangenti krožnice (razen njenega
dotikališča), zunanje točke te krožnice. S pomočjo te
lastnosti bomo dokazali naslednjo trditev.


        \bzgled \label{tangKrozEnaStr}
        All points of a circle are on the one side of its tangent.
        \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.7.pic}
\caption{} \label{sl.skl.3.3.7.pic}
\end{figure}

\textbf{\textit{Proof.}}  Naj bo $T$ dotikališče krožnice $k(S, r)$
in njene tangente $t$ (Figure \ref{sl.skl.3.3.7.pic}). Tangenta $t$
deli ravnino, v kateri ležita $k$ in $t$, na dve polravnini. Tisto
polravnino, v kateri leži točka $S$, označimo z $\alpha_1$, drugo
polravnino pa z $\alpha_2$. Dokažimo, da vse točke krožnice $k$
ležijo v polravnini $\alpha_1$. Naj bo $X$ poljubna točka polravnine
$\alpha_2$. Ker sta
 točki $S$ in $X$ na različnih straneh premice $t$, sledi da jo odprta
daljica $SX$ seka v neki točki $Y$. Potem velja:
 $$SX = SY + YX > SY \geq ST = r,$$
  kar pomeni, da točka $X$ ne leži na krožnici $k$ in je njena
zunanja točka. Torej nobena od točk polravnine $\alpha_2$ ne
leži na krožnici $k$, oz.  so vse  v  polravnini
$\alpha_1$ z robom $t$. \kdokaz

Direktna posledica izreka \ref{TangPogoj} je tudi ta, da v vsaki
točki krožnice lahko narišemo eno samo tangento. Če je $X$
notranja točka krožnice $k(S, r)$, potem skozi to točko ne
poteka nobena tangenta, saj so vse premice skozi $X$
sekante, kar je posledica Dedekindovega aksioma (izrek
\ref{DedPoslKrozPrem}). Kasneje (izrek \ref{tangentiKroznice})
bomo ugotovili, da lahko skozi vsako zunanjo točko krožnice
narišemo natanko dve tangenti. Zaenkrat dokažimo naslednjo
trditev (bralec se bo spomnil, da gre za trditev, ki smo jo
obravnavali že na samem začetku v uvodnem poglavju - trditev
\ref{TalesUvod}).


            \bizrek \label{TalesovIzrKroz} \index{izrek!Talesov za krožnico}
            Thales' theorem for a circle\footnote{Starogrški
            filozof in matematik \textit{Tales}
            \index{Tales} iz Mileta (640--546 pr. n. š.)
             ni prvi, ki je odkril to trditev. Kot empirično dejstvo so jo poznali
             že stari Egipčani in Babilonci. Izrek imenujemo po Talesu, ki ga je prvi dokazal.
             V dokazu je uporabljal lastnosti enakokrakih trikotnikov in dejstvo, da je
             vsota notranjih kotov trikotnika enaka vsoti dveh pravih kotov. Torej je
             dokaz enak temu, ki ga bomo izpeljali tukaj.}:\\
            Let $AB$ be a diameter of a circle $k$. Then for any point $X$ of this circle different from $A$ and $B$
            ($X\in k$ in $X\neq A$ in $X\neq B$) is $\angle AXB=90^0$
            \index{izrek!Talesov za krožnico}
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.8.pic}
\caption{} \label{sl.skl.3.3.8.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $O$ središče krožnice $k$ (Figure
\ref{sl.skl.3.3.8.pic}). Ker $A,B,X\in k$, je
 $OA\cong OB\cong OX$. Torej sta
 trikotnika $AOX$ in $BOX$  enakokraka, zato je (izrek
\ref{enakokraki}):
 $\angle AXO\cong\angle XAO=\alpha$ in $\angle BXO\cong\angle XBO=\beta$.
Tedaj je $\angle AXB=\alpha+\beta$.
 Vsota notranjih kotov v
trikotniku $AXB$ je enaka $180^0$ (izrek \ref{VsotKotTrik}), torej
je $2\alpha+2\beta=180^0$. Iz tega sledi
 $$\angle AXB=\alpha+\beta=90^0,$$ kar je bilo treba dokazati. \kdokaz

 Dokažimo tudi obratno trditev.


             \bizrek \label{TalesovIzrKrozObrat}
            If $A$, $B$ and $X$ are non-collinear points such that
            $\angle AXB=90^0$, then the point $X$ lies on a circle with the diameter $AB$.
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.9.pic}
\caption{} \label{sl.skl.3.3.9.pic}
\end{figure}


\textbf{\textit{Proof.}} Naj bo $O$ središče daljice $AB$ in $k$
krožnica s središčem $O$ in polmerom $OA$ oz. premerom $AB$
(Figure \ref{sl.skl.3.3.9.pic}). Iz $\angle AXB=90^0$ je po izreku
\ref{VsotKotTrik}:
 \begin{eqnarray}
 \angle XAB+ \angle XBA = 90^0 \label{relacija336}
 \end{eqnarray}

Dokažimo $X\in k$. Predpostavimo nasprotno, torej da točka $X$ ne
leži na krožnici $k$. V tem primeru je $OX\neq OA$. Naj bo $X_1$
točka na poltraku $OX$, za katero je $OX_1\cong OA$ (izrek
\ref{ABnaPoltrakCX}). To pomeni, da točka $X_1$ leži na krožnici
$k$ in po Talesovem izreku \ref{TalesovIzrKroz} velja $\angle
AX_1B=90^0$.

Po naši predpostavki $OX\neq OA$ je jasno, da $X\neq X_1$.
Obravnavali bomo dve možnosti:

\textit{1)} Naj bo $OX_1<OX$ oz. $\mathcal{B}(O,X_1,X)$. V tem
primeru je $X_1$ notranja točka kotov $XAB$ in $XBA$, zato je
$\angle X_1AB<\angle XAB$ in $\angle X_1BA<\angle XBA$. Iz tega in
relacije \ref{relacija336} sledi:
 $$\angle X_1AB+ \angle X_1BA<\angle XAB+ \angle XBA = 90^0.$$
 Ker je še $\angle AX_1B=90^0$, je vsota kotov v trikotniku $AX_1B$
 manjša od $180^0$, kar po izreku \ref{VsotKotTrik} ni mogoče.


\textit{2)} Naj bo $OX_1>OX$ oz. $\mathcal{B}(O,X,X_1)$. Podobno
kot v prvem primeru dobimo:
 $$\angle X_1AB+ \angle X_1BA>\angle XAB+ \angle XBA = 90^0.$$
 V tem primeru je vsota kotov v trikotniku $AX_1B$ večja od
$180^0$, kar  po izreku \ref{VsotKotTrik} ni mogoče.

Iz tega sledi, da je $OX=OX_1$  oz. $X\in k$.
 \kdokaz


 Uporabimo prejšnja izreka za načrtovanje tangent.


             \bzgled \label{tangKrozKonstr}
             Let $A$ be an exterior point of a circle $k(S,r)$.
             Construct all tangents of this circle passing through the point $A$.
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.10.pic}
\caption{} \label{sl.skl.3.3.10.pic}
\end{figure}


 \textbf{\textit{Solution.}} Naj bo $l$ krožnica s premerom $SA$
(Figure \ref{sl.skl.3.3.10.pic}). Ker je $S$ notranja, $A$ pa zunanja
točka dane krožnice $k$, imata krožnici $k$ in $l$ natanko
dve skupni točki $T_1$ in $T_2$ (izrek \ref{DedPoslKrozKroz}).
Po Talesovem izreku \ref{TalesovIzrKroz} je
$\angle ST_1A\cong \angle ST_2A=90^0$. Ker sta $ST_1$ in  $ST_2$
polmera krožnice $k$, sta $AT_1$ in $AT_2$ tangenti krožnice $k$
skozi točko $A$ (izrek \ref{TangPogoj}).

 Dokažimo, da sta $AT_1$ in $AT_2$ edini tangenti krožnice $k$
 iz točke $A$. Če je $AT$ tangenta iz točke $A$, ki se krožnice $k$
 dotika v točki $T$, je po izreku \ref{TangPogoj} $\angle ATS=90^0$.
 To pomeni, da točka $T$ leži na krožnici $l$
 (izrek \ref{TalesovIzrKrozObrat}) oz. $T\in k\cap l$. Torej $T$ je ena
 od točk $T_1$ in $T_2$, zato sta $AT_1$ in $AT_2$ edini tangenti krožnice
  $k$ iz točke $A$.
  \kdokaz

  Iz prejšnje konstrukcije sledi naslednji izrek.



        \bizrek \label{tangentiKroznice}
         If $V$ is an exterior point of a circle $k(S,r)$, then there are exactly
       two tangents of the circle $k$ through the point $V$.
        \eizrek


 Dokažimo še nekaj lastnosti tangent krožnice.


            \bzgled \label{TangOdsek}
            If $VA$ and $VB$ are tangents of a circle $k(S,r)$ in a points
            $A$ and $B$ of the circle, then the centre $S$ lies on the bisector
            of the angle $AVB$ and $VA \cong VB$.
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.11.pic}
\caption{} \label{sl.skl.3.3.11.pic}
\end{figure}


\textbf{\textit{Proof.}} Iz izreka \ref{TangPogoj} sledi: $VA
\perp AS$ in $VB \perp BS$
(Figure \ref{sl.skl.3.3.11.pic}). Torej sta $ASV$ in $BSV$  pravokotna
trikotnika s skupno hipotenuzo $SV$. Ker je še $SA \cong SB = r$,
sta ta dva trikotnika skladna (izrek \textit{SSA} \ref{SSK}). Torej sta tudi kota
$AVS$ in $BVS$  skladna, kar pomeni, da je premica $VS$
simetrala kota $AVB$. Iz skladnosti teh dveh trikotnikov sledi
tudi $VA \cong VB$.
 \kdokaz

Velja tudi obratna trditev.


             \bzgled \label{SimKotaKraka}
             If a point $S$ lies on the bisector of a convex angle,
            then it is the centre of a circle touching both sides of this angle.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.12.pic}
\caption{} \label{sl.skl.3.3.12.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bosta $A$ in $B$ pravokotni projekciji
točke $S$ na krakih danega kota z vrhom $V$ (Figure
\ref{sl.skl.3.3.12.pic}). Trikotnika $ASV$ in $BSV$ sta skladna
(izrek \textit{ASA} \ref{KSK}), ker imata skupno stranico $VS$ in
dva para skladnih kotov - iz $\angle AVS\cong \angle BVS$ in $\angle
SAV\cong \angle SBV=90^0$ sledi $\angle ASV\cong \angle BSV$. Zaradi
tega velja $SA\cong SB$ in je  $k(S,SA)$  iskana krožnica. Kraka
danega kota sta namreč  po izreku \ref{TangPogoj} tangenti krožnice.
 \kdokaz

Sedaj bomo dokazali še en kriterij o medsebojni legi premice in
krožnice v ravnini.



        \bizrek \label{TangSekMimobKrit}
        Let $P$ be the foot of the perpendicular from the centre of a circle  $k(S,r)$
            on a line $p$ (lying in the plane of the circle). Then the line $p$ is:

        (i) secant, if and only if $SP < r$;

        (ii) tangent, if and only if  $SP \cong r$;

         (iii) non-intersecting line,  if and only if  $SP> r$.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.13.pic}
\caption{} \label{sl.skl.3.3.13.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.3.13.pic})

Trditev (ii) sledi direktno iz kriterija
za tangento (izrek \ref{TangPogoj}).

(i) V dokazu direktne smeri ekvivalence uporabljamo dejstvo, da je
hipotenuza pravokotnega trikotnika daljša od obeh katet (izrek
\ref{vecstrveckotHipot}). Če sta $A$ in $B$ presečišči sekante $p$
in krožnice $k$, je $SA$ hipotenuza pravokotnega trikotnika $ASP$ in
velja:
 $r \cong SA > SP$.

 V dokazu obratne smeri
ekvivalence uporabimo  posledico Dedekindovega aksioma (izrek
\ref{DedPoslKrozPrem}). Ker je v tem primeru $P$ notranja točka te
krožnice, je vsaka premice te ravnine, ki gre skozi
točko $P$, sekanta krožnice $k$.

(iii) Sledi iz dokazanega (i) in (ii). Če je namreč $SP > r$,
potem ni niti $SP < r$ niti $SP \cong r$. Iz ekvivalenc (i) in (ii)
sledi, da premica $p$ ni niti sekanta niti tangenta. Zato je $p$
mimobežnica krožnice $k$. Na isti način dokazujemo tudi obratno smer
ekvivalence.
  \kdokaz

%________________________________________________________________________________
 \poglavje{Quadrilaterals} \label{odd3Stirik}


V razdelku \ref{odd2AKSURJ} smo  pojem štirikotnika vpeljali kot
večkotnik, ki ima štiri stranice in štiri oglišča.
Definirali smo pojme sosednji in nasprotni stranici, sosednji in
nasprotni koti ter diagonalo. Štirikotniku $ABCD$ dolžine
njegovih stranic $AB$, $BC$, $CD$ in $DA$ običajno označimo z $a$,
$b$, $c$ in $d$, dolžini njegovih diagonal $AC$ in $BD$ pa z $e$ in
$f$  (Figure \ref{sl.skl.3.4.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.1.pic}
\caption{} \label{sl.skl.3.4.1.pic}
\end{figure}

 V istem razdelku  smo kot pojme vpeljali  notranje
  in zunanje kote štirikotnika. Omenili smo tudi, da notranje kote ob ogliščih $A$, $B$, $C$ in $D$ štirikotnika $ABCD$
   navadno označimo
   z $\alpha$, $\beta$, $\gamma$ in $\delta$, njegove zunanje kote
    pa z $\alpha'$, $\beta'$, $\gamma'$ in $\delta'$.
Dokazali smo (posledica splošnega izreka \ref{VsotKotVeck}), da je
vsota vseh štirih notranjih kotov poljubnega štirikotnika
enaka $360^0$ (Figure \ref{sl.skl.3.4.1.pic}). Enaka  je tudi vsota zunanjih kotov (v konveksnem štirikotniku). Torej:
 \begin{eqnarray*}
 \alpha+\beta+\gamma+\delta=360^0,\\
 \alpha'+\beta'+\gamma'+\delta'=360^0
 \end{eqnarray*}

Dodajmo še, da za notranja kota pravimo, da sta
\index{kota!sosednja} \pojem{sosednja} oz. \index{kota!nasprotna} \pojem{nasprotna}, če sta pripadajoči oglišči sosednji oz. nasprotni.



Sedaj bomo nekatere vrste štirikotnikov podrobneje obravnavali.

 Štirikotnik
$ABCD$ je \index{trapez}\pojem{trapez}, če je $AB\parallel CD$ (Figure \ref{sl.skl.3.4.2.pic}).
Stranici $AB$ in $CD$ sta \index{osnovnica!trapeza}
\pojem{osnovnici}, $BC$ in $AD$ pa
\index{krak!trapeza}\pojem{kraka} tega trapeza.
Daljica $PQ$ ($P\in AB$, $Q\in CD$ in $PQ\perp AB$) je \index{višina!trapeza}\pojem{višina trapeza}. Pogosto jo označimo z $v$.


Trapez je
 \index{trapez!enakokraki}\pojem{enakokraki},
 Če je $BC \cong AD$ in ni $BC \parallel AD$,
 oz. \index{trapez!pravokotni}\pojem{pravokotni}, če je vsaj
eden  notranji kot pravi.




\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.2.pic}
\caption{} \label{sl.skl.3.4.2.pic}
\end{figure}


Dva notranja kota ob istem kraku trapeza sta suplementarna, ker
sta kota z vzporednima krakoma (izrek \ref{KotiTransverzala}). Suplementarnost teh kotov je tudi
zadosten pogoj, da je štirikotnik trapez. Iz tega sledi, da ima pravokotni trapez  vsaj dva prava notranja kota.


Kot posebno vrsto trapezov dobimo še eno skupino štirikotnikov.
To so \pojem{paralelogrami}. Možno jih je definirati na različne načine.
Izbrali bomo enega, za vse ostale pa bomo
dokazali, da so ekvivalentni.

Štirikotnik $ABCD$ je \index{paralelogram} \pojem{paralelogram}, če
velja $AB
\parallel CD$ in $AD \parallel BC$ (Figure \ref{sl.skl.3.4.3.pic}).
Daljici $PQ$ ($P\in AB$, $Q\in CD$ in $PQ\perp AB$) in $MN$ ($M\in BC$, $N\in AD$ in $MN\perp BC$) sta
  \index{višina!paralelograma}\pojem{višini paralelograma}. Pogosto ju označimo z $v_a$ in $v_b$.



\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.3.pic}
\caption{} \label{sl.skl.3.4.3.pic}
\end{figure}

 Paralelogram je torej štirikotnik, ki ima dva para
vzporednih stranic. V definiciji paralelograma ni uporabljen pojem
skladnosti. Paralelograme (tudi trapeze) lahko obravnavamo
tudi v t. i. \index{geometrija!afina} \pojem{afini geometriji}.
To je geometrija, ki je zasnovana na vseh aksiomah evklidske
geometrije, če iz seznama izključimo aksiome tretje skupine -
aksiome skladnosti.

Dokažimo sedaj že omenjene ekvivalente za definicijo
paralelograma.


            \bizrek  \label{paralelogram}
            Let $ABCD$ be a convex quadrilateral.
            Then the following statements are equivalent:
            \begin{enumerate}
              \item The quadrilateral $ABCD$ is a parallelogram.
              \item Any two adjacent interior angles of  the quadrilateral $ABCD$ are supplementary.
              \item Any two opposite interior angles of  the quadrilateral $ABCD$ are congruent.
             \item $AB \parallel CD$ and $AB \cong CD$\footnote{Ta ekvivalent
                v nekoliko drugačni obliki navaja \index{Evklid}
                \textit{Evklid iz Aleksandrije} (3. stol. pr. n. š.) v
                prvi knjigi svojih ‘‘Elementov’’.}.
             \item $AB \cong CD$ and $AD \cong BC$.
             \item The diagonals of the quadrilateral $ABCD$ bisect each other, i.e.
               line segments $AC$ and $BD$ have a common midpoint.
            \end{enumerate}
             \eizrek

 \textbf{\textit{Proof.}}
Potrebno je dokazati ekvivalentnost vseh izjav $(1)-(6)$. Da bi se
izognili dokazovanju vseh ekvivalenc (po dve implikaciji - npr. z
izjavo (1), kar bi skupaj dalo 10 implikacij), bomo dokaz nekoliko
poenostavili, tako da dokažemo implikacije po naslednji shemi.

\vspace*{5mm}
\hspace*{25mm}
$\begin{array}{ccccccc}
  \textit{(1)} & \Leftarrow & \textit{(2)} & \Leftarrow & \textit{(3)} &   &   \\
  \Downarrow &   &   &   & \Uparrow &   &   \\
  \textit{(4)} &   & \Rightarrow &   & \textit{(5)} & \Leftrightarrow & \textit{(6)}
\end{array}$

\vspace*{5mm}

 Kot vidimo, je to dovolj, ker implikacija $\textit{(1)}
\Rightarrow \textit{(2)}$ sledi direktno iz: $\textit{(1)}\Rightarrow \textit{(4)}\Rightarrow
\textit{(5)}\Rightarrow \textit{(3)} \Rightarrow \textit{(2)}$.

Označimo z $\alpha$, $\beta$, $\gamma$ in $\delta$ notranje kote pri
ogliščih $A$, $B$, $C$ in $D$ štirikotnika $ABCD$. Štirikotnik
$ABCD$ je konveksen, kar pomeni, da se njegovi diagonali sekata v
neki točki $S$.

$\textit{(2)}\Rightarrow \textit{(1)}$. Naj bosta kota $\alpha$ in
$\beta$ suplementarna  (Figure \ref{sl.skl.3.4.4.pic}). Potem sta to
kota ob transverzali $AB$ premic $AD$ in $BC$, zato je $AD\parallel
BC$ (izrek \ref{KotiTransverzala}). Podobno iz suplementarnosti
kotov $\beta$ in $\gamma$ sledi $AB\parallel CD$. Torej je štirikotnik
$ABCD$ paralelogram.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4.pic}
\caption{} \label{sl.skl.3.4.4.pic}
\end{figure}

$\textit{(3)}\Rightarrow\textit{(2)}$. Naj bo $\alpha =\gamma$ in $\beta =\delta$ (Figure \ref{sl.skl.3.4.4.pic}).
Ker je $\alpha + \beta +\gamma +\delta = 360°$ (vsota vseh
notranjih kotov v štirikotniku je $360°$ - izrek \ref{VsotKotVeck}), sledi
$\alpha + \beta =180°$ in $\beta +\gamma = 180°$.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4a.pic}
\caption{} \label{sl.skl.3.4.4a.pic}
\end{figure}

$\textit{(1)}\Rightarrow\textit{(4)}$. Naj bo štirikotnik $ABCD$
paralelogram, oz. naj velja $AB \parallel CD$ in $AD \parallel BC$
(Figure \ref{sl.skl.3.4.4a.pic}). Dokažimo, da je potem tudi $AB \cong CD$.
Premica $AC$ je transverzala vzporednic $AB$ in $CD$, kar
pomeni, da sta kota $CAB$ in $ACD$ izmenična kota na tej
transverzali in sta zato skladna. Podobno iz vzporednosti premic
$AD$ in $BC$ sledi, da sta tudi kota $ACB$ in $CAD$ skladna. Ker je
$AC \cong AC$, sta trikotnika $ACB$ in $CAD$ skladna (izrek
\ref{KSK} - \textit{ASA}). Zato je  $AB \cong CD$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4b.pic}
\caption{} \label{sl.skl.3.4.4b.pic}
\end{figure}

 $\textit{(4)}\Rightarrow \textit{(5)}$. Naj bo $ABCD$ takšen štirikotnik, da velja
 $AB \parallel CD$ in $AB \cong CD$ (Figure \ref{sl.skl.3.4.4b.pic}).
 Dokažimo, da je  $AD \cong BC$.
 Premica $AC$ je transverzala vzporednic $AB$ in
$CD$, kar pomeni, da sta kota $CAB$ in $ACD$ izmenična kota ob tej
transverzali in sta zato skladna. Ker je še $AC \cong AC$, sta
trikotnika $ACB$ in $CAD$ skladna (izrek \ref{SKS} - \textit{SAS}). Zato je
$BC \cong AD$.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4c.pic}
\caption{} \label{sl.skl.3.4.4c.pic}
\end{figure}

 $\textit{(5)}\Rightarrow \textit{(3)}$. Naj bo $ABCD$ takšen štirikotnik, da je $AB \cong CD$ in
 $AD \cong BC$ (Figure \ref{sl.skl.3.4.4c.pic}). Dokažimo, da
je potem $\beta =\delta$ in $\alpha =\gamma$. Ker je še $AC \cong
AC$, sta trikotnika $ACB$ in $CAD$ skladna (izrek \ref{SSS} - \textit{SSS}).
Iz tega sledi $\angle ABC \cong \angle CDA$ oz. $\beta =\delta$. Na
podoben način dokažemo tudi $\alpha =\gamma$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4d.pic}
\caption{} \label{sl.skl.3.4.4d.pic}
\end{figure}

$\textit{(5)}\Leftrightarrow \textit{(6)}$. Naj bo $ABCD$ takšen štirikotnik, da
je $AB \cong CD$ in $AD \cong BC$ (Figure \ref{sl.skl.3.4.4d.pic}). Dokažimo, da je točka $S$
skupno središče njegovih diagonal $AC$ in $BD$. Ker je $AC \cong
AC$ je $\triangle ACB \cong \triangle CAD$ (izrek \ref{SSS} - \textit{SSS}). Zato
je $\angle ACB \cong \angle CAD$ oz. $\angle SCB \cong \angle
SAD$. Iz skladnosti sovršnih kotov $CSB$ in $ASD$ sledi, da sta
skladna tudi kota $SBC$ in $SDA$. Ker je še $AD \cong BC$, sledi
$\triangle CSB \cong \triangle ASD$ (izrek \ref{KSK} - \textit{ASA}). Zato je $SB
\cong SD$ in $SC \cong SA$ oz. točka $S$ je skupno središče
diagonal $AC$ in $BD$.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4e.pic}
\caption{} \label{sl.skl.3.4.4e.pic}
\end{figure}


Obratno, naj bo $S$ skupno središče diagonal $AC$ in $BD$ (Figure \ref{sl.skl.3.4.4e.pic}). Tedaj
je $SB \cong SD$ in $SC \cong SA$. Skladna sta tudi sovršna kota
$CSB$ in $ASD$, zato je $\triangle CSB \cong \triangle ASD$ (izrek
\ref{SKS} - \textit{SAS}). Iz tega sledi $AD \cong BC$. Na podoben način
dokažemo tudi $AB \cong CD$.
 \kdokaz

Bralcu priporočamo, da dokaže prejšnji izrek z uporabo neke
podobne sheme. To bo dobra vaja za uporabo izrekov o skladnosti
trikotnikov.

Definirajmo sedaj še neke vrste štirikotnikov, za katere se bo
izkazalo, da so posebni primeri paralelogramov (Figure
\ref{sl.skl.3.4.5.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.5.pic}
\caption{} \label{sl.skl.3.4.5.pic}
\end{figure}

Štirikotnik, ki ima vse stranice skladne, imenujemo \index{romb}
\pojem{romb}.

Štirikotnik, pri katerem so vsi notranji koti skladni (in torej
enaki $90^0$, ker je njihova vsota $360^0$), je \index{pravokotnik}
\pojem{pravokotnik}.

Štirikotnik, pri katerem so vse stranice skladne in vsi notranji
koti skladni (in enaki $90^0$), imenujemo \index{kvadrat}
\pojem{kvadrat}.


Ni težko dokazati, da je vsak od teh štirikotnikov hkrati
paralelogram. To je direktna posledica prejšnjega izreka. Romb je
paralelogram zaradi $\textit{(5)}\Rightarrow\textit{(1)}$; pravokotnik pa zaradi
$\textit{(2)}\Rightarrow\textit{(1)}$ (ali $\textit{(3)}\Rightarrow\textit{(1)}$). Za kvadrat je
jasno, da je hkrati pravokotnik in romb, zato je tudi
paralelogram.

Iz prejšnjega izreka \ref{paralelogram} - ekvivalent (\textit{5}) sledi,
da je paralelogram, ki ima dve sosednji stranici skladni, romb. Prav tako
 po istem izreku iz ekvivalentov \textit{(2)} in \textit{(3)} sledi,
 da je paralelogram, ki ima vsaj en pravi kot, pravokotnik.

Naslednji izrek daje dodatne kriterije, kdaj je paralelogram hkrati romb,
pravokotnik oz. kvadrat. Ta izrek se nanaša na diagonale. Pri
paralelogramu se diagonali vedno razpolavljata, toda pri rombu,
pravokotniku in kvadratu bomo imeli še dodatne lastnosti.



        \bizrek \label{RombPravKvadr} $ $  (Figure \ref{sl.skl.3.4.5a.pic})

        a) A parallelogram is a rhombus if and only if their diagonals are perpendicular.

         b) A parallelogram is a rectangle if and only if their diagonals are congruent.

        c) A parallelogram is a square if and only if their diagonals are perpendicular and congruent.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.5a.pic}
\caption{} \label{sl.skl.3.4.5a.pic}
\end{figure}

 \textbf{\textit{Proof.}}
 Naj bo $ABCD$ paralelogram in $S$ presečišče njegovih diagonal $AC$ in $BD$. Po
prejšnjem izreku \ref{paralelogram} je točka $S$ njuno skupno
središče. Iz istega izreka sledi tudi $AB \cong CD$ in $AD \cong
BC$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.6.pic}
\caption{} \label{sl.skl.3.4.6.pic}
\end{figure}

\textit{a)}  (Figure \ref{sl.skl.3.4.6.pic})

 Če je $ABCD$ romb, ima vse stranice skladne. Zato sta
trikotnika $ABS$ in
  $ADS$
skladna (izrek \ref{SSS} - \textit{SSS}). Potem sta skladna tudi kota $ASB$
in $ASD$ in sta (kot sokota) oba prava kota. To pomeni, da sta
diagonali pravokotni.

Če sta diagonali paralelograma $ABCD$ pravokotni, sta trikotnika
$ABS$ in $ADS$ skladna (izrek \ref{SKS} - \textit{SAS}). Zato sta stranici
$AB$ in $AD$ skladni. Na podoben način dokazujemo, da so skladne
vse stranice tega paralelograma, kar pomeni, da je paralelogram
romb.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.6a.pic}
\caption{} \label{sl.skl.3.4.6a.pic}
\end{figure}


\textit{b)}  (Figure \ref{sl.skl.3.4.6a.pic})

 Če je $ABCD$ pravokotnik, ima vse notranje kote skldne in prave. Tedaj
sta trikotnika $ABC$ in $DCB$ skladna (izrek \ref{SKS} - \textit{SAS}).
Zato je $AC \cong DB$.

Če pri paralelogramu $ABCD$ velja $AC \cong DB$, sta trikotnika
$ABC$ in $DCB$ skladna (izrek \ref{SSS} - \textit{SSS}). Iz tega sledi, da
sta skladna notranja kota pri ogliščih $B$ in $D$ paralelograma
$ABCD$. Po prejšnjem izreku \ref{paralelogram} sta kota
suplementarna, kar pomeni, da sta oba prava kota. Analogno so pravi
tudi vsi koti tega paralelograma, zato je paralelogram pravokotnik.

 \textit{c)} Paralelogram je kvadrat natanko tedaj, ko je hkrati romb in pravokotnik.
 Slednje je pa
izpolnjeno natanko tedaj, ko sta diagonali pravokotni in
skladni, kar sledi iz dokazanega  (\textit{a.} in \textit{b.}).
 \kdokaz


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.7.pic}
\caption{} \label{sl.skl.3.4.7.pic}
\end{figure}



Ker sta diagonali pravokotnika skladni in se razpolavljata,
obstaja krožnica, ki vsebuje vsa oglišča tega pravokotnika (Figure \ref{sl.skl.3.4.7.pic}). To
je t. i. \index{očrtana krožnica!pravokotnika} \pojem{očrtana
krožnica pravokotnika}. Njeno središče je presečišče
njegovih diagonal. Če je namreč točka $S$ presečišče
diagonal pravokotnika $ABCD$, potem iz prejšnjega izreka
\ref{RombPravKvadr} sledi:
 $$SA \cong SC \cong SB \cong SD.$$
Polmer te krožnice je enak polovici diagonale pravokotnika. Ker
je kvadrat posebna vrsta pravokotnika, tudi za njega obstaja
očrtana krožnica.

Dokažimo sedaj še pomembno lastnost enakokrakih trapezov.


     \bizrek \label{trapezEnakokraki}
     Interior base angles of an isosceles trapezium are congruent.
     The diagonals of an isosceles trapezium are congruent line segments.
     \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.8.pic}
\caption{} \label{sl.skl.3.4.8.pic}
\end{figure}

  \textbf{\textit{Proof.}}
  Naj bo $ABCD$ enakokraki trapez z osnovnico $AB$ (Figure \ref{sl.skl.3.4.8.pic}). Brez škode za splošnost predpostavimo, da je $AB>CD$. Po definiciji enakokrakega trapeza je $BC\cong AD$. Označimo s $C'$ in $D'$ pravokotni projekciji oglišč $C$ in $D$ na premici $AB$. Štirikotnik $D'C'CD$ je paralelogram s pravim kotom, zato je pravokotnik. Že iz dejstva, da je $D'C'CD$ paralelogram, sledi $CC'\cong DD'$ (izrek \ref{paralelogram}). Ker je še $\angle CC'B\cong \angle DD'A=90^0$, sta trikotnika $CC'B$ in $DD'A$ skladna (izrek \textit{SSA} \ref{SSK}), zato je $\beta=\angle CBC'\cong \angle DAD'=\alpha$.

  Dokažimo še, da sta diagonali $AC$ in $BD$ skladni. To sledi iz skladnosti trikotnikov $ABC$ in $BAD$ (izrek \textit{SAS} \ref{SKS}).
  \kdokaz


            \bzgled
            Let $ABCD$, $AEBK$ and $CEFG$ be equally oriented squares in a plane.
            Then $B$, $D$ and $F$ are collinear points and the point $B$ is a midpoint of the line segment $DF$.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.9.pic}
\caption{} \label{sl.skl.3.4.9.pic}
\end{figure}

 \textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.4.9.pic})

 Trikotnika $CAE$ in $FBE$ sta skladna, ker je $CE\cong FE$, $AE\cong BE$  in
 $\angle AEC=90^0-\angle CEB=\angle BEF$ (izrek \ref{SKS} - \textit{SAS}). Zato je
 $\angle EBF$ pravi kot  in so točke $D$, $B$ in $F$ kolinearne. Iz
 skladnosti teh dveh trikotnikov sledi tudi $BF\cong AC\cong BD$.
  \kdokaz


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10.pic}
\caption{} \label{sl.skl.3.4.10.pic}
\end{figure}

Razen trapezov in paralelogramov bomo definirali še eno novo skupino
štirikotnikov. Štirikotnik $ABCD$ je
\index{deltoid}\pojem{deltoid}, če sta njegovi diagonali pravokotni in
ena od diagonal razpolavlja drugo (Figure \ref{sl.skl.3.4.10.pic}).
Naslednji izrek se nanaša na deltoid in je ekvivalent njegove
definicije.


        \bzgled
        A quadrilateral is a deltoid if and only if it has two pairs of congruent adjacent sides.
        \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.11.pic}
\caption{} \label{sl.skl.3.4.11.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.4.11.pic})

 Naj bo štirikotnik $ABCD$ deltoid. Tedaj sta diagonali
$AC$ in $BD$ pravokotni in ena od diagonal razpolavlja drugo. Brez
škode za splošnost naj diagonala $BD$ razpolavlja diagonalo $AC$.
Sledi, da sta pravokotna trikotnika $ABS$ in $CBS$ skladna (izrek
\ref{SKS} - \textit{SAS}). Potem je $AB \cong CB$. Iz skladnosti
trikotnikov $ADS$ in $CDS$ pa sledi $AD \cong CD$.

 Naj bo $ABCD$ štirikotnik, v katerem velja $AB \cong CB$ in $AD \cong CD$.
 Trikotnika $ABD$ in $CBD$ sta
skladna (izrek \ref{SSS} - \textit{SSS}), zato sta skladna tudi kota $ADS$
in $CDS$. Iz tega sledi, da sta skladna tudi trikotnika $ADS$ in
$CDS$ (izrek \ref{SKS} - \textit{SAS}). Zato je $S$ središče diagonale $AC$, kota $DSA$ in $DSC$
pa sta  prava kota, ker sta skladna sokota.
 \kdokaz



            \bzgled
            Let $k_1(S_1,r)$, $k_2(S_2,r)$, $k_3(S_3,r)$ be congruent circles and
            $k_1\cap k_2=\{B,A_3\}$, $k_2\cap k_3=\{B,A_1\}$, $k_3\cap k_1=\{B,A_2\}$.
            Prove that the lines $S_1A_1$,
             $S_2A_2$ and $S_3A_3$ intersect at a single point .
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.12.pic}
\caption{} \label{sl.skk.4.2.12.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Dokazali bomo še več, da imajo daljice $O_1A_1$, $O_2A_2$ in $O_3A_3$
 isto središče, oziroma da so ustrezni štirikotniki
paralelogrami (Figure \ref{sl.skk.4.2.12.pic}). Ker so $k_1$, $k_2$
in $k_3$ skladne krožnice, sta štirikotnika $O_1A_2O_3B$ in $O_2A_1O_3B$
 romba. Zaradi tega sta daljici $O_1A_2$ in $O_2A_1$ skladni in
vzporedni, kar pomeni, da je štirikotnik $O_1A_2A_1O_2$ paralelogram
(izrek \ref{paralelogram}). Iz istega izreka sledi, da imata njegovi
diagonali $O_1A_1$ in $O_2A_2$  skupno središče. Na podoben
način dokazujemo, da imata tudi daljici $O_2A_2$ in $O_3A_3$  skupno
središče, kar pomeni, da to velja tudi za vse tri daljice $O_1A_1$,
$O_2A_2$ in $O_3A_3$ hkrati. \kdokaz


            \bzgled
            Construct a rectangle $ABCD$ if its diagonals and the difference of its sides
             are congruent with the two given line segments $d$ and $l$.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10a.pic}
\caption{} \label{sl.skl.3.4.10a.pic}
\end{figure}

\textbf{\textit{Solution.}} Naj bo $ABCD$ pravokotnik, pri katerem je $AC\cong d$ in $AB-BC=l$ (Figure \ref{sl.skl.3.4.10a.pic}). Označimo z $E$ takšno točko stranice $AB$, da velja $EB\cong BC$. V tem primeru je $AE=AC-EB=AC-BC=l$. Ker je $EBC$ enakokraki pravokotni trikotnik, je $\angle CEB\cong\angle ECB=45^0$ (izreka \ref{enakokraki} in \ref{VsotKotTrik}) oz. $\angle AEC=135^0$.
To nam  omogoča najprej konstrukcijo  trikotnika $AEC$ ($AC\cong d$, $\angle AEC=135^0$ in $AE\cong l$), nato pa še pravokotnika $ABCD$.
 \kdokaz


        \bzgled
        Construct a triangle with given $b$, $c$ and $t_a$ (sides $AC$, $AB$ and triangle median $AA_1$).
        \ezgled



\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10b.pic}
\caption{} \label{sl.skl.3.4.10b.pic}
\end{figure}

\textbf{\textit{Solution.}} Naj bo $ABC$ trikotnik, pri katerem je $AC\cong b$, $AB\cong c$ in $AA_1\cong t_a$, kjer je $A_1$ središče daljice $BC$ (Figure \ref{sl.skl.3.4.10b.pic}). Označimo z $D$ takšno točko poltraka $AA_1$, da je $DA_1\cong AA_1$ in $\mathcal{B}(A, A_1,D)$. To pomeni, da je $A_1$ skupno središče daljic $BC$ in $AD$, zato je po izreku \ref{paralelogram} štirikotnik $ABDC$ paralelogram. Po istem izreku je $CD\cong AB\cong c$. To nam omogoča najprej konstrukcijo  trikotnika $ADC$ ($AC\cong b$, $CD\cong c$ in $AD=2t_a$), nato pa še točke $A$.
 \kdokaz

 Sedaj bomo vpeljali krajšo obliko zapisa podatkov za načrtovanje trikotnikov. Podobno, kot smo imeli pri prejšnji nalogi  zapis:  $b$, $c$, $t_a$, bomo za elemente trikotnika $ABC$ običajno uporabljali oznake:
 \begin{itemize}
   \item $a$, $b$, $c$ - stranice,
   \item $\alpha$, $\beta$, $\gamma$ - notranji koti,
   \item $v_a$, $v_b$, $v_c$ - višine,
   \item $t_a$, $t_b$, $t_c$ - težiščnice,
   \item $l_a$, $l_b$, $l_c$ - daljice, ki so določene z ogliščem in s presečiščem simetrale notranjega kota v tem oglišču z nasprotno stranico;
   \item $s$ - polobseg  ($s=\frac{a+b+c}{2}$),
   \item $R$ - polmer očrtane krožnice (glej razdelek \ref{odd3ZnamTock}),
   \item $r$ - polmer včrtane krožnice (glej razdelek \ref{odd3ZnamTock}),
   \item  $r_a$, $r_b$, $r_c$ - polmeri pričrtanih krožnic (glej razdelek \ref{odd4Pricrt}).
 \end{itemize}


        \bzgled
        Construct a trapezium if its sides are congruent with the four given line segments $a$, $b$, $c$ and $d$.
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10c.pic}
\caption{} \label{sl.skl.3.4.10c.pic}
\end{figure}

\textbf{\textit{Solution.}} Brez škode za splošnost predpostavimo najprej, da je $a\geq c$. Naj bo $ABCD$ trapez, v katerem so stranice $AB\cong a$, $BC\cong b$, $CD\cong c$ in $DA\cong d$ (Figure \ref{sl.skl.3.4.10c.pic}). V tem primeru je $AB\geq CD$, zato na stranici $AB$ obstaja takšna točka $E$, da velja $AE\cong CD$. Ker je še $AB\parallel CD$, je po izreku \ref{paralelogram} štirikotnik $AECD$ paralelogram, zato je po istem izreku tudi $CE\cong DA\cong d$. Velja tudi $EB=AB-AE=AB-CD=a-c$. To omogoča konstrukcijo trikotnika $EBC$ ($EB=a-c$, $BC\cong c$ in $CE\cong d$), nato pa še oglišč $A$ in $D$ (iz pogoja $AE\cong CD\cong c$).
 \kdokaz



%________________________________________________________________________________
 \poglavje{Regular Polygons}\label{odd3PravilniVeck}

 Pojem kvadrata se vklaplja v splošno definicijo nove vrste večkotnikov.
 Večkotnik je
\index{pravilni!večkotniki} \pojem{pravilen}, če ima vse
stranice skladne in so vsi notranji koti skladni (Figure
\ref{sl.skl.3.5.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.1.pic}
\caption{} \label{sl.skl.3.5.1.pic}
\end{figure}

 Kvadrat je torej pravilni štirikotnik. Prav tako je enakostranični trikotnik
 \index{trikotnik!pravilni}\pojem{pravilni trikotnik}.
To je namreč posledica dejstva, da so pri enakostraničnem
trikotniku tudi vsi koti enaki.

Ugotovili smo že, da je vsota vseh notarnjih kotov poljubnega
$n$-kotnika enaka $(n - 2) \cdot 180^0$ (izrek \ref{VsotKotVeck}). Ker
so pri pravilnem $n$-kotniku vsi notranji koti skladni, lahko notranji kot
izračunamo tako, da vsoto vseh kotov delimo s številom $n$. Tako smo
dokazali naslednjo trditev (Figure \ref{sl.skl.3.5.2.pic}).


             \bizrek \label{pravVeckNotrKot}
             The measure of each interior angle of a regular $n$-gon is:
            $$\frac{(n - 2)\cdot 180^0}{n}.$$
            \eizrek

 Tako notranji kot pravilnega trikotnika meri $60^0$, štirikotnika $90^0$, petkotnika $108^0$, šestkotnika $120^0$, ...


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.2.pic}
\caption{} \label{sl.skl.3.5.2.pic}
\end{figure}

Dokažimo še dve pomembni lastnosti pravilnih večkotnikov.


        \bizrek \label{sredOcrtaneKrozVeck}
        For each regular polygon, there exists a circle passing through each of its vertices.
        \eizrek

\textbf{\textit{Proof.}} Naj bo $A_1A_2\ldots A_n$ pravilen
$n$-kotnik (Figure \ref{sl.skl.3.5.2.pic}). Potem ima vse
stranice skladne in vsi notranji koti so skladni ter enaki $\frac{(n
- 2)\cdot 180^0}{n}$. Naj bosta $s_1$ in $s_2$ simetrali stranic
$A_1A_2$ in $A_2A_3$ tega večkotnika ter točka $S$ njuno
presečišče. Iz izreka \ref{simetrala} sledi $SA_1 \cong SA_2$
in $SA_2 \cong SA_3$  oz.:
 $$SA_1 \cong SA_2 \cong SA_2 \cong SA_3.$$
 Sledi, da sta enakokraka trikotnika $A_1SA_2$ in $A_2SA_3$
skladna (izrek \ref{SSS} - \textit{SSS}). Potem so skladni tudi koti
$SA_1A_2$, $SA_2A_1$, $SA_2A_3$ in $SA_3A_2$. Iz $\angle SA_2A_1 \cong
\angle SA_2A_3$  sledi, da sta oba kota enaka polovici notranjega
kota tega večkotnika oz. $\frac{\alpha}{2}=\frac{(n-2)\cdot
180^0}{2n}$. Zato je tudi:
 $$\angle SA_3A_4 =\alpha - \frac{\alpha}{2}=\frac{\alpha}{2} = \angle
 SA_3A_2.$$
Torej sta trikotnika $A_2SA_3$ in $A_3SA_4$ skladna (izrek
\ref{SKS} - \textit{SAS}). Zaradi tega je   $SA_3 \cong SA_4$  oz.:
 $$SA_1 \cong SA_2 \cong SA_2 \cong SA_3\cong SA_4.$$
 Če ta postopek nadaljujemo, dobimo:
 $$SA_1 \cong SA_2 \cong SA_2 \cdots \cong SA_n,$$
kar pomeni, da je točka $S$ središče krožnice $k(S, SA_1)$, ki
vsebuje vsa njegova oglišča.
 \kdokaz

Krožnico iz prejšnjega izreka imenujemo \index{očrtana
krožnica!pravilnega večkotnika} \pojem{očrtana krožnica
pravilnega večkotnika}. Iz dokaza prejšnjega izreka je jasno, da
se njeno središče nahaja v presečišču simetral vseh njegovih
stranic.


Analogno dokazujemo tudi naslednji izrek.


        \bizrek \label{sredVcrtaneKrozVeck}
        For each regular polygon, there exists a circle  touching each of its sides.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.3.pic}
\caption{} \label{sl.skl.3.5.3.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $A_1A_2\ldots A_n$ pravilen $n$-kotnik
 (Figure \ref{sl.skl.3.5.3.pic}).
Točko $S$ definirajmo enako kot v dokazu prejšnjega izreka.
Dokazali smo, da velja:  $SA_1 \cong SA_2 \cong SA_2 \cdots \cong
SA_n$. Iz tega po izreku \ref{SSS} - \textit{SSS} sledi skladnost
enakokrakih trikotnikov:
 $$\triangle A_1SA_2 \cong \triangle A_2 SA_3 \cong \cdots \cong
  \triangle A_{n-1}SA_n \cong \triangle A_nSA_1.$$
Zaradi tega so skladni tudi vsi koti ob osnovnicah teh trikotnikov.
Torej so premice $SA_1$, $SA_2$,..., $SA_n$ simetrale notranjih
kotov večkotnika $A_1A_2\ldots A_n$. Naj bodo $P_1$, $P_2$,...,
$P_n$ nožišča višin iz oglišča $S$ omenjenih enakokrakih trikotnikov.
Iz skladnosti trikotnikov $\triangle A_1SP_1$, $\triangle A_2SP_1$,
$\triangle A_2SP_2$, ..., $\triangle A_1SP_n$ (izreka \ref{SSK} in
\ref{KSK}) sledi skladnost daljic $SP_1$, $SP_2$,..., $SP_n$. Po
izreku \ref{TangPogoj} se krožnica $k(S, SP_1)$ dotika vseh stranic
večkotnika $A_1A_2\ldots A_n$.
 \kdokaz

Krožnico iz prejšnjega izreka imenujemo \index{včrtana krožnica!pravilnega večkotnika} \pojem{včrtana krožnica pravilnega
večkotnika}. Iz dokaza tega izreka je jasno, da se središče včrtane
krožnice pravilnega večkotnika nahaja na presečišču simetral vseh
njegovih notranjih kotov. Iz dokaza je očitno tudi, da so točke, v
katerih se ta krožnica dotika stranic pravilnega večkotnika, hkrati
središča teh stranic. Središče očrtane in včrtane krožnice je ista
točka in jo zato imenujemo tudi \index{središče!pravilnega
večkotnika}\pojem{središče pravilnega večkotnika}.

 Videli smo tudi, da so vsi trikotniki,
 določeni s središčem
pravilnega $n$-kotnika in z njegovimi stranicami, enakokraki in vsi
skladni. Polmera očrtane in včrtane krožnice $n$-kotnika sta enaka
kraku oz. višini vsakega od teh trikotnikov. Koti ob vrhu teh
trikotnikov so tudi skladni in ker jih je skupaj $n$ (enako kot
stranic $n$-kotnika), vsak od njih meri (Figure \ref{sl.skl.3.5.4.pic}):
 $$\varphi = \frac{360^0}{n}.$$

\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.4.pic}
\caption{} \label{sl.skl.3.5.4.pic}
\end{figure}

 Pri pravilnem šestkotniku, oz. za $n = 6$, velja:
 $$\varphi = \frac{360^0}{6}=60^0.$$

 To pomeni, da so omenjeni trikotniki pravilni.
Torej je pravilni šestkotnik sestavljen iz šestih
pravilnih trikotnikov  (Figure \ref{sl.skl.3.5.4.pic}).

V nadaljevanju bomo obravnavali lastnosti pravilnih $n$-kotnikov.

 Naj bo najprej $n$ sodo število in $k = \frac{n}{2}+1$.
Pravimo, da je $A_k$ \pojem{nasprotno oglišče} oglišča $A_1$
pravilnega $n$-kotnika $A_1A_2\ldots A_n$ (Figure
\ref{sl.skl.3.5.5.pic}). Analogno sta $A_2$ in $A_{k+1}$, $A_3$ in
$A_{k+2}$, ... , $A_{k-1}$ in $A_n$ nasprotni oglišči tega
$n$-kotnika. Podobno sta stranici $A_1A_2$ in $A_kA_{k+1}$, ... ,
$A_{k-1} A_k$ in $A_nA_1$ \pojem{nasprotni stranici} večkotnika
$A_1A_2\ldots A_n$. Opazimo, da velja:
 $$\angle A_1SA_k=\frac{n}{2}\varphi = \frac{n}{2}\cdot
  \frac{360^0}{n}=180^0,$$
kar pomeni, da diagonala $A_1A_k$ tega $n$-kotnika vsebuje njegovo
središče. Zato ta diagonala predstavlja premer očrtane krožnice.
Analogno to velja za vse diagonale, ki so določene z nasprotnimi
oglišči. Zaradi tega takšne diagonale imenujemo \index{velika diagonala
pravilnega $n$-kotnika} \pojem{velike diagonale} pravilnega
$n$-kotnika. Polmer očrtane krožnice je
 enak polovici velike diagonale.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.5.pic}
\caption{} \label{sl.skl.3.5.5.pic}
\end{figure}

 Na podoben način se dokaže, da za sodo število $n$ središči
 nasprotnih stranic pravilnega $n$-kotnika
$A_1A_2\ldots A_n$ določata premere včrtane krožnice tega
$n$-kotnika. Če upoštevamo prejšnje oznake, dobimo:
 \begin{eqnarray*}
 \angle P_1SP_k&=&\angle P_1SA_2 + \angle A_2SA_{k-1} + \angle
 A_{k-1}SP_k\\
 &=&  \frac{\varphi}{2}+\frac{n-2}{2}\cdot \varphi+\frac{\varphi}{2}
 =\frac{n}{2}\cdot\varphi
 =180^0.
  \end{eqnarray*}


 Daljice, ki so določene s parom središč nasprotnih stranic $n$-kotnika
 $A_1A_2\ldots A_n$ oz. daljice $P_1P_k$,
$P_2P_{k+1}$, ... , $P_{k-1}P_n$, imenujemo \pojem{višine}
\index{višina!pravilnega $n$-kotnika} tega $n$-kotnika. Polmer
včrtane krožnice je enak polovici višine.

 Torej vsak pravilni $n$-kotnik, kjer je $n$ sodo število, vsebuje
$\frac{n}{2}$ velikih diagonal (enakih premeru očrtane krožnice) in
$\frac{n}{2}$ višin (enakih premeru včrtane krožnice). Vsaka od njih
gre skozi središče tega $n$-kotnika.


 Naj bo sedaj $n$ liho število (Figure \ref{sl.skl.3.5.6.pic}) in
  $k=\frac{n+1}{2}+1$.
 Potem je:
\begin{eqnarray*}
 \angle P_1SA_k=\angle P_1SA_2 + \angle A_2SA_k=
  \frac{\varphi}{2}+\frac{n-1}{2}\cdot \varphi
 =\frac{n}{2}\cdot\varphi
 =180^0.
  \end{eqnarray*}

\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.6.pic}
\caption{} \label{sl.skl.3.5.6.pic}
\end{figure}

To pomeni, da daljica $P_1A_k$ vsebuje središče $S$ pravilnega
$n$-kotnika  $A_1A_2\ldots A_n$. To daljico imenujemo \index{višina!pravilnega $n$-kotnika}
\pojem{višina} tega $n$-kotnika, stranica
$A_1A_2$ in oglišče $A_k$ sta si \pojem{nasprotni}. Analogno
definiramo tudi preostalih $n$ višin in $n$ parov nasprotnih
stranic in oglišč. Na podoben način lahko dokažemo, da tudi ostale
višine tega $n$-kotnika  vsebujejo njegovo središče.

Pri pravilnem (enakostraničnem) trikotniku  imamo torej tri
višine, ki se sekajo v njegovem središču (Figure
\ref{sl.skl.3.5.7.pic}). Če to velja pri
poljubnem trikotniku, bomo ugotovili kasneje


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.7.pic}
\caption{} \label{sl.skl.3.5.7.pic}
\end{figure}

 V kvadratu sta njegovi  diagonali hkrati veliki
 diagonali in se sekata v
njegovem središču  (Figure \ref{sl.skl.3.5.7.pic}). Višini
kvadrata sta skladni z njegovo stranico, kar ni težko dokazati.

Omenili smo že, da je pravilni šestkotnik sestavljen iz šestih
trikotnikov, ki se stikajo v njegovem središču. Pravilni
šestkotnik bomo obširneje obravnavali v nadaljevanju. Dokazali bomo
tudi nekaj lastnosti pravilnega petkotnika, sedemkotnika,
devetkotnika in dvanajstkotnika. Posebej zanimiv bo problem
načrtovanja pravilnih $n$-kotnikov za poljubno število $n$.

Dokažimo sedaj zanimivo lastnost pravilnega devetkotnika.

             \bzgled
            If $a$ is a side and $d$ and $e$ are the shortest and longest
            diagonal of a regular nonagon ($9$-gon), then $e - d = a$.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.8.pic}
\caption{} \label{sl.skl.3.5.8.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bosta $d = CE$ in $e = BF$ najkrajša in
najdaljša diagonala pravilnega devetkotnika $ABCDEFGHI$ s stranico
$a$ ter $P$ presečišče premic $BC$ in $FE$  (Figure
\ref{sl.skl.3.5.8.pic}). Notranji kot tega devetkotnika meri
 $\angle CDE=\frac{9-2}{9}\cdot 180^0=140^0$,
zato je $\angle ECD = \angle CED = 20^0$. Iz tega sledi
 $\angle BCE = \angle FEC = 120^0$, oz.:
 $$\angle ECP = \angle CEP = 60^0.$$
 Torej je trikotnik $CPE$ pravilen. Ker je $CB = EF=a$
in $\angle BPF \cong \angle CPE = 60^0$, je pravilen tudi
trikotnik $BPF$. Torej:
 $$e = BF = BP = BC + CP = BC + CE = a + d,$$ kar je bilo treba dokazati. \kdokaz


%%________________________________________________________________________________
 \poglavje{Midsegment of Triangle} \label{odd3SrednTrik}

Sedaj bomo obravnavali zelo pomembno lastnost trikotnika, ki jo
bomo pogosto uporabljali. Naj bosta $P$ in $Q$ središči stranic
$AB$ in $AC$ trikotnika $ABC$. Daljico $PQ$ imenujemo
\index{srednjica!trikotnika} \pojem{srednjica trikotnika} $ABC$,
ki je pripadajoča stranici $BC$ (Figure \ref{sl.skl.3.6.1.pic}).
Pravimo tudi, da je $PQ$ srednjica trikotnika $ABC$ za osnovnico
$BC$. Dokažimo osnovno lastnost, ki se nanaša na srednjico.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.1.pic}
\caption{} \label{sl.skl.3.6.1.pic}
\end{figure}


           \bizrek \label{srednjicaTrik}
             Let $PQ$ be the midsegment of a triangle $ABC$ corresponding to the side $BC$. Then:
            $$ PQ = \frac{1}{2} BC\hspace*{2mm}
            \textrm{ in } \hspace*{2mm} PQ \parallel BC.$$
           \eizrek



 \textbf{\textit{Proof.}} Naj bo $R$ takšna točka, da velja $PQ \cong QR$ in
$\mathcal{B}(P,Q,R)$ (Figure \ref{sl.skl.3.6.1.pic}). Daljici $AC$
in $PR$ imata skupno središče, zato je štirikotnik $APCR$
paralelogram (izrek \ref{paralelogram}). Zaradi tega sta daljici
$AP$ in $RC$ skladni in vzporedni. Točka $P$ je središče daljice
$AB$, zato sta tudi daljici $PB$ in $RC$ skladni in vzporedni. To
pomeni, da je tudi štirikotnik $PBCR$ paralelogram. Iz tega
sledi, da sta daljici $BC$ in $PR$ skladni in vzporedni. Končna
ugotovitev sledi iz dejstva, da je točka $Q$ središče daljice
$PR$.
 \kdokaz


            \bzgled
            Let $AB$ and $A'B'$ be congruent line segments, $C$ and $D$ the midpoints of the line segments
            $AA'$ and $BB'$. Suppose that $CD =\frac{1}{2}  AB$.
            What is a measure of the angle between the lines $AB$ and $A'B'$?
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.2.pic}
\caption{} \label{sl.skl.3.6.2.pic}
\end{figure}



\textbf{\textit{Solution.}} Naj bo točka $S$ središče daljice
$A'B$ (Figure \ref{sl.skl.3.6.2.pic}). Daljici $CS$ in $DS$ sta
srednjici trikotnikov $A'AB$ in $BA'B'$, zato je: $$CS =
\frac{1}{2}AB = CD = \frac{1}{2}A'B'= DS,$$
 oziroma $SCD$ je pravilen trikotnik. Kota $\angle AB,A'B'$ in $\angle CSD$
  imata vzporedne krake. Torej je:
$\angle AB, A'B' \cong \angle CSD = 60^0$.
 \kdokaz

Naslednja posledica izreka \ref{srednjicaTrik} se nanaša na
trapez.


             \bizrek \label{srednjTrapez}
             Let $P$ and $Q$ be the midpoints of legs $BC$ and $DA$  of a trapezium $ABCD$.
            Suppose that $M$ and $N$ are the midpoints of the diagonals $AC$ and $BD$ of that trapezium.
            Then the points $M$ and $N$ lie on the line $PQ$, which is parallel to the bases $AB$ in $CD$ of the trapezium,
             and also:
             $$PQ = \frac{1}{2}( AB + CD)     \hspace*{2mm}
             \textrm{ in } \hspace*{2mm} MN=\frac{1}{2}( AB - CD).$$
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.3.pic}
\caption{} \label{sl.skl.3.6.3.pic}
\end{figure}


 \textbf{\textit{Proof.}}  Daljice $PN$, $NQ$ in $PM$ so po vrsti srednjice
  trikotnikov
 $DAC$, $ACB$ in $ADB$ za
pripadajoče osnovnice $DC$, $AB$ in $AB$ (Figure
\ref{sl.skl.3.6.3.pic}). Zaradi tega so vse tri premice $PN$, $NQ$
in $PM$ vzporedne z osnovnicama $CD$ in $AB$. Ker skozi vsako
točko (najprej $N$, nato $P$) obstaja le ena vzporednica s premico
$AB$ (Playfairjev\footnote{\index{Playfair, J.}\textit{J.
Playfair} (1748--1819), škotski matematik.} aksiom
\ref{Playfair}), so točke $P$, $N$, $M$ in $Q$ kolinearne. Velja
še (izrek \ref{srednjicaTrik}):
 $PN = \frac{1}{2} CD$ in
  $NQ = PM = \frac{1}{2} AB$. Iz tega sledi:
   \begin{eqnarray*}
   PQ&=& PN+NQ=\frac{1}{2}CD+
   \frac{1}{2}AB=\frac{1}{2}\left(AB+CD\right)\\
  NM&=& PM-PN=\frac{1}{2}AB-
   \frac{1}{2}CD=\frac{1}{2}\left(AB-CD\right),
  \end{eqnarray*}
  kar je bilo potrebno dokazati.  \kdokaz

Daljico $PQ$ iz prejšnjega izreka imenujemo
\index{srednjica!trapeza} \pojem{srednjica trapeza}.

 Naslednje trditve se nanašajo na poljubni štirikotnik.


             \bizrek \label{Varignon}
             Let $ABCD$ be an arbitrary quadrilateral and $P$, $Q$, $K$ and $L$
            the midpoints of the sides $AB$, $CD$, $BC$ and $AD$, respectively. Then the quadrilateral $PKQL$ is
            a parallelogram (so-called \index{paralelogram!Varignonov}
              Varignon\footnote{\index{Varignon, P.}
              \textit{P. Varignon} (1654--1722),
             francoski matematik,
            ki je prvi dokazal to lastnost. Vendar je bil izrek  objavljen šele
            po njegovi smrti leta 1731. Glede na enostavnost pa je  prav
            presenetljivo, da je ta trditev toliko časa ‘‘čakala’’ na svoje
            odkritje.} parallelogram).
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.4.pic}
\caption{} \label{sl.skl.3.6.4.pic}
\end{figure}


 \textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.6.4.pic})
Daljici $PK$ in $LQ$ sta srednjici trikotnikov $ABC$ in $ADC$ za
isto osnovnico $AC$, zato sta skladni in
vzporedni. Torej je štirikotnik $PKQL$  paralelogram.
 \kdokaz

V posebnem primeru je lahko Varignonov paralelogram celo pravokotnik,
romb ali kvadrat. Kdaj je to možno? To vprašanje nam da idejo za
naslednji izrek. Vemo, da je paralelogram pravokotnik, če  ima
vsaj en notranji  kot pravi. Drugi (ekkvivalenten) pogoj  pa je,
da ima skladni diagonali. Podobno obravnavo lahko uporabimo tudi
pri rombu in kvadratu.


            \bzgled \label{VarignonPoslPravRomb}
            Let $ABCD$ be an arbitrary quadrilateral and $P$, $K$, $Q$ and $L$
            the midpoints of the sides $AB$, $BC$, $CD$ and
            $DA$, respectively. Then:

            a) $AC \perp BD \Leftrightarrow PQ \cong KL$;

             b) $AC \cong BD \Leftrightarrow PQ \perp KL$.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.5.pic}
\caption{} \label{sl.skl.3.6.5.pic}
\end{figure}


\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.6.5.pic})
 Iz prejšnjega izreka \ref{Varignon} sledi, da je
 štirikotnik $PKQL$ vedno paralelogram – Varignonov
paralelogram. Daljici $PL$ in $PK$ sta srednjici trikotnikov $ABD$
in $ABC$ za osnovnici $AD$ oz. $AC$. Zaradi tega velja:
 $PL= \frac{1}{2}BD$ in $PL \parallel BD$ ter $PK= \frac{1}{2}AC$ in $PK \parallel AC$.
 Zatorej velja:

 a) $AC \perp BD \Leftrightarrow PL \perp PK
\Leftrightarrow PKQL \textrm{ pravokotnik} \Leftrightarrow PQ
\cong KL$;

 b) $AC \cong BD \Leftrightarrow PL \cong PK \Leftrightarrow
  PKQL \textrm{ romb } \Leftrightarrow PQ \perp KL$.
 \kdokaz

Če je Varignonov paralelogram kvadrat, so izpolnjeni vsi štirje
pogoji iz prejšnjih ekvivalenc, oz. je v tem primeru: $AB \perp CD$, $AB \cong CD$, $PQ \perp KL$ in $PQ \cong KL$.

Oglejmo si še eno uporabo lastnosti Varignonovega paralelograma.


            \bzgled \label{VagnanPosl}
            Let $ABCD$ be an arbitrary quadrilateral. If $P$, $Q$, $K$, $L$, $M$ and
             $N$ are the midpoints of the line segments $AB$, $CD$, $BC$, $AD$, $AC$ and $BD$,  respectively,
             then the line segments $PQ$, $KL$ and
            $MN$  have a common midpoint.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.6.pic}
\caption{} \label{sl.skl.3.6.6.pic}
\end{figure}


\textbf{\textit{Proof.}}
 (Figure \ref{sl.skl.3.6.6.pic}) Štirikotnik $PKQL$ je Varignonov
paralelogram (izrek \ref{Varignon}). Na podoben način dokazujemo, da
je tudi štirikotnik $LNKM$ paralelogram (srednjice trikotnikov $ADB$
in $ACB$). Paralelograma $PKQL$ in $LPKQ$ imata skupno diagonalo
$LK$. Ker se diagonali poljubnega paralelograma razpolavljata (izrek
\ref{paralelogram}), imajo daljice $LK$, $PQ$ in $MN$  skupno
središče.
 \kdokaz

Točko iz prejšnjega primera, v kateri se daljice sekajo, imenujemo
\index{težišče!štirikotnika} \pojem{težišče štirikotnika}. Več
o tem bomo povedali v razdelku \ref{odd5TezVeck}.

Naslednja trditev je lep primer kombiniranja neenakosti trikotnika
in srednjice trikotnika. Trditev je pravzaprav posplošitev izreka
o srednjici trapeza \ref{srednjTrapez}.


              \bizrek
             If $P$ and $Q$ are the midpoints of the sides $AB$ and $CD$ of
             an arbitrary quadrilateral
            $ABCD$, then: $$PQ \leq \frac{1}{2}\left( BC + AD\right).$$
             \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.7.pic}
\caption{} \label{sl.skl.3.6.7.pic}
\end{figure}


\textbf{\textit{Proof.}}
 Naj bo $S$ središče diagonale $AC$ štirikotnika $ABCD$
  (Figure \ref{sl.skl.3.6.7.pic}).
Če uporabimo izrek o srednjici trikotnika (\ref{srednjicaTrik}) in
trikotniško neenakost  (\ref{neenaktrik}), dobimo:
 $$BC + AD = 2PS
+ 2SQ = 2(PS + SQ) \geq 2PQ.$$
 Enakost velja v primeru, kadar so
točke $P$, $S$ in $Q$ kolinearne, oz. ko je štirikotnik $ABCD$
trapez z osnovnico $BC$.
 \kdokaz

 Omenimo še, da
neenakost iz prejšnjega primera velja tudi, če točke $A$, $B$,
$C$ in $D$ niso v isti ravnini, oz. če je $ABCD$
\index{tetraeder} \pojem{tetraeder}.


        \bzgled \label{TezisceSredisceZgled}
        Let $P$ be the midpoint of the median $AA_1$ of a triangle $ABC$ and
        $Q$
        the intersection of the side $AC$ and the line $BP$. Determine the ratios
        $AQ :QC$ and $BP : PQ$.
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.8.pic}
\caption{} \label{sl.skl.3.6.8.pic}
\end{figure}


\textbf{\textit{Solution.}} Naj bo $R$ središče daljice $QC$
  (Figure \ref{sl.skl.3.6.8.pic}). Daljica $A_1R$ je srednjica
trikotnika $BCQ$ za osnovnico $BQ$, zato je (izrek
\ref{srednjicaTrik}) $BQ = 2A_1R$ in $BQ\parallel A_1R$. Iz te
vzporednosti in definicije točke $P$ sledi, da je $PQ$ srednjica
trikotnika $AA_1R$ za osnovnico $A_1R$, zato je (izrek
\ref{srednjicaTrik} in Playfairjev aksiom \ref{Playfair}) točka $Q$
središče daljice $AR$ in velja $A_1R = 2PQ$. Torej: $AQ \cong QR
\cong RC$ oz. $AQ:QC=1:2$. Na koncu je še $BQ=2A_1R=4PQ$ oz.
$BP:PQ=3:1$.
 \kdokaz



                 \bnaloga\footnote{19. IMO Yugoslavia - 1977, Problem 1.}
                Equilateral triangles $ABP$, $BCL$, $CDM$, $DAN$ are constructed inside the
                square $ABCD$. Prove that the midpoints of the segments $LM$, $MN$, $NP$, $PL$, $AN$, $LB$,
                  $BP$, $CM$, $CL$, $DN$, $DM$ in $AP$
                are the twelve vertices of a regular dodecagon ($12$-gon).
                \enaloga

\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.IMO1.pic}
\caption{} \label{sl.skl.3.6.IMO1.pic}
\end{figure}

\textbf{\textit{Solution.}} Označimo z $a$ dolžino stranice in
z $O$ središče kvadrata $ABCD$ (Figure \ref{sl.skl.3.6.IMO1.pic}).

Dokažimo najprej, da je štirikotnik $MNPL$ tudi kvadrat z istim
središčem $O$. Ker so $ABP$, $BCL$, $CDM$ in $DAN$ vsi pravilni
trikotniki, ležita diagonali $MP$ in $LN$ štirikotnika $MNPL$ na
simetralah stranic $AB$ in $BC$ kvadrata $ABCD$. Iz tega sledi $MP \perp LN$.
Ker je še $d(M,AB)=d(P,CD)=a-v$ (kjer je $v$ dolžina
višine omenjenih pravilnih trikotnikov), velja tudi $OM\cong OP$.
Podobno je tudi $OL\cong ON$, kar pomeni, da je štirikotnik $MNPL$
res kvadrat z istim središčem~$O$.

Dokažimo sedaj, da je $LAM$ pravilni trikotnik. Ker je $AB\cong
AD\cong BL\cong DM=a$ in $\angle LBA\cong\angle MDA
=90^0-60^0=30^0$, sta trikotnika $LBA$ in $MDA$ skladna (izrek
\textit{SAS} \ref{SKS}). To pomeni, da je $LA\cong MA$ in $\angle
DAL= 90^0-\angle LAB=15^0$. Podobno je tudi $\angle BAM=15^0$ oz.
$\angle LAM = 90^0-2\cdot 15^0=60^0$. Torej je $LAM$ pravilni
trikotnik, zato ima stranica kvadrata $MNPL$  dolžino
$b=|LM|=|LA|$.

Označimo s $S$ središče daljice $LM$. Središča stranic kvadrata $MNPL$
ležijo na krožnici $k(O,\frac{b}{2})$, ki je včrtana krožnica tega
kvadrata. Dokažimo, da tudi točka $T$ - središče daljice $AN$ -
leži na tej krožnici. Daljica $OT$ je srednjica trikotnika $LAN$
za osnovnico $LA$, zato je $OT\parallel LA$ in
$|OT|=\frac{1}{2}|LA|=\frac{b}{2}$. Torej točka $T$ in analogno
tudi vse točke v nalogi definiranega $12$-kotnika ležijo na
krožnici $k(O,\frac{b}{2})$.

Dokažimo še, da je omenjeni $12$-kotnik pravilen. Brez škode za
splošnost zadošča dokazati, da je $\angle
SOT=\frac{360^0}{12}=30^0$. Toda iz že dokazanega dejstva
$OT\parallel LA$ sledi $\angle SOT\cong \angle
LAS=\frac{1}{2}\angle LAM=30^0$.
 \kdokaz

%________________________________________________________________________________
 \poglavje{Triangle Centers} \label{odd3ZnamTock}

 Našo raziskavo bomo nadaljevali s trikotnikom – najbolj enostavnim
 večkotnikom,
 ki pa je  hkrati
lik, ki ima nepričakovano veliko zanimivih lastnosti. Nekatere  bomo
obravnavali v tem razdelku, nekatere pa kasneje, ko se bomo ukvarjali
z drugimi pojmi, kot so izometrije in podobnost.

 Sedaj bomo obravnavali štiri \index{značilne točke
 trikotnika}\pojem{značilne točke
 trikotnika}\footnote{Te štiri točke omenjajo že Stari Grki, čeprav so
 (še posebej to velja za težišče) bile znane verjetno že veliko časa pred
tem.} in
 njihovo uporabo pri štiri- in večkotnikih.

Začnimo najprej s prvo med značilnimi točkami, ki je povezana s
 težiščnicami trikotnika. Težiščnico smo  že definirali
  v poglavju \ref{odd3NeenTrik}.



         \bizrek \label{tezisce}
         The medians of a triangle intersect at one point.
        That point divides  the medians in the ratio $2:1$
         (from the vertex to the midpoint of the opposite side).
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.1.pic}
\caption{} \label{sl.skl.3.7.1.pic}
\end{figure}


\textbf{\textit{Proof.}}
  Naj bodo $AA_1$, $BB_1$ in $CC_1$ težiščnice trikotnika $ABC$
   (Figure \ref{sl.skl.3.7.1.pic}).
Zaradi Paschevega aksioma, \ref{AksPascheva} glede na trikotnik
$BCB_1$ in premico $AA_1$, premica $AA_1$ seka daljico $BB_1$.
Analogno premica $BB_1$ seka daljico $AA_1$, kar pomeni, da se
težiščnici $AA_1$ in $BB_1$ sekata v neki točki $T$. Naj bosta $A_2$
in $B_2$ središči daljic $AT$ in $BT$. Daljici $A_1B_1$ in $A_2B_2$
sta srednjici trikotnikov $ABC$ in $ABT$ z isto osnovnico $AB$. To
pomeni, da sta daljici $A_1B_1$ in $A_2B_2$ vzporedni in enaki
polovici stranice $AB$. Zaradi tega je štirikotnik $B_2A_1B_1A_2$
paralelogram (izrek \ref{paralelogram}), kar pomeni da se njegovi
diagonali $A_1A_2$ in $B_1B_2$ razpolavljata in je točka $T$
njuno skupno središče. Torej velja:
 $A_1T\cong TA_2 \cong A_2A$  in $B_1T\cong TB_2 \cong B_2B$
 oz. $AT:TA_1=2:1$ in $BT:TB_1=2:1$ ter
  $$A_1T=\frac{1}{3}A_1A \textrm{ in }    B_1T = \frac{1}{3}B_1B.$$
  Na enak način
 dokažemo, da se tudi težiščnici $AA_1$ in $CC_1$ sekata v neki
točki $T’$, za katero velja $AT':T'A_1=2:1$ in $CT':T'C_1=2:1$ oz.:
 $$A_1T'=\frac{1}{3}A_1A \textrm{ in }    C_1T' = \frac{1}{3}C_1C.$$
To pomeni, da sta $T$ in $T'$ točki poltraka $A_1A$, za kateri velja
$A_1T\cong A_1T'=\frac{1}{3}A_1A$, zato je po izreku
\ref{ABnaPoltrakCX} $T = T'$, kar pomeni, da se težiščnice $AA_1$,
$BB_1$ in $CC_1$ sekajo v točki $T$ in velja
$AT:TA_1=BT:TB_1=CT:TC_1=2:1$.
 \kdokaz


Točka iz prejšnjega izreka, v kateri se sekajo vse težiščnice
trikotnika, se imenuje \index{težišče!trikotnika}\pojem{težišče
trikotnika}.

Težišče trikotnika v fizičnem smislu predstavlja točko, ki je
središče mase tega trikotnika. To bo še bolj jasno, ko bomo
v razdelku \ref{odd8PloTrik} dokazali dejstvo, da težišče
 deli  trikotnik na trikotnike z enako ploščino.
  V naslednjem poglavju \ref{pogVEKT} (razdelek \ref{odd5TezVeck})
bomo obravnavali težišče poljubnega večkotnika.

V  razdelku \ref{odd3PravilniVeck} smo ugotovili, da za vsak
pravilni večkotnik obstajata očrtana krožnica (ki vsebuje vsa njegova
oglišča) in včrtana krožnica (ki se dotika vseh njegovih stranic) z
istim središčem. Ta lastnost se prenaša tudi na pravilne oz.
enakostranične trikotnike. Kako pa je s poljubnim trikotnikom?
Dokazali bomo, da obstajata omenjeni krožnici za poljuben trikotnik, le
da imata v splošnem primeru  različni središči.


        \bizrek \label{SredOcrtaneKrozn}
       The perpendicular bisectors of the sides of any triangle intersect at a single point,
             which is the centre of a circle containing all its vertices.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.2.pic}
\caption{} \label{sl.skl.3.7.2.pic}
\end{figure}


\textbf{\textit{Proof.}}
  Naj bodo $p$, $q$ in $r$  simetrale stranic $BC$, $AC$ in $AB$
   trikotnika $ABC$ (Figure \ref{sl.skl.3.7.2.pic}).
 Simetrali $p$
in $q$ nista vzporedni (ker bi bili v tem primeru po Playfairjevem aksiomu
\ref{Playfair}  vzporedni tudi premici $BC$ in $AC$) in se
sekata v neki točki $O$. Ker le-ta leži na simetralah $p$ in $q$
stranic $BC$ in $AC$,  je $OB \cong OC$ in $OC \cong OA$. Iz tega
sledi  $OA \cong OB$, kar pomeni, da točka $O$ leži tudi na
simetrali $r$ daljice $AB$. Torej se simetrale $p$, $q$ in $r$
sekajo v eni točki.

Ker je  $OA \cong OB \cong OC$, je točka $O$ središče krožnice
$k(O,OA)$, ki vsebuje vsa oglišča trikotnika $ABC$.
 \kdokaz

 Krožnico iz prejšnjega izreka, ki vsebuje vsa oglišča trikotnika,
  imenujemo  \index{očrtana krožnica!trikotnika} \pojem{trikotniku očrtana
 krožnica}, njeno središče pa
        \index{središče!očcrtane krožnice!trikotnika}
        \pojem{središče trikotniku očrtane krožnice}.



         \bizrek \label{SredVcrtaneKrozn}
          The bisectors of the interior angles of any triangle intersect at a single point,
             which is the centre of a circle touching all its sides.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.3.pic}
\caption{} \label{sl.skl.3.7.3.pic}
\end{figure}


\textbf{\textit{Proof.}}
  Naj bodo $p$, $q$ in $r$  simetrale notranjih kotov pri
  ogliščih  $A$, $B$ in $C$
   trikotnika $ABC$ (Figure \ref{sl.skl.3.7.3.pic}).
   Dokažimo, da simetrali $p$ in $q$ nista vzporedni. V nasprotnem
    bi bila po izreku \ref{KotiTransverzala} vsota polovic
   notranjih kotov pri ogliščih $A$ in $B$
 enaka $180°$, kar po izreku \ref{VsotKotTrik} ni mogoče. Torej se
$p$ in $q$  sekata v neki točki $S$. Ker točka $S$ leži na
simetralah notranjih kotov pri ogliščih $A$ in $B$, je  enako
oddaljena od nosilk stranic $AC$ in $AB$ oz. od nosilk stranic $BA$
in $BC$ (izrek \ref{SimKotaKraka}). Iz tega sledi, da je točka $S$
enako oddaljena od nosilk stranic $CA$ in $CB$, kar pomeni, da leži
na simetrali $r$ notranjega kota pri oglišču $C$. Torej se simetrale
$p$, $q$ in $r$ sekajo v točki $S$.

S $P$, $Q$ in $R$ označimo pravokotne projekcije točke $S$ na
stranicah $BC$, $CA$ in $AB$. Ker velja $\frac{1}{2}\angle CBA<90^0$
in $\frac{1}{2}\angle BCA<90^0$, je $\mathcal{B}(B,P,C)$. Podobno je
tudi  $\mathcal{B}(C,Q,A)$ in $\mathcal{B}(A,R,B)$. Zaradi že
dokazane lastnosti točke $S$ velja $SP \cong SQ \cong SR$. Torej je
točka $S$  središče krožnice $l$, ki poteka skozi točke $P$, $Q$ in
$R$. Zaradi pravokotnosti polmerov $SP$, $SQ$ in $SR$ na ustrezne
stranice,  so le-te tangente krožnice $l$. Ker je
$\mathcal{B}(B,P,C)$,  $\mathcal{B}(C,Q,A)$ in $\mathcal{B}(A,R,B)$
se krožnica $l$ dotika vseh
         stranic trikotnika $ABC$.
 \kdokaz


 Krožnico iz prejšnjega izreka, ki se dotika vseh
         stranic trikotnika, imenujemo  \index{včrtana krožnica!trikotnika} \pojem{trikotniku včrtana
 krožnica}, njeno središče pa
        \index{središče!včcrtane krožnice!trikotnika}
        \pojem{središče trikotniku včrtane krožnice}.

Ostala je še ena od štirih omenjenih značilnih točk trikotnika.
Nanaša se na višine trikotnika.


        \bizrek \label{VisinskaTocka}
        The lines containing the altitudes of a triangle  intersect at a single point.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.4.pic}
\caption{} \label{sl.skl.3.7.4.pic}
\end{figure}


\textbf{\textit{Proof.}}
  Naj bodo $p$, $q$ in $r$  nosilke višin
    $AA'$, $BB'$ in $CC'$
   trikotnika $ABC$ (Figure \ref{sl.skl.3.7.4.pic}).
Označimo z $a$, $b$ in $c$ premice, ki so v točkah $A$, $B$ in $C$
pravokotne na ustrezne višine. Ker so premice $a$, $b$ in $c$
vzporedne s stranicama trikotnika $ABC$, se vsaki dve med seboj
sekata. Označimo s $P$, $Q$ in $R$ po vrsti presečišča premic $b$ in
$c$, $a$ in $c$ ter $a$ in $b$. Štirikotnika $ABCQ$ in $RBCA$ sta
 paralelograma, kar pomeni, da je $RA \cong BC \cong AQ$, oz. je točka
$A$ središče daljice $RQ$. Premica $AA’$ je zato simetrala
stranice $RQ$ trikotnika $PQR$. Analogno sta $BB’$ in $CC’$
simetrali stranic $PR$ in $PQ$ istega trikotnika. Po izreku
\ref{SredOcrtaneKrozn} se simetrale $AA’$, $BB’$ in $CC’$ trikotnika
$PQR$ sekajo v neki točki $V$. Točka $V$ je torej presečišče
nosilk višin
    $AA'$, $BB'$ in $CC'$
   trikotnika $ABC$.
   \kdokaz

Točko iz prejšnjega izreka, v kateri se sekajo nosilke višin, imenujemo
\index{višinska točka trikotnika}
         \pojem{višinska točka trikotnika}. Trikotnik $A'B'C'$, ki ga
         določajo nožišča višin trikotnika $ABC$ imenujemo
\index{trikotnik!pedalni} \pojem{pedalni trikotnik} trikotnika
$ABC$.

Ugotovili smo, ima vsak trikotnik štiri značilne točke,
in sicer: težišče, središče očrtane krožnice, središče včrtane
krožnice in višinsko točko. Toda to niso edine značilne točke
trikotnika. Nekatere od njih bomo omenili kasneje. Za
neko točko v ravnini trikotnika na splošno rečemo, da je njegova
\pojem{značilna točka}, če je njena definicija simetrična glede na
oglišča tega trikotnika.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.5.pic}
\caption{} \label{sl.skl.3.7.5.pic}
\end{figure}


 Jasno je, da se pri poljubnem trikotniku štiri značilne točke razlikujejo
 (Figure \ref{sl.skl.3.7.5.pic}).

          Pri enakokrakem trikotniku imajo težiščnica,
višina, simetrala osnovnice in simetrala notranjega kota nasproti
osnovnice  isto nosilko. Če je $A_1$ središče osnovnice
$BC$ enakokrakega trikotnika $ABC$, sta trikotnika $ABA_1$ in
$ACA_1$ skladna, kar pomeni, da je kot pri oglišču $A_1$ pravi kot
in sta kota $BAA_1$ in $CAA_1$ skladna. Torej je daljica
$AA_1$ hkrati težiščnica in višina, premica $AA_1$ pa hkrati
simetrala stranice $BC$ in simetrala notranjega kota pri oglišču $A$
trikotnika $ABC$. Iz tega sledi, da vse štiri značilne točke tega
trikotnika ležijo na eni premici $AA_1$ (Figure
\ref{sl.skl.3.7.6.pic}).

Če uporabimo že dokazano lastnost enakokrakega trikotnika za
enakostranični trikotnik, ugotovimo, da imajo  pri njem vse ustrezne
težiščnice, višine, simetrale stranic in simetrale notranjih kotov
iste nosilke. To pomeni, da se pri enakostraničnem trikotniku
vse štiri značilne točke prekrivajo (Figure \ref{sl.skl.3.7.6.pic}).
To je pravzaprav že definirano (razdelek \ref{odd3PravilniVeck})
središče tega enakostraničnega (oz. pravilnega) trikotnika.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.6.pic}
\caption{} \label{sl.skl.3.7.6.pic}
\end{figure}

Pokazali bomo še, kakšno lego imajo značilne točke glede na vrsto
trikotnika.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.7.pic}
\caption{} \label{sl.skl.3.7.7.pic}
\end{figure}

Težiščnice so vedno v notranjosti trikotnika. Zato je tudi težišče
notranja točka vsakega trikotnika (Figure \ref{sl.skl.3.7.7.pic}).
Ista ugotovitev velja tudi za središče včrtane krožnice (Figure
\ref{sl.skl.3.7.7s.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.7s.pic}
\caption{} \label{sl.skl.3.7.7s.pic}
\end{figure}

Pri ostrokotnem trikotniku nožišča pravokotnic iz njegovih oglišč
ležijo na stranicah tega trikotnika, kar pomeni (Paschev aksiom
\ref{AksPascheva}), da se njegove višine sekajo v notranjosti. Torej pri
ostrokotnem trikotniku leži višinska točka  v njegovi notranjosti
(Figure \ref{sl.skl.3.7.7v.pic}). Pri pravokotnem trikotniku je višinska
točka oglišče pri pravemu kotu. To je zato, ker sta njegovi
kateti hkrati višini trikotnika. Višinska točka topokotnega
trikotnika leži v njegovi zunanjosti, ker
 niso vse višine v njegovi notranjosti. Ustrezna nožišča
pripadajo namreč nosilkam stranic, ne pa samim stranicam.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.7v.pic}
\caption{} \label{sl.skl.3.7.7v.pic}
\end{figure}

Središče očrtane krožnice je notranja oz. zunanja točka trikotnika,
odvisno od tega, ali je trikotnik ostrokotni oz. topokotni (Figure
\ref{sl.skl.3.7.7o.pic}). Formalni dokaz tega dejstva  bomo
izpustili. Dokažimo le naslednji izrek, ki se nanaša na pravokotne
trikotnike.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.7o.pic}
\caption{} \label{sl.skl.3.7.7o.pic}
\end{figure}


        \bizrek The circumcentre of a right-angled triangle is at the same time the midpoint of
        its hypotenuse.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.8.pic}
\caption{} \label{sl.skl.3.7.8.pic}
\end{figure}


\textbf{\textit{Proof.}} Označimo z $O$ središče hipotenuze $AB$ in
s $P$ središče katete $AC$ pravokotnega trikotnika $ABC$ (Figure
\ref{sl.skl.3.7.8.pic}). Daljica $OP$ je srednjica tega trikotnika,
ki ustreza kateti $BC$, zato je $OP\parallel BC$. Iz tega sledi $OP
\perp AC$. Torej sta trikotnika $OPC$ in $OPA$  skladna (izrek
\textit{SAS} \ref{SKS}) in je potem $OC \cong OA$.
Ker je še $OB \cong OA$,
 je točka $O$ središče očrtane krožnice tega trikotnika.
 \kdokaz

Daljica $OC$ iz prejšnjega izreka je težiščnica trikotnika. To
pomeni, da je težiščnica na hipotenuzo pravokotnega
trikotnika enaka polmeru očrtane krožnice tega trikotnika, hkrati pa
tudi polovici njegove hipotenuze.

Prejšnji izrek je povezan tudi s Talesovim izrekom za krožnico
\ref{TalesovIzrKroz} in njegovim obratnim izrekom
\ref{TalesovIzrKrozObrat}. Vse omenjene trditve bomo sedaj podali v
enem izreku.


          \bizrek Thales’ theorem for a circle (several forms - Figure
          \ref{sl.skl.3.7.9.pic}):
         \index{izrek!Talesov za krožnico}
           \label{TalesovIzrKroz2}
           \begin{enumerate}
            \item The circumcentre of a right-angled triangle is at the same time the midpoint of
                 its hypotenuse.
             \item If $t_c$ is the median of a right-angled triangle for its hypotenuse $c$ and $R$
               the circumradius of that triangle, then
            $R=t_c=\frac{c}{2}$.
               \item If $AB$ is a diameter of a circle $k$, then for any point $X\in k$  ($X\neq A$ and $X\neq B$) is
               $\angle AXB=90^0$.
              \item If $A$, $B$ in $X$ are three non-collinear points, such that $\angle AXB=90^0$, then the point $X$ lies on a circle with the diameter $AB$.
                 \end{enumerate}
            \index{izrek!Talesov za krožnico}
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.9.pic}
\caption{} \label{sl.skl.3.7.9.pic}
\end{figure}

Poznavanje značilnih točk trikotnika in lastnosti srednjice
trikotnika omogočata dokazovanje raznih drugih lastnosti tako
trikotnika  kot tudi štirikotnika in $n$-kotnika.


              \bzgled
              Let $CD$ be the altitude  at the hypotenuse $AB$ of a right-angled triangle $ABC$.
            If $M$ and $N$ are the midpoints of the line segments $CD$ and $BD$, then $AM \perp CN$.
           \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.10.pic}
\caption{} \label{sl.skl.3.7.10.pic}
\end{figure}

\textbf{\textit{Proof.}}  Daljica $NM$ je srednjica trikotnika
$BCD$, zato je po izreku \ref{srednjicaTrik} $NM \parallel BC$
(Figure \ref{sl.skl.3.7.10.pic}). Ker je kot pri oglišču $C$ pravi
kot, je tudi $NM \perp AC$. Zaradi tega je premica $NM$ nosilka
višine trikotnika $ANC$, Ker je še $CD$ višina tega trikotnika, je
 $M$ njegova višinska točka. Torej je premica $AM$ nosilka
tretje višine tega trikotnika in velja $AM \perp CN$.
 \kdokaz


        \bzgled
        If $P$ and $Q$ are the midpoints of the sides $BC$ and $CD$ of a parallelogram $ABCD$,
          then the lines $AP$ and $AQ$
         divide the diagonal $BD$ of this parallelogram into three congruent line segments.
        \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.11.pic}
\caption{} \label{sl.skl.3.7.11.pic}
\end{figure}

\textbf{\textit{Proof.}} Označimo z $E$ in $F$ presečišči daljic
$AP$ in $AQ$ z diagonalo $BD$ paralelograma $ABCD$ ter s $S$
presečišče njegovih diagonal $AC$ in $BD$ (Figure
\ref{sl.skl.3.7.11.pic}). Diagonali paralelograma se razpolavljata
(izrek \ref{paralelogram}), zato je točka $S$ skupno središče daljic
$AC$ in $BD$. To pomeni, da sta točki $E$ in $F$ težišči trikotnikov
$ACB$ in $ACD$, zato delita težiščnici $SB$ in $SD$ teh trikotnikov
v razmerju $2:1$ (izrek \ref{tezisce}). Torej:
 \begin{eqnarray*}
     BE &=& \frac{2}{3}BS = \frac{2}{3}DS = FD,\\
     EF&=& ES+ SF= \frac{1}{3}SB+ \frac{1}{3}SD=
     \frac{1}{3}(SB +SD)=\frac{1}{3} BD,
 \end{eqnarray*}
  kar smo želeli dokazati.  \kdokaz


           \bzgled
            Let $BAKL$ and $ACPQ$ be positively oriented squares
        in the same plane. Prove that the lines $BP$ and $CL$ intersect at a point lying
        on the line containing the altitude $AA'$ of the triangle $ABC$.
           \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.12.pic}
\caption{} \label{sl.skl.3.7.12.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bo  $AA'$
 višina trikotnika $ABC$ (Figure \ref{sl.skl.3.7.12.pic}). Označimo z $X$
  in $Y$ presečišči premice $AA'$ s
pravokotnicama na premico $CL$ skozi točko $B$ in na premico $BP$ skozi točko $C$.
Dokažimo da je $X = Y$. Trikotnika $BLC$ in $ABX$ sta po izreku \textit{ASA} \ref{KSK} skladna, ker je: $BL \cong AB$,
$\angle BLC\cong\angle ABX$ in $\angle BCL\cong\angle AXB$ (kota s pravokotnima krakoma -
izrek \ref{KotaPravokKraki}). Zaradi tega je $AX \cong BC$. Analogno
sta skladna tudi trikotnika $CPB$ in $ACY$, zato je $AY \cong BC$.
Torej velja $AX \cong AY$ oziroma $X = Y$. To pomeni, da so premice
$AA'$, $BP$ in $CL$ nosilke višin trikotnika $XBC$, zato se sekajo v
eni točki.
 \kdokaz


          \bzgled \label{zgledPravokotnik}
            Let $K$ be the midpoint of the side $CD$ of a rectangle $ABCD$.
          A point $L$ is the foot of the perpendicular from the vertex $B$ on the diagonal
         $AC$ and $S$ is the midpoint of
            the line segment $AL$. Prove that $\angle KSB$ is a right angle.
         \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.13.pic}
\caption{} \label{sl.skl.3.7.13.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bo $V$ središče daljice $BL$ (Figure \ref{sl.skl.3.7.13.pic}).
 Daljica $SV$ je srednjica
 trikotnika $ABL$ za osnovnico $AB$, zato je $SV\parallel AB$ in
 $SV =\frac{1}{2} AB$ (izrek \ref{srednjicaTrik}). Iz
 prve relacije in $BC\perp AB$ sledi $SV\perp BC$
 (izrek \ref{KotiTransverzala}). To pomeni, da sta
 $BL$ in $SV$ nosilki višin trikotnika $CSB$. Torej je $V$  višinska
 točka tega trikotnika, zato je $CV$ nosilka njegove tretje višine
 (izrek \ref{VisinskaTocka}) oz. velja $CV\perp SB$. Iz $SV\parallel AB$ in
 $SV =\frac{1}{2} AB=KC$ sledi, da je štirikotnik $SVCK$
 paralelogram oz. $CV\parallel SK$. Iz tega in $CV\perp SB$ na
 koncu sledi (izrek \ref{KotiTransverzala})  $SK\perp SB$, torej je
$\angle KSB$ pravi kot.
 \kdokaz



              \bzgled
              Let $AP$, $BQ$ and $CR$ be the altitude, the median
            and the bisector of the angle $ACB$ ($R\in AB$) of a triangle $ABC$. Prove that if
            the triangle $PQR$ is regular, then the triangle $ABC$ is also regular.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.14.pic}
\caption{} \label{sl.skl.3.7.14.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $PQR$ pravilni trikotnik oz.
$PQ\cong QR\cong RP$ (Figure \ref{sl.skl.3.7.14.pic}). Točka $Q$ je
središče hipotenuze $AC$ pravokotnega trikotnika $APC$, zato je $QA
\cong QC \cong QP$ (izrek \ref{TalesovIzrKroz2}. Ker je v tem
primeru tudi $QR\cong QC\cong QP$, iz istega izreka sledi, da je tudi
$\angle ARC$ pravi kot. Iz skladnosti trikotnikov $ACR$ in $BCR$
(izrek \ref{KSK}) dobimo, da je točka $R$ središče stranice $AB$ in
da velja $AC\cong BC$. Ker je točka $R$ središče hipotenuze $AB$
pravokotnega trikotnika $APB$, je $AB = 2RP = 2PQ = 2AQ = AC$.
Torej velja  $AB\cong AC\cong BC$, kar pomeni, da je tudi $ABC$
pravilni trikotnik.
 \kdokaz


Ni težko dokazati, da je nek trikotnik enakokrak natanko tedaj, ko
sta ustrezni težiščnici skladni. Analogno velja tudi za višine. Ali
podobno velja tudi za t. i. odseke simetral kotov?
 Daljici $BB'$ in $CC'$, kjer sta $BB'$ in $CC'$ simetrali notranjih kotov
  trikotnika $ABC$ ter $B'\in AC$ in $C'\in AB$, imenujemo
 \index{odsek simetrale kota} \pojem{odseka simetral kotov}. Odseke simetral ozačimo z $l_a$, $l_b$ in $l_c$.
 Omenjena
  trditev  velja tudi v tem primeru, ampak
dokaz ni tako enostaven. O tem govori naslednji znani izrek.



            \bizrek \index{izrek!Steiner-Lemusov}
            (Steiner-Lehmus\footnote{\textit{D. C. L. Lehmus} (1780--1863),\index{Lehmus, D. C. L.} francoski
            matematik, ki je leta 1840 poslal to, na prvi pogled enostavno
            trditev, slavnem švicarskemu geometru \index{Steiner, J.} \textit{J. Steinerju} (1796--1863),
             ki  je izpeljal zelo obsežen dokaz tega izreka. Nato je sledilo
             več različnih rešitev tega problema in eno od njih je leta 1908
              objavil
             francoski matematik \index{Poincar\'{e}, J. H.} \textit{J. H. Poincar\'{e}} (1854--1912).})
            Let  $BB'$ ($B' \in AC$) and $CC'$ ($C' \in AB$) be the bisectors
              of the interior angles of a triangle $ABC$. Then:
             $$AB \cong AC \Leftrightarrow BB'\cong CC'.$$
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.15.pic}
\caption{} \label{sl.skl.3.7.15.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.7.15.pic})

($\Rightarrow$) Iz $AB \cong AC$ sledi $\angle ABC \cong \angle
ACB$ (izrek \ref{enakokraki}) oz. $\angle B'BC \cong \angle C'CB$.
Po izreku \textit{ASA} \ref{KSK} sta trikotnika $B'BC$ in $C'CB$
skladna, zato je $BB'\cong CC'$.

($\Leftarrow$) Naj bo  $BB'\cong CC'$.
 Predpostavimo,  da ni $AB\cong AC$. Brez škode za splošnost
 naj bo $AB < AC$. V tem primeru je $\angle ACB < \angle ABC$
 (izrek \ref{vecstrveckot}) oz.
$\angle ACC'< \angle ABB'$. To pomeni, da v notranjosti kota $ABB'$
obstaja poltrak $p$ z izhodiščem $B$, ki stranico $AC$ seka v
takšni točki $D$, da hkrati velja  $\mathcal{B}(A,D,B')$ in $\angle
DBB'\cong \angle ACC'$. V trikotniku $BCD$ je $\angle ACB < \angle
DBC$ in zaradi tega tudi $BD < CD$ (izrek \ref{vecstrveckot}).
Torej obstaja takšna točka $E$, ki je med točkama $C$ in $D$, tako da je
$BD \cong CE$. Po izreku \textit{SAS} \ref{SKS} sta trikotnika
$BDB'$ in $CEC'$ skladna, zato sta skladna tudi kota $BDB'$ in
$CEC'$. Dokažimo, da to ni mogoče. Zaradi Paschevega aksioma
\ref{AksPascheva} (uporabljenega za trikotnik $AC'E$ in premico
$BD$) premica $BD$ seka daljico $C'E$ v neki točki $S$. V trikotniku
$SDE$ je kot $SEC$ (oz. kot $CEC'$) zunanji in po izreku
\ref{zunanjiNotrNotrVecji} ne more biti skladen nesosednjemu notranjemu
kotu $SDE$ (oz. kotu $BDB'$). To pomeni, da predpostavka $AB < AC$
(analogno tudi $AB > AC$) ni mogoča. Torej je $AB\cong AC$.
 \kdokaz


         \bzgled
          Let $A_1$ be the midpoint of the side $BC$ of a triangle $ABC$.
         Calculate the measure of the angle $AA_1C$, if
           $\angle BAC=45^0$ and $\angle ABC=30^0$.
         \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.1a.pic}
\caption{} \label{sl.skl.3.7.1a.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $CC'$ višina trikotnika $ABC$ (Figure
\ref{sl.skl.3.7.1a.pic}).

Iz $\angle CC'B = 90^0$ sledi najprej
$\angle C'CB=60^0$, nato pa še, da točka $C'$ leži na krožnici nad
premerom $CB$ in s središčem $A_1$ (izrek \ref{TalesovIzrKroz}), zato
je $A_1C'\cong A_1C\cong A_1B$. Torej je trikotnik $CC'A_1$
enakokrak, oz. po izreku \ref{enakokraki} velja $\angle CC'A_1
\cong\angle C'CB=60^0$. To pomeni, da je trikotnik $CC'A_1$
pravilen in je $C'C\cong C'A_1$. Iz dejstva, da je $AC'C$ enakokraki
trikotnik ($\angle CAC'=\angle ACC'=45^0$), pa sledi $AC'\cong C'C$. Če to povežemo s prejšnjo relacijo, dobimo $AC'\cong C'A_1$, kar
pomeni, da je tudi trikotnik $AC'A_1$ enakokrak. Zato je (izreka
\ref{enakokraki} in \ref{zunanjiNotrNotr}):
 $$\angle C'A_1A\cong\angle C'AA_1=\frac{1}{2}\angle A_1C'B=
 \frac{1}{2}\angle C'BA_1=\frac{1}{2}\cdot 30^0=15^0.$$
 Na koncu je še:
  $$\angle AA_1C=\angle C'A_1C-\angle C'A_1A =60^0-15^0=45^0,$$ kar je bilo potrebno izračunati. \kdokaz


        \bzgled
        Let $P$ be the midpoint of the side $BC$ of an isosceles triangle $ABC$
            and $Q$ the foot of the perpendicular from the point $P$ on the leg
        $AC$ of that triangle. Let $S$ be the midpoint of the line segment $PQ$. Prove that
        $AS \perp BQ$.
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.16.pic}
\caption{} \label{sl.skl.3.7.16.pic}
\end{figure}

\textbf{\textit{Proof.}} Iz skladnosti trikotnikov $ABP$ in $ACP$
(izrek \textit{SSS} \ref{SSS}) sledi skladnost sokotov $APB$ in
$APC$ oz. $AP\perp BC$ (Figure \ref{sl.skl.3.7.16.pic}). Označimo z
$R$ središče daljice $QC$. Daljica $SR$ je srednjica trikotnika
$QPC$ za osnovnico $PC$, zato je po izreku \ref{srednjicaTrik}
$SR\parallel CP$. Iz tega in $AP\perp BC$ sledi $SR\perp AP$. Torej je
$S$  višinska točka trikotnika $APR$, zato je po izreku
\ref{VisinskaTocka} tudi $AS\perp PR$. Toda daljica $PR$ je
srednjica trikotnika $BQC$ za osnovnico $BQ$, zato je $PR\parallel BQ$
(izrek \ref{srednjicaTrik}). Iz $AS\perp PR$ in $PR\parallel BQ$
dobimo $AS\perp BQ$.
 \kdokaz


       \bzgled \label{kotBSC}
      If $S$ is the incentre and $\alpha$, $\beta$,
       $\gamma$ the interior angles  at the vertices
        $A$, $B$, $C$  of a triangle
       $ABC$, then
       $$\angle BSC=90^0+\frac{1}{2}\cdot\alpha.$$
       \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.1c.pic}
\caption{} \label{sl.skl.3.7.1c.pic}
\end{figure}

\textbf{\textit{Proof.}}  Po izreku \ref{SredVcrtaneKrozn} se
simetrale notranjih kotov trikotnika $ABC$ sekajo v središču včrtane
krožnice - v točki $S$ (Figure \ref{sl.skl.3.7.1c.pic}). Zato je
$\angle SBC =\frac{1}{2}\cdot \beta$ in $\angle SCB
=\frac{1}{2}\cdot \gamma$. Ker je po izreku \ref{VsotKotTrik} v vsakem
trikotniku vsota notranjih kotov enaka $180^0$, sledi:
 $$\angle BSC = 180^0-\frac{1}{2}\cdot\left( \beta+
  \gamma\right)=180^0-\frac{1}{2}\cdot\left( 180^0-
 \alpha\right)=90^0+\frac{1}{2}\cdot\alpha,$$ kar je bilo treba dokazati. \kdokaz


        \bzgled
        Construct a triangle with given $a$, $t_a$, $R$ (see the labels  in section \ref{odd3Stirik}).
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.16a.pic}
\caption{} \label{sl.skl.3.7.16a.pic}
\end{figure}

\textbf{\textit{Proof.}} Konstrukcijo lahko izpeljemo tako, da najprej narišemo očrtano krožnico  $k(O,R)$, izberemo poljubno točko $B\in k$, načrtamo tetivo $BC\cong a$ te krožnice, središče $A_1$ tetive $BC$ in na koncu oglišče $A$ kot presečišče krožnic $k(O,R)$ in $k_1(A_1,t_a)$ (Figure \ref{sl.skl.3.7.16a.pic}). Jasno je, da ima naloga  rešitve natanko tedaj, ko je $a\leq 2R$ in presečišče krožnic $k(O,R)$ in $k_1(A_1,t_a)$ ni prazna množica. Število rešitev je v tem primeru odvisno od števila presečišč krožnic $k(O,R)$ in $k_1(A_1,t_a)$.
 \kdokaz

        \bzgled
        Construct a right-angled triangle if the hypotenuse and the altitude to that hypotenuse
         are congruent to the given line segments $c$ and $v_c$.
        \ezgled



\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.16b.pic}
\caption{} \label{sl.skl.3.7.16b.pic}
\end{figure}

\textbf{\textit{Analysis.}}
Naj bo $ABC$ pravokotni trikotnik s pravim kotom v oglišču $C$,
pri katerem sta hipotenuza $AB$ in višina $CC'$ skladni z daljicama $c$ in $v_c$ (Figure \ref{sl.skl.3.7.16b.pic}).
Po izreku \ref{TalesovIzrKroz2} je središče $O$ hipotenuze $AB$ hkrati središče očrtane krožnice trikotnika $ABC$.
Torej oglišče $C$  leži na krožnici $k$ s premerom $AB$. Ker je še $CC'\cong v_c$, leži oglišče $C$ tudi na vzporednici premice $AB$,
ki je od nje oddaljena za $v_c$. Točka $C$ je potem presečišče te vzporednice in krožnice $k$.


\textbf{\textit{Construction.}}
Najprej načrtajmo  daljico $AB$, ki je skladna z dano daljico $c$, nato še središče $O$ daljice $AB$ in krožnico $k(O,OA)$. Potem načrtajmo  vzporednico $p$ premice $AB$ na razdalji $v_c$. Eno od presečišč premice $p$ in krožnice $k(O,OA)$ označimo s $C$. Dokažimo, da je $ABC$ iskani trikotnik.


\textbf{\textit{Proof.}}
 Po konstrukciji točka $C$ leži na krožnici s polmerom $AB$, zato je po izreku \ref{TalesovIzrKroz2} $\angle ACB=90^0$, kar pomeni, da je $ABC$ pravokotni trikotnik s hipotenuzo $AB$. Po konstrukciji je le-ta skladna z daljico $c$. Naj bo $CC'$ višina trikotnika $ABC$. Po konstrukciji leži točka $C$ na premici $p$, ki je od premice $AB$ oddaljena $v_c$, zato je tudi $|CC'|=d(C,AB)=d(p,AB)$ oz. $CC'\cong v_c$.


\textbf{\textit{Discussion.}}
 Število rešitev je odvisno od števila presečišč premice $p$ in krožnice $k(O,OA)$.
 \kdokaz



        \bnaloga\footnote{2. IMO Romania - 1960, Problem 4.}
         Construct triangle ABC, given $v_a$, $v_b$ (the altitudes from $A$ and $B$) and $t_a$,
         the median from vertex $A$.
         \enaloga


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.IMO1.pic}
\caption{} \label{sl.skl.3.7.IMO1.pic}
\end{figure}

\textbf{\textit{Solution.}} Naj bo $ABC$ takšen trikotnik, da sta
$AA' \cong v_a$ in $BB' \cong v_b$ njegovi višini ter $AA_1\cong t_a$
njegova težiščnica (Figure \ref{sl.skl.3.7.IMO1.pic}). Označimo
z $A'_1$ pravokotno projekcijo točke $A_1$ na premici $AC$.
Daljica $A_1A'_1$ je srednjica trikotnika $BB'C$ za osnovnico
$BB'$, zato je po izreku \ref{srednjicaTrik}:
 $$|A_1A'_1|=\frac{1}{2}\cdot|BB'|=\frac{1}{2}\cdot v_b
 \hspace*{1mm} \textrm{ in }  \hspace*{1mm} A_1A'_1
\parallel BB'.$$ Iz tega sledi, da sta premici
$A_1A'_1$ in $AC$ pravokotni v točki $A'_1$, torej je premica $AC$
tangenta krožnice $k(A_1,\frac{1}{2} v_b)$ \ref{TangPogoj}.
Dokazane lastnosti nam omogočajo konstrukcijo.

 Najprej lahko načrtamo pravokotni trikotnik $AA'A_1$ ($AA'\cong v_a$,
 $AA_1\cong t_a$ in $\angle AA'A_1 = 90^0$), nato pa krožnico
 $k(A_1,\frac{1}{2} v_b)$. Iz točke $A$ načrtamo tangenti na
 krožnico $k(A_1,\frac{1}{2} v_b)$. Presečišče ene od tangent
 s premico $A'A_1$ označimo s $C$. Na koncu načrtamo takšno točko
  $B$, da velja
  $BA_1 \cong CA_1$ in $\mathcal{B}(C,A_1,B)$.

 Dokažimo, da trikotnik $ABC$ izpolnjuje dane pogoje. Iz
 konstrukcije je  $AA'\cong v_a$ višina in $AA_1 \cong t_a$
 težiščnica (ker je $A_1$ središče daljice $BC$) trikotnika
 $ABC$. Naj bo $BB'$ višina tega trikotnika. Dokažimo še $BB' \cong
 v_b$.
 Premica $AC$ je po konstrukciji tangenta krožnice $k(A_1,\frac{1}{2}
 v_b)$. Njuno dotikališče označimo z $A'_1$. Po izreku
 \ref{TangPogoj} sta premici
$A_1A'_1$ in $AC$ pravokotni v točki $A'_1$, zato je daljica
$A_1A'_1$ srednjica trikotnika $BB'C$ za osnovnico $BB'$ in velja
$|BB'|= 2\cdot |A_1A'_1|=2\cdot\frac{1}{2}\cdot v_b=v_b$.

 Naloga nima rešitev, kadar je $v_a>t_a$. Če je  $v_a\leq
 t_a$, je število rešitev odvisno od števila tangent, ki jih
 lahko načrtamo iz točke $A$ na krožnico $k(A_1,\frac{1}{2}
 v_b)$. Pri tem mora tangenta sekati premico $A'A_1$.
 Če velja $\frac{1}{2} v_b<t_a$ in $\frac{1}{2} v_b\neq v_a$,
  ima naloga dve rešitvi, v primeru $\frac{1}{2} v_b<t_a$ in
  $\frac{1}{2} v_b = v_a$ je rešitev le ena,  v primeru
  $\frac{1}{2} v_b\geq t_a$ pa rešitve ni.
 \kdokaz


%________________________________________________________________________________
 \poglavje{Euler's Circle. Eight Point Circle}
 \label{odd3EulKroz}

Sedaj bomo obravnavali zanimivo lastnost, ki se nanaša na
\index{trikotnik!pedalni}pedalni trikotnik, ki smo ga že definirali
kot trikotnik, ki je določen z nožišči višin nekega trikotnika, in t.
i. \index{trikotnik!središčni} \pojem{središčni trikotnik}, ki ga
določajo središča stranic tega trikotnika. Dokazali bomo namreč, da
imata omenjena trikotnika  skupno očrtano krožnico (Figure
\ref{sl.skl.3.8.1.pic}). Pred tem pa dokažimo naslednji pomožni izrek.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.8.1.pic}
\caption{} \label{sl.skl.3.8.1.pic}
\end{figure}



        \bizrek \label{EulerKroznicaLema}
        Let $V$ be the orthocentre of a triangle $ABC$. If $K$, $L$, $M$
         and $N$ are the midpoints of the line segments $AB$, $AC$, $VC$
        and $VB$, respectively, then the quadrilateral $KLMN$ is a rectangle.
        \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.8.2.pic}
\caption{} \label{sl.skl.3.8.2.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bo $AA'$ višina tega trikotnika. Daljici $KN$
in $LM$ sta srednjici trikotnikov $ABA'$ in $CAA'$ za skupno
osnovnico $AA'$, zato je po izreku \ref{srednjicaTrik}
$KN=\frac{1}{2}AA'=LM$ in $KN\parallel AA'\parallel LM$ (Figure
\ref{sl.skl.3.8.2.pic}). Torej je štirikotnik $KLMN$  paralelogram.
Dovolj je dokazati, da ima vsaj en notranji kot pravi.
Daljica $KL$ je srednjica trikotnika $ABC$, zato je $KL\parallel
BC$. Ker je še $KN\parallel AA'$ in $AA'\perp BC$, je tudi
$KL\perp KN$ oz. $\angle LKN=90^0$, kar pomeni, da je
paralelogram $KLMN$ hkrati pravokotnik.
 \kdokaz

 Sedaj smo pripravljeni na dokaz osnovnega izreka.



        \bizrek \label{EulerKroznica}
        For any given triangle
        the midpoints of the sides, the foots of the altitudes and
         the midpoints of the line segments from each vertex of the triangle to the orthocentre
         lie on the common circle - so-called  \index{krožnica!Eulerjeva}
        \pojem{Euler’s circle}\color{blue}\footnote{Krožnico imenujemo po
        švicarskem matematiku \index{Euler, L.} \textit{L. Eulerju}
        (1707--1783), ki je že leta 1765 dokazal, da imata pedalni in središčni
        trikotnik  skupno očrtano krožnico.
        Ostale lastnosti te krožnice so  leta 1821
        najprej obravnavali francoski matematiki \index{Poncelet, J. V.}
        \index{Brianchon, C. J.} \index{Terquem, O.} \index{Feuerbach, K. W.}
        \textit{J. V.
        Poncelet} (1788--1867) \textit{C. Brianchon}  (1783--1864) in
        \textit{O. Terquem}
        (1782--1862), kasneje pa še nemški matematik
         \textit{K. W. Feuerbach} (1800--1834).} of that triangle.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.8.3.pic}
\caption{} \label{sl.skl.3.8.3.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Uporabili bomo prejšnjo trditev \ref{EulerKroznica}. Če ohranimo
 iste oznake, smo že dokazali, da je štirikotnik $KLMN$ pravokotnik
 (Figure
\ref{sl.skl.3.8.3.pic}). Če s $P$ označimo središče
stranice $BC$ in s $Q$ središče daljice $AV$, je tudi $PMQK$
pravokotnik. Ker je $KM$ skupna diagonala teh dveh pravokotnikov, je
ta premer njune skupne očrtane krožnice $e$. Torej središča
stranic in središča daljic,
         ki povezujejo višinsko točko in oglišča,
        pripadajo isti krožnici $e$. Dokažimo še, da tudi nožišča višin
ležijo na tej krožnici. Točka $A'$, ki je nožišče višine iz oglišča
$A$, leži na krožnici $e$, ker je $\angle QA'P$ pravi kot in $PQ$
premer krožnice $e$ (Talesov izrek \ref{TalesovIzrKroz2}). Analogno na tej krožnici ležita tudi  nožišči $B'$ in $C'$ višin $BB'$
in $CC'$.
 \kdokaz

 Eulerjevo krožnico imenujemo tudi
 \index{krožnica!devetih točk} \index{krožnica!Feuerbachova}
 \pojem{Feuerbachova krožnica} in \pojem{krožnica devetih točk}.
 Še nekaj lastnosti Eulerjeve krožnice bomo obravnavali v razdelkih \ref{odd5EulPrem} in \ref{odd7SredRazteg}. Sedaj pa dokažimo analogno trditev za
 štirikotnike  t. i. \index{krožnica!osmih točk} \pojem{krožnica osmih točk}.



        \bizrek
        Let $ABCD$ be a quadrilateral with the perpendicular diagonals.
        Then the midpoints of the sides
         and the foots of the perpendiculars from these midpoints to the line
         containing the opposite sides of that quadrilateral lie on the same circle.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.8.4.pic}
\caption{} \label{sl.skl.3.8.4.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $ABCD$ štirikotnik s pravokotnima
diagonalama $AC$ in $BD$ (Figure \ref{sl.skl.3.8.4.pic}). Označimo z
$A_1$, $B_1$, $C_1$ in $D_1$ središča njegovih stranic $AB$, $BC$,
$CD$ in $DA$ ter z $A'$, $B'$, $C'$ in $D'$ pravokotne projekcije
teh središč na nosilkah nasprotnih stranic tega štirikotnika.
Štirikotnik $A_1B_1C_1D_1$ je paralelogram (Varignonov paralelogram
- izrek \ref{Varignon}). Ker sta diagonali $AC$ in $BD$ pravokotni,
je ta paralelogram  pravokotnik (izrek \ref{VarignonPoslPravRomb}),
zato njegova oglišča ležijo na isti krožnici. Diagonali $A_1C_1$ in
$B_1D_1$ sta premera te krožnice. Ker je $\angle C_1C'A_1=\angle
C_1A'A_1=\angle B_1D'D_1=\angle B_1B'D_1=90^0$, sledi (Talesov izrek
\ref{TalesovIzrKroz2}), da tudi točke $A'$, $B'$, $C'$ in $D'$ ležijo
na tej krožnici.
 \kdokaz

 Omenimo še, da lahko za poljuben trikotnik $ABC$ z višinsko točko $V$
  njegovo Eulerjevo krožnico  vidimo kot
krožnico osmih točk štirikotnika $ABVC$ (njegovi diagonali $AV$ in
$BC$ sta pravokotni - slika \ref{sl.skl.3.8.5.pic}), vendar se v tem
primeru dva para točk prekrivata in dejansko dobimo le šest
točk\footnote{To dejstvo je leta 1944 dokazal ameriški matematik
\index{Brand, L.} \textit{L. Brand} (1885--1971)}. Da bi dokazali, da
trditev (za Eulerjevo krožnico) velja za ostale tri točke, uporabimo
še krožnico osmih točk za štirikotnik $CAVB$. Ker imata dve krožnici
(za štirikotnika $ABVC$ in $CAVB$)  vsaj tri skupne točke, se
krožnici prekrivata – sta identični Eulerjevi krožnici trikotnika
$ABC$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.8.5.pic}
\caption{} \label{sl.skl.3.8.5.pic}
\end{figure}

 %_______________________________________________________________________________
 \poglavje{Tessellations} \label{odd3Tlakovanja}

V tem razdelku se bomo ukvarjali s prekrivanjem ravnine s skladnimi
liki. Takšno prekrivanje imenujemo \index{tlakovanja}
\pojem{tlakovanje} ali \index{teselacija} \pojem{teselacija}
ravnine. Lik, s katerim na ta način pokrivamo ravnino, je
\index{celica tlakovanja} \pojem{celica tlakovanja}. Najbolj znano
 tlakovanje je seveda prekrivanje ravnine s skladnimi
kvadrati. Obravnavali bomo še tlakovanje z drugimi liki. Najprej
bomo dali odgovor na vprašanje, katera so možna tlakovanja s
pravilnimi večkotniki.



        \bizrek \label{pravilnaTlakovanja}
        All possible tessellations $(n,m)$ of the plane with a regular $n$-gons,
        $m$ of them around each vertex, are
        (Figure \ref{sl.skl.3.9.1.pic})\footnote{Ta problem je rešil
        znameniti starogrški filozof in matematik \index{Pitagora}
        \textit{Pitagora z otoka Samosa}
         (582--497 pr. n. š.).}:
        $$(4,4),\hspace*{1mm} (6,3)\textrm{ in }
        (3,6).$$
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.9.1aa.pic}
\input{sl.skl.3.9.1bb.pic}
\input{sl.skl.3.9.1.pic}
\caption{} \label{sl.skl.3.9.1.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $O$ središče in $AB$ ena stranica
celice tlakovanja $(n,m)$ - pravilnega $n$-kotnika (Figure
\ref{sl.skl.3.9.2.pic}). S $S$ označimo središče stranice $AB$. Ker
je začetni $n$-kotnik pravilen in je $m$ takšnih okrog oglišča $B$,
notranji koti trikotnika $OSB$ pri ogliščih $O$, $B$ in $S$  po vrsti
merijo  $\frac{360^0}{2n}$, $\frac{360^0}{2m}$ in $90^0$. Po izreku
\ref{VsotKotTrik} je $\frac{360^0}{2n}+\frac{360^0}{2m}+90^0=180^0$.
Če enakost poenostavimo, dobimo ekvivalentno enakost:
$$\frac{1}{n}+\frac{1}{m}=\frac{1}{2},$$
oz. $nm-2n-2m=0$ in na koncu:
 \begin{eqnarray}
(n-2)(m-2)=4. \label{teselRelEvk}
\end{eqnarray}

 Ker sta $n$ in $m$ naravni števili in večji kot $2$,
so edine rešitve zadnje enačbe: $(n,m)\in \{(4,4), (3,6), (6,3)\}$.
 \kdokaz

\begin{figure}[!htb]
\centering
\input{sl.skl.3.9.2.pic}
\caption{} \label{sl.skl.3.9.2.pic}
\end{figure}

Tlakovanja ravnine s pravilnimi večkotniki imenujemo
\index{tlakovanja!pravilna} \pojem{pravilna tlakovanja} ravnine. V
evklidski ravnini  obstajajo torej tri pravilna tlakovanja.

Ker je v hiperbolični geometriji vsota notranjih kotov v trikotniku
vedno manjša od $180^0$, relacija za trikotnik $OSB$ iz prejšnjega
\ref{pravilnaTlakovanja} izreka postane:
$\frac{360^0}{2n}+\frac{360^0}{2m}+90^0<180^0$ in potem namesto
relacije \ref{teselRelEvk} dobimo:
 \begin{eqnarray}
(n-2)(m-2)>4. \label{teselRelHyp}
\end{eqnarray}
 Ta neenačba ima neskončno mnogo rešitev v množici $\mathbb{N}^2$, kar pomeni,
da imamo v hiperbolični geometriji  neskončno mnogo pravilnih tlakovanj.
Dve od njih sta npr. $(3,7)$ in $(4,5)$ (Figure
\ref{sl.skl.3.9.2H.pic}\footnote{http://math.slu.edu/escher/index.php/Category:Hyperbolic-Tessellations}).
Pri slednji se pet kvadratov stika okrog enega oglišča. To je
mogoče, ker je v hiperbolični geometriji notranji kot pri kvadratu vedno
oster in ni konstanten. Izkaže se, da ima kvadrat z daljšo stranico
manjši notranji kot. Mogoče je izbrati takšno stranico kvadrata,
da je notranji kot enak $\frac{360^0}{5} =72^0$, kar ravno
ustreza tlakovanju $(4,5)$.

\begin{figure}[!htb]
\centering
\includegraphics[width=0.413\textwidth]{whyptess1.eps}\hspace*{4mm}
 \includegraphics[width=0.387\textwidth]{whyptess.eps}
\caption{} \label{sl.skl.3.9.2H.pic}
\end{figure}

V eliptični geometriji, kjer je vsota kotov v trikotniku vedno
večja od $180^0$, omenjena relacija za trikotnik $OSB$ postane:
$\frac{360^0}{2n}+\frac{360^0}{2m}+90^0>180^0$, oz.:
 \begin{eqnarray}
(n-2)(m-2)<4. \label{teselRelElipt}
\end{eqnarray}
Ta enačba ima v množici $\mathbb{N}^2$  rešitve $(3,3)$, $(4,3)$,
$(3,4$), $(5,3)$ in $(3,5)$. Ker se eliptična geometrija realizira
kot model na sferi, te rešitve pomenijo tlakovanja sfere s sfernimi
večkotniki. Stranice teh večkotnikov so loki velikih krožnic sfere.
Če v evklidskem prostoru z daljicami povežemo ustrezna oglišča teh
tlakovanj, dobimo t. i. \index{pravilni!poliedri} \pojem{pravilne
poliedre} (Figure
\ref{sl.skl.3.9.2E.pic}\footnote{http://www.upc.edu/ea-smi/personal/claudi/web3d/}):
\pojem{pravilni tetraeder}, \pojem{kocko} (oz. \pojem{pravilni
heksaeder}), \pojem{pravilni oktaeder}, \pojem{pravilni dodekaeder}
in \pojem{pravilni ikozaeder}. Npr. $(4,3)$ bi predstavljal kocko,
pri kateri se po trije kvadrati (pravilna 4-kotnika) stikajo v eni
točki.


\begin{figure}[!htb]
\centering
 \includegraphics[bb=0 0 11cm 6cm]{wpoliedri.eps}
\caption{} \label{sl.skl.3.9.2E.pic}
\end{figure}


Vrnimo se nazaj k evklidski ravnini. Če dopustimo možnost, da pri
prekrivanju ravnine uporabimo več (končno mnogo) vrst pravilnih
večkotnikov oz. več vrst celic, ki so enako razporejene v vsakem oglišču, potem razen treh pravilnih
tlakovanj iz izreka \ref{pravilnaTlakovanja} obstaja še osem t. i.
\index{tlakovanja!Arhimedova} \pojem{Arhimedovih tlakovanj}
\footnote{Dokaz te trditve je izvedel nemški astronom, matematik in
fizik \index{Kepler, J.} \textit{J. Kepler} (1571--1630).} (Figure
\ref{sl.skl.3.9.2A.pic}\footnote{http://commons.wikimedia.org/wiki/File\%3AArchimedean-Lattice.png}).



\begin{figure}[!htb]
\centering
 \includegraphics[bb=0 0 10cm 7.7cm]{Archimedean.eps}
\caption{} \label{sl.skl.3.9.2A.pic}
\end{figure}

Razen pravilnih in Arhimedovih tlakovanj obstajajo tudi druga
tlakovanja z večkotniki, ki niso pravilni. Najbolj enostaven primer
je tlakovanje s skladnimi paralelogrami (Figure
\ref{sl.skl.3.9.3a.pic}), ki ga dobimo, če pravilno
tlakovanje $(4,4)$ tako deformiramo, da se namesto kvadratov v enem oglišču stikajo štirje
paralelogrami. To tlakovanje je določeno z mrežo
dveh šopov vzporednic.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.9.3aa.pic}
\input{sl.skl.3.9.3aaa.pic}
\caption{} \label{sl.skl.3.9.3a.pic}
\end{figure}

\begin{figure}[!htb]
\centering
\input{sl.skl.3.9.3bb.pic}
\input{sl.skl.3.9.3cc.pic}
\caption{} \label{sl.skl.3.9.3bc.pic}
\end{figure}

Če vse paralelograme razdelimo na
dva trikotnika z diagonalami, ki imajo isto smer,  dobimo tlakovanje ravnine s skladnimi trikotniki
(Figure \ref{sl.skl.3.9.3a.pic}). Trikotnik (osnovna celica) je lahko
poljuben, saj lahko dva takšna (skladna) trikotnika po skupni
stranici vedno povežemo  v paralelogram in tako dobimo tlakovanje s
paralelogrami. Tlakovanje s poljubnimi skladnimi trikotniki je
posplošitev pravilnega tlakovanja $(3,6)$ s pravilnimi trikotniki.


%\vspace*{-1mm}

Kot posebna primera tlakovanja s paralelogrami dobimo tlakovanje s
pravokotniki in tlakovanje z rombi (Figure \ref{sl.skl.3.9.3bc.pic}).
Dokazali bomo še bolj splošno
trditev, ki morda ni tako samoumevna. Mogoče je namreč tudi
tlakovanje s poljubnimi skladnimi štirikotniki.

%\vspace*{-1mm}



        \bzgled
        Let $ABCD$ be an arbitrary quadrilateral. Prove that it is
        possible to tessellate the plane with the cell $ABCD$ so that each vertex
         is surrounded by four such quadrilaterals.
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.9.4.pic}
\caption{} \label{sl.skl.3.9.4.pic}
\end{figure}

 \textbf{\textit{Proof.}}  (Figure
\ref{sl.skl.3.9.4.pic})
 Naj bo $ABCD$ poljuben štirikotnik v
ravnini z notranjimi koti $\alpha$, $\beta$, $\gamma$ in $\delta$.
Točki $O$ in $S$ naj bosta središči njegovih stranic $AB$ in $BC$. S središčnima
zrcaljenjema
 $\mathcal{S}_O$ in $\mathcal{S}_S$ (za definicijo središčnega zrcaljenja
 glej razdelek \ref{odd6SredZrc})
 se štirikotnik  $ABCD$ preslika v štirikotnika
$BAC_1D_1$ in $A_2CBD_2$. Pri tem je $\angle ABD_1\cong\alpha$ in
$CBD_2\cong\gamma$, zato je tudi $\angle D_1BD_2\cong\delta$. Ker je
še $BD_1\cong AD$ in $BD_2\cong CD$, obstaja takšna točka $E$,  da
sta štirikotnika $D_1ED_2B$ in $ABCD$ skladna. Torej se okrog točke
$B$ stikajo štirje štirikotniki, ki so vsi skladni štirikotniku
$ABCD$. Postopek ‘‘prekrivanja’’ ravnine lahko nadaljujemo, če
uporabljamo središčne simetrije glede na središča stranic
novonastalih štirikotnikov.
 \kdokaz

 Torej obstajajo tlakovanja ravnine s poljubnim trikotnikom in poljubnim
  štirikotnikom. Jasno je, da za poljubni petkotnik, šestkotnik,...
  ta lastnost ne velja.
Za pravilni šestkotnik obstaja pravilno tlakovanje $(6,3)$. Če v
prejšnjem izreku sestavimo po dva ustrezna sosednja štirikotnika,
dobimo prekrivanje ravnine s skladnimi šestkotniki, ki niso nujno
pravilni, so pa vedno središčno simetrični.


 %_______________________________________________________________________________
 \poglavje{Sets of Points in a Plane. Sylvester's Problem}
 \label{odd3Silvester}

V tem razdelku bomo raziskovali probleme, ki so povezani z množicami
točk v ravnini in s premicami, ki jih te točke določajo. Na začetku bomo
obravnavali nekaj posledic prvih dveh skupin aksiomov (incidence
in urejenosti).
 Najprej bomo definirali nove pojme. Naj bo $\mathfrak{T}$ množica
 $n$ ($n>2$) točk v ravnini. S $\mathcal{P}(\mathfrak{T})$ označimo
 množico vseh premic, od katerih gre vsaka skozi vsaj dve točki iz
 množice $\mathfrak{T}$ (Figure
\ref{sl.skl.3.10.1.pic}). Ker množica $\mathfrak{T}$ vsebuje vsaj
dve točki,
 iz aksiomov incidence sledi, da je
 množica $\mathcal{P}(\mathfrak{T})$ neprazna. Zastavlja se
 vprašanje, koliko  premic je v množici
 $\mathcal{P}(\mathfrak{T})$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.1.pic}
\caption{} \label{sl.skl.3.10.1.pic}
\end{figure}



        \bizrek \label{stevPremic}
        Let $\mathfrak{T}$ be a set of $n$ ($n>2$) points in the plane such that
        no three of them are collinear. Then the number of lines of the set $\mathcal{P}(\mathfrak{T})$ is equal to
         $$\frac{n(n-1)}{2}.$$
         \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.2.pic}
\caption{} \label{sl.skl.3.10.2.pic}
\end{figure}

\textbf{\textit{Proof.}} Skozi vsako od $n$ točk iz množice
$\mathfrak{T}$ poteka natanko $n -1$ premic iz množice
$\mathcal{P}(\mathfrak{T})$. Ker na ta način vsako premico štejemo
dvakrat (Figure \ref{sl.skl.3.10.2.pic}), moramo še deliti z 2. Torej je v množici
$\mathcal{P}(\mathfrak{T})$ ravno $\frac{n(n-1)}{2}$ premic.
 \kdokaz

Prejšnji izrek lahko rešimo tudi na naslednji način: skozi prvo
točko gre $n -1$ premic, skozi drugo $n - 2$ premic (ena manj, ker
premice, ki je določena s tema dvema točkama, ne štejemo dvakrat), $n
- 3$ premic skozi tretjo točko in tako naprej vse do ene premice
skozi predzadnjo točko. To je skupaj  $(n -1) + (n - 2) +\cdots+1$
premic. Seveda je to spet enako $\frac{n(n-1)}{2}$. Če vzamemo
$n-1= k$, dobimo znano formulo za vsoto prvih $k$ naravnih števil:
 $$1+ 2+ \cdots + k=\frac{k(k+1)}{2}.$$

 Iz prejšnjega izreka lahko izpeljemo formulo za število diagonal
 poljubnega $n$-kotnika.



            \bizrek
            If $D_n$ is the number of diagonals of an arbitrary $n$-gon,
            then
             $$D_n=\frac{n( n-3)}{2}.$$
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.3.pic}
\caption{} \label{sl.skl.3.10.3.pic}
\end{figure}

\textbf{\textit{Proof.}} Označimo s $\mathfrak{O}$ množico vseh
oglišč poljubnega $n$-kotnika.
  Število diagonal je enako številu vseh premic
iz množice $\mathcal{P}(\mathfrak{O})$ (izreka \ref{stevPremic})
zmanjšano za število njegovih stranic (Figure
\ref{sl.skl.3.10.3.pic}). Torej:
 $$D_n=\frac{n(n- 1)}{2}-n=\frac{n^2-3n}{2}=\frac{n(n-3)}{2},$$ kar je bilo treba dokazati. \kdokaz

Omenimo še, da bi lahko formulo za število diagonal $n$-kotnika
izpeljali tudi direktno - s podobno obravnavo kot v dokazu izreka
\ref{stevPremic}. Iz vsakega od $n$ oglišč $n$-kotnika lahko
narišemo $n - 3$ diagonal. Na ta način vsako diagonalo štejemo
dvakrat, zato moramo še deliti z 2 in dobimo prejšnjo formulo.

Izrek \ref{stevPremic} se je nanašal na število premic, ki so
določene z množico točk v ravnini, ki so v takšni legi, da
nobene tri niso kolinearne. V naslednjem primeru bomo preverili, kaj se
zgodi, če dodamo nove pogoje.



            \bzgled
            Let $\mathfrak{T}$ be a set of $n$ ($n > 2$) points in the plane which are
            in such a position that $m$ ($m < n$) of them lies on the same line, but otherwise
            no other three points are collinear. What is the number of lines
            in the set $\mathcal{P}(\mathfrak{T})$?
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.4.pic}
\caption{} \label{sl.skl.3.10.4.pic}
\end{figure}

\textbf{\textit{Solution.}}
 (Figure \ref{sl.skl.3.10.4.pic})

 Brez dodatnega pogoja bi v množici $\mathcal{P}(\mathfrak{T})$
  obstajalo  $\frac{n(n -1)}{2}$ premic (izrek \ref{stevPremic}).
  Dodatni pogoj v nalogi  to
število zmanjša, in sicer za $1$ manj kot je število premic, ki jih določa
množica $m$ točk v splošni legi. To je zaradi tega, ker bi sicer
te premice šteli večkrat. Torej je število premic množice
$\mathcal{P}(\mathfrak{T})$  enako:
$$\frac{(n-1)}{2}-\frac{(m -1)}{2}+1.$$
 \kdokaz

Naslednji enostaven primer bo uvod v zelo zanimiv problem odnosa
množice točk $\mathfrak{T}$ in množice vseh premic
$\mathcal{P}(\mathfrak{T})$, ki jo ta množica točk določa.


            \bzgled
            Construct nine points lying on ten lines
            in such a way, that each of those ten lines contains exactly three of these nine points\footnote{\index{Newton, I.}
            \textit{I. Newton} (1642--1727), znani angleški
            matematik
            in fizik, ki je zastavil ta problem v obliki:
            ‘‘How can you plant 9 trees in a garden with 10 rows and each row containing exactly 3 trees?’’}.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.5.pic}
\caption{} \label{sl.skl.3.10.5.pic}
\end{figure}

\textbf{\textit{Proof.}} Ena od možnosti je naslednja. Naj bo $ABCD$
poljubni pravokotnik, $P$ in $Q$ središči stranic $AB$ in $CD$, $S$
presečišče diagonal, $K$ presečišče premic $AP$ in $DQ$ ter $L$
presečišče premic $BP$ in $CQ$ (Figure \ref{sl.skl.3.10.5.pic}). Ker
je $ABCD$ pravokotnik, so točke $P$, $Q$ in $S$  kolinearne. Prav tako
so kolinearne tudi
 točke $K$, $L$ in $S$ (točki $K$ in $L$ sta središči pravokotnikov
  $AQPD$ in $QBCP$). Torej imamo devet točk $A$, $B$, $C$, $D$, $P$,
  $Q$, $S$, $K$ in $L$, od katerih po tri ležijo na vsaki od desetih premic $AB$,
   $CD$, $PQ$, $KL$, $AC$, $BD$,
$PA$, $PB$, $QC$ in $QD$.
 \kdokaz

 Če v prejšnjem zgledu množico devetih točk označimo s $\mathfrak{T}$, vidimo,
 da množica desetih premic ni množica $\mathcal{P}(\mathfrak{T})$.
  V množici $\mathcal{P}(\mathfrak{T})$ bi namreč imeli  šestnajst
  premic - naših deset in še dodatne premice $AD$, $BC$ $DL$, $AL$, $CK$ in $BK$.
  Toda vsaka od teh šestih premic vsebuje
le dve točki. Za njih torej ni izpolnjen pogoj, da vsebujejo
natanko tri točke začetne množice. Sedaj je logično zastaviti
naslednje vprašanje: Ali je v ravnini sploh mogoče postaviti končno
množico nekolinearnih točk $\mathfrak{T}$ tako, da vsaka premica iz množice
$\mathcal{P}(\mathfrak{T})$ vsebuje natanko tri točke iz množice
$\mathfrak{T}$? Jasno je namreč, da je to možno, če zahtevamo,
da vsaka premica iz $\mathcal{P}(\mathfrak{T})$ vsebuje natanko dve
točki iz $\mathfrak{T}$. Najbolj enostaven primer za to so oglišča
trikotnika in njegove nosilke, ali pa poljubna množica točk iz
izreka \ref{stevPremic}. Že omenjeni problem za tri točke ni tako
enostaven, odgovor pa bomo poiskali v nadaljevanju. Omenimo, da je
negativen. Celo več - odgovor je negativen tudi v primeru,
ko zahtevamo, da vsaka premica iz $\mathcal{P}(\mathfrak{T})$ vsebuje
vsaj tri točke iz  $\mathfrak{T}$. Najprej pa dokažimo  eno lemo
(pomožno trditev).



            \bizrek \label{SylvesterLema}
           Let $\mathfrak{T}$ be a finite set of points in the plane which do not all lie on the same line
            and $\mathcal{P}=\mathcal{P}(\mathfrak{T})$. If $T_0\in \mathfrak{T}$ and $p_0\in \mathcal{P}$ ($T_0\notin p_0$)
             are such that they determine the minimum distance, i.e.
            $$(\forall T\in \mathfrak{T})(\forall p\in \mathcal{P})
              ( T\notin p\Rightarrow d(T,p)\geq d(T_0,p_0)),$$
            then the line $p_0$ contains exactly two points from the set $\mathfrak{T}$.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.6.pic}
\caption{} \label{sl.skl.3.10.6.pic}
\end{figure}

\textbf{\textit{Proof.}} Predpostavimo nasprotno. Naj premica $p_0$
vsebuje vsaj tri različne točke $A$, $B$ in $C$ iz množice
$\mathfrak{T}$ (Figure \ref{sl.skl.3.10.6.pic}). Označimo s $T'_0$ pravokotno projekcijo točke $T_0$
na premici $p_0$. Če se točka $T'_0$ razlikuje od točk $A$, $B$ in
$C$, sta vsaj dve od teh treh točk (naj bosta to $B$ in $C$) na premici $p_0$ na isti
strani točke $T'_0$. Brez škode za splošnost naj bo
$\mathcal{B}(T'_0,B,C)$. Ker $T_0,C \in \mathfrak{T}$, potem tudi premica
$q= CT_0$  ($q \neq p_0$, ker $T_0\notin p_0$) pripada množici
$\mathcal{P}$. Naj bo $B'$ pravokotna projekcija točke  $B$ na
premici $q$. Ni težko dokazati, da v tem primeru velja:
 $$d(B,q)=|BB'|<T_0T'_0=d(T_0,p_0).$$
 Zadnja relacija je v
nasprotju s predpostavko, zato premica $p_0$ vsebuje natanko dve
točki.

Če  $T_0$ leži na eni od točk $A$, $B$ ali $C$, je dokaz
 podoben.
 \kdokaz

 Sedaj bomo dokazali napovedan izrek.


            \bizrek
            Let $\mathfrak{T}$ be a finite set of points in the plane which do not all lie on the same line.
            Then there is a line that contains exactly two points from the set
            $\mathfrak{T}$
            \index{problem!Sylvestrov}
             (\textit{Sylvester's\footnote{\index{Sylvester, J. J.} \index{Karamata, J.}
            \index{Erdös, P.} \index{Gallai, T.} \index{Kelly, L. M.}
            \index{Coxeter, H. S. M.}
             Angleški matematik \textit{J. J. Sylvester} (1814--1897)
              je zastavil ta problem že leta 1893,
              ki takrat ni bil rešen in so nanj pozabili.
                Šele čez štirideset let (leta 1933) sta sta ga ponovno ‘‘obudila’’ Madžarski matematik
            \textit{P. Erdös} (1913--1996) in srbski matematik \textit{J.
            Karamata} (1902--1967), madžarski matematik
            \textit{T. Gallai} (1912–-1992) pa ga je istega leta rešil. Nato je bilo
            objavljenih več različnih dokazov rešitve tega problema - najbolj eleganten
            iz leta 1948, ki ga je podal ameriški matematik \textit{L. M. Kelly}
            (1914-–2002), je prikazan tukaj. Leta 1961 je veliki kanadski
            geometer \textit{H. S. M. Coxeter} (1907--2003) dokazal to
            trditev brez uporabe skladnosti - le kot posledico aksiomov
            incidence in urejenosti.} problem}).
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.7.pic}
\caption{} \label{sl.skl.3.10.7.pic}
\end{figure}

\textbf{\textit{Proof.}}
Naj bo $\mathcal{P}=\mathcal{P}(\mathfrak{T})$. Ker je množica
$\mathfrak{T}$ končna,  je končna tudi množica $\mathcal{P}$, nato
pa tudi množica vseh razdalj (Figure \ref{sl.skl.3.10.7.pic}):
$$\mathcal{D} = \{d(T,p);\hspace*{1mm}
T\in \mathfrak{T},\hspace*{1mm} p\in \mathcal{P},\hspace*{1mm} T\notin p\}.$$
 Ker je $\mathcal{D}$ končna množica pozitivnih realnih števil, ima svoj
minimalni element $d(T_0,p_0)$ (nobena razdalja iz
$\mathcal{D}$ ni manjša), ki se doseže za neko točko $T_0\in
\mathfrak{T}$ in neko premico $p_0\in \mathcal{P}$. Iz definicije
množice $\mathcal{D}$ sledi $T_0\notin p_0$. Po prejšnji lemi
\ref{SylvesterLema} ležita na premici $p_0$  natanko dve točki iz
množice $\mathfrak{T}$.
 \kdokaz

 Ta razdelek bomo končali še z dvema zanimivima primeroma.



            \bizrek
            Let $\mathfrak{T}$ be a finite set of points,
            such that distances between two points of this set are all different.
            If we connect each point with a line segment to its nearest point, then none of the points will be
            directly connected to more than five points from this set\footnote{Poljski matematik, astronom in fizik
              \index{Steinhaus, H.}\textit{H. Steinhaus} (1887--1972)
              je ta problem zapisal v obliki:
              ‘‘Vsako mesto na zemljevidu Evrope povežemo... ’’}.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.8.pic}
\caption{} \label{sl.skl.3.10.8.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Najprej ugotovimo, da sta lahko dve poljubni točki $X$ in $Y$  povezani
 v eni od treh različnih
možnosti (Figure \ref{sl.skl.3.10.8.pic}):

 \textit{1)} točki $X$ je najbližja točka $Y$, ne pa obratno;

 \textit{2)} točki
$Y$ je najbližja točka $X$, ne pa obratno;

\textit{3)} točki $X$ je najbližja točka $Y$ in obratno - točki $Y$
je najbližja točka $X$.

Vsaki  točki je najbližja samo ena točka, toda ta je
lahko povezana z več točkami,  katerim je  najbližja. Potrebno
je dokazati, da takšnih točk, s katerimi je povezana, ni več kot
pet. Predpostavimo nasprotno. Naj bo $P$ točka dane množice
$\mathfrak{T}$ in je z daljico povezana z vsaj šestimi točkami $A$,
$B$, $C$, $D$, $E$ in $F$. Brez škode za splošnost lahko
predpostavimo, da so tako razporejene (oz. lahko jih tako označimo),
da bo $ABCDEF$ šestkotnik (Figure \ref{sl.skl.3.10.8.pic}). Ena izmed
točk $A$, $B$, $C$, $D$, $E$ in $F$ je najbližja točki $P$, naj bo
to točka $A$. Torej velja: $PA < PB, PC, PD, PE, PF$. Ker so tudi
točke $B$, $C$, $D$, $E$ in $F$ povezane s točko $P$, pomeni da je
točka $P$ najbližja vsaki od njih (ne pa obratno). Na osnovi tega je
najprej $BA > BP > PA$, zato je $\angle APB$ največji kot v
trikotniku $APB$ in je zaradi tega večji od $60^0$. Podobno je $CB >
BP,BC$, zato je tudi $\angle BPC > 60^0$. Enako bi veljalo tudi za
kote $CPD$, $DPE$, $EPF$ in $EPA$, kar pa ni mogoče, saj je njihova
vsota vedno enaka ali celo večja od $360^0$, ne glede na to, ali je
$P$ notranja ali zunanja točka šestkotnika $ABCDEF$. Torej točka $P$
ni povezana z več kot s petimi točkami.
 \kdokaz


            \bzgled
            What is the maximum number of regions in the plane that can be
            divided by $n$ lines\footnote{Ta problem je rešil švicarski geometer
            \index{Steiner, J.} \textit{J. Steiner} (1796--1863).}?
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.9.pic}
\caption{} \label{sl.skl.3.10.9.pic}
\end{figure}

\textbf{\textit{Solution.}}  Opisali bomo postopek načrtovanja takšnih
$n$ premic (Figure \ref{sl.skl.3.10.9.pic}). Če je $n = 1$, oz. če
gre le za eno premico, je ravnina razdeljena na dve območji. Dve
premici, če nista vzporedni, razdelita ravnino na štiri območja. Če
dodamo tretjo premico $p_3$, ki z njima ni vzporedna in ne gre skozi
njuno skupno točko,  seka začetni dve premici v dveh točkah. Ti
dve točki delita premico $p_3$ na tri dele, vsak od njih pa je v
enem od treh od prejšnjih štirih območij ravnine. Torej s premico
$p_3$ dobimo še tri nove dele ravnine, torej skupaj sedem. Postopek
nadaljujemo. Če $n -1$ premic deli ravnino na $k$ delov, z
dodajanjem $n$-te premice $p_n$ (ki ni vzporednica nobene od
prejšnjih $n -1$ premic in ne vsebuje nobenega njihovega presečišča),
dobimo najprej $n -1$ presečišč na tej premici, nato $n$ njenih
delov oz. $n$ novih območij dane ravnine. Torej je največje možno
število območij za $n$ premic enako:
\begin{eqnarray*}
2+2+3+\cdots+n&=&1+1+2+3+\cdots+n=\\
&=&1+\frac{n(n+1)}{2}=\\&=&\frac{n^2+n+2}{2}.
\end{eqnarray*}
Formalni dokaz tega dejstva bi lahko izpeljali z matematično indukcijo.
 \kdokaz


 %_______________________________________________________________________________
 \poglavje{Helly's Theorem}
\label{odd3Helly}

Naslednji pomemben izrek je posledica le prvih dveh skupin aksiomov
oz. aksiomov incidence in aksiomov urejenosti. Uporabili ga bomo
tudi pri nalogah, ki so povezane s skladnostjo.



            \bizrek \label{Helly}
            Let $\Phi_1$, $\Phi_2$, ... , $\Phi_n$ ($n \geq 4$) be convex sets in the plane.
            If every three of these sets have a common point, then all $n$ sets have a common point
            \index{izrek!Hellyjev}(Helly's theorem\footnote{Avstrijski
            matematik  \index{Helly, E.} \textit{E. Helly} (1884--1943)
             je odkril to trditev v splošnem primeru $n$-razsežnega
             prostora $\mathbb{E}^n$
              leta 1913, objavil pa šele leta 1923. Alternativna dokaza sta
              medtem podala avstrijski matematik \index{Radon, J. K. A.}
              \textit{J. K. A. Radon} (1887-–1956) leta 1921 in
              madžarski matematik \index{Kőnig, D.}
              \textit{D. Kőnig} (1884–-1944) leta 1922.}).
            \eizrek

\begin{figure}[!htb]
\centering
\hspace*{10mm}
\input{sl.skl.3.11.1.pic}
\caption{} \label{sl.skl.3.11.1.pic}
\end{figure}

\textbf{\textit{Proof.}} Dokaz bomo izvedeli z indukcijo po $n$.

\textit{(A)} Naj bo najprej $n = 4$ in (Figure
\ref{sl.skl.3.11.1.pic}):
\begin{itemize}
  \item $P_4\in \Phi_1 \cap \Phi_2 \cap \Phi_3$,
  \item $P_3\in \Phi_1 \cap \Phi_2 \cap \Phi_4$,
  \item $P_2\in \Phi_1 \cap \Phi_3 \cap \Phi_4$,
  \item $P_1\in \Phi_2 \cap \Phi_3 \cap \Phi_4$.
\end{itemize}
Dokažimo, da obstaja točka, ki leži v vsakem od likov  $\Phi_1$,
$\Phi_2$, $\Phi_3$ in $\Phi_4$. Glede na medsebojno lego
točk $P_1$, $P_2$, $P_3$ in $P_4$ bomo od več možnih primerov
obravnavali samo dva najbolj
splošna (dokaz v ostalih primerih je
podoben).

\textit{1)} Štirikotnik, ki ga določajo točke $P_1$, $P_2$, $P_3$ in
$P_4$, je nekonveksen. V tem primeru je ena od točk $P_1$, $P_2$,
$P_3$ in $P_4$ notranja točka trikotnika, ki ga določajo preostale
tri točke. Brez škode za splošnost naj bo $P_4$ notranja točka
trikotnika $P_1P_2P_3$. Oglišča tega trikotnika ležijo v liku
$\Phi_4$. Ker je $\Phi_4$ konveksni lik, v njemu ležijo tudi vse
stranice in notranje točke trikotnika $P_1P_2P_3$, prav tako tudi
točka $P_4$. V tem primeru je točka $P_4$  skupna točka likov
$\Phi_1$, $\Phi_2$, $\Phi_3$ in $\Phi_4$.

\textit{2)}  Štirikotnik, ki ga določajo točke $P_1$, $P_2$, $P_3$
in $P_4$, je konveksen. Brez škode za splošnost naj bosta njegovi
diagonali $P_1P_2$ in $P_3P_4$. Ker je štirikotnik konveksen, se
njegovi diagonali sekata v neki točki $S$. Dani liki so konveksni,
zato iz $P_1, P_2\in \Phi_3,\Phi_4$ sledi, da diagonala $P_1P_2$
vsa leži v likih $\Phi_3$ in $\Phi_4$. Analogno iz $P_3, P_4\in
\Phi_1,\Phi_2$ sledi, da diagonala $P_3P_4$ vsa leži v likih
$\Phi_1$ in $\Phi_2$. Točka $S$, ki leži na obeh diagonalah
$P_1P_2$ in $P_3P_4$, leži v vseh štirih likih $\Phi_1$, $\Phi_2$,
$\Phi_3$ in $\Phi_4$.

S tem smo dokazali, da trditev velja za $n=4$.

\textit{(B)} Predpostavimo sedaj, da trditev velja za $n = k$ ($k\in
\mathbb{N}$ in $k>4$).
 Dokažimo, da trditev velja tudi za
$n = k +1$. Naj bodo $\Phi_1$, $\Phi_2$, $\ldots$ , $\Phi_{k-1}$,
$\Phi_k$ in $\Phi_{k+1}$ takšni liki, da ima vsaka poljubna trojica teh likov
vsaj eno skupno točko. Naj bo $\Phi'=\Phi_k\cap\Phi_{k+1}$. Dokažimo
najprej, da ima vsaka trojica likov $\Phi_1$, $\Phi_2$ ,$\ldots$,
$\Phi_{k-1}$, $\Phi'$ skupno točko. Za trojice likov izmed
$\Phi_1$, $\Phi_2$, $\ldots$, $\Phi_{k-1}$ je to izpolnjeno že po
predpostavki. Brez škode za splošnost je dovolj, če dokazažemo, da
imajo liki $\Phi_1$, $\Phi_2$ in $\Phi'=\Phi_k\cap\Phi_{k+1}$
skupno točko. To pa velja  (na osnovi dokazanega primera za $n = 4$),
ker ima vsaka trojica izmed likov $\Phi_1$, $\Phi_2$,  $\Phi_k$ in
$\Phi_{k+1}$  skupno točko. Iz indukcijske predpostavke
(za $n=k$) sledi, da imajo liki $\Phi_1$, $\Phi_2$, $\ldots$,
$\Phi_{k-1}$, $\Phi'$  skupno točko, ta točka pa hkrati leži v
vsakem od likov $\Phi_1$, $\Phi_2$, $\ldots$,  $\Phi_{k-1}$,
$\Phi_k$, $\Phi_{k+1}$.
 \kdokaz

V nadaljevanju bomo obravnavali nekaj posledic Hellyjevega izreka.



            \bzgled
           Let $\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$
            ($n > 3$) be half-planes covering a plane $\alpha$.
            Prove that there are three of these half-planes that also cover the plane $\alpha$.
            \ezgled


\textbf{\textit{Proof.}} Naj bodo $\beta_1$, $\beta_2$, $\cdots$,
$\beta_n$ odprte polravnine, ki so določene s polravninami
$\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$ kot  komplementarne
polravnine glede na ravnino $\alpha$ oz.
$\beta_k=\alpha\setminus\alpha_k$, $k\in\{1,2,\ldots,n\}$.
Za vsako točko $X$ ravnine $\alpha$ in vsak
$k\in\{1,2,\ldots,n\}$ velja ekvivalenca:
 $$X\in \alpha_k \Leftrightarrow X\notin \beta_k.$$
Predpostavimo nasprotno, da nobena trojica polravnin $\alpha_1$,
$\alpha_2$, $\cdots$, $\alpha_n$ ne prekriva ravnine $\alpha$. To
 pomeni, da za vsako trojico izmed njih obstaja točka v ravnini $\alpha$,
ki ne leži na nobeni od njih, oziroma da za vsako trojico izmed polravnin
$\beta_1$, $\beta_2$, $\cdots$, $\beta_n$ obstaja točka ravnine
$\alpha$, ki leži na vsaki od njih. Ker so polravnine konveksni
liki, iz Hellyjevega izreka \ref{Helly} sledi, da obstaja točka
$X$, ki leži  na vsaki od polravnin $\beta_1$, $\beta_2$, $\cdots$,
$\beta_n$. Ta točka torej leži v  ravnini $\alpha$, ne leži pa v
nobeni od polravnin $\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$,
kar je v nasprotju z osnovno predpostavko, da polravnine $\alpha_1$,
$\alpha_2$, $\cdots$, $\alpha_n$ prekrivajo ravnino $\alpha$.
 Torej  obstaja vsaj ena trojica izmed
polravnin $\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$, ki
prekrivajo ravnino $\alpha$.
 \kdokaz



        \bzgled \label{lemaJung}
        If for every three of $n$ ($n > 3$) points of a plane
        there is such a circle with radius $r$ containing these three points, then it exists
        a circle of equal radius containing all these $n$ points.
        \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.11.2.pic}
\caption{} \label{sl.skl.3.11.2.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.11.2.pic})

 Naj bodo $A_1$, $A_2$,$\ldots$, $A_n$ točke z danimi lastnostmi. S
$\mathcal{K}_i$ ($i\in\{1,2,\ldots,n\}$) označimo kroge s središči $A_i$ in s
polmerom $r$. Naj bodo $A_p$, $A_q$ in $A_l$ poljubne točke iz
množice $\{A_1, A_2,\ldots, A_n\}$. Po predpostavki obstaja krog s
polmerom $r$, ki te tri točke vsebuje. Označimo središče tega kroga
z $O$. Iz tega sledi $|OA_p|, |OA_q|, |OA_l|\leq r$, kar pomeni, da
točka $O$ leži v vsakem od krogov $\mathcal{K}_p$, $\mathcal{K}_q$ in $\mathcal{K}_l$. Torej,
vsaki trije izmed krogov $\mathcal{K}_1$, $\mathcal{K}_2$,$\ldots$, $\mathcal{K}_n$ imajo vsaj eno
skupno točko. Ker so krogi konveksni liki (izrek \ref{KrogKonv}), po
Hellyjevem izreku obstaja točka $S$, ki leži v vsakem izmed krogov
$\mathcal{K}_1$, $\mathcal{K}_2$,$\ldots$, $\mathcal{K}_n$. Iz tega sledi, da je $\mathcal{K}(S, r)$ iskani
krog, saj velja $|SA_1|, |SA_2|,\ldots |SA_n|\leq r$.
 \kdokaz

 Zanimiva posledica zadnje trditve \ref{lemaJung} bo podana v razdelku
 \ref{odd7Pitagora} (izrek \ref{Jung}).

%________________________________________________________________________________
\naloge{Exercises}

\begin{enumerate}

 \item Naj bo $S$ točka, ki leži v kotu $pOq$, točki $A$ in $B$ pa
 pravokotni projekciji  točke $S$ na krakih $p$ in $q$ tega
kota. Dokaži, da je $SA\cong SB$ natanko tedaj, ko je premica
$OS$ simetrala kota $pOq$.

\item Dokaži, da je vsota diagonal konveksnega štirikotnika večja od
vsote dveh njegovih nasprotnih stranic.

  \item Dokaži, da je v vsakemu trikotniku
  največ ena stranica krajša od pripadajoče višine.

  \item Naj bo $AA_1$ težiščnica trikotnika $ABC$. Dokaži,
   da je od dveh kotov, ki jih težiščnica $AA_1$ določa s
stranicama $AB$ in $AC$, večji tisti, ki ga težiščnica določa s
krajšo stranico.

  \item Naj  bosta $BB_1$ in $CC_1$ težiščnici trikotnika $ABC$ ter
  $AB<AC$.
  Dokaži, da je $BB_1<CC_1$.

  \item Naj bodo $a$, $b$ in $c$ stranice, $t_a$, $t_b$ in $t_c$
   ustrezne težiščnice ter $s$ polobseg poljubnega trikotnika.
Dokaži, da velja:
 \begin{enumerate}
  \item $s <  t_a  + t_b +  t_c  < 2s$;
  \item $t_a + t_b + t_c  >  \frac{3}{4}(a + b + c)$.
 \end{enumerate}

\item Naj bo premica $p$ mimobežnica krožnice $k$. Dokaži, da so
vse točke te krožnice na istem bregu premice $p$.

\item Če krožnica $k$ leži v nekem konveksnem liku $\Phi$, potem tudi
krog, ki je določen s to krožnico, leži v tem liku. Dokaži.

\item Naj bosta $p$ in $q$ različni tangenti krožnice $k$, ki se jo dotikata v
točkah $P$ in $Q$. Dokaži ekvivalenco: $p \parallel q$ natanko
tedaj, ko je $AB$ premer krožnice $k$.

\item Če je $AB$ tetiva krožnice $k$, potem je presek premice $AB$ in
kroga, ki ga krožnica $k$ določa, enak tej tetivi. Dokaži.

\item Naj bo $S'$ pravokotna projekcija središča $S$ krožnice $k$ na
premici $p$. Dokaži, da je $S'$ zunanja točka te krožnice
natanko tedaj, ko premica $p$ krožnice ne seka.

\item Naj bo $V$ višinska točka trikotnika $ABC$, pri katerem velja
$CV \cong AB$. Določi velikost kota $ACB$.

\item Naj bo $CC'$ višina pravokotnega trikotnika $ABC$ ($\angle ACB =
90^0$). Če sta $O$ in $S$ središči včrtanih krožnic trikotnikov
$ACC'$ in $BCC'$, je simetrala notranjega kota $ACB$
pravokotna na premici $OS$. Dokaži.

\item Naj bo $ABC$ trikotnik, v katerem je $\angle ABC = 15^0$ in
$\angle ACB = 30^0$. Naj bo $D$ takšna točka stranice $BC$, da je
 $\angle BAD=90^0$. Dokaži, da je $BD = 2AC$.

\item Dokaži, da obstaja takšen petkotnik, da je mogoče prekriti ravnino
 s takšnimi petkotniki, ki so mu skladni.

\item Dokaži, da obstaja takšen desetkotnik, da je mogoče prekriti ravnino
 s takšnimi desetkotniki, ki so mu skladni.

\item V neki ravnini je vsaka točka pobarvana rdeče ali črno.
        Dokaži, da obstaja pravilni trikotnik, ki ima vsa
        oglišča iste barve.

\item Naj bodo $l_1,l_2,\ldots, l_n$ ($n > 3$) loki, ki vsi ležijo na isti
krožnici. Središčni kot vsakega loka je kvečjemu enak $180^0$.
 Dokaži, da obstaja točka, ki leži na vsakem  loku,
 če imajo vsaki trije loki vsaj eno skupno točko.

%drugi del

\item
Naj bosta $p$ in $q$ pravokotnici, ki  se sekata v točki $A$. Če
je $B, B'\in p$, $C, C'\in q$, $AB\cong AC'$, $AB'\cong AC$,
$\mathcal{B}(B,A,B')$ in $\mathcal{B}(C,A,C')$, potem
pravokotnica na premico $BC$ skozi točko $A$ poteka skozi središče
daljice $B'C'$. Dokaži.

\item
Dokaži, da se simetrale notranjih kotov pravokotnika, ki ni
kvadrat, sekajo v točkah, ki so oglišča kvadrata.

\item
 Dokaži, da se simetrale notranjih kotov paralelograma, ki ni
romb, sekajo v točkah, ki so oglišča pravokotnika. Dokaži še, da so diagonale
tega pravokotnika vzporedne s stranicami paralelograma in so
enake razliki sosednjih stranic tega paralelograma.

\item
Dokaži, da sta simetrali dveh sokotov med seboj pravokotni.

\item Naj bosta $B'$ in $C'$ nožišči višin iz oglišč $B$ in $C$ trikotnika
$ABC$. Dokaži ekvivalenco $AB\cong AC \Leftrightarrow BB'\cong
CC'$.

\item Dokaži, da je trikotnik pravilen,
če središče trikotniku očrtane krožnice in njegova višinska točka sovpadata.
Ali podobna trditev velja za poljubni dve značilni
točki tega trikotnika?

\item Dokaži, da sta ostrokotna trikotnika $ABC$ in $A'B'C'$ skladna natanko
tedaj, ko imata skladni višini $CD$ in $C'D'$, stranici $AB$ in
$A'B'$ ter kota $ACD$ in $A'C'D'$.

\item Če je $ABCD$ pravokotnik ter $AQB$ in $APD$ pravilna
  trikotnika z enako orientacijo, je daljica $PQ$
skladna z diagonalo tega pravokotnika. Dokaži.

\item Naj bosta $BB'$ in $CC'$ višini trikotnika $ABC$ ($AC>AB$) ter
 $D$ takšna točka poltraka $AB$, da velja $AD\cong AC$. Točka
$E$ je presečišče premice $BB'$ s premico, ki poteka skozi točko $D$ in je
vzporedna s premico $AC$. Dokaži, da je $BE=CC'-BB'$.

\item Naj bo $ABCD$ konveksni štirikotnik, pri katerem velja
 $AB\cong BC\cong CD$ in $AC\perp BD$. Dokaži, da je $ABCD$
 romb.

\item Naj bo $BC$ osnovnica enakokrakega trikotnika $ABC$. Če sta $K$ in
$L$ takšni točki, da je $\mathcal{B}(A,K,B)$, $\mathcal{B}(A,C,L)$ in $KB\cong LC$, potem
središče daljice $KL$ leži na osnovnici $BC$. Dokaži.

\item Naj bo $S$ središče trikotniku $ABC$ včrtane krožnice.
Premica, ki poteka skozi točko $S$ in je vzporedna s stranico $BC$
tega trikotnika, seka stranici $AB$ in $AC$ po vrsti v točkah
$M$ in $N$. Dokaži, da je $BM+NC=NM$.

\item Naj bo $ABCDEFG$ konveksni sedemkotnik. Izračunaj vsoto
konveksnih kotov, ki jih določa lomljenka $ACEGBDFA$.

\item Dokaži, da so središča stranic in nožišče poljubne višine trikotnika,
v katerem nobeni dve stranici nista skladni, oglišča
enakokrakega trapeza.

 \item Naj bo $ABC$ pravokotni trikotnik s pravim kotom pri oglišču $C$.
Točki $E$ in $F$ naj bosta presečišči simetral notranjih kotov pri
ogliščih $A$ in $B$ z nasprotnima katetama,  $K$ in $L$ pa
pravokotni projekciji točk $E$ in $F$ na hipotenuzi tega
trikotnika. Dokaži, da je $\angle LCK=45^0$.


\item Naj bo $M$ središče stranice $CD$ kvadrata $ABCD$ in $P$ takšna točka
 diagonale $AC$, da velja $3AP=PC$. Dokaži, da je $\angle BPM$
pravi kot.

 \item Naj bodo $P$, $Q$ in $R$ središča stranic $AB$, $BC$ in $CD$
  paralelograma $ABCD$. Premici $DP$ in $BR$ naj sekata daljico
$AQ$ v točkah $K$ in $L$. Dokaži, da je $KL= \frac{2}{5} AQ$.

 \item  Naj bo $D$ središče hipotenuze $AB$ pravokotnega
trikotnika $ABC$ ($AC>BC$). Točki $E$ in $F$ naj bosta presečišči
poltrakov $CA$ in $CB$ s premico, ki poteka skozi $D$ in je pravokotna
na premico $CD$. Točka $M$ naj bo središče daljice $EF$. Dokaži, da
je $CM\perp AB$.

\item Naj bosta $A_1$ in $C_1$ središči stranic $BC$ in $AB$ trikotnika $ABC$.
 Simetrala notranjega kota pri oglišču $A$ seka daljico
$A_1C_1$ v točki $P$. Dokaži, da je $\angle APB$  pravi kot.

 \item Naj bosta $P$ in $Q$ takšni točki stranic $BC$ in $CD$ kvadrata $ABCD$,
  da je premica $PA$ simetrala kota $BPQ$. Določi velikost kota
  $PAQ$.

\item Dokaži, da  središče očrtane krožnice leži najbliže najdaljši stranici
trikotnika.

 \item Dokaži, da je središče včrtane krožnice najbliže oglišču, ki je vrh
največjega notranjega kota trikotnika.

\item Naj bo $ABCD$ konveksen štirikotnik. Določi točko $P$, tako da
bo vsota $AP+BP+CP+DP$ minimalna.

 \item Diagonali $AC$ in $BD$ enakokrakega trapeza $ABCD$ z osnovnico $AB$
se sekata v točki $O$ in velja $\angle AOB=60^0$. Točke $P$, $Q$
in $R$ so po vrsti središča daljic $OA$, $OD$ in $BC$. Dokaži, da
je $PQR$ pravilni trikotnik.

\item Naj bo $P$ poljubna notranja točka trikotnika $ABC$, za katero velja
 $\angle PBA\cong \angle PCA$. Točki $M$ in $L$ sta pravokotni
projekciji točke $P$ na stranicah $AB$ in $AC$, točka $N$ pa
središče stranice $BC$. Dokaži, da je $NM\cong
NL$\footnote{Predlog za MMO 1982 (SL 9.)).}.

\item Naj bodo $P$, $Q$ in $R$ središča stranic $BC$, $AC$ in $AB$
 trikotnika $ABC$ ($AB<AC$) in $D$ nožišče višine iz oglišča
$A$. Dokaži, da je $\angle DRP\cong \angle DQP=\angle ABC-\angle ACB$.

\item Naj bo $AD$ simetrala notranjega kota pri oglišču $A$ ($D\in BC$) trikotnika
$ABC$ in $E$ takšna točka stranice $AB$, da velja $\angle
BDE\cong\angle BAC$. Dokaži, da je $DE\cong DC$.

\item Naj bo $O$ središče kvadrata $ABCD$ ter $P$, $Q$ in $R$ točke,
 ki razdelijo njegov obseg na tri enake dele. Dokaži, da se
minimum vsote $|OP|+|OQ|+|OR|$ doseže, kadar je ena od teh točk
središče stranice kvadrata.

\item Dano je končno število premic, ki ravnino razdelijo na območja.
Dokaži, da lahko ravnino pobarvamo z dvema barvama, tako da je
vsako območje pobarvano z eno barvo, sosednji območji pa vedno z
različnima barvama.


\item Načrtaj trikotnik $ABC$, če so dani podatki (glej oznake v razdelku \ref{odd3Stirik}):

 (\textit{a}) $\alpha$, $\beta$, $s$; \hspace*{2mm}
 (\textit{b}) $a-b$, $c$, $\gamma$; \hspace*{2mm}
 (\textit{c}) $a$, $\beta-\gamma$, $b-c$; \hspace*{2mm}

 (\textit{d}) $a$, $\beta-\gamma$, $b+c$; \hspace*{2mm}
 (\textit{e}) $b$, $c$, $v_a$; \hspace*{2mm}
 (\textit{f}) $b$, $v_a$, $v_b$; \hspace*{2mm}

(\textit{g}) $\alpha$, $v_a$, $v_b$; \hspace*{2mm}
 (\textit{h}) $c$, $a+b$, $\gamma$;
 (\textit{i}) $v_a$, $\alpha$, $\beta$; \hspace*{2mm}

 (\textit{j}) $b$, $a+c$, $v_c$; \hspace*{2mm}
 (\textit{k}) $b-c$, $v_b$, $\alpha$; \hspace*{2mm}
 (\textit{l}) $a$, $t_b$, $t_c$;\hspace*{2mm}
 (\textit{m}) $b$, $c$, $t_a$; \hspace*{2mm}

 (\textit{n}) $t_a$, $t_b$, $t_c$; \hspace*{2mm}
(\textit{o}) $c$, $v_a$, $l_a$; \hspace*{2mm}
 (\textit{p}) $c$, $v_a$, $t_b$;
 (\textit{r}) $b$, $l_a$, $\alpha$; \hspace*{2mm}

 (\textit{s}) $v_a$, $v_b$, $t_a$; \hspace*{2mm}
(\textit{t}) $t_a$, $v_b$, $b+c$; \hspace*{2mm}
 (\textit{u}) $a$, $b$, $\alpha-\beta$;

 \item Načrtaj enakokraki trikotnik $ABC$, če so dani:
        \begin{enumerate}
        \item osnovnica ter vsota kraka in višine na osnovnico,
        \item obseg in višina na osnovnico,
        \item obe višini,
        \item kot ob osnovnici in odsek njegove simetrale,
        \item krak in na njem nožišče pripadajoče višine,
        \item krak in pripadajoča višina.
        \end{enumerate}

 \item Načrtaj pravokotni trikotnik $ABC$ s pravim kotom v oglišču $C$, če so dani naslednji podatki:

 (\textit{a}) $\alpha$, $a+b$, \hspace*{2mm}
 (\textit{b}) $\alpha$, $a-b$, \hspace*{2mm}
 (\textit{c}) $a$, $b+c$,

 (\textit{d}) $c$, $a+b$,\hspace*{2mm}
 (\textit{e}) $t_a$, $t_c$, \hspace*{2mm}
 (\textit{f}) $a$, $c-b$,

(\textit{g}) $a+v_c$, $\alpha$, \hspace*{2mm}
 (\textit{h}) $t_c$, $v_c$,\hspace*{2mm}
 (\textit{i}) $a$, $t_a$,\hspace*{2mm}
 (\textit{j}) $v_c$, $l_c$.

 \item Načrtaj pravokotnik $ABCD$, če je dano:
        \begin{enumerate}
        \item diagonala in ena stranica,
        \item diagonala in obseg,
        \item ena stranica in kot, ki ga oklepata diagonali,
        \item obseg in kot, ki ga oklepata diagonali.
        \end{enumerate}

 \item Načrtaj romb $ABCD$, če je dano:
        \begin{enumerate}
        \item stranica in vsota diagonal,
        \item stranica in razlika diagonal,
        \item en kot in vsota diagonal,
        \item en kot in razlika diagonal.
        \end{enumerate}

 \item Načrtaj paralelogram $ABCD$, če je dano:
        \begin{enumerate}
        \item ena stranica in diagonali,
        \item ena stranica in višini,
        \item ena diagonala in višini,
        \item stranica $AB$, kot ob oglišču $A$ in vsota $BC+AC$.
        \end{enumerate}

 \item Načrtaj trapez $ABCD$, če je dano:
        \begin{enumerate}
        \item osnovnici, krak in manjši kot, ki ne leži ob tem kraku,
        \item osnovnici in diagonali,
        \item osnovnici in kota ob daljši osnovnici,
        \item vsota osnovnic, višina in kota ob daljši osnovnici.
        \end{enumerate}

 \item Načrtaj deltoid $ABCD$, če so dani: diagonala $AC$, ki leži na somernici deltoida, $\angle CAD$ in vsota $AD+DC$.


 \item Načrtaj štirikotnik $ABCD$, če je dano:
        \begin{enumerate}
        \item štiri stranice in en kot,
        \item štiri stranice in kot, ki ga oklepata nosilki nasprotnih stranic,
        \item tri stranice in kota ob četrti stranici,
        \item središča treh stranic in daljica, ki je skladna in vzporedna s četrto stranico.
        \end{enumerate}


\end{enumerate}



%%% Do tu pregledala tudi Ana.

% DEL 4 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
% SKLADNOST TRIKOTNIKOV IN KROŽNICA
%________________________________________________________________________________

  \del{Congruence and Circle} \label{pogSKK}


Nekatere lastnosti krožnice smo obravnavali že v prejšnjih
dveh poglavjih – določene lastnosti polmera, premera, tetive, odnos
krožnice in premice ter lastnosti tangente na krožnico. Videli smo, da
za vsak trikotnik obstajata  očrtana in včrtana krožnica. Dokazali smo, da za pravilne večkotnike in
nekatere štirikotnike (pravokotnik, kvadrat)
obstaja očrtana krožnica, za nekatere pa tudi včrtana
krožnica. V tem poglavju se bomo poglobili v nadalnje lastnosti
krožnice, ki so posledice skladnosti trikotnikov.

%________________________________________________________________________________
 \poglavje{Two Circles} \label{odd4DveKroz}

 Analogno obravnavi medsebojne lege krožnice in premice,
 ki smo jo izvedli v razdelku \ref{odd3KrozPrem}, bomo v tem
 razdelku podobno naredili za dve krožnici v isti ravnini. V
 nadaljevanju bomo predpostavljali, da sta krožnici, ki ju
 obravnavamo, v isti ravnini.

 Definirajmo najprej nekaj pojmov, ki se nanašajo na dve krožnici.
 Premica, ki jo določata središči dveh krožnic, je
 \index{centrala dveh krožnic}\pojem{centrala} teh dveh krožnic.
 Razdaljo med središčema dveh krožnic imenujemo
 \index{središčna razdalja dveh krožnic}
  \pojem{središčna razdalja dveh krožnic}
 (Figure \ref{sl.skk.4.1.1.pic}).


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.1.pic}
\caption{} \label{sl.skk.4.1.1.pic}
\end{figure}


  Krožnici v isti ravnini z istim
  središčem (njuna središčna razdalja je enaka $0$)
  imenujemo
\index{krožnici!koncentrični}
 \pojem{koncentrični krožnici}
 (Figure \ref{sl.skk.4.1.1.pic}). Če imata koncentrični krožnici  vsaj
 eno skupno točko, sta krožnici identični (sovpadata). Če je $X$ skupna točka
 koncentričnih krožnic $k_1(S,r_1)$ in $k_2(S,r_2)$, velja
 $|SX|=r_1=r_2$ oz. velja $r_1=r_2$, kar pomeni, da sta krožnici
 identični. Koncentrični krožnici sta bodisi identični bodisi nimata
 skupnih točk. Podobno kot za krožnico in premico se tudi tu zastavlja
 vprašanje, koliko skupnih točk lahko imata različni krožnici in
 kakšna je njuna medsebojna lega. To raziskavo bomo začeli
 z naslednjim izrekom.


            \bizrek
            Two different circles lying in the same plane
            have at most two common points.
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.2.pic}
\caption{} \label{sl.skk.4.1.2.pic}
\end{figure}

\textbf{\textit{Proof.}} Predpostavimo nasprotno. Naj bodo $A$, $B$
in $C$ tri različne skupne točke dveh krožnic $k(O,r_1)$ in
$l(S,r_2)$ (Figure \ref{sl.skk.4.1.2.pic}). Te tri točke niso
kolinearne, kar bi pomenilo, da premica $AB$ seka krožnico (npr.
$k$) v treh različnih točkah, kar po izreku \ref{KroznPremPresek} ni
mogoče. Če pa so  $A$, $B$ in $C$ nekolinearne točke, določajo
trikotnik $ABC$, kar po izreku \ref{SredOcrtaneKrozn} pomeni, da je
$O=S$, oz. se obe točki nahajata v presečišču simetral stranic tega
trikotnika. Tudi polmera sta enaka, ker je $r_1=|OA|=|SA|=r_2$, zato
sta krožnici  $k(O,r_1)$ in $l(S,r_2)$ identični - obe predstavljata
trikotniku $ABC$ očrtano krožnico.
 \kdokaz

Torej lahko imata dve različni krožnici v isti ravnini dve
skupni točki, eno skupno točko ali pa nobene skupne točke. V prvem
primeru pravimo, da se \index{krožnici!se sekata} \pojem{krožnici
sekata}, v drugem se \index{krožnici!se dotikata} \pojem{krožnici
dotikata} v njunem \index{dotikališče!dveh krožnic}
\pojem{dotikališču}, v tretjem pa sta \index{krožnici!sta
mimobežni}\pojem{krožnici mimobežni} (Figure \ref{sl.skk.4.1.3.pic}).


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.3.pic}
\caption{} \label{sl.skk.4.1.3.pic}
\end{figure}


Če se  krožnici ne sekata, je notranjost vsaj ene od teh dveh
krožnic ali v notranjosti ali v zunanjosti druge krožnice. To je
posledica izreka \ref{DedPoslKrozKroz}.

Premica, ki je določena s presečiščema
 dveh krožnic, ki se
sekata, se imenuje \pojem{sekanta, ki je nosilka njune skupne
tetive}. V zvezi s tem dokažimo naslednji izrek.



            \bizrek \label{KroznPresABpravokOS}
            If two circles intersect at two points $A$ and $B$,
            then the line containing the centres of the two circles is perpendicular to the line $AB$.
             \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.4.pic}
\caption{} \label{sl.skk.4.1.4.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bosta $A$ in $B$ presečišči krožnic
$k_1(S_1,r_1)$ in  $k_2(S_2,r_2)$ (Figure \ref{sl.skk.4.1.4.pic}).
 Ker je $S_1A\cong S_1B\cong r_1$ in $S_2A\cong S_2B\cong r_2$,
 je premica $S_1S_2$  simetrala daljice $AB$ (izrek \ref{simetrala}),
 zato je $S_1S_2\perp
 AB$.
  \kdokaz


 Dokazali bomo, da imata krožnici, ki se dotikata, skupno tangento v
njunem dotikališču.



            \bizrek \label{tangSkupnaDotikKrozn}
            Let $k_1$ and $k_2$ be different circles with centres $S_1$ and
            $S_2$ touching at a point $T$. Then:

            (i) $S_1$, $S_2$ and $T$  are collinear points;

             (ii) the tangent of the circle $k_1$ at the point $T$ is at the same time the tangent of the circle $k_2$ at
            the same point.
            \eizrek



\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.5.pic}
\caption{} \label{sl.skk.4.1.5.pic}
\end{figure}

\textbf{\textit{Proof.}}  (Figure \ref{sl.skk.4.1.5.pic}).

(\textit{i}) Predpostavimo, da točke $S_1$, $S_2$ in $T$ niso
kolinearne. Premica $S_1S_2$ razdeli ravnino, v kateri ležita
krožnici, na dve polravnini. Tisto polravnino, ki vsebuje točko $T$,
označimo s $\pi_1$, drugo pa s $\pi_2$. Iz izreka \ref{izomEnaC'}
sledi, da v polravnini $\pi_2$ obstaja (ena sama) točka $T'$, za
katero je $S_1T'\cong S_1T$ in $S_2T'\cong ST_2$. To bi pomenilo,
da še točka $T'$, ki je različna od točke $T$, leži na krožnicah
$k_1$ in $k_2$, kar ni mogoče. Torej so točke $S_1$, $S_2$ in $T$
kolinearne.

 (\textit{ii}) Po izreku \ref{TangPogoj} je tangenta
krožnice $k_1$ v točki $T$ pravokotna na polmer $S_1T$. Podobno
je tangenta krožnice $k_2$ v isti točki $T$  pravokotna na polmer
$S_2T$. Ker iz (\textit{i}) premici $S_1T$ in $S_2T$ sovpadata,
sta tudi obe pravokotnici oz. tangenti identičnii.
 \kdokaz

Po izreku \ref{tangKrozEnaStr} so vse točke krožnice na isti strani
vsake njene tangente – na tisti strani, kjer je njeno središče. To
pomeni, da sta krožnici $k_1$ in $k_2$ iz prejšnjega izreka bodisi
 na isti strani bodisi na različnih straneh njune skupne tangente.
 Kadar je $B(S_1,T,S_2)$, sta krožnici na različnih straneh
njune skupne tangente  in pravimo, da se krožnici $k_1$
in $k_2$ \pojem{dotikata od zunaj}. Sicer sta krožnici na isti strani
te tangente in pravimo, da se  \pojem{dotikata od znotraj}. V
prvem primeru je notranjost ene od teh dveh krožnic v zunanjosti, v
drugem  pa v notranjosti druge krožnice (Figure
\ref{sl.skk.4.1.6.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.6.pic}
\caption{} \label{sl.skk.4.1.6.pic}
\end{figure}

Ko se  krožnici $k_1(S_1,r_1)$ in $k_2(S_2,r_2)$ dotikata zunaj,
iz prejšnjega izreka sledi, da je $|S_1S_2| = r_1 + r_2$.
Če se krožnici dotikata od znotraj, je $|S_1S_2| = |r_1 - r_2|$.
Jasno je, da velja tudi obratno. Pogoja $|S_1S_2| = r_1 +
r_2$ oz. $|S_1S_2| = |r_1 - r_2|$ sta zadostna, da se krožnici
dotikata od zunaj oz. od znotraj. Na podoben način dobimo tudi ostale
kriterije za medsebojno lego dveh krožnic.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.7.pic}
\caption{} \label{sl.skk.4.1.7.pic}
\end{figure}

            \bizrek
            Let $k_1(S_1,r_1)$
            and $k_2(S_2,r_2)$ ($r_1\geq r_2$) be two circles. Then
            (Figure \ref{sl.skk.4.1.7.pic}):

            (i) the circles $k_1(S_1,r_1)$
            and $k_2(S_2,r_2)$ are lying outside each other
             if and only if $|S_1S_2|>r_1+r_2$;

             (ii) the circles $k_1(S_1,r_1)$
            and $k_2(S_2,r_2)$ are touching each other externally
            if and only if $|S_1S_2|=r_1+r_2$;

             (iii) the circles $k_1(S_1,r_1)$
            and $k_2(S_2,r_2)$ are intersecting each other at two points
            if and only if $r_1-r_2<|S_1S_2|<r_1+r_2$;

            (iv) the circles $k_1(S_1,r_1)$
            and $k_2(S_2,r_2)$ are touching each other internally
             if and only if $|S_1S_2|=r_1-r_2$;

            (v) one of the circles $k_1(S_1,r_1)$
            and $k_2(S_2,r_2)$ is lying inside another
             if and only if $|S_1S_2|<r_1-r_2$.
            \eizrek


Sedaj bomo definirali še nekaj pojmov, ki se nanašata na dve
krožnici.

\pojem{Kot med krožnicama}, ki se sekata, je kot, ki ga določata
tangenti teh dveh krožnic v njuni skupni točki. Ni težko dokazati,
da ta kot ni odvisen od izbire skupne točke, oz. da sta kota med
tangentama v vsaki od dveh skupnih točk skladna (Figure
\ref{sl.skk.4.1.8.pic}).

Ko se krožnici dotikata, pravimo, da določata kot $0^0$.


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.8.pic}
\caption{} \label{sl.skk.4.1.8.pic}
\end{figure}

Krožnici sta \index{pravokotni!krožnici} \pojem{pravokotni}, če
določata kot $90^0$, oz. če sta njuni tangenti v skupni točki
pravokotni (Figure \ref{sl.skk.4.1.8.pic}).

Direktna posledica izreka \ref{TangPogoj} je naslednji pogoj
pravokotnosti dveh krožnic.



            \bizrek \label{pravokotniKroznici}
            Two circles are perpendicular if and only if
            the tangent of one of the circles at the points of intersection
            contains the centre of  another circle.
             \eizrek

V zgledu \ref{tangKrozKonstr} smo ugotovili, kako lahko narišemo
tangenti krožnice iz njene poljubne zunanje točke. V izreku
\ref{tangSkupnaDotikKrozn} pa smo  dokazali, da imata krožnici, ki se
dotikata,  vsaj eno skupno tangento. V naslednjem zgledu bomo
konstruirali \index{skupna tangenta}\pojem{skupne tangente} dveh
krožnic v splošni legi.

            \bzgled \label{tang2ehkroz}
            Construct a common tangent of two given circles
            lying in the same plane.
            \ezgled

\textbf{\textit{Solution.}} Naj bosta $k_1(S_1,r_1)$ in
$k_2(S_2,r_2)$ ($r_1\geq r_2$) poljubni krožnici v isti ravnini ter
$t$ njuna skupna tangenta, ki se krožnic $k_1$ in $k_2$
dotika po vrsti v točkah $T_1$ in $T_2$.

Obravnavali bomo dva primera:

\textit{1)} Predpostavimo najprej, da sta točki $T_1$ in $T_2$ na
istem bregu centrale $S_1S_2$
 (Figure \ref{sl.skk.4.1.9.pic}). Označimo $S'_2=pr_{\perp
S_1T_1}(S_2)$. Po izreku \ref{TangPogoj} je $\angle
S_1T_1T_2\cong\angle S_2T_2T_1=90^0$. To pomeni, da je štirikotnik
$S_2T_2T_1S'_2$ pravokotnik, zato je tudi $\angle S_2S'_2T_1=90^0$
in $|S'_2T_1|=|S_2T_2|=r_2$.
 Ker je po predpostavki $r_1\geq r_2$ in $|S_1T_1|=r_1$, je
 $|S_1S'_2|=r_1-r_2$. Označimo s $k$ krožnico s središčem $S_1$ in
 polmerom $r_1-r_2$. Krožnica $k$ poteka skozi točko $S'_2$.
 Če je $S_2$ zunanja točka krožnice $k$,
 iz $\angle S_2S'_2T_1=90^0$
 sledi, da je premica $S_2S_2'$ tangenta
 te krožnice.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.9.pic}
\caption{} \label{sl.skk.4.1.9.pic}
\end{figure}

 Prejšnja analiza nam omogoča konstrukcijo. Najprej načrtamo
 krožnico $k(S_1,r_1-r_2)$, nato pa njeno tangento $S_1S'_2$ v
 dotikališču $S'_2$ (zgled \ref{tangKrozKonstr}), točko $T_1$ kot
 presečišče poltraka $S'_2T_1$ in krožnice $k_1$, četrto oglišče
 $T_2$ pravokotnika $T_1S'_2S_2T_2$ (ker je že iz konstrukcije
 $\angle S_2S'_2T_1=90^0$) in na koncu skupno tangento $t=T_1T_2$.


 Dokažimo, da je $t$ res skupna tangenta. Ker je že po
 konstrukciji $T_1\in k_1$ in $\angle S_1T_1T_2\cong
 \angle S_2T_2T_1=90^0$, je dovolj dokazati, da velja $T_2\in
 k_2$. To pa sledi iz dejstva, da je štirikotnik $T_1S'_2S_2T_2$
 pravokotnik oz. $|S_2T_2|=|S'_2T_1|=r_1-(r_1-r_2)=r_2$.

Razen načrtane tangente $t$ dobimo še tangento $t_1$,
ki je simetrična tangenti $t$ glede na centralo $S_1S_2$. Za
tangenti $t$ in $t_1$ pravimo, da sta \index{skupna
tangenta!zunanja}\pojem{zunanji tangenti}.

\textit{2)} Če predpostavimo, da sta $T_1$ in $T_2$ na različnih
bregovih centrale $S_1S_2$, dobimo v določenih primerih  še dve t. i. \index{skupna tangenta!notranja}\pojem{notranji tangenti} po
enakem postopku, le da krožnico $k(S_1,r_1-r_2)$ zamenjamo s krožnico
$k'(S_1, r_1+r_2)$.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.10.pic}
\caption{} \label{sl.skk.4.1.10.pic}
\end{figure}

Obravnavajmo še število rešitev naloge (Figure
\ref{sl.skk.4.1.10.pic}). Kadar sta krožnici mimobežni in
nobena ni v notranjosti druge, imata krožnici vse štiri opisane
skupne tangente - dve zunanji in dve notranji tangenti. Če
se krožnici dotikata od zunaj, ima naloga tri rešitvi, ker se notranji
tangenti prekrivata in dobimo skupno tangento, ki je omenjena v
izreku \ref{tangSkupnaDotikKrozn}. Ko se krožnici sekata,
imamo le dve rešitvi - dve zunanji tangenti. Kadar se krožnici dotikata od
znotraj, obstaja le ena skupna tangenta (tista iz izreka
\ref{tangSkupnaDotikKrozn}). In na koncu, če sta krožnici mimobežni
in je ena v notranjosti druge, nimata
skupnih tangent.
\kdokaz



            \bzgled
            Let $A$, $B$, $C$ and $D$ be points in the plane such that do not all lie
            on the same circle nor all on the same line. Prove that there are two such circles
            $k$ and $l$, which have no common points, the first of them passes
            through the points $A$ and $B$, and the other one
             through the points $C$ and $D$.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.1a.pic}
\caption{} \label{sl.skk.4.1.1a.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bosta
$m$ in $n$ simetrali daljic $AB$ in $CD$. Obravnavali bomo dva
primera (Figure \ref{sl.skk.4.1.1a.pic}):

 \textit{1)}
Če se premici $m$ in $n$ sekata v točki $O$, sta iskani krožnici
$k(O,OA)$ in $l(O,OC)$, ker sta koncentrični in po predpostavki
različni.

\textit{2)} Če sta premici $m$ in $n$ vzporedni, sta vzporedni tudi
premici $AB$ in $CD$ (in po predpostavki različni). S $p$ označimo
poljubno vzporednico premic $AB$ in $CD$, tako da bosta $AB$ in $CD$
na različnih straneh premice $p$. Naj bosta $M$ in $N$ presečišči
premic $m$ in $n$ s premico $p$. Če je $M \neq N$, sta iskani
krožnici očrtani krožnici trikotnikov $ABM$ in $CDN$ (izrek
\ref{SredOcrtaneKrozn}), ker ležita na različnih bregovih premice
$p$. Če je $M = N$ oz. $m = n$, sta iskani krožnici spet
koncentrični $k(M,MA)$ in $l(M,MC)$.
 \kdokaz



%________________________________________________________________________________
 \poglavje{Center Angle and Circumferential Angle} \label{odd4SredObod}


 Definirajmo najprej pojma središčni in obodni kot
  (Figure \ref{sl.skk.4.2.1a.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.1a.pic}
\caption{} \label{sl.skk.4.2.1a.pic}
\end{figure}

 \pojem{Središčni kot}
  \index{kot!središčni}  krožnice $k(S,r)$ je poljuben kot,
  ki leži v ravnini te krožnice  in ima vrh v točki $S$.
   \pojem{Obodni kot}
  \index{kot!obodni} te krožnice je poljuben kot z vrhom
  na krožnici $k$, njegova kraka pa vsebujeta dve tetivi te
krožnice. Presek krožnice in njegovega središčnega oz. obodnega kota
je lok, ki ga imenujemo \pojem{pripadajoči lok} tega kota. V tem
primeru za središčni oz. obodni kot pravimo, da je kot \pojem{nad tem lokom}.
 Vemo, da poljubna tetiva $PQ$ na krožnici $k(S,r)$ določa dva loka.
 Če bomo vedeli, za kateri
od obeh lokov gre, bomo včasih za kot nad pripadajočim lokom $PQ$
rekli, da je kot \pojem{nad tetivo} $PQ$.

V posebnem primeru, ko je tetiva premer, je pripadajoč središčni kot
nad to tetivo  enak $180^0$. Talesov izrek za krožnico (izrek
\ref{TalesovIzrKroz}) lahko v terminih obodnih kotov zapišemo v
naslednji obliki:



             \bizrek \label{TalesovIzrKroz2oblika}
            All inscribed angles subtending a diameter of a circle are right angles.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.2a.pic}
\caption{} \label{sl.skk.4.2.2a.pic}
\end{figure}

Torej je središčni kot nad premerom dvakrat večji od
obodnega kota nad tem premerom (Figure \ref{sl.skk.4.2.2a.pic}).
Dokazali bomo, da ta trditev velja tudi  za obodni in središčni kot nad
poljubno tetivo.


\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.3.pic}
\caption{} \label{sl.skk.4.2.3.pic}
\end{figure}



         \bizrek
            \label{SredObodKot}
            In any circle, a central angle is twice of the measure
            of the circumferential angle subtending the
            same arc\footnote{Predpostavlja se, da je to trditev prvi dokazal
           \index{Tales}\textit{Tales} iz Mileta (7.--6. stol. pr. n. š.).} (Figure \ref{sl.skk.4.2.3.pic}).
          \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.4.pic}
\caption{} \label{sl.skk.4.2.4.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $PQ=l$  lok krožnice $k(S, r)$ in
$V$ poljubna točka te krožnice, ki ne leži na tem loku. Dokazali
bomo, da za središčni kot $PSQ$ in obodni kot $PVQ$ velja:
$$\angle PSQ = 2\angle PVQ.$$ Obravnavali bomo tri različne možnosti
(Figure \ref{sl.skk.4.2.4.pic}):

\textit{1)} Središče $S$ krožnice $k$ leži na enem od krakov
obodnega kota $PVQ$. Brez škode za splošnost naj bo to krak $VQ$. V
tem primeru je $PSV$ enakokraki trikotnik ($SP \cong SV = r$), zato
je $\angle SPV \cong \angle PVS$ (izrek \ref{enakokraki}). V
trikotniku $PSQ$ je zunanji kot $PSQ$ enak vsoti nesosednjih
notranjih kotov (izrek \ref{zunanjiNotrNotr}). Torej:
 $$ \angle PSQ =
\angle SPV + \angle PVS = 2\angle PVS\\ = 2\angle PVQ.$$

\textit{2)} Središče $S$ krožnice $k$ leži v notranjosti obodnega
kota $PVQ$. V tem primeru drugo presečišče krožnice $k$ s premico
$VS$ – točka $V'$ – leži na loku $l$, ker le-ta predstavlja presek
obodnega kota  $PVQ$ in krožnice $k$. Če dvakrat uporabimo dokazano
dejstvo iz \textit{1)}, dobimo:
  \begin{eqnarray*}
\angle PSQ &=& \angle PSV'+\angle V'SQ =
2\angle PVV'+2\angle V'VQ=\\ &=& 2(\angle PVV'+\angle V'VQ) = 2\angle PVQ.
  \end{eqnarray*}
\textit{3)} Središče $S$ krožnice $k$ je zunanja točka obodnega
kota. Na enak način kot v \textit{2)} definirajmo točko $V'$. V tem
primeru točka $V'$ ne leži na loku $l$. Brez škode za splošnost
predpostavimo, da je $P$ notranja točka obodnega kota $\angle V'VQ$.
Spet uporabimo rezultat iz \textit{1)}:
  \begin{eqnarray*}
  \angle PSQ &=& \angle V'SQ
-\angle V'SP = 2\angle V'VQ - 2\angle V'VP=\\ &=& 2(\angle V'VQ -\angle
V'VP) = 2\angle PVQ,
  \end{eqnarray*}
 kar je bilo potrebno dokazati.  \kdokaz

Najpomembnejši sta naslednji posledici prejšnjega izreka.



        \bizrek
        \label{ObodObodKot}
        In a circle, different circumferential angles
        subtending the same arc are congruent.
        \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.5.pic}
\caption{} \label{sl.skk.4.2.5.pic}
\end{figure}

\textbf{\textit{Proof.}} Iz prejšnjega izreka \ref{SredObodKot}
sledi, da so vsi obodni koti nad istim lokom enaki polovici
 središčnega kota nad tem lokom (Figure \ref{sl.skk.4.2.5.pic}).
  Zaradi tega so vsi
omenjeni obodni koti med seboj skladni.
 \kdokaz



        \bizrek
        \label{ObodObodKotNaspr}
        Two circumferential angles
        subtending the same chord of a circle, with the vertices lying
        on different sides of the line containing this chord,
        are supplementary.
        \eizrek


\textbf{\textit{Proof.}} Tetiva krožnice določa na njej dva loka, ki
se dopolnjujeta do cele krožnice (Figure \ref{sl.skk.4.2.5.pic}).
Vsak od obeh omenjenih obodih kotov ustreza enemu od teh dveh
lokov, kar pomeni, da je vsota ustreznih središčnih kotov enaka
$360^0$. Ker je vsota obodnih kotov po izreku \ref{SredObodKot}
enaka polovici vsote ustreznih središčnih kotov, sta obodna kota
suplementarna.
 \kdokaz

Kot smo že omenili, bomo pogosto govorili o obodnih in središčnih
kotih nad isto tetivo, če le vemo, za katerega od obeh pripadajočihih lokov te
tetive gre. V tem smislu formulirajmo naslednji trditvi.



        \bizrek
          \label{SklTetSklObKot}
          Two circumferential angles
        subtending the congruent chords of a circle
        are congruent.
         \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.4a.pic}
\caption{} \label{sl.skk.4.2.4a.pic}
\end{figure}

\textbf{\textit{Proof.}}  Po izreku \textit{SSS} \ref{SSS} skladnima
tetivama ustrezata skladna središčna kota (Figure
\ref{sl.skk.4.2.4a.pic}). Trditev je potem direktna posledica izreka
\ref{SredObodKot}.  \kdokaz

Jasno je, da velja tudi naslednja trditev  (Figure
\ref{sl.skk.4.2.4b.pic}).


            \bizrek
          \label{SklTetSklObKot2}
          Two circumferential angles
        subtending the congruent chords of congruent circles
        are congruent.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.4b.pic}
\caption{} \label{sl.skk.4.2.4b.pic}
\end{figure}

Zelo zanimiva in uporabna je tudi naslednja posledica.



         \bizrek
          \label{ObodKotTang}
          The angle determined by a chord of a circle and the tangent of that circle
            in one of the endpoints of this chord is congruent to the circumferential
            angle subtending this chord.
         \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.6.pic}
\caption{} \label{sl.skk.4.2.6.pic}
\end{figure}

\textbf{\textit{Proof.}}  Naj bo $PAQ$ obodni kot neke krožnice nad
tetivo $PQ$, $LP$ takšna tangenta te krožnice v točki $P$, da sta
točki $L$ in $A$ na različnih straneh premice $PQ$, in $PB$ premer te
krožnice (Figure \ref{sl.skk.4.2.6.pic}). Ker je $BP \perp PL$ (izrek
\ref{TangPogoj}) in $BQ \perp PQ$ (Talesov izrek
\ref{TalesovIzrKroz}), sta  kota $LPQ$ in $PBQ$ skladna (izrek
\ref{KotaPravokKraki}). Toda po izreku \ref{ObodObodKot} sta
 kota $PAQ$ in $PBQ$ skladna, zato je tudi $\angle LPQ \cong PAQ$.
 \kdokaz

Prejšnji rezultat omogoča realizacijo ene zelo pomembne konstrukcije
-- načrtovanje geometrijskega mesta točk v ravnini, iz katerih se
dana daljica ‘‘vidi’’ pod danim kotom. Pravzaprav gre za
naslednji problem.

%angle of view of a line segment!!!


        \bizrek
          \label{ObodKotGMT}
          Let $A$ and $B$ be two different points and $\omega$ a given angle.
        The set of all points $X$ in the plane from which the angle of view of the line segment $AB$ is
        $\omega$, i.e. $\angle AXB\cong \omega$, is the union of two open circular arcs, which are
        symmetric with respect to the line $AB$.
        \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.7.pic}
\caption{} \label{sl.skk.4.2.7.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $p$ poltrak z izhodiščem $A$, tako da
je $\angle p,BA \cong \omega$, premica $n$ pravokotnica tega
poltraka v točki $A$ in $s$ simetrala daljice $AB$ (Figure
\ref{sl.skk.4.2.7.pic}). Presečišče premic $n$ in $s$ označimo s
$S$, krožnico s središčem $S$ in polmerom $SA$ pa s $k$. Z $l$
označimo lok, ki je presek krožnice $k$ in polravnine z robom $AB$,
v kateri ne leži poltrak $p$. V dopolnilni polravnini na podoben
način določimo lok $l'$, ki je skladen z lokom $l$. Dokažimo, da je
iskano geometrijsko mesto točk množica $l \cup l'\setminus\{A,B\}$.

Dejstvo, da se iz vsake točke loka $l$ (oz. $l'$), ki je različna od
točk $A$ in $B$, daljica $AB$ vidi pod kotom $\omega$, sledi iz
izrekov \ref{TangPogoj} in \ref{ObodKotTang}. Za poljubno točko
$P$ odprtega loka $l$ velja: $\angle APB \cong \angle p,AB \cong
\omega$.

Predpostavimo, da točka $M$ ne pripada množici $l \cup
l'\setminus\{A,B\}$. V primeru, kadar je $M$ ena od točk $A$ ali
$B$, kot $AMB$ sploh ne obstaja. Naj bo $M \neq A,B$ in brez škode
za splošnost točka $M$ v isti polravnini kot lok $l$.
Označimo z $N$ drugo presečišče poltraka $AM$ in loka $l$ ($N\neq A$).
Če je $\mathcal{B}(A,M,N)$, je v trikotniku $NMB$ zunanji kot $AMB$
večji od nesosednjega notranjega kota $MNB$ (izrek
\ref{zunanjiNotrNotrVecji}), ki je po že dokazanem enak $\omega$,
zato je $\angle AMB>\omega$. Če pa velja $\mathcal{B}(A,N,M)$, lahko s
podobnim sklepanjem  ugotovimo, da je v tem primeru $\angle
AMB<\omega$, kar pomeni, da za nobeno točko $M\notin l \cup
l'\setminus\{A,B\}$ ne velja $\angle AMB \cong \omega$.
 \kdokaz

Iz dokaza prejšnjega izreka dobimo tudi naslednjo ugotovitev.


            \bizrek \label{obodKotGMTZunNotr}
             Let $AB$ be an arc of a circle $k$, $\omega$ the corresponding circumferential angle
          of this arc and $M$ a point of the half-plane with the edge $AB$ not containing this arc (Figure
            \ref{sl.skk.4.2.8.pic}). Then:

             (i) $\angle AMB >\omega$ if and only if the point $M$ is an interior point of the circle $k$;

             (ii) $\angle AMB \cong\omega$ if and only if the point $M$ lies on the circle $k$;

             (iii) $\angle AMB <\omega$ if and only if the point $M$ is an exterior point of the circle $k$.
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.8.pic}
\caption{} \label{sl.skk.4.2.8.pic}
\end{figure}

V naslednjih primerih bomo videli uporabo izreka o obodnem in
središčnem kotu in njegovih posledic.



         \bzgled
         Construct a triangle with given $a$, $\alpha$, $v_a$. \label{konstr_aalphava}
         \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1d.pic}
\caption{} \label{sl.skk.4.3.1d.pic}
\end{figure}

   \textbf{\textit{Analysis.}} Točka $A$ leži hkrati na geometrijskem mestu
točk, iz katerih se daljica $BC$ vidi pod kotom $\alpha$ (unija dveh krožnih lokov - izrek \ref{ObodKotGMT}) in vzporednici premice $BC$, ki je od nje
oddaljena $v_a$ (Figure \ref{sl.skk.4.3.1d.pic}). Torej je oglišče $A$ presečišče te
vzporednice in omenjenega geometrijskega mesta točk.

\textbf{\textit{Construction.}} Načrtajmo najprej daljico
$BC\cong a$, nato pa geometrijsko mesto točk $\mathcal{L}$, iz
katerih se ta daljica vidi pod kotom $\alpha$ (izrek \ref{ObodKotGMT}).
Nato načrtajmo  vzporednico $p$ premice $BC$ na razdalji $v_a$. Z $A$ označimo presečišče premice $p$
in omenjenega geometrijskega mesta točk $\mathcal{L}$. Dokažimo, da je $ABC$ iskani trikotnik.

\textbf{\textit{Proof.}} Že po konstrukciji je jasno, da je $BC\cong a$. Po konstrukciji točka $A$ leži na
geometrijskem mestu točk, iz katerih se daljica $BC$ vidi pod kotom $\alpha$, zato je tudi $BAC\cong\alpha$. Višina
trikotnika $ABC$ iz oglišča $A$ je skladna daljici $v_a$, ker točka $A$ po konstrukciji leži na premici $p$, ki je na
razdalji $v_a$ vzporedna premici $BC$.

\textbf{\textit{Discussion.}} Nujni pogoj je seveda $\alpha<180^0$. Število rešitev naloge je enako številu presečišč
premice $p$ in množice $\mathcal{L}$.
 \kdokaz



            \bzgled
           Let $p$, $q$ and $r$ be lines in the plane intersecting
            at one point and divide this plane into six congruent angles. Suppose that $P$, $Q$ and $R$
            are the foots of the perpendiculars from an arbitrary point $X$ of this plane on the lines $p$, $q$ and
            $r$, respectively. Prove that $PQR$ is a regular triangle.
            \ezgled



\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.9.pic}
\caption{} \label{sl.skk.4.2.9.pic}
\end{figure}

\textbf{\textit{Proof.}}  (Figure \ref{sl.skk.4.2.9.pic}).
 Naj bo $S$
presečišče premic $p$, $q$ in $r$. Jasno je, da premice določajo
kote $60^0$. Ker je $\angle XPS \cong \angle XQS \cong \angle XRS =
90^0$, po izreku \ref{TalesovIzrKroz2} točke $S$, $X$, $P$, $Q$ in
$R$ ležijo na krožnici $k$ s premerom $SX$.
 Če uporabimo izrek \ref{ObodObodKot} za ustrezne loke $PQ$ in $QR$,
 je $\angle PRQ \cong \angle PSQ =
60^0$ in $\angle QPR \cong \angle QSR = 60^0$. Ker ima vse kote
enake $60^0$, je torej $PQR$ pravilni trikotnik.
 \kdokaz


            \bzgled
            Let $k(O,R)$ and $l(S,r)$ ($R = 2r$) be circles touching each other internally
            and $P$ an arbitrary point on the circle $l$. Which curve
            is described by the point $P$ if the circle $l$ rolls without slipping around the circle $k$\footnote{Ta problem je rešil poljski astronom
             \index{Copernicus, N.} \textit{N. Copernicus} (1473--1543).
             V splošnem primeru, kadar ni nujno $R = 2r$, krivuljo, po
             kateri se giblje točka $P$, imenujemo \index{hipocikloida}
              \pojem{hipocikloida}. V primeru zunanjega kotaljenja krožnice
              po drugi krožnici, krivuljo imenujemo \index{epicikloida}
              \pojem{epicikloida}, v primeru
              kotaljenja krožnice po premici pa je to \index{cikloida}
              \pojem{cikloida}. Cikloido je prvi raziskoval nemški matematik in
              filozof \index{Kuzanski, N.} \textit{N. Kuzanski} (1401--1464)
              in kasneje francoski matematik in filozof \index{Mersenne, M.}
              \textit{M. Mersenne} (1588--1648). Poimenoval jo je italijanski fizik,
              matematik, astronom in filozof \index{Galilei, G.}
               \textit{G. Galilei} (1564--1642) leta 1599.}?
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.10.pic}
\caption{} \label{sl.skk.4.2.10.pic}
\end{figure}

\textbf{\textit{Solution.}}
 Naj bo
$P_0$ lega točke $P$ v trenutku, ko leži na krožnici $k$ (Figure
\ref{sl.skk.4.2.10.pic}). Takrat, ko je točka $P$ v legi $P_i$,
se krožnica $l$, ki je v legi $l_i$, dotika krožnice $k$ v neki
točki $T_i$. Ker gre za ‘‘gibanje brez spodrsavanja’’, sta dolžini
ustreznih lokov $P_0T_i$ in $P_iT_i$ krožnic $k$ in $l$ med seboj
enaki. Polmer krožnice $k$ je dvakrat večji od polmera krožnice $l$,
zato za pripadajoče središčne kote omenjenih lokov velja $\angle
T_iS_iP_i= 2\angle T_iOP_0$. Toda $\angle T_iOP_i$ je ustrezni
obodni kot krožnice $l$ za isti lok $P_iT_i$, zato je $2\angle
T_iOP_i = \angle T_iS_iP_i$ (izrek \ref{ObodObodKot}). Iz prejšnjih
dveh relacij dobimo $\angle T_iOP_i= \angle T_iOP_0$, kar pomeni,
da je točka $P_i$ kolinearna s točkama $O$ in $P_0$, zato iskani tir
točke $P$ predstavlja premer $P_0P'_0$  krožnice $k$.
 \kdokaz



            \bzgled
            Let $C$ be the midpoint of an arc $AB$ and $D$ an arbitrary point of this
            arc other than $C$. Prove that
                $$AC + BC > AD + BD.$$
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.11.pic}
\caption{} \label{sl.skk.4.2.11.pic}
\end{figure}

\textbf{\textit{Proof.}}
  (Figure
\ref{sl.skk.4.2.11.pic}).
 Naj bosta $C'$ in $D'$ takšni točki poltrakov $AC$ in $AD$,
 da velja: $CC'\cong CB \cong CA$, $DD'\cong DB$,
$\mathcal{B}(A,C,C')$ in $\mathcal{B}(A,D,D')$. Trikotnika $C'CB$ in
$D'DB$ sta enakokraka, zato po izrekih \ref{enakokraki} in \ref{zunanjiNotrNotr},
sledi:
 $$\angle CC'B \cong \angle CBC' = \frac{1}{2}\angle ACB
\hspace*{2mm}\textit{ in }\hspace*{2mm}
 \angle DD'B \cong \angle DBD'
= \frac{1}{2}\angle ADB.$$
 Ker sta kota $ACB$ in $ADB$ obodna kota nad tetivo $AB$, sta skladna
  (izrek \ref{ObodObodKot}).
Skladna sta tudi kota $AC'B$ in $AD'B$,  točki $C'$ in $D'$ pa
pripadata pripadajočemu loku $l'$ nad tetivo $AB$ (izrek
\ref{ObodKotGMT}). Ker je $CC'\cong CB \cong CA$, je daljica $AC'$
premer krožnice, ki vsebuje lok $l'$, zato je $\angle AD'C'$ pravi
kot (izrek \ref{TalesovIzrKroz2}). Daljica $AC'$ je torej
hipotenuza pravokotnega trikotnika $AD'C'$ in zato po izreku
\ref{vecstrveckot} velja:
$$AC + CB = AC'> AD'= AD + DB,$$ kar je bilo treba dokazati. \kdokaz



      \bnaloga\footnote{35. IMO Hong Kong - 1994, Problem 2.}
      $ABC$ is an isosceles triangle with $BC \cong AC$. Suppose that:

        (i) $D$ is the midpoint of $AB$ and $E$ is the point on the line $CD$ such that
            $EA\perp AC$;

        (ii) $F$ is an arbitrary point on the segment $AB$ different from $A$ and $B$;

        (iii) $G$ lies on the line $CA$ and $H$ lies on the line $CB$ such that $G$, $F$, $H$ are
              distinct and collinear.

        Prove that $EF$ is perpendicular to $HG$ if and only if $GF\cong FH$.
        \enaloga


\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.IMO1.pic}
\caption{} \label{sl.skk.4.2.IMO1.pic}
\end{figure}


\textbf{\textit{Proof.}} Najprej iz skladnosti trikotnikov $CAE$ in
$CBE$ (izrek \textit{SAS} \ref{SKS}) sledi $\angle EBC\cong\angle
EAC=90^0$ in $EA\cong EB$ (Figure \ref{sl.skk.4.2.IMO1.pic}).
Dokažimo ekvivalenco $EF\perp HG \Leftrightarrow GF\cong FH$ v obe
smeri.

 ($\Rightarrow$) Predpostavimo, da sta premici $EF$ in $HG$
 pravokotni oz. $\angle EFG\cong\angle EFH=90^0$.
 Naj bosta $k$ in $l$ krožnici s premeroma $EG$ in
$EH$. Ker je $\angle EAG\cong\angle EFG=90^0$ in $\angle
EBH\cong\angle EFH=90^0$, po izreku \ref{TalesovIzrKroz} velja
$A,F\in k$ in $B,F\in l$. Najprej iz $EA\cong EB$ sledi $\angle
EAB\cong\angle EBA$. Iz tega in izreka \ref{ObodObodKot} sledi:
 $$\angle EGF\cong\angle EAF\cong\angle EBF\cong\angle EHF.$$
 Torej je trikotnik $EGH$ enakokrak, zato je njegova višina $EF$
 hkrati težiščnica (skladnost trikotnikov $EFG$ in $EFH$, izrek
 \textit{ASA} \ref{KSK}) oz. velja $GF\cong FH$.

($\Leftarrow$) Naj bo sedaj $GF\cong FH$, oz. je točka $F$
središče daljice $GH$. Naj bo $k$ krožnica s premerom $EG$.
Poleg točke $A$ označimo s $\widehat{F}$ drugo presečišče te
krožnice s premico $AB$. Če se krožnica $k$ dotika premice
$AC$, sledi $G=A$ oz. $F=D$ in $H=B$, torej je v tem primeru že
izpolnjeno $GF\cong FH$.

Predpostavimo, da je $\widehat{F}\neq F$. Naj bo $\widehat{H}$
presečišče premic $G\widehat{F}$ in $CB$. Ker točka
$\widehat{F}$ leži na krožnici $k$ s premerom $EG$, je $\angle
G\widehat{F}E=90^0$, oz. velja $E\widehat{F}\perp G\widehat{H}$.
Torej so za točke $G$, $\widehat{F}$ in $\widehat{H}$ izpolnjene
predpostavke leve strani ekvivalence, zato iz že dokazanega
prvega dela trditve ($\Rightarrow$) sledi $G\widehat{F}\cong
\widehat{F}\widehat{H}$, oz. točka $\widehat{F}$ je središče
daljice $G\widehat{H}$. V trikotniku $GH\widehat{H}$ je
$\widehat{F}F$ srednjica, zato je $\widehat{F}F\parallel
\widehat{H}H$ in $AB\parallel BC$, kar pa ni mogoče. Tako
predpostavka $\widehat{F}\neq F$ odpade, torej velja $\widehat{F}=
F$, zato je tudi $\widehat{H}=H$. Na koncu iz $E\widehat{F}\perp
G\widehat{H}$ sledi $EF\perp GH$.
 \kdokaz





%________________________________________________________________________________
 \poglavje{More About Circumcircle and Incircle of a Triangle}
 \label{odd4OcrtVcrt}


Najprej bomo obravnavali nekatere pomembne točke, ki ležijo na
očrtani krožnici trikotnika.



        \bizrek \label{TockaN}
        The bisector of the side $BC$ and the bisector of the interior angle $BAC$ of a
        triangle $ABC$ ($AB\neq AC$) intersect at the Circumcircle $l(O,R)$
        of that triangle.
         \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1.pic}
\caption{} \label{sl.skk.4.3.1.pic}
\end{figure}


\textbf{\textit{Proof.}}
   (Figure \ref{sl.skk.4.3.1.pic}).

 Naj bo točka $N$ eno od presečišč očrtane krožnice trikotnika $ABC$ in
 simetrale stranice $BC$
(takšna, da je $A,N÷BC$). Ker leži točka $N$ na simetrali stranice
$BC$, velja $NB \cong NC$. Torej je $BNC$ enakokraki trikotnik,
zato sta  $\angle NBC$ in $\angle NCB$ skladna kota (izrek
\ref{enakokraki}). Ker leži točka $N$ tudi na očrtani krožnici
trikotnika $ABC$, po izreku \ref{ObodObodKot} velja:
 \begin{eqnarray*}
 \angle BAN
\cong \angle BCN \textrm{ (obodna kota za krajši lok }BN \textrm{) }\\
 \angle NAC \cong \angle NBC \textrm{ (obodna kota za krajši lok }
 CN \textrm{).}
 \end{eqnarray*}
 Torej je $\angle BAN \cong \angle NAC$ oz. premica $AN$ je simetrala kota
$BAC$, s tem pa je trditev dokazana.
 \kdokaz


 Točka $N$ iz prejšnjega izreka je središče tistega loka $BC$ očrtane
 krožnice trikotnika $ABC$, ki ne vsebuje oglišča $A$.
 Dokažimo še eno pomembno lastnost točke $N$.



        \bizrek \label{TockaN.NBNC}
        For the point $N$ from the previous theorem is $NB\cong NS\cong NC$,
        where $S$ is the incentre of the triangle $ABC$.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.2.pic}
\caption{} \label{sl.skk.4.3.2.pic}
\end{figure}


\textbf{\textit{Proof.}} Označimo z $\alpha$ in $\beta$ notranja
kota trikotnika $ABC$ ob ogliščih $A$ in  $B$  (Figure
\ref{sl.skk.4.3.2.pic}). $BNS$ je enakokraki trikotnik (izrek
\ref{enakokraki}), ker sta kota pri ogliščih $B$ in $S$ skladna.
Če uporabimo izreka \ref{zunanjiNotrNotr} in \ref{ObodObodKot},
dobimo:
 \begin{eqnarray*}
 \angle BSN &=& \angle ABS + \angle BAS =\frac{1}{2}\alpha+\frac{1}{2}\beta,\\
\angle SBN &=& \angle SBC +\angle CBN  = \angle SBC + \angle CAN =
\frac{1}{2}\beta+\frac{1}{2}\alpha.
 \end{eqnarray*}
Torej velja $NB \cong NS$  in podobno tudi $NC \cong NS$.
\kdokaz



           \bizrek \label{TockaNbetagama}
            Let $AA'$ be the altitude from the vertices $A$ and $AE$ bisector of the interior
           angle $BAC$ of a triangle $ABC$ ($A',E\in BC$). Suppose that $l(O,R)$ is the
            circumcircle of that triangle. If $\angle CBA=\beta\geq\angle ACB=\gamma$,
          then
           $$\angle A'AE\cong \angle EAO=\frac{1}{2}\left( \beta-\gamma\right).$$
           \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1b.pic}
\caption{} \label{sl.skk.4.3.1b.pic}
\end{figure}


\textbf{\textit{Proof.}}
 Naj bo $N$ točka, definirana kot v v prejšnjih trditvah
  (Figure \ref{sl.skk.4.3.1b.pic}). Premici
 $AA'$ in $ON$ sta vzporedni, ker sta obe pravokotni na premico $BC$.
 Ker je $OA\cong ON=R$, je $AON$ enakokraki trikotnik. Zaradi tega je
 (izreka \ref{KotiTransverzala} in \ref{enakokraki}) najprej:
 $$\angle A' AE \cong \angle ANO \cong \angle NAO =
\angle EAO,$$
 nato pa še:
 $$\angle A'AE=\frac{1}{2}\alpha-\left(90^0-\beta \right)=
 \frac{1}{2}\alpha-\left(\frac{\alpha+\beta+\gamma}{2}-\beta \right)=
 \frac{1}{2}\left( \beta-\gamma\right),$$ kar je bilo treba dokazati. \kdokaz




           \bzgled \label{tockaNtockePQR}
             Let $P$, $Q$ and $R$ be the midpoints of those arcs $BC$, $AC$ and $AB$ of
           the circumcircle of a triangle $ABC$ not containing the vertices $A$, $B$ and $C$
            of that triangle.
            If $E$ and $F$ are intersections of the line $QR$ with sides $AB$ and $AC$, respectively
             and $S$ the incentre of this triangle, then:

             (i) $AP \perp QR$,

              (ii) the quadrilateral $AESF$ is a rhombus.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.2a.pic}
\caption{} \label{sl.skk.4.3.2a.pic}
\end{figure}


\textbf{\textit{Proof.}} (Figure \ref{sl.skk.4.3.2a.pic})

(\textit{i}) Naj bo $L$ presecišče premic $AP$ in $QR$. Po izreku
\ref{TockaN} točke $P$, $Q$ in $R$ ležijo na simetralah $AS$, $BS$
in $CS$ notranjih kotov trikotnika $ABC$ ($S$ je središče trikotniku
$ABC$ včrtane krožnice). Če z $\alpha$, $\beta$ in $\gamma$ označimo
notranje kote trikotnika $ABC$, potem zaradi skladnosti ustreznih
obodnih kotov (izrek \ref{ObodObodKot}) dobimo:
 \begin{eqnarray*}
\angle RPL &=& \angle RPA = \angle RCA =\frac{1}{2}\gamma,\\
 \angle PRL &=& \angle PRQ = \angle PRC + \angle CRQ =
\angle PAC + \angle CBQ = \frac{1}{2}\alpha+ \frac{1}{2}\beta.
 \end{eqnarray*}
Torej je vsota kotov v trikotniku $PRL$  (izrek \ref{VsotKotTrik})
$180^0 =\frac{1}{2}\alpha+ \frac{1}{2}\beta +\frac{1}{2}\gamma
+\angle RLP = 90° + \angle RLP$. Zato je $\angle RLP = 90°$ oz. $AP
\perp QR$.

 (\textit{ii}) Po
izreku \ref{TockaN.NBNC} je $RA \cong RS$, zato iz skladnosti
pravokotnih trikotnikov $ALR$ in $SLR$ (izrek \textit{SSA}
\ref{SSK}) sledi, da je točka $L$ središče diagonale $AS$
štirikotnika $AESF$. Iz skladnosti trikotnikov $AEL$ in $AFL$ (izrek
\textit{ASA} \ref{KSK}) sledi, da je točka $L$ tudi središče
diagonale $EF$, zato je $AESF$ paralelogram (izrek
\ref{paralelogram}. Ker sta diagonali $AS$ in $EF$ še pravokotni, je
 štirikotnik $AESF$ romb (izrek \ref{RombPravKvadr}).
  \kdokaz

Iz prejšnje trditve dobimo direktno posledico.


          \bzgled \label{PedalniLemasPQR}
           Let $P$, $Q$ and $R$ be the midpoints of those arcs $BC$, $AC$ and $AB$ of
           the circumcircle of a triangle $ABC$ not containing the vertices $A$, $B$ and $C$
            of that triangle.
            Prove that the incentre of the  triangle $ABC$ is at the same time
            orthocentre  of the triangle $PQR$ (Figure \ref{sl.skk.4.3.2b.pic}).
          \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.2b.pic}
\caption{} \label{sl.skk.4.3.2b.pic}
\end{figure}



Dokažimo nekaj posledic izreka \ref{ObodObodKot}, ki so povezane z
višinsko točko.



         \bizrek \label{TockaV'}
         Points that are symmetric to the orthocentre of an acute triangle
            with respect to its sides lie on the circumcircle of this triangle.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.3.pic}
\caption{} \label{sl.skk.4.3.3.pic}
\end{figure}


\textbf{\textit{Proof.}} Naj bo $V$ višinska točka trikotnika $ABC$,
$l$ očrtana krožnica trikotnika $ABC$ in $V_a$ drugo presečišče
krožnice $l$ z nosilko višine $AA'$ (Figure \ref{sl.skk.4.3.3.pic}).
Dokažimo da je točka $V_a$ simetrična točki $V$ glede na premico
$BC$. Dovolj je dokazati, da je $VA'\cong V_aA'$. Kota $V_aBC$ in
$V_aAC$ sta skladna (obodna kota za tetivo $V_aC$ - izrek
\ref{ObodObodKot}), kota $V_aAC$ in $CBV$  sta skladna kota s
pravokotnima krakoma (izrek \ref{KotaPravokKraki}). Torej sta skladna
 tudi kota $V_aBC$ in $CBV$, zato pa tudi trikotnika $V_aBA'$ in
$VBA'$ oz. velja $VA'\cong V_aA'$. Podobno velja tudi za drugi dve
višini.
 \kdokaz

            \bizrek \label{TockaV'a}
            Let $V$ be the orthocentre of a triangle
            $ABC$. The circumcircles of the triangles $VBC$, $AVB$ and $ACV$ are congruent to
            the circumcircle of the triangle $ABC$.
             \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.3a.pic}
\caption{} \label{sl.skk.4.3.3a.pic}
\end{figure}


\textbf{\textit{Proof.}} Direktna posledica prejšnjega izreka
\ref{TockaV'}, kajti tri omenjene očrtane krožnice so simetrične
očrtani krožnici trikotnika $ABC$ glede na nosilke njegovih stranic
(Figure \ref{sl.skk.4.3.3a.pic}).



         \bizrek \label{TockaV1}
          Points that are symmetric to the orthocentre of an acute triangle
            with respect to the midpoints of its sides lie on the circumcircle of this triangle.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.3b.pic}
\caption{} \label{sl.skk.4.3.3b.pic}
\end{figure}


\textbf{\textit{Proof.}} Naj bo $V$ višinska točka trikotnika $ABC$,
$l$ očrtana krožnica (s središčem $O$) trikotnika $ABC$ in $V_{A_1}$ točka, ki je simetrična točki $A$ glede na točko $O$ (Figure \ref{sl.skk.4.3.3.pic}). Iz same definicije točke $V_{A_1}$ je jasno, da ta leži na krožnici $l$. Dokažimo še, da je $V_{A_1}$ simetrična točki $V$ glede na točko $A_1$, ki je središče daljice $BC$. Ker je $AV_{A_1}$ premer krožnice $l$, je po izreku \ref{TalesovIzrKroz2} $\angle ACV_{A_1}=90^0$ oz. $V_{A_1}C\perp AC$.  Premica $BV$ je nosilka višine trikotnika $ABC$, zato velja $BV\perp AC$. Iz zadnjih dveh relacij sledi $V_{A_1}C\parallel BV$. Analogno je tudi
$V_{A_1}B\parallel CV$. Torej je štirikotnik $V_{A_1}CVB$ paralelogram, zato imata njegovi diagonali $VV_{A_1}$ in $BC$ skupno središče. Središče daljice $BC$ je točka $A_1$, kar pomeni, da  je $V_{A_1}$ simetrična točki $V$ glede na točko $A_1$. Točka $V_{A_1}$ pa po konstrukciji leži na krožnici $l$.
\kdokaz


Dokažimo še nekaj posledic izreka \ref{ObodObodKot}, ki so povezane z očrtano
krožnico trikotnika.


        \bzgled \label{zgledTrikABCocrkrozP}
        Let  $k$ be the circumcircle of a regular triangle $ABC$.
         If $P$ is an arbitrary point lying
        on the shorter arc $BC$ of the circle $k$, then
         $$|PA|=|PB|+|PC|.$$
         \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.4.pic}
\caption{} \label{sl.skk.4.3.4.pic}
\end{figure}


\textbf{\textit{Proof.}} Ker je $\angle ACP>60^0>\angle PAC$, je
po izreku \ref{vecstrveckot} $AP>PC$ (Figure
\ref{sl.skk.4.3.4.pic}). Zato na daljici $AP$ obstaja takšna točka
$Q$, da velja $PQ\cong PC$. Po izreku \ref{ObodObodKot} je $\angle
CPQ=\angle CPA\cong\angle CBA=60^0$, kar pomeni, da je $PCQ$
enakostranični trikotnik, zato je tudi $CQ\cong CP$ in $\angle
PCQ=60^0$. Iz tega sledi $\angle ACQ=\angle ACP-60^0=\angle BCP$.
Po izreku \textit{SAS} (izrek \ref{SKS}) sta torej skladna trikotnika
$ACQ$ in $BCP$, zato je tudi $AQ\cong BP$.

Na koncu je: $|PB|+|PC|=|AQ|+|PQ|=|AP|$.
\kdokaz



            \bzgled
            Three circles of equal radii $r$ intersect at point $O$.
            Furthermore each two of them intersect at one more point: $A$, $B$, and $C$.
            Prove that the radius of the circumcircle of the triangle $ABC$ is also $r$.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.5.pic}
\caption{} \label{sl.skk.4.3.5.pic}
\end{figure}


\textbf{\textit{Proof.}}
   (Figure \ref{sl.skk.4.3.5.pic})

Označimo s $k$, $l$, $j$ in $o$ očrtane krožnice trikotnikov $OBC$,
$OAC$, $OAB$ in $ABC$ ter s $P$ poljubno točko krožnice $k$ tako, da
sta točki $O$ in $P$ na različnih straneh premice $BC$. Po
predpostavki so krožnice $k$, $l$ in $j$ skladne. Kota $BAO$ in
$BCO$ sta tudi skladna, ker sta obodna kota skladnih krožnic $k$ in $j$
nad tetivo $BO$ (izrek \ref{SklTetSklObKot2}). Analogno sta skladna
tudi kota $CAO$ in $CBO$. Zaradi tega je:
 $$\angle BAC = \angle BAO + \angle CAO = \angle BCO
+ \angle CBO = 180° - \angle BOC = \angle BPC.$$
 Torej imata krožnici $k$ in $o$ skladna
obodna kota nad skupno tetivo $BC$, zato sta med seboj skladna.
   \kdokaz



             \bzgled \label{KvadratKonstr4tocke}
            Construct a square $ABCD$ such that given points $P$, $Q$, $R$ and $S$
             lyes on the sides $AB$, $BC$, $CD$ and $DA$ of this square, respectively.
             \ezgled



\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1c.pic}
\caption{} \label{sl.skk.4.3.1c.pic}
\end{figure}


\textbf{\textit{Solution.}}
Ker sta $\angle PAS$ in $\angle QCR$ prava kota, oglišči $A$ in $B$ ležita na krožnicah $k$ in $l$ s premeroma
$PS$ in $QR$ (Figure \ref{sl.skk.4.3.1c.pic}). Nosilka diagonale $AC$ kvadrata $ABCD$ je hkrati simetrala notranjih kotov $BAD$ in $BCD$, zato gre skozi
središči $N$ in $M$ ustreznih polkrožnic, ki sta določeni s $k$ in $l$ (izrek \ref{TockaN}).
Konstrukcijo  lahko torej  izpeljemo tako, da najprej načrtamo krožnici $k$ in $l$, nato premico $NM$, oglišči $A$ in $C$ in na koncu še
oglišči $B$ in $D$.
 \kdokaz




         \bzgled
         Construct a triangle $v_a$, $t_a$, $l_a$.
         \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1e.pic}
\caption{} \label{sl.skk.4.3.1e.pic}
\end{figure}

   \textbf{\textit{Solution.}}
   Naj bo $ABC$ trikotnik, v katerem so višina $AA'$,
težiščnica $AA_1$ in odsek simetrale $AE$ notranjega kota $BAC$ skladni z
daljicami $v_a$, $t_a$ in $l_a$. Z $O$ označimo središče trikotniku $ABC$ očrtane
krožnice $k$. Po izreku \ref{TockaN}
se premici $AE$ in $OA_1$ sekata v točki $N$, ki leži na
krožnici $k$ (Figure \ref{sl.skk.4.3.1e.pic}).

Torej lahko najprej načrtamo
pravokotni trikotnik $AA'E$ s kateto $v_a$ in hipotenuzo $l_a$ ter točko $A_1$ iz pogoja $AA_1\cong t_a$. Nato
načrtamo točko $N$ kot presečišče premice $AE$ in pravokotnice premice $A'E$ skozi
točko $A_1$. Središče $O$ je  presečišče premice $A_1N$ in
simetrale daljice $AN$ (ker je $AN$ tetiva krožnice $k$). Oglišči $B$ in $C$ sta presečišči
krožnice $k(O,OA)$ s premico $A'E$.
   \kdokaz




         \bzgled
         Construct a triangle  $R$, $r$, $a$. \label{konstr_Rra}
         \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1a.pic}
\caption{} \label{sl.skk.4.3.1a.pic}
\end{figure}


\textbf{\textit{Solution.}} Naj bo $ABC$ takšen trikotnik, da velja
$BC\cong a$ in sta $l(O,R)$ in $k(S,r)$ njegova očrtana oz. včrtana
krožnica
   (Figure \ref{sl.skk.4.3.1a.pic}). Označimo z $\alpha$, $\beta$ in $\gamma$
njegove notranje kote pri ogliščih $A$, $B$ in $C$. Po izreku
\ref{SredObodKot} je $\alpha = \angle BAC = \frac{1}{2}\cdot\angle BOC$.
Iz zgleda \ref{kotBSC} sledi $\angle BSC=90^0+\frac{1}{2}\cdot\alpha$.
Iz dveh relacij dobimo enakost
$\angle BSC=90^0+\frac{1}{4}\cdot\angle BOC$, ki omogoča konstrukcijo.

Najprej načrtamo enakokraki trikotnik $BOC$ ($BC\cong a$ in $OB\cong
OC\cong R$). Točko $S$ dobimo kot eno od presečišč loka s tetivo
$BC$ in obodnim kotom $90^0+\frac{1}{4}\cdot\angle BOC$ ter premico,
ki je na razdalji $r$ vzporedna s premico $BC$. Nato načrtamo
včrtano krožnico $k(S,r)$ in točko $A$ kot presečišče ostalih dveh tangent
te krožnice iz točk $B$ in $C$.
 \kdokaz



        \bnaloga\footnote{47. IMO Slovenia - 2006, Problem 1.}
        Let $ABC$ be a triangle with incentre $I$. A point $P$ in the interior of the
        triangle satisfies
        $$\angle PBA + \angle PCA = \angle PBC + \angle PCB.$$
        Show that $|AP| \geq |AI|$, and that equality holds if and only if $P = I$.
         \enaloga


\begin{figure}[!htb]
\centering
\input{sl.skl.4.3.IMO1.pic}
\caption{} \label{sl.skl.4.3.IMO1.pic}
\end{figure}


\textbf{\textit{Proof.}} Označimo z $\alpha$, $\beta$ in $\gamma$
notranje kote trikotnika $ABC$ pri ogliščih $A$, $B$ in $C$
(Figure \ref{sl.skl.4.3.IMO1.pic}). Pogoj $\angle PBA + \angle PCA
= \angle PBC + \angle PCB$ lahko preoblikujemo v obliko
$\beta-\angle PBC + \gamma-\angle PCB = \angle PBC + \angle PCB$
oziroma:
 $$\angle PBC + \angle PCB=\frac{1}{2}\left( \beta+\gamma\right).$$
Iz tega in dejstva, da je vsota notranjih kotov vsakega izmed
trikotnikov $BPC$ in $ABC$ enaka $180^0$ (izrek\ref{VsotKotTrik}),
sledi:
 $$\angle BPC =180^0-\frac{1}{2}\left( \beta+\gamma\right)=90^0+
 \frac{1}{2} \alpha.$$
Toda iz zgleda \ref{kotBSC} sledi $\angle BIC =90^0+
 \frac{1}{2}\cdot \alpha$, zato je $\angle BPC\cong \angle BIC$.
 Torej točki $P$ in $I$ ležita na istem loku $\mathcal{L}$ s
 tetivo $BC$ in obodnim kotom $90^0+
 \frac{1}{2} \alpha$. Naj bo točka $N$ presečišče
 simetrale stranice $BC$ in simetrale
 notranjega kota $BAC$ trikotnika $ABC$. Po izreku
 \ref{TockaN} leži točka $N$ na očrtani krožnici
  trikotnika $ABC$ in velja $NB\cong NI\cong NC$ (izrek
  \ref{TockaN.NBNC}). To pomeni, da je $N$ središče loka
  $\mathcal{L}$, zato je $NP\cong NI$ oz. $\angle NIP\cong\angle
  NPI<90^0$. Ker so točke $A$, $I$ in $N$ kolinearne (ležijo na
  simetrali notranjega kota $BAC$), je $\angle AIP =180^0-\angle
  NIP>90^0$. Iz izreka \ref{vecstrveckot} (za trikotnik $API$)
  sedaj sledi $|AP| \geq |AI|$ in enakost velja natanko tedaj, ko
  trikotnika $API$ ni oz. kadar je $P=I$.
  \kdokaz


        \bnaloga\footnote{43. IMO United Kingdom - 2002, Problem 2.}
          $BC$ is a diameter of a circle center $O$. $A$ is any point on
        the circle with $\angle AOC>60^0$. $EF$ is the chord which is the perpendicular
        bisector of $AO$. $D$ is the midpoint of the minor arc $AB$. The line through
        $O$ parallel to $AD$ meets $AC$ at $J$. Show that $J$ is the incenter of triangle
        $CEF$.
         \enaloga


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.IMO4.pic}
\caption{} \label{sl.skk.4.3.IMO4.pic}
\end{figure}


\textbf{\textit{Proof.}} Ker
točki $E$ in $F$ ležita na simetrali daljice $EF$, hkrati pa na
krožnici s središčem $O$, je $$AF\cong FO\cong AO\cong EO \cong EA.$$ To
pomeni, da je štirikotnik $EOFA$ romb, ki je sestavljen iz dveh enakostraničnih trikotnikov $AOF$ in $AEO$.

Brez škode za splošnost predpostavimo, da
je $\angle COE>\angle COF$ (Figure \ref{sl.skk.4.3.IMO4.pic}).
Najprej iz pogoja $\angle
        AOC>60^0$ sledi, da je $\angle COF=60^0- \angle
        AOC>0^0$, zato sta točki $A$ in $F$ na isti strani premice
        $BC$.

 Ker je $AOC$ enakokraki trikotnik z osnovnico $AC$, po izrekih
 \ref{enakokraki} in \ref{zunanjiNotrNotr} velja
  $\angle ACO =\frac{1}{2}\angle AOB$. Točka $D$ je središče
  loka $BD$, zato je $\angle AOD\cong\angle DOB$
  oz. $\angle DOB=\frac{1}{2}\angle AOB$. To pomeni, da je
   $\angle ACO\cong\angle DOB$ in sta po izreku
   \ref{KotiTransverzala} premici $AC$ in $DO$ vzporedni oz.
   $AJ\parallel DO$. Ker je po predpostavki $AD\parallel JO$, je
   štirikotnik $ADOJ$ paralelogram, zato je $AJ\cong OD$. Torej
   $$AJ\cong OD\cong OE\cong AF\cong AE.$$
   Iz $AF\cong AE$ sledi, da
  je $AJ$ simetrala notranjega kota pri oglišču $C$ trikotnika $CEF$
   (izrek \ref{SklTetSklObKot}). Ker je še
  $AJ\cong  AF\cong AE$,
  je po izreku \ref{TockaN.NBNC} točka $J$ središče
        včrtane krožnice tega trikotnika.
\kdokaz


%________________________________________________________________________________
 \poglavje{Cyclic Quadrilateral} \label{odd4Tetivni}

Za večkotnik pravimo, da je
\index{štirikotnik!tetiven}\index{večkotnik!tetiven}\pojem{tetiven},
če zanj obstaja očrtana krožnica, oz. če obstaja krožnica, ki
vsebuje vsa njegova oglišča (Figure \ref{sl.skk.4.5.10.pic}). Za
oglišča v tem primeru pravimo, da so \index{konciklične
točke}\pojem{konciklične točke}.  Ugotovili smo že, da je vsak
trikotnik tetiven (izrek \ref{SredOcrtaneKrozn}) in prav tako, da je
vsak pravilni večkotnik tetiven (izrek \ref{sredOcrtaneKrozVeck}).
Po drugi strani je jasno, da niso vsi večkotniki tetivni. Npr. romb
je štirikotnik, ki nima očrtane krožnice.
V tem razdelku se bomo torej ukvarjali s tetivnimi štirikotniki.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.10.pic}
\caption{} \label{sl.skk.4.5.10.pic}
\end{figure}

Ker je kvadrat pravilni večkotnik, je hkrati tetivni štirikotnik. Ni
težko dokazati, da je tudi pravokotnik vrsta tetivnega štirikotnika
- središče očrtane krožnice je presečišče njegovih diagonal, ki sta
skladni in se razpolavljata. Toda kako bi na splošno ugotovili ali
je nek štirikotnik tetiven? Jasno je, da se pri tetivnem
štirikotniku (na splošno tudi večkotniku) simetrale vseh njegovih
stranic sekajo v eni točki (Figure \ref{sl.skk.4.5.10.pic}). Ta pogoj
je zadosten, da je štirikotnik tetiven, ni pa
preveč operativen v konkretnih primerih. Za tetivnost štirikotnikov
obstaja namreč potreben in zadosten pogoj, ki je uporabnejši.



             \bizrek \label{TetivniPogoj}
               A convex quadrilateral is cyclic if and only if
            its opposite interior angles are supplementary.
            Thus, if $\alpha$, $\beta$, $\gamma$ and $\delta$ are
            the interior angles of a convex quadrilateral $ABCD$,
            it is cyclic if and only if
                $$\alpha+\gamma=180^0.$$
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.11.pic}
\caption{} \label{sl.skk.4.5.11.pic}
\end{figure}

\textbf{\textit{Proof.}}
 (Figure \ref{sl.skk.4.5.11.pic})

($\Rightarrow$) Predpostavimo najprej, da je štirikotnik $ABCD$
tetiven. Ker je konveksen, sta oglišči $A$ in $C$ na različnih
straneh premice $BD$. Po izreku \ref{ObodObodKotNaspr} je
$\alpha+\gamma=180^0$.

($\Leftarrow)$ Predpostavimo sedaj, da sta nasprotna kota
štirikotnika $ABCD$ suplementarna oz. $\alpha+\gamma=180^0$. Naj bo
$k$ očrtana krožnica trikotnika $ABD$. V tem primeru se iz četrtega
oglišča $C$ tetiva $BD$ vidi pod kotom, ki je suplementaren kotu pri
oglišču $A$, kar pomeni, da tudi točka $C$ leži na krožnici $k$
(izrek \ref{ObodKotGMT}).
  \kdokaz

  A direct consequence is the following theorem.



             \bizrek \label{TetivniPogojZunanji}
              A convex quadrilateral is cyclic if and only if
            one of its interior angles is congruent to the opposite exterior angle.
            Thus, if $\alpha$, $\beta$, $\gamma$ and $\delta$ are
            the interior angles and
            $\alpha'$, $\beta'$, $\gamma'$ in $\delta'$ the exterior angles
             of a convex quadrilateral $ABCD$,
            it is cyclic if and only if
                $$\alpha\cong\gamma'.$$
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.12.pic}
\caption{} \label{sl.skk.4.5.12.pic}
\end{figure}

Uporabimo kriterij iz izreka \ref{TetivniPogoj} za paralelogram in
trapez.

            \bizrek \label{paralelogramTetivEnakokr}
            A parallelogram is cyclic if and only if it is a rectangle.
            \eizrek


\textbf{\textit{Proof.}} Naj bodo $\alpha$, $\beta$, $\gamma$ in
$\delta$ notranji koti paralelograma $ABCD$
 (Figure \ref{sl.skk.4.5.13.pic}).

($\Leftarrow$) Če je paralelogram pravokotnik, je
$\alpha+\gamma=90^0+90^0=180^0$, kar pomeni, da je $ABCD$ tetiven
štirikotnik (izrek \ref{TetivniPogoj}).

 ($\Rightarrow$) Predpostavimo, da je $ABCD$ tetivni paralelogram.
 Ker je $ABCD$ paralelogram, je po izreku \ref{paralelogram}
 $\alpha\cong\gamma$. Ker je tudi tetiven, je po izreku \ref{TetivniPogoj}
$\alpha+\gamma=180^0$. Torej velja $\alpha\cong\gamma=90^0$, zato je
  $ABCD$ pravokotnik.
 \kdokaz

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.13.pic}
\caption{} \label{sl.skk.4.5.13.pic}
\end{figure}



            \bizrek \label{trapezTetivEnakokr}
            A trapezium is cyclic if and only if it is isosceles.
            \eizrek

\textbf{\textit{Proof.}} Naj bo $ABCD$ trapez z osnovnico $AB$ in z
notranjimi koti $\alpha$, $\beta$, $\gamma$ in $\delta$
 (Figure \ref{sl.skk.4.5.13.pic}). V poljubnem trapezu
  velja $\alpha+\delta=180^0$ in $\beta+\gamma=180^0$.


($\Leftarrow$) Predpostavimo, da je trapez $ABCD$ enakokrak oz. $AD
\cong BC$. Po izreku \ref{trapezEnakokraki} je v tem primeru
$\alpha\cong\beta$. Torej $\alpha+\gamma=\beta+\gamma=180^0$, zato
je po izreku \ref{TetivniPogoj} $ABCD$ tetivni štirikotnik.

($\Rightarrow$) Naj bo trapez $ABCD$ tetivni štirikotnik in $k$
njegova očrtana krožnica. Osnovnici $AB$ in $CD$ sta vzporedni
tetivi te krožnice, zato imata skupno simetralo, ki poteka skozi
središče $S$ krožnice $k$ in je pravokotna na tetivi $AB$ in
$CD$. To pomeni, da sta kraka $AD$ in $BC$ simetrična glede na to
simetralo, zato sta med seboj skladna in je trapez $ABCD$  enakokrak.
 \kdokaz

 Posebej so zanimivi tetivni štirikotniki s pravokotnima
 diagonalama\footnote{\index{Brahmagupta}\textit{Brahmagupta} (598--660), indijski matematik, ki je
 preučeval takšne štirikotnike.}.
 Na te štirikotnike se nanaša
naslednji primer.


            \bzgled \label{TetivniLemaBrahm}
            Suppose that the diagonals of a cyclic quadrilateral $ABCD$ are perpendicular and intersect
            at a point $S$. Prove that the foot of the perpendicular from the point $S$ on the line $AB$
            contains the midpoint of the line $CD$.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.14.pic}
\caption{} \label{sl.skk.4.5.14.pic}
\end{figure}

\textbf{\textit{Proof.}}
 (Figure \ref{sl.skk.4.5.14.pic})

Označimo z $N$ in $M$ presečišči pravokotnice na premico $AB$ skozi
točko $S$ s stranicama $AB$ in $CD$ štirikotnika $ABCD$. Tedaj velja:
 \begin{eqnarray*}
 \angle CDB &\cong& \angle CAB \hspace*{3mm}
 \textrm{(obodna kota za ustrezni lok } CB
 \textrm{ - izrek \ref{ObodObodKot}})\\
      &\cong& \angle NSB  \hspace*{3mm}
 \textrm{ (kota s
pravokotnima krakoma - izrek \ref{KotaPravokKraki})}\\
     &\cong& \angle MSD  \hspace*{3mm}
 \textrm{(sovršna kota)}
 \end{eqnarray*}
 Ker je $\angle CDB\cong \angle MSD$, je $MD \cong MS$ (izrek \ref{enakokraki}).
 Analogno je tudi $MC \cong MS$. Torej je
 $MD \cong MC$, kar pomeni, da je $M$ središče stranice $CD$.
 \kdokaz

Eno lastnost tetivnih štirikotnikov s pravokotnima diagonalama
bomo obravnavali še v zgledu \ref{HamiltonPoslTetiv}.



             \bzgled \label{TetŠtirZgl0}
             Let $k$ be the circumcircle of a cyclic quadrilateral $ABCD$
            and $N$, $M$, $L$ and $P$ the midpoints of those arcs $AB$, $B$C, $CD$ and $AD$
            of the circle $k$, not containing the third vertices of this quadrilateral.
            Prove that $NL\perp PM$.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.0.pic}
\caption{} \label{sl.skk.4.5.0.pic}
\end{figure}

\textbf{\textit{Proof.}} Naj bo $S$ presečišče premic $NL$ in $PM$
(Figure \ref{sl.skk.4.5.0.pic}).
 Če dvakrat uporabimo izreka \ref{ObodObodKot} in \ref{TockaN}, dobimo:

 \begin{eqnarray*}
  \angle PNS &=& \angle PND +\angle DNL =
\angle PBD +\angle DBL =\\
 &=& \frac{1}{2} \angle ABD +\frac{1}{2}\angle CBD = \frac{1}{2}\angle
 ABC.
 \end{eqnarray*}

 Na enak način dokažemo tudi $\angle NPS = \frac{1}{2}\angle
 ADC$. Zato je po izreku \ref{TetivniPogoj}:
 $$\angle PNS +\angle NPS = \frac{1}{2} \left(\angle ABC+\angle
 ADC\right)=90^0.$$
 Če izrek \ref{VsotKotTrik} uporabimo za trikotnik $PSN$, dobimo
 $\angle PSN = 90^0$.
  \kdokaz


              \bzgled \label{TetivniVcrtana}
             Let $ABCD$ be a cyclic quadrilateral.
             Prove that incentres of the triangles $BCD$, $ACD$, $ABD$ and $ABC$
             are the vertices of a rectangle.
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.1.pic}
\caption{} \label{sl.skk.4.5.1.pic}
\end{figure}

\textbf{\textit{Proof.}} Označimo z $A_1$, $B_1$, $C_1$ in $D_1$
središča včrtanih krožnic trikotnikov $BCD$, $ACD$, $ABD$ in $ABC$
ter z $N$, $M$, $L$ in $P$ središča tistih lokov $AB$, $BC$, $CD$ in
$AD$ očrtane krožnice štirikotnika $ABCD$, ki ne vsebujejo ostalih
oglišč tega štirikotnika (Figure \ref{sl.skk.4.5.1.pic}). Iz zgleda
\ref{TockaN} sledi, da sta $BL$ in $DM$ simetrali kotov $CBD$ in
$BDC$, zato je točka $A_1$ presečišče premic $BL$ in $DM$. Analogno
je točka $B_1$ presečišče premic $CP$ in $AL$. Po zgledu
\ref{TockaN.NBNC} je
 $LC\cong LA_1\cong LB_1\cong LD$, torej je $A_1LB_1$ enakokraki trikotnik
 z osnovnico $A_1B_1$. Iz zgleda \ref{TockaN} sledi tudi,
 da je $LN$ simetrala kota $ALB$ oz. $B_1LA_1$. V enakokrakem
 trikotniku $A_1LB_1$ simetrala kota $B_1LA_1$ vsebuje višino
 tega trikotnika iz točke $L$. To pomeni, da velja $LN\perp
 A_1B_1$. Analogno sledi tudi $LN\perp C_1D_1$,  $PM\perp A_1D_1$
 in
 $PM\perp C_1B_1$. Iz prejšnjega zgleda \ref{TetŠtirZgl0} je $LN\perp PM$,
 zato je štirikotnik $A_1B_1C_1D_1$ pravokotnik.
  \kdokaz

Omenili smo že, da je pravokotnik tetivni štirikotnik. Sedaj bomo
dokazali zanimivo lastnost pravokotnika, ki se nanaša na točke,
ki ležijo na njegovi očrtani krožnici.



            \bzgled
             Let $P$ be an arbitrary point on the shorter arc $AB$ of the circumcircle of a rectangle $ABCD$.
            Suppose that $L$ and $M$ are the foots of the perpendiculars from the point $P$ on the
            diagonals $AC$ and $BD$, respectively. Prove that the length of the line segment $LM$ does not depend
            on the position of the point $P$.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.15.pic}
\caption{} \label{sl.skk.4.5.15.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bo točka $O$ središče krožnice $k$ (Figure \ref{sl.skk.4.5.15.pic}).
Štirikotnik $PMOL$ je tetiven, ker je $\angle OLP + \angle OMP
=90^0+90^0= 180^0$ (izrek \ref{TetivniPogoj}). Označimo z $l$
očrtano krožnico tega štirikotnika. Ker sta kota $OLP$ in $OMP$ oba
prava, je daljica $OP$ (oz. polmer krožnice $k$) premer krožnice
$l$. Potem je $LM$ tetiva krožnice $l$, ki pripada obodnemu kotu
$\angle LOM =\angle AOB$, ki je konstanten. Ne glede na izbiro
točke $P$ je daljica $LM$ tetiva krožnice s konstantnim premerom
$OA$, ki pripada konstantnem obodnem kotu $AOB$ (oziroma ustreznemu
konstantnemu središčnem kotu te krožnice). Tetivi, ki pripadata
skladnima središčnima kotoma skladnih krožnic, sta med seboj skladni,
zato dolžina daljice $LM$ ni odvisna od lege točke $P$.
 \kdokaz

  Lastnosti tetivnega štirikotnika pogosto uporabljamo tudi za dokazovanje
  različnih
lastnosti trikotnika.


            \bzgled \label{PedalniVS}
            The orthocentre of an acute triangle is the incentre of its \index{trikotnik!pedalni} pedal triangle.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.16.pic}
\caption{} \label{sl.skk.4.5.16.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Naj bodo $AA'$, $BB'$ in $CC'$ višine trikotnika $ABC$, ki se sekajo
 v višinski točki $V$ tega
trikotnika (Figure \ref{sl.skk.4.5.16.pic}). Če je $A_1$ središče
stranice $BC$, točki $B'$ in $C'$ ležita na krožnici $k(A_1,A_1B)$
(izrek \ref{TalesovIzrKroz2}). Torej je štirikotnik $BC'B'C$
tetiven, zato je po izreku \ref{TetivniPogojZunanji} $\angle
AC'B'\cong \angle ACB = \gamma$. Analogno dokažemo, da je
štirikotnik $AC'A'C$ tetiven, zato je tudi $\angle BC'A'\cong
\angle ACB = \gamma$. Torej sta kota $AC'B'$ in $BC'A'$ skladna. Ker
je $CC'\perp AB$, sta skladna tudi kota $CC'B'$ in $CC'A'$. To
pomeni, da je premica $C'C$ simetrala kota $A'C'B'$. Analogno sta
tudi premici $A'A$ in $B'B$ simetrali ustreznih notranjih kotov
trikotnika $A'B'C'$, zato je točka $V$ središče trikotniku $A'B'C'$
včrtane krožnice.
 \kdokaz

 Iz dokaza prejšnje trditve (\ref{PedalniVS}) lahko ugotovimo, da so koti, ki jih določajo stranice
pedalnega trikotnika $A'B'C'$  s stranicami trikotnika
$ABC$, enaki ustreznim kotom trikotnika $ABC$. To dejstvo bomo
uporabili v naslednjem primeru.



            \bzgled \label{PedalniLemaOcrtana}
             Let $O$ be the circumcentre of a triangle $ABC$.
            Prove that the lines $OA$, $OB$ and $OC$ are perpendicular to the corresponding sides of the
            pedal triangle $A'B'C'$.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.17.pic}
\caption{} \label{sl.skk.4.5.17.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skk.4.5.17.pic}).

Z $L$ označimo presečišče premic $OA$ in $B'C'$. Dovolj je dokazati,
da je notranji kot pri oglišču $L$ trikotnika $C'LA$ pravi kot.
Izračunajmo druga dva kota tega trikotnika. Iz prejšnjega zgleda
\ref{PedalniVS} je kot pri oglišču $C'$ enak $\gamma$. Trikotnik
$AOB$ je enakokrak in $\angle AOB=2\gamma$ (izrek \ref{SredObodKot}).
Torej velja (izreka \ref{enakokraki} in \ref{VsotKotTrik})
 $\angle C' AL=\angle BAO =90^0-\gamma$,
zato je $\angle ALC'=90^0$.
 \kdokaz

Direktna posledica trditev \ref{PedalniVS} in \ref{PedalniLemasPQR}
je naslednja trditev.



            \bzgled \label{PedalniLemasLMN}
            Let $P$, $Q$ and $R$ be the midpoints of those arcs $BC$, $AC$ and $AB$
            of the circumcircle of a triangle $ABC$ not containing the vertices $A$, $B$ and $C$.
            Suppose that the point $S$ is the incentre of the triangle $ABC$
             and $L=SA\cap QR$, $M=SB\cap PR$ and $N=SC\cap PQ$. Then the triangles $LMN$ and $ABC$ have
            the common incentre.
             (Figure \ref{sl.skk.4.5.18.pic}).
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.18.pic}
\caption{} \label{sl.skk.4.5.18.pic}
\end{figure}



             \bzgled \label{Miquelova točka}
             Let $P$, $Q$ and $R$ be an arbitrary points on the sides $BC$, $AC$ and $AB$
             of the triangle $ABC$, respectively. Prove that the circumcircles of triangles
              $AQR$, $PBR$ and $PQC$ intersect at in one point (so-called \index{točka!Miquelova}
            \pojem{Miquel point}\color{green1}\footnote{Točko imenujemo po
            francoskem matematiku \index{Miquel, A.} \textit{A. Miquelu} (1816–-1851), ki je
            to trditev objavil leta 1838 kot članek v Liouvilleovem
            (\index{Liouville, J.}\textit{J. Liouville} (1809–-1882), francoski
            matematik) časopisu. Toda, kot je to pogosto pri matematiki, Miquel
            ni bil prvi, ki je omenjeni izrek dokazal. Že deset let pred njim je
            to dejstvo odkril in objavil znani švicarski matematik
            \index{Steiner, J.} \textit{J. Steiner} (1769--1863).}).
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.2.pic}
\caption{} \label{sl.skk.4.5.2.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skk.4.5.2.pic})

Označimo  s $k_A$, $k_B$ in $k_C$ očrtane krožnice trikotnikov
$AQR$, $PBR$ in $PQC$ ter notranje kote trikotnika $ABC$ po vrsti z
$\alpha$, $\beta$ in $\gamma$. Naj bo $S$ drugo presečišče krožnic
$k_B$ in $k_C$ (dokaz je podoben tudi v primeru, če je $S = P$).
Štirikotnika $BPSR$ in $PCQS$ sta tetivna, zato je $\angle RSP =
180^0 - \beta$ in $\angle QSP = 180^0 -\gamma$ (izrek
\ref{TetivniPogoj}). Iz tega sledi $\angle RSQ = \beta +\gamma$ in
potem tudi $\angle RAQ + \angle RSQ =\alpha + \beta +\gamma =
180^0$. Tudi štirikotnik $ARSQ$ je tetiven (izrek
\ref{TetivniPogoj}) oz. ima svojo očrtano krožnico, ki je
pravzaprav  krožnica $k_A$, ki je očrtana trikotniku $AQR$.
To pomeni, da se krožnice $k_A$, $k_B$ in $k_C$ sekajo v točki $S$.
 \kdokaz

 V poglavju \ref{pogINV} bomo dokazali eno posplošitev prejšnje
 trditve (zgled \ref{MiquelKroznice}).



        \bnaloga\footnote{45. IMO Greece - 2004, Problem 1.}
          Let $ABC$ be an acute-angled triangle with $AB\neq AC$. The
circle with diameter $BC$ intersects the sides $AB$ and $AC$ at $M$ and $N$,
respectively. Denote by $O$ the midpoint of the side $BC$. The bisectors of
the angles $\angle BAC$ and $\angle MON$ intersect at $L$. Prove that the circumcircles
of the triangles $BML$ and $CNL$ have a common point lying on the side
$BC$.
         \enaloga


\begin{figure}[!htb]
\centering
\input{sl.skk.4.4.IMO1.pic}
\caption{} \label{sl.skk.4.4.IMO1.pic}
\end{figure}


\textbf{\textit{Proof.}} Označimo z $E$ presečišče simetrale kota
$BAC$ s stranico $BC$ trikotnika $ABC$ (Figure
\ref{sl.skk.4.4.IMO1.pic}). Dokažimo, da je $E$ iskana točka  oz.
da leži na očrtanih krožnicah obeh trikotnikov $BML$
        in $CNL$.

Ker iz konstrukcije točk $M$ in $N$ sledi $OM\cong ON$, je $OMN$
enakokraki trikotnik z osnovnico $MN$. To pomeni, da je simetrala
$OL$ kota $MON$ hkrati simetrala stranice $MN$ (sledi iz
skladnosti trikotnikov $MSO$ in $NSO$, kjer je $S$ središče
daljice $MN$). Torej točka $L$ leži na simetrali daljice $MN$
 trikotnika, zato po izreku \ref{TockaN} leži na očrtani krožnici
 $k$
 trikotnika $AMN$. Pogoj $AB\neq AC$ nam pove, da se simetrali kota $BAC$ in
 stranice $MN$ (oz. kota $MON$) razlikujeta, zato je njun presek
 točka.

  Če  uporabimo izreka \ref{TetivniPogojZunanji} in \ref{ObodObodKot},
 dobimo:
  \begin{eqnarray*}
   \angle BCA &\cong& AMN \cong\angle ALN,\\
   \angle ABC &\cong& ANM \cong\angle ALM.
  \end{eqnarray*}
Iz teh relacij in izreka  \ref{TetivniPogojZunanji} sledi, da sta
 $NLEC$ in $LMBE$ tetivna
štirikotnika. Torej točka $E$ leži na  očrtanih krožnicah
obeh trikotnikov $BML$
        in $CNL$.
 \kdokaz

%________________________________________________________________________________
  \poglavje{Tangential Quadrilateral} \label{odd4Tangentni}



Za večkotnik pravimo, da je
\index{štirikotnik!tangenten}\index{večkotnik!tangenten}\pojem{tangenten},
če za njega obstaja včrtana krožnica, oziroma če obstaja takšna
krožnica, da so nosilke vseh stranic večkotnika njene tangente
(Figure \ref{sl.skk.4.6.1.pic}). Ugotovili smo že, da je vsak
trikotnik tangenten (izrek \ref{SredVcrtaneKrozn}) in prav tako
je tangenten tudi vsak pravilni večkotnik (izrek
\ref{sredVcrtaneKrozVeck}). Po drugi strani pa je jasno, da vsi
večkotniki niso tangentni. Na primer pravokotnik je štirikotnik, ki nima
včrtane krožnice. V tem razdelku se bomo posebej ukvarjali s
tangentnimi štirikotniki.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.1.pic}
\caption{} \label{sl.skk.4.6.1.pic}
\end{figure}

Ker je kvadrat pravilni večkotnik, je tudi tangentni štirikotnik.
 Kako pa bi na
splošno ugotovili, ali je nek štirikotnik tangenten? Jasno je, da se
pri tangentnem štirikotniku (na splošno tudi večkotniku) simetrale
vseh njegovih notranjih kotov sekajo v eni točki (Figure
\ref{sl.skk.4.6.1.pic}). Ta pogoj je za tangentnost večkotnika tudi zadosten.
Žal pa ta pogoj ni preveč uporaben v
konkretnih primerih. Obstaja namreč uporabnejši pogoj, ki je za tangentnost štirikotnikov potreben in
hkrati zadosten.



             \bizrek \label{TangentniPogoj}
              A quadrilateral $ABCD$ is tangential if and only if
               $$|AB| + |CD| = |BC| + |AD|.$$

... (truncated 22858 lines) ...
```

**Note**: Source truncated for display. Full file is 32858 lines.

## High-Level Overview

Source file of type .tex.

## Detailed Analysis

File contains 32858 lines with structured content.

## Usage & Examples

See file content for usage details.

## Performance & Security Notes

📊 **Performance**: Contains nested loops - consider complexity
📊 **Performance**: Large file - may impact load times

## Related Files

**Same directory**:
- [geometry_English.tex](./geometry_English.tex_docs.md)

**Imported modules**:
- `a`
- `an`
- `any`
- `each`
- `its`
- `the`
- `these`
- `this`
- `triangle`
- `vertex`
- `which`

## Testing & Execution

See project documentation for testing procedures.

---
*Generated by Repo Book Generator v1.0.0*

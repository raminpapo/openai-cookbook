# Documentation: geometry_English.tex

## File Metadata
- **Path**: `examples/book_translation/data/geometry_English.tex`
- **Type**: .tex file
- **Size**: 1,583,983 bytes (1546.86 KB)
- **Lines**: 30,259
- **Words**: 202,898
- **Characters**: 1,583,315

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

\def\contentsname{Content}

\makeindex

\newcommand{\ch}{\mathop {\mathrm{ch}}}
\newcommand{\sh}{\mathop {\mathrm{sh}}}
\newcommand{\tgh}{\mathop {\mathrm{th}}}
\newcommand{\tg}{\mathop {\mathrm{tg}}}
\newcommand{\ctg}{\mathop {\mathrm{ctg}}}
\newcommand{\arctg}{\mathop {\mathrm{arctg}}}
\newcommand{\arctgh}{\mathop {\mathrm{arcth}}}

\def\indexname{Index}

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

We learn a lot of geometric concepts in elementary school, such as:
triangle, circle, right angle, etc. Later we also learn some
propositions: propositions about the congruence of triangles,
Pythagoras' and Tales' proposition. At the beginning we do not
prove the propositions, but we verify the facts based on several
individual examples. This way of reasoning is called inductive
method. Inductive method (lat. inductio -- introduction) is thus a
way of reasoning, in which we come to general conclusions from
individual examples. Later we start proving individual
propositions. Through these proofs we first encounter the so-called
deductive way of reasoning, or deduction. Deduction (lat. deductio
-- deduction) is a way of reasoning, in which we come from general
to individual conclusions. The idea of this method is thus to
deduce a general conclusion by proving it and then use it in
individual examples. Since we cannot verify all examples using
inductive method, because their number is usually infinite, we can
also come to wrong conclusions using this method. With deductive
method we always get correct conclusions, if the assumptions we
use in the proof are correct. Let us analyze both of these methods
using the following example. We try to come to the conclusion:
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

If we used inductive method, we would verify whether this proposition
is true in some individual examples; for example in the case when
the apex of the angle is in the center of the circle and similar
(Figure \ref{sl.sl.1.2.1.6.pic}). If we only deduced the general
conclusion from these individual examples, of course we could not
be sure that the proposition is not true in some example we did not
verify.

We will now use the deductive method. Let $AB$ be the radius of the circle with center $O$ and $L$ any point on this circle, different from points $A$ and $B$ (Figure \ref{sl.sl.1.2.1.6.pic}). We will prove that the angle $ALB$ is a right angle. Because $OA\cong OB\cong OL$, it follows that the triangles $AOL$ and $BOL$ are isosceles, therefore $\angle ALO\cong\angle LAO=\alpha$ and $\angle BLO\cong\angle LBO=\beta$. Then $\angle ALB=\alpha+\beta$. The sum of the interior angles in triangle $ALB$ is equal to $180^0$, therefore $2\alpha+2\beta=180^0$. From this it follows:
 $$\angle ALB=\alpha+\beta=90^0$$

We notice that in the case of using the deductive method or in the proof of the statement, we have not considered a certain point $L$ on the circle, but an arbitrary point (in general position). This means that the statement is valid for every point on the circle (except $A$ and $B$), if the proof is correct, of course. But is the proof correct? In this proof, we used the following two statements:
 \btrditev
 If two sides in a triangle are congruent, then the angles opposite the congruent sides are congruent angles.
 \etrditev
 \btrditev
  The sum of the interior angles of a triangle is equal to $180^0$.
   \etrditev
We also used concepts such as: isosceles triangle, angle congruence; in the statement itself, we also used the concepts: diameter, circle, angle over the diameter and right angle. In order to be sure that the statement we proved is true, we must be sure that the two statements we used in the proof are also true. In our case, we assume that we have already proved the aforementioned two statements and that we have introduced all the concepts mentioned. It is clear that this problem arises with every statement - even with the two on which we relied in the proof. This requires a certain systematization of the entire geometry. The question arises as to how to start if we again refer to previously proven statements in the proof of each statement. This process could then continue indefinitely. Thus we come to the need for initial statements - \index{aksiomi} \pojem{aksiomih}. The same applies to concepts - we need t. i. \pojem{začetni pojmi}.\index{začetni pojmi} In this way, each geometry (there can be more of them), which we consider, depends on the choice of initial concepts and axioms. We call this approach to building a geometry \pojem{sintetični postopek}, and we call the geometry itself \pojem{sintetična geometrija}\index{geometrija!sinteti\v{c}na}.


%________________________________________________________________________________
\poglavje{Basic Terms and Basic Theorems} \label{odd1POJMI}

In some theory (like geometry) we introduce every new
concept with a \index{definition} \pojem{definition}, which describes this concept
with the help
 of some initial or already defined concepts.
 The connections between concepts and their appropriate properties are given by
statements,
 which we call
\pojem{theory statements}. As we have already mentioned, we call the initial statements
\index{aksiomi} \pojem{aksiomi}, the statements derived from them
are  \pojem{izreki} of this theory. Formally,
\pojem{proof} \index{dokaz izreka} of some statement $\tau$ is a sequence of statements, which logically follow one
 from the other, each of which
is either an axiom or a statement derived from the axioms (izrek), and the last one in this
sequence is precisely the statement $\tau$.

 Although the choice of axioms is not uniquely determined, it cannot be arbitrary.
 When making this choice
we must be careful not to lead to contradictory statements
or to a contradiction. This means that, for a given choice of
axioms, there is no such statement that both the statement and its
negation are izreki in this theory. We also need enough
axioms so that we can determine, for every statement that we can formulate in this
theory, whether it is true or not. This means that
either the statement or its negation is an izrek in this theory. For a system of axioms that satisfies the first requirement, we say that it is
\index{sistem aksiomov!neprotisloven} \pojem{neprotisloven}, for one that satisfies the second requirement, we say that it is \index{sistem
aksiomov!popoln} \pojem{popoln}. When choosing axioms, there is also a third requirement -- that the system of axioms is \index{sistem
aksiomov!minimalen} \pojem{minimalen}, which means that none of the axioms can be derived from the others. We mention that the last
 requirement is not as important as the first two.

We must also add that we do not build Euclidean geometry
independently from algebra and logic. We will use concepts such as
set, function, relation with properties that apply to them. We will
also use so-called rules of inference, such as
the method of contradiction. For mathematical disciplines that we use in this way to build geometry, we say that they are
\pojem{predpostavljene teorije}.

%________________________________________________________________________________
\poglavje{A Brief Historical Overview of the Development of Geometry}
\label{odd1ZGOD}

People started dealing with geometry in early history.
At first, it was only the observation of characteristic shapes, such as
a circle or a square. Based on the drawings found on the walls of old caves, we conclude
that people in prehistory were interested in the symmetry of shapes.

In further development, man was discovering various properties
of geometric shapes. This was due to practical needs, e.g.
measuring the area of ​​land - which is also how the word
"geometry" came about. In this period, geometry developed as
an inductive science. This means that geometric propositions were coming from experiences - by means of measurements and checking on
individual examples. In this sense, geometry was developed by
all ancient civilizations: Chinese, Indian and especially
Egyptian.

In Egypt, geometry developed mainly as a study of
measurements. Because the Nile river often flooded,
the land had to be measured very often. In addition,
the knowledge of geometry was used in construction. They knew
e.g. the formula for calculating the volume of a pyramid and a truncated
pyramid, although they came to it empirically. So geometry was for
the Egyptians primarily a pragmatic discipline.
The oldest records date back to approximately 1700 BC.

Geometry of three-dimensional space was not
discussed as much as in Egypt.

There is not as much data on Chinese geometry as on Egyptian,
although we know that it was also very developed. In
the oldest preserved records we find a description of the calculation of
the volume of a prism, pyramid, cylinder, cone, truncated pyramid and
truncated cone.

Indian geometry is much younger than the previous three. It dates
back to approximately the 5th century BC. In it we already see the first
attempts at proof. Later it developed parallel to
Greek geometry.

The turning point in the development of geometry took place in Ancient Greece. This is when the deductive method was first used in geometry. The first geometric proofs are associated with Tales\footnote{The Ancient Greek philosopher and mathematician \textit{Tales} \index{Tales} from Miletus (640--546 BC).}. We connect his name with the well-known statement about the proportionality of segments in parallel lines. He also proved the statement that the angles above the diameter of a circle are right, even though this claim was known without proof to the Babylonians 1000 years earlier. This way of developing geometry was continued by other Ancient Greek philosophers, of which Pythagoras\footnote{The Ancient Greek philosopher and mathematician \textit{Pythagoras} \index{Pythagoras} from the island of Samos (ca. 580--490 BC).} was one of the most important. Of course, his \index{statement!Pythagorean}\textit{Pythagorean statement} is famous. However, the Egyptians knew this statement as a fact 3000 years BC (maybe the statement was known even before that), but Pythagoras gave the first known proof. Archimedes\footnote{The Ancient Greek philosopher and mathematician \textit{Archimedes} \index{Archimedes} from Syracuse (287--212 BC).} was the first to present a theoretical calculation of the number $\pi$, by considering the inscribed and circumscribed polygons with $96$ sides. The statements about the congruence of triangles were also proven. With the rapid progress of geometry, reflected in the large number of proven statements, the need for systematization and, with that, the need for axioms, became apparent. The need for axioms was first described by Plato\footnote{The Ancient Greek philosopher and mathematician \textit{Plato} \index{Plato} (427--347 BC).} and Aristotle\footnote{The Ancient Greek philosopher and mathematician \textit{Aristotle} \index{Aristotle} from Athens (384--322 BC).}. Plato is also known in mathematics for his research of regular polygons: the tetrahedron, the cube, the octahedron, the dodecahedron and the icosahedron, which is why we also call them Platonic solids after him.

One of the first attempts at an axiomatic approach to geometry - and the only one that has been preserved from that time - was made by the most famous mathematician of that time, Euclid, Plato's student, in his well-known work \textit{The Elements}, which consists of 13 books. In it, he systematized all the existing knowledge of geometry. He divided the initial statements into axioms and so-called postulates, of which the latter are purely geometric content (today we also call them axioms). \textit{The Elements} became one of the most important and influential books in the history of mathematics. The geometry, which he developed in this way, with minor unimportant changes, is the one that is taught in schools today. Proofs, such as the one about the central and peripheral angle, have been preserved in practically unchanged form. We give the postulates as Euclid gave them (Figure \ref{sl.sl.1.3.1.9.pic}):
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


However, the system of axioms that Euclid gave was not perfect. In some proofs, he took certain parts as obvious and did not prove them. Of course, we should not be too critical, because this was a revolutionary work for those times. \textit{The Elements} were an example and inspiration for mathematicians for centuries and laid the foundations for the further development of geometry to this day. The last axiom, i.e. the \index{aksiom!fifth Euclid's axiom} \pojem{fifth Euclid's axiom}, was particularly important for the further development of geometry. The problem of its independence from the other axioms was open for the next 2000 years!

The last in a series of great ancient Greek mathematicians were
Apolonius\footnote{The Greek mathematician \textit{Apolonius}
\index{Apolonius} from Perga (262--190 BC).},
Menelaus\footnote{The Greek mathematician \textit{Menelaus}
\index{Menelaus} from Alexandria
  (ca. 70--130).} and Pappus\footnote{The Greek mathematician \textit{Pappus}
  \index{Pappus} from
  Alexandria (ca. 290--350).}. In his book \textit{On the Cutting of a Cone}, Apolonius defined the ellipse, parabola and hyperbola as the intersections of a plane and a circular (infinite) cone. This allowed him to consider their properties simultaneously, which was quite a modern approach for the time. Menelaus and Pappus proved certain theorems which didn't become relevant until the 19th century with the development of projective geometry. So the ideas of these three mathematicians were quite modern and in a way we can say that they were on the brink of discovering the first non-Euclidean geometry.

After the final fall of the Old Greece under the Roman Empire,
the period of the glorious ancient Greek geometry came to an end. Although the Old Romans took over a large part of the ancient Greek culture and built roads,
aqueducts and so on, it is interesting that they never really showed much interest in
the ancient theoretical mathematics. So their contribution to the development
of geometry is very modest.

An important role in the further development of geometry was taken over by the Arabs.
First of all, we should say that all the works of the Ancient Greeks
including Euclid's \textit{Elements} are known to us today because they
were translated and thus preserved by the Arabs. After the foundation of
Baghdad in 762, in the next 100 years they translated most of the works
of ancient Greek and Indian mathematics. They also made a synthesis
of ancient Greek mostly geometric and Indian mostly
algebraic approach. We mention that the word itself \pojem{algebra}
is of Arabic origin. In addition, the Arabs continued the development
of \pojem{trigonometry}, which was designed by the Ancient Greeks. A. R. al-Biruni\footnote{The Arab mathematician \textit{ A. R. al-Biruni} \index{al-Biruni, A. R.} (973--1048).} proved the now known \pojem{sine theorem}.

The development of geometry in Europe began in the 12th century, when
Arabic and Jewish mathematicians brought their knowledge to
Spain and Sicily. (Euclid's \textit{Elements} were translated from
Arabic into Latin around 1200); but Europe did not experience its
true flowering until the 16th century. In the Middle Ages,
mathematics developed very slowly. In the Middle Ages,
Western European mathematicians only learned the Greek geometric
heritage from Arabic translations, but this process was not
quick. When this knowledge was accumulated and social and
political conditions changed, a new era began in the
development of geometry. The first new results were given by Italian
mathematicians of that time, who paid a lot of attention to
constructions using a ruler and a compass.

As we mentioned earlier, Euclid's fifth axiom had a very big impact on
the further development of geometry. Because of its
formulation, which is not as simple as the previous axioms, and
also because of its importance, many mathematicians of that time
thought that it did not need to be considered as an axiom, but it
could be proven as a theorem with the other axioms. If we read
Euclid's other initial propositions, it is really true that the
fifth axiom is more complex. The problem of the independence of the
fifth axiom from the others occupied many
mathematicians in the following centuries. Until the second half of
the 19th century the problem was not solved. In many attempts to
prove the fifth axiom from the others, propositions were used,
whose proof was omitted.
It was later shown that these propositions could not even be
proven from the other axioms if the fifth axiom was omitted from the
list.
Just as they follow from the fifth axiom, these propositions
also follow from the fifth axiom (of course using the other
axioms).
We therefore call them \pojem{equivalents of the fifth Euclidean
axiom}.
We give some examples of these equivalents (Figure
\ref{sl.sl.1.3.1.9a.pic}):

\color{blue}
\begin{ekv}
If $ ABCD $ is a quadrilateral with two right angles on the side $BC$
and the sides $AB$ and $CD$ are congurent, then the two remain angles
of this quadrilateral are also right angles.\footnote{This equivalent was set by
Italian mathematician \index{Saccheri, G. G.} \textit{G. G.
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
H. Lambert} (1728--1777), French mathematician.}
\end{ekv}
\begin{ekv}
The sum of the interior angles in every triangle is $180^0$.\footnote{\index{Legendre, A. M.} \textit{A. M. Legendre}
(1752--1833), French mathematician.}
\end{ekv}
\begin{ekv}
For any given line $p$ and point $A$ not on $p$, in the plane containing both line $p$ and point $A$ there is just one line
 through point $A$ that do not intersect line $p$\footnote{\index{Playfair, J.} \textit{J. Playfair}
(1748--1819), Scottish mathematician.}.
 \end{ekv}
\normalcolor


\begin{figure}[!htb]
\centering
\input{sl.1.3.1.9a.pic}
\caption{} \label{sl.sl.1.3.1.9a.pic}
\end{figure}

So mathematicians were able to prove the fifth Euclidean axiom with
the help of each of these assertions, but eventually it turned out that
none of them could be proved without the fifth axiom. Therefore,
these assertions, as we have already mentioned, are equivalent to the fifth axiom.
Today, Playfair's equivalent is most commonly used, which was later
added to Euclid's axioms instead of the fifth axiom.

But how did mathematicians find out that the fifth Euclidean axiom could not
be derived from the other axioms? Just the fact that they were not able
to prove it did not mean that it was not possible. The answer to this
question came at the end of the 19th century and, as we will see,
brought much more to the development of geometry than just the fact of
the unprovability of the fifth axiom.

The next breakthrough in the development of geometry was the discovery
\index{geometrija!neevklidska}\pojem{non-Euclidean geometries} in the 19th century. For the beginning of this development
we count N.~I.~Lobačevskega\footnote{\index{Lobačevski, N.
I.}\textit{N. I. Lobačevski} (1792--1856), Russian mathematician.}. He also dealt with the problem of the independence of the fifth Euclidean axiom.
Based on its negation or the negation of Playfair's equivalent statement, Lobačevski postulated that through a point that does not lie on a straight line, there are at least two straight lines that do not intersect with that line and are coplanar. In an attempt to come to a contradiction (thus the fifth axiom would be proven), he built a whole
sequence of new statements. One of them, for example, is that the sum of the interior angles
of a triangle is always less than the extended angle. But none of these statements
were in contradiction with the other axioms, if of course we exclude
the fifth Euclidean axiom from the list. From this he got the idea that it is possible to build
a completely new geometry that is non-contradictory and based on all
Euclidean axioms except the fifth, which we replace with its
negation. Today we call this geometry
\index{geometrija!hiperbolična} \pojem{hyperbolic geometry}
or \pojem{Lobačevski geometry}.

Independently of Lobačevski, J.
Bolyai\footnote{\index{Bolyai, J.} \textit{J. Bolyai} (1802--1860),
Hungarian mathematician.}. As it often happens, the ideas of Lobačevski during his lifetime
unfortunately were not accepted. The complete confirmation of these ideas
or the proof of the non-contradiction of this new geometry was at the end of the 19th century, that is, only after the death of Lobačevski, presented by A.
Poincar\'{e}\footnote{\index{Poincar\'{e}, J. H.} \textit{J. H.
Poincar\'{e}} (1854--1912), French mathematician.}.
Poincar\'{e} built a model on
the basis of which he showed that a possible contradiction of Lobačevski geometry
would at the same time be a contradiction of Euclidean geometry.
Later, the discovery of other non-Euclidean geometries followed.

Although at the end of the 19th and the beginning of the 20th century the system of Euclid's geometry axioms was already almost completely built, the first correct and complete system was given by D. Hilbert\footnote{\index{Hilbert, D.} \textit{D. Hilbert} (1862--1943), German mathematician.} in his famous book \textit{The Foundations of Geometry}, published in 1899. We use a very similar system of axioms in an almost unchanged form even today.

Parallel to the research of the fifth Euclid's axiom and the development of non-Euclidean geometries, other important methods have also emerged in the study of geometry. As early as around 1637, R. Descartes\footnote{\index{Descartes, R.} \textit{R. Descartes} (1596--1650), French mathematician.} in his book \textit{Geometry} showed that every point in a plane can be described by a suitable pair of two real numbers and similarly in space as a triple of three real numbers. He connected this with the concept of a coordinate representation of the dependence of one quantity (function) on another (variable), which was known earlier. Today, we call such a way of determining points in space after him \pojem{Cartesian coordinate system}. Lines and planes can then be described as sets of solutions of appropriate linear equations, where the unknowns are coordinates of points.

Thus, under the influence of the ideas of F. Vi\'{e}te\footnote{\index{Vi\'{e}te, F.} \textit{F. Vi\'{e}te} (1540--1603), French mathematician.}, Descartes and P. Fermat\footnote{\index{Fermat, P.} \textit{P. Fermat} (1601--1665), French mathematician.}, the two very important mathematical disciplines began to develop - first \index{geometry!analytical} \pojem{analytical geometry}, then \index{linear algebra} \pojem{linear algebra}, which represent the connection between algebra and geometry. The further development of these two disciplines allowed the development of \index{geometry!multidimensional} \pojem{multidimensional geometry}, in which spaces of dimensions greater than three can be considered, because in algebra there are no such limitations as we have in the geometric perception of space. Thus, we can define the so-called \pojem{polytope} - objects of multidimensional space, which are the analogy of two-dimensional polygons and three-dimensional polyhedrons.

Later, the discovery of other non-Euclidean geometries followed.
In the 19th century, the so-called \index{geometrija!projektivna}\pojem{projective geometry} developed, but
its development was not axiomatic like in hyperbolic
geometry; the appropriate system of axioms was set only
later. In this geometry, there are no lines in the plane that do not intersect.

One of the first motives for the beginning of the
 development
 of projective geometry originates from painting or from the desire to transfer
 the feeling of three-dimensional space into a plane. Already in very
 early painting, we encounter a very important property--that
 in the picture, parallel lines are represented as lines that intersect.

 In the 15th century, Italian artists were very interested in
 the geometry of space. The theory of perspective was first considered by F.
 Brunellechi\footnote{\index{Brunellechi, F.} \textit{F.
 Brunellechi} (1377--1446), Italian architect.} in 1425.
   His work was continued by L. B. Alberti\footnote{\index{Alberti, L. B.}
  \textit{L. B.
 Alberti} (1404--1472), Italian mathematician and painter.} and A.
 D\"{u}rer\footnote{\index{D\"{u}rer, A.} \textit{A.
 D\"{u}rer} (1471--1528), German painter.}. Alberti's book from
 1435 represents the first presentation of central projection.

 For the beginning of the development of projective geometry as a mathematical
 discipline, we consider the period when
 J. Kepler\footnote{\index{Kepler, J.} \textit{J. Kepler} (1571--1630),
  German astronomer.}  and G. Desargues\footnote{\index{Desargues, G.}
  \textit{G. Desargues}
 (1591--1661), French architect.}
 independently introduced the concept of points at infinity.
  Kepler showed that a parabola has two foci, one of which
   is a point at infinity. Desargues
 was writing in 1639: ‘‘Two parallel lines have a common endpoint at
 an infinite distance.’’ In 1636, he wrote a book on perspective,
 and in 1639, he wrote about cones. The famous \textit{Desargues' Theorem}
 was published  in 1648.

With the further development of projective geometry we connect French mathematics.
  The genius B. Pascal\footnote{\index{Pascal, B.} \textit{B. Pascal} (1623--1662),
  French philosopher and mathematician.} was
  already as a sixteen year old when he proved an important theorem about
  cones, which we today call \textit{Pascal's theorem}.
  This theorem, which is one of the basic
  theorems of projective geometry, was published in 1640.
  G. Monge\footnote{\index{Monge, G.} \textit{G. Monge}
  (1746--1818), French mathematician.}
  was among the first mathematicians who we can consider a specialist; he
  is in fact the first true geometer. He developed \pojem{descriptive geometry} as
  a special discipline. In his research in descriptive geometry
  we find many ideas of projective geometry.
  The most original Monge's student was
  J. V. Poncelet\footnote{\index{Poncelet, J. V.}
  \textit{J. V. Poncelet} (1788--1867), French mathematician.}.
  Although Pappus\footnote{\index{Pappus} \textit{Pappus of Alexandria} (3rd century), Greek mathematician.}
  discovered the first projective theorems, Poncelet
  with a completely projective way of reasoning proved them only in the 19th century.
  In 1822
  Poncelet published his famous "Treatise on the projective properties of figures",
  in which all the important concepts characteristic for
  projective geometry appear: harmonic quadruple, perspectivity, projectivity,
  involution, etc. Poncelet introduced a line at infinity for all
  planes that are parallel to a given plane. Poncelet and J. D.
  Gergonne\footnote{\index{Gergonne, J. D.} \textit{J. D. Gergonne} (1771--1859), French mathematician.} independently
  from each other studied duality in projective geometry,
  C.~J.~Brianchon\footnote{\index{Brianchon, C. J.} \textit{C. J. Brianchon}
   (1783--1864), French mathematician.} however
 proved a theorem which is dual to Pascal's theorem.
 M.~Chasles\footnote{\index{Chasles, M.} \textit{M. Chasles} (1793--1880), French mathematician.} was the last of
  the great
 school of
 French projective  geometers of that time.

A typical representative of so-called pure geometry
 (today we would say synthetic geometry) was
 J. Steiner\footnote{\index{Steiner, J.} \textit{J. Steiner}
 (1796--1863),
 Swiss mathematician.}.
 Steiner developed projective geometry very systematically,
  from perspective to projectivity and then to conics.

 In the middle of the 19th century, German mathematicians took over the lead in the development of projective geometry. They advocated a synthetic approach
 h geometry. All mathematicians until then had designed projective geometry
  based on Euclidean metric geometry -- by adding
  points at infinity. But C.~G.~C.~Staudt
  \footnote{\index{Staudt, K. G. C.} \textit{C. G. C. Staudt} (1798--1867),
  German mathematician.}
   was the first to try to make it independent and
    design it only on incidence axioms, without the help of metric.
    This led to the abolition of the difference between points at infinity and ordinary
     points
    or the transition from extended Euclidean to projective space.

  F. Klein\footnote{\index{Klein, F. C.} \textit{F. C. Klein} (1849--1925), German mathematician.} set the projective geometry on algebraic foundations in 1871
   with the help of
    so-called \pojem{homogeneous coordinates}, which were discovered independently of each other in 1827,
     by K. W. Feuerbach\footnote{\index{Feuerbach, K. W.} \textit{K. W. Feuerbach}
      (1800--1834), German mathematician.}
      and A. F. M\"{o}bius\footnote{\index{M\"{o}bius, A. F.} \textit{A. F. M\"{o}bius}
       (1790--1868), German mathematician.}.
     A. Cayley\footnote{\index{Cayley, A.} \textit{A. Cayley} (1821--1895), English mathematician.} and
     Klein
     found the use of projective geometry in other non-Euclidean geometries.
     They discovered the model of hyperbolic geometry and models of other geometries
     in projective.

   The first to completely axiomatically design projective geometry, were
    G. Fano\footnote{\index{Fano, G.} \textit{G. Fano} (1871--1952), Italian mathematician.}
     in 1892 and M. Pieri\footnote{\index{Pieri, M.} \textit{M. Pieri} (1860--1913), Italian mathematician.}
      in 1899.

Because of its relative simplicity, the development of classical
(synthetic) projective geometry was almost completed by the end of
the 19th century. Its development today continues within the framework
of other theories -- especially in algebra and algebraic geometry as
$n$-dimensional projective geometry.

G. F. B. Riemann\footnote{\index{Riemann, G. F. B.} \textit{G. F.
B. Riemann} (1828--1866), German mathematician.} defined the space of
arbitrary dimension in his book \textit{On the hypotheses which lie at
the foundations of geometry}, which is not always of constant
curvature. After him, we today call it the \pojem{Riemann metric
space}\index{Riemann spaces}. Euclidean geometry is then obtained as a
special case: if the curvature is constant and equal to 0; hyperbolic
geometry is obtained if we choose that the curvature is constant and
negative. If the curvature is constant and positive, we obtain the so-
called \index{geometry!elliptic} \pojem{elliptic geometry}. The latter
geometry is actually projective geometry, if we add a metric to it.
This research was also the beginning of the development of a new
discipline in mathematics, namely the \index{geometry!differential}
\pojem{differential geometry}.

If we think about non-Euclidean geometries, it may seem strange to us
that in mathematics there can be considered more different theories,
such as Euclidean geometry and hyperbolic geometry, which are in
contradiction with each other. For modern mathematics, it is most
important that both geometries are determined by systems of axioms,
which are (each for itself) consistent and complete. To the question
of which of these two geometries is valid, it is pointless to seek an
answer within mathematics. This is because it depends on which
axioms we have chosen. Such a question would be the same as the
question of which axioms are valid. But the axioms are assumed by
definition without proof. Of course, we can ask the question of what
the geometry of space is in the physical sense and how we can describe
it with axioms."

To answer this question, a physical interpretation of the basic geometric concepts is needed. For example, it is most natural to interpret a line as a ray of light. In this sense, physical space is not Euclidean. It is not even determined by hyperbolic geometry. With the advent of Einstein's\footnote{\index{Einstein, A.} \textit{A. Einstein} (1879--1955), famous German physicist.} theory of relativity at the beginning of the 20th century, it turned out that in space of cosmic dimensions it is more convenient to use non-Euclidean geometry with variable curvature (Riemann metric spaces!). We can say that the geometry of the universe is locally different in each point, depending on the proximity and size of some mass. Einstein's theory also tells us that space and time are interrelated and that time (which is of course surprising) does not flow evenly in each point of the universe. In connection with the mentioned connection of space and time, the so-called \pojem{Minkowsky space of four dimensions}\footnote{This space was discovered by \index{Minkowsky, H.} \textit{H. Minkowsky} (1864--1909), German mathematician.} is important.

Since the 20s of the 20th century and the development of the theory of the primordial soup, we know that the universe is not static and that it is expanding. Its destiny depends on what geometry globally describes it best. But we still do not know for sure what the shape of the universe is or what its destiny is. We do not even know if the universe is finite or infinite. As S. Hawking writes in his famous popular book from 1988 A Brief History of Time (\cite{KratkaZgodCasa}), the universe may even be finite and unlimited. The latter seems paradoxical, although we can imagine it if, instead of three-dimensional, we imagine a "two-dimensional universe". So the beings of this two-dimensional universe could once find out that their universe is actually not a plane but a sphere that is finite but unlimited. The sphere is part of three-dimensional space. So we can theoretically imagine the universe as a three-dimensional sphere in four-dimensional space. The three-dimensional sphere is one of the 3-manifolds. In this case, the geometry of the universe would be globally elliptical.

Although the question of the shape and destiny of the universe is a question of theoretical physics and cosmology, we see how modern geometry (non-Euclidean geometry, geometry of multi-dimensional spaces, etc.) is closely related to this problem (\cite{Oblika}). It is important to understand that geometry (and every other mathematical discipline) develops and is treated as an abstract discipline in which physical interpretations are only inspiration - in this sense, only axioms and initial concepts remain on which we then build mathematical theory.

At the end, we mention another one of the most important geometers of the 20th century H. S. M. Coxeter\footnote{\index{Coxeter, H. S. M.}
\textit{H. S. M. Coxeter} (1907--2003), Canadian mathematician. One
of the greatest geometers of the 20th century.}. Coxeter further researched polytopes in arbitrary dimensions, primarily regular polytopes. In addition, he
was mostly occupied with groups of isometries in hyperbolic geometry and
with multidimensional hyperbolic geometry.

It needs to be added that with everything
that we have
said, the development of geometry is far from over. Quite the opposite -- contrary to the usual
perception -- geometry and mathematics in general are now developing
even faster than ever before. Even today, there are in mathematics (in geometry in particular from the non-Euclidean
geometries) many
problems that are still unresolved.







% DEL 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
%  AKSIOMI RAVNINSKE EVKLIDSKE GEOMETRIJE
%________________________________________________________________________________


\del{Axioms of Planar Euclidean Geometry} \label{pogAKS}

In what follows, we will illustrate the axiomatic design of planar Euclidean
geometry. We will list the initial concepts and initial statements -
axioms, and then derive some new concepts and statements.
We mention that we have chosen the axioms of the plane, because in this book
we will only deal with the geometry of the Euclidean plane.

Let $\mathcal{S}$ be a non-empty set. Its elements are called
\index{point} \pojem{points} and we denote them with $A, B, C, \ldots$
Certain subsets of the set $\mathcal{S}$ are called \index{line}
\pojem{lines} and we denote them with $a, b, c, \ldots$ The set
$\mathcal{S}$ (the set of all points) is also called the
\index{plane} \pojem{plane}. In addition to these basic concepts,
there are also two relations on the set $\mathcal{S}$. The first is
the \index{relation!$\mathcal{B}$} \pojem{relation $\mathcal{B}$}
and it applies to three points. The fact that points $A$, $B$ and $C$
are in this relation, we will denote with $\mathcal{B}(A,B,C)$ and
read: Point $B$ is between points $A$ and $C$. The second is the
\index{relation!compatibility of point pairs} \pojem{relation of
compatibility of point pairs}; the fact that pairs of points $A, B$
and $C, D$ are in this relation, we will denote with $(A,B) \cong
(C,D)$ and read: The pair of points $(A,B)$ is compatible with the
pair of points $(C,D)$.

 With the help of the aforementioned basic concepts, we can
also define the following derived concepts:

If point $A$ belongs to line $p$ ($A\in p$), or line $p$ contains
point $A$ ($p\ni A$), we will say that
 point $A$\index{relation!lies on a line} \pojem{lies on} line $p$, or that line $p$ \index{relation!goes through a point}\pojem{goes
 through} point $A$.
 For three or
more points we say that they are \index{collinear points}\pojem{collinear},
if they lie on the same line, otherwise they are
\index{non-collinear points}\pojem{non-collinear}. Two
different lines \pojem{intersect}, if their intersection (the
intersection of two subsets) is not an empty set. We call their
intersection the \index{intersection of two lines} \pojem{intersection} of two lines. Any non-empty subset $\Phi$ of the set $\mathcal{S}$ ($\Phi\subset\mathcal{S}$) is called a \index{figure} \pojem{figure}. We say that figures $\Phi_1$ and $\Phi_2$ \index{figures!coincide}\pojem{coincide} (or they are \index{figures!identical}\pojem{identical}), if $\Phi_1=\Phi_2$.

 Now we will
also list some basic theorems - axioms. By their nature, they are
divided into five groups:

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

 Because lines as basic notions represent certain sets of points,
 we can
consider appropriate relations between elements
and sets
of points and lines: $\in$ and $\ni$ - relations we also call
\index{relacija!incidencije}\pojem{relations of incidence}. These axioms describe just the basic properties of these relations  (Figure
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



 From the first two axioms \ref{AksI1} and \ref{AksI2} it follows that each line is determined by
 its two distinct points. Therefore
the line $p$, which is determined by the points $A$ and $B$, we also call the line $AB$.

 From the first axiom \ref{AksI1} it follows that the intersection of two
 lines that intersect is one point. If, for example, two lines
 had one more common point, according to this axiom they would coincide (they would be identical),
 but in the definition of lines that intersect, we required
 that
they are different.
 The fact that the lines $p$ and $q$ intersect in the point $A$, we will
 write $p\cap q=\{A\}$ or shorter $p\cap q=A$ (Figure \ref{sl.aks.2.1.2.pic}).



\begin{figure}[!htb]
\centering
\input{sl.aks.2.1.2.pic}
\caption{} \label{sl.aks.2.1.2.pic}
\end{figure}



The third axiom \ref{AksI3} can also be expressed as follows: There exist
at least three  points that are not collinear.

So we deduced the first consequences of the incidence axioms;
 for simplicity, we did not express them in the form of propositions. These are almost all the consequences that arise from the first group of axioms.
 Because of this, geometry, which is based solely on the axioms of incidence,
 is too simple. In it, we could only prove the existence of three points and three
 lines. So we need new axioms.



%________________________________________________________________________________
 \poglavje{Ordering Axioms}
 \label{odd2AKSURJ}

The axioms in this group describe the basic characteristics of the relation
$\mathcal{B}$, which we listed as the basic concept.
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
        (1843--1930), German mathematician, who introduced the concept of ordering points
        in his 'Lectures on Modern Geometry' from 1882. These
        axioms were later supplemented by Italian mathematician \index{Peano, G.} \textit{G. Peano}
        (1858--1932), in 'Principles of Geometry', then by German mathematician
        \index{Hilbert, D.}\textit{D. Hilbert} (1862--1943) in his famous book
         'Foundations of Geometry' from
        1899.} axiom)
        Let $A$, $B$ and $C$ be three noncollinear points and $l$ be a line that does not contain point $A$.
        If there is a point $P$ on $l$ that is $\mathcal{B}(B,P,C)$ then either $l$ contains a point $Q$ that is  $\mathcal{B}(A,Q,C)$ or $l$ contains a point $R$ that is $\mathcal{B}(A,R,B)$ (Figure \ref{sl.aks.2.2.4.pic}).
        \eaksiom


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.4.pic}
\caption{} \label{sl.aks.2.2.4.pic}
\end{figure}


In the previous axiom, we did not particularly emphasize that the line $l$ lies in the plane $ABC$, because we are building a plane Euclidean geometry, where all points lie in the same plane.

 At this point we will not derive all the consequences of the ordering axioms.
The formal derivation of all the facts is not so simple and would take up a lot of space. Most of the proofs can be found in \cite{Lucic}.

We prove the first consequence of the ordering axioms.


        \bizrek \label{izrekAksUrACB}
        Given a pair of distinct points $A$ and $B$ there is a point $C$, so that
        is $\mathcal{B}(A,C,B)$.
        \eizrek


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.5.pic}
\caption{} \label{sl.aks.2.2.5.pic}
\end{figure}

\textbf{\textit{Proof.}} By Axiom \ref{AksI1} there exists exactly one line that goes through points $A$ and $B$ - we'll mark it with $AB$.
By Axiom \ref{AksI3} there are at least three non-linear points.
Therefore, there is at least one point outside of line $AB$ - we'll mark it with $D$
  (Figure \ref{sl.aks.2.2.5.pic}). Next, by
Axiom \ref{AksII3} there is such a point $E$, that $\mathcal{B}(B,D,E)$ is true, and then such a point $F$, that $\mathcal{B}(A,E,F)$ is true. $A$, $B$ and $E$ are non-linear points,
because otherwise point $D$ would lie on line $AB$ (Axiom \ref{AksI1}).
Line $FD$ does not go through point $A$, because by Axiom \ref{AksI1} points $F$, $D$, $A$ and $E$
would be linear, and so would point $B$. But that is not possible, because it would imply that point $D$ lies on line $AB$.
We'll now use Pasch's Axiom \ref{AksPascheva} on
points $A$, $B$ and $E$ and line $FD$. Line $FD$ intersects line $EB$ in such a point $D$,
that $\mathcal{B}(B,D,E)$ is true, and therefore it intersects either line $AE$ in such a point $F$, that $\mathcal{B}(A,F,E)$ is true, or
line $AB$ in such a point $C$, that $\mathcal{B}(A,C,B)$ is true. But since $\mathcal{B}(A,E,F)$ is already true, by Axiom \ref{AksII2} $\mathcal{B}(A,F,E)$ cannot be true as well. Therefore line $FD$ intersects
line $AB$ in such a point $C$, for which $\mathcal{B}(A,C,B)$ is true.
\kdokaz

Relation $\mathcal{B}$ and the order axioms related to it, allow us to define new concepts.


 Let $A$ and $B$ be any two different points.
  \index{distance!open}\pojem{Open distance} $AB$ with notation $(AB)$ is the set of all points
  $X$, for
  which $\mathcal{B}(A,X,C)$ is true (Figure \ref{sl.aks.2.2.6.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6.pic}
\caption{} \label{sl.aks.2.2.6.pic}
\end{figure}

If we add points $A$ and $B$ to an open line segment $AB$, we get a \pojem{line segment} (or a \pojem{closed line segment}) $AB$, which we also denote with $[AB]$. Points $A$ and $B$ are its \pojem{endpoints}, and all other points on it are \pojem{interior points} of the line segment (Figure \ref{sl.aks.2.2.6.pic}). More formally: a line segment (or a closed line segment) is the union of an open line segment and the set $\{A,B\}$ or $[AB]=(AB)\cup \{A,B\}$.

Similarly, we define a \pojem{half-open line segment}: $(AB]=(AB)\cup \{B\}$, or $[AB)=(AB)\cup \{A\}$ (Figure \ref{sl.aks.2.2.6a.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6a.pic}
\caption{} \label{sl.aks.2.2.6a.pic}
\end{figure}

  From Axiom \ref{AksII1} it follows immediately that line segments $AB$ and $BA$ are the same. From the same axiom it also follows that line segment $AB$ is a subset of the line $AB$. Therefore, we say that line segment $AB$ \pojem{lies on the line} $AB$, and we call the line $AB$ the \pojem{line supporting the line segment} $AB$  (Figure \ref{sl.aks.2.2.6b.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6b.pic}
\caption{} \label{sl.aks.2.2.6b.pic}
\end{figure}

By Theorem \ref{izrekAksUrACB}, line segment $AB$ has, besides its endpoints $A$ and $B$, at least one more point $C_1$. In this way, we can get an infinite sequence of points $C_1$, $C_2$, ..., for which $\mathcal{B}(A, C_n, C_{n-1})$ is true ($n\in \{2,3,\cdots\}$)  (Figure \ref{sl.aks.2.2.6c.pic}). At this point, we will not formally prove the fact that all points in the sequence are different and that all of them lie on line segment $AB$. From this statement it follows that every line segment (and consequently every line) has infinitely many points.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6c.pic}
\caption{} \label{sl.aks.2.2.6c.pic}
\end{figure}

Let's define the relation $\mathcal{B}$, which relates to more than three collinear points. We say that $\mathcal{B}(A_1,A_2,\ldots,A_n)$ ($n\in\{4,5,\ldots\}$), if for every $k\in\{1,2,\ldots,n-2\}$ it holds that $\mathcal{B}(A_k,A_{k+1},A_{k+2})$ (Figure \ref{sl.aks.2.2.6d.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.6d.pic}
\caption{} \label{sl.aks.2.2.6d.pic}
\end{figure}

 Let $S$ be a point that lies on the line $p$. On the set $p\setminus \{S\}$ (all points of the line $p$ without the point $S$) we define two relations.
We say that the points $A$ and $B$ ($A,B\in p\setminus \{S\}$) \index{relacija!na različnih straneh točke} \pojem{on different sides of the point} $S$ (which we denote by $A,B\div S$), if $B(A,S,B)$, otherwise the points $A$ and $B$ ($A,B\in p\setminus \{S\}$) \index{relacija!na isti strani točke} \pojem{on the same side of the point} $S$ (which we denote by $A,B\ddot{-} S$). So for points $A,B\in p\setminus \{S\}$ it holds that $A,B\ddot{-} S$, if it is not $A,B\div S$  (Figure \ref{sl.aks.2.2.7.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.7.pic}
\caption{} \label{sl.aks.2.2.7.pic}
\end{figure}


Let $A$ and $B$ be two different points. The set of all such points $X$, for which $B,X\ddot{-} A$ including the point $A$, we call \index{poltrak}\pojem{poltrak} $AB$ with \pojem{starting point} or \pojem{origin} $A$. The line $AB$ is
\index{nosilka!poltraka}  \pojem{the carrier of the poltrak} $AB$ (Figure \ref{sl.aks.2.2.8.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.8.pic}
\caption{} \label{sl.aks.2.2.8.pic}
\end{figure}

From the definition itself it follows that the poltrak is a subset of its carrier or that it lies on its carrier. From the relation $B,X\ddot{-} A$ it follows that $B$, $X$ and $A$ are collinear points, so the point $X$ lies on the line $AB$.

We will not prove other important properties of lines and line segments that we will use later. Let's mention some of these properties.

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

The proof of the previous statement is based on the fact that the relation $\ddot{-} A$ is equivalent to the relation that has two classes. Each of the classes is a suitable open ray.

The rays from the previous statement, which are determined by the same initial point on the line, are called \index{poltrak!komplementarni}\pojem{complementary rays}.

The concepts of line and ray allow us to define new concepts.

Let $A_1$, $A_2$, ... $A_n$ be such points in the plane that no three of them are collinear. The union of the lines $A_1A_2$, $A_2A_3$,... $A_{n-1}A_n$ is called \index{lomljenka} \pojem{broken line} $A_1A_2\cdots A_n$ or \index{poligonska
črta}\pojem{polygonal line} $A_1A_2\cdots A_n$ (Figure \ref{sl.aks.2.2.10.pic}). The points  $A_1$, $A_2$, ... $A_n$ are \index{oglišče!lomljenke} \pojem{vertices of the broken line},
the lines $A_1A_2$, $A_2A_3$,... $A_{n-1}A_n$ are \index{stranica!lomljenke} \pojem{sides of the broken line}. The sides of the broken line with a common vertex are \index{sosednji stranici!lomljenke} \pojem{adjacent sides of the broken line}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10.pic}
\caption{} \label{sl.aks.2.2.10.pic}
\end{figure}

If the sides of a broken line do not have common points, except for adjacent sides that have a common vertex, such a broken line is called a \index{lomljenka!enostavna} \pojem{simple broken line} (Figure \ref{sl.aks.2.2.10a.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10a.pic}
\caption{} \label{sl.aks.2.2.10a.pic}
\end{figure}

A broken line $A_1A_2\cdots A_nA_{n+1}$, for which $A_{n+1}=A_1$ and $A_n$, $A_1$ and $A_2$ are non-linear points, is called a \index{lomljenka!sklenjena} \pojem{closed broken line} $A_1A_2\cdots A_n$ (Figure \ref{sl.aks.2.2.10b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10b.pic}
\caption{} \label{sl.aks.2.2.10b.pic}
\end{figure}

We will be particularly interested in \pojem{simple closed broken lines} (Figure \ref{sl.aks.2.2.10b.pic}).

Let $p$ and $q$ be two semi-lines with a common starting point $O$ (Figure \ref{sl.aks.2.2.10c.pic}). The union of these two semi-lines is called a \index{kotna lomljenka} \pojem{angular broken line} $pq$ (or $pOq$).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10c.pic}
\caption{} \label{sl.aks.2.2.10c.pic}
\end{figure}


For a figure $\Phi$ we say that it is \index{lik!konveksen}\pojem{convex}, if for any two of its points $A,B\in \Phi$ the distance $AB$ is a subset of this figure or if the following is true (Figure \ref{sl.aks.2.2.10d.pic}):
 $$(\forall A)(\forall B)\hspace*{1mm} (A,B\in \Phi \Rightarrow [AB]\subseteq \Phi).$$
For a figure that is not convex, we say that it is \index{lik!nekonveksen}\pojem{non-convex} (Figure \ref{sl.aks.2.2.10d.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10d.pic}
\caption{} \label{sl.aks.2.2.10d.pic}
\end{figure}

It follows directly from the definition that a straight line is a convex figure. As a result of the axioms of this group, it can be proved that a distance and a semi-line are convex figures.

We say that a figure $\Phi$ is
\index{figure!connected}\pojem{connected}, if for every two of its points $A,B\in \Phi$ there exists a broken line $AT_1T_2\cdots T_nB$, which is a subset of this figure, or if the following is true (Figure \ref{sl.aks.2.2.10e.pic}):
 $$(\forall A\in \Phi)(\forall B\in \Phi)(\exists T_1,T_2,\cdots , T_n)\hspace*{1mm}  AT_1T_2\cdots T_nB\subseteq \Phi.$$


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.10e.pic}
\caption{} \label{sl.aks.2.2.10e.pic}
\end{figure}

 A figure that is not connected, we call \index{figure!not connected}\pojem{not connected}.

 It is clear that every convex figure is also connected. For the broken line it is enough to take the distance $AB$. The converse is of course not true. There are figures that are connected, but not convex, which we will discover later.



Now we will define two relations that are analogous to the relations $\ddot{-} S$ and $\div S$.
 Let $p$ be a line that lies in the plane $\alpha$ (because we axiomatically build only the Euclidean geometry of the plane, in fact all the points that exist to us are in this plane). On the set $\alpha\setminus p$ (all points except the points of the line $p$) we define two relations.
We say that the points $A$ and $B$ ($A,B\in \alpha\setminus p$) are \index{relation!on different sides of the line} \pojem{on different sides of the line} $p$ (which we denote by $A,B\div p$), if the line $AB$ has a common point with the line $p$, otherwise the points $A$ and $B$ ($A,B\in \alpha\setminus p$) are \index{relation!on the same side of the line} \pojem{on the same side of the line} $p$ (which we denote by $A,B\ddot{-} p$). So for points $A,B\in \alpha\setminus p$ it is $A,B\ddot{-} p$, if it is not $A,B\div p$ (Figure \ref{sl.aks.2.2.11.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.11.pic}
\caption{} \label{sl.aks.2.2.11.pic}
\end{figure}

Let $A$ be a point that does not lie on the line $p$. The set of all such points $X$, for which $A,X\ddot{-} p$, is called
\index{polravnina!odprta}\pojem{open half-line} $pA$. The union of the open half-lines $pA$ and the line $p$ is the \index{polravnina!zaprta}\pojem{closed half-line} or just
\index{polravnina}\pojem{half-line} $pA$. The line $p$ is the \index{rob!polravnine} \pojem{edge} of this half-line (Figure \ref{sl.aks.2.2.11a.pic}). If the points $B$ and $C$ lie on the edge $p$ of the half-line $pA$, we will call this half-line the half-line $BCA$. In addition, we will denote half-lines by Greek letters $\alpha$, $\beta$, $\gamma$,...

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.11a.pic}
\caption{} \label{sl.aks.2.2.11a.pic}
\end{figure}

Similarly to the case of a segment, it can be shown (as a consequence of the axioms of this group), that each line $p$ in the plane determines two half-lines $\alpha$ and $\alpha'$, which have the line $p$ as an edge (Figure \ref{sl.aks.2.2.11a.pic}). We say that in this case $\alpha$ and $\alpha'$ are \index{polravnina!komplementarna}\pojem{complementary half-lines}.
It turns out that the union of two complementary half-lines is the whole plane. Similarly to the case of a segment, the proof of these statements is based on the fact that the relation $\ddot{-} p$ is equivalent to the relation with two classes. Each of the classes is the appropriate open half-line.

Let $pq$ or $pOq$ be an angle. Define a new relation on the set of all points of the plane except the points that lie on the angle. We say that the points $A$ and $B$ are on the same side of the angle $pq$ (which we denote by $A,B\ddot{-} pq$), if there exists an angle $AT_1T_2\cdots T_nB$, which does not intersect the angle $pq$ or does not have any common points with it (Figure \ref{sl.aks.2.2.12.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12.pic}
\caption{} \label{sl.aks.2.2.12.pic}
\end{figure}

The relation $\ddot{-} pq$ is also an equivalence relation that has two classes. The union of each of these two classes with the angular bracket $pq$ is called
 \index{kot}\pojem{the angle} $pq$, which is denoted by $\angle pq$, or $\angle pOq$.
  The angular bracket therefore determines two angles. We will soon resolve the dilemma of which angle is meant by the notation  $\angle pOq$.
 The segments $p$ and $q$ are
\index{krak!kota}\pojem{the sides of the angle} and the point $O$ \index{vrh kota}\pojem{the vertex of the angle}.
If $P\in p$ and $Q\in q$ are points that lie on the sides of the angle $pOq$ and differ from its vertex $O$, we will also call the angle $POQ$ and denote it by $\angle POQ$ (Figure \ref{sl.aks.2.2.12a.pic}). If we know which angle it is, we will denote it by its vertex: $\angle O$. We will also denote angles by Greek letters $\alpha$, $\beta$, $\gamma$,...

All points of the angle $pOq$, which do not lie on either of the sides $p$ and $q$, are called \index{notranje točke!kota} \pojem{internal points of the angle}, the set of all these points is called \index{notranjost!kota}\pojem{the interior of the angle}. It is clear that these are points of the appropriate class determined by the relation $\ddot{-} pq$. The points of the other class are \index{zunanje!točke kota}\pojem{external points of the angle}, the whole class is \index{zunanjost!kota}\pojem{the exterior of the angle}. The points that lie on the sides, or on the angular bracket $pOq$, which determines the angle $pOq$, are \index{robne točke!kota}\pojem{the boundary points of the angle}, the whole bracket is \index{rob!kota}\pojem{the boundary of the angle}.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12a.pic}
\caption{} \label{sl.aks.2.2.12a.pic}
\end{figure}

If the sides of the angle are complementary segments, such an angle is called
\index{kot!iztegnjeni}\pojem{an extended angle} (Figure \ref{sl.aks.2.2.12b.pic}). As a set of points, this angle is essentially the same as the half-line with the boundary that is the carrier of both sides.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12b.pic}
\caption{} \label{sl.aks.2.2.12b.pic}
\end{figure}

If the angular bisector $pOq$ does not determine the extended angle or is not equal to the line, it turns out that $pOq$ determines two angles that represent a convex and a concave shape - we call them the \index{kot!konveksen}\pojem{convex (protruding) angle} and the \index{kot!nekonveksen}\pojem{concave (indented) angle}. We will omit the formal proof of this fact here. Unless otherwise stated, we will always mean the convex angle under the label $\angle pOq$ (or $\angle pq$ or $\angle POQ$). In this sense, it is clear from the definition of the angle that (convex) angle $pOq$ and $qOp$ represent the same angle.

The angle $pOq$ and $qOr$, which have a common leg $q$, which is also their intersection (as a set of points), are \index{kot!sosednji}\pojem{adjacent angles} (Figure \ref{sl.aks.2.2.12c.pic}). If in addition the segments $p$ and $r$ are complementary (or determine the extended angle), we say that $pOq$ and $qOr$ are \index{kota!sokota}\pojem{sokota}  (Figure \ref{sl.aks.2.2.12c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12c.pic}
\caption{} \label{sl.aks.2.2.12c.pic}
\end{figure}

The angle $pOq$ and $rOs$ are \index{kota!sovršna}\pojem{sovršna kota}, if $p$ and $r$ or $q$ and $s$ are a pair of complementary (supplementary) segments (Figure \ref{sl.aks.2.2.12d.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.12d.pic}
\caption{} \label{sl.aks.2.2.12d.pic}
\end{figure}

 Let $A_1A_2\cdots A_n$ ($n\in \{3,4,5,\cdots\}$) be a simple closed curve.
 Similarly to the angular bisector, on the set of all points in the plane except for the points that lie on the curve $A_1A_2\cdots A_n$, we can define the following relation: we say that the points $B$ and $C$ are on the same side of the simple closed curve $A_1A_2\cdots A_n$ (which we denote by $B,C\ddot{-} A_1A_2\cdots A_n$), if there exists a curve $BT_1T_2\cdots T_nC$, which does not intersect the simple closed curve $A_1A_2\cdots A_n$ or does not have any common points with it (Figure \ref{sl.aks.2.2.13.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13.pic}
\caption{} \label{sl.aks.2.2.13.pic}
\end{figure}

 It can also be proven in this case that it is an equivalence relation with two classes - for one class there is a line that lies entirely within it, but for the other class there is no such line. The union of the class that does not contain any line (intuitively - the one that is limited) and the simple closed broken line, $A_1A_2\cdots A_n$ is called
\index{polygon}\pojem{polygon} $A_1A_2\cdots A_n$ or
\index{$n$-gon}\pojem{$n$-gon} $A_1A_2\cdots A_n$ (Figure \ref{sl.aks.2.2.13a.pic}). All points of the aforementioned class that do not contain any line are called \index{internal points!of a polygon} \pojem{internal points of a polygon}, the entire class is \index{interior!of a polygon}\pojem{interior of a polygon}. The points of the other class are \index{external!points of a polygon}\pojem{external points of a polygon}, the entire class is \index{exterior!of a polygon}\pojem{exterior of a polygon}. The points that lie on the broken line $A_1A_2\cdots A_n$, which determines the polygon, are \index{vertices!of a polygon}\pojem{vertices of a polygon}, the entire broken line is \index{border!of a polygon}\pojem{border of a polygon}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13a.pic}
\caption{} \label{sl.aks.2.2.13a.pic}
\end{figure}


An equivalent statement holds true for the internal points of a polygon. We will state the statement without proof.

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

The points $A_1$, $A_2$,..., $A_n$ (the vertices of the broken line) are the \index{oglišče!večkotnika}\pojem{vertices of the polygon}, the segments $A_1A_2$, $A_2A_3$, ... $A_{n-1}A_n$, $A_nA_1$ are the \index{stranica!večkotnika}\pojem{sides of the polygon}. The lines $A_1A_2$, $A_2A_3$, ... $A_{n-1}A_n$, $A_nA_1$ are the \index{nosilka!stranice}\pojem{supports of the sides} $A_1A_2$, $A_2A_3$, ... $A_{n-1}A_n$, $A_nA_1$. The sides that contain a common vertex are the \index{stranica!sosednja}\pojem{adjacent sides}, otherwise the sides are \index{stranica!nesosednja}\pojem{non-adjacent}. If the vertices are at the same time the endpoints of the same side, we say that the vertices are \index{oglišče!sosednje}\pojem{adjacent}, otherwise the vertices are \index{oglišče!nesosednje}\pojem{non-adjacent}.
It is clear from the definition that each vertex has exactly two adjacent vertices. Similarly, each side has exactly two adjacent sides.
 The segment determined by two non-adjacent vertices is called the
\index{diagonala!večkotnika}\pojem{diagonal of the polygon} (Figure \ref{sl.aks.2.2.13c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13c.pic}
\caption{} \label{sl.aks.2.2.13c.pic}
\end{figure}

The following statement is true for the diagonals of the polygon.

            \bizrek
            The number of diagonals of an $n$-gon is $\frac{n(n-3)}{2}$.
            \eizrek

We will give the proof of this statement in section \ref{odd3Helly}, where we will separately consider the combinatorial properties of sets of points in the plane.

Let's define the angles of a polygon. Let $O$ be any vertex of a polygon, and $P$ and $Q$ be its two adjacent vertices. The line segments $OP$ and $OQ$ are denoted by $p$ and $q$. In this case, the angular bisector $pOq$ determines two angles. The angle for which it is true that every line segment with initial point $O$, which belongs to this angle and does not contain any other vertices of the polygon, intersects the edge of the polygon except at point $O$ in an odd number of points, is called the \index{angle!inner polygon}\pojem{inner angle of the polygon} or, more briefly, the \index{angle!inner}\pojem{angle of the polygon} at vertex $O$ (Figure \ref{sl.aks.2.2.13d.pic}). If the inner angle of the polygon is convex, its supplement is called the \index{angle!outer polygon}\pojem{outer angle of the polygon} (Figure \ref{sl.aks.2.2.13d.pic}).
  The angles of the polygon are
  \index{angle!adjacent}\pojem{adjacent angles}, if their vertices are adjacent vertices of the polygon, otherwise the angles are \index{angle!non-adjacent}\pojem{non-adjacent}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.13d.pic}
\caption{} \label{sl.aks.2.2.13d.pic}
\end{figure}

The most simple $n$-gon and at the same time one of the most used shapes in the geometry of a plane is the case $n=3$ - \index{trikotnik}\pojem{trikotnik}.
In the case of the triangle $ABC$ (we will mark it with $\triangle ABC$), the points $A$, $B$ and $C$ are its \pojem{oglišča}, and the lines $AB$, $BC$ and $CA$ are its
\index{stranica!trikotnika}\pojem{stranice} (Figure \ref{sl.aks.2.2.14.pic}). Obviously, every two sides of the triangle are adjacent. The same goes for every two vertices. The triangle therefore has no diagonal. We say that the vertex $A$ ($B$ and $C$) or the angle $BAC$ ($ABC$ and $ACB$) is the \index{oglišče!nasprotno trikotnika}\pojem{nasprotno oglišče} or the \index{kot!nasprotni trikotnika}\pojem{nasprotni kot} of the side $BC$ ($AC$ and $AB$) of the triangle $ABC$. And also the side $BC$ ($AC$ and $AB$) is the \index{stranica!nasprotna trikotnika}\pojem{nasprotna stranica} of the vertex $A$ ($B$ and $C$) or the angle $BAC$ ($ABC$ and $ACB$) of the triangle $ABC$. The angles (internal) of the triangle $ABC$ at the vertices $A$, $B$ and $C$ are often marked with $\alpha$, $\beta$ and $\gamma$, the corresponding external ones with $\alpha_1$, $\beta_1$ and $\gamma_1$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14.pic}
\caption{} \label{sl.aks.2.2.14.pic}
\end{figure}

The triangle $ABC$ can also be defined as the intersection of the half-planes $ABC$, $ACB$ and $BCA$. We will not prove the equivalence of these two definitions here.

 Pasch's axiom in terms of triangles can now be expressed in a shorter form:

If a line in the plane of a triangle intersects one of its sides
and does not pass through any of its vertices, then intersects exactly one more side of this triangle



             \bizrek \label{PaschIzrek}
           If a line, not passing through any vertex of a triangle, intersects one side of the triangle
           then the line intersects exactly one more side of the triangle (Figure \ref{sl.aks.2.2.14a.pic}).
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14a.pic}
\caption{} \label{sl.aks.2.2.14a.pic}
\end{figure}

In the case of $n=4$ for the $n$-gon we get
\index{štirikotnik}\pojem{štirikotnik}. Because each vertex of the quadrilateral has exactly one non-adjacent vertex, we will also call this vertex the \index{oglišče!nasprotno štirikotnika}\pojem{opposite vertex} of the quadrilateral. Similarly, the non-adjacent sides will be the \index{stranica!nasprotna štirikotnika}\pojem{opposite sides} of the quadrilateral. The diagonal of the quadrilateral is therefore determined by the opposite vertices.
 From the definition itself, it is clear that the quadrilateral has two diagonals\index{diagonala!štirikotnika} (Figure \ref{sl.aks.2.2.14b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14b.pic}
\caption{} \label{sl.aks.2.2.14b.pic}
\end{figure}

For the non-adjacent angle of the quadrilateral, we also say that they are the
 \index{kot!nasprotni štirikotnika}\pojem{opposite angles} of the quadrilateral. The angles (internal) of the quadrilateral $ABCD$ at the vertices $A$, $B$, $C$ and $D$ are usually denoted by $\alpha$, $\beta$, $\gamma$ and $\delta$, and the corresponding external (those that exist) by $\alpha_1$, $\beta_1$, $\gamma_1$ and $\delta_1$ (Figure \ref{sl.aks.2.2.14c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.14c.pic}
\caption{} \label{sl.aks.2.2.14c.pic}
\end{figure}



As a result of the axioms of order, we will also introduce the concepts of orientation of a triangle and orientation of an angle in this section.

The triangle $ABC$, for which the vertices are a triple $(A,B,C)$, is called the
  \index{orientacija!trikotnika} \pojem{oriented triangle}.
We say that the oriented triangles $ABC$ and $BCA'$ are of the \pojem{same orientation}, if $A,A'\ddot{-} BC$, and of the opposite orientation, if $A,A'\div BC$
 (Figure \ref{sl.aks.2.2.15.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.15.pic}
\caption{} \label{sl.aks.2.2.15.pic}
\end{figure}

When we talk about the orientation of two triangles, from now on we will always mean an oriented triangle (we will often omit the word oriented). Triangles $ABC$ and $A'B'C'$ are of the \pojem{same orientation} or are \pojem{equally oriented}, if there exists such a sequence of triangles: $\triangle ABC=\triangle P_1P_2P_3$, $\triangle P_2P_3P_4$, $\triangle P_3P_4P_5$, ..., $\triangle P_{n-2}P_{n-1}P_n=\triangle A'B'C'$, that in this sequence the number of changes in orientation of two adjacent triangles is even
 (Figure \ref{sl.aks.2.2.15a.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.15a.pic}
\caption{} \label{sl.aks.2.2.15a.pic}
\end{figure}

It can be proven that the relation of the same orientation of two triangles is equivalent to a relation that has two classes. For two triangles that are not in the same class, we say that they are of \pojem{different orientation} or are \pojem{differently oriented}. Each of the two classes determines the \index{orientation!plane}\pojem{orientation of the plane}. We call them the \pojem{positive orientation} and the \pojem{negative orientation}. For the sake of easier understanding, let us agree that the orientation that corresponds to the direction of the rotation of the hour hand is negative, and the opposite is the positive orientation
 (Figure \ref{sl.aks.2.2.15b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.15b.pic}
\caption{} \label{sl.aks.2.2.15b.pic}
\end{figure}


Let us also define the orientation of angles. Angles $ASB$ and $A'S'B'$, neither of which is a right angle, are of the \pojem{same orientation}, if:
\begin{itemize}
  \item both are convex or both are concave, and triangles $ASB$ and $A'S'B'$ are of the same orientation (Figure \ref{sl.aks.2.2.16.pic}),
  \item one angle is convex and the other is concave, and triangles $ASB$ and $A'S'B'$ are of opposite orientation (Figure \ref{sl.aks.2.2.16c.pic}).
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

 If $\angle ASB$ is an obtuse angle, $\angle A'S'B'$ is a convex angle, then the angles $ASB$ and $A'S'B'$ have the same orientation, if there is a point $C$ inside the angle $ASB$, such that the angles $ASC$ and $A'S'B'$ have the same orientation (Figure \ref{sl.aks.2.2.16d.pic}). We do the same if the angle $A'S'B'$ is obtuse or if both angles $ASB$ and $A'S'B'$ are obtuse.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.2.16d.pic}
\caption{} \label{sl.aks.2.2.16d.pic}
\end{figure}


It turns out that the relation of the same orientation of angles is an equivalent relation that has two classes. In this case, the positive orientation of the angle represents the class in which the triangle $ASB$ has a negative orientation for the convex angle $ASB$ from this class (Figure \ref{sl.aks.2.2.16a.pic}). In this sense, the angles $ASB$ and $BSA$ are oriented in the opposite direction.
   \index{orientation!angle} \pojem{Oriented angle} $ASB$  we will denote with $\measuredangle ASB$.


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

If $C$ is an arbitrary point that does not lie on the edge of the angle $ASB$, we will define the sum of the oriented angles $\measuredangle ASC$ and $\measuredangle CSB$
 (Figure \ref{sl.aks.2.2.16b.pic}):
 \begin{eqnarray}
 \measuredangle ASC+\measuredangle CSB = \measuredangle ASB.
 \label{orientKotVsota}
 \end{eqnarray}


%________________________________________________________________________________
 \poglavje{Congruence Axioms}
 \label{odd2AKSSKL}


The following axioms are needed to introduce the concept and properties of
the congruence of figures. With the previous axioms, we could introduce and
consider the concepts: distance, segment, angle, polygon, ... but not
the concepts related to congruence: circle, right angle,
congruence of triangles,~...

The intuitive idea of the compatibility of shapes that we used in
elementary school is associated with the movement that the first
shape transforms into the other. We will now use this idea to
formally define the concept of compatibility and its properties.
We will first start with the basic, already mentioned, concept of
compatibility of pairs of points $(A,B)\cong (C,D)$ (Figure
\ref{sl.aks.2.3.1.pic}) and formally define the concept of
‘‘movement’’.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.1.pic}
\caption{} \label{sl.aks.2.3.1.pic}
\end{figure}

 Using the compatibility of pairs of points, we first define the compatibility of an $n$-tuple of points.
 We say that
two $n$-tuples of points are compatible (Figure \ref{sl.aks.2.3.2.pic}) or
$$(A_1 , A_2,\ldots ,A_n ) \cong ( A'_1 , A'_2 ,\ldots , A'_n ),$$
if: $(A_i,A_j)\cong (A'_i,A'_j)$ for every $i,j\in \{1,2,\ldots,
n\}$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.2.pic}
\caption{} \label{sl.aks.2.3.2.pic}
\end{figure}


A bijective mapping of a plane into a plane
$\mathcal{I}:\mathcal{S}\rightarrow \mathcal{S}$ is
\index{izometrija}\pojem{izometrija} or \pojem{izometrijska
transformacija}, if it preserves the relation of compatibility of
pairs of points (Figure \ref{sl.aks.2.3.3.pic}) or if for every two
points $A$ and $B$ it holds:
 $$(\mathcal{I}(A),\mathcal{I}(B))\cong (A,B).$$

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.3.pic}
\caption{} \label{sl.aks.2.3.3.pic}
\end{figure}


With the following axioms, we will introduce the properties of the
newly defined mapping.


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

We mention that in the structure of a group the property of associativity is also required, i.e. $\mathcal{I}_1\circ (\mathcal{I}_2\circ \mathcal{I}_3)=
  (\mathcal{I}_1\circ \mathcal{I}_2)\circ \mathcal{I}_3$ (for any isometries
  $\mathcal{I}_1$, $\mathcal{I}_2$ and $\mathcal{I}_3$), which is automatically fulfilled
  in the operation of the composition of functions. We also mention the \pojem{identity} \index{identity}
 $\mathcal{E}$ from the previous axiom of the mapping, for which
 $\mathcal{E}(A)=A$ for every point on the plane. The mapping
 $\mathcal{I}^{-1}$ is the \pojem{inverse mapping} for the isometry
 $\mathcal{I}$, if $\mathcal{I}^{-1}\circ \mathcal{I}
 =\mathcal{I}\circ\mathcal{I}^{-1}=\mathcal{E}$. According to the previous
 axiom, the identity and the inverse mapping are therefore also isometries of every isometry.



We prove the first consequences of the compatibility axioms. First, we will
consider the following properties of isometries.



            \bizrek \label{izrekIzoB} Isometry maps a line to a line, a line segment to a line segment, a ray to a ray,
            a half-plane to a half-plane, an angle to an angle and an $n$-gon to an $n$-gon.
             \eizrek

\textbf{\textit{Proof.}}
 According to axiom \ref{aksIII1}, isometries preserve the relation
 $\mathcal{B}$. Therefore, all points of the line $AB$ are mapped by isometry $I$
  into points that lie on the line $A'B'$, where $A'=\mathcal{I}(A)$ and
  $B'=\mathcal{I}(B)$. Since the inverse mapping $\mathcal{I}^{-1}$ is also an isometry (axiom \ref{aksIII4}), each point of the line
  $A'B'$ is the image of some point that lies on the line $AB$. So with
  isometry $\mathcal{I}$
  the line $AB$ is mapped into the line $A'B'$.

 We defined the other shapes from the statement using the relation
 $\mathcal{B}$, so the proof is similar to the one for the line.
 \kdokaz

From the proof of the previous statement it follows that the endpoints of the line $AB$
are mapped by isometry into the endpoints of the image $A'B'$. In a similar
way, the starting point of the ray is mapped into the starting point of the ray, the edge of the half-plane into the edge of the half-plane, the vertex of the angle into the vertex of the angle and
the vertices of the polygon into the vertices of the polygon.

Isometries are defined as bijective maps, which preserve the
congruence of pairs of points. But does it also hold true, that for every congruent pair of points
there is an isometry, which maps the first pair into the second one? Let us answer this question with the following theorem.


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
 Let $C$ be a point, which does not lie on the line $AB$, and $C'$ be a point,
 which does not lie on the line $A'B'$ (Figure \ref{sl.aks.2.3.7.pic}).
 By Axiom \ref{aksIII2} there is a single isometry $\mathcal{I}$, which
 maps the point $A$ into the point $A'$, the segment $AB$ into the segment $A'B'$
 and the plane $ABC$ into the plane $A'B'C'$. Because of $(A,B)\cong (A',B')$ from the same Axiom \ref{aksIII2}, it follows that $\mathcal{I}(B)=B'$.
 \kdokaz

The proof of the following theorem, which will later be stated in a different form as the first theorem about the congruence of triangles, is similar.



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
By Axiom \ref{aksIII2} there exists a single isometry $\mathcal{I}$,
that maps point $A$ to point $A'$, line segment $AB$ to line segment
$A'B'$ and plane $ABC$ to plane $A'B'C'$ (Figure \ref{sl.aks.2.3.5.pic}).
Because, by the assumption $(A,B,C)\cong (A',B',C')$ from the same
Axiom \ref{aksIII2}, it follows that $\mathcal{I}(B)=B'$ and
$\mathcal{I}(C)=C'$.

  It is necessary to prove that $\mathcal{I}$ is the only such isometry.
  Assume that there exists such an isometry $\mathcal{\widehat{I}}$, that
  $\mathcal{\widehat{I}}: A, B,C\mapsto A',B',C'$. By
  Theorem \ref{izrekIzoB} isometry $\mathcal{\widehat{I}}$
  also maps line segment $AB$ to line segment $A'B'$ and plane $ABC$
  to plane $A'B'C'$. From Axiom \ref{aksIII2} it follows that
   $\mathcal{\widehat{I}}=\mathcal{I}$.
 \kdokaz

A direct consequence is the following theorem.


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

First, the identical mapping $\mathcal{E}$, that maps points $A$, $B$
and $C$ to the same points $A$, $B$ and $C$, is an isometry by Axiom
\ref{aksIII4}. From the previous theorem \ref{IizrekABC} it follows
that such an isometry is unique.
 \kdokaz

For point $A$ we say that it is \index{point!fixed} \pojem{fixed point}
(or \index{point!invariant} \pojem{invariant point}) of isometry
$\mathcal{I}$, if $\mathcal{I}(A)=A$. The previous theorem tells us
that the only isometries that have three fixed non-collinear points
are identities.

We will discuss isometries in more detail in chapter
\ref{pogIZO}, but here we will use them primarily to help us
introduce the concept of congruence of figures. Two figures $\Phi$
and $\Phi'$ are \index{figures!congruent}\poem{congruent} (we will
write $\Phi\cong \Phi'$), if there exists an isometry $I$, that
transforms figure $\Phi$ into figure $\Phi'$.

A direct consequence of axiom \ref{aksIII4} is the following
proposition.

\bizrek
             Congruence of figures is an equivalence relation. \label{sklRelEkv}
            \eizrek

\textbf{\textit{Proof.}}

\textit{Reflexivity.} For every figure $\Phi$ it holds that $\Phi \cong
\Phi$, because the identity transformation $\mathcal{E}$ is an isometry
(axiom \ref{aksIII4}) and $\mathcal{E}:\Phi\rightarrow\Phi$.

\textit{Symmetry.} From $\Phi \cong \Phi_1$ it follows that there exists an isometry $\mathcal{I}$, that transforms figure $\Phi$ into figure $\Phi_1$.
The inverse transformation $\mathcal{I}^{-1}$, which is an isometry according to axiom \ref{aksIII4}, transforms figure $\Phi_1$ into figure $\Phi$,
so $\Phi_1 \cong \Phi$ holds.

\textit{Transitivity.} From $\Phi \cong \Phi_1$ and $\Phi_1 \cong
\Phi_2$ it follows that there exist such isometries $\mathcal{I}$ and
$\mathcal{I}'$, that $\mathcal{I}:\Phi\rightarrow\Phi_1$ and
$\mathcal{I}':\Phi_1\rightarrow\Phi_2$ hold.
Then the composition $\mathcal{I}'\circ\mathcal{I}$,
  which is an isometry according to axiom \ref{aksIII4}, transforms figure $\Phi$
into figure $\Phi_2$, so $\Phi \cong \Phi_2$ holds.
\kdokaz


  The concept of congruence of figures also applies to lines. We have intuitively
  associated the congruence of lines with the congruence of pairs of points.
  Now we will prove the equivalence of both relations.

            \bizrek  \label{izrek(A,B)} $AB \cong A'B' \Leftrightarrow
            (A,B)\cong (A',B')$
             \eizrek

\textbf{\textit{Proof.}}

 ($\Rightarrow$) If $(A,B)\cong
(A',B')$, according to proposition \ref{izrekAB} there exists an isometry
$\mathcal{I}$, that transforms points $A$ and $B$ into points $A'$ and
$B'$. From proposition \ref{izrekIzoB} it follows that isometry $\mathcal{I}$
transforms line $AB$ into line $A'B'$ or $AB \cong A'B'$ holds.

($\Leftarrow$) If $AB \cong A'B'$, there exists an isometry
$\mathcal{I}$, which maps the line segment $AB$ to the line segment $A'B'$. By
the consequence of Theorem \ref{izrekIzoB}, the endpoint of the line segment is mapped to the endpoint of the line segment. This means that either
$\mathcal{I}:A,B\mapsto A',B'$ or $\mathcal{I}:A,B\mapsto
B',A'$ holds. From the first relation it follows that $(A,B)\cong (A',B')$ and from the second that $(A,B)\cong (B',A')$. But from the second example we also get
$(A,B)\cong (A',B')$, which is a consequence of Axioms \ref{aksIII3} and
\ref{aksIII4}.
\kdokaz

 Because of the previous theorem, in the following we will always write
  the relation $(A,B)\cong (A',B')$ instead of $AB\cong
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



 \textbf{\textit{Proof.}} Let $P$ be a point that does not lie on the line $AB$ and $Q$ be a point that does not lie on the line $CX$ (Figure \ref{sl.aks.2.3.5b.pic}).
  By Axiom \ref{aksIII2}, there is only one
  isometry $\mathcal{I}$, which
 maps the point $A$ to the point $C$, the line segment $AB$ to the line segment $CX$
 and the half-plane $ABP$ to the half-plane $CXQ$.
 Let $D=\mathcal{I}(C)$, then $AB \cong CD$ holds.

 We assume that
 on the line segment $CX$ there is another point $\widehat{D}$, for
 which
 $AB \cong C\widehat{D}$ holds. Because the line segments
 $CX$ and $CD$ are congruent, and the isometry $\mathcal{I}$ maps the point
 $A$ to the point $C$, the line segment $AB$ to the line segment $CD$
 and the half-plane $ABP$ to the half-plane $CDQ$,
  from Axiom \ref{aksIII2} it follows that $\mathcal{I}(C)=\widehat{D}$ or
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

 By Axiom \ref{aksIII2} there is only one
  isometry $\mathcal{I}$, which
 maps the point $A$ into the point $A'$, the segment $AB$ into the segment $A'B'$
 and the plane $ABC$ into the plane $\pi$ and holds $\mathcal{I}(B)=B'$.
 Let $C'=\mathcal{I}(C)$, then it holds $AC \cong A'C'$ and
 $BC \cong B'C'$. We assume that there is such a point
 $\widehat{C}'$, which lies in the plane $\pi$ and holds $AC \cong A'\widehat{C}'$ and
 $BC \cong B'\widehat{C}'$. Because $AB \cong
A'B'$, by Theorem \ref{IizrekABC} there is only one isometry
$\mathcal{\widehat{I}}$, which maps the points $A$, $B$ and $C$ into
the points $A'$, $B'$ and $\widehat{C}'$. But this also maps
the segment $AB$ into the segment $A'B'$ and the plane $ABC$ into the plane
$A'B'\widehat{C}'=\pi$. By Axiom \ref{aksIII2} is
$\mathcal{\widehat{I}}=\mathcal{I}$ and therefore also
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

\textbf{\textit{Proof.}} Let $X$ be an arbitrary point on the line
$AB$. Without loss of generality, we assume that the point $X$ lies
on the segment $AB$ (Figure \ref{sl.aks.2.3.8.pic}). We prove that
$\mathcal{I}(X)=X$.

Let $P$ be a point that does not lie on the line $AB$ and
$P'=\mathcal{I}(P)$. The isometry $\mathcal{I}$
maps the point $A$ to the point $A$, the segment $AB$ to the segment $AB$
 (or the segment $AX$ to the segment $AX$)
 and the half-plane $ABP$ to the half-plane $ABP'$
 (or the half-plane $AXP$ to the half-plane $AXP'$).
 By Axiom \ref{aksIII2}
  from $AX\cong AX$ it follows that $\mathcal{I}(X)=X$.
 \kdokaz

 We introduce new concepts related to distances.

We say that the line $EF$ \index{vsota!daljic}\pojem{vsota daljic}
$AB$ and $CD$, which we denote $EF=AB+CD$, if there exists such a point $P$
on the line $EF$, that $AB \cong EP$ and $CD \cong PF$ (Figure
\ref{sl.aks.2.3.9.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.9.pic}
\caption{} \label{sl.aks.2.3.9.pic}
\end{figure}


The line $EF$ is \index{razlika!daljic}\pojem{razlika daljic} $AB$
and $CD$, which we denote $EF=AB-CD$, if $AB=EF+CD$ (Figure
\ref{sl.aks.2.3.9.pic}).

 In a similar way, we can also define
  multiplication of a line by a natural and a positive rational
  number. For the lines $AB$ and $CD$ it is $AB=n\cdot CD$
  ($n\in \mathbb{N}$), if  there exist such points
  $X_1$, $X_2$,..., $X_{n-1}$, that
  $\mathcal{B}(X_1,X_2,\ldots,X_{n-1})$ and
  $AX_1 \cong X_1X_2 \cong X_{n-1}B \cong CD$ (Figure
\ref{sl.aks.2.3.10.pic}).
  In this case, it is also $CD=\frac{1}{n}\cdot AB$.

  At this point, we will not formally prove the fact that for every line $PQ$ and every natural number $n$ there exists a line $AB$, for which $AB=n\cdot PQ$, and a line $CD$, for which $CD=\frac{1}{n}\cdot PQ$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.10.pic}
\caption{} \label{sl.aks.2.3.10.pic}
\end{figure}

We introduce multiplication of a line segment with a positive rational number in the following way. For $q=\frac{n}{m} \in \mathbb{Q^+}$ we have:
$$q\cdot AB=\frac{n}{m}\cdot AB = n\cdot\left(\frac{1}{m}\cdot AB\right)$$

If for a point $P$ on the line segment $AB$ it holds that $AP=\frac{n}{m}\cdot PB$, we say that the point $P$ \pojem{divides} the line segment $AB$ in the \index{razmerje} \pojem{ratio} $n:m$, which we write as $AP:PB=n:m$.

The line segment $AB$ is \index{relacija!urejenosti daljic}\pojem{longer} than the line segment $CD$, which we denote $AB>CD$, if there exists such a point $P\neq B$ on the line segment $AB$, that it holds $CD \cong AP$ (Figure \ref{sl.aks.2.3.11.pic}). In this case we also say that the line segment $CD$ is \pojem{shorter} than the line segment $AB$ (notation $CD<AB$).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.11.pic}
\caption{} \label{sl.aks.2.3.11.pic}
\end{figure}

It is not hard to prove that for the line segments $AB$ and $CD$ exactly one of the relations $AB>CD$, $AB<CD$ or $AB \cong CD$ holds. This is a consequence of \ref{ABnaPoltrakCX}.

The point $S$ is the \index{središče!daljice} \pojem{midpoint (bisector)} of the line segment $AB$, if it lies on that line segment and it holds that $AS \cong SB$ (Figure \ref{sl.aks.2.3.12.pic}). Obviously, the midpoint divides the line segment in the ratio $1:1$. We still need to prove that such a point always exists.

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
 Let $AB$ be a line segment and $C$ an arbitrary point that does not lie on the line segment $AB$ (Figure \ref{sl.aks.2.3.13.pic}). We denote by $\pi$ the plane $ABC$ and by $\pi'$ the complementary plane of the plane $\pi$. By Axiom \ref{aksIII2}, there exists a single isometry $\mathcal{I}$, which maps the point $A$ to the point $B$, the line segment $AB$ to the line segment $BA$, and the plane $\pi$ to the plane $\pi'$. From $AB\cong BA$ (a consequence of Axiom \ref{aksIII3}) by the same Axiom it follows that $\mathcal{I}(B)=A$.

 Let $C'=\mathcal{I}(C)$, then $AC \cong B'C'$ and $BC \cong A'C'$. Because $C$ and $C'$ are on different sides of the line segment $AB$, the line segment $CC'$ intersects the line segment $AB$ at some point $S$. If $\widehat{C}=\mathcal{I}(C')$, then $A'C' \cong B\widehat{C}$ and $B'C' \cong A\widehat{C}$. Because $AC \cong B'C'$ and $BC \cong A'C'$, by Theorem \ref{izomEnaC'} it follows that $\widehat{C}=C$ or $\mathcal{I}(C')=C$. Therefore, the isometry $\mathcal{I}$ maps the line segment $AB$ and the line segment $CC'$ to themselves, so:
 $$\mathcal{I}(S)=\mathcal{I}(AB\cap CC')=
 \mathcal{I}(AB)\cap \mathcal{I}(CC')=
 AB\cap CC'=S.$$
 Now from $\mathcal{I}:A,S\mapsto B,S$ it follows that $AS\cong SB$.

 To prove that the point $S$ is indeed the center of the line segment $AB$, it is necessary to prove that the point $S$ lies on the line segment $AB$. Assume the contrary. Without loss of generality, let $\mathcal{B}(A,B,S)$. But in this case, on the line segment $SA$ there are two such points $A$ and $B$, that $SA\cong SB$, which contradicts Theorem \ref{ABnaPoltrakCX}.

 We also prove that the line segment has only one center. Let $\widehat{S}\neq S$ be a point on the line segment $AB$ and $A\widehat{S}\cong \widehat{S}B$. From Axiom \ref{aksIII3} it follows that $\mathcal{I}(A\widehat{S})=A\widehat{S}$. This means (from Theorem \ref{izoABAB}), that for every point $X\in AB$ it holds that $\mathcal{I}(X)=X$ and also $\mathcal{I}(A)=A$, which is not possible. Therefore, $\widehat{S}= S$.
 \kdokaz

We say that point $A$ is \index{symmetry!with respect to a point}\emph{symmetric} to point $B$ with respect to point $S$, if $S$ is the center of the line segment $AB$. The symmetry with respect to a translation over a point (i.e. central reflection) will be
further discussed in section \ref{odd6SredZrc}.

Now we will introduce the concepts and derive
the properties that relate
to angles and are analogous to those that we introduced for line segments.
If the statement \ref{ABnaPoltrakCX} is intuitively related to the transfer of a line segment with a compass
to a ray, the next statement will represent the transfer of an angle to a given
ray.


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
 Let $\alpha=\angle BAC$ and $\pi'$ be one of the half-planes determined by the line $p$ that contains the ray $Sp$ (Figure \ref{sl.aks.2.3.14.pic}).

 By statement \ref{ABnaPoltrakCX} there is
 only one point $P$ on the ray $Sp$, such that $AB \cong SP$.
 By axiom \ref{aksIII2} there is only one isometry $\mathcal{I}$, that
 maps point $A$ to point $S$, the ray $AB$ to the ray $Sp$
 and the half-plane $ABC$ to the half-plane $\pi'$.
  If $Q=\mathcal{I}(C)$, then the ray $AC$ is mapped by this isometry
  to the ray $SQ$. Therefore, the ray $SQ=Sq$ lies in the half-plane
  $\pi'$ and we have $\angle BAC\cong pSq$.

Let's assume that $S\widehat{q}$ is also a segment, lying in the plane
  $\pi'$ and $\angle BAC\cong pS\widehat{q}$. From the definition of congruence
   it follows that there exists an isometry $\mathcal{\widehat{I}}$, which
   maps the angle $BAC$ to the angle $\angle BAC\cong pS\widehat{q}$. Because
   the isometry $\mathcal{\widehat{I}}$
 also maps the point $A$ to the point $S$, the segment $AB$ to the segment $Sp$
 and the plane $ABC$ to the plane $\pi'$, by the axiom
 \ref{aksIII2} $\mathcal{\widehat{I}}=\mathcal{I}$. Therefore,
  $$S\widehat{q}=\mathcal{\widehat{I}}(AB)=\mathcal{I}(AB)=Sq,$$ which was needed to be proven. \kdokaz

 Because the carrier of the segment $Sp$ from the previous statement determines two
 planes, there exist two angles with the leg $Sp$, which are congruent to the angle
 $\alpha$. The mentioned angles are differently oriented. This means that one of these two angles has the same
 orientation as the angle $\alpha$ (Figure \ref{sl.aks.2.3.15.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.15.pic}
\caption{} \label{sl.aks.2.3.15.pic}
\end{figure}


Similarly to the case of distances, we define certain operations and
relations also among angles.

 The angle $pq$ with the vertex $S$ is the \index{vsota!kotov}\pojem{sum of angles} $ab$ and $cd$ or
 $\angle pq = \angle ab + \angle cd$, if there exists a segment
 $s=SX$, lying in the angle $pq$ and $\angle ps \cong \angle ab$
 and $\angle sq \cong \angle cd$ (Figure \ref{sl.aks.2.3.16.pic}).
  In this case we also say that
 the angle $ab$ is the \index{razlika!kotov}\pojem{difference of angles} $pq$ and $cd$, or
  $ \angle ab= \angle pq - \angle cd$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.16.pic}
\caption{} \label{sl.aks.2.3.16.pic}
\end{figure}

Similarly to the case of distances, for the angle $ab$ we define the angles
$n\cdot \angle ab$ and  $\frac{1}{n}\cdot \angle ab$ ($n\in
\mathbb{N}$) and $q\cdot \angle ab$ ($q\in \mathbb{Q}$).

We say that the angle $ab$ with the vertex $S$ \index{relation!order of angles}\pojem{is greater} than the angle $cd$ ($\angle ab > \angle cd$), if there exists a segment $s=SX$ in the angle $ab$, such that $\angle as \cong \angle cd$ (Figure \ref{sl.aks.2.3.17.pic}). In this case, the angle $cd$ is also \pojem{smaller} than the angle $ab$ ($\angle cd< \angle ab$). It is not difficult to prove that for two angles $ab$ and $cd$ one of the relations holds: $\angle ab > \angle cd$, $\angle ab < \angle cd$ or $\angle ab \cong \angle cd$.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.17.pic}
\caption{} \label{sl.aks.2.3.17.pic}
\end{figure}


The angles are \index{angles!supplementary}\pojem{supplementary}, if their sum is equal to the straight angle  (Figure
\ref{sl.aks.2.3.18.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.18.pic}
\caption{} \label{sl.aks.2.3.18.pic}
\end{figure}


The segment $s=SX$ is the \index{bisector of an angle}\pojem{bisector of the angle} $\angle pSq=\alpha$ (Figure \ref{sl.aks.2.3.19.pic}), if it lies in this angle and
it holds $\angle ps \cong \angle sq$. The carrier of this bisector  is the \index{simetrala!kota}\pojem{simetrala kota} $pSq$ (the line $s_{\alpha}$).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.19.pic}
\caption{} \label{sl.aks.2.3.19.pic}
\end{figure}



Similarly to the center of a line, the following statement holds for the bisector of an angle.

            \bizrek \label{izrekSimetralaKota}
             An angle has exactly one bisector.
             %(oz. eno samo simetralo).
            \eizrek

\textbf{\textit{Proof.}}
 Let $\alpha=pSq$ be an arbitrary angle, $P$ an arbitrary point, which lies on the
 segment $Sp$ ($P\neq S$) and $Q$ a point, which lies on the segment $Sq$ and it holds
 $SP\cong SQ$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.20.pic}
\caption{} \label{sl.aks.2.3.20.pic}
\end{figure}

Let the angle $\alpha$ be the extended angle
 (Figure \ref{sl.aks.2.3.20.pic}), which determines
 the line $\pi$. Let $A$ be any point on it. By the statement
 \ref{izomEnaC'} in the line $\pi$ there is only one point $B$,
 so that $(P,Q,A)\cong (Q,P,B)$. From the statement \ref{IizrekABC} it follows that there is only one izometry $\mathcal{I}$, which maps points $P$, $Q$ and
 $A$ into points $Q$, $P$ and $B$. Let
 $\mathcal{I}(B)=\widehat{A}$. Because
 $(Q,P,B)\cong(P,Q,\widehat{A})$, by the statement \ref{izomEnaC'}
 $\widehat{A}=A$. Therefore:
  $$\mathcal{I}:P,Q,A,B\mapsto Q,P,B,A.$$
Therefore, the centers $S$ and $L$ of the lines $PQ$ and $AB$ map into each other
(axiom \ref{aksIII4}), which then also holds for the line segment $s=SL$ and
every point on it (statement \ref{izoABAB}). Therefore, the izometry
$\mathcal{I}$ maps the line segment $pSs$ into the line segment $sSq$, so
  the line segment $pSs\cong sSq$ or the line segment $s$ is the bisector of the angle $pSq$.

  We will prove that $s$ is the only bisector of the angle $\alpha$. Let
  $\widehat{s}=S\widehat{L}$
  be a line segment that lies in the angle $\alpha$ and $pS\widehat{s}\cong
  \widehat{s}Sq$. Then there is an izometry $\mathcal{\widehat{I}}$, which
  maps the angle $pS\widehat{s}$ into the angle $\widehat{s}Sq$. This izometry
  maps the point $S$ into the point $S$, the line segment $p$ into the line segment $q$ and
  the line $\pi$ into the line $\pi$, so by the axiom
  \ref{aksIII2} $\mathcal{\widehat{I}}=\mathcal{I}$. Therefore
  $\mathcal{I}(\widehat{s})=
  \mathcal{\widehat{I}}(\widehat{s})=\widehat{s}$. If $\widehat{L} \notin
  s$, the izometry $\mathcal{I}$ maps three non-collinear points
  $S$, $L$ and $\widehat{L}$ into itself and is the identical mapping
  (statement \ref{IizrekABCident}), which is not possible. Therefore $\widehat{L} \in
  s$ or $\widehat{s}=s$.

If $\alpha$ is an unextended convex angle  (Figure \ref{sl.aks.2.3.20.pic}),
 then points $S$, $P$ and $Q$
 are nonlinear, so according to  Theorem \ref{IizrekABC} there is only one
  isometry $\mathcal{I}$, which maps points $P$, $S$ and $Q$ to
 points $Q$, $S$ and $P$. With $L$ we denote the center of the line $PQ$.
 By the Axiom \ref{aksIII3} we have $\mathcal{I}(L)=L$. Then also all
 points of the ray $s=SL$ are mapped to themselves (Theorem \ref{izoABAB}). As
$\alpha$ is a convex angle, this means that the point $L$ and then also
the ray $s$ lie within this angle.
 Therefore the isometry $\mathcal{I}$ maps angle $pSs$ to angle $sSq$, so
  $pSs\cong sSq$ or the ray $s$ is the bisector of angle $pSq$.

Similarly as in the previous example we prove that angle $\alpha$ has no other bisectors.

If $\alpha$ is a non-convex angle, the bisector is obtained as the
complementary (supplementary) ray of the ray $s$.
 \kdokaz

We prove two theorems, which relate to right angles and perfect angles.\index{angle!right} \index{angle!perfect}



               \bizrek
              The adjacent supplementary angles  of two congruent angles are also congruent. \label{sokota}
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.20a.pic}
\caption{} \label{sl.aks.2.3.20a.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $\alpha'=\angle P'OQ$ and $\alpha_1'=\angle P_1'O_1Q_1$ be the supplement angles of two adjacent angles $\alpha=\angle POQ$ and $\alpha_1=\angle P_1O_1Q_1$ (Figure \ref{sl.aks.2.3.20a.pic}). By Axiom \ref{aksIII2}, there exists a single isometry $\mathcal{I}$, which maps point $O$ to point $O_1$, line segment $OP$ to line segment $O_1P_1$, and line $POQ$ to line $P_1O_1Q_1$. Let $Q_2=\mathcal{I}(Q)$. Then $\angle P_1O_1Q_2\cong \angle POQ$. Isometry $\mathcal{I}$ maps line $POQ$ to line $P_1O_1Q_1$, so point $Q_2$ (and also line segment $O_1Q_2$) lies on line $P_1O_1Q_1$. Since, by assumption, $\angle POQ\cong\angle P_1O_1Q_1$, by  \ref{KotNaPoltrak} Theorem, $OQ_1$ and $OQ_2$ represent the same line segment. Therefore, point $Q_2$ lies on line segment $O_1Q_1$. Let $P_2'=\mathcal{I}(P')$. Since isometries map line segments to line segments (Theorem \ref{izrekIzoB}), point $P_2'$ lies on line segment $O_1P_1'$. From $\mathcal{I}:P',O,Q\mapsto P_2',O_1,Q_2$ it follows that isometry $\mathcal{I}$ maps angle $P'OQ$ to angle $P_2'O_1Q_2$  (Theorem \ref{izrekIzoB}), so
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


\textbf{\textit{Proof.}} Let $\alpha=\angle POQ$ and $\alpha'=\angle P'OQ'$ be two adjacent angles, where points $P$, $O$, $P'$ (or $Q$, $O$, $Q'$) are collinear (Figure \ref{sl.aks.2.3.20b.pic}). Angle $\beta=\angle QOP'$ is the supplement of both angles $\alpha$ and $\alpha'$. Since $\beta\cong\beta$, by the previous Theorem \ref{sokota}, $\alpha\cong\alpha'$.
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


\textbf{\textit{Proof.}} Let $P$ be an arbitrary point different from $S$  (Figure \ref{sl.aks.2.3.20c.pic}). By Axiom \ref{AksII3}, there exists a point $Q$ on the line $SP$ such that $\mathcal{B}(P,S,Q)$. We mark the half-planes determined by the edge $SP$ with $\alpha$ and $\alpha'$. By Axiom \ref{aksIII2}, there exists (one and only one) isometry $\mathcal{I}$, which maps the point $S$ to the point $S$, the line segment $SP$ to the line segment $SQ$, and the half-plane $\alpha$ to the half-plane $\alpha'$.

We mark the line $SP$ with $p$.
The point $P'=\mathcal{I}(P)$ lies on the line segment $SQ$ or on the line $p$. Therefore, since  $\mathcal{I}:S,P \mapsto S,P'$, the line $SP$ is mapped to the line $SP'$ by Axiom \ref{aksIII1}, i.e. $\mathcal{I}:p\rightarrow p$.
The image of the half-plane $\alpha'$ with the edge $p$ is therefore a half-plane with the same edge (Proposition \ref{izrekIzoB}). This half-plane cannot be $\alpha'$, since the isometry  $\mathcal{I}$ is a bijective mapping and it maps the half-plane  $\alpha$ to the half-plane $\alpha'$.  Therefore, $\mathcal{I}:\alpha'\rightarrow \alpha$.

Now it is clear that, without loss of generality, it is enough to carry out the proof only for points that lie in the half-plane $\alpha$ (without the edge or only the line segment $SP$).

Let $X\in \alpha\setminus p$ and $X'=\mathcal{I}(X)$. We immediately see that $X'\in \alpha'\setminus p$. By Axiom \ref{AksII3} there exists on the line $SX$ such a point $X_1$, that $\mathcal{B}(X,S,X_1)$ is true. Because $\angle PSX$ and $\angle P'SX_1$ are perfect angles, by Theorem \ref{sovrsnaSkladna} they are also compatible. But from $\mathcal{I}:S,P,X \mapsto S,P',X'$ it follows that $\angle PSX \cong \angle P'SX'$. Therefore $\angle P'SX_1\cong \angle P'SX'$ is true (Theorem \ref{sklRelEkv})), so by Theorem \ref{KotNaPoltrak} the line segments $SX_1$ and $SX'$ are identical. This means that the point $X'$ lies on the line segment $SX_1$ or $\mathcal{B}(X,S,X')$ is true. Because of $\mathcal{I}:S,X \mapsto S,X'$ it is also true that $SX\cong SX'$, so by definition the point $S$ is the center of the line $XX'$.

 Let in the end $Y$ be an arbitrary point on the line segment $SP$, which is different from the point $S$, and $Y'=\mathcal{I}(Y)$. The point $Y'$ lies on the line segment $SQ$, so $\mathcal{B}(Y,S,Y')$ is true. Because of $\mathcal{I}:S,Y \mapsto S,Y'$ it is also true that $SY\cong SY'$, so by definition the point $S$ is the center of the line $YY'$.
\kdokaz

In section \ref{odd6SredZrc} we will discuss the isometry, which is mentioned in the previous Theorem \ref{sredZrcObstoj}, in more detail.


 Let us define new types of angles.
 A \index{kot!ostri}\pojem{acute angle} is a \index{kot!pravi}
 \pojem{right angle} or a \index{kot!topi}\pojem{obtuse angle}, if it is
 smaller, equal to or greater than its supplement (Figure \ref{sl.aks.2.3.21.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.21.pic}
\caption{} \label{sl.aks.2.3.21.pic}
\end{figure}



From the definition it follows that acute (or obtuse) angles are those convex angles, which are smaller (or greater) than a right angle.

From Theorem \ref{izrekSimetralaKota} it follows that a right angle
exists, since the bisector of an extended angle divides it into two compatible supplements.

It is not difficult to prove that every two right angles are compatible and that an angle, which is compatible with a right angle, is also a right angle.

If the sum of two angles is a right angle, we say that the angles are
\pojem{complementary} (Figure
\ref{sl.aks.2.3.22.pic}).


\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.22.pic}
\caption{} \label{sl.aks.2.3.22.pic}
\end{figure}



We will now introduce an extremely important relation between lines. If
the lines $p$ and $q$ contain the segments of a right angle, we say that
$p$ and $q$ are \pojem{perpendicular}, which we denote $p \perp q$
(Figure \ref{sl.aks.2.3.23.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.23.pic}
\caption{} \label{sl.aks.2.3.23.pic}
\end{figure}

From the definition itself it is clear that the perpendicularity is a
symmetric relation, i.e. from $p \perp q$ it follows that $q \perp p$. If
$p \perp q$ and $p \cap q=S$, we say that the line $p$ is
\pojem{perpendicular} to the line $q$ at the point $S$ or that $p$ is a
\pojem{perpendicular} of the line $q$ at this point.



The following theorem is the most important theorem that characterizes
the relation of perpendicularity.



                \bizrek \label{enaSamaPravokotnica}
                For each point $A$ and each line $p$, there is a unique line $n$
            going through the point $A$, which is perpendicular on the line $p$.
                \eizrek

\textbf{\textit{Proof.}}
Assume that point $A$ does not lie on line $p$. Let $B$ and $C$ be any points that lie on line $p$ (Figure \ref{sl.aks.2.3.24.pic}). We denote the plane $BCA$ with $\pi$, and the complementary plane with $\pi_1$. By izreku \ref{izomEnaC'}, there exists only one point $A_1\in \pi_1$, for which $(A,B,C) \cong (A_1,B,C)$. From izreku \ref{IizrekABC} it follows that there exists only one izometrija $\mathcal{I}$, which maps points $A$, $B$ and $C$ into points $A_1$, $B$ and $C$. We denote the line $AA_1$ with $n$. Because $A$ and $A_1$ are on different sides of line $p$, line $n$ intersects line $p$ in some point $S$. From $\mathcal{I}:B,C \mapsto B,C$ it follows that $\mathcal{I}(S)=S$ (izrek \ref{izoABAB}). Therefore, izometrija $\mathcal{I}$ maps angle $ASB$ into angle $A_1SB$. It follows that $\angle ASB$ and $\angle A_1SB$ are complementary angles, therefore they are right angles. Therefore, $n \perp p$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.24.pic}
\caption{} \label{sl.aks.2.3.24.pic}
\end{figure}

We will prove that $n$ is the only perpendicular to line $p$ through point $A$. Let $\widehat{n}$ be a line, for which $A\in \widehat{n}$ and $\widehat{n} \perp p$. Let point $\widehat{S}$ be the intersection of lines $\widehat{n}$ and $p$. By the assumption, $\angle A\widehat{S}B$ is a right angle and is compatible with its complementary angle $\angle B\widehat{S}A_2$ ($A_2$ is such a point that $\mathcal{B}(A,\widehat{S},A_2)$), which is also a right angle.

From $\mathcal{I}:B,C \mapsto B,C$ it follows
$\mathcal{I}(\widehat{S})=\widehat{S}$ (statement \ref{izoABAB}).
Therefore, the isometry $\mathcal{I}$ maps the angle $A\widehat{S}B$ into the angle
$A_1\widehat{S}B$. It follows that $\angle A\widehat{S}B$ and $\angle
A_1\widehat{S}B$ are congruent, so $\angle A_1\widehat{S}B$
is a right angle. Therefore, the angle $A_1\widehat{S}B$ and $A_2\widehat{S}B$
are right angles and are therefore congruent. It follows that the line segments
$\widehat{S}A_1$ and $\widehat{S}A_2$ are the same, so $A_1 \in
\widehat{S}A_2=\widehat{n}$ or $\widehat{n}=AA_1=n$.

 In the case when the point $A$ lies on the line $p$, the rectangle $n$
 is the symmetry of the corresponding extended angle (statement \ref{izrekSimetralaKota}).
\kdokaz


The previous statement has the following important consequence - the existence of pairs of disjoint lines in the plane - or those that do not have common points. This is the content of the following two statements.


            \bizrek \label{absolGeom1}
             Let $p$ and $q$ be a lines perpendicular on a line $PQ$ in the points $P$ and $Q$.
            Then the lines $p$ and $q$ do not have a common points i.e. $p\cap q=\emptyset$.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.25b.pic}
\caption{} \label{sl.aks.2.3.25b.pic}
\end{figure}

\textbf{\textit{Proof.}} The statement is a direct consequence of the previous statement \ref{enaSamaPravokotnica}. Namely, if the lines $p$ and $q$ intersected at some point $S$, we would have two rectangles on the line $PQ$ from the point $S$ (Figure \ref{sl.aks.2.3.25b.pic}), which is in contradiction with the aforementioned statement.
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

\textbf{\textit{Proof.}} By the statement \ref{enaSamaPravokotnica} there exists (exactly one) rectangle $n$ of the line $p$, which goes through the point $A$. We mark with $A'$ the intersection of the lines $p$ and $n$. From the same statement it follows that there exists another rectangle $q$ of the line $n$ in the point $A$. By the previous statement \ref{absolGeom1} the line $q$ goes through the point $A$ and doesn't have any common points with the line $p$.
 \kdokaz

The point $A'$ is the \index{node}\pojem{node} or the
\index{orthogonal projection}\pojem{orthogonal projection} of the
point $A$ on the line $p$, if the rectangle of the line $p$ through
the point $A$ intersects the line in the point $A'$. We will mark
it with $A'=pr_{\perp p}(A)$ (Figure \ref{sl.aks.2.3.25.pic}). From
the previous statement it follows that for every point and line
there exists only one orthogonal projection.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.25.pic}
\caption{} \label{sl.aks.2.3.25.pic}
\end{figure}

The line, which goes through the center $S$ of the distance $AB$ and is perpendicular to the line $AB$, is called the \index{symmetry!of a line}\pojem{symmetry of the line} $AB$ and we mark it with $s_{AB}$
(Figure \ref{sl.aks.2.3.26.pic}). The properties of the symmetry of a line we will discuss in the next chapter.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.26.pic}
\caption{} \label{sl.aks.2.3.26.pic}
\end{figure}


We say that the point $A$ is \index{symmetry!with respect to a line}\pojem{symmetric} to the point $B$ with respect to the line $s$, if the line $s$ is the symmetry of the line $AB$. The symmetry with respect to a line (as a mapping - i.e. the basic mirroring) we will discuss in more detail in the section \ref{odd6OsnZrc}.

Let $S$ be a point and $AB$ a line. The set of all points $X$, for
which it holds that $SX \cong AB$, is called the
\index{circle}\pojem{circle} with
\index{center!of a circle}\pojem{center} $S$ and \index{radius
of a circle}\pojem{radius} $AB$; we mark it with $k(S,AB)$ (Figure
\ref{sl.aks.2.3.27.pic})  i.e.:
 $$k(S,AB)=\{X;\hspace*{1mm}SX \cong AB\}.$$

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.27.pic}
\caption{} \label{sl.aks.2.3.27.pic}
\end{figure}

 Of course, a circle is a set
 of points in a plane, because in this book we only consider
 planar geometry (all points and all figures belong to the same plane).

 From the definition it is clear that for the radius we can choose any distance
 that is consistent with
 the distance $AB$, that is, any distance $SP$, where $P$ is any
 point on the circle. Since the radius is not tied to
 a specific distance, we usually denote it with a small letter $r$. So we can also write the circle like this:
 $$k(S,r)=\{X;\hspace*{1mm}SX \cong r\}.$$
 The set

$$\{X;\hspace*{1mm}SX \leq r\}$$
we call the \index{krog}\pojem{circle} with center $S$ and radius $r$ (Figure \ref{sl.aks.2.3.28.pic}) and denote it with $\mathcal{K}(S,r)$.
The set
 $$\{X;\hspace*{1mm}SX < r\}$$
 is the \index{notranjost!kroga}
 \pojem{interior of the circle} $\mathcal{K}(S, r)$, and its points are
 \pojem{interior points of the circle}.
 This means that the circle is actually the union of its interior and the corresponding circle.

The set
 $$\{X;\hspace*{1mm}SX > r\}$$
 we call the \index{zunanjost!kroga}\pojem{exterior of the circle} $\mathcal{K}(S, r)$
  and its points \pojem{exterior points of the circle}.

 For practical reasons, we will call the interior of the circle $\mathcal{K}(S, r)$ the \index{notranjost!krožnice}\pojem{interior} of the corresponding circle $k(S,r)$, the exterior of the circle $\mathcal{K}(S, r)$ the \index{zunanjost!krožnice}\pojem{exterior} of the corresponding circle $k(S,r)$. We define the \pojem{interior} and \pojem{exterior} points of the circle in the same way.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.28.pic}
\caption{} \label{sl.aks.2.3.28.pic}
\end{figure}

If $P$ and $Q$ are two points on the circle $k(S, r)$, the distance $PQ$
   is called the \index{tetiva krožnice} \pojem{tetiva} of
  the circle. If
the tether contains the center of the circle, it is called
\index{premer krožnice}\pojem{premer} or \index{diameter
krožnice}\pojem{diameter} of the circle (Figure
\ref{sl.aks.2.3.29.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.3.29.pic}
\caption{} \label{sl.aks.2.3.29.pic}
\end{figure}

We prove the following statement.


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

 If $PQ$ is the diameter of the circle $k(S, r)$, the points $P$ and $Q$ lie
on the circle, which means: $SP \cong SQ \cong r$ (Figure
\ref{sl.aks.2.3.30.pic}). Because the point $S$ lies on the line $PQ$,
it follows that the point $S$ is the center of this line.
 \kdokaz

 From the previous statement it follows that the diameter is equal to two radii, because:
$PQ = PS + SQ = 2\cdot PS = 2\cdot r$. This means
that all diameters of a circle are consistent with each other.


Let $P$ and $Q$ be any two points on the circle  $k(S, r)$. The intersection
of the circle $k$ with one of the planes (in the plane of this circle) with the edge
$s=PQ$ is called the \index{krožni!lok} \pojem{krožni lok} $PQ$ (or
shorter \pojem{lok}) with the endpoints $P$ and $Q$.

Thus, each tether $PQ$ on a circle $k$ determines two arcs. Assume that the center $S$ does not lie on the edge of the plane that generates the circular arc.
If this plane
contains the center $S$ of the circle $k$,
it is a \pojem{veliki lok} $PQ$, otherwise it is a \pojem{mali
lok} $PQ$.
 But if
  the center $S$ is on the edge $PQ$ of the plane, then each of the two arcs $PQ$
 \index{polkrožnica}\pojem{polkrožnica} $PQ$ (Figure
\ref{sl.skk.4.2.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.1.pic}
\caption{} \label{sl.skk.4.2.1.pic}
\end{figure}

Since the locus is not uniquely determined by its endpoints, we must also know
at least one point on the circle that belongs or does not belong to this locus.

In a similar way, we define certain parts of the circle.

Let $P$ and $Q$ be arbitrary points on the circle $k(S, r)$. The intersection
of the circle $\mathcal{K}(S, r)$ with one of the planes (in the plane of this circle) with the edge
$s=PQ$ is called
\index{krožni!odsek} \pojem{circular segment}.
 So each chord $PQ$ on some circle $k(S, r)$ determines on the circle $\mathcal{K}(S, r)$ two circular segments. Assume that the center $S$ does not lie on the edge of the plane that generates the circular segment.
If this plane
contains the center $S$ of the circle $k$,
it is a \pojem{major circular segment} $PQ$, otherwise it is a \pojem{minor
circular segment} $PQ$.
 If the
  center $S$ is on the edge $PQ$ of the plane, then each of the two circular segments
\index{polkrog}\pojem{arc}
 is an \pojem{arc}.
 From the definition it is clear that the edge of the circular segment is the union of the chord $PQ$ and the corresponding arc (Figure
\ref{sl.skk.4.2.1b.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.1b.pic}
\caption{} \label{sl.skk.4.2.1b.pic}
\end{figure}


We will also define one more term related to the circle.
Let $P$ and $Q$ be arbitrary points on the circle $k(S, r)$. The intersection
of the circle $\mathcal{K}(S, r)$ with one of the angles $PSQ$ is called
\index{krožni!izsek} \pojem{circular sector}. Again we have two circular sectors. If the angle $PSQ$ is an obtuse angle, we get two arcs, otherwise a convex and a concave circular sector, depending on whether the angle $PSQ$ is convex or concave (Figure
\ref{sl.skk.4.2.1c.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.1c.pic}
\caption{} \label{sl.skk.4.2.1c.pic}
\end{figure}





%________________________________________________________________________________
 \poglavje{Continuity Axiom} \label{odd2AKSZVE}

We have already learned in elementary school, when introducing the numerical line and the coordinate system, that it is possible to establish a connection in which each point of a line corresponds to a certain real number, and vice versa, each real number can be assigned a point that lies on that line. This is related to the following axiom.

\baksiom \label{aksDed}\index{aksiom!Dedekind's}
(Dedekind's\footnote{\index{Dedekind, R.}
\textit{R. Dedekind} (1831--1916),
German mathematician.}
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

Let us state without proof two important consequences of the axiom
of continuity\footnote{Until the 19th century, mathematicians did not
feel the need to prove these two statements, or the need to
introduce the axiom of continuity. Even \index{Evklid} Euclid from
Alexandria (3rd century BC) in his famous work
'Elements', does not prove that a certain circle intersects.}.


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

\poglavje{The basics of Geometry} \label{osn9Geom}
We have already learned in elementary school, when introducing the numerical line and the coordinate system, that it is possible to establish a connection in which each point of a line corresponds to a certain real number, and vice versa, each real number can be assigned a point that lies on that line. This is related to the following axiom.

\baksiom \label{aksDed}\index{aksiom!Dedekind's}
(Dedekind's\footnote{\index{Dedekind, R.}
\textit{R. Dedekind} (1831--1916),
German mathematician.}
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

Let us state without proof two important consequences of the axiom
of continuity\footnote{Until the 19th century, mathematicians did not
feel the need to prove these two statements, or the need to
introduce the axiom of continuity. Even \index{Evklid} Euclid from
Alexandria (3rd century BC) in his famous work
'Elements', does not prove that a certain circle intersects.}.


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

Dedekind's axiom is used in a few different ways to establish the set of real numbers. This is reminiscent of the already mentioned connection between the set of points on a line and the set of real numbers.

We have already defined the multiplication operation of line segment $AB$ by any positive rational number $q$. Now we can extend the concept of multiplication to any positive real number $\lambda$. The definition of line segment $\lambda\cdot AB$, ($\lambda \in \mathbb{R}^+$), which we will not formally derive here, is associated with two sets of points on line segment $CD$:
 \begin{eqnarray*}
&& \{X\in CD;\hspace*{1mm}CX=q\cdot
AB,\hspace*{1mm}q\leq\lambda,\hspace*{1mm}q\in
\mathbb{Q}^+ \} \hspace*{1mm}\textrm{ in}\\
&& \{X\in CD;\hspace*{1mm}CX=q\cdot
AB,\hspace*{1mm}q>\lambda,\hspace*{1mm}q\in \mathbb{Q}^+ \}
 \end{eqnarray*}
 and
Dedekind's axiom \ref{aksDed}.

 With the help of the axiom of continuity \ref{aksDed} we can also introduce the concepts of measuring line segments and angles.

 When measuring line segments we will assign each line segment $AB$ a positive real number $\textsl{m}(AB)$ in the following way.
  Let $\mathcal{D}$ be the set of all line segments and $\mathbb{R}^+$ be the set of all positive real numbers. The mapping $\textsl{m}:\mathcal{D}\rightarrow\mathbb{R}^+$, which satisfies the following properties:
  \begin{itemize}
    \item $(\exists A_0B_0\in\mathcal{D})\hspace*{1mm}\textsl{m}(A_0B_0)=1$,
    \item $(\forall AB, CD\in\mathcal{D})\hspace*{1mm}(AB\cong CD \Rightarrow\textsl{m}(AB)=\textsl{m}(CD))$,
    \item $(\forall AB, CD, EF\in\mathcal{D})\hspace*{1mm}(AB+CD=EF\Rightarrow \textsl{m}(AB)+\textsl{m}(CD)=\textsl{m}(EF))$,
  \end{itemize}
  is called the \index{dolžina!daljice}\pojem{length of a line segment} or the \index{mera!daljice}\pojem{measure of a line segment}, and the triple $\textsl{M}=(\mathcal{D},\mathbb{R}^+,\textsl{m})$ is called the \index{sistem merjenja!daljic}\pojem{system of measuring line segments}.

The length of the line $AB$ (or $\textsl{m}(AB)$) will usually be denoted by $|AB|$.

  It is intuitively clear that there are an infinite number of measuring systems, which depend on the choice of the unit length line $A_0B_0$ - the one that has a length of 1, or $\textsl{m}(A_0B_0)=1$. In one measuring system, the length of any line $AB$ is represented by a positive real number $x$, for which $AB=x\cdot A_0B_0$. So $\textsl{m}(AB)=x$ exactly when $AB=x\cdot A_0B_0$ (Figure \ref{sl.aks.2.4.4.pic}). Now it is clear why we need the axiom of connectivity - without it, we would have problems with the definition of the length of the diagonal of a square with a unit length side (of length 1)\footnote{The ancient Greeks always represented the length as a rational number, so they called the side
and the diagonal of the square \pojem{incomparable lines}.}.


\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.4.pic}
\caption{} \label{sl.aks.2.4.4.pic}
\end{figure}


        \bizrek \label{meraDalj1}
        For any measuring system of lengths it holds:

          (\textit{i}) $AB<CD\Rightarrow |AB|<|CD|$;

          (\textit{ii}) $|AB|=|CD|\Rightarrow AB\cong CD$.
        \eizrek

    \textbf{\textit{Proof.}}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.5.pic}
\caption{} \label{sl.aks.2.4.5.pic}
\end{figure}

          (\textit{i}) From $AB<CD$ it follows that there is a point $T$ on the line $CD$, such that $CT\cong AB$. Because $\mathcal{B}(C,T,D)$, it is clear that $CD=CT+TD$ (Figure \ref{sl.aks.2.4.5.pic}). From the definition of the measure, it then follows: $|CD|=|CT|+|TD|=|AB|+|TD|>|AB|$.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.6.pic}
\caption{} \label{sl.aks.2.4.6.pic}
\end{figure}

(\textit{ii}) Suppose that $AB\not\cong CD$. Without loss of generality, let $AB<CD$. But in this case, from the proven (\textit{i}), it follows that $|AB|<|CD|$, which is in contradiction with the assumption $|AB|=|CD|$. Therefore $AB\cong CD$ (Figure \ref{sl.aks.2.4.6.pic}).
    \kdokaz

Because, by definition, the lengths of the lines and the previous statement \ref{meraDalj1} are consistent only when they have the same length, we will often look at the \index{polmer krožnice}polmer $r$ of the circle $k(S,r)$ as the length of this radius.

The next statement will be given without proof.

            \bizrek \label{meraDaljice}
            Let $\textsl{m}:\mathcal{D}\rightarrow\mathbb{R}^+$ be the measure of the line. The mapping $\textsl{m}_1:\mathcal{D}\rightarrow\mathbb{R}^+$ also represents the measure exactly when there is such a positive real number $\mu$, that for every line $AB$ it holds:
            $$\textsl{m}_1(AB)=\mu\cdot\textsl{m}(AB).$$
            \eizrek

The measure of the line allows us to define a new concept.
 \index{razmerje!daljic}\pojem{Razmerje daljic} $AB$ and $CD$ with labels $AB:CD$ or $\frac{AB}{CD}$ is the ratio of the lengths of these two lines (Figure \ref{sl.aks.2.4.7a.pic}). Therefore:
  $$AB:CD=\frac{AB}{CD}=\frac{|AB|}{|CD|}.$$

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.7a.pic}
\caption{} \label{sl.aks.2.4.7a.pic}
\end{figure}

  It is clear that the ratio of two lines must always be the same number, regardless of the measuring system.

 We will therefore confirm the correctness of the previous definition with the following statement.

            \bizrek
            The ratio of two lines is not dependent on the measuring system.
            \eizrek

\textbf{\textit{Proof.}} Let $(\mathcal{D},\mathbb{R}^+,\textsl{m})$ and $(\mathcal{D},\mathbb{R}^+,\textsl{m}_1)$ be two measuring systems. By the previous statement \ref{meraDaljice} there exists a $\mu\in\mathbb{R}^+$, such that $\textsl{m}_1(PQ)=\mu\cdot\textsl{m}(PQ)$ for any distance $PQ$. For any distances $AB$ and $CD$ it therefore holds:
     $$\frac{\textsl{m}_1(AB)}{\textsl{m}_1(CD)}=
     \frac{\mu\cdot\textsl{m}(AB)}{\mu\cdot\textsl{m}(CD)}=
     \frac{\textsl{m}(AB)}{\textsl{m}(CD)},$$ which had to be proven. \kdokaz


 The concept of dividing a distance in a given ratio is easily extended, so that the ratio is a positive real number.
  We say that a point $T$ divides the distance $AB$ in the \index{delitev daljice!v razmerju}\pojem{ratio} $\lambda \in \mathbb{R}^+$, if $\mathcal{B}(A,T,B)$ and $\frac{AT}{TB}=\lambda$ (Figure \ref{sl.aks.2.4.7.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.7.pic}
\caption{} \label{sl.aks.2.4.7.pic}
\end{figure}

 The equality of two ratios we will call the \pojem{ratio}. So the distances $AB$, $CD$, $EF$ and $GH$ (in this order)  are proportional, if:
  $$\frac{AB}{CD}=\frac{EF}{GH}.$$


On a similar way we define the measure of an angle.

  Let $\mathcal{K}$ be the set of all angles and $\mathbb{R}^+$ the set of all positive real numbers. A mapping $\textsl{l}:\mathcal{K}\rightarrow\mathbb{R}^+$, which satisfies the following properties:
  \begin{itemize}
    \item $(\exists \alpha_0\in\mathcal{K})\hspace*{1mm}\textsl{l}(\alpha_0)=1$,
    \item $(\forall \alpha, \beta\in\mathcal{K})\hspace*{1mm}(\alpha\cong \beta \Rightarrow\textsl{l}(\alpha)=\textsl{l}(\beta))$,
    \item $(\forall \alpha, \beta, \gamma\in\mathcal{K})\hspace*{1mm}(\alpha+\beta=\gamma\Rightarrow \textsl{l}(\alpha)+\textsl{l}(\beta)=\textsl{l}(\gamma))$.
  \end{itemize}
  we call the \index{mera!kota}\pojem{measure of an angle}, and the triple $\textsl{L}=(\mathcal{K},\mathbb{R}^+,\textsl{l})$ the \index{sistem merjenja!kotov}\pojem{measuring system of angles}.

The fact that the measure of the angle $\alpha$ is equal to $x$ (or $\textsl{l}(\alpha)=x$) will be more often written in the form $\alpha=x$.


  Similarly to measuring distances, there exists an infinite number of systems of measuring angles, which depend on the unit angle $\alpha_0$ - the one for which the measure is equal to 1, or $\textsl{l}(\alpha_0)=1$. So in one measuring system, the measure of any angle $\alpha$ is a positive real number $x$, for which $\alpha=x\cdot \alpha_0$. Therefore $\textsl{l}(\alpha)=x$ exactly when $\alpha=x\cdot \alpha_0$. Of course, we must also use the axiom of continuity in order to introduce multiplication of an angle by a positive real number.

  Of all measuring systems, we will highlight two.
  \begin{itemize}
    \item In the first system, which we will use most often, the unit angle is the 180-th part of the extended angle. For this angle we will say that it measures \pojem{one angular degree} and this measure is denoted by $1^0$ (Figure \ref{sl.aks.2.4.8.pic}). So if we use the properties of the measure function $\textsl{l}$, in this system the extended angle measures $180^0$, and the right angle measures $90^0$.
    \item In the second measuring system with \pojem{radians}, denoted by $[\textrm{rad}]$, the extended angle measures $\pi$ (where $\pi$ is an irrational number - $\pi\doteq 3,14$), and the right angle measures $\frac{\pi}{2}$. In this measuring system of angles, the notation $[\textrm{rad}]$ is usually not written.
  \end{itemize}


\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.8.pic}
\caption{} \label{sl.aks.2.4.8.pic}
\end{figure}

  So in both systems we can write the measure of the extended angle $\alpha$ as $\alpha=180^0=\pi$, and the measure of the right angle $\beta$ as $\beta=90^0=\frac{\pi}{2}$ (Figure \ref{sl.aks.2.4.8a.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.4.8a.pic}
\caption{} \label{sl.aks.2.4.8a.pic}
\end{figure}

The general relation between the two measuring systems can be written with the following formulas:

$$1\hspace*{1mm}\textrm{rad}=\frac{180^0}{\pi}, \textrm{ or }
1^0=\frac{\pi}{180^0}\hspace*{1mm}\textrm{rad}.$$



%________________________________________________________________________________
 \poglavje{Playfair's Axiom} \label{odd2AKSVZP}

As a result of the axioms of the previous four groups, we have already proven (the statement \ref{absolGeom}), that for a point $A$, which does not lie on the line $p$, there exists (in this plane) at least one line $q$, that goes through the point $A$ and does not intersect the line $p$ (Figure \ref{sl.aks.2.5.0.pic}).
But is such a line just one? Intuitively, the answer is affirmative. But can we prove it with the axioms we have so far?\footnote{This question is connected with the already mentioned problem of the fifth Euclidean postulate and was open for almost 2000 years.} It turns out that we cannot answer this question if we stay only with the first four groups of axioms.\footnote{This fact was first realized by the Russian mathematician \textit{N. I. Lobachevski} (1792--1856) and the Hungarian mathematician  \textit{J. Bolyai} (1802--1860). The first one to formally prove it was the French mathematician \index{Poincar\'{e}, J. H.} \textit{J. H.
Poincar\'{e}} (1854--1912).} The axioms we have so far form an incomplete system of axioms, because there is a statement, that we can formulate in this
theory, but we cannot determine if it is true or not.
  Therefore, we need to add a new axiom, with which we will decide, whether there is just one such line $q$ or there are more of them.


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

The second option offers the following axiom.

\baksiom \label{Lobac}\index{aksiom!Lobačevskega}
(Lobachevsky's\footnote{Russian mathematician \textit{N. I. Lobachevsky} (1792--1856) and Hungarian mathematician  \textit{J. Bolyai} (1802--1860) independently from each other built the first non-Euclidean geometry, which is based on
this axiom and the axioms of the first four groups.} axiom)
For any given line $p$ and point $A$ not on $p$ (in the plane containing both line $p$ and point $A$), there are
at least two lines  through the point $A$ that do not intersect the line $p$
(Figure \ref{sl.aks.2.5.1.pic}).
\eaksiom



In this way, we get two geometries, each of which is internally consistent.
The first geometry, which is determined by the axioms of the first four groups and Playfair's axiom \ref{Playfair}, is called
\index{geometrija!evklidska}\pojem{planar Euclidean geometry}. The second geometry, which is determined by the axioms of the first four groups and
Lobachevsky's axiom \ref{Lobac}, is called \index{geometrija!hiperbolična}\pojem{planar hyperbolic
geometry}.

Although they are obviously different, the aforementioned geometries have a lot in common. This is clear already because the first four groups of axioms are the same - they only differ in the fifth. The consequences of the first four
groups of axioms that we have considered so far, are valid in
both Euclidean and hyperbolic geometry.
The geometry that is based
 only on the first four groups of axioms, is called
\index{geometrija!absolutna}\pojem{planar absolute geometry}. It determines the common properties of Euclidean and hyperbolic geometry. Because the system of axioms that determines it is incomplete, we say that absolute geometry is a \pojem{incomplete theory}.

Despite the similarity, in hyperbolic geometry there are strange statements that are, of course, a consequence of Lobachevsky's axiom \ref{Lobac} or the negation of Playfair's axiom \ref{Playfair}. The sum of the internal angles of a triangle is always less than $180^0$ and is not constant; a rectangle of one acute angle does not always intersect the other angle; there are even triangles for which there is no inscribed circle, etc. Of course, these statements seem contradictory to us, but they are only contradictory in Euclidean geometry; in hyperbolic geometry they are not. It turns out that hyperbolic geometry - like Euclidean geometry - is a consistent theory\footnote{The consistency of hyperbolic geometry was first proved by the French mathematician \index{Poincaré, J. H.} \textit{J. H. Poincaré} (1854--1912), who built a model of hyperbolic geometry in Euclidean geometry. So the contradiction of hyperbolic geometry would mean a contradiction in Euclidean geometry.}.

In addition to the mentioned geometries, there are also other non-Euclidean geometries. Geometry in which every two lines of a plane intersect is called \index{geometry!elliptical}\pojem{elliptical geometry\footnote{This geometry was developed by the German mathematician \index{Riemann, G. F. B.} \textit{G. F. B. Riemann} (1828--1866).}}. From the already mentioned statement \ref{absolGeom} it is clear that elliptical geometry cannot be built on the axioms of the first four groups or absolute geometry. In this sense, this geometry differs more from Euclidean and hyperbolic geometry.

We also mention \index{geometry!projective}\pojem{projective geometry}. In a certain way, this is the most simple of all the mentioned geometries, because it is based only on three groups of axioms. Also in this geometry every two lines intersect, but unlike elliptical geometry, we do not have a defined metric or a relation of compliance. In projective geometry, it is possible to make models of all three geometries: Euclidean, hyperbolic and elliptical.

We will reiterate that in this book we are only building the Euclidean geometry of a plane. So, at the beginning, we called the set of all points $\mathcal{S}$ a plane. From now on, we will also denote it with $\mathbb{E}^2$ (or $\mathbb{E}^2=\mathcal{S}$). We have chosen only the axioms of a plane and thus obtained the system of axioms of Euclidean geometry of a plane. With a slightly different choice of basic concepts (the basic set of all points $\mathcal{S}$ is called space, certain subsets are lines and planes) and by adding new axioms (we would need to add them already in the first group), we would obtain the \pojem{Euclidean geometry of space} or, shorter, the \index{geometry!Euclidean}\pojem{Euclidean geometry}. In a similar way, we would obtain the \pojem{hyperbolic geometry}\index{geometry!hyperbolic} and the \index{geometry!absolute}\pojem{absolute geometry}.

We will only consider the Euclidean geometry of a plane, so we will always assume that all points, lines, and figures lie in the same plane (because, in this geometry, there are no others anyway). However, for the sake of clarity, we will occasionally emphasize this fact again.

In Euclidean geometry of a plane, it is now possible to introduce a new concept. We say that the lines $p$ and $q$ are \index{vzporednost!premic}\pojem{parallel}, which we denote $p\parallel q$, if they coincide or if they have no common points.
 $$p\parallel q \hspace*{2mm} \Leftrightarrow \hspace*{2mm}p=q \hspace*{1mm}\vee \hspace*{1mm} p\cap q=\emptyset .$$

Of course, in Euclidean geometry (of space), we would also need to add the condition that $p$ and $q$ lie in the same plane.

We can now express Playfair's axiom in the following form.



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

 We will now prove an important property of the defined relation of parallelism.

\bizrek
        The relation of being parallel is an equivalence relation.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.2.pic}
\caption{} \label{sl.aks.2.5.2.pic}
\end{figure}

 \textbf{\textit{Proof.}} It is necessary (and sufficient) to prove that the relation is reflexive, symmetric and transitive (Figure \ref{sl.aks.2.5.2.pic}).


 (\textit{R}) The relation is reflexive by definition, because for every line $p$ it holds $p\parallel p$.

 (\textit{S}) If $p\parallel q$, then by definition it also holds $q\parallel p$, which means that the relation is symmetric.

 (\textit{T}) Assume that $p\parallel q$ and $q\parallel r$ (all three lines are in the same plane). We will prove that $p\parallel r$ also holds. If at least two of the three lines coincide, the proof is trivial. Assume that lines $p$ and $r$ intersect in a point $A$. In this case, through point $A$ there pass at least two lines that do not intersect line $q$, which is in contradiction with Playfair's axiom \ref{Playfair}. Therefore $p\parallel r$ holds, which means that the relation is transitive.
\kdokaz

We will also define the relation of parallelism for segments and distances. Segments (or distances) are \index{parallelism!segments}\index{parallelism!distances}\pojem{parallel}, if their supporting lines are parallel lines.

We will now prove an important theorem of Euclidean geometry.



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

 ($\Rightarrow$) We will first assume that $\angle XAB\cong\angle YBA$. We will mark with $S$ the center of distance $AB$ and with $N$ the orthogonal projection of point $S$ on line $a$ (Figure \ref{sl.aks.2.5.3.pic}).

According to the statement \ref{sredZrcObstoj} there exists an isometry $\mathcal{I}$, which maps the point $S$ to the point $S$, for every point $T\neq S$ and its image $T'=\mathcal{I}(T)$ it holds that $S$ is the center of the line $TT'$. So first $\mathcal{I}:A,B\mapsto B,A$.
 Let $\mathcal{I}(X)=X'$ and $\mathcal{I}(N)=M$. We mark with $n$ the line $NM$. We prove that $n$ is the common perpendicular of the lines $a$ and $b$.

We prove first $\mathcal{I}:a\rightarrow b$ and $M\in b$. Because $S$ is the center of the line $XX'$, $X,X'\div S$ or $X,X'\div l$ and $X',Y\ddot{-} l$. From $\mathcal{I}:B,A,X\mapsto A,B,X'$ it follows $\angle XAB\cong \angle X'BA$. Because $\angle XAB\cong\angle YBA$, also $\angle X'BA\cong\angle YBA$ holds. Because the points $Y$ and $X'$ are also in the same plane $ABY$, according to the statement \ref{KotNaPoltrak} the line segment $BX'$ and $BY$ correspond. This means that the point $X'$ lies on the line segment $BY$, so $X'\in b$ holds. From $\mathcal{I}:A,X\mapsto B,X'$ it now follows (the axiom \ref{aksIII1}) $\mathcal{I}:a\rightarrow b$.
Because $N\in a$, also $\mathcal{I}(N)\in \mathcal{I}(a)$ or $M\in b$ holds.

From $\mathcal{I}:S,N\mapsto S,M$ according to the axiom \ref{aksIII1} it follows $\mathcal{I}:n\rightarrow n$.
So it holds $\mathcal{I}:a,n\rightarrow b,n$, so $\angle b,n\cong a,n=90^0$ or $b\perp n$ holds.
Because $n$ is the common perpendicular of different lines $a$ and $b$, according to the statement  \ref{absolGeom} the lines $a$ and $b$ don't have common points, which means that $a\parallel b$ holds.

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.3a.pic}
\caption{} \label{sl.aks.2.5.3a.pic}
\end{figure}

($\Leftarrow$) Let $a\parallel b$ now (Figure \ref{sl.aks.2.5.3a.pic}). We assume the opposite - that is, that $\angle XAB\cong\angle YBA$ does not hold. According to Theorem \ref{KotNaPoltrak}, there exists such a line segment $BZ$ in the plane $ABY$, that $\angle ZBA\cong\angle XAB$ holds. We mark the line $ZB$ with $b'$. From the first part of the proof ($\Rightarrow$) it follows that $b'\parallel a$. Therefore, both $b$ and $b'$ go through the point $B$ and are parallel to the line $a$ or, in other words, they do not have any common points with it (because $a\neq b$). According to Playfair's axiom, this is not possible, which means that $b=b'$. Therefore, the point $Z$ lies on the line segment $BY$, so $\angle YBA=\angle ZBA \cong\angle XAB$.
\kdokaz

A line $l$, that intersects lines $a$ and $b$, is called their \pojem{transversal}. The angles, that are determined by the line $l$ and lines $a$ and $b$, are called the \index{koti!ob transverzali}\pojem{angles on the transversal}. From the previous theorem \ref{KotiTransverzala} and theorem \ref{sovrsnaSkladna} it follows, that each of the two angles on the transversal $l$ of the parallel lines $a$ and $b$ is either congruent or supplementary (Figure \ref{sl.aks.2.5.3b.pic}).
Therefore, the following theorem holds.

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

\textbf{\textit{Proof.}} Let $\angle aSb$ and $\angle a'S'b'$ be such angles that $a\parallel a'$ and $b\parallel b'$ (Figure \ref{sl.aks.2.5.4.pic}).
 If $b'\parallel a$, by Playfair's axiom, the sides of the $\angle a'S'b'$ match. From this it also follows for the sides of $\angle aSb$, which means that $\angle aSb$ and $\angle a'S'b'$ are both extended and consistent.
 With $S_1$ we mark the intersection of the sides of $\angle aSb$ and $\angle b'S'$. By the previous theorem \ref{KotiTransverzala1}, each of the two angles at the transversal $SS_1$ of the sides of $\angle b$ and $\angle b'$ is either congruent or supplementary to the angle at the transversal $S_1S'$ of the sides of $\angle a$ and $\angle a'$. Similarly, the angle $\angle aSb$ and $\angle a'S'b'$ are either congruent or supplementary.
 \kdokaz


In the following we will deal with the internal and external angles of a polygon. We start with a triangle.


         \bizrek \label{VsotKotTrik} The sum of the interior angles of a triangle is equal to
         $180^0$.
          \eizrek

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.7.pic}
\caption{} \label{sl.aks.2.5.7.pic}
\end{figure}

 \textbf{\textit{Proof.}} Let $ABC$ be an arbitrary triangle  (Figure \ref{sl.aks.2.5.7.pic}). By the consequence of Playfair's axiom \ref{Playfair1}, there is only one line $l$, which is parallel to the line $BC$. Let $Y$ and $Z$ be such points of the line $l$, that $Y,B\div AC$ and $Z,C\div AB$. The line $AB$ is the transversal of the sides of $BC$ and $l$. Because $Z,C\div AB$, by theorem \ref{KotiTransverzala}
 $\angle ABC\cong\angle ZAB$. Similarly, the line $AC$ is the transversal of the sides of $BC$ and $l$, so from  $Y,B\div AC$ and theorem \ref{KotiTransverzala} it follows that $\angle BCA\cong\angle YAC$. In the end we have:
  $$\angle ABC +\angle BAC +\angle BCA = \angle ZAB +\angle BAC +\angle CAY=\angle ZAY=180^0,$$ which was to be proven. \kdokaz

 The following theorems are very useful.


          \bizrek \label{zunanjiNotrNotr}
          An exterior angle of a triangle is equal to the sum of the two opposite interior angles.
           \eizrek

\textbf{\textit{Proof.}}  Let $ABC$ be an arbitrary triangle  (Figure \ref{sl.aks.2.5.6.pic}). We denote its internal angles at the vertices $A$, $B$ and $C$ with $\alpha$, $\beta$ and $\gamma$, and the corresponding external angles with  $\alpha'$, $\beta'$ and $\gamma'$. Without loss of generality, it is enough to prove that $\alpha+\beta=\gamma'$.
 From the previous  \ref{VsotKotTrik} follows: $$\alpha+\beta+\gamma=180^0.$$ Because both are external and internal angle to him by definition of a supplement, it is also $$\gamma'+\gamma=180^0.$$ From the previous two relations we obtain:
  $$\alpha+\beta=\gamma',$$ which had to be proven. \kdokaz

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.6.pic}
\caption{} \label{sl.aks.2.5.6.pic}
\end{figure}

A direct consequence is the following theorem.


       \bizrek \label{zunanjiNotrNotrVecji}
       An exterior angle of a triangle is greater than either opposite interior angle.
        \eizrek

\textbf{\textit{Proof.}} We introduce the same notation as in the previous  \ref{zunanjiNotrNotr} (Figure \ref{sl.aks.2.5.6.pic}). Without loss of generality, it is enough to prove that $\gamma'>\alpha$ and $\gamma'>\beta$. The relations are a direct consequence of the proven inequality $\alpha+\beta=\gamma'$ from the previous  \ref{zunanjiNotrNotr}.
 \kdokaz

Based on the internal angles, we can consider three types of triangles.
 We have already proven
  that in any triangle the sum of the internal angles is equal to $180^0$
  (the statement  \ref{VsotKotTrik}).
This means that at most one of these angles is a right angle or a reflex angle,
or at least two are acute. So we have three possibilities (Figure
\ref{sl.aks.2.6.4a.pic}):
\begin{itemize}
  \item The triangle is \index{trikotnik!ostrokotni}
  \pojem{acute-angled}, if all of its internal angles are acute.
  \item The triangle is \index{trikotnik!pravokotni}\pojem{right-angled},
    if it has one internal angle that is a right angle. The side opposite
the right angle of a right-angled triangle is called
\index{hipotenuza}\pojem{the hypotenuse}, the other two sides are
\index{kateta}\pojem{the catheti}. Because the sum of the internal angles in any
  triangle is equal to $180^0$, the
angles at the hypotenuse of a right-angled triangle are complementary.
  \item The triangle is \index{trikotnik!topokotni}\pojem{obtuse-angled},
  if it has one internal angle that is obtuse.
  The other two internal angles are then acute.
\end{itemize}

\begin{figure}[!htb]
\centering
\input{sl.aks.2.6.4a.pic}
\caption{} \label{sl.aks.2.6.4a.pic}
\end{figure}

%slika 33.1

 We will now prove a statement that applies to any $n$-gon.



         \bizrek \label{VsotKotVeck}
         The sum of the interior angles of any $n$-gon is equal to
         $(n - 2) \cdot 180^0$.
          \eizrek




\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5c.pic}
\caption{} \label{sl.aks.2.5.5c.pic}
\end{figure}

\textbf{\textit{Proof.}} First, let's assume that $A_1A_2\ldots A_n$ is a convex $n $-gon (Figure \ref{sl.aks.2.5.5c.pic}). Its $n-3$ diagonals $A_1A_3$, $A_1A_4$, ... $A_1A_{n-1}$ divide this polygon into $n-2$ triangles $\triangle_1$, $\triangle_2$, ..., $\triangle_{n-2}$. Because each internal angle of the $n $-gon $A_1A_2\ldots A_n$ is divided into the appropriate internal angles of the aforementioned triangles, the sum of all internal angles
 $n $-gon  $A_1A_2\ldots A_n$ is equal to the sum of all angles of triangles  $\triangle_1$, $\triangle_2$, ..., $\triangle_{n-2}$. By Theorem \ref{VsotKotTrik} in the end this sum is equal to exactly $(n - 2) \cdot 180^0$.

 At this point we will not prove the fact that even in the case of a non-convex $n $-gon  $A_1A_2\ldots A_n$ it can be divided into $n-2$ triangles.
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

 \textbf{\textit{Proof.}} We mark with $\alpha_1$, $\alpha_2$,..., $\alpha_n$ the internal and $\alpha'_1$, $\alpha'_2$, ..., $\alpha'_n$ the corresponding external angles at the vertices $A_1$, $A_2$,...,$A_n$ of a convex $n $-gon  $A_1A_2\ldots A_n$. (Figure \ref{sl.aks.2.5.5b.pic}). For the appropriate internal and external angle we have:

 \begin{eqnarray*}
 & & \alpha_1+\alpha'_1=180^0\\
 & & \alpha_2+\alpha'_2=180^0\\
 & & \vdots\\
 & & \alpha_n+\alpha'_n=180^0
 \end{eqnarray*}

 If we add all the equalities and take into account the proven equality from the previous theorem \ref{VsotKotVeck} $$\alpha_1+\alpha_2+\cdots + \alpha_n=(n - 2) \cdot 180^0,$$
  we get $(n - 2) \cdot 180^0+\alpha'_1+\alpha'_2+\cdots + \alpha'_n=n\cdot 180^0$ or
  $$\alpha'_1+\alpha'_2+\cdots + \alpha'_n=2 \cdot 180^0=360^0,$$ which was to be proven. \kdokaz

From the statement \ref{VsotKotVeck} it follows that the sum of all the internal angles of an arbitrary quadrilateral is equal to $360^0$, and from the statement \ref{VsotKotVeckZuna} it also follows that the sum of all the external angles of a convex quadrilateral is equal to $360^0$ (Figure \ref{sl.aks.2.5.5a.pic}).



\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5a.pic}
\caption{} \label{sl.aks.2.5.5a.pic}
\end{figure}



 Because a triangle (as the intersection of three planes) is a convex figure, the sum of all the external angles of an arbitrary triangle is equal to $360^0$ (Figure \ref{sl.aks.2.5.5d.pic}).

\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5d.pic}
\caption{} \label{sl.aks.2.5.5d.pic}
\end{figure}


A similar claim, based on the statement \ref{KotaVzporKraki}, which refers to an angle with parallel sides, also applies to an angle with perpendicular sides.



        \bizrek \label{KotaPravokKraki}
        Angles with perpendicular sides are either congruent or supplementary.
         \index{kota!s pravokotnimi kraki}
        \eizrek



\begin{figure}[!htb]
\centering
\input{sl.aks.2.5.5.pic}
\caption{} \label{sl.aks.2.5.5.pic}
\end{figure}


 \textbf{\textit{Proof.}} Let $\angle aSb$ and $\angle a'S'b'$ be such angles that $a\perp a'$ and $b\perp b'$ (Figure \ref{sl.aks.2.5.5.pic}). Let $A$ be the intersection of the sides of $a$ and $a'$, and $B$ be the intersection of the sides of $b$ and $b'$. In the quadrilateral $SAS'B$, the internal angles at the vertices $A$ and $B$ each measure $90^0$. According to the statement \ref{VsotKotVeck}, the sum of all the internal angles of this quadrilateral is equal to $360^0$. Therefore, the internal angle $BSA$ and $AS'B$ of this quadrilateral measure together $180^0$, which means that two angles, determined by the sides of $a$ and $b$ or $a'$ and $b'$, are supplementary. However, if we replace one of these angles with its supplement, the corresponding angles are congruent.
 \kdokaz


%________________________________________________________________________________
\naloge{Exercises}
\begin{enumerate}

\item Let $P$, $Q$ and $R$ be the internal points of the sides of a triangle
$ABC$. Prove that $P$, $Q$ and $R$ are non-collinear.

\item Let $P$ and $Q$ be points on sides $BC$ and $AC$ of triangle $ABC$ and at the same time different from its vertices. Prove that the line segments $AP$ and $BQ$ intersect in one point.

\item Points $P$, $Q$ and $R$ are located in order on sides $BC$, $AC$ and $AB$ of triangle $ABC$ and are different from its vertices. Prove that the line segments $AP$ and $QR$ intersect in one point.

\item A line $p$, which lies in the plane of the quadrilateral, intersects its diagonal $AC$ and does not pass through any vertex of this quadrilateral. Prove that the line $p$ intersects exactly two sides of this quadrilateral.

\item Prove that the half-line is a convex figure.

\item Prove that the intersection of two convex figures is a convex figure.

\item Prove that any triangle is a convex figure.

\item If $\mathcal{B}(A,B,C)$ and $\mathcal{B}(D,A,C)$, then $\mathcal{B}(B,A,D)$ is also true. Prove it.

\item Let $A$, $B$, $C$ and $D$ be such collinear points that $\neg\mathcal{B}(B,A,C)$ and $\neg\mathcal{B}(B,A,D)$ are true. Prove that $\neg\mathcal{B}(C,A,D)$ is also true.

\item Let $A_1A_2\ldots,A_{2k+1}$ be an arbitrary polygon with an even number of vertices. Prove that there is no line that intersects all of its sides.

\item If izometry $\mathcal{I}$ maps figure $\Phi_1$ and $\Phi_2$ into figure  $\Phi'_1$ and $\Phi'_2$, then the intersection $\Phi_1\cap\Phi_2$ is mapped by this izometry into the intersection $\Phi'_1\cap\Phi'_2$. Prove it.

\item Prove that any two strips of a plane are compatible with each other.

\item Prove that any two lines of a plane are compatible with each other.


\item Let $k$ and $k'$ be two circles of a plane with centers $O$ and $O'$ and radii $AB$ and $A'B'$. Prove the equivalence: $k\cong k' \Leftrightarrow AB\cong A'B'$.

\item Let $\mathcal{I}$ be a non-identical izometry of a plane with two fixed points $A$ and $B$. If $p$ is a line of this plane, which is parallel to the line $AB$ and $A\notin p$. Prove that there are no fixed points of izometry $\mathcal{I}$ on the line $p$.

\item   Let $S$ be the only fixed point
of the isometry $\mathcal{I}$ in some plane. Prove that if this isometry
maps the line $p$ to itself, then $S\in p$.

\item  Prove that any two lines
of a plane either intersect or are parallel.

\item  If a
line in a plane intersects one of the two parallel lines of the same plane,
 then it also intersects the other parallel line. Prove.

\item  Prove that every isometry maps a parallel line to a parallel line.

\item  Let $p$, $q$ and $r$ be such lines of a plane that
$p\parallel q$ and $r\perp p$. Prove that $r\perp q$.

\item Prove that a convex $n$-gon cannot have more than three
acute angles.

\end{enumerate}



% DEL 3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
% SKLADNOST TRIKOTNIKOV. VEČKOTNIKI
%________________________________________________________________________________

 \del{Congruence. Triangles and Polygons} \label{pogSKL}

%________________________________________________________________________________
 \poglavje{Triangle Congruence Theorems} \label{odd3IzrSkl}

From the general definition of the congruence of figures it follows that two
triangles are congruent if there exists an isometry that maps the first triangle to
the second. It is clear that from the congruence of two triangles follows the
congruence of the corresponding sides and interior angles. We are interested in the inverse problem:
When does the congruence of some of
the corresponding sides and angles imply the congruence of two triangles? This is
expressed by the following \index{statement!about the congruence
of triangles}\emph{triangle congruence theorems}\footnote{The first, third and fourth triangle congruence theorems are attributed to \index{Pythagoras} \textit{Pythagoras of Samos} (6th century BC), while the second theorem is assumed to have been known to \index{Thales} \textit{Thales of Miletus} (7th--6th century BC). All four
are mentioned by \index{Euclid} \textit{Euclid of Alexandria}
(3rd century BC) in the first book of his \textit{Elements}.}:

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
 From the congruence of sides by \ref{izrek(A,B)} there is also $(A,B)
 \cong (A',B')$, $(B,C) \cong (B',C')$
 and $(A,C)
 \cong (A',C')$ or $(A,B,C) \cong (A',B',C')$. From
 \ref{IizrekABC} it follows that there is an isometry $\mathcal{I}$, which
 maps points $A$, $B$ and $C$ to points $A'$, $B'$ and $C'$.
 It maps triangle $ABC$ to triangle $A'B'C'$, which is
 a consequence of \ref{izrekIzoB}. So triangles $ABC$ and
 $A'B'C'$ are congruent.
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
  Because angles $BAC$ and $B'A'C'$ are congruent,
  there exists an isometry $\mathcal{I}$, which maps angle $BAC$ to angle $B'A'C'$.
  This isometry maps point $A$ to point $A'$, and segments $AB$ and $AC$ to $A'B'$ and $A'C'$.
  Let $\mathcal{I}(B)=\widehat{B}'$ and  $\mathcal{I}(C)=\widehat{C}'$.
  From this
  it follows that $AB \cong A'\widehat{B}'$ and $AC \cong A'\widehat{C}'$,
  but according to \ref{ABnaPoltrakCX} we have that $\widehat{B}'=B'$ and
  $\widehat{C}'=C'$.
  So the isometry $\mathcal{I}$
  maps points $A$, $B$ and $C$ to points $A'$, $B'$ and $C'$,
  or triangle $ABC$ to triangle $A'B'C'$, which means that triangles $ABC$ and
  $A'B'C'$ are congruent.
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
 From axiom \ref{aksIII2} it follows that there exists an isometry  $\mathcal{I}$,
  that maps
 point $A$ to point $A'$, line segment $AB$ to line segment $A'B'$ and
 plane $ABC$ to plane $A'B'C'$.
 Because $AB \cong A'B'$, from the same axiom it follows
 $\mathcal{I}(B)=B'$. Let $\mathcal{I}(C)=\widehat{C}'$.
 Then $\angle BAC \cong \angle B'A'\widehat{C}'$ and
   $\angle ABC \cong \angle A'B'\widehat{C}'$.
  Because according to the assumption also $\angle BAC \cong \angle B'A'C'$ and
   $\angle ABC \cong \angle A'B'C'$, from 
   \ref{KotNaPoltrak} it follows that line segments $A'\widehat{C}'$ and
   $A'\widehat{C}'$ (or $B'C'$ and
   $B'\widehat{C}'$) are equal. Therefore $\widehat{C}'=A'\widehat{C}'\cap
   A'\widehat{C}'=A'C'\cap
   A'C'=C'$. So $\mathcal{I}:A,B,C \mapsto A',B',C'$, therefore triangles $ABC$ and $A'B'C'$ are congruent.
 \kdokaz

We will omit the proof of the fourth statement about congruent triangles.

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


One of the most important consequences of theorems about the congruence of triangles is the following statement.



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
 Let $ABC$ be such a triangle that $AB \cong AC$
 (Figure \ref{sl.skl.3.1.5.pic}). Because $AC \cong AB$ and $BC \cong CB$ still hold, from the \textit{SSS} theorem it follows that
the triangles $ABC$ and $ACB$ are congruent (these two triangles have
different orientations). Therefore, $\angle ABC \cong \angle CBA$. In the same way, we could have proven the converse statement. In this case, we would have used the \textit{ASA} theorem.
 \kdokaz

 A triangle (as is the triangle $ABC$ from the previous theorem),
 which has at least two
sides congruent, is called
\index{trikotnik!enakokraki}\pojem{an isosceles triangle}. Each of the
two congruent sides is a \index{krak!enakokrakega
trikotnika}\pojem{arm}, and the third side is
\index{osnovnica!enakokrakega trikotnika}\pojem{the base} of this
triangle. So, according to the previous theorem, the angles at the
base of an isosceles triangle are congruent. And vice versa - if two
angles of a triangle are congruent, then this triangle is isosceles.

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

 The internal angle of the triangle $ABC$ at the
 vertices
 $A$ and $B$ we denote by $\alpha$ and
  $\beta$.
 The triangle $EAC$ and $CBF$ are
 isosceles triangles with the bases $CE$ and $CF$, so $\angle CEA \cong \angle ACE$ and
 $\angle CFB \cong \angle BFC$ (statement \ref{enakokraki}). The
 $\alpha$ is the external angle of the triangle $EAC$, so by the statement \ref{zunanjiNotrNotr}:
  $\alpha = 2\angle ECA$ or  $\angle ECA = \frac{1}{2} \alpha$.
  Similarly, $\angle FCB = \frac{1}{2} \beta$. Therefore:
\begin{eqnarray*}
   \angle ECF&=&\angle ECA+\angle ACB+\angle BCF=\\
   &=&\frac{1}{2}
   \cdot\alpha+90^0+
    \frac{1}{2} \cdot\beta=90^0+
    \frac{1}{2} \cdot\left(\alpha+\beta\right)=\\
    &=&90^0+
    \frac{1}{2}\cdot 90^0=135^0,
    \end{eqnarray*}
or $\angle ECF=135^0$. \kdokaz

A triangle in which all sides are equal is called
\index{trikotnik!enakostranični}\pojem{an equilateral triangle}
(Figure \ref{sl.skl.3.1.7.pic}), which is a special case
of an isosceles triangle. Therefore, from the above statement it follows that
all the internal angles of an equilateral triangle are equal. Since their sum is equal to $180^0$, each of these angles measures $60^0$. The converse is also true: if at least two angles of a triangle are equal to $60^0$ (and therefore also the third one), then this triangle is equilateral.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.7.pic}
\caption{} \label{sl.skl.3.1.7.pic}
\end{figure}

\bzgled
Let $ABC$ be an equilateral triangle and $P$, $Q$ and $R$ points such that $\mathcal{B}(A,B,R)$, $\mathcal{B}(B,C,Q)$, $\mathcal{B}(C,A,P)$ and
$BR\cong CQ\cong AP$. Prove that $PQR$ is also an equilateral triangle.
\ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.8.pic}
\caption{} \label{sl.skl.3.1.8.pic}
\end{figure}


 \textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.1.8.pic})

 From the given conditions, it follows first that
  $AR\cong BQ\cong CP$. The triangle $ABC$ is an equilateral triangle,
  so all three internal angles measure $60^0$. From this it follows
  that $\angle PAR\cong \angle RBQ\cong QCP$. By the \textit{SAS} theorem,
  the triangles $PAR$, $RBQ$ and $QCP$ are similar and $PR\cong RQ\cong QP$.
  This means that $PQR$ is also an equilateral triangle.
 \kdokaz


In the previous chapter we defined the perpendicular bisector of a line segment as the line that is perpendicular to the line segment and goes through its center. Now we prove an equivalent definition of the perpendicular bisector, which will be very important in the sequel. \index{perpendicular bisector}


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
   Let $s$ be a line that is the perpendicular bisector of the line
segment $AB$ in some plane. By definition, $s$ is perpendicular to the line
$AB$ through its center - the point $S$. We denote by $\mathcal{M}$
the set of all points $X$ in this plane, for which $AX \cong BX$.
It is necessary to prove that $s =\mathcal{M}$. We will prove this by two inclusions (Figure \ref{sl.skl.3.1.9.pic}).

($s\subseteq \mathcal{M}$). Let $X \in s$. We will prove that
then $X \in \mathcal{M}$ is true. From the relations $AS \cong BS$, $XS \cong XS$
and $\angle ASX \cong \angle BSX = 90^0$ it follows that the triangles
$ASX$ and $BSX$ are congruent (theorem \ref{SAS}). Therefore $AX \cong BX$
or $X \in \mathcal{M}$.

($\mathcal{M}\subseteq s$). Now let $X \in \mathcal{M}$.
We will prove that $X \in s$ is true. From $X \in \mathcal{M}$ it follows that $AX \cong BX$.
Now from $AS \cong BS$, $XS \cong XS$ and $AX \cong BX$ it follows that
the triangles $ASX$ and $BSX$ are congruent (theorem \ref{SSS}). Therefore the angles
$ASX$ and $BSX$ are congruent and the angle between the lines is both a right angle. This means that
the line $XS$ is perpendicular to the line segment $AB$ in its center.
Therefore, the line $XS$ is the perpendicular bisector of $s$ or $X \in s$.
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

\textbf{\textit{Solution.}} Let's mark the interior angles of triangle $ABC$ with
$\alpha=60^0$, $\beta$ and $\gamma$. Let $D$ and $E$ be such
points that $BD\cong BP$, $\mathcal{B}(A,B,D)$, $QE \cong QB$
and $\mathcal{B}(A,Q,E)$ (Figure \ref{sl.skk.4.9.IMO1.pic}). From these
conditions it follows that $DBP$ and $BQE$ are isosceles triangles with
bases $DP$ and $BE$. From the given condition $|AB|+|BP|=|AQ|+|QB|$
it also follows that $AD\cong AE$, which means that $ADE$ is also an isosceles triangle with base $DE$.

Since $DBP$ is an isosceles triangle, from the statements \ref{enakokraki} and \ref{zunanjiNotrNotr} it follows: $\angle BDP\cong \angle BPD =\frac{1}{2}\angle ABC=\frac{1}{2}\beta$.
Since $BQE$ is also an isosceles triangle, $\angle QBE\cong\angle QEB$ follows.
From the congruence of triangles $ADP$ and $AEP$ (the statement \textit{SAS} \ref{SKS}) it follows that $\angle ADP\cong \angle AEP$ and $PD\cong PE$.

If we connect the proven relations, it holds:
 \begin{eqnarray*}
&& \angle AEP\cong \angle BDP
=\frac{1}{2}\beta\cong \angle QBP\\
&&\textrm{ and } \angle AEB\cong\angle QBE
 \end{eqnarray*}

 Let's first assume that $QB>QC$ or $\mathcal{B}(Q,C,E)$ holds. In this case:
 \begin{eqnarray*}
 \angle PEB &=&\angle AEB-\angle AEP=\\
 &=&\angle QBE-\angle QBP=\\
 &=&\angle PBE.
 \end{eqnarray*}
This means that $PBE$ is an isosceles triangle with the base $BE$ or $PE\cong PB$. But from the already proven $PE\cong PD$ and the assumption $PB\cong BD$ it follows that $PD\cong PB\cong BD$, therefore $BDP$ is an equilateral triangle. From this it follows that $\beta=2\angle BDP=2\cdot 60^0=120^0$, or $\alpha+\beta=60^0+120^0=180^0$, which is not possible (the statement \ref{VsotKotTrik}). Therefore the relation $QB>QC$ is not possible.

In a similar way, the relation $QB>QC$ leads to a contradiction. This means that only $QB\cong QC$ is possible. In this case $C=E$ and $\gamma=\angle ACB=\angle AEB\cong AEP=\frac{1}{2}\beta$ holds. From $\alpha+\beta+\gamma=180^0$, it follows that $60^0+\beta+\frac{1}{2}\beta=180^0$ or $\beta=80^0$.

We have shown that from the conditions of the task it follows that $\beta=80^0$. So the only possible solution is $\beta=80^0$. It is still necessary to show that $\beta=80^0$ is a solution, or that from $\alpha=60^0$, $\beta=80^0$ it follows that $|AB|+|BP|=|AQ|+|QB|$.
First, from $\angle QCB=\gamma=\frac{1}{2}\beta=40^0=\angle QBC$ it follows
 (from the statement \ref{enakokraki}) $QC\cong QB$ or
 $|AQ|+|QB|=|AQ|+|QC|=|AC|$.
If we define the point $D$ in the same way as in the first part, we again
get $\angle ADP\cong \angle BPD=\frac{1}{2}\angle ABC=40^0=\angle ACB=\angle ACP$.
This means that the triangles
$ADP$ and $ACP$ are congruent (from the statement \textit{ASA} \ref{KSK}) or
$AD\cong AC$. Therefore, in the end:
 $$|AB|+|BP|=|AB|+|BD|=|AD|=|AC|=|AQ|+|QB|,$$ which had to be proven. \kdokaz



%________________________________________________________________________________
 \poglavje{Constructions in Geometry} \label{odd3NacrtNaloge}

At the next example we will describe the so-called design tasks.


             \bzgled \label{načrt1odd3}
              Two congruent line segments $AB$ and $A'B'$ in a plane are given.
              Construct a point $C$ such that $\triangle ABC \cong \triangle A'B'C$.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.1.10.pic}
\caption{} \label{sl.skl.3.1.10.pic}
\end{figure}

 \textbf{\textit{Solution.}} We assume that $C$ is a point in the plane of the segments, for
 which $\triangle ABC \cong \triangle A'B'C$. Then $AC\cong A'C$
 and  $BC\cong B'C$ or the point $C$ lies on the perpendiculars of the segments $AA'$
 and $BB'$ (from the statement  \ref{simetrala}). This fact allows us to construct
  (Figure \ref{sl.skl.3.1.10.pic}).

 We draw the perpendiculars of the segments $AA'$
 and $BB'$. We get the point $C$ as their intersection.

 We prove that $C$ is the desired point or that it satisfies the conditions of
 the task. By assumption, $AB\cong A'B'$ already. Because we got the point $C$ as
 the intersection of the perpendiculars of the segments $AA'$
 and $BB'$, it is  $AC\cong A'C$ and $BC\cong B'C$. From the statement \ref{SSS} (SSS) it follows that the triangles $ABC$ and $A'B'C$
 are congruent.

The task has a solution (one) exactly when the lines of symmetry
  $AA'$
 and $BB'$ intersect, or when the lines $AA'$
 and $BB'$ are not parallel.
  \kdokaz

  The previous example is therefore called the \index{task!design}
   \pojem{design task}, in which
  for the given data it is necessary to plan or construct a new element or figure,
  which in relation to the given data
  satisfies certain conditions. The \pojem{planning} or \index{construction}
  \pojem{construction}
   means
  the use of a ruler and a compass or the use of
  \index{construction!elementary}
  \pojem{elementary construction}:\label{elementarneKonstrukcije}
\begin{itemize}
  \item for the given points $A$ and $B$ we draw:
 \begin{itemize}
  \item the line $AB$,
  \item the line segment $AB$,
  \item the midpoint $AB$;
\end{itemize}
 \item we draw the circle $k$:
\begin{itemize}
  \item with the center $S$, which goes through the given point $A$,
  \item with the center $S$ and the radius, which is consistent with the given
  line segment;
\end{itemize}
\item we draw the circular arc with the given center and radius,
\item we draw the intersection (or intersections):
\begin{itemize}
  \item of two lines,
  \item of a line and a circle,
  \item of two circles.
\end{itemize}
\end{itemize}

  The solution to the design task (draw the figure $\Phi$, which satisfies the conditions
  $\mathcal{A}$) is formally composed of four steps:
\begin{itemize}
  \item \textit{analysis} - in which we assume that
  the figure $\Phi$ is already designed and satisfies the conditions $\mathcal{A}$, then
  we look for new conditions $\mathcal{B}$, which the figure satisfies.
  These follow from the conditions $\mathcal{A}$ and are more favorable for
  the construction of the figure $\Phi$. We prove
  $\mathcal{A}\Rightarrow \mathcal{B}$.
  \item \textit{construction} - we plan the figure $\Phi'$, which satisfies
   the conditions
   $\mathcal{B}$. We exactly describe the course of the design.
  \item \textit{proof} - we prove that $\Phi' = \Phi$ or
  $\mathcal{B}\Rightarrow \mathcal{A}$.
  \item \textit{discussion} - we investigate
  the number of task solutions, depending on the conditions  $\mathcal{A}$.
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


 \textbf{\textit{Analysis.}} Let $ABC$ be a triangle, where $BC \cong a$, the sum of $AB+AC$ is equal to the given line segment $l$ and
$\angle BAC\cong \alpha$ (Figure \ref{sl.skl.3.1.10a.pic}). Let $D$ be a point on the line segment $BA$, such that $AD\cong AC$ and points $B$ and $D$ are on different sides
of point $A$. Therefore $BD=BA+AD=AB+AC=l$ or $BD\cong l$. Triangle $ACD$ is isosceles, so the angles $ADC$ and $ACD$
are congruent by Theorem \ref{enakokraki}. Because they are also the interior
angles of triangle $CAD$, both are equal to half of the exterior angle $BAC$ of this triangle (Theorem  \ref{zunanjiNotrNotr}), or
 $\angle BDC=\angle ADC\cong \angle ACD=\frac{1}{2}\angle BAC=\frac{1}{2}\alpha$.
 This allows us
to construct triangle $BCD$.

\textbf{\textit{Construction.}} First, let's construct triangle $BCD$, where
$\angle BDC=\frac{1}{2}\alpha$,
 $BC\cong a$ and $BD\cong l$,
then point $A$ as the intersection of the line segment $CD$'s perpendicular with line segment $BD$. We will prove that $ABC$
is the desired triangle.

\textbf{\textit{Proof.}} First, $BC\cong a$ by construction. By construction, point $A$ lies on the perpendicular of line
segment $CD$, so $AD\cong AC$ (Theorem \ref{simetrala}). Therefore triangle $CAD$ is isosceles with the base $CD$, so it is (Theorem \ref{enakokraki}) also $\angle ADC\cong \angle ACD$. Because of this, (Theorem \ref{zunanjiNotrNotr}) $\angle BAC = 2 \cdot \angle BDC= 2\cdot\frac{1}{2}\alpha=\alpha$. From $AD\cong AC$ it follows
 $AB + AC = AB + AD = BD \cong l$
.

\textbf{\textit{Discussion.}} The task has a solution (namely one or two) exactly when
the line segment $DC$ intersects the circle $k(B,a)$
and the perpendicular of line segment $CD$ intersects line segment $BD$.
 \kdokaz

In the future, we will not carry out all the steps in every design task.
In most cases, we will only do the first step and thus indicate
the course of the solution.




%________________________________________________________________________________
 \poglavje{Triangle inequality} \label{odd3NeenTrik}

First, we will prove two important expressions that are a consequence
of theorems about the congruence of triangles.

            \bizrek \label{vecstrveckot}
            One side of a triangle is longer than another side of a triangle if and only if
            the measure of the angle opposite the longer side is greater than the angle opposite the shorter side.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.1.pic}
\caption{} \label{sl.skl.3.2.1.pic}
\end{figure}

 \textbf{\textit{Proof.}} Let $ABC$ be a triangle in which $AC > AB$ (Figure \ref{sl.skl.3.2.1.pic}).
 We prove that then $\angle ABC > \angle ACB$. Because $AC > AB$, there is
such a point $B'$ between points $A$ and $C$, for which $AB \cong AB'$.
Then the triangle $BAB’$ is isosceles and $\angle ABB' \cong \angle AB'B$ (theorem \ref{enakokraki}).
The segment $BB'$ is inside the angle $ABC$, so $\angle ABC > \angle ABB '$.
Then $\angle AB'B$ is the external angle of the triangle $BCB'$. By
  theorem  \ref{zunanjiNotrNotrVecji} this angle is greater than its adjacent internal
angle $B'CB$. If we use what has been proven so far, we get:
 $$\angle ABC >
\angle ABB ' \cong \angle AB'B > \angle B'CB \cong \angle ACB.$$
 Therefore $\angle ABC
> \angle ACB$. In a similar way, we prove that the converse is also true.
\kdokaz

 If we denote the lengths of the sides $BC$, $AC$ and
 $AB$ of the triangle $ABC$ with $a$, $b$ and $c$, and the measures of the opposite angles at the vertices $A$, $B$ and $C$ with $\alpha$, $\beta$ and $\gamma$, we can write the previous theorem
 in the form:
  $$a > b \Leftrightarrow \alpha > \beta,$$
  the theorem about the isosceles triangle \ref{enakokraki} in the form:
 $$a = b \Leftrightarrow \alpha = \beta.$$


 This means that both expressions $a-b$ and $\alpha-\beta$ are both positive,
 both negative or both equal to zero. Thus we have proven the following property:

\bzgled \label{vecstrveckotAlgeb}
            For each triangle $ABC$ is:
             $$(a-b)(\alpha-\beta)\geq 0, \hspace*{4mm}
             (b-c)(\beta-\gamma)\geq 0, \hspace*{4mm}
             (c-a)(\gamma-\alpha)\geq 0$$
            \ezgled

The following proposition follows directly from 
\ref{vecstrveckot}:


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

 The sum of the inner angles of a triangle is equal to $180^0$. Therefore, in
a right-angled triangle, the largest angle is a right angle. The hypotenuse of a right-angled triangle is the longest side of this triangle according to the previous proposition. We can similarly prove this for an obtuse triangle.
 \kdokaz

A line $AA'$ is the \index{height!of a triangle}\pojem{height} of a triangle $ABC$, if $AA'\perp BC$ and $A'\in BC$. The latter of the two relations means that the point $A'$ lies on the line $BC$, but not necessarily on the line segment $BC$. The relation $\mathcal{B}(B,A',C)$ is valid exactly when both of the internal angles at the vertices $B$ and $C$ are acute (Figure \ref{sl.skl.3.2.3.pic}). This is a consequence of the theorem about the sum of the internal angles of any triangle (theorem \ref{VsotKotTrik}). In the case that $\angle ABC\geq 90^0$ and $\mathcal{B}(B,A',C)$, the sum of the internal angles in the triangle $ABA'$ would be greater than $180^0$. So the height of a triangle is not always inside the triangle. In a right triangle, the heights from the two vertices with acute angles are equal to the corresponding catheti. The heights from the vertices $A$, $B$ and $C$ are usually denoted by $v_a$, $v_b$ and $v_c$. From the previous theorem \ref{vecstrveckotHipot} it follows that the length of the height of any triangle is less than or equal to the length of the opposite side of that triangle, e.g.: $v_a\leq b$, $v_a\leq c$, ...

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.3.pic}
\caption{} \label{sl.skl.3.2.3.pic}
\end{figure}

Now we will solve a design problem in which the height of a triangle is given as data.

\bzgled
        	 Construct a triangle $ABC$ such that the sides $AB$,
            $AC$ and the altitude  from the vertex $B$ are congruent to the three given line segments $c$, $b$ and $v_b$.
        \ezgled



\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.4a.pic}
\caption{} \label{sl.skl.3.2.4a.pic}
\end{figure}

\textbf{\textit{Analysis.}} Let $ABC$ be a triangle for which $AB\cong c$,
 $AC\cong b$ and $AD\cong v_b$ (where $BD$ is the height of this triangle from the vertex $B$). In the right triangle $ABD$
therefore the known hypotenuse $AB\cong c$ and the cathetus
$AD\cong v_b$ are known, which means that we can design it. The third vertex $C$ of the triangle $ABC$ lies on the line $AD$ (Figure \ref{sl.skl.3.2.4a.pic}).

\textbf{\textit{Construction.}} Let's first draw a rectangular triangle
$ABD$ (with conditions: $AB \cong c$, $\angle ADB = 90^0$ and $BD \cong v_b$). On the line $AD$ then determine such a point $C$,
so that $AC \cong b$. Prove that $ABC$ is the desired triangle.


\textbf{\textit{Proof.}} First, $AB \cong c$ and
 $AC \cong b$ already by construction. Since $\angle ADB = 90^0$, $BD$ is the height of the triangle $ABC$ from the vertex $B$ and is consistent with the distance $v_b$ by construction.


\textbf{\textit{Discussion.}} The task has a solution exactly when it is possible
construction of the triangle $ABD$ or $hb \leq c$. In the construction of point $C$
there are two possibilities - on different sides of point $A$, which means that we have two solutions for triangle $ABC$. In the case $hb \cong c$, the solutions are a right triangle and a congruent triangle.
 \kdokaz



        \bzgled
        If $v_a$, $v_b$ and $v_c$ are altitudes corresponding
        to the sides $a$, $b$ and $c$ of a triangle, then:
        $$\frac{v_a}{b+c}+\frac{v_b}{a+c}+\frac{v_c}{a+b}<\frac{3}{2}.$$
        \ezgled

\textbf{\textit{Proof.}}
By adding the inequalities $v_a \leq b$,
$v_a \leq c$
we get $2v_a \leq b + c$ or $\frac{v_a}{b + c} \leq \frac{1}{2}$.
Similarly, we get $\frac{v_b}{a + c} \leq \frac{1}{2}$ and
$\frac{v_c}{a + b} \leq \frac{1}{2}$. Since all inequalities cannot be true at the same time,
by adding we get the desired inequality.
 \kdokaz

The next property of the triangle will be called \index{triangle
inequality} \pojem{triangle inequality}.


             \bizrek \label{neenaktrik}
             The sum of any two sides of a triangle is greater than the third side.
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.4.pic}
\caption{} \label{sl.skl.3.2.4.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $ABC$ be an arbitrary triangle. We will prove that $AB + AC > BC$. We mark a point $D$ so that $\mathcal{B}(B,A,D)$ and $AD \cong  AC$ (Figure \ref{sl.skl.3.2.4.pic}). By the \ref{enakokraki} theorem ($\triangle CAD$ is an isosceles triangle with the base $CD$), we also have that $\angle BDC=\angle ADC  \cong  \angle ACD$. The line segment $CA$ is inside the angle $DCB$, so $\angle ACD <  \angle DCB$. Then $\angle BDC <  \angle DCB$ as well. From \ref{vecstrveckot} (referring to the triangle $BCD$) it follows that: $$BC < BD = AB + AD = AB + AC,$$ which was to be proven. \kdokaz

From the triangle inequality we obtain a criterion for the existence of such a triangle, that its sides are consistent with three given line segments.


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

\textbf{\textit{Proof.}}  If such a triangle exists, then the three relations are direct consequences of the triangle inequality \ref{neenaktrik}. So we assume that all three relations are true. Without loss of generality, let $a$ be the longest side of this triangle (it is enough that it is not shorter than any other side) and let $B$ and $C$ be any points for which $BC \cong a$ (Figure \ref{sl.skl.3.2.5.pic}). Because $b + c > a$, this means that the circles $k(B,c)$ and $k(C,b)$ intersect in some point $A$ (a consequence of Dedekind's axiom - \ref{DedPoslKrozKroz} theorem, because each of them contains the inner points of the other), which is not on the line segment $BC$. The triangle $ABC$ is then the desired triangle. \kdokaz

If we know which of the three sides is the longest,
 it is enough to check only one inequality, as
 the other two are automatically fulfilled. The proof
 of the previous statement can also be used for the following, equivalent
 criterion.

             \bzgled \label{neenaktrik1}
               Let $a$, $b$ and $c$ be three line segments, such that $a \geq b,c$. A triangle with sides $a$,
            $b$ and $c$ exist if and only if $b + c > a$.
              \ezgled

For example, we can determine that a triangle exists with sides that have lengths 7, 5 and 3 (because $5+3>7$), but a triangle with sides that have lengths 9, 6 and 2
does not exist (because $6+2$ is not greater than 9).

 Let's look at some consequences of the previous statements.


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

\textbf{\textit{Proof.}} If we use the triangle inequality for
the triangles $ABX$ and $AXC$ (Figure \ref{sl.skl.3.2.6.pic}), we get:
 $$AX < AB + BX \hspace*{1mm} \textrm{ and }\hspace*{1mm}  AX < AC + CX.$$
By adding these two inequalities and using the triangle inequality for the triangle $ABC$, we get:
 $$2AX < AB + AC +
BC < 2(AB + AC),$$ which was to be proven. \kdokaz

%%  !!! Dosegel magično stran - 100!!! Wow Bravo!!!

The next inequality is a generalization of the previous one. In this sense, the previous statement is its consequence and it was not necessary to prove it separately.


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

\textbf{\textit{Proof.}} Because for the point $X$ it holds that $\mathcal{B}(B, X, C)$,
one of the sides $AXB$ and $AXC$ is not acute. Without loss of
generality, let it be $AXC$ (Figure \ref{sl.skl.3.2.7.pic}). Then
it is the largest angle in the triangle $AXB$, which means that \\
$AX < AC$ (statement \ref{vecstrveckot}). Similarly, if the angle $AXB$ is not acute,
it holds that $AX < AB$.
 \kdokaz

We will especially consider the case of the distance $AX$, if the point $X$ is from
the previous two statements the center of the side $BC$ (Figure
\ref{sl.skl.3.2.8.pic}). Such a distance, which is determined by the vertex
and the center of the opposite side of the triangle, is called
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

\textbf{\textit{Proof.}} We mark with $A_1$ the center of the side $BC$
of the triangle $ABC$. Then $t_a  =AA_1$  (Figure
\ref{sl.skl.3.2.9.pic}).

If we use the triangle inequality for the triangle $ABX$ and $ACX$ (statement \ref{neenaktrik}), we get: $AA_1 + A_1B > AB$ and
$AA_1 + A_1C > AC$  or:
$$t_a+\frac{a}{2}>c \hspace*{2mm} \textrm{ in } \hspace*{2mm}
 t_a+\frac{a}{2}>b.$$
If we add these two inequalities, we get $\frac{b+c-a}{2}<t_a$.
We will also prove $t_a<\frac{b+c}{2}$.
Let $D$ be the point, for which
 $A_1D \cong AA_1$ and $\mathcal{B}(A,A_1,D)$. The triangles $AA_1B$ and $DA_1C$
  are
congruent (statement \textit{SAS} \ref{SKS}), which means that $AB \cong DC$. If
we use the triangle inequality again (statement \ref{neenaktrik}) for
the triangle $ACD$, we get:
$$b+c = AC + AB = AC + CD > AD = 2AA_1 = 2t_a,$$ which had to be proven. \kdokaz

 We will show some more examples of the use of the triangle inequality.


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


 \textbf{\textit{Proof.}} Let $D$ be such a point on the line segment $BC$, that $AC \cong CD$
 and $\mathcal{B}(A,C,D)$ (Figure
\ref{sl.skl.3.2.10.pic}). The triangles $ACM$ and $DCM$ are congruent,
by  statement \textit{SAS}  \ref{SKS} ($AC \cong DC$, $CM \cong CM$, $\angle ACM \cong
\angle DCM$). Therefore $MA \cong MD$. If we use the triangle inequality now, we get: $$MA + MB = MD + MB \geq BD = DC +
CB = CA + CB.$$
 Of course, the equality holds when the points $B$, $M$ and $D$ are collinear or $M = C$.
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

 \textbf{\textit{Proof.}}  Because $\mathcal{B}(B,E,C)$, the angle
 $AEB$ is the external angle  of triangle $AEC$ (Figure
\ref{sl.skl.3.2.11.pic}). Therefore $\angle BEA > \angle EAC \cong
\angle BAE$ (statement \ref{zunanjiNotrNotrVecji}). Opposite the larger
angle in triangle $BAE$ is the larger side, or $AB > BE$
(statement \ref{vecstrveckot}). Similarly, we prove that the other of the two relations is also true.
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

\textbf{\textit{Proof.}} Let $N$ be the intersection of lines $BM$ and
$CA$ (Figure \ref{sl.skl.3.2.12.pic}). Because $M$ is an interior point of
triangle $ABC$, $\mathcal{B}(B,M,N)$ and
$\mathcal{B}(A,N,C)$ are true. If we now use the triangle inequality (statement \ref{neenaktrik}) twice, we get:
 \begin{eqnarray*}
\hspace*{-4mm}BM + MC &<& BM + (MN + NC) = (BM + MN) + NC = BN + NC\\
 \hspace*{-4mm}&<& (BA +
AN) + NC = BA + (AN + NC) = BA + AC.
  \end{eqnarray*}

Let's define two new concepts. The sum of all sides of a polygon is called its \index{obseg!večkotnika} \pojem{obseg}. Half of this sum is the \pojem{polobseg} of this polygon.



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
  We first get the inequality, if
we use the triangle inequality for the triangles $MAB$,
$MBC$ and $MCA$ and then add them up. The second inequality is obtained,
if we use the previous statement (Example \ref{zgled3.2.9})
and add the corresponding inequalities (Figure \ref{sl.skl.3.2.13.pic}).
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
 Let $AD$ be the longest diagonal
of the pentagon $ABCDE$ (not shorter than any other
diagonal). We prove that $AD$, $AC$ and $BD$ are the desired diagonals,
i.e. those for which there exists a triangle, whose sides
 are congruent to these diagonals (Figure \ref{sl.skl.3.2.14.pic}). Because
 $AD\geq AC$ and $AD\geq BD$, it is enough to prove (Example \ref{neenaktrik1}),
that $AC + BD > AD$. The pentagon $ABCDE$ is convex,
so its diagonals $AC$ and
$BD$ intersect in some point $S$. Then: $$AC + BD > AS + SD > AD,$$ which was to be proven. \kdokaz

The following consequence of the theorems about the congruence of
triangles is very important. We will also need the triangle inequality in this proof.


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

($\Leftarrow$) Let $\angle BAC > \angle B' A'C'$. Then there exists
within the angle $BAC$ such a line segment $l$, that $\angle BA,l \cong \angle B'A'C'$.
With $C''$ we mark the point of the line segment $l$, for which
$AC'' \cong A'C'$. Then both triangle $ABC''$ and
$A'B'C'$ are congruent and $BC'' \cong B'C'$. It is enough to prove that
$BC > BC''$. If $C''$ lies on the side $BC$, it is trivially
fulfilled. We assume that the point $C''$ does not lie on the side $BC$.
Let the point $E$ be the intersection of the perpendicular bisector of the angle $CAC''$ and the side $BC$.
By the \textit{SAS} theorem, the triangles $ACE$ and $AC''E$ are congruent, therefore
$CE \cong C''E$. Now it is:
$$BC = BE + EC = BE + EC'' \hspace{0.1mm} > BC'' = B'C'.$$
 ($\Rightarrow$) Let $BC > B'C'$. The relation $\angle BAC \cong
  \angle B' A'C'$ is not true,
  because then (by the \textit{SAS} theorem) the triangle
$ABC$ and $A'B'C'$ would be congruent and then also $BC \cong B'C'$. If
it would be true that $\angle BAC < \angle B' A'C'$,  then from what has already been proven it would follow that $BC < B'C'$. Therefore $\angle BAC > \angle B' A'C'$.
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

\textbf{\textit{Proof.}} We will carry out the proof by induction over $n$
(Figure \ref{sl.skl.3.2.16.pic}).

 In the case $n=3$ we get the triangle inequality - izrek
 \ref{neenaktrik}.

Let's assume that the inequality is true for $n=k$ ($k\in \mathbb{N}$, $k> 3$) or
  $|A_1A_2|+|A_2A_2|+\cdots +|A_{k-1}A_k|\geq |A_1A_k|.$ We will prove that
  the inequality is also true for $n=k+1$ or
  $|A_1A_2|+|A_2A_2|+\cdots +|A_kA_{k+1}|\geq |A_1A_{k+1}|.$ If
  we first use the induction
  assumption, and then the triangle inequality, we get:
  \begin{eqnarray*}
   && |A_1A_2|+|A_2A_2|+\cdots +|A_{k-1}A_k|+|A_kA_{k+1}|\geq\\
   && \geq|A_1A_k|+|A_kA_{k+1}|\geq |A_1A_{k+1}|,
  \end{eqnarray*}
 which is what needed to be proven. \kdokaz

We will now prove another inequality that is true in any triangle.


             \bzgled
             If $a$, $b$, $c$ are the sides and $\alpha$, $\beta$, $\gamma$
              the opposite interior angles of a triangle, then
              $$60^0\leq \frac{a\alpha+b\beta +c\gamma}{a+b+c} < 90^0.$$
               \ezgled

\textbf{\textit{Proof.}} We will prove each of the inequalities separately. In doing so, we will use the statement about the sum of the interior angles of a triangle (statement \ref{VsotKotTrik}). First, we will prove the second inequality:
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
 The last inequality is fulfilled because, according to the triangle inequality (statement \ref{neenaktrik}), $b+c-a>0$, $a+c-b>0$ and  $a+b-c>0$ hold.
 We will now prove the first inequality:
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
 The last inequality is a consequence of statement \ref{vecstrveckotAlgeb}.
 \kdokaz

 The next statement will be the motivation for defining the distance of a point from a line.

             \bizrek Let $A'=pr_{\perp p}(A)$ be the foot of the perpendicular from a point  $A$ on a line $p$.
            If $X\in p$ and $X\neq A'$, then $AX>AA'$.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.2.17.pic}
\caption{} \label{sl.skl.3.2.17.pic}
\end{figure}

  \textbf{\textit{Proof.}}
 By definition, $AA'\perp p$
(Figure \ref{sl.skl.3.2.17.pic}), which means that $AA'X$
 is a right angled triangle with hypotenuse $AX$. From 
 \ref{vecstrveckotHipot} it follows that $AX>AA'$.
 \kdokaz

 If $A'=pr_{\perp
p}(A)$, we say that the length of the line $AA'$ \index{distance!point
 from a line} \pojem{distance of point $A$ from line $p$}.
We denote it by $d(A,p)$. So $d(A,p)=|AA'|$.




%________________________________________________________________________________
 \poglavje{Circle and Line} \label{odd3KrozPrem}

In the following we will deal with a circle and the mutual
position of a circle and a line. We prove first a property of the
diameter of a circle, which is a simple consequence of the
triangle inequality.


            \bizrek \label{premerNajdTetiva}
               The longest chord of a circle is its diameter.
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.1.pic}
\caption{} \label{sl.skl.3.3.1.pic}
\end{figure}

 \textbf{\textit{Proof.}}  Let
$AB$ be any chord of a circle that is not a diameter, and $C$ a
point on the line $AS$, for which $CS\cong SA$ and $\mathcal{B}(A,S,C)$
(Figure \ref{sl.skl.3.3.1.pic}). Then point $C$ lies on
the circle $k$ and $AC$ is its diameter. We have already shown (a consequence
of \ref{premerInS}) that all diameters of a circle
are mutually congruent. So it is enough to show that $AC>AB$. This follows 
from the triangle inequality (triangle $ASB$). It holds:
 $$AC=AS+SC=AS+SB>AB,$$ which was to be proved. \kdokaz

It follows another property of a chord of a circle, as a consequence of 
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

\textbf{\textit{Proof.}} Let $X$ be an inner point of the segment $AB$
with shorter sides on the circle $k(S,r)$ (Figure \ref{sl.skl.3.3.2.pic}). The angle $AXS$ and
$BXS$ are adjacent angles, which means that they are not both acute angles. Without
loss of generality, assume that the angle $BXS$ is not an acute angle. Then in
the triangle $SXB$ the side $SB$ is the longest  (by
\ref{vecstrveckotHipot}), which means that:
 $$SX<SB=r.$$
Therefore, $X$ is an inner point of the circle  $k(S,r)$.
 \kdokaz

Similarly, we will prove the following important statement.


        \bizrek \label{KrogKonv}
         A circular disc is a convex set.
          \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.3.pic}
\caption{} \label{sl.skl.3.3.3.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $A$ and $B$ be two points of the circle
$\mathcal{K}(S,r)$ (Figure \ref{sl.skl.3.3.3.pic}). It is necessary to prove that
the whole segment $AB$ lies in this circle, or that this is true for any
point $X$, for which $\mathcal{B}(A,X,B)$. Because points $A$ and $B$
lie in the circle $\mathcal{K}$, then $SA, SB\leq r$.
As in the proof of the previous statement, we write: because
$\mathcal{B}(A,X,B)$, then at least one of the adjacent angles $AXS$ and $BXS$ is not
acute. Without loss of generality, let $\angle BXS\geq 90^0$. If
we use the statement \ref{vecstrveckotHipot} for the triangle $SXB$, we get:
$$SX<SB\leq r.$$
 Therefore, the point $X$ lies in the circle $\mathcal{K}$, which means that $\mathcal{K}$
is a convex figure.
 \kdokaz

It is intuitively clear that a line and a circle can have at most
two common points. We will now prove this fact.

        \bizrek \label{KroznPremPresek}
        A line and a circle can have at most two common points.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.4.pic}
\caption{} \label{sl.skl.3.3.4.pic}
\end{figure}

\textbf{\textit{Proof.}} We assume the opposite, that the circle
$k(S,r)$ and the line $p$ have at least three different common
points: $A$, $B$ and $C$, or $A,B,C\in p\cap k$ (Figure
\ref{sl.skl.3.3.4.pic}). If the center $S$ lies on the line $p$,
then on this line there are only two points that are distant from
the point $S$ by the radius $r$ (statement \ref{ABnaPoltrakCX}). Let
$S\notin p$. From the condition $A,B,C\in p\cap k$ it follows that
$SA=SB=SC=r$, which means that the triangles $ASC$, $ASB$ and $BSC$
are isosceles. Without loss of generality, we assume that
$\mathcal{B}(A,C,B)$. From this it follows (statement
\ref{enakokraki}), that the angles:
 $$\angle  SCA\cong \angle SAC \cong \angle SBC \cong \angle SCB.$$
are congruent. Therefore, the angle $SCA$ and the angle $SCB$ are
congruent and are both right angles. Then the angle $SAC$ is also
a right angle. But this is not possible, because in this case the
triangle $SAC$ would have two right internal angles. This means
that the assumption $A,B,C\in p\cap k$ is false. \kdokaz

 From statement \ref{KroznPremPresek} it follows that a line and a circle can have two, one or no common
points. In the first case we say that the line and the circle
\pojem{intersect}, in the second case they \pojem{touch}, in the
third case they are
 \pojem{non-intersecting} (Figure
\ref{sl.skl.3.3.5.pic}). The line is in the first case \index{secant
of a circle}\pojem{secant} or \pojem{secant}, in the second case
\index{tangent of a circle}\pojem{tangent} or \pojem{tangent}, and
in the third case \index{non-secant of a circle}\pojem{non-secant}.
The point in which the tangent touches the circle is called
\index{tangent point}\pojem{tangent point}.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.5.pic}
\caption{} \label{sl.skl.3.3.5.pic}
\end{figure}

We often use the following criterion for the tangent, which is
actually a necessary and sufficient condition for a line to be a
tangent to a circle.

\bizrek \label{TangPogoj}
Let $T$ be a point lying on the circle $k(S, r)$. A line
$PT$ (lying in the plane of the circle) is a tangent of the circle at the point $T$ if and only if $PT \perp TS$.
\eizrek

\textbf{\textit{Proof.}}  ($\Rightarrow$) Let $PT$ be a tangent
of the circle $k$ at the point $T$. If the angle $PTS$ is not a right angle, one
of the angles, determined by the lines $PT$ and $TS$, is acute. Without loss of
generality, let $\angle STX =w < 90°$ (Figure
\ref{sl.skl.3.3.6.pic}). With $l$ we denote
 the half-line with the origin $S$, lying in the plane $STX$, so that
 $\angle ST,l = 180° - 2w $. If $Y$ is the intersection of the half-lines $TX$ and $l$,
the triangle $STY$ is isosceles ($\angle STY = \angle SYT =w$ ) and $ST = SY = r$. But this is not possible, because $PT$ is a tangent of the circle $k$
and they have only one common point. Therefore, the angle $PTS$ is a right angle or $PT \perp TS$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.6.pic}
\caption{} \label{sl.skl.3.3.6.pic}
\end{figure}

($\Leftarrow$) Now let $PT \perp TS$ (Figure
\ref{sl.skl.3.3.6.pic}). For each point $T_1\in PT$  ($T_1 \neq T$)
the triangle $STT_1$ is a right triangle with the hypotenuse $ST_1$ and then
it holds (from \ref{vecstrveckotHipot}):
 $$ST_1 > ST = r.$$
 Therefore, none of the points $T_1$ ($T_1 \neq T$), lying on
the line $PT$, lies on the circle $k$. This means that the line
$PT$ is a tangent of this circle.
 \kdokaz

From the proof of the previous statement ($\Leftarrow$) it follows that all
points lying on the tangent of the circle (except for its
point of contact), are external points of this circle. With this
property we will prove the following statement.


\bzgled \label{tangKrozEnaStr}
All points of a circle are on the one side of its tangent.
\ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.7.pic}
\caption{} \label{sl.skl.3.3.7.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $T$ be the point of tangency of the circle $k(S, r)$ and its tangent $t$ (Figure \ref{sl.skl.3.3.7.pic}). The tangent $t$ divides the plane in which $k$ and $t$ lie into two half-planes. The half-plane in which the point $S$ lies, we denote by $\alpha_1$, the other half-plane by $\alpha_2$. We prove that all points of the circle $k$ lie in the half-plane $\alpha_1$. Let $X$ be an arbitrary point of the half-plane $\alpha_2$. Since the points $S$ and $X$ are on different sides of the line $t$, it follows that the open line segment $SX$ intersects at some point $Y$. Then we have:
 $$SX = SY + YX > SY \geq ST = r,$$
  which means that the point $X$ does not lie on the circle $k$ and is its external point. Therefore, none of the points of the half-plane $\alpha_2$ lies on the circle $k$, that is, all of them are in the half-plane $\alpha_1$ with the edge $t$. \kdokaz

A direct consequence of the statement \ref{TangPogoj} is also that in each point of the circle we can draw only one tangent. If $X$ is an internal point of the circle $k(S, r)$, then no tangent passes through this point, since all lines through $X$ are intersecting, which is a consequence of Dedekind's axiom (statement \ref{DedPoslKrozPrem}). Later (statement \ref{tangentiKroznice}) we will find that through each external point of the circle we can draw exactly two tangents. For the time being, we prove the following statement (the reader will remember that this is a statement that we have already considered at the beginning of the introductory chapter - statement \ref{TalesUvod}).

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


\textbf{\textit{Proof.}} Let $O$ be the center of the line $AB$ and $k$
the circle with center $O$ and radius $OA$ or diameter $AB$
(Figure \ref{sl.skl.3.3.9.pic}). From $\angle AXB=90^0$ it follows from
the theorem \ref{VsotKotTrik}:
 \begin{eqnarray}
 \angle XAB+ \angle XBA = 90^0 \label{relacija336}
 \end{eqnarray}

We prove $X\in k$. We assume the contrary, i.e. that the point $X$ does not
lie on the circle $k$. In this case $OX\neq OA$. Let $X_1$
be the point on the segment $OX$, for which $OX_1\cong OA$ (theorem
\ref{ABnaPoltrakCX}). This means that the point $X_1$ lies on the circle
$k$ and by the theorem \ref{TalesovIzrKroz} we have $\angle
AX_1B=90^0$.

By our assumption $OX\neq OA$ it is clear that $X\neq X_1$.
We will consider two possibilities:

\textit{1)} Let $OX_1<OX$ or $\mathcal{B}(O,X_1,X)$. In this
case $X_1$ is an inner point of the angles $XAB$ and $XBA$, therefore $\angle X_1AB<\angle XAB$ and $\angle X_1BA<\angle XBA$. From this and
relation \ref{relacija336} it follows:
 $$\angle X_1AB+ \angle X_1BA<\angle XAB+ \angle XBA = 90^0.$$
 Since $\angle AX_1B=90^0$, the sum of the angles in the triangle $AX_1B$
 is less than $180^0$, which by the theorem \ref{VsotKotTrik} is not possible.


\textit{2)} Let $OX_1>OX$ or $\mathcal{B}(O,X,X_1)$. Similarly
as in the first case we get:
 $$\angle X_1AB+ \angle X_1BA>\angle XAB+ \angle XBA = 90^0.$$
 In this case the sum of the angles in the triangle $AX_1B$ is greater than
$180^0$, which by the theorem \ref{VsotKotTrik} is not possible.

It follows that $OX=OX_1$  or $X\in k$.
 \kdokaz


 Use the previous theorem for the design of tangents.


             \bzgled \label{tangKrozKonstr}
             Let $A$ be an exterior point of a circle $k(S,r)$.
             Construct all tangents of this circle passing through the point $A$.
             \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.10.pic}
\caption{} \label{sl.skl.3.3.10.pic}
\end{figure}


 \textbf{\textit{Solution.}} Let $l$ be a circle with diameter $SA$
(Figure \ref{sl.skl.3.3.10.pic}). Because $S$ is an interior, $A$ is an exterior point of the given circle $k$, the circle $k$ and $l$ have exactly two common points $T_1$ and $T_2$ (statement \ref{DedPoslKrozKroz}).
By Tales' statement \ref{TalesovIzrKroz},
$\angle ST_1A\cong \angle ST_2A=90^0$. Because $ST_1$ and  $ST_2$
are radii of the circle $k$, $AT_1$ and $AT_2$ are tangents of the circle $k$
through the point $A$ (statement \ref{TangPogoj}).

 We prove that $AT_1$ and $AT_2$ are the only tangents of the circle $k$
  from the point $A$. If $AT$ is a tangent from the point $A$, which the circle $k$
 touches in the point $T$, by  statement \ref{TangPogoj} $\angle ATS=90^0$.
 This means that the point $T$ lies on the circle $l$
 (statement \ref{TalesovIzrKrozObrat}) or $T\in k\cap l$. Therefore $T$ is one
 of the points $T_1$ and $T_2$, so $AT_1$ and $AT_2$ are the only tangents of the circle
  $k$  from the point $A$.
  \kdokaz

  The following statement follows from the previous construction.



        \bizrek \label{tangentiKroznice}
         If $V$ is an exterior point of a circle $k(S,r)$, then there are exactly
       two tangents of the circle $k$ through the point $V$.
        \eizrek


 We prove some more properties of a tangent of a circle.


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

\textbf{\textit{Proof.}} From izrek \ref{TangPogoj} it follows: $VA
\perp AS$ and $VB \perp BS$
(Figure \ref{sl.skl.3.3.11.pic}). Therefore $ASV$ and $BSV$ are right-angled
triangles with a shared hypotenuse $SV$. Because $SA \cong SB = r$,
these two triangles are congruent (izrek \textit{SSA} \ref{SSK}). Therefore the angles
$AVS$ and $BVS$ are also congruent, which means that the line $VS$
is the bisector of angle $AVB$. From the congruence of these two triangles it also follows
that $VA \cong VB$.
 \kdokaz

The converse is also true.


             \bzgled \label{SimKotaKraka}
             If a point $S$ lies on the bisector of a convex angle,
            then it is the centre of a circle touching both sides of this angle.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.3.12.pic}
\caption{} \label{sl.skl.3.3.12.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $A$ and $B$ be the right-angled projections
of point $S$ on the sides of given angle with the vertex $V$ (Figure
\ref{sl.skl.3.3.12.pic}). Triangles $ASV$ and $BSV$ are congruent
(izrek \textit{ASA} \ref{KSK}), because they have a shared side $VS$ and
two pairs of congruent angles - from $\angle AVS\cong \angle BVS$ and $\angle
SAV\cong \angle SBV=90^0$ it follows that $\angle ASV\cong \angle BSV$. Therefore $SA\cong SB$ and $k(S,SA)$ is the desired circle. The sides
of given angle are tangents to the circle by izrek \ref{TangPogoj}.
 \kdokaz

Now we will prove another criterion for the mutual position of a line and
a circle in a plane.



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

The statement (ii) follows directly from the criterion for tangency (the statement \ref{TangPogoj}).

(i) In the proof of the direct direction of equivalence we use the fact that the hypotenuse of a right angled triangle is longer than either of the two shorter sides (the statement \ref{vecstrveckotHipot}). If $A$ and $B$ are the intersections of the secant $p$ and the circle $k$, then $SA$ is the hypotenuse of the right angled triangle $ASP$ and it holds:
 $r \cong SA > SP$.

 In the proof of the inverse direction of equivalence we use the consequence of Dedekind's axiom (the statement \ref{DedPoslKrozPrem}). Because in this case $P$ is an inner point of this circle, each straight line of this plane that goes through
the point $P$ is a secant of the circle $k$.

(iii) It follows from the proven (i) and (ii). Because if $SP > r$,
then neither $SP < r$ nor $SP \cong r$. From the equivalences (i) and (ii) it follows that the straight line $p$ is neither a secant nor a tangent. Therefore $p$
is a parallel of the circle $k$. In the same way we prove the inverse direction of equivalence.
  \kdokaz

%________________________________________________________________________________
 \poglavje{Quadrilaterals} \label{odd3Stirik}


In section \ref{odd2AKSURJ} we introduced the concept of a quadrilateral as
a polygon with four sides and four vertices.
We defined the concepts of adjacent and opposite sides, adjacent and
opposite angles and diagonal. To a quadrilateral $ABCD$ with the lengths of its sides $AB$, $BC$, $CD$ and $DA$ we usually assign the letters $a$,
$b$, $c$ and $d$, and to the lengths of its diagonals $AC$ and $BD$ the letters $e$ and
$f$  (Figure \ref{sl.skl.3.4.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.1.pic}
\caption{} \label{sl.skl.3.4.1.pic}
\end{figure}

In the same section, we introduced the concepts of internal and external angles of a quadrilateral. We also mentioned that the internal angles at vertices $A$, $B$, $C$ and $D$ of a quadrilateral $ABCD$ are usually denoted by $\alpha$, $\beta$, $\gamma$ and $\delta$, and its external angles by $\alpha'$, $\beta'$, $\gamma'$ and $\delta'$. We proved (as a consequence of the general statement \ref{VsotKotVeck}) that the sum of all four internal angles of an arbitrary quadrilateral is equal to $360^0$ (Figure \ref{sl.skl.3.4.1.pic}). The sum of external angles is also equal to $360^0$ (in a convex quadrilateral). So:
 \begin{eqnarray*}
 \alpha+\beta+\gamma+\delta=360^0,\\
 \alpha'+\beta'+\gamma'+\delta'=360^0
 \end{eqnarray*}

Let us also add that we call the internal angle \pojem{adjacent} or \pojem{opposite}, if the corresponding vertices are adjacent or opposite.



Now we will consider some types of quadrilaterals in more detail.

 A quadrilateral
$ABCD$ is a \pojem{trapezoid}, if $AB\parallel CD$ (Figure \ref{sl.skl.3.4.2.pic}).
Sides $AB$ and $CD$ are the \pojem{bases}, $BC$ and $AD$ are the
\pojem{legs} of this trapezoid.
The line $PQ$ ($P\in AB$, $Q\in CD$ and $PQ\perp AB$) is the \pojem{height} of the trapezoid. We often denote it by $v$.


A trapezoid is
 \pojem{isosceles},
 if $BC \cong AD$ and $BC \not\parallel AD$,
 or \pojem{right}, if at least
one of the internal angles is a right angle.




\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.2.pic}
\caption{} \label{sl.skl.3.4.2.pic}
\end{figure}


Two internal angles at the same leg of a trapezoid are supplementary, because
they are angles with parallel legs (statement \ref{KotiTransverzala}). The supplementarity of these angles is also
a sufficient condition for a quadrilateral to be a trapezoid. It follows from this that a right trapezoid has at least two right internal angles.

We get another group of quadrilaterals as a special type of trapezoids. These are \pojem{parallelograms}. They can be defined in different ways. We will choose one, and prove that the others are equivalent.

Quadrilateral $ABCD$ is a \index{paralelogram} \pojem{parallelogram}, if $AB \parallel CD$ and $AD \parallel BC$ (Figure \ref{sl.skl.3.4.3.pic}). Line $PQ$ ($P\in AB$, $Q\in CD$ and $PQ\perp AB$) and $MN$ ($M\in BC$, $N\in AD$ and $MN\perp BC$) are the \index{višina!paralelograma}\pojem{heights of the parallelogram}. We often denote them with $v_a$ and $v_b$.



\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.3.pic}
\caption{} \label{sl.skl.3.4.3.pic}
\end{figure}

 A parallelogram is therefore a quadrilateral that has two pairs of parallel sides. The term congruence is not used in the definition of a parallelogram. We can also consider parallelograms (and trapezoids) in so-called \index{geometrija!afina} \pojem{affine geometry}. This is a geometry that is based on all the axioms of Euclidean geometry, with the exception of the third group of axioms - the axioms of congruence.

We will now prove the aforementioned equivalents for the definition of a parallelogram.

\bizrek  \label{paralelogram}
Let $ABCD$ be a convex quadrilateral.
Then the following statements are equivalent:
\begin{enumerate}
  \item The quadrilateral $ABCD$ is a parallelogram.
  \item Any two adjacent interior angles of  the quadrilateral $ABCD$ are supplementary.
  \item Any two opposite interior angles of  the quadrilateral $ABCD$ are congruent.
 \item $AB \parallel CD$ and $AB \cong CD$\footnote{This equivalent
    in a slightly different form is given by \index{Euclid}
    \textit{Euclid of Alexandria} (3rd century BC) in
    the first book of his 'Elements'.}.
 \item $AB \cong CD$ and $AD \cong BC$.
 \item The diagonals of the quadrilateral $ABCD$ bisect each other, i.e.
   line segments $AC$ and $BD$ have a common midpoint.
\end{enumerate}
 \eizrek

 \textbf{\textit{Proof.}}
It is enough to prove the equivalence of all the statements $(1)-(6)$. To avoid proving all equivalences (two implications - for example, with the statement (1), which would give 10 implications in total), we will simplify the proof a little, so that we prove implications according to the following scheme.

\vspace*{5mm}
\hspace*{25mm}
$\begin{array}{ccccccc}
  \textit{(1)} & \Leftarrow & \textit{(2)} & \Leftarrow & \textit{(3)} &   &   \\
  \Downarrow &   &   &   & \Uparrow &   &   \\
  \textit{(4)} &   & \Rightarrow &   & \textit{(5)} & \Leftrightarrow & \textit{(6)}
\end{array}$

\vspace*{5mm}

 As we can see, this is enough because the implication $\textit{(1)}
\Rightarrow \textit{(2)}$ follows directly from: $\textit{(1)}\Rightarrow \textit{(4)}\Rightarrow
\textit{(5)}\Rightarrow \textit{(3)} \Rightarrow \textit{(2)}$.

Let's mark with $\alpha$, $\beta$, $\gamma$ and $\delta$ the internal angles at
the vertices $A$, $B$, $C$ and $D$ of the quadrilateral $ABCD$. The quadrilateral
$ABCD$ is convex, which means that its diagonals intersect in
some point $S$.

$\textit{(2)}\Rightarrow \textit{(1)}$. Let the angles $\alpha$ and
$\beta$ be complementary (Figure \ref{sl.skl.3.4.4.pic}). Then the angles at the transversal $AB$ are congruent to the angles $AD$ and $BC$, so $AD\parallel
BC$ (by Theorem \ref{KotiTransverzala}). Similarly, from the complementarity of the angles $\beta$ and $\gamma$ it follows that $AB\parallel CD$. Therefore, the quadrilateral $ABCD$ is a parallelogram.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4.pic}
\caption{} \label{sl.skl.3.4.4.pic}
\end{figure}

$\textit{(3)}\Rightarrow\textit{(2)}$. Let $\alpha =\gamma$ and $\beta =\delta$ (Figure \ref{sl.skl.3.4.4.pic}).
Since $\alpha + \beta +\gamma +\delta = 360°$ (the sum of all
internal angles in a quadrilateral is $360°$ - by Theorem \ref{VsotKotVeck}), it follows that
$\alpha + \beta =180°$ and $\beta +\gamma = 180°$.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4a.pic}
\caption{} \label{sl.skl.3.4.4a.pic}
\end{figure}

$\textit{(1)}\Rightarrow\textit{(4)}$. Let the quadrilateral $ABCD$
be a parallelogram, i.e. let $AB \parallel CD$ and $AD \parallel BC$
(Figure \ref{sl.skl.3.4.4a.pic}). We will prove that then also $AB \cong CD$.
The line $AC$ is a transversal of the parallels $AB$ and $CD$, which
means that the angles $CAB$ and $ACD$ are alternate angles at this
transversal and are therefore congruent. Similarly, from the parallelism of the lines
$AD$ and $BC$ it follows that the angles $ACB$ and $CAD$ are congruent. Since $AC \cong AC$, the triangles $ACB$ and $CAD$ are congruent (by Theorem \ref{KSK} - \textit{ASA}). Therefore,  $AB \cong CD$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4b.pic}
\caption{} \label{sl.skl.3.4.4b.pic}
\end{figure}

 $\textit{(4)}\Rightarrow \textit{(5)}$. Let $ABCD$ be such a quadrilateral that
 $AB \parallel CD$ and $AB \cong CD$ (Figure \ref{sl.skl.3.4.4b.pic}).
 We will prove that then also $AD \cong BC$.
 The line $AC$ is a transversal of the parallels $AB$ and
$CD$, which means that the angles $CAB$ and $ACD$ are alternate angles at this
transversal and are therefore congruent. Since $AC \cong AC$, the triangles $ACB$ and $CAD$ are congruent (by Theorem \ref{SKS} - \textit{SAS}). Therefore, $BC \cong AD$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4c.pic}
\caption{} \label{sl.skl.3.4.4c.pic}
\end{figure}

 $\textit{(5)}\Rightarrow \textit{(3)}$. Let $ABCD$ be a quadrilateral such that $AB \cong CD$ and
 $AD \cong BC$ (Figure \ref{sl.skl.3.4.4c.pic}). We prove that
then $\beta =\delta$ and $\alpha =\gamma$. Because $AC \cong
AC$, the triangles $ACB$ and $CAD$ are congruent (\ref{SSS} - \textit{SSS}).
It follows that $\angle ABC \cong \angle CDA$ or $\beta =\delta$. In a
similar way we prove that $\alpha =\gamma$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4d.pic}
\caption{} \label{sl.skl.3.4.4d.pic}
\end{figure}

$\textit{(5)}\Leftrightarrow \textit{(6)}$. Let $ABCD$ be a quadrilateral such that
$AB \cong CD$ and $AD \cong BC$ (Figure \ref{sl.skl.3.4.4d.pic}). We prove that the point $S$
is the common center of its diagonals $AC$ and $BD$. Because $AC \cong
AC$, the triangle $ACB$ is congruent to the triangle $CAD$ (\ref{SSS} - \textit{SSS}). Therefore
$\angle ACB \cong \angle CAD$ or $\angle SCB \cong \angle
SAD$. From the congruence of the right angles $CSB$ and $ASD$, it follows that the
angles $SBC$ and $SDA$ are also congruent. Because $AD \cong BC$, it follows that
$\triangle CSB \cong \triangle ASD$ (\ref{KSK} - \textit{ASA}). Therefore $SB
\cong SD$ and $SC \cong SA$ or the point $S$ is the common center
of the diagonals $AC$ and $BD$.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.4e.pic}
\caption{} \label{sl.skl.3.4.4e.pic}
\end{figure}


Conversely, let $S$ be the common center of the diagonals $AC$ and $BD$ (Figure \ref{sl.skl.3.4.4e.pic}). Then
$SB \cong SD$ and $SC \cong SA$. The right angles $CSB$ and $ASD$ are also congruent, so
$\triangle CSB \cong \triangle ASD$ (\ref{SKS} - \textit{SAS}). It follows that $AD \cong BC$. In a similar way
we prove that $AB \cong CD$.
 \kdokaz

We recommend to the reader to prove the previous statement by using a
similar scheme. This will be a good exercise in using theorems about the congruence of triangles.

Let us now define a type of quadrilateral for which it will
be shown that they are special cases of parallelograms (Figure
\ref{sl.skl.3.4.5.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.5.pic}
\caption{} \label{sl.skl.3.4.5.pic}
\end{figure}

A quadrilateral with all sides congruent is called a \index{rhombus}
\pojem{rhombus}.

A quadrilateral with all interior angles congruent (and therefore
equal to $90^0$, because their sum is $360^0$) is a \index{rectangle}
\pojem{rectangle}.

A quadrilateral with all sides congruent and all interior angles
congruent (and equal to $90^0$) is called a \index{square}
\pojem{square}.


It is not difficult to prove that each of these quadrilaterals is also a parallelogram. This is a direct consequence of the previous statement. The rhombus is a parallelogram due to $\textit{(5)}\Rightarrow\textit{(1)}$; the rectangle is a parallelogram due to
$\textit{(2)}\Rightarrow\textit{(1)}$ (or $\textit{(3)}\Rightarrow\textit{(1)}$). For the square it is
clear that it is also a rectangle and a rhombus, so it is also
a parallelogram.

From the previous statement \ref{paralelogram} - equivalent (\textit{5}) it follows that a parallelogram with two adjacent sides congruent is a rhombus. Similarly,
 according to the same statement from the equivalents \textit{(2)} and \textit{(3)} it follows that a parallelogram with at least one right angle is a rectangle.

The next statement provides additional criteria when a parallelogram is also a rhombus,
a rectangle or a square. This statement refers to diagonals. In
a parallelogram, the diagonals always intersect, but in a rhombus,
a rectangle or a square we will have additional properties.



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
 Let $ABCD$ be a parallelogram and $S$ the intersection of its diagonals $AC$ and $BD$. According to
the previous statement \ref{paralelogram}, $S$ is their common
center. From the same statement it also follows that $AB \cong CD$ and $AD \cong
BC$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.6.pic}
\caption{} \label{sl.skl.3.4.6.pic}
\end{figure}

\textit{a)}  (Figure \ref{sl.skl.3.4.6.pic})

 If $ABCD$ is a rhombus, all sides are congruent. Therefore the
triangles $ABS$ and
  $ADS$
are congruent (statement \ref{SSS} - \textit{SSS}). Then the angles $ASB$
and $ASD$ are also congruent and are (as the supplement of the angle) both right angles. This means that the diagonals are perpendicular.

If the diagonals of the parallelogram $ABCD$ are perpendicular, the triangles
$ABS$ and $ADS$ are congruent (statement \ref{SKS} - \textit{SAS}). Therefore the sides
$AB$ and $AD$ are congruent. In a similar way, we prove that all sides of this parallelogram are congruent, which means that the parallelogram is a rhombus.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.6a.pic}
\caption{} \label{sl.skl.3.4.6a.pic}
\end{figure}


\textit{b)}  (Figure \ref{sl.skl.3.4.6a.pic})

 If $ABCD$ is a rectangle, all interior angles are congruent and are right angles. Then
the triangles $ABC$ and $DCB$ are congruent (statement \ref{SKS} - \textit{SAS}).
Therefore $AC \cong DB$.

If in the parallelogram $ABCD$ it holds that $AC \cong DB$, the triangles
$ABC$ and $DCB$ are congruent (statement \ref{SSS} - \textit{SSS}). From this it follows that
the interior angles at the vertices $B$ and $D$ of the parallelogram
$ABCD$ are congruent. According to the previous statement \ref{paralelogram} they are supplementary, which means that they are both right angles. Similarly, all angles of this parallelogram are right angles, which means that the parallelogram is a rectangle.

 \textit{c)} A parallelogram is a square if and only if it is a rhombus and a rectangle at the same time.
 The latter is equivalent to
the fact that the diagonals are perpendicular and
congruent, which follows from the proven  (\textit{a.} and \textit{b.}).
 \kdokaz


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.7.pic}
\caption{} \label{sl.skl.3.4.7.pic}
\end{figure}

Since the diagonals of a rectangle are perpendicular and intersect, there is a circle that contains all the vertices of this rectangle (Figure \ref{sl.skl.3.4.7.pic}). This is called the \index{circumscribed circle!rectangle} \pojem{circumscribed circle of the rectangle}. Its center is the intersection of its diagonals. If the point $S$ is the intersection of the diagonals of the rectangle $ABCD$, then from the previous equation \ref{RombPravKvadr} it follows:
 $$SA \cong SC \cong SB \cong SD.$$
The radius of this circle is equal to half the diagonal of the rectangle. Since the square is a special type of rectangle, it also has a circumscribed circle.

We will now prove an important property of isosceles trapezoids.


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
  Let $ABCD$ be an isosceles trapezoid with the base $AB$ (Figure \ref{sl.skl.3.4.8.pic}). Without loss of generality, assume that $AB>CD$. Let $C'$ and $D'$ be the orthogonal projections of the vertices $C$ and $D$ onto the line $AB$. The quadrilateral $D'C'CD$ is a parallelogram with a right angle, so it is a rectangle. From the fact that $D'C'CD$ is a parallelogram, it follows that $CC'\cong DD'$ (equation \ref{paralelogram}). Since $\angle CC'B\cong \angle DD'A=90^0$, the triangles $CC'B$ and $DD'A$ are congruent (the \textit{SSA} equation \ref{SSK}), so $\beta=\angle CBC'\cong \angle DAD'=\alpha$.

  We will now prove that the diagonals $AC$ and $BD$ are congruent. This follows from the congruence of the triangles $ABC$ and $BAD$ (the \textit{SAS} equation \ref{SKS}).
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

 The triangles $CAE$ and $FBE$ are congruent, because $CE\cong FE$, $AE\cong BE$  and
 $\angle AEC=90^0-\angle CEB=\angle BEF$ (statement \ref{SKS} - \textit{SAS}). Therefore $\angle EBF$ is a right angle and the points $D$, $B$ and $F$ are collinear. From
 the congruence of these two triangles it also follows that $BF\cong AC\cong BD$.
  \kdokaz


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10.pic}
\caption{} \label{sl.skl.3.4.10.pic}
\end{figure}

Except for trapezoids and parallelograms, we will define one more group
of quadrilaterals. A quadrilateral $ABCD$ is
\index{deltoid}\pojem{deltoid}, if its diagonals are perpendicular and
one of the diagonals bisects the other (Figure \ref{sl.skl.3.4.10.pic}).
The following statement is related to the deltoid and is equivalent to its
definition.


        \bzgled
        A quadrilateral is a deltoid if and only if it has two pairs of congruent adjacent sides.
        \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.11.pic}
\caption{} \label{sl.skl.3.4.11.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.4.11.pic})

 Let the quadrilateral $ABCD$ be a deltoid. Then the diagonals
$AC$ and $BD$ are perpendicular and one of the diagonals bisects the other. Without
loss of generality, let the diagonal $BD$ bisect the diagonal $AC$.
It follows that the right triangles $ABS$ and $CBS$ are congruent (statement
\ref{SKS} - \textit{SAS}). Then $AB \cong CB$. From the congruence of the triangles $ADS$ and $CDS$ it follows that $AD \cong CD$.

 Let $ABCD$ be a quadrilateral, in which $AB \cong CB$ and $AD \cong CD$ hold.
 The triangles $ABD$ and $CBD$ are
congruent (statement \ref{SSS} - \textit{SSS}), so the angles $ADS$
and $CDS$ are also congruent. From this it follows that the triangles $ADS$ and
$CDS$ are also congruent (statement \ref{SKS} - \textit{SAS}). Therefore $S$ is the center of the diagonal $AC$, and the angles $DSA$
and $DSC$ are right angles, because they are congruent with the angles.
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
 We will prove that the lines $O_1A_1$, $O_2A_2$ and $O_3A_3$
 have the same center, or that the corresponding quadrilaterals
are parallelograms (Figure \ref{sl.skk.4.2.12.pic}). Because $k_1$, $k_2$
and $k_3$ are congruent circles, the quadrilaterals $O_1A_2O_3B$ and $O_2A_1O_3B$
 are rhombuses. Because of this, the lines $O_1A_2$ and $O_2A_1$ are congruent and
parallel, which means that the quadrilateral $O_1A_2A_1O_2$ is a parallelogram
(statement \ref{paralelogram}). From the same statement it follows that its
diagonals $O_1A_1$ and $O_2A_2$ have a common center. In a similar way we prove that the lines $O_2A_2$ and $O_3A_3$ have a common center, which means that this is also true for all three lines $O_1A_1$,
$O_2A_2$ and $O_3A_3$ at the same time. \kdokaz


            \bzgled
            Construct a rectangle $ABCD$ if its diagonals and the difference of its sides
             are congruent with the two given line segments $d$ and $l$.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10a.pic}
\caption{} \label{sl.skl.3.4.10a.pic}
\end{figure}

\textbf{\textit{Solution.}} Let $ABCD$ be a rectangle, where $AC\cong d$ and $AB-BC=l$ (Figure \ref{sl.skl.3.4.10a.pic}). Let $E$ be a point on side $AB$ such that $EB\cong BC$. In this case, $AE=AC-EB=AC-BC=l$. Because $EBC$ is an isosceles right triangle, $\angle CEB\cong\angle ECB=45^0$ (\ref{enakokraki} and \ref{VsotKotTrik}) or $\angle AEC=135^0$.
This allows us to first construct the triangle $AEC$ ($AC\cong d$, $\angle AEC=135^0$ and $AE\cong l$), and then the rectangle $ABCD$.
 \kdokaz


        \bzgled
        Construct a triangle with given $b$, $c$ and $t_a$ (sides $AC$, $AB$ and triangle median $AA_1$).
        \ezgled



\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10b.pic}
\caption{} \label{sl.skl.3.4.10b.pic}
\end{figure}

\textbf{\textit{Solution.}} Let $ABC$ be a triangle, where $AC\cong b$, $AB\cong c$ and $AA_1\cong t_a$, where $A_1$ is the center of line segment $BC$ (Figure \ref{sl.skl.3.4.10b.pic}). Let $D$ be a point on line segment $AA_1$ such that $DA_1\cong AA_1$ and $\mathcal{B}(A, A_1,D)$. This means that $A_1$ is the common center of line segments $BC$ and $AD$, so by \ref{paralelogram} quadrilateral $ABDC$ is a parallelogram. By the same \ref{paralelogram}, $CD\cong AB\cong c$. This allows us to first construct the triangle $ADC$ ($AC\cong b$, $CD\cong c$ and $AD=2t_a$), and then point $A$.
 \kdokaz

We will now introduce a shorter form of data entry for designing triangles. Similarly, as we had in the previous task with the notation:  $b$, $c$, $t_a$, for the elements of the triangle $ABC$ we will usually use the following labels:
 \begin{itemize}
   \item $a$, $b$, $c$ - sides,
   \item $\alpha$, $\beta$, $\gamma$ - internal angles,
   \item $v_a$, $v_b$, $v_c$ - altitudes,
   \item $t_a$, $t_b$, $t_c$ - centroids,
   \item $l_a$, $l_b$, $l_c$ - distances that are determined by the vertex and the intersection of the internal angle's symmetry line at that vertex with the opposite side;
   \item $s$ - semi-perimeter  ($s=\frac{a+b+c}{2}$),
   \item $R$ - radius of the circumscribed circle (see section \ref{odd3ZnamTock}),
   \item $r$ - radius of the inscribed circle (see section \ref{odd3ZnamTock}),
   \item  $r_a$, $r_b$, $r_c$ - radii of the excircles (see section \ref{odd4Pricrt}).
 \end{itemize}


        \bzgled
        Construct a trapezium if its sides are congruent with the four given line segments $a$, $b$, $c$ and $d$.
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.4.10c.pic}
\caption{} \label{sl.skl.3.4.10c.pic}
\end{figure}

\textbf{\textit{Solution.}} Without loss of generality, we will first assume that $a\geq c$. Let $ABCD$ be a trapezium, in which sides $AB\cong a$, $BC\cong b$, $CD\cong c$ and $DA\cong d$ (Figure \ref{sl.skl.3.4.10c.pic}). In this case, $AB\geq CD$, so on the side $AB$ there exists a point $E$, such that $AE\cong CD$. Because $AB\parallel CD$, by \ref{paralelogram} the quadrilateral $AECD$ is a parallelogram, so by the same theorem $CE\cong DA\cong d$. It also holds that $EB=AB-AE=AB-CD=a-c$. This allows us to construct the triangle $EBC$ ($EB=a-c$, $BC\cong c$ and $CE\cong d$), and then the vertices $A$ and $D$ (from the condition $AE\cong CD\cong c$).
 \kdokaz



%________________________________________________________________________________
 \poglavje{Regular Polygons}\label{odd3PravilniVeck}

The concept of a square fits into the general definition of a new type of polygons.
 A polygon is
\index{pravilni!večkotniki} \pojem{regular}, if all
of its sides are congruent and all of its interior angles are congruent (Figure
\ref{sl.skl.3.5.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.1.pic}
\caption{} \label{sl.skl.3.5.1.pic}
\end{figure}

 A square is therefore a regular quadrilateral. An equilateral triangle
 \index{trikotnik!pravilni}\pojem{regular triangle}
is also a regular polygon.
This is due to the fact that, in an equilateral triangle,
all angles are also equal.

We have already established that the sum of the interior angles of any
$n$-gon is equal to $(n - 2) \cdot 180^0$ (Theorem \ref{VsotKotVeck}). Because
in a regular $n$-gon, all interior angles are congruent, we can calculate the interior angle
by dividing the sum of all angles by the number $n$. Thus, we have
proved the following theorem (Figure \ref{sl.skl.3.5.2.pic}).


             \bizrek \label{pravVeckNotrKot}
             The measure of each interior angle of a regular $n$-gon is:
            $$\frac{(n - 2)\cdot 180^0}{n}.$$
            \eizrek

 Thus, the interior angle of a regular triangle measures $60^0$, the interior angle of a regular quadrilateral measures $90^0$, the interior angle of a regular pentagon measures $108^0$, the interior angle of a regular hexagon measures $120^0$, ...


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.2.pic}
\caption{} \label{sl.skl.3.5.2.pic}
\end{figure}

We shall now prove two important properties of regular polygons.


        \bizrek \label{sredOcrtaneKrozVeck}
        For each regular polygon, there exists a circle passing through each of its vertices.
        \eizrek

\textbf{\textit{Proof.}} Let $A_1A_2\ldots A_n$ be a regular
$n$-gon (Figure \ref{sl.skl.3.5.2.pic}). Then all sides are
congruent and all internal angles are congruent and equal to $\frac{(n
- 2)\cdot 180^0}{n}$. Let $s_1$ and $s_2$ be the lines of symmetry of sides
$A_1A_2$ and $A_2A_3$ of this polygon and let $S$ be their
intersection point. From  \ref{simetrala} it follows that $SA_1 \cong SA_2$
and $SA_2 \cong SA_3$  or:
 $$SA_1 \cong SA_2 \cong SA_2 \cong SA_3.$$
 It follows that the triangle $A_1SA_2$ and $A_2SA_3$
are congruent (from \ref{SSS} - \textit{SSS}). Then the angles
$SA_1A_2$, $SA_2A_1$, $SA_2A_3$ and $SA_3A_2$ are congruent. From $\angle SA_2A_1 \cong
\angle SA_2A_3$  it follows that both angles are equal to half of the internal
angle of the polygon or $\frac{\alpha}{2}=\frac{(n-2)\cdot
180^0}{2n}$. Therefore:
 $$\angle SA_3A_4 =\alpha - \frac{\alpha}{2}=\frac{\alpha}{2} = \angle
 SA_3A_2.$$
Thus the triangle $A_2SA_3$ and $A_3SA_4$ are congruent (from \ref{SKS} - \textit{SAS}). Because of this,  $SA_3 \cong SA_4$  or:
 $$SA_1 \cong SA_2 \cong SA_2 \cong SA_3\cong SA_4.$$
 If we continue this process, we get:
 $$SA_1 \cong SA_2 \cong SA_2 \cdots \cong SA_n,$$
which means that the point $S$ is the center of the circle $k(S, SA_1)$, which
contains all its vertices.
 \kdokaz

The circle from the previous theorem is called the \index{circumscribed circle!regular polygon} \pojem{circumscribed circle
of a regular polygon}. From the proof of the previous theorem it is clear that
its center lies at the intersection of the lines of symmetry of all its sides.

We prove the following theorem in an analogous way.


        \bizrek \label{sredVcrtaneKrozVeck}
        For each regular polygon, there exists a circle  touching each of its sides.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.3.pic}
\caption{} \label{sl.skl.3.5.3.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $A_1A_2\ldots A_n$ be a regular $n$-gon
 (Figure \ref{sl.skl.3.5.3.pic}).
Define the point $S$ as in the proof of the previous statement.
We have shown that:  $SA_1 \cong SA_2 \cong SA_2 \cdots \cong
SA_n$. From this, by statement \ref{SSS} - \textit{SSS}, it follows that the congruence of the isosceles triangles:
 $$\triangle A_1SA_2 \cong \triangle A_2 SA_3 \cong \cdots \cong
  \triangle A_{n-1}SA_n \cong \triangle A_nSA_1.$$
Because of this, all angles at the bases of these triangles are also congruent.
Therefore, the lines $SA_1$, $SA_2$,..., $SA_n$ are the altitudes of the polygon $A_1A_2\ldots A_n$. Let $P_1$, $P_2$,...,
$P_n$ be the points of intersection of these altitudes with the polygon $A_1A_2\ldots A_n$.
From the congruence of the triangles $\triangle A_1SP_1$, $\triangle A_2SP_1$,
$\triangle A_2SP_2$, ..., $\triangle A_1SP_n$ (statements \ref{SSK} and
\ref{KSK}), it follows that the segments $SP_1$, $SP_2$,..., $SP_n$ are congruent. By statement \ref{TangPogoj}, the circle $k(S, SP_1)$ touches all sides
of the polygon $A_1A_2\ldots A_n$.
 \kdokaz

The circle from the previous statement is called the \index{circumscribed circle!of a regular polygon} \pojem{circumscribed circle of a regular
polygon}. From the proof of this statement, it is clear that the center of the circumscribed circle of a regular polygon lies at the intersection of the altitudes of all its internal angles. From the proof it is also clear that the points at which this circle touches the sides of the regular polygon are also the centers of these sides. The center of the circumscribed and inscribed circle is the same point and is therefore also called the \index{center!of a regular polygon}\pojem{center of a regular polygon}.

We have also seen that all triangles,
determined by the center
of the regular $n$-gon and by its sides, are isosceles and all
congruent. The radius of the circumscribed and inscribed circle of the $n$-gon is equal
to the leg or. the height of each of these triangles. The angles at the top of these
triangles are also congruent and because there are a total of $n$ (the same as
the sides of the $n$-gon), each of them measures (Figure \ref{sl.skl.3.5.4.pic}):
 $$\varphi = \frac{360^0}{n}.$$

\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.4.pic}
\caption{} \label{sl.skl.3.5.4.pic}
\end{figure}

 For a regular hexagon, or for $n = 6$, it holds:
 $$\varphi = \frac{360^0}{6}=60^0.$$

 This means that the aforementioned triangles are regular.
Therefore, a regular hexagon is composed of six
regular triangles  (Figure \ref{sl.skl.3.5.4.pic}).

In the following we will consider the properties of regular $n$-gons.

 Let $n$ be an even number and $k = \frac{n}{2}+1$.
We say that $A_k$ is the \pojem{opposite vertex} of vertex $A_1$
of the regular $n$-gon $A_1A_2\ldots A_n$ (Figure
\ref{sl.skl.3.5.5.pic}). Analogously, $A_2$ and $A_{k+1}$, $A_3$ and
$A_{k+2}$, ... , $A_{k-1}$ and $A_n$ are opposite vertices of this
$n$-gon. Similarly, the sides $A_1A_2$ and $A_kA_{k+1}$, ... ,
$A_{k-1} A_k$ and $A_nA_1$ of the polygon
$A_1A_2\ldots A_n$ are \pojem{opposite sides}. We notice that it holds:
 $$\angle A_1SA_k=\frac{n}{2}\varphi = \frac{n}{2}\cdot
  \frac{360^0}{n}=180^0,$$
which means that the diagonal $A_1A_k$ of this $n$-gon contains its
center. Therefore, this diagonal represents the diameter of the circumscribed circle.
Analogously, this holds for all diagonals determined by opposite
vertices. Because of this, we call such diagonals \index{velika diagonala
pravilnega $n$-kotnika} \pojem{major diagonals} of a regular
$n$-gon. The radius of the circumscribed circle is
 equal to half the major diagonal.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.5.pic}
\caption{} \label{sl.skl.3.5.5.pic}
\end{figure}

It can be proven in a similar way that for an even number $n$ of centers of the opposite sides of a regular $n$-gon
$A_1A_2\ldots A_n$ determine the diameters of the inscribed circle of this
$n$-gon. If we consider the previous labels, we get:
 \begin{eqnarray*}
 \angle P_1SP_k&=&\angle P_1SA_2 + \angle A_2SA_{k-1} + \angle
 A_{k-1}SP_k\\
 &=&  \frac{\varphi}{2}+\frac{n-2}{2}\cdot \varphi+\frac{\varphi}{2}
 =\frac{n}{2}\cdot\varphi
 =180^0.
  \end{eqnarray*}


 The distances that are determined by a pair of centers of opposite sides of an $n$-gon
 $A_1A_2\ldots A_n$ or the distances $P_1P_k$,
$P_2P_{k+1}$, ... , $P_{k-1}P_n$, are called the \pojem{heights}
\index{height!of a regular $n$-gon} of this $n$-gon. The radius of the inscribed circle is equal to half the height.

 So every regular $n$-gon, where $n$ is an even number, contains
$\frac{n}{2}$ big diagonals (equal to the diameter of the circumscribed circle) and
$\frac{n}{2}$ heights (equal to the diameter of the inscribed circle). Each of them
goes through the center of this $n$-gon.


 Let $n$ be an odd number now (Figure \ref{sl.skl.3.5.6.pic}) and
  $k=\frac{n+1}{2}+1$.
 Then:
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

This means that the distance $P_1A_k$ contains the center $S$ of a regular
$n$-gon  $A_1A_2\ldots A_n$. This distance is called the \index{height!of a regular $n$-gon}
\pojem{height} of this $n$-gon, the side
$A_1A_2$ and the point $A_k$ are \pojem{opposite}. We define the remaining $n$ heights and $n$ pairs of opposite sides and points in a similar way. In a similar way we can prove that the other heights of this $n$-gon also contain its center.

In a right (isosceles) triangle, we therefore have three
heights, which intersect in its center (Figure
\ref{sl.skl.3.5.7.pic}). If this is true for
any triangle, we will find out later


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.7.pic}
\caption{} \label{sl.skl.3.5.7.pic}
\end{figure}

 In a square, its  diagonals are also the main
 diagonals and intersect in
its center  (Figure \ref{sl.skl.3.5.7.pic}). The heights
of the square are consistent with its side, which is not difficult to prove.

We have already mentioned that a regular hexagon is composed of six
triangles, which intersect in its center. We will consider a regular
hexagon in more detail later. We will also prove
some properties of a regular pentagon, heptagon, nonagon and dodecagon. The problem
of designing regular $n$-gons for any number $n$ will be particularly interesting.

We will now prove an interesting property of a regular nonagon.

             \bzgled
            If $a$ is a side and $d$ and $e$ are the shortest and longest
            diagonal of a regular nonagon ($9$-gon), then $e - d = a$.
             \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.5.8.pic}
\caption{} \label{sl.skl.3.5.8.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $d = CE$ and $e = BF$ be the shortest and longest
diagonals of a regular nonagon $ABCDEFGHI$ with side
$a$ and $P$ the intersection of lines $BC$ and $FE$  (Figure
\ref{sl.skl.3.5.8.pic}). The internal angle of this nonagon measures
 $\angle CDE=\frac{9-2}{9}\cdot 180^0=140^0$,
so $\angle ECD = \angle CED = 20^0$. From this it follows
 $\angle BCE = \angle FEC = 120^0$, i.e.:
 $$\angle ECP = \angle CEP = 60^0.$$
 Therefore, triangle $CPE$ is regular. Since $CB = EF=a$
and $\angle BPF \cong \angle CPE = 60^0$, triangle $BPF$ is also regular. Therefore:
 $$e = BF = BP = BC + CP = BC + CE = a + d,$$ which was to be proved. \kdokaz


%%________________________________________________________________________________
 \poglavje{Midsegment of Triangle} \label{odd3SrednTrik}

We will now look at a very important property of a triangle, which we will use often. Let $P$ and $Q$ be the centers of the sides $AB$ and $AC$ of the triangle $ABC$. The distance $PQ$ is called the \index{midsegment!of a triangle} \pojem{midsegment of the triangle} $ABC$, which corresponds to the side $BC$ (Figure \ref{sl.skl.3.6.1.pic}). We also say that $PQ$ is the midsegment of the triangle $ABC$ with the base $BC$. We prove the basic property that relates to the midsegment.


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



 \textbf{\textit{Proof.}} Let $R$ be a point such that $PQ \cong QR$ and $\mathcal{B}(P,Q,R)$ (Figure \ref{sl.skl.3.6.1.pic}). The line segments $AC$ and $PR$ have a common center, so the quadrilateral $APCR$ is a parallelogram (\ref{paralelogram}). Therefore, the line segments $AP$ and $RC$ are congruent and parallel. The point $P$ is the center of the line segment $AB$, so the line segments $PB$ and $RC$ are congruent and parallel. This means that the quadrilateral $PBCR$ is a parallelogram. It follows that the line segments $BC$ and $PR$ are congruent and parallel. The final conclusion follows from the fact that the point $Q$ is the center of the line segment $PR$.
 \kdokaz


            \bzgled
            Let $AB$ and $A'B'$ be congruent line segments, $C$ and $D$ the midpoints of the line segments
            $AA'$ and $BB'$. Suppose that $CD =\frac{1}{2}  AB$.
            What is a measure of the angle between the lines $AB$ and $A'B'$?
             \ezgled

\textbf{\textit{Solution.}} Let point $S$ be the center of line
$A'B$ (Figure \ref{sl.skl.3.6.2.pic}). Lines $CS$ and $DS$ are the
medians of triangles $A'AB$ and $BA'B'$, so: $$CS = \frac{1}{2}AB =
CD = \frac{1}{2}A'B'= DS,$$ or $SCD$ is an equilateral triangle.
Angles $\angle AB,A'B'$ and $\angle CSD$ have corresponding sides.
Therefore: $\angle AB, A'B' \cong \angle CSD = 60^0$.
 \kdokaz

The next consequence of \ref{srednjicaTrik} applies to a trapezium.


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

\textbf{\textit{Proof.}}  The lines $PN$, $NQ$ and $PM$ are in turn medians of
the triangles
$DAC$, $ACB$ and $ADB$ for
the corresponding bases $DC$, $AB$ and $AB$ (Figure
\ref{sl.skl.3.6.3.pic}). Because of this, all three lines $PN$, $NQ$
and $PM$ are parallel to the bases $CD$ and $AB$. Since through each point (first $N$, then $P$) there is only one parallel to the line
$AB$ (Playfair's\footnote{\index{Playfair, J.}\textit{J.
Playfair} (1748--1819), Scottish mathematician.} axiom
\ref{Playfair}), the points $P$, $N$, $M$ and $Q$ are collinear. It also holds (from the statement \ref{srednjicaTrik}):
 $PN = \frac{1}{2} CD$ and
  $NQ = PM = \frac{1}{2} AB$. From this it follows:
   \begin{eqnarray*}
   PQ&=& PN+NQ=\frac{1}{2}CD+
   \frac{1}{2}AB=\frac{1}{2}\left(AB+CD\right)\\
  NM&=& PM-PN=\frac{1}{2}AB-
   \frac{1}{2}CD=\frac{1}{2}\left(AB-CD\right),
  \end{eqnarray*}
  which was to be proven.  \kdokaz

The line $PQ$ from the previous statement is called
\index{srednjica!trapeza} \pojem{median of the trapezoid}.

 The following statements apply to an arbitrary quadrilateral.


             \bizrek \label{Varignon}
             Let $ABCD$ be an arbitrary quadrilateral and $P$, $Q$, $K$ and $L$
            the midpoints of the sides $AB$, $CD$, $BC$ and $AD$, respectively. Then the quadrilateral $PKQL$ is
            a parallelogram (so-called \index{paralelogram!Varignonov}
              Varignon\footnote{\index{Varignon, P.}
              \textit{P. Varignon} (1654--1722),
             French mathematician,
            who was the first to prove this property. However, the statement was not published until
            after his death in 1731. Given the simplicity, it is
            quite surprising that this statement "waited" so long to be
            discovered.} parallelogram).
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.6.4.pic}
\caption{} \label{sl.skl.3.6.4.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skl.3.6.4.pic})
The lines $PK$ and $LQ$ are the medians of the triangles $ABC$ and $ADC$ for the same base $AC$, so they are congruent and
parallel. Therefore, the quadrilateral $PKQL$ is a parallelogram.
 \kdokaz

In a special case, Varignon's parallelogram can even be a rectangle,
rhombus or square. When is this possible? This question gives us an idea for
the next statement. We know that a parallelogram is a rectangle if it has
at least one internal  angle right. The other (equivalent) condition  is that it has congruent diagonals. A similar treatment can be used for rhombus and square.


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
 From the previous statement \ref{Varignon} it follows that
 the quadrilateral $PKQL$ is always a parallelogram – Varignon's
parallelogram. The lines $PL$ and $PK$ are the medians of the triangles $ABD$
and $ABC$ for the bases $AD$ and $AC$. Therefore, we have:
 $PL= \frac{1}{2}BD$ and $PL \parallel BD$ and $PK= \frac{1}{2}AC$ and $PK \parallel AC$.
 Therefore, we have:

 a) $AC \perp BD \Leftrightarrow PL \perp PK
\Leftrightarrow PKQL \textrm{ rectangle} \Leftrightarrow PQ
\cong KL$;

 b) $AC \cong BD \Leftrightarrow PL \cong PK \Leftrightarrow
  PKQL \textrm{ rhombus } \Leftrightarrow PQ \perp KL$.
 \kdokaz

If Varignon's parallelogram is a square, all four
conditions from the previous equivalences are fulfilled, or in this case: $AB \perp CD$, $AB \cong CD$, $PQ \perp KL$ and $PQ \cong KL$.

Let's look at one more use of the property of Varignon's parallelogram.

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

\textbf{\textit{Proof.}} Let $S$ be the center of the diagonal $AC$ of the quadrilateral $ABCD$ (Figure \ref{sl.skl.3.6.7.pic}). If we use the theorem about the median of a triangle (\ref{srednjicaTrik}) and the triangle inequality (\ref{neenaktrik}), we get: $$BC + AD = 2PS + 2SQ = 2(PS + SQ) \geq 2PQ.$$ The equality holds when the points $P$, $S$ and $Q$ are collinear, i.e. when the quadrilateral $ABCD$ is a trapezoid with the base $BC$. \kdokaz

 We mention that the inequality from the previous example also holds when the points $A$, $B$, $C$ and $D$ are not in the same plane, i.e. when the $ABCD$ is a \pojem{tetrahedron}.


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


\textbf{\textit{Solution.}} Let $R$ be the center of the line segment $QC$ (Figure \ref{sl.skl.3.6.8.pic}). The line segment $A_1R$ is the median of the triangle $BCQ$ for the base $BQ$, so (by the theorem \ref{srednjicaTrik}) $BQ = 2A_1R$ and $BQ\parallel A_1R$. From this parallelism and the definition of the point $P$ it follows that $PQ$ is the median of the triangle $AA_1R$ for the base $A_1R$, so (by the theorem \ref{srednjicaTrik} and Playfair's axiom \ref{Playfair}) the point $Q$ is the center of the line segment $AR$ and it holds $A_1R = 2PQ$. Therefore: $AQ \cong QR \cong RC$ i.e. $AQ:QC=1:2$. In the end it is also $BQ=2A_1R=4PQ$ i.e. $BP:PQ=3:1$.
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

\textbf{\textit{Solution.}} We mark with $a$ the length of the side and
with $O$ the center of the square $ABCD$ (Figure \ref{sl.skl.3.6.IMO1.pic}).

We first prove that the quadrilateral $MNPL$ is also a square with the same
center $O$. Because $ABP$, $BCL$, $CDM$ and $DAN$ are all right
triangles, the diagonals $MP$ and $LN$ of the quadrilateral $MNPL$ are on
the similitudes of the sides $AB$ and $BC$ of the square $ABCD$. From this it follows that $MP \perp LN$.
Since $d(M,AB)=d(P,CD)=a-v$ (where $v$ is the length
of the height of the aforementioned right triangles), it also holds that $OM\cong OP$.
Similarly, $OL\cong ON$, which means that the quadrilateral $MNPL$
is really a square with the same center~$O$.

We now prove that $LAM$ is a right triangle. Because $AB\cong
AD\cong BL\cong DM=a$ and $\angle LBA\cong\angle MDA
=90^0-60^0=30^0$, the triangles $LBA$ and $MDA$ are similar (by the \textit{SAS} \ref{SKS}). This means that $LA\cong MA$ and $\angle
DAL= 90^0-\angle LAB=15^0$. Similarly, $\angle BAM=15^0$ or
$\angle LAM = 90^0-2\cdot 15^0=60^0$. Therefore, $LAM$ is a right triangle, so the side of the square $MNPL$ has length
$b=|LM|=|LA|$.

Let's mark the center of the line $LM$ with $S$. The centers of the sides of the square $MNPL$ lie on the circle $k(O,\frac{b}{2})$, which is the inscribed circle of this square. We will prove that the point $T$ - the center of the line $AN$ - also lies on this circle. The line $OT$ is the median of the triangle $LAN$ for the base $LA$, so $OT\parallel LA$ and $|OT|=\frac{1}{2}|LA|=\frac{b}{2}$. Therefore, the point $T$ and, analogously, all the points defined in the problem of the $12$-gon lie on the circle $k(O,\frac{b}{2})$.

We will also prove that the aforementioned $12$-gon is regular. Without loss of generality, it is enough to prove that $\angle SOT=\frac{360^0}{12}=30^0$. But from the already proven fact $OT\parallel LA$ it follows that $\angle SOT\cong \angle LAS=\frac{1}{2}\angle LAM=30^0$.
 \kdokaz

%________________________________________________________________________________
 \poglavje{Triangle Centers} \label{odd3ZnamTock}

 We will continue our research with a triangle - the most simple
 polygon,
 which is at the same time
a figure that has unexpectedly many interesting properties. We will
discuss some of them in this section, some of them later, when we will
deal with other concepts, such as isometries and similarity.

 Now we will consider four \index{značilne točke
 trikotnika}\pojem{značilne točke
 trikotnika}\footnote{These four points are mentioned by the Ancient Greeks, although they
 (especially the centroid) were probably known long before that.} and
 their use in quadrilaterals and polygons.

We will start with the first among the characteristic points, which is related to
 the medians of the triangle. We have already defined
  the median in chapter \ref{odd3NeenTrik}.



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
 Let $AA_1$, $BB_1$ and $CC_1$ be the altitudes of the triangle $ABC$
   (Figure \ref{sl.skl.3.7.1.pic}).
Because of Pasch's axiom, \ref{AksPascheva} with respect to the triangle
$BCB_1$ and the line $AA_1$, the line $AA_1$ intersects the line segment $BB_1$.
Similarly, the line $BB_1$ intersects the line $AA_1$, which means that the
altitudes $AA_1$ and $BB_1$ intersect at some point $T$. Let $A_2$
and $B_2$ be the midpoints of the line segments $AT$ and $BT$. The line segments $A_1B_1$ and $A_2B_2$
are the medians of the triangles $ABC$ and $ABT$ with the same base $AB$. This
means that the line segments $A_1B_1$ and $A_2B_2$ are parallel and equal
to half of the side $AB$. Therefore, the quadrilateral $B_2A_1B_1A_2$
is a parallelogram (statement \ref{paralelogram}), which means that its
diagonals $A_1A_2$ and $B_1B_2$ intersect at their common center $T$. So it holds:
 $A_1T\cong TA_2 \cong A_2A$  and $B_1T\cong TB_2 \cong B_2B$
 or $AT:TA_1=2:1$ and $BT:TB_1=2:1$ and
  $$A_1T=\frac{1}{3}A_1A \textrm{ and }    B_1T = \frac{1}{3}B_1B.$$
  In the same way
 we prove that the altitudes $AA_1$ and $CC_1$ intersect at some
point $T'$, for which it holds $AT':T'A_1=2:1$ and $CT':T'C_1=2:1$ or:
 $$A_1T'=\frac{1}{3}A_1A \textrm{ and }    C_1T' = \frac{1}{3}C_1C.$$
This means that $T$ and $T'$ are points on the line segment $A_1A$, for which it holds
$A_1T\cong A_1T'=\frac{1}{3}A_1A$, so according to  \ref{ABnaPoltrakCX} $T = T'$, which means that the altitudes $AA_1$,
$BB_1$ and $CC_1$ intersect at the point $T$ and it holds
$AT:TA_1=BT:TB_1=CT:TC_1=2:1$.
 \kdokaz


The point from the previous statement, in which all altitudes of the triangle intersect, is called the
\index{težišče!trikotnika}\pojem{center of the triangle}.

The center of a triangle in the physical sense represents the point that is the center of mass of that triangle. This will be even more clear when we in section \ref{odd8PloTrik} prove the fact that the center divides the triangle into triangles with the same area. In the next chapter \ref{pogVEKT} (section \ref{odd5TezVeck}) we will consider the center of any polygon.

In section \ref{odd3PravilniVeck} we found that for any regular polygon there exist circumscribed (which contains all its vertices) and inscribed (which touches all its sides) circle with the same center. This property is also transferred to regular or equilateral triangles. But how is it with any triangle? We will prove that there exist the mentioned circles for any triangle, just that in the general case they have different centers.

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
  Let $p$, $q$ and $r$ be the perpendicular bisectors of sides $BC$, $AC$ and $AB$ of triangle $ABC$ (Figure \ref{sl.skl.3.7.2.pic}). The perpendicular bisectors $p$ and $q$ are not parallel (because in that case by Playfair's axiom \ref{Playfair} the lines $BC$ and $AC$ would be parallel too) and they intersect in some point $O$. Because this point lies on the perpendicular bisectors $p$ and $q$ of sides $BC$ and $AC$, we have $OB \cong OC$ and $OC \cong OA$. From this follows $OA \cong OB$, which means that the point $O$ also lies on the perpendicular bisector $r$ of the line $AB$. So the perpendicular bisectors $p$, $q$ and $r$ intersect in one point.

Because $OA \cong OB \cong OC$, the point $O$ is the center of the circle $k(O,OA)$, which contains all vertices of the triangle $ABC$.
 \kdokaz

The circle from the previous theorem, which contains all the vertices of the triangle, is called the \index{circumscribed circle!triangle} \pojem{circumscribed circle of the triangle}, and its center is the \index{center!circumscribed circle!triangle} \pojem{center of the circumscribed circle of the triangle}.

\bizrek \label{SredVcrtaneKrozn}
The bisectors of the interior angles of any triangle intersect at a single point, which is the centre of a circle touching all its sides.
\eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.3.pic}
\caption{} \label{sl.skl.3.7.3.pic}
\end{figure}

\textbf{\textit{Proof.}}
Let $p$, $q$, and $r$ be the angle bisectors of the angles at the vertices $A$, $B$, and $C$ of the triangle $ABC$ (Figure \ref{sl.skl.3.7.3.pic}). We shall prove that the bisectors $p$ and $q$ are not parallel. Otherwise, by Theorem \ref{KotiTransverzala}, the sum of the halves of the angles at the vertices $A$ and $B$ would be equal to $180°$, which, by Theorem \ref{VsotKotTrik}, is not possible. Therefore, $p$ and $q$ intersect at some point $S$. Since the point $S$ lies on the angle bisectors of the angles at the vertices $A$ and $B$, it is equidistant from the sides $AC$ and $AB$ (Theorem \ref{SimKotaKraka}). From this it follows that the point $S$ is also equidistant from the sides $BA$ and $BC$, which means that it lies on the bisector $r$ of the angle at the vertex $C$. Therefore, the angle bisectors $p$, $q$, and $r$ intersect at the point $S$.

With $P$, $Q$ in $R$ we denote the orthogonal projections of point $S$ onto
the sides $BC$, $CA$ and $AB$. Because $\frac{1}{2}\angle CBA<90^0$
and $\frac{1}{2}\angle BCA<90^0$, it follows that $\mathcal{B}(B,P,C)$. Similarly,
$\mathcal{B}(C,Q,A)$ and $\mathcal{B}(A,R,B)$ also hold. Because of the already proven properties of point $S$, it follows that $SP \cong SQ \cong SR$. Therefore, the point $S$ is the center of the circle $l$, which passes through points $P$, $Q$ and
$R$. Because of the perpendicularity of the radii $SP$, $SQ$ and $SR$ to the respective sides, they are tangent to the circle $l$. Because $\mathcal{B}(B,P,C)$,  $\mathcal{B}(C,Q,A)$ and $\mathcal{B}(A,R,B)$ hold, the circle $l$ is tangent to all
         sides of the triangle $ABC$.
 \kdokaz


 The circle from the previous  statement, which is tangent to all
         sides of the triangle, is called  \index{včrtana krožnica!trikotnika} \pojem{the inscribed circle of the triangle}, and its center
        \index{središče!včcrtane krožnice!trikotnika}
        \pojem{the center of the inscribed circle of the triangle}.

There is one more of the four aforementioned characteristic points of the triangle.
It is related to the altitudes of the triangle.


        \bizrek \label{VisinskaTocka}
        The lines containing the altitudes of a triangle  intersect at a single point.
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.4.pic}
\caption{} \label{sl.skl.3.7.4.pic}
\end{figure}

\textbf{\textit{Proof.}}
  Let $p$, $q$ and $r$ be the altitude lines
    $AA'$, $BB'$ and $CC'$
   of the triangle $ABC$ (Figure \ref{sl.skl.3.7.4.pic}).
We denote by $a$, $b$ and $c$ the lines that are perpendicular to the respective heights in points $A$, $B$ and $C$. Because the lines $a$, $b$ and $c$ are parallel to the sides of the triangle $ABC$, each two of them intersect. We denote by $P$, $Q$ and $R$ the intersections of the lines $b$ and $c$, $a$ and $c$, and $a$ and $b$, in order. The quadrilateral $ABCQ$ and $RBCA$ are parallelograms, which means that $RA \cong BC \cong AQ$, or the point $A$ is the center of the line $RQ$. The line $AA'$ is therefore the perpendicular bisector of the side $RQ$ of the triangle $PQR$. Similarly, $BB'$ and $CC'$ are the perpendicular bisectors of the sides $PR$ and $PQ$ of the same triangle. By the theorem \ref{SredOcrtaneKrozn}, the perpendicular bisectors $AA'$, $BB'$ and $CC'$ of the triangle $PQR$ intersect in some point $V$. The point $V$ is therefore the intersection of the altitude lines
    $AA'$, $BB'$ and $CC'$
   of the triangle $ABC$.
   \kdokaz

The point from the previous theorem, in which the altitude lines intersect, is called
\index{višinska točka trikotnika}
         \pojem{the altitude point of the triangle}. The triangle $A'B'C'$, which is determined by the altitudes of the triangle $ABC$, is called
\index{trikotnik!pedalni} \pojem{the pedal triangle} of the triangle
$ABC$.

We have found that every triangle has four characteristic points,
namely: the centroid, the center of the circumscribed circle, the center of the inscribed circle and the altitude point. But these are not the only characteristic points
of the triangle. We will mention some of them later. For
a point in the plane of the triangle in general, we say that it is its
\pojem{characteristic point}, if its definition is symmetrical with respect to
the vertices of this triangle.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.5.pic}
\caption{} \label{sl.skl.3.7.5.pic}
\end{figure}


 It is clear that in any triangle the four characteristic points differ
 (Figure \ref{sl.skl.3.7.5.pic}).

In an isosceles triangle, the centroid,
the altitude, the line of symmetry of the base, and the line of symmetry of the internal angle opposite the base
have the same carrier. If $A_1$ is the center of the base
$BC$ of the isosceles triangle $ABC$, the triangles $ABA_1$ and
$ACA_1$ are congruent, which means that the angle at the vertex $A_1$ is a right angle
and the angles $BAA_1$ and $CAA_1$ are congruent. Therefore, the distance
$AA_1$ is both the centroid and the altitude, and the line $AA_1$ is both
the line of symmetry of the side $BC$ and the line of symmetry of the internal angle at the vertex $A$
of the triangle $ABC$. It follows that all four characteristic points of this
triangle lie on one line $AA_1$ (Figure
\ref{sl.skl.3.7.6.pic}).

If we use the already proven property of an isosceles triangle for
an equilateral triangle, we find that all the appropriate
centroids, altitudes, side lines of symmetry, and internal angle lines of symmetry
have the same carrier. This means that in an equilateral triangle
all four characteristic points coincide (Figure \ref{sl.skl.3.7.6.pic}).
This is actually already defined (section \ref{odd3PravilniVeck})
as the center of this equilateral (or regular) triangle.


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.6.pic}
\caption{} \label{sl.skl.3.7.6.pic}
\end{figure}

We will also show the position of the characteristic points with respect to the type of
triangle.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.7.pic}
\caption{} \label{sl.skl.3.7.7.pic}
\end{figure}

The centroids are always inside the triangle. Therefore, the center
is an internal point of every triangle (Figure \ref{sl.skl.3.7.7.pic}).
The same conclusion applies to the center of the inscribed circle (Figure
\ref{sl.skl.3.7.7s.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.7s.pic}
\caption{} \label{sl.skl.3.7.7s.pic}
\end{figure}

In an acute triangle, the vertices of the perpendiculars from its vertices
lie on the sides of this triangle, which means (Pasch's axiom
\ref{AksPascheva}), that its altitudes intersect in the interior. So in
an acute triangle, the altitude point lies in its interior
(Figure \ref{sl.skl.3.7.7v.pic}). In a right-angled triangle, the altitude point is the vertex at the right angle. This is because its
catheti are at the same time altitudes of the triangle. The altitude point of an obtuse triangle lies in its exterior, because
 not all of the altitudes are in its interior. The corresponding vertices
belong to the sides' supports, not to the sides themselves.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.7v.pic}
\caption{} \label{sl.skl.3.7.7v.pic}
\end{figure}

The centre of the circumscribed circle is an interior or exterior point of the triangle, depending on whether the triangle is acute or obtuse (Figure
\ref{sl.skl.3.7.7o.pic}). We will omit the formal proof of this fact. We will only prove the following statement, which refers to right-angled triangles.

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


\textbf{\textit{Proof.}} We mark with $O$ the centre of the hypotenuse $AB$ and
with $P$ the centre of the cathetus $AC$ of the right-angled triangle $ABC$ (Figure
\ref{sl.skl.3.7.8.pic}). The distance $OP$ is the median of this triangle,
which corresponds to the cathetus $BC$, so $OP\parallel BC$. From this it follows that $OP
\perp AC$. Therefore, the triangles $OPC$ and $OPA$  are congruent (the statement
\textit{SAS} \ref{SKS}) and then $OC \cong OA$.
Since $OB \cong OA$ as well,
 the point $O$ is the centre of the circumscribed circle of this triangle.
 \kdokaz

The line $OC$ from the previous theorem is the median of the triangle. This means that the median of a right angled triangle is equal to the radius of the inscribed circle of that triangle, and also to half of its hypotenuse.

The previous theorem is also connected to Thales’ theorem for a circle \ref{TalesovIzrKroz} and its converse \ref{TalesovIzrKrozObrat}. We will now state all of these theorems in one theorem.


          \bizrek Thales’ theorem for a circle (several forms - Figure
          \ref{sl.skl.3.7.9.pic}):
         \index{theorem!Thales’ for a circle}
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
            \index{theorem!Thales’ for a circle}
             \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.9.pic}
\caption{} \label{sl.skl.3.7.9.pic}
\end{figure}

Knowing the characteristic points of a triangle and the properties of a median of a triangle allows us to prove various other properties of both triangles and quadrilaterals and $n$-gons.


              \bzgled
              Let $CD$ be the altitude  at the hypotenuse $AB$ of a right-angled triangle $ABC$.
            If $M$ and $N$ are the midpoints of the line segments $CD$ and $BD$, then $AM \perp CN$.
           \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.10.pic}
\caption{} \label{sl.skl.3.7.10.pic}
\end{figure}

\textbf{\textit{Proof.}}  The line $NM$ is the median of the triangle
$BCD$, so by the \ref{srednjicaTrik} $NM \parallel BC$
(Figure \ref{sl.skl.3.7.10.pic}). Because the angle at the vertex $C$ is a right
angle, $NM \perp AC$ as well. Because of this, the line $NM$ is the altitude of the triangle $ANC$. Since $CD$ is also the altitude of this triangle, $M$ is its height point. Therefore, the line $AM$ is the altitude of the third triangle of this triangle and $AM \perp CN$ applies.
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

\textbf{\textit{Proof.}} We mark with $E$ and $F$ the intersections of the lines
$AP$ and $AQ$ with the diagonal $BD$ of the parallelogram $ABCD$ and with $S$
the intersection of its diagonals $AC$ and $BD$ (Figure
\ref{sl.skl.3.7.11.pic}). The diagonals of the parallelogram are divided
(from \ref{paralelogram}), so the point $S$ is the common center of the lines
$AC$ and $BD$. This means that the points $E$ and $F$ are the centers of the triangles
$ACB$ and $ACD$, so they divide the altitudes $SB$ and $SD$ of these triangles
in the ratio $2:1$ (from \ref{tezisce}). Therefore:
 \begin{eqnarray*}
     BE &=& \frac{2}{3}BS = \frac{2}{3}DS = FD,\\
     EF&=& ES+ SF= \frac{1}{3}SB+ \frac{1}{3}SD=
     \frac{1}{3}(SB +SD)=\frac{1}{3} BD,
 \end{eqnarray*}
  which is what we wanted to prove.  \kdokaz


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
 Let $AA'$
 be the altitude of the triangle $ABC$ (Figure \ref{sl.skl.3.7.12.pic}). We mark with $X$
  and $Y$ the intersections of the line $AA'$ with
the rectangles on the line $CL$ through the point $B$ and on the line $BP$ through the point $C$.
We prove that $X = Y$. The triangle $BLC$ and $ABX$ are similar according to the \textit{ASA} theorem \ref{KSK} because: $BL \cong AB$,
$\angle BLC\cong\angle ABX$ and $\angle BCL\cong\angle AXB$ (the angle with perpendicular sides -
theorem \ref{KotaPravokKraki}). Therefore $AX \cong BC$. Similarly,
the triangle $CPB$ and $ACY$ are similar, so $AY \cong BC$.
Therefore $AX \cong AY$ or $X = Y$. This means that the lines
$AA'$, $BP$ and $CL$ are the altitudes of the triangle $XBC$, so they intersect at
one point.
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

\textbf{\textit{Proof.}} Let $V$ be the center of the line $BL$ (Figure \ref{sl.skl.3.7.13.pic}). The line $SV$ is the median of the triangle $ABL$ for the base $AB$, so $SV\parallel AB$ and $SV =\frac{1}{2} AB$ (statement \ref{srednjicaTrik}). From the first relation and $BC\perp AB$ it follows that $SV\perp BC$ (statement \ref{KotiTransverzala}). This means that $BL$ and $SV$ are the altitude of the triangle $CSB$. Therefore, $V$  is the altitude point of this triangle, so $CV$ is the altitude of its third altitude (statement \ref{VisinskaTocka}) or $CV\perp SB$ is true. From $SV\parallel AB$ and $SV =\frac{1}{2} AB=KC$ it follows that the quadrilateral $SVCK$ is a parallelogram or $CV\parallel SK$ is true. From this and $CV\perp SB$ it finally follows (statement \ref{KotiTransverzala})  $SK\perp SB$, so $\angle KSB$ is a right angle.
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

\textbf{\textit{Proof.}} Let $PQR$ be a right triangle or $PQ\cong QR\cong RP$ (Figure \ref{sl.skl.3.7.14.pic}). The point $Q$ is the center of the hypotenuse $AC$ of the right triangle $APC$, so $QA \cong QC \cong QP$ (statement \ref{TalesovIzrKroz2}. Because in this case $QR\cong QC\cong QP$, from the same statement it follows that $\angle ARC$ is a right angle. From the similarity of the triangles $ACR$ and $BCR$ (statement \ref{KSK}) we get that the point $R$ is the center of the side $AB$ and that $AC\cong BC$ is true. Because the point $R$ is the center of the hypotenuse $AB$ of the right triangle $APB$, $AB = 2RP = 2PQ = 2AQ = AC$. Therefore, $AB\cong AC\cong BC$ is true, which means that $ABC$ is a right triangle.
 \kdokaz

It is not difficult to prove that a triangle is equilateral if and only if the corresponding medians are concurrent. The same is true for altitudes. But is something similar true for so-called angle bisectors?
 The line segments $BB'$ and $CC'$, where $BB'$ and $CC'$ are angle bisectors of the triangle $ABC$ and $B'\in AC$ and $C'\in AB$, are called
 \index{angle bisector} \pojem{angle bisectors}. Angle bisectors are denoted by $l_a$, $l_b$ and $l_c$.
 The aforementioned
  statement  is also true in this case, but
the proof is not so simple. This is the subject of the following well-known theorem.



            \bizrek \index{theorem!Steiner-Lemus}
            (Steiner-Lehmus\footnote{\textit{D. C. L. Lehmus} (1780--1863),\index{Lehmus, D. C. L.} French
            mathematician, who in 1840 sent this, at first glance simple
            statement, to the famous Swiss geometer \index{Steiner, J.} \textit{J. Steiner} (1796--1863),
             who  derived a very extensive proof of this theorem. Then followed
             several different solutions to this problem and one of them was published in 1908
              by
             the French mathematician \index{Poincar\'{e}, J. H.} \textit{J. H. Poincar\'{e}} (1854--1912).})
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

($\Rightarrow$) From $AB \cong AC$ it follows that $\angle ABC \cong \angle
ACB$ (theorem \ref{enakokraki}) or $\angle B'BC \cong \angle C'CB$.
By the \textit{ASA} theorem \ref{KSK}, the triangles $B'BC$ and $C'CB$
are congruent, so $BB'\cong CC'$.

($\Leftarrow$) Let $BB'\cong CC'$.
 We assume that $AB\not\cong AC$. Without loss of generality
 let $AB < AC$. In this case $\angle ACB < \angle ABC$
 (by \ref{vecstrveckot}) or
$\angle ACC'< \angle ABB'$. This means that inside the angle $ABB'$
there is a segment $p$ with endpoint $B$, which intersects the side
$AC$ in such a point $D$, that both $\mathcal{B}(A,D,B')$ and $\angle
DBB'\cong \angle ACC'$ are true. In the triangle $BCD$ is $\angle ACB <
\angle DBC$ and because of that also $BD < CD$ (by \ref{vecstrveckot}).
Therefore there is such a point $E$, which is between the points $C$
and $D$, so that $BD \cong CE$. By the \textit{SAS} \ref{SKS} the
triangles $BDB'$ and $CEC'$ are similar, therefore the angles $BDB'$
and $CEC'$ are similar. We prove that this is not possible. Because
of Pasch's axiom \ref{AksPascheva} (used for the triangle $AC'E$ and
the line $BD$) the line $BD$ intersects the line $C'E$ in some point
$S$. In the triangle $SDE$ is the angle $SEC$ (or the angle $CEC'$)
external and by \ref{zunanjiNotrNotrVecji} it can not be similar to
the adjacent internal angle $SDE$ (or the angle $BDB'$). This means
that the assumption $AB < AC$ (analogously $AB > AC$) is not possible.
Therefore $AB\cong AC$.
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

From $\angle CC'B = 90^0$ it follows first
$\angle C'CB=60^0$, then that the point $C'$ lies on the circle above
the diameter $CB$ and with the center $A_1$ (by \ref{TalesovIzrKroz}), so
$A_1C'\cong A_1C\cong A_1B$. Therefore, the triangle $CC'A_1$
is isosceles, or by \ref{enakokraki} it holds $\angle CC'A_1
\cong\angle C'CB=60^0$. This means that the triangle $CC'A_1$
is equilateral and $C'C\cong C'A_1$. From the fact that $AC'C$ is an isosceles triangle ($\angle CAC'=\angle ACC'=45^0$), it follows that $AC'\cong C'C$. If we connect this with the previous relation, we get $AC'\cong C'A_1$, which
means that the triangle $AC'A_1$ is also isosceles. Therefore, it is (by \ref{enakokraki} and \ref{zunanjiNotrNotr}):
 $$\angle C'A_1A\cong\angle C'AA_1=\frac{1}{2}\angle A_1C'B=
 \frac{1}{2}\angle C'BA_1=\frac{1}{2}\cdot 30^0=15^0.$$
 In the end there is also:
  $$\angle AA_1C=\angle C'A_1C-\angle C'A_1A =60^0-15^0=45^0,$$ which needed to be calculated. \kdokaz


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

\textbf{\textit{Proof.}} From the congruence of the triangles $ABP$ and $ACP$
(from the statement \textit{SSS} \ref{SSS}) it follows that the congruence of the sides $APB$ and
$APC$ or $AP\perp BC$ (Figure \ref{sl.skl.3.7.16.pic}). We mark with
$R$ the center of the line $QC$. The line $SR$ is the median of the triangle
$QPC$ for the base $PC$, so according to the statement \ref{srednjicaTrik}
$SR\parallel CP$. From this and $AP\perp BC$ it follows that $SR\perp AP$. So
$S$ is the altitude point of the triangle $APR$, so according to the statement
\ref{VisinskaTocka} also $AS\perp PR$. But the line $PR$ is
the median of the triangle $BQC$ for the base $BQ$, so $PR\parallel BQ$
(from the statement \ref{srednjicaTrik}). From $AS\perp PR$ and $PR\parallel BQ$
we get $AS\perp BQ$.
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

\textbf{\textit{Proof.}}  According to the statement \ref{SredVcrtaneKrozn} the simetrals of the internal angles of the triangle $ABC$ intersect in the center of the inscribed circle - in the point $S$ (Figure \ref{sl.skl.3.7.1c.pic}). So
$\angle SBC =\frac{1}{2}\cdot \beta$ and $\angle SCB
=\frac{1}{2}\cdot \gamma$. Because according to the statement \ref{VsotKotTrik} in every
triangle the sum of the internal angles is equal to $180^0$, it follows:
 $$\angle BSC = 180^0-\frac{1}{2}\cdot\left( \beta+
  \gamma\right)=180^0-\frac{1}{2}\cdot\left( 180^0-
 \alpha\right)=90^0+\frac{1}{2}\cdot\alpha,$$ which had to be proven. \kdokaz


        \bzgled
        Construct a triangle with given $a$, $t_a$, $R$ (see the labels  in section \ref{odd3Stirik}).
        \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skl.3.7.16a.pic}
\caption{} \label{sl.skl.3.7.16a.pic}
\end{figure}

\textbf{\textit{Proof.}} The construction can be carried out by first drawing the circumscribed circle $k(O,R)$, choosing an arbitrary point $B\in k$, planning the cord $BC\cong a$ of the circle, the center $A_1$ of the cord $BC$ and finally the point $A$ as the intersection of the circles $k(O,R)$ and $k_1(A_1,t_a)$ (Figure \ref{sl.skl.3.7.16a.pic}). It is clear that the task of the solution is exactly when $a\leq 2R$ and the intersection of the circles $k(O,R)$ and $k_1(A_1,t_a)$ is not an empty set. The number of solutions in this case depends on the number of intersections of the circles $k(O,R)$ and $k_1(A_1,t_a)$.
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
Let $ABC$ be a right-angled triangle with a right angle at the vertex $C$,
in which the hypotenuse $AB$ and the altitude $CC'$ are congruent to the line segments $c$ and $v_c$ (Figure \ref{sl.skl.3.7.16b.pic}).
By the \ref{TalesovIzrKroz2} theorem, the center $O$ of the hypotenuse $AB$ is also the center of the circumscribed circle of the triangle $ABC$.
Therefore, the vertex $C$ lies on the circle $k$ with diameter $AB$. Since $CC'\cong v_c$, the vertex $C$ also lies on the parallel $p$ to the line $AB$ at a distance $v_c$. The point $C$ is then the intersection of this parallel and the circle $k$.


\textbf{\textit{Construction.}}
First, we plan the line $AB$, which is congruent to the given line segment $c$, then the center $O$ of the line $AB$ and the circle $k(O,OA)$. Then we plan the parallel $p$ to the line $AB$ at a distance $v_c$. One of the intersections of the line $p$ and the circle $k(O,OA)$ is denoted by $C$. We prove that $ABC$ is the desired triangle.

\textbf{\textit{Proof.}}
 By construction, point $C$ lies on the circle with radius $AB$, so by \ref{TalesovIzrKroz2} $\angle ACB=90^0$, which means that $ABC$ is a right triangle with hypotenuse $AB$. By construction, it is consistent with the distance $c$. Let $CC'$ be the altitude of the triangle $ABC$. By construction, point $C$ lies on the line $p$, which is from the line $AB$ at a distance $v_c$, so also $|CC'|=d(C,AB)=d(p,AB)$ or $CC'\cong v_c$.


\textbf{\textit{Discussion.}}
 The number of solutions is dependent on the number of intersections of the line $p$ and the circle $k(O,OA)$.
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

\textbf{\textit{Solution.}} Let $ABC$ be a triangle, such that
$AA' \cong v_a$ and $BB' \cong v_b$ are its altitudes and $AA_1\cong
t_a$ is its median (Figure \ref{sl.skl.3.7.IMO1.pic}). We mark with
$A'_1$ the orthogonal projection of point $A_1$ on the line $AC$.
The distance $A_1A'_1$ is the median of the triangle $BB'C$ for the
base $BB'$, so by \ref{srednjicaTrik}:
 $$|A_1A'_1|=\frac{1}{2}\cdot|BB'|=\frac{1}{2}\cdot v_b
 \hspace*{1mm} \textrm{ in }  \hspace*{1mm} A_1A'_1
\parallel BB'.$$ From this it follows that the lines
$A_1A'_1$ and $AC$ are perpendicular in point $A'_1$, thus the line $AC$
is tangent to the circle $k(A_1,\frac{1}{2} v_b)$ \ref{TangPogoj}.
The proven properties allow us to construct it.

First, we can plan the rectangular triangle $AA'A_1$ ($AA'\cong v_a$,
 $AA_1\cong t_a$ and $\angle AA'A_1 = 90^0$), then the circle
 $k(A_1,\frac{1}{2} v_b)$. From the point $A$ we plan the tangents to
 the circle $k(A_1,\frac{1}{2} v_b)$. The intersection of one of the tangents
 with the line $A'A_1$ is denoted by $C$. In the end, we plan such a point
  $B$, that
  $BA_1 \cong CA_1$ and $\mathcal{B}(C,A_1,B)$.

 We prove that the triangle $ABC$ satisfies the given conditions. From
 the construction it is $AA'\cong v_a$ the height and $AA_1 \cong t_a$
 the centroid (because $A_1$ is the center of the line $BC$) of the triangle
 $ABC$. Let $BB'$ be the height of this triangle. We prove that $BB' \cong
 v_b$.
 The line $AC$ is by construction the tangent of the circle $k(A_1,\frac{1}{2}
 v_b)$. Their point of contact is denoted by $A'_1$. By the theorem
 \ref{TangPogoj} the lines
$A_1A'_1$ and $AC$ are perpendicular in the point $A'_1$, therefore the line
$A_1A'_1$ is the median of the triangle $BB'C$ for the base $BB'$ and it is valid
$|BB'|= 2\cdot |A_1A'_1|=2\cdot\frac{1}{2}\cdot v_b=v_b$.

 The task has no solution when $v_a>t_a$. If  $v_a\leq
 t_a$, the number of solutions depends on the number of tangents, which we
 can plan from the point $A$ on the circle $k(A_1,\frac{1}{2}
 v_b)$. In this case, the tangent must intersect the line $A'A_1$.
 If $\frac{1}{2} v_b<t_a$ and $\frac{1}{2} v_b\neq v_a$,
  the task has two solutions, in the case $\frac{1}{2} v_b<t_a$ and
  $\frac{1}{2} v_b = v_a$ there is only one solution,  in the case
  $\frac{1}{2} v_b\geq t_a$ there are no solutions.
 \kdokaz


%________________________________________________________________________________
 \poglavje{Euler's Circle. Eight Point Circle}
 \label{odd3EulKroz}

We will now look at an interesting property that relates to
\index{trikotnik!pedalni}pedalni trikotnik, which we have already defined
as a triangle that is determined by the points of intersection of the heights of some triangle, and i.e.
\index{trikotnik!središčni} \pojem{središčni trikotnik}, which is determined by
the midpoints of the sides of this triangle. We will prove that
the aforementioned triangles have a common circumscribed circle (Figure
\ref{sl.skl.3.8.1.pic}). But before we do that, we prove the following lemma.


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
 Let $AA'$ be the height of this triangle. The line segments
$KN$
and $LM$ are the midpoints of the triangles $ABA'$ and $CAA'$ for the common
base $AA'$, so according to izrek \ref{srednjicaTrik}
$KN=\frac{1}{2}AA'=LM$ and $KN\parallel AA'\parallel LM$ (Figure
\ref{sl.skl.3.8.2.pic}). Therefore, the quadrilateral $KLMN$  is a parallelogram.
It is enough to prove that it has at least one internal angle that is a right angle.
The line segment $KL$ is the midpoint of the triangle $ABC$, so $KL\parallel
BC$. Since $KN\parallel AA'$ and $AA'\perp BC$, it follows that
$KL\perp KN$ or $\angle LKN=90^0$, which means that
the parallelogram $KLMN$ is also a rectangle.
 \kdokaz

 We are now ready to prove the main theorem.

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
We will use the previous claim \ref{EulerKroznica}. If we keep the same labels, we have already proven that the quadrilateral $KLMN$ is a rectangle (Figure \ref{sl.skl.3.8.3.pic}). If we denote with $P$ the midpoint of the side $BC$ and with $Q$ the midpoint of the line $AV$, then also $PMQK$ is a rectangle. Because $KM$ is the common diagonal of these two rectangles, it is the diameter of their common circumscribed circle $e$. Therefore, the midpoints of the sides and the midpoints of the lines connecting the altitude point and the vertex belong to the same circle $e$. We will also prove that the intersection points of the altitudes lie on this circle. The point $A'$, which is the intersection point of the altitude from the vertex $A$, lies on the circle $e$, because $\angle QA'P$ is a right angle and $PQ$ is the diameter of the circle $e$ (Tales' theorem \ref{TalesovIzrKroz2}). Analogously, on this circle also lie the intersection points $B'$ and $C'$ of the altitudes $BB'$ and $CC'$.
 \kdokaz

 We call the Euler circle also the \index{circle!nine points} \index{circle!Feuerbach's} \pojem{Feuerbach circle} and the \pojem{circle of nine points}. We will discuss some more properties of the Euler circle in sections \ref{odd5EulPrem} and \ref{odd7SredRazteg}. Now we prove the analogous claim for the quadrilaterals called the \index{circle!eight points} \pojem{circle of eight points}.



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

\textbf{\textit{Proof.}} Let $ABCD$ be a quadrilateral with
perpendicular diagonals $AC$ and $BD$ (Figure \ref{sl.skl.3.8.4.pic}).
Let $A_1$, $B_1$, $C_1$ and $D_1$ be the centers of its sides $AB$,
$BC$, $CD$ and $DA$, and let $A'$, $B'$, $C'$ and $D'$ be the
perpendicular projections of these centers onto the lines of the
opposite sides of this quadrilateral. The quadrilateral $A_1B_1C_1D_1$
is a parallelogram (Varignon's parallelogram - Theorem
\ref{Varignon}). Because the diagonals $AC$ and $BD$ are
perpendicular, this parallelogram is a rectangle (Theorem
\ref{VarignonPoslPravRomb}), so its vertices lie on the same circle.
The diagonals $A_1C_1$ and $B_1D_1$ are the diameters of this circle.
Because $\angle C_1C'A_1=\angle C_1A'A_1=\angle B_1D'D_1=\angle
B_1B'D_1=90^0$, it follows (Tales' Theorem \ref{TalesovIzrKroz2}) that
the points $A'$, $B'$, $C'$ and $D'$ also lie on this circle.
 \kdokaz

 We mention that for any triangle $ABC$ with altitude point $V$
  its Euler circle  can be seen as
the circle of eight points of the quadrilateral $ABVC$ (its diagonals
$AV$ and $BC$ are perpendicular - Figure \ref{sl.skl.3.8.5.pic}), but
in this case two pairs of points overlap and we actually get only six
points\footnote{This fact was proved by the American mathematician
\index{Brand, L.} \textit{L. Brand} (1885--1971) in 1944}. To prove
that the statement (for the Euler circle) is true for the other three
points, we use the circle of eight points for the quadrilateral
$CAVB$. Because the two circles (for the quadrilateral $ABVC$ and
$CAVB$) have at least three common points, the circles overlap - they
are the same Euler circle of the triangle $ABC$.

\begin{figure}[!htb]
\centering
\input{sl.skl.3.8.5.pic}
\caption{} \label{sl.skl.3.8.5.pic}
\end{figure}

 %_______________________________________________________________________________
 \poglavje{Tessellations} \label{odd3Tlakovanja}

In this section we will deal with the covering of the plane with
congruent figures. Such a covering is called a
\index{tlakovanja} \pojem{tessellation} or a
\index{teselacija} \pojem{tessellation} of the plane. The figure
with which we cover the plane in this way is called a
\index{celica tlakovanja} \pojem{tessellation cell}. The most
famous tessellation is of course the covering of the plane with
congruent squares. We will also consider tessellations with other
figures. First we will answer the question of which tessellations
with regular polygons are possible.

\bizrek \label{pravilnaTlakovanja}
All possible tessellations $(n,m)$ of the plane with a regular $n$-gons,
$m$ of them around each vertex, are
(Figure \ref{sl.skl.3.9.1.pic})\footnote{This problem was solved by
the famous Greek philosopher and mathematician \index{Pitagora}
\textit{Pitagora from the island of Samos}
 (582--497 BC).}:
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

\textbf{\textit{Proof.}} Let $O$ be the center and $AB$ one side of
the tessellation cell $(n,m)$ - a regular $n$-gon (Figure
\ref{sl.skl.3.9.2.pic}). With $S$ we denote the center of the side
$AB$. Because the initial $n$-gon is regular and there are $m$ such
around the vertex $B$, the internal angles of the triangle $OSB$ at
the vertices $O$, $B$ and $S$ measure $\frac{360^0}{2n}$,
$\frac{360^0}{2m}$ and $90^0$ in order. By \ref{VsotKotTrik} the
$\frac{360^0}{2n}+\frac{360^0}{2m}+90^0=180^0$. If we simplify the
equality, we get the equivalent equality:
$$\frac{1}{n}+\frac{1}{m}=\frac{1}{2},$$
or $nm-2n-2m=0$ and finally:
 \begin{eqnarray}
(n-2)(m-2)=4. \label{teselRelEvk}
\end{eqnarray}

Since $n$ and $m$ are natural numbers and greater than $2$,
the only solutions of the last equation are: $(n,m)\in \{(4,4), (3,6), (6,3)\}$.
 \kdokaz

\begin{figure}[!htb]
\centering
\input{sl.skl.3.9.2.pic}
\caption{} \label{sl.skl.3.9.2.pic}
\end{figure}

Tiling of the plane with regular polygons is called
\index{tlakovanja!pravilna} \pojem{pravilna tlakovanja} ravnine. In
Euclidean plane  there are therefore three regular tilings.

Since in hyperbolic geometry the sum of the interior angles of a triangle
is always less than $180^0$, the relation for the triangle $OSB$ from the previous
\ref{pravilnaTlakovanja} izreka becomes:
$\frac{360^0}{2n}+\frac{360^0}{2m}+90^0<180^0$ and then instead of
relation \ref{teselRelEvk} we get:
 \begin{eqnarray}
(n-2)(m-2)>4. \label{teselRelHyp}
\end{eqnarray}
 This inequality has infinitely many solutions in the set $\mathbb{N}^2$, which means
that we have in hyperbolic geometry  infinitely many regular tilings.
Two of them are for example $(3,7)$ and $(4,5)$ (Figure
\ref{sl.skl.3.9.2H.pic}\footnote{http://math.slu.edu/escher/index.php/Category:Hyperbolic-Tessellations}).
In the latter, five squares touch around one vertex. This is
possible because in hyperbolic geometry the interior angle of a square is always
sharp and is not constant. It turns out that the square with the longer side
has a smaller interior angle. It is possible to choose such a side of the square
that the interior angle is equal to $\frac{360^0}{5} =72^0$, which just
corresponds to the tiling $(4,5)$.

\begin{figure}[!htb]
\centering
\includegraphics[width=0.413\textwidth]{whyptess1.eps}\hspace*{4mm}
 \includegraphics[width=0.387\textwidth]{whyptess.eps}
\caption{} \label{sl.skl.3.9.2H.pic}
\end{figure}

In elliptic geometry, where the sum of the angles in a triangle is always
greater than $180^0$, the aforementioned relation for triangle $OSB$ becomes:
$\frac{360^0}{2n}+\frac{360^0}{2m}+90^0>180^0$, or:
 \begin{eqnarray}
(n-2)(m-2)<4. \label{teselRelElipt}
\end{eqnarray}
This equation has solutions $(3,3)$, $(4,3)$,
$(3,4$), $(5,3)$ and $(3,5)$ in the set $\mathbb{N}^2$. Because elliptic geometry is realized
as a model on a sphere, these solutions represent tessellations of the sphere with spherical
polygons. The sides of these polygons are arcs of great circles of the sphere.
If in Euclidean space with distances we connect the appropriate vertices of these
tessellations, we get the so-called \index{pravilni!poliedri} \pojem{regular
polyhedra} (Figure
\ref{sl.skl.3.9.2E.pic}\footnote{http://www.upc.edu/ea-smi/personal/claudi/web3d/}):
\pojem{regular tetrahedron}, \pojem{cube} (or \pojem{regular
hexahedron}), \pojem{regular octahedron}, \pojem{regular dodecahedron}
and \pojem{regular icohedron}. For example, $(4,3)$ would represent a cube,
in which three squares (regular 4-gon) meet at one point.


\begin{figure}[!htb]
\centering
 \includegraphics[bb=0 0 11cm 6cm]{wpoliedri.eps}
\caption{} \label{sl.skl.3.9.2E.pic}
\end{figure}


Let's go back to the Euclidean plane. If we allow the possibility that in
covering the plane we use more (finitely many) types of regular
polygons or more types of cells that are arranged the same way at each vertex, then in addition to the three regular
tessellations from the statement \ref{pravilnaTlakovanja} there are eight so-called
\index{tlakovanja!Arhimedova} \pojem{Archimedean tessellations}
\footnote{The proof of this statement was carried out by the German astronomer, mathematician and
physicist \index{Kepler, J.} \textit{J. Kepler} (1571--1630).} (Figure
\ref{sl.skl.3.9.2A.pic}\footnote{http://commons.wikimedia.org/wiki/File\%3AArchimedean-Lattice.png}).



\begin{figure}[!htb]
\centering
 \includegraphics[bb=0 0 10cm 7.7cm]{Archimedean.eps}
\caption{} \label{sl.skl.3.9.2A.pic}
\end{figure}

In addition to regular and Archimedean tilings, there are also other
tilings with polygons that are not regular. The simplest example
is the tiling with congruent parallelograms (Figure
\ref{sl.skl.3.9.3a.pic}), which we get if we deform the regular
tiling $(4,4)$ so that instead of squares in one vertex, four
parallelograms meet. This tiling is determined by the grid
of two sets of parallel lines.

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

If we divide all parallelograms into
two triangles with diagonals that have the same direction, we get a tiling of the plane with congruent triangles
(Figure \ref{sl.skl.3.9.3a.pic}). The triangle (basic cell) can be
arbitrary, because two such (congruent) triangles can always be connected by a common
side into a parallelogram and thus get a tiling with
parallelograms. Tiling with arbitrary congruent triangles is
a generalization of the regular tiling $(3,6)$ with regular triangles.


%\vspace*{-1mm}

As special cases of tiling with parallelograms, we get tiling with
rectangles and tiling with rhombuses (Figure \ref{sl.skl.3.9.3bc.pic}).
We will prove an even more general
statement, which may not be so obvious. It is possible that
there is also a tiling with arbitrary congruent quadrilaterals.

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
 Let $ABCD$ be an arbitrary quadrilateral in
the plane with internal angles $\alpha$, $\beta$, $\gamma$ and $\delta$.
Points $O$ and $S$ are the centers of its sides $AB$ and $BC$. With central
reflections
 $\mathcal{S}_O$ and $\mathcal{S}_S$ (for the definition of central reflection
 see section \ref{odd6SredZrc})
 the  quadrilateral  $ABCD$ is mapped into quadrilateral
$BAC_1D_1$ and $A_2CBD_2$. Here $\angle ABD_1\cong\alpha$ and
$CBD_2\cong\gamma$, therefore $\angle D_1BD_2\cong\delta$. Because
$BD_1\cong AD$ and $BD_2\cong CD$, there exists a point $E$,  such
that quadrilaterals $D_1ED_2B$ and $ABCD$ are congruent. So around point
$B$ four quadrilaterals intersect, all of which are congruent to quadrilateral
$ABCD$. We can continue the process of tiling the plane, if
we use central symmetry with respect to the centers of sides
of newly formed quadrilaterals.
 \kdokaz

 Therefore there exist tilings of the plane with any triangle and any
  quadrilateral. It is clear that for any pentagon, hexagon,...
  this property does not hold.
For a regular hexagon there exists a regular tiling $(6,3)$. If in
the previous statement we put together two appropriate adjacent quadrilaterals,
we get a tiling of the plane with congruent hexagons, which are not necessarily
regular, but are always centrally symmetric.


 %_______________________________________________________________________________
 \poglavje{Sets of Points in a Plane. Sylvester's Problem}
 \label{odd3Silvester}

In this section we will investigate problems related to sets of points in the plane and the lines determined by these points. At the beginning we will consider some consequences of the first two groups of axioms (incidence and order). First we will define new concepts. Let $\mathfrak{T}$ be a set of $n$ ($n>2$) points in the plane. With $\mathcal{P}(\mathfrak{T})$ we denote the set of all lines, each of which goes through at least two points from the set $\mathfrak{T}$ (Figure \ref{sl.skl.3.10.1.pic}). Because the set $\mathfrak{T}$ contains at least two points, from the axioms of incidence it follows that the set $\mathcal{P}(\mathfrak{T})$ is not empty. The question arises, how many lines are in the set $\mathcal{P}(\mathfrak{T})$.

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

\textbf{\textit{Proof.}} Through each of the $n$ points from the set $\mathfrak{T}$ there are exactly $n -1$ lines from the set $\mathcal{P}(\mathfrak{T})$. Because we count each line in this way twice (Figure \ref{sl.skl.3.10.2.pic}), we have to divide by 2. So there are exactly $\frac{n(n-1)}{2}$ lines in the set $\mathcal{P}(\mathfrak{T})$.
 \kdokaz

The previous statement can also be solved in the following way: through the first point there are $n -1$ lines, through the second point $n - 2$ lines (one less, because the line determined by these two points is not counted twice), $n - 3$ lines through the third point and so on until one line through the penultimate point. This is a total of $(n -1) + (n - 2) +\cdots+1$ lines. Of course, this is again equal to $\frac{n(n-1)}{2}$. If we take $n-1= k$, we get the known formula for the sum of the first $k$ natural numbers:
 $$1+ 2+ \cdots + k=\frac{k(k+1)}{2}.$$

 From the previous statement we can derive the formula for the number of diagonals of an arbitrary $n$-gon.



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

\textbf{\textit{Proof.}} We mark with $\mathfrak{O}$ the set of all vertices of an arbitrary $n$-gon.
  The number of diagonals is equal to the number of all lines
from the set $\mathcal{P}(\mathfrak{O})$ (statement \ref{stevPremic})
decreased by the number of its sides (Figure
\ref{sl.skl.3.10.3.pic}). Therefore:
 $$D_n=\frac{n(n- 1)}{2}-n=\frac{n^2-3n}{2}=\frac{n(n-3)}{2},$$ which was to be proven. \kdokaz

We mention that the formula for the number of diagonals of an $n$-gon could also be derived directly - with a similar treatment as in the proof of statement \ref{stevPremic}. From each of the $n$ vertices of an $n$-gon we can draw $n - 3$ diagonals. In this way we count each diagonal twice, so we have to divide by 2 and we get the previous formula.

Statement \ref{stevPremic} referred to the number of lines determined by a set of points in a plane that are in such a position that no three of them are collinear. In the next example we will check what happens if we add new conditions.

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

 Without the additional condition, there would be $\frac{n(n -1)}{2}$ lines in the set $\mathcal{P}(\mathfrak{T})$
  (statement \ref{stevPremic}).
  The additional condition in the problem reduces this
number by one less than the number of lines determined
by the set of $m$ points in general position. This is because otherwise
these lines would be counted multiple times. So the number of lines in the set
$\mathcal{P}(\mathfrak{T})$ is equal to:
$$\frac{(n-1)}{2}-\frac{(m -1)}{2}+1.$$
 \kdokaz

The next simple example will be an introduction to the very interesting problem of the relationship
between the set of points $\mathfrak{T}$ and the set of all lines
$\mathcal{P}(\mathfrak{T})$, which this set of points determines.


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

\textbf{\textit{Proof.}} One of the possibilities is the following. Let $ABCD$
be an arbitrary rectangle, $P$ and $Q$ be the centers of sides $AB$ and $CD$, $S$
be the intersection of the diagonals, $K$ be the intersection of lines $AP$ and $DQ$, and $L$
be the intersection of lines $BP$ and $CQ$ (Figure \ref{sl.skl.3.10.5.pic}). Because
the rectangle $ABCD$ is a rectangle, the points $P$, $Q$ and $S$  are collinear. So are
the points $K$, $L$ and $S$ (points $K$ and $L$ are the centers of rectangles
$AQPD$ and $QBCP$). So we have nine points $A$, $B$, $C$, $D$, $P$,
$Q$, $S$, $K$ and $L$, of which three lie on each of the ten lines $AB$,
$CD$, $PQ$, $KL$, $AC$, $BD$,
$PA$, $PB$, $QC$ and $QD$.
 \kdokaz

 If in the previous example we denote the set of nine points with $\mathfrak{T}$, we see that the set of ten lines is not the set $\mathcal{P}(\mathfrak{T})$.
  In the set $\mathcal{P}(\mathfrak{T})$ we would have  sixteen
  lines - our ten and also the additional lines $AD$, $BC$ $DL$, $AL$, $CK$ and $BK$.
  But each of these six lines contains
only two points. So the condition that they contain
exactly three points of the initial set is not fulfilled. It is now logical to ask
the following question: Is it possible in a plane to set a finite
set of non-collinear points $\mathfrak{T}$ so that each line from the set
$\mathcal{P}(\mathfrak{T})$ contains exactly three points from the set
$\mathfrak{T}$? It is clear that it is possible if we require
that each line from $\mathcal{P}(\mathfrak{T})$ contains exactly two
points from $\mathfrak{T}$. The most simple example for this are the vertices
of a triangle and its altitudes, or any set of points from
the statement \ref{stevPremic}. The aforementioned problem for three points is not so
simple, and we will find the answer in the continuation. We mention that
the answer is negative. Even more - the answer is negative even if we require that each line from $\mathcal{P}(\mathfrak{T})$ contains
at least three points from  $\mathfrak{T}$. First, we prove one lemma
(an auxiliary statement).

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

\textbf{\textit{Proof.}} We assume the opposite. Let the line $p_0$
contain at least three different points $A$, $B$ and $C$ from the set
$\mathfrak{T}$ (Figure \ref{sl.skl.3.10.6.pic}). We mark with $T'_0$ the orthogonal projection of the point $T_0$
on the line $p_0$. If the point $T'_0$ differs from the points $A$, $B$ and
$C$, then at least two of these three points (let it be $B$ and $C$) are on the line $p_0$ on the same
side of the point $T'_0$. Without loss of generality, let
$\mathcal{B}(T'_0,B,C)$. Because $T_0,C \in \mathfrak{T}$, then the line
$q= CT_0$  ($q \neq p_0$, because $T_0\notin p_0$) belongs to the set
$\mathcal{P}$. Let $B'$ be the orthogonal projection of the point  $B$ on
the line $q$. It is not difficult to prove that in this case it holds:
 $$d(B,q)=|BB'|<T_0T'_0=d(T_0,p_0).$$
 The last relation is
in contradiction with the assumption, therefore the line $p_0$ contains exactly two
points.

If  $T_0$ lies on one of the points $A$, $B$ or $C$, the proof
 is similar.
 \kdokaz

 Now we will prove the predicted statement.

\bizrek
Let $\mathfrak{T}$ be a finite set of points in the plane which do not all lie on the same line.
Then there is a line that contains exactly two points from the set
$\mathfrak{T}$
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
Let $\mathcal{P}=\mathcal{P}(\mathfrak{T})$. Because the set
$\mathfrak{T}$ is finite, the set $\mathcal{P}$ is also finite, and then
the set of all distances (Figure \ref{sl.skl.3.10.7.pic}) is finite:
$$\mathcal{D} = \{d(T,p);\hspace*{1mm}
T\in \mathfrak{T},\hspace*{1mm} p\in \mathcal{P},\hspace*{1mm} T\notin p\}.$$
 Because $\mathcal{D}$ is a finite set of positive real numbers, it has its
minimum element $d(T_0,p_0)$ (no distance from
$\mathcal{D}$ is smaller), which is achieved for some point $T_0\in
\mathfrak{T}$ and some line $p_0\in \mathcal{P}$. From the definition
of the set $\mathcal{D}$ it follows that $T_0\notin p_0$. By the previous lemma
\ref{SylvesterLema} there are exactly two points from the set
$\mathfrak{T}$ on the line $p_0$.
 \kdokaz

 We will finish this section with two interesting examples.



            \bizrek
            Let $\mathfrak{T}$ be a finite set of points,
            such that distances between two points of this set are all different.
            If we connect each point with a line segment to its nearest point, then none of the points will be
            directly connected to more than five points from this set\footnote{Polish mathematician, astronomer and physicist
              \index{Steinhaus, H.}\textit{H. Steinhaus} (1887--1972)
              wrote this problem in the form:
              ‘‘Every city in the map of Europe is connected... ’’}.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skl.3.10.8.pic}
\caption{} \label{sl.skl.3.10.8.pic}
\end{figure}

\textbf{\textit{Proof.}}
First, we determine that two arbitrary points $X$ and $Y$ can be connected
in one of three different
ways (Figure \ref{sl.skl.3.10.8.pic}):

 \textit{1)} the point $X$ is the nearest point to $Y$, but not vice versa;

 \textit{2)} the
point $Y$ is the nearest point to $X$, but not vice versa;

\textit{3)} the point $X$ is the nearest point to $Y$ and vice versa - the point $Y$
is the nearest point to $X$.

Every point has only one point closest to it, but that point can be connected to multiple points, which are closest to it. It needs to be proven that there are no more than five such points. We assume the opposite. Let $P$ be a point of the given set $\mathfrak{T}$ and is connected to at least six points $A$, $B$, $C$, $D$, $E$, and $F$ by distance. Without loss of generality, we can assume that they are arranged (or we can label them) so that $ABCDEF$ is a hexagon (Figure \ref{sl.skl.3.10.8.pic}). One of the points $A$, $B$, $C$, $D$, $E$, or $F$ is closest to the point $P$, let it be the point $A$. So it holds: $PA < PB, PC, PD, PE, PF$. Because the points $B$, $C$, $D$, $E$, and $F$ are also connected to the point $P$, it means that the point $P$ is closest to each of them (and not the other way around). Based on this, first $BA > BP > PA$, so $\angle APB$ is the largest angle in the triangle $APB$ and is therefore larger than $60^0$. Similarly, $CB > BP,BC$, so $\angle BPC > 60^0$. The same would hold for the angles $CPD$, $DPE$, $EPF$, and $EPA$, but that is not possible, because their sum is always equal to or even greater than $360^0$, regardless of whether $P$ is an inner or outer point of the hexagon $ABCDEF$. Therefore, the point $P$ is connected to no more than five points.
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

\textbf{\textit{Solution.}}  We will describe the process of designing such
$n$ lines (Figure \ref{sl.skl.3.10.9.pic}). If $n = 1$, or
if there is only one line, the plane is divided into two areas. Two
lines, if they are not parallel, divide the plane into four areas. If
we add a third line $p_3$, which is not parallel to them and does not go through
their common point, it intersects the initial two lines in two points. These
two points divide the line $p_3$ into three parts, each of which is in
one of the three previous four areas of the plane. So with line
$p_3$ we get three more parts of the plane, a total of seven. We continue the process. If $n -1$ lines divide the plane into $k$ parts, by
adding the $n$-th line $p_n$ (which is not parallel to any of the previous $n -1$ lines and does not contain any of their intersections),
we first get $n -1$ intersections on that line, then $n$ of its
parts or $n$ new areas of the given plane. So the maximum possible
number of areas for $n$ lines is equal to:
\begin{eqnarray*}
2+2+3+\cdots+n&=&1+1+2+3+\cdots+n=\\
&=&1+\frac{n(n+1)}{2}=\\&=&\frac{n^2+n+2}{2}.
\end{eqnarray*}
A formal proof of this fact could be derived by mathematical induction.
 \kdokaz


 %_______________________________________________________________________________
 \poglavje{Helly's Theorem}
\label{odd3Helly}

The next important statement is a consequence of only the first two groups of axioms
or the axioms of incidence and the axioms of order. We will also use it
in tasks related to consistency.

\bizrek \label{Helly}
            Let $\Phi_1$, $\Phi_2$, ... , $\Phi_n$ ($n \geq 4$) be convex sets in the plane.
            If every three of these sets have a common point, then all $n$ sets have a common point
            \index{izrek!Hellyjev}(Helly's theorem\footnote{Austrian
            mathematician  \index{Helly, E.} \textit{E. Helly} (1884--1943)
             discovered this statement in the general case of $n$-dimensional space $\mathbb{E}^n$
              in 1913, but published it only in 1923. Alternative proofs were
              meanwhile given by Austrian mathematician \index{Radon, J. K. A.}
              \textit{J. K. A. Radon} (1887-–1956) in 1921 and
              Hungarian mathematician \index{Kőnig, D.}
              \textit{D. Kőnig} (1884–-1944) in 1922.}).
            \eizrek

\begin{figure}[!htb]
\centering
\hspace*{10mm}
\input{sl.skl.3.11.1.pic}
\caption{} \label{sl.skl.3.11.1.pic}
\end{figure}

\textbf{\textit{Proof.}} We will prove this by induction on $n$.

\textit{(A)} Let $n = 4$ and (Figure
\ref{sl.skl.3.11.1.pic}):
\begin{itemize}
  \item $P_4\in \Phi_1 \cap \Phi_2 \cap \Phi_3$,
  \item $P_3\in \Phi_1 \cap \Phi_2 \cap \Phi_4$,
  \item $P_2\in \Phi_1 \cap \Phi_3 \cap \Phi_4$,
  \item $P_1\in \Phi_2 \cap \Phi_3 \cap \Phi_4$.
\end{itemize}
We will prove that there exists a point that lies in each of the figures $\Phi_1$,
$\Phi_2$, $\Phi_3$ and $\Phi_4$. Based on the mutual position
of points $P_1$, $P_2$, $P_3$ and $P_4$ we will consider only two most
general cases (the proof in the other cases
is similar).

\textit{1)} A quadrilateral, determined by points $P_1$, $P_2$, $P_3$ and
$P_4$, is non-convex. In this case, one of the points $P_1$, $P_2$,
$P_3$ and $P_4$ is an inner point of the triangle determined by the remaining
three points. Without loss of generality, let $P_4$ be the inner point
of the triangle $P_1P_2P_3$. The vertices of this triangle lie in the shape
$\Phi_4$. Because $\Phi_4$ is a convex shape, all sides and inner points of the triangle $P_1P_2P_3$, as well as the point $P_4$, lie in it. In this case, the point $P_4$ is the common point of shapes
$\Phi_1$, $\Phi_2$, $\Phi_3$ and $\Phi_4$.

\textit{2)} The quadrilateral determined by points $P_1$, $P_2$, $P_3$ and $P_4$ is convex. Without loss of generality, let its diagonals be $P_1P_2$ and $P_3P_4$. Because the quadrilateral is convex, its diagonals intersect in a point $S$. Given shapes are convex, so from $P_1, P_2\in \Phi_3,\Phi_4$ it follows that the diagonal $P_1P_2$ lies entirely in shapes $\Phi_3$ and $\Phi_4$. Analogously, from $P_3, P_4\in \Phi_1,\Phi_2$ it follows that the diagonal $P_3P_4$ lies entirely in shapes $\Phi_1$ and $\Phi_2$. The point $S$, which lies on both diagonals
$P_1P_2$ and $P_3P_4$, lies in all four shapes $\Phi_1$, $\Phi_2$,
$\Phi_3$ and $\Phi_4$.

With this we have proven that the statement is true for $n=4$.

\textit{(B)} Let's now assume that the statement is true for $n = k$ ($k\in
\mathbb{N}$ and $k>4$).
 We shall prove that the statement is also true for
$n = k +1$. Let $\Phi_1$, $\Phi_2$, $\ldots$ , $\Phi_{k-1}$,
$\Phi_k$ and $\Phi_{k+1}$ be such figures that every triplet of these figures
has at least one common point. Let $\Phi'=\Phi_k\cap\Phi_{k+1}$. We shall first prove that every triplet of figures $\Phi_1$, $\Phi_2$ ,$\ldots$,
$\Phi_{k-1}$, $\Phi'$ has a common point. For triplets of figures from
$\Phi_1$, $\Phi_2$, $\ldots$, $\Phi_{k-1}$ this is already fulfilled according to the assumption. Without loss of generality, it is enough to prove that
figures $\Phi_1$, $\Phi_2$ and $\Phi'=\Phi_k\cap\Phi_{k+1}$
have a common point. This is true  (based on the proven example for $n = 4$),
because every triplet of figures from $\Phi_1$, $\Phi_2$,  $\Phi_k$ and
$\Phi_{k+1}$  has a common point. From the induction assumption
(for $n=k$) it follows that figures $\Phi_1$, $\Phi_2$, $\ldots$,
$\Phi_{k-1}$, $\Phi'$  have a common point, which at the same time lies in
each of figures $\Phi_1$, $\Phi_2$, $\ldots$,  $\Phi_{k-1}$,
$\Phi_k$, $\Phi_{k+1}$.
 \kdokaz

In the continuation we shall consider some consequences of Helly's theorem.



            \bzgled
           Let $\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$
            ($n > 3$) be half-planes covering a plane $\alpha$.
            Prove that there are three of these half-planes that also cover the plane $\alpha$.
            \ezgled

\textbf{\textit{Proof.}} Let $\beta_1$, $\beta_2$, $\cdots$,
$\beta_n$ be open half-planes, which are determined by the half-planes
$\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$ as complementary
half-planes with respect to the plane $\alpha$ or
$\beta_k=\alpha\setminus\alpha_k$, $k\in\{1,2,\ldots,n\}$.
For every point $X$ of the plane $\alpha$ and every
$k\in\{1,2,\ldots,n\}$ the equivalence holds:
 $$X\in \alpha_k \Leftrightarrow X\notin \beta_k.$$
Assume the contrary, that none of the three half-planes $\alpha_1$,
$\alpha_2$, $\cdots$, $\alpha_n$ covers the plane $\alpha$. This
means that for every triple of them there is a point in the plane $\alpha$,
which does not lie on any of them, or for every triple of the half-planes
$\beta_1$, $\beta_2$, $\cdots$, $\beta_n$ there is a point of the plane
$\alpha$, which lies on each of them. Because the half-planes are convex
shapes, from Helly's theorem \ref{Helly} it follows that there is a point
$X$, which lies  on each of the half-planes $\beta_1$, $\beta_2$, $\cdots$,
$\beta_n$. This point therefore lies in  the plane $\alpha$, but does not lie in
any of the half-planes $\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$,
which is in contradiction with the basic assumption that the half-planes $\alpha_1$,
$\alpha_2$, $\cdots$, $\alpha_n$ cover the plane $\alpha$.
 Therefore, there is at least one triple of the
half-planes $\alpha_1$, $\alpha_2$, $\cdots$, $\alpha_n$, which
covers the plane $\alpha$.
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

Let $A_1$, $A_2$,$\ldots$, $A_n$ be points with given properties. With
$\mathcal{K}_i$ ($i\in\{1,2,\ldots,n\}$) we denote circles with centers $A_i$ and with
radius $r$. Let $A_p$, $A_q$ and $A_l$ be any points from
the set $\{A_1, A_2,\ldots, A_n\}$. By assumption, there exists a circle with
radius $r$, which contains these three points. We denote the center of this circle
with $O$. From this it follows that $|OA_p|, |OA_q|, |OA_l|\leq r$, which means that
point $O$ lies in each of the circles $\mathcal{K}_p$, $\mathcal{K}_q$ and $\mathcal{K}_l$. Therefore,
each three of the circles $\mathcal{K}_1$, $\mathcal{K}_2$,$\ldots$, $\mathcal{K}_n$ have at least one
common point. Because the circles are convex figures (statement \ref{KrogKonv}), by
Helly's theorem there exists a point $S$, which lies in each of the circles
$\mathcal{K}_1$, $\mathcal{K}_2$,$\ldots$, $\mathcal{K}_n$. From this it follows that $\mathcal{K}(S, r)$ is the desired
circle, since $|SA_1|, |SA_2|,\ldots |SA_n|\leq r$.
 \kdokaz

 An interesting consequence of the last statement \ref{lemaJung} will be given in section
 \ref{odd7Pitagora} (statement \ref{Jung}).

%________________________________________________________________________________
\naloge{Exercises}

\begin{enumerate}

 \item Let $S$ be a point, which lies in the angle $pOq$, and to point $A$ and $B$ the orthogonal projection of
 point $S$ on the sides $p$ and $q$ of this
angle. Prove that $SA\cong SB$ if and only when the line
$OS$ is the angle bisector of the angle $pOq$.

\item Prove that the sum of the diagonals of a convex quadrilateral is greater than
the sum of its opposite sides.

  \item Prove that in every triangle
  there is at most one side shorter than the corresponding altitude.

  \item Let $AA_1$ be the altitude of triangle $ABC$. Prove
   that of the two angles, which altitude $AA_1$ determines with
sides $AB$ and $AC$, the larger one is the one, which altitude $AA_1$ determines with
the shorter side.

  \item Let $BB_1$ and $CC_1$ be the altitudes of triangle $ABC$ and
  $AB<AC$.
  Prove that $BB_1<CC_1$.

\item Let $a$, $b$ and $c$ be the sides, $t_a$, $t_b$ and $t_c$
   the corresponding centroids, and $s$ the semi-perimeter of any triangle.
Prove that:
 \begin{enumerate}
  \item $s <  t_a  + t_b +  t_c  < 2s$;
  \item $t_a + t_b + t_c  >  \frac{3}{4}(a + b + c)$.
 \end{enumerate}

\item Let $p$ be a line that is parallel to a circle $k$. Prove that
all points of this circle are on the same side of the line $p$.

\item If the circle $k$ lies in a convex figure $\Phi$, then the
circle determined by this circle also lies in this figure. Prove it.

\item Let $p$ and $q$ be two different tangents to the circle $k$ that
touch it in points $P$ and $Q$. Prove the equivalence: $p \parallel q$
exactly when $AB$ is the diameter of the circle $k$.

\item If $AB$ is the chord of the circle $k$, then the intersection of
the line $AB$ and the circle determined by the circle $k$ is equal to
this chord. Prove it.

\item Let $S'$ be the orthogonal projection of the center $S$ of the
circle $k$ onto the line $p$. Prove that $S'$ is an external point of
this circle exactly when the line $p$ does not intersect the circle.

\item Let $V$ be the altitude of the triangle $ABC$, for which $CV \cong
AB$. Determine the size of the angle $ACB$.

\item Let $CC'$ be the altitude of the right triangle $ABC$ ($\angle
ACB = 90^0$). If $O$ and $S$ are the centers of the inscribed circles
of the triangles $ACC'$ and $BCC'$, then the altitude of the internal
angle $ACB$ is perpendicular to the line $OS$. Prove it.

\item Let $ABC$ be a triangle in which $\angle ABC = 15^0$ and $\angle
ACB = 30^0$. Let $D$ be such a point of the side $BC$ that $\angle BAD
= 90^0$. Prove that $BD = 2AC$.

\item Prove that there exists a pentagon that can be covered with
such pentagons that are congruent to it.

\item Prove that there exists a decagon that can be covered with
such decagons that are congruent to it.

\item In a plane, each point is painted red or black. Prove that
there exists a right triangle that has all its vertices the same
color.

\item Let $l_1,l_2,\ldots, l_n$ ($n > 3$) be arcs, which all lie on the same
circle. The central angle of each arc is at most $180^0$.
 Prove that there exists a point, which lies on each arc,
 if every three arcs have at least one common point.

%drugi del

\item
Let $p$ and $q$ be rectangles, which intersect in the point $A$. If
$B, B'\in p$, $C, C'\in q$, $AB\cong AC'$, $AB'\cong AC$,
$\mathcal{B}(B,A,B')$ and $\mathcal{B}(C,A,C')$, then
the rectangle on the line $BC$ through the point $A$ goes through the center
of the line $B'C'$. Prove.

\item
Prove that the altitudes of an inner angle of a rectangle, which is not
a square, intersect in points, which are the vertices of a square.

\item
 Prove that the altitudes of an inner angle of a parallelogram, which is not
a rhombus, intersect in points, which are the vertices of a rectangle. Prove also that the diagonals
of this rectangle are parallel to the sides of the parallelogram and are
equal to the difference of the adjacent sides of this parallelogram.

\item
Prove that the altitudes of two sides of a triangle
are perpendicular to each other.

\item Let $B'$ and $C'$ be the points of intersection of the altitudes from the vertices $B$ and $C$ of the triangle
$ABC$. Prove the equivalence $AB\cong AC \Leftrightarrow BB'\cong
CC'$.

\item Prove that a triangle is right,
if the center of the circle drawn through the triangle and its altitude point coincide.
Is a similar statement true for any two characteristic
points of this triangle?

\item Prove that a right triangle $ABC$ and a right triangle $A'B'C'$ are congruent
exactly when they have congruent altitudes $CD$ and $C'D'$, sides $AB$ and
$A'B'$ and angle $ACD$ and $A'C'D'$.

\item If $ABCD$ is a rectangle and $AQB$ and $APD$ are right triangles with the same orientation, then the line $PQ$
is congruent with the diagonal of this rectangle. Prove.

\item Let $BB'$ and $CC'$ be the altitudes of the triangle $ABC$ ($AC>AB$) and
 $D$ is such a point on the line segment $AB$, that $AD\cong AC$. The point
$E$ is the intersection of the line $BB'$ with the line, which goes through the point $D$ and is
parallel to the line $AC$. Prove that $BE=CC'-BB'$.

\item Let $ABCD$ be a convex quadrilateral, for which it holds that
 $AB\cong BC\cong CD$ and $AC\perp BD$. Prove that $ABCD$
 is a rhombus.

\item Let $BC$ be the base of an isosceles triangle $ABC$. If $K$ and
$L$ are such points, that $\mathcal{B}(A,K,B)$, $\mathcal{B}(A,C,L)$ and $KB\cong LC$, then
the center of the line $KL$ lies on the base $BC$. Prove.

\item Let $S$ be the center of the triangle $ABC$ of an inscribed circle.
A line, which goes through the point $S$ and is parallel to the side $BC$
of this triangle, intersects the sides $AB$ and $AC$ in succession in the points
$M$ and $N$. Prove that $BM+NC=NM$.

\item Let $ABCDEFG$ be a convex heptagon. Calculate the sum
of the convex angles, which are determined by the broken line $ACEGBDFA$.

\item Prove that the centers of the sides and the vertex of an altitude of an arbitrary triangle,
in which no two sides are congruent, are the vertices
of an isosceles trapezoid.

 \item Let $ABC$ be a right triangle with a right angle at the vertex $C$.
The points $E$ and $F$ shall be the intersections of the internal angle bisectors at
the vertices $A$ and $B$ with the opposite sides,  $K$ and $L$ shall
be the orthogonal projections of the points $E$ and $F$ on the hypotenuse of this
triangle. Prove that $\angle LCK=45^0$.


\item Let $M$ be the center of the side $CD$ of a square $ABCD$ and $P$ such a point
 on the diagonal $AC$, for which it holds that $3AP=PC$. Prove that $\angle BPM$
is a right angle.

 \item Let $P$, $Q$ and $R$ be the centers of the sides $AB$, $BC$ and $CD$
  of a parallelogram $ABCD$. The lines $DP$ and $BR$ shall intersect the line
$AQ$ in the points $K$ and $L$. Prove that $KL= \frac{2}{5} AQ$.

 \item  Let $D$ be the center of the hypotenuse $AB$ of a right triangle $ABC$ ($AC>BC$).
The points $E$ and $F$ shall be the intersections of the angle trisectors of
the sides $CA$ and $CB$ with a line, which goes through $D$ and is orthogonal
to the line $CD$. The point $M$ shall be the center of the line $EF$. Prove that
$CM\perp AB$.

\item Let $A_1$ and $C_1$ be the centers of sides $BC$ and $AB$ of triangle $ABC$.
 The internal angle bisector at point $A$ intersects the line
$A_1C_1$ at point $P$. Prove that $\angle APB$ is a right angle.

 \item Let $P$ and $Q$ be points on sides $BC$ and $CD$ of square $ABCD$,
  such that the line $PA$ is the angle bisector of angle $BPQ$. Determine the size of the angle
  $PAQ$.

\item Prove that the center of the circumscribed circle lies closest to the longest side
of the triangle.

 \item Prove that the center of the inscribed circle is closest to the vertex of
the largest internal angle of the triangle.

\item Let $ABCD$ be a convex quadrilateral. Find a point $P$, such that
the sum $AP+BP+CP+DP$ is minimal.

 \item The diagonals $AC$ and $BD$ of the trapezoid $ABCD$ with the base $AB$
intersect at point $O$ and $\angle AOB=60^0$. Points $P$, $Q$
and $R$ are in order the centers of the lines $OA$, $OD$ and $BC$. Prove that $PQR$ is a right triangle.

\item Let $P$ be an arbitrary internal point of triangle $ABC$, for which
 $\angle PBA\cong \angle PCA$. Points $M$ and $L$ are the orthogonal
projections of point $P$ on sides $AB$ and $AC$, point $N$ is
the center of side $BC$. Prove that $NM\cong
NL$\footnote{Predlog za MMO 1982 (SL 9.)).}.

\item Let $AD$ be the internal angle bisector at point $A$ ($D\in BC$) of triangle
$ABC$ and $E$ a point on side $AB$, such that $\angle
BDE\cong\angle BAC$. Prove that $DE\cong DC$.

\item Let $O$ be the center of square $ABCD$ and $P$, $Q$ and $R$ points,
 which divide its perimeter into three equal parts. Prove that the minimum of the sum $|OP|+|OQ|+|OR|$ is achieved, when one of these points
is the center of a side of the square.

\item There is a given finite number of lines that divide the plane into areas.
Prove that the plane can be colored with two colors, so that each area is colored with one color, and adjacent areas are always colored with different colors.


\item Draw a triangle $ABC$, if the following data are given (see labels in section \ref{odd3Stirik}):

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

 \item Draw an isosceles triangle $ABC$, if the following are given:
        \begin{enumerate}
        \item the base and the sum of the leg and the height on the base,
        \item the circumference and the height on the base,
        \item both heights,
        \item the angle at the base and the segment of its altitude,
        \item the leg and the point of intersection of the corresponding altitude on it,
        \item the leg and the corresponding altitude.
        \end{enumerate}

 \item Draw a right triangle $ABC$ with a right angle at point $C$, if the following data are given:

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

 \item Draw a rectangle $ABCD$, if given:
        \begin{enumerate}
        \item the diagonal and one side,
        \item the diagonal and the perimeter,
        \item one side and the angle between the diagonals,
        \item the perimeter and the angle between the diagonals.
        \end{enumerate}

 \item Draw a rhombus $ABCD$, if given:
        \begin{enumerate}
        \item a side and the sum of the diagonals,
        \item a side and the difference of the diagonals,
        \item one angle and the sum of the diagonals,
        \item one angle and the difference of the diagonals.
        \end{enumerate}

 \item Draw a parallelogram $ABCD$, if given:
        \begin{enumerate}
        \item one side and the diagonals,
        \item one side and the altitude,
        \item one diagonal and the altitude,
        \item side $AB$, the angle at point $A$ and the sum $BC+AC$.
        \end{enumerate}

 \item Draw a trapezoid $ABCD$, if given:
        \begin{enumerate}
        \item the bases, the leg and the smaller angle that is not adjacent to this leg,
        \item the bases and the diagonals,
        \item the bases and the angle at the longer base,
        \item the sum of the bases, the altitude and the angle at the longer base.
        \end{enumerate}

 \item Draw a deltoid $ABCD$, if given: the diagonal $AC$, which lies on the slanted side of the deltoid, $\angle CAD$ and the sum $AD+DC$."

\item Draw a quadrilateral $ABCD$, if it is given:
        \begin{enumerate}
        \item four sides and one angle,
        \item four sides and an angle between the opposite sides,
        \item three sides and an angle at the fourth side,
        \item the centers of three sides and a distance that is consistent and parallel to the fourth side.
        \end{enumerate}


\end{enumerate}



%%% Do tu pregledala tudi Ana.

% DEL 4 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
% SKLADNOST TRIKOTNIKOV IN KROŽNICA
%________________________________________________________________________________

  \del{Congruence and Circle} \label{pogSKK}


We have already looked at some of the properties of circles in the previous two chapters - certain properties of the radius, diameter, cord, the relationship between the circle and the line, and the properties of the tangent to the circle. We saw that for every triangle there is an inscribed and circumscribed circle. We proved that for regular polygons and some quadrilaterals (rectangle, square) there is a circumscribed circle, and for some there is also an inscribed circle. In this chapter we will look further into the properties of the circle that are a result of the congruence of triangles.

%________________________________________________________________________________
 \poglavje{Two Circles} \label{odd4DveKroz}

 We will carry out a similar analysis of the position of the circles and lines that we did in section \ref{odd3KrozPrem}, but this time with two circles in the same plane. We will assume that the two circles we are dealing with are in the same plane from now on.

 First, let's define some terms that relate to two circles. The line that goes through the centers of two circles is the
 \index{centrala dveh krožnic}\pojem{centrala} of those two circles.
 The distance between the centers of two circles is called the
 \index{središčna razdalja dveh krožnic}
  \pojem{središčna razdalja dveh krožnic}
 (Figure \ref{sl.skk.4.1.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.1.pic}
\caption{} \label{sl.skk.4.1.1.pic}
\end{figure}

Circles in the same plane with the same
center (their central distance is equal to $0$)
we call
\index{circles!concentric}
 \pojem{concentric circles}
 (Figure \ref{sl.skk.4.1.1.pic}). If concentric circles have at least
 one common point, the circles are identical (coincide). If $X$ is a common point
 of concentric circles $k_1(S,r_1)$ and $k_2(S,r_2)$, it holds
 $|SX|=r_1=r_2$ or $r_1=r_2$, which means that the circles
 are identical. Concentric circles are either identical or have
 no common points. Similarly to the circle and the line, here we raise the question of how many common points different circles can have and what is their mutual position. We will begin
 with the following statement.


            \bizrek
            Two different circles lying in the same plane
            have at most two common points.
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.2.pic}
\caption{} \label{sl.skk.4.1.2.pic}
\end{figure}

\textbf{\textit{Proof.}} We assume the opposite. Let $A$, $B$
and $C$ be three different common points of two circles $k(O,r_1)$ and
$l(S,r_2)$ (Figure \ref{sl.skk.4.1.2.pic}). These three points are not
collinear, which would mean that the line $AB$ intersects the circle (e.g.
$k$) in three different points, which according to izrek \ref{KroznPremPresek} is not
possible. But if  $A$, $B$ and $C$ are non-collinear points, they determine
the triangle $ABC$, which according to izrek \ref{SredOcrtaneKrozn} means that $O=S$, or both points are
located in the intersection of the perpendiculars of this
triangle. The radii are also equal, because $r_1=|OA|=|SA|=r_2$, so
the circles  $k(O,r_1)$ and $l(S,r_2)$ are identical - both represent
the circle circumscribed around the triangle $ABC$.
 \kdokaz

So, two different circles in the same plane can have two common points, one common point, or no common points. In the first case, we say that the \index{circles!intersect} \pojem{circles intersect}, in the second case the \index{circles!touch} \pojem{circles touch} in their \index{touching point!of two circles} \pojem{touching point}, and in the third case they are \index{circles!are non-intersecting}\pojem{non-intersecting circles} (Figure \ref{sl.skk.4.1.3.pic}).


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.3.pic}
\caption{} \label{sl.skk.4.1.3.pic}
\end{figure}


If the circles do not intersect, then the interior of at least one of these two circles is either in the interior or in the exterior of the other circle. This is a consequence of Theorem \ref{DedPoslKrozKroz}.

The line that is determined by the intersection
 of two circles that
intersect is called the \pojem{secant, which is the tangent of their common chord}. In connection with this, we prove the following theorem.



            \bizrek \label{KroznPresABpravokOS}
            If two circles intersect at two points $A$ and $B$,
            then the line containing the centres of the two circles is perpendicular to the line $AB$.
             \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.4.pic}
\caption{} \label{sl.skk.4.1.4.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $A$ and $B$ be the intersection points of the circles $k_1(S_1,r_1)$ and  $k_2(S_2,r_2)$ (Figure \ref{sl.skk.4.1.4.pic}).
 Because $S_1A\cong S_1B\cong r_1$ and $S_2A\cong S_2B\cong r_2$,
 the line $S_1S_2$  is the perpendicular bisector of the line segment $AB$ (Theorem \ref{simetrala}),
 so $S_1S_2\perp
 AB$.
  \kdokaz


 We will prove that the circles that touch have a common tangent at
their touching point.



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

(\textit{i}) We assume that the points $S_1$, $S_2$ and $T$ are not
collinear. The line $S_1S_2$ divides the plane in which the circles
lie, into two half-planes. The half-plane that contains the point $T$,
we denote by $\pi_1$, the other by $\pi_2$. From the statement \ref{izomEnaC'}
it follows that in the half-plane $\pi_2$ there exists (one and only one) point $T'$, for
which $S_1T'\cong S_1T$ and $S_2T'\cong ST_2$. This would mean that even the point $T'$, which is different from the point $T$, lies on the circles
$k_1$ and $k_2$, which is not possible. Therefore, the points $S_1$, $S_2$ and $T$
are collinear.

 (\textit{ii}) By the statement \ref{TangPogoj} the tangent
of the circle $k_1$ at the point $T$ is perpendicular to the radius $S_1T$. Similarly
the tangent of the circle $k_2$ at the same point $T$ is perpendicular to the radius $S_2T$. Because of (\textit{i}) the lines $S_1T$ and $S_2T$ coincide,
so do both perpendiculars or tangents.
 \kdokaz

By the statement \ref{tangKrozEnaStr} all points of the circle are on the same side
of each of its tangents - on the side where its center is. This
means that the circles $k_1$ and $k_2$ from the previous statement are either
 on the same side or on different sides of their common tangent. When $B(S_1,T,S_2)$, the circles are on different sides
of their common tangent and we say that the circles $k_1$
and $k_2$ \pojem{touch each other from the outside}. Otherwise the circles are on the same side
of this tangent and we say that they \pojem{touch each other from the inside}. In
the first case, the interior of one of these two circles is in the exterior of the other, in
the second case, however, it is in the interior of the other circle (Figure
\ref{sl.skk.4.1.6.pic}).

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.6.pic}
\caption{} \label{sl.skk.4.1.6.pic}
\end{figure}

When the circles $k_1(S_1,r_1)$ and $k_2(S_2,r_2)$ touch each other from the outside,
it follows from the previous statement that $|S_1S_2| = r_1 + r_2$.
If the circles touch each other from the inside, then $|S_1S_2| = |r_1 - r_2|$.
It is clear that the converse is also true. The condition $|S_1S_2| = r_1 +
r_2$ or $|S_1S_2| = |r_1 - r_2|$ is sufficient for the circles
to touch each other from the outside or from the inside. In a similar way, we obtain the other
criteria for the mutual position of two circles.

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


Now we will define some concepts that relate to two
circles.

\pojem{Kot med krožnicama}, which intersect, is the angle that is determined
by the tangents of these two circles at their common point. It is not difficult to prove
that this angle is not dependent on the choice of the common point, or that the angles between
the tangents in each of the two common points are consistent (Figure
\ref{sl.skk.4.1.8.pic}).

When the circles touch, we say that they determine the angle $0^0$.


\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.8.pic}
\caption{} \label{sl.skk.4.1.8.pic}
\end{figure}

The circles are \index{pravokotni!krožnici} \pojem{pravokotni}, if
they determine the angle $90^0$, or if their tangents in the common point
are perpendicular (Figure \ref{sl.skk.4.1.8.pic}).

A direct consequence of izrek \ref{TangPogoj} is the following condition
of pravokotnosti of two circles.



            \bizrek \label{pravokotniKroznici}
            Two circles are perpendicular if and only if
            the tangent of one of the circles at the points of intersection
            contains the centre of  another circle.
             \eizrek

In zgled \ref{tangKrozKonstr} we have determined how to draw
the tangents of a circle from its arbitrary external point. In izrek
\ref{tangSkupnaDotikKrozn} we have  proved that the circles, which touch,  have at least one common tangent. In the next example we will
construct \index{skupna tangenta}\pojem{common tangents} of two
circles in general position.

            \bzgled \label{tang2ehkroz}
            Construct a common tangent of two given circles
            lying in the same plane.
            \ezgled

\textbf{\textit{Solution.}} Let $k_1(S_1,r_1)$ and $k_2(S_2,r_2)$
($r_1\geq r_2$) be any two circles in the same plane and $t$ their
common tangent, which touches the circles $k_1$ and $k_2$ in
succession in the points $T_1$ and $T_2$.

We will consider two cases:

\textit{1)} First, let us assume that the points $T_1$ and $T_2$ are
on the same side of the central line $S_1S_2$ (Figure
\ref{sl.skk.4.1.9.pic}). We mark $S'_2=pr_{\perp S_1T_1}(S_2)$. By
\ref{TangPogoj} we have $\angle S_1T_1T_2\cong\angle
S_2T_2T_1=90^0$. This means that the quadrilateral $S_2T_2T_1S'_2$
is a rectangle, so $\angle S_2S'_2T_1=90^0$ and $|S'_2T_1|=|S_2T_2|=r_2$.
 Since by assumption $r_1\geq r_2$ and $|S_1T_1|=r_1$, we have
 $|S_1S'_2|=r_1-r_2$. We mark with $k$ the circle with center $S_1$ and
 radius $r_1-r_2$. The circle $k$ passes through the point $S'_2$.
 If $S_2$ is an external point of the circle $k$,
 from $\angle S_2S'_2T_1=90^0$
 it follows that the line $S_2S_2'$ is tangent
 to this circle.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.9.pic}
\caption{} \label{sl.skk.4.1.9.pic}
\end{figure}

 The previous analysis allows us to construct it. First, we plan
 the circle $k(S_1,r_1-r_2)$, then its tangent $S_1S'_2$ in
 the point of contact $S'_2$ (example \ref{tangKrozKonstr}), the point $T_1$ as
 the intersection of the segment $S'_2T_1$ and the circle $k_1$, the fourth vertex
 $T_2$ of the rectangle $T_1S'_2S_2T_2$ (because from the construction $\angle S_2S'_2T_1=90^0$) and finally the common tangent $t=T_1T_2$.

We will prove that $t$ is indeed the common tangent. Because by
construction $T_1\in k_1$ and $\angle S_1T_1T_2\cong
\angle S_2T_2T_1=90^0$, it is enough to prove that $T_2\in
k_2$. This follows from the fact that the quadrilateral $T_1S'_2S_2T_2$
is a rectangle or $|S_2T_2|=|S'_2T_1|=r_1-(r_1-r_2)=r_2$.

In addition to the planned tangent $t$, we also get the tangent $t_1$,
which is symmetrical to the tangent $t$ with respect to the center $S_1S_2$. For
the tangents $t$ and $t_1$, we say that they are \index{skupna
tangenta!zunanja}\pojem{external tangents}.

\textit{2)} If we assume that $T_1$ and $T_2$ are on different
banks of the center $S_1S_2$, we get two more t. i. \index{skupna tangenta!notranja}\pojem{internal tangents} in
certain cases, by the same procedure, only that we replace the circle $k(S_1,r_1-r_2)$ with the circle
$k'(S_1, r_1+r_2)$.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.1.10.pic}
\caption{} \label{sl.skk.4.1.10.pic}
\end{figure}

Let us also consider the number of solutions to the task (Figure
\ref{sl.skk.4.1.10.pic}). When the circles are non-intersecting and
none of them is inside the other, the circles have all four described
common tangents - two external and two internal tangents. If
the circles touch from the outside, the task has three solutions, because the internal
tangents overlap and we get a common tangent, which is mentioned in
the statement \ref{tangSkupnaDotikKrozn}. When the circles intersect,
we have only two solutions - two external tangents. When the circles touch from
the inside, there is only one common tangent (that from the statement
\ref{tangSkupnaDotikKrozn}). And finally, if the circles are non-intersecting
and one of them is inside the other, they don't have
common tangents.
\kdokaz

\bzgled
            Let $A$, $B$, $C$ and $D$ be points in the plane such that they do not all lie
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
 Let
$m$ and $n$ be the perpendicular lines of $AB$ and $CD$. We will consider two
cases (Figure \ref{sl.skk.4.1.1a.pic}):

 \textit{1)}
If the lines $m$ and $n$ intersect at point $O$, the desired circles
$k(O,OA)$ and $l(O,OC)$ are concentric and different (by assumption).

\textit{2)} If the lines $m$ and $n$ are parallel, the lines $AB$ and $CD$ are also
parallel (and different by assumption). Let $p$ be any parallel line of $AB$ and $CD$ such that $AB$ and $CD$
are on different sides of $p$. Let $M$ and $N$ be the intersections of $m$ and $n$ with $p$. If $M \neq N$, the desired circles are the circumscribed circles of the triangles $ABM$ and $CDN$ (by Theorem \ref{SredOcrtaneKrozn}), because they lie on different sides of the line $p$. If $M = N$ or $m = n$, the desired circles are concentric again $k(M,MA)$ and $l(M,MC)$.
 \kdokaz



%________________________________________________________________________________
 \poglavje{Center Angle and Circumferential Angle} \label{odd4SredObod}


 Let us first define the concepts of central and circumferential angle
  (Figure \ref{sl.skk.4.2.1a.pic}).

\pojem{Central angle}
  \index{angle!central}  of a circle $k(S,r)$ is any angle,
  that lies in the plane of this circle  and has its vertex in the point $S$.
   \pojem{Circumferential angle}
  \index{angle!circumferential} of this circle is any angle with its vertex
  on the circle $k$, and its legs contain two chords of
this circle. The intersection of the circle and its central or circumferential angle
is an arc, which we call the \pojem{arc corresponding} to this angle. In this
case, for the central or circumferential angle we say that the angle is \pojem{over this arc}.
 We know that any chord $PQ$ on the circle $k(S,r)$ determines two arcs.
 If we know
for which
of the two arcs it is, we sometimes for the angle over the corresponding arc $PQ$
say that the angle is \pojem{over the chord} $PQ$.

In a special case, when the chord is a diameter, the corresponding central angle
over this chord is equal to $180^0$. Tales's theorem for a circle (theorem
\ref{TalesovIzrKroz}) can be written in terms of circumferential angles in the
following way:



             \bizrek \label{TalesovIzrKroz2oblika}
            All inscribed angles subtending a diameter of a circle are right angles.
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.2a.pic}
\caption{} \label{sl.skk.4.2.2a.pic}
\end{figure}

Therefore, the central angle over a diameter is twice as big as
the circumferential angle over this diameter (Figure \ref{sl.skk.4.2.2a.pic}).
We will prove that this statement is also true for the circumferential and central angle over
any chord.


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

\textbf{\textit{Proof.}} Let $PQ=l$ be a chord of the circle $k(S, r)$ in
$V$ and let $P$ be an arbitrary point of this circle which does not lie on this chord. We will
prove that for the central angle $PSQ$ and the inscribed angle $PVQ$ it holds:
$$\angle PSQ = 2\angle PVQ.$$ We will consider three different cases
(Figure \ref{sl.skk.4.2.4.pic}):

\textit{1)} The center $S$ of the circle $k$ lies on one of the sides
of the inscribed angle $PVQ$. Without loss of generality, let this be
the side $VQ$. In this case, the triangle $PSV$ is an isosceles triangle
($SP \cong SV = r$), therefore $\angle SPV \cong \angle PVS$ (by the isosceles triangle theorem). In
the triangle $PSQ$, the exterior angle $PSQ$ is equal to the sum of the non-adjacent interior
angles (by the theorem about the sum of the interior angles of a triangle). Therefore:
 $$ \angle PSQ =
\angle SPV + \angle PVS = 2\angle PVS\\ = 2\angle PVQ.$$

\textit{2)} The center $S$ of the circle $k$ lies in the interior of the inscribed angle $PVQ$. In
this case, the other intersection of the circle $k$ with the line $VS$ – point $V'$ – lies on the
chord $l$, because this chord represents the intersection of the inscribed angle  $PVQ$ and the
circle $k$. If we use the result from \textit{1)} twice, we get:
  \begin{eqnarray*}
\angle PSQ &=& \angle PSV'+\angle V'SQ =
2\angle PVV'+2\angle V'VQ=\\ &=& 2(\angle PVV'+\angle V'VQ) = 2\angle PVQ.
  \end{eqnarray*}
\textit{3)} The center $S$ of the circle $k$ is an exterior point of the inscribed angle. In the
same way as in \textit{2)}, we define the point $V'$. In this case, the point $V'$ does not lie on
the chord $l$. Without loss of generality, let $P$ be an interior point of the inscribed angle $\angle V'VQ$.
Again, we use the result from \textit{1)}:
  \begin{eqnarray*}
  \angle PSQ &=& \angle V'SQ
-\angle V'SP = 2\angle V'VQ - 2\angle V'VP=\\ &=& 2(\angle V'VQ -\angle
V'VP) = 2\angle PVQ,
  \end{eqnarray*}
 which is what needed to be proven.  \kdokaz

The two most important consequences of the previous theorem are the following.

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

\textbf{\textit{Proof.}} From the previous statement \ref{SredObodKot}
it follows that all circumferential angles over the same line are equal to half
of the central angle over that line (Figure \ref{sl.skk.4.2.5.pic}).
  Because of this, all
of the aforementioned circumferential angles are congruent to each other.
 \kdokaz



        \bizrek
        \label{ObodObodKotNaspr}
        Two circumferential angles
        subtending the same chord of a circle, with the vertices lying
        on different sides of the line containing this chord,
        are supplementary.
        \eizrek


\textbf{\textit{Proof.}} The chord of a circle determines two lines on it which are complementary to each other (Figure \ref{sl.skk.4.2.5.pic}).
Each of the aforementioned circumferential angles corresponds to one of these two lines, which means that the sum of the corresponding central angles is equal
to $360^0$. Because the sum of circumferential angles according to statement \ref{SredObodKot}
is equal to half of the sum of the corresponding central angles, the circumferential angles are supplementary.
 \kdokaz

As we have already mentioned, we will often talk about circumferential and central
angles over the same chord, if we only know to which of the two corresponding lines this
chord belongs. In this sense, let us formulate the following statement.



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

\textbf{\textit{Proof.}}  According to the \textit{SSS} statement \ref{SSS} congruent
chords correspond to congruent central angles (Figure
\ref{sl.skk.4.2.4a.pic}). The statement is then a direct consequence of statement
\ref{SredObodKot}.  \kdokaz

It is clear that the following statement is also true  (Figure
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

The following consequence is also very interesting and useful.



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

\textbf{\textit{Proof.}}  Let $PAQ$ be the circumferential angle of some circle over the arc $PQ$, $LP$ such a tangent of this circle in the point $P$, that the points $L$ and $A$ are on different sides of the line $PQ$, and $PB$ the diameter of this circle (Figure \ref{sl.skk.4.2.6.pic}). Because $BP \perp PL$ (izrek
\ref{TangPogoj}) and $BQ \perp PQ$ (Talesov izrek
\ref{TalesovIzrKroz}), the angles $LPQ$ and $PBQ$ are congruent (izrek
\ref{KotaPravokKraki}). But according to izrek \ref{ObodObodKot}, the angles $PAQ$ and $PBQ$ are congruent, therefore $\angle LPQ \cong PAQ$.
 \kdokaz

The previous result allows the realization of one very important construction
-- the design of the geometric location of points in the plane, from which the angle of view of the line segment $AB$ is
$\omega$, i.e. $\angle AXB\cong \omega$, is the union of two open circular arcs, which are
symmetric with respect to the line $AB$.
This is actually the following problem.

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

\textbf{\textit{Proof.}} Let $p$ be a chord with the endpoint $A$, so that
$\angle p,BA \cong \omega$, line $n$ is the perpendicular to this
chord at point $A$ and $s$ is the line symmetrical to the line segment $AB$ (Figure
\ref{sl.skk.4.2.7.pic}). The intersection of lines $n$ and $s$ is denoted by
$S$, the circle with the center $S$ and the radius $SA$ is denoted by $k$. With $l$
we denote the arc, which is the intersection of circle $k$ and the plane not containing the chord $p$. In the complementary plane we determine the arc $l'$ in a similar way as the arc $l$. We prove that the desired geometric location of points is the set $l \cup l'\setminus\{A,B\}$.

The fact that from each point of the arc $l$ (or $l'$), which is different from
the points $A$ and $B$, the line segment $AB$ is seen under the angle $\omega$, follows from
theorems \ref{TangPogoj} and \ref{ObodKotTang}. For an arbitrary point
$P$ of the open arc $l$ it holds: $\angle APB \cong \angle p,AB \cong
\omega$.

Assume that the point $M$ does not belong to the set $l \cup
l'\setminus\{A,B\}$. In the case when $M$ is one of the points $A$ or
$B$, the angle $AMB$ does not even exist. Let $M \neq A,B$ and without loss of generality assume that the point $M$ is in the same plane as the arc $l$.
We denote by $N$ the other intersection of the chord $AM$ and the arc $l$ ($N\neq A$).
If $\mathcal{B}(A,M,N)$, then in the triangle $NMB$ the external angle $AMB$
is greater than the adjacent internal angle $MNB$ (theorem
\ref{zunanjiNotrNotrVecji}), which, according to what has already been proven, is equal to $\omega$,
so $\angle AMB>\omega$. If $\mathcal{B}(A,N,M)$ holds, we can, by using a similar reasoning,  conclude that in this case $\angle
AMB<\omega$, which means that for no point $M\notin l \cup
l'\setminus\{A,B\}$ it holds that $\angle AMB \cong \omega$.
 \kdokaz

From the proof of the previous theorem we also get the following conclusion.


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

In the following examples we will see the use of the theorem about the peripheral and central angle and its consequences.



         \bzgled
         Construct a triangle with given $a$, $\alpha$, $v_a$. \label{konstr_aalphava}
         \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1d.pic}
\caption{} \label{sl.skk.4.3.1d.pic}
\end{figure}

   \textbf{\textit{Analysis.}} The point $A$ lies at the same time at the geometric location of the points from which the line $BC$ is seen at an angle $\alpha$ (the union of two circular arcs - Theorem \ref{ObodKotGMT}) and at the parallel of the line $BC$, which is $v_a$ away from it (Figure \ref{sl.skk.4.3.1d.pic}). So the vertex $A$ is the intersection of this parallel and the aforementioned geometric location of points.

\textbf{\textit{Construction.}} First, let's draw the line $BC\cong a$, then the geometric location of points $\mathcal{L}$, from which this line is seen at an angle $\alpha$ (Theorem \ref{ObodKotGMT}). Then let's draw the parallel $p$ of the line $BC$ at a distance $v_a$. With $A$ we mark the intersection of the line $p$ and the aforementioned geometric location of points $\mathcal{L}$. We will prove that the triangle $ABC$ is the desired triangle.

\textbf{\textit{Proof.}} By construction, it is clear that $BC\cong a$. By construction, the point $A$ lies on the geometric location of points from which the line $BC$ is seen at an angle $\alpha$, so $BAC\cong\alpha$. The altitude of the triangle $ABC$ from the vertex $A$ is consistent with the line $v_a$, because the point $A$ by construction lies on the line $p$, which is $v_a$ away from the line $BC$.

\textbf{\textit{Discussion.}} The necessary condition is of course $\alpha<180^0$. The number of solutions to the task is equal to the number of intersections
of the line $p$ and the set $\mathcal{L}$.
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
 Let $S$
be the intersection of the lines $p$, $q$ and $r$. It is clear that the lines determine
the angles $60^0$. Because $\angle XPS \cong \angle XQS \cong \angle XRS =
90^0$, by  \ref{TalesovIzrKroz2} the points $S$, $X$, $P$, $Q$ and
$R$ lie on the circle $k$ with diameter $SX$.
 If we use \ref{ObodObodKot} for the appropriate arcs $PQ$ and $QR$,
 we have $\angle PRQ \cong \angle PSQ =
60^0$ and $\angle QPR \cong \angle QSR = 60^0$. Because all angles
are equal to $60^0$, $PQR$ is a regular triangle.
 \kdokaz

Let $k(O,R)$ and $l(S,r)$ ($R = 2r$) be circles touching each other internally
and $P$ an arbitrary point on the circle $l$. Which curve
is described by the point $P$ if the circle $l$ rolls without slipping around the circle $k$\footnote{This problem was solved by the Polish astronomer
 \index{Copernicus, N.} \textit{N. Copernicus} (1473--1543).
 In the general case, when it is not necessarily $R = 2r$, the curve
 which is described by the point $P$, is called \index{hipocikloida}
  \pojem{hipocikloida}. In the case of the outer rolling of the circle
  around the other circle, the curve is called \index{epicikloida}
  \pojem{epicikloida}, in the case
  of the rolling of the circle around the straight line, it is called \index{cikloida}
  \pojem{cikloida}. The cikloida was first investigated by the German mathematician and
  philosopher \index{Kuzanski, N.} \textit{N. Kuzanski} (1401--1464)
  and later by the French mathematician and philosopher \index{Mersenne, M.}
  \textit{M. Mersenne} (1588--1648). It was named by the Italian physicist,
  mathematician, astronomer and philosopher \index{Galilei, G.}
   \textit{G. Galilei} (1564--1642) in 1599.}?

\begin{figure}[!htb]
\centering
\input{sl.skk.4.2.10.pic}
\caption{} \label{sl.skk.4.2.10.pic}
\end{figure}

\textbf{\textit{Solution.}}
 Let
$P_0$ be the position of the point $P$ at the moment when it lies on the circle $k$ (Figure
\ref{sl.skk.4.2.10.pic}). At the moment when the point $P$ is in position $P_i$,
the circle $l$, which is in position $l_i$, touches the circle $k$ at some
point $T_i$. Since this is a "movement without slipping", the lengths
of the corresponding arcs $P_0T_i$ and $P_iT_i$ of the circles $k$ and $l$ are equal to each other. The radius of the circle $k$ is twice as large as the radius of the circle $l$,
so for the corresponding central angles of the aforementioned arcs we have $\angle
T_iS_iP_i= 2\angle T_iOP_0$. But $\angle T_iOP_i$ is the corresponding arc angle of the circle $l$ for the same arc $P_iT_i$, so $2\angle
T_iOP_i = \angle T_iS_iP_i$ (statement \ref{ObodObodKot}). From the two previous
relations we obtain $\angle T_iOP_i= \angle T_iOP_0$, which means that the point $P_i$ is collinear with the points $O$ and $P_0$, so the desired path
of the point $P$ represents the diameter $P_0P'_0$  of the circle $k$.
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
 Let $C'$ and $D'$ be such points on the line segments $AC$ and $AD$,
 that: $CC'\cong CB \cong CA$, $DD'\cong DB$,
$\mathcal{B}(A,C,C')$ and $\mathcal{B}(A,D,D')$. The triangles $C'CB$ and
$D'DB$ are isosceles, therefore by  \ref{enakokraki} and \ref{zunanjiNotrNotr},
it follows:
 $$\angle CC'B \cong \angle CBC' = \frac{1}{2}\angle ACB
\hspace*{2mm}\textit{ and }\hspace*{2mm}
 \angle DD'B \cong \angle DBD'
= \frac{1}{2}\angle ADB.$$
 Because the angles $ACB$ and $ADB$ are supplementary
  (by \ref{ObodObodKot}).
The angles $AC'B$ and $AD'B$ are supplementary as well,  and the points $C'$ and $D'$ lie
on the corresponding arc $l'$ over the segment $AB$ (by \ref{ObodKotGMT}). Because $CC'\cong CB \cong CA$, the distance $AC'$
is the diameter of the circle that contains the arc $l'$, therefore the $\angle AD'C'$ is a right angle (by \ref{TalesovIzrKroz2}). The distance $AC'$ is therefore
the hypotenuse of the right triangle $AD'C'$ and by  \ref{vecstrveckot} it follows:
$$AC + CB = AC'> AD'= AD + DB,$$ which was to be proven. \kdokaz



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


\textbf{\textit{Proof.}} First, from the similarity of the triangles $CAE$ and
$CBE$ (by \textit{SAS} \ref{SKS}) it follows that $\angle EBC\cong\angle
EAC=90^0$ and $EA\cong EB$ (Figure \ref{sl.skk.4.2.IMO1.pic}).
We prove the equivalence $EF\perp HG \Leftrightarrow GF\cong FH$ in both
directions.

($\Rightarrow$) Let's assume that the lines $EF$ and $HG$ are
perpendicular, i.e. $\angle EFG\cong\angle EFH=90^0$. Let $k$
and $l$ be circles with diameters $EG$ and $EH$. Because
$\angle EAG\cong\angle EFG=90^0$ and $\angle EBH\cong\angle
EFH=90^0$, by \ref{TalesovIzrKroz} we have $A,F\in k$ and $B,F\in
l$. First, from $EA\cong EB$ it follows that $\angle EAB\cong
\angle EBA$. From this and \ref{ObodObodKot} it follows:
 $$\angle EGF\cong\angle EAF\cong\angle EBF\cong\angle EHF.$$
 Therefore, the triangle $EGH$ is equilateral, so its height $EF$
 is also the altitude (congruence of triangles $EFG$ and $EFH$,
 \textit{ASA} \ref{KSK}) or $GF\cong FH$.

($\Leftarrow$) Now let $GF\cong FH$, i.e. the point $F$ is the
center of the line $GH$. Let $k$ be a circle with diameter $EG$.
In addition to the point $A$ we mark with $\widehat{F}$ the
other intersection of this circle with the line $AB$. If the
circle $k$ touches the line $AC$, it follows that $G=A$ or $F=D$
and $H=B$, so in this case $GF\cong FH$ is already fulfilled.

Assume that $\widehat{F}\neq F$. Let $\widehat{H}$ be the
intersection of the lines $G\widehat{F}$ and $CB$. Because the
point $\widehat{F}$ lies on the circle $k$ with diameter $EG$,
$\angle G\widehat{F}E=90^0$, i.e. $E\widehat{F}\perp
G\widehat{H}$. Therefore, for the points $G$, $\widehat{F}$ and
$\widehat{H}$ the assumptions of the left side of the
equivalence are fulfilled, so from the already proven first part
of the statement ($\Rightarrow$) it follows that
$G\widehat{F}\cong \widehat{F}\widehat{H}$, i.e. the point
$\widehat{F}$ is the center of the line $G\widehat{H}$. In the
triangle $GH\widehat{H}$ the $\widehat{F}F$ is the median, so
$\widehat{F}F\parallel \widehat{H}H$ and $AB\parallel BC$, which
is not possible. Thus, the assumption $\widehat{F}\neq F$
disappears, so $\widehat{F}= F$, so $\widehat{H}=H$. In the end,
from $E\widehat{F}\perp G\widehat{H}$ it follows that $EF\perp
GH$.
 \kdokaz





%________________________________________________________________________________
 \poglavje{More About Circumcircle and Incircle of a Triangle}
 \label{odd4OcrtVcrt}


First, we will consider some important points that lie on the
circumcircle of a triangle.

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

 Let the point $N$ be one of the intersections of the Circumcircle $l(O,R)$ of the triangle $ABC$ and
 the bisector of the side $BC$
(such that $A,N\perp BC$). Because the point $N$ lies on the bisector of the side
$BC$, it follows that $NB \cong NC$. Therefore, the triangle $BNC$ is an isosceles triangle,
so the angles $\angle NBC$ and $\angle NCB$ are congruent angles (by Theorem \ref{enakokraki}). Because the point $N$ also lies on the Circumcircle $l(O,R)$
of the triangle $ABC$, by Theorem \ref{ObodObodKot} it follows that:
 \begin{eqnarray*}
 \angle BAN
\cong \angle BCN \textrm{ (obodna kota za krajši lok }BN \textrm{) }\\
 \angle NAC \cong \angle NBC \textrm{ (obodna kota za krajši lok }
 CN \textrm{).}
 \end{eqnarray*}
 Therefore, $\angle BAN \cong \angle NAC$ or the line $AN$ is the bisector of the angle
$BAC$, thus the theorem is proven.
 \kdokaz


 The point $N$ from the previous theorem is the center of that arc $BC$ of the Circumcircle $l(O,R)$ of the triangle $ABC$ which does not contain the vertex $A$.
 We shall now prove another important property of the point $N$.



        \bizrek \label{TockaN.NBNC}
        For the point $N$ from the previous theorem is $NB\cong NS\cong NC$,
        where $S$ is the incentre of the triangle $ABC$.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.2.pic}
\caption{} \label{sl.skk.4.3.2.pic}
\end{figure}

\textbf{\textit{Proof.}} Let's mark with $\alpha$ and $\beta$ the internal
angles of the triangle $ABC$ at the vertices $A$ and $B$ (Figure
\ref{sl.skk.4.3.2.pic}). $BNS$ is an isosceles triangle (statement
\ref{enakokraki}), because the angles at the vertices $B$ and $S$ are equal.
If we use the statement \ref{zunanjiNotrNotr} and \ref{ObodObodKot},
we get:
 \begin{eqnarray*}
 \angle BSN &=& \angle ABS + \angle BAS =\frac{1}{2}\alpha+\frac{1}{2}\beta,\\
\angle SBN &=& \angle SBC +\angle CBN  = \angle SBC + \angle CAN =
\frac{1}{2}\beta+\frac{1}{2}\alpha.
 \end{eqnarray*}
Therefore $NB \cong NS$  and similarly $NC \cong NS$.
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
 Let $N$ be the point defined as in the previous statements
  (Figure \ref{sl.skk.4.3.1b.pic}). The lines
 $AA'$ and $ON$ are parallel, because they are both perpendicular to the line $BC$.
 Because $OA\cong ON=R$, $AON$ is an isosceles triangle. Therefore, first of all:
 $$\angle A' AE \cong \angle ANO \cong \angle NAO =
\angle EAO,$$
 and then:
 $$\angle A'AE=\frac{1}{2}\alpha-\left(90^0-\beta \right)=
 \frac{1}{2}\alpha-\left(\frac{\alpha+\beta+\gamma}{2}-\beta \right)=
 \frac{1}{2}\left( \beta-\gamma\right),$$ which was to be proven. \kdokaz

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

(\textit{i}) Let $L$ be the intersection of the lines $AP$ and $QR$. By
\ref{TockaN} points $P$, $Q$ and $R$ lie on the simetrals $AS$, $BS$
and $CS$ of the internal angles of the triangle $ABC$ ($S$ is the center of the triangle
$ABC$ of the inscribed circle). If we denote with $\alpha$, $\beta$ and $\gamma$ the internal angles of the triangle $ABC$, then due to the similarity of the corresponding external angles (\ref{ObodObodKot}) we get:
 \begin{eqnarray*}
\angle RPL &=& \angle RPA = \angle RCA =\frac{1}{2}\gamma,\\
 \angle PRL &=& \angle PRQ = \angle PRC + \angle CRQ =
\angle PAC + \angle CBQ = \frac{1}{2}\alpha+ \frac{1}{2}\beta.
 \end{eqnarray*}
Therefore, the sum of the angles in the triangle $PRL$  (\ref{VsotKotTrik})
$180^0 =\frac{1}{2}\alpha+ \frac{1}{2}\beta +\frac{1}{2}\gamma
+\angle RLP = 90° + \angle RLP$. So $\angle RLP = 90°$ or $AP
\perp QR$.

(\textit{ii}) By
the statement \ref{TockaN.NBNC} it is $RA \cong RS$, therefore from the similarity of
right-angled triangles $ALR$ and $SLR$ (statement \textit{SSA}
\ref{SSK}) it follows that the point $L$ is the center of the diagonal $AS$
of the quadrilateral $AESF$. From the similarity of triangles $AEL$ and $AFL$ (statement
\textit{ASA} \ref{KSK}) it follows that the point $L$ is also the center
of the diagonal $EF$, therefore the $AESF$ is a parallelogram (statement
\ref{paralelogram}). Because the diagonals $AS$ and $EF$ are also perpendicular, the
quadrilateral $AESF$ is a rhombus (statement \ref{RombPravKvadr}).
 \kdokaz

From the previous statement we directly get a consequence.


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



We prove some consequences of statement \ref{ObodObodKot}, which are related to
the altitude point.



         \bizrek \label{TockaV'}
         Points that are symmetric to the orthocentre of an acute triangle
            with respect to its sides lie on the circumcircle of this triangle.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.3.pic}
\caption{} \label{sl.skk.4.3.3.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $V$ be the orthocentre of a triangle
$ABC$, $l$ the circumcircle of the triangle $ABC$ and $V_a$ the other
intersection point of the circle $l$ with the altitude $AA'$ (Figure
\ref{sl.skk.4.3.3.pic}). We prove that the point $V_a$ is symmetric to
the point $V$ with respect to the line $BC$. It is enough to prove
that $VA'\cong V_aA'$. The angles $V_aBC$ and $V_aAC$ are complementary
(circumscribed angle for the chord $V_aC$ - izrek \ref{ObodObodKot}),
the angles $V_aAC$ and $CBV$  are complementary angles with
perpendicular legs (izrek \ref{KotaPravokKraki}). Therefore, the
angles $V_aBC$ and $CBV$ are also complementary, and so are the
triangles $V_aBA'$ and $VBA'$ or $VA'\cong V_aA'$. A similar statement
holds for the other two altitudes.
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


\textbf{\textit{Proof.}} A direct consequence of the previous izrek
\ref{TockaV'}, because the three aforementioned circumcircles are
symmetric to the circumcircle of the triangle $ABC$ with respect to
the altitude of its sides (Figure \ref{sl.skk.4.3.3a.pic}).



         \bizrek \label{TockaV1}
          Points that are symmetric to the orthocentre of an acute triangle
            with respect to the midpoints of its sides lie on the circumcircle of this triangle.
         \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.3b.pic}
\caption{} \label{sl.skk.4.3.3b.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $V$ be the altitude point of the triangle $ABC$,
$l$ the circumscribed circle (with the center $O$) of the triangle $ABC$ and $V_{A_1}$ the point that is symmetrical to the point $A$ with respect to the point $O$ (Figure \ref{sl.skk.4.3.3.pic}). From the very definition of the point $V_{A_1}$ it is clear that it lies on the circle $l$. We shall prove that $V_{A_1}$ is symmetrical to the point $V$ with respect to the point $A_1$, which is the center of the line $BC$. Because $AV_{A_1}$ is the diameter of the circle $l$, according to the Theorem \ref{TalesovIzrKroz2} $\angle ACV_{A_1}=90^0$ or $V_{A_1}C\perp AC$.  The line $BV$ is the altitude of the triangle $ABC$, therefore $BV\perp AC$. From the last two relations it follows that $V_{A_1}C\parallel BV$. Similarly
$V_{A_1}B\parallel CV$. Therefore the quadrilateral $V_{A_1}CVB$ is a parallelogram, thus its diagonals $VV_{A_1}$ and $BC$ have a common center. The center of the line $BC$ is the point $A_1$, which means that  $V_{A_1}$ is symmetrical to the point $V$ with respect to the point $A_1$. The point $V_{A_1}$ but, according to the construction, lies on the circle $l$.
\kdokaz


We shall also prove some consequences of the Theorem \ref{ObodObodKot}, which are connected with the circumscribed
circle of a triangle.


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

\textbf{\textit{Proof.}} Because $\angle ACP>60^0>\angle PAC$, by
the statement \ref{vecstrveckot} $AP>PC$ (Figure
\ref{sl.skk.4.3.4.pic}). Therefore, on the line $AP$ there exists such
a point $Q$, that $PQ\cong PC$. By the statement \ref{ObodObodKot}
$\angle CPQ=\angle CPA\cong\angle CBA=60^0$, which means that
$PCQ$ is an isosceles triangle, therefore also $CQ\cong CP$ and
$\angle PCQ=60^0$. From this it follows that $\angle ACQ=\angle
ACP-60^0=\angle BCP$. By the statement \textit{SAS} (statement
\ref{SKS}) the triangles $ACQ$ and $BCP$ are similar, therefore
also $AQ\cong BP$.

In the end: $|PB|+|PC|=|AQ|+|PQ|=|AP|$.
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

We mark with $k$, $l$, $j$ and $o$ the circumcircles of the triangles
$OBC$, $OAC$, $OAB$ and $ABC$ and with $P$ an arbitrary point of the
circle $k$ so that the points $O$ and $P$ are on different sides of
the line $BC$. By the assumption the circles $k$, $l$ and $j$ are
similar. The angles $BAO$ and $BCO$ are also similar, because they
are the angles between the similar circumcircles $k$ and $j$ over
the chord $BO$ (statement \ref{SklTetSklObKot2}). Analogously the
angles $CAO$ and $CBO$ are similar. Because of this:
 $$\angle BAC = \angle BAO + \angle CAO = \angle BCO
+ \angle CBO = 180° - \angle BOC = \angle BPC.$$
 Therefore the circles $k$ and $o$ have a similar
circumferential angle over the common chord $BC$, therefore they are
similar.
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
Since $\angle PAS$ and $\angle QCR$ are right angles, points $A$ and $B$ lie on the circles $k$ and $l$ with diameters
$PS$ and $QR$ (Figure \ref{sl.skk.4.3.1c.pic}). The carrier of the diagonal $AC$ of the square $ABCD$ is also the symmetry of the internal angles $BAD$ and $BCD$, so it goes through
the centers $N$ and $M$ of the corresponding arcs, which are determined by $k$ and $l$ (statement \ref{TockaN}).
The construction can therefore be carried out by first planning the circles $k$ and $l$, then the line $NM$, the points $A$ and $C$ and finally
the points $B$ and $D$.
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
   Let $ABC$ be a triangle in which the altitude $AA'$,
the median $AA_1$ and the section of the symmetry $AE$ of the internal angle $BAC$ are consistent
with the distances $v_a$, $t_a$ and $l_a$. With $O$ we mark the center of the triangle $ABC$ of the drawn
circle $k$. By statement \ref{TockaN}
the lines $AE$ and $OA_1$ intersect in the point $N$, which lies on
the circle $k$ (Figure \ref{sl.skk.4.3.1e.pic}).

So we can first plan
a right triangle $AA'E$ with the leg $v_a$ and the hypotenuse $l_a$ and the point $A_1$ from the condition $AA_1\cong t_a$. Then
plan the point $N$ as the intersection of the line $AE$ and the perpendicular of the line $A'E$ through
the point $A_1$. The center $O$ is the intersection of the line $A_1N$ and
the symmetry of the distance $AN$ (because $AN$ is the chord of the circle $k$). The points $B$ and $C$ are the intersections
of the circle $k(O,OA)$ with the line $A'E$.
   \kdokaz




         \bzgled
         Construct a triangle  $R$, $r$, $a$. \label{konstr_Rra}
         \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.3.1a.pic}
\caption{} \label{sl.skk.4.3.1a.pic}
\end{figure}


\textbf{\textit{Solution.}} Let $ABC$ be a triangle such that $BC\cong a$ and $l(O,R)$ and $k(S,r)$ are its circumscribed and inscribed circle
   (Figure \ref{sl.skk.4.3.1a.pic}). We denote with $\alpha$, $\beta$ and $\gamma$ its internal angles at vertices $A$, $B$ and $C$. By 
\ref{SredObodKot} we have $\alpha = \angle BAC = \frac{1}{2}\cdot\angle BOC$.
From \ref{kotBSC} it follows that $\angle BSC=90^0+\frac{1}{2}\cdot\alpha$.
From two relations we obtain the equality
$\angle BSC=90^0+\frac{1}{4}\cdot\angle BOC$, which allows the construction.

First we draw an isosceles triangle $BOC$ ($BC\cong a$ and $OB\cong
OC\cong R$). We obtain point $S$ as one of the intersections of the arc with the chord
$BC$ and the external angle $90^0+\frac{1}{4}\cdot\angle BOC$ and the line,
which is at a distance $r$ parallel to the line $BC$. Then we draw
the inscribed circle $k(S,r)$ and point $A$ as the intersection of the other two tangents
of this circle from points $B$ and $C$.
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

\textbf{\textit{Proof.}} We mark with $\alpha$, $\beta$ and $\gamma$
the internal angles of the triangle $ABC$ at the vertices $A$, $B$ and $C$
(Figure \ref{sl.skl.4.3.IMO1.pic}). The condition $\angle PBA + \angle PCA
= \angle PBC + \angle PCB$ can be rewritten in the form
$\beta-\angle PBC + \gamma-\angle PCB = \angle PBC + \angle PCB$
or:
 $$\angle PBC + \angle PCB=\frac{1}{2}\left( \beta+\gamma\right).$$
From this and the fact that the sum of the internal angles of each of the
triangles $BPC$ and $ABC$ is equal to $180^0$ (\izrekref{VsotKotTrik}),
it follows:
 $$\angle BPC =180^0-\frac{1}{2}\left( \beta+\gamma\right)=90^0+
 \frac{1}{2} \alpha.$$
But from \kotBSC it follows $\angle BIC =90^0+
 \frac{1}{2}\cdot \alpha$, so $\angle BPC\cong \angle BIC$.
 Therefore, the points $P$ and $I$ lie on the same curve $\mathcal{L}$ with
 the chord $BC$ and the central angle $90^0+
 \frac{1}{2} \alpha$. Let the point $N$ be the intersection
 of the perpendicular bisector of the side $BC$ and the perpendicular
 bisector of the internal angle $BAC$ of the triangle $ABC$. By
 \izrekref{TockaN}, the point $N$ lies on the circumscribed circle
 of the triangle $ABC$ and $NB\cong NI\cong NC$ (\izrekref{TockaN.NBNC}). This means that $N$ is the center of the curve
 $\mathcal{L}$, so $NP\cong NI$ or $\angle NIP\cong\angle
 NPI<90^0$. Because the points $A$, $I$ and $N$ are collinear (they lie on
 the perpendicular bisector of the internal angle $BAC$), $\angle AIP =180^0-\angle
 NIP>90^0$. From \izrekref{vecstrveckot} (for the triangle $API$)
 it now follows that $|AP| \geq |AI|$ and the equality holds exactly when
 the triangle $API$ is not, i.e. when $P=I$.
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

\textbf{\textit{Proof.}} Because
the points $E$ and $F$ lie on the line of symmetry $EF$, and also on
the circle with center $O$, we have $$AF\cong FO\cong AO\cong EO \cong EA.$$ This
means that the quadrilateral $EOFA$ is a rhombus, which is made up of two congruent triangles $AOF$ and $AEO$.

Without loss of generality, we
assume that
$\angle COE>\angle COF$ (Figure \ref{sl.skk.4.3.IMO4.pic}).
First, from the condition $\angle
        AOC>60^0$ it follows that $\angle COF=60^0- \angle
        AOC>0^0$, so the points $A$ and $F$ are on the same side of the line
        $BC$.

 Because $AOC$ is an isosceles triangle with the base $AC$, by the
 \ref{enakokraki} and \ref{zunanjiNotrNotr} we have
  $\angle ACO =\frac{1}{2}\angle AOB$. The point $D$ is the center
  of the arc $BD$, so $\angle AOD\cong\angle DOB$
  or $\angle DOB=\frac{1}{2}\angle AOB$. This means that
   $\angle ACO\cong\angle DOB$ and the lines $AC$ and $DO$ are parallel by
   \ref{KotiTransverzala}. Because $AD\parallel JO$ by assumption, the
   quadrilateral $ADOJ$ is a parallelogram, so $AJ\cong OD$. Therefore
   $$AJ\cong OD\cong OE\cong AF\cong AE.$$
   From $AF\cong AE$ it follows that
  $AJ$ is the line of symmetry of the internal angle at the vertex $C$ of the triangle $CEF$
   (\ref{SklTetSklObKot}). Because $AJ\cong  AF\cong AE$,
  by \ref{TockaN.NBNC} the point $J$ is the center
        of the inscribed circle of this triangle.
\kdokaz


%________________________________________________________________________________
 \poglavje{Cyclic Quadrilateral} \label{odd4Tetivni}

We say that a
\index{štirikotnik!tetiven}\index{večkotnik!tetiven}\pojem{tetiven},
if there exists a circumscribed circle, or if there is a circle that
contains all of its vertices (Figure \ref{sl.skk.4.5.10.pic}). For
vertices in this case we say that they are \index{konciklične
točke}\pojem{konciklične točke}. We have already seen that every
triangle is tetiven (izrek \ref{SredOcrtaneKrozn}) and also that every
regular polygon is tetiven (izrek \ref{sredOcrtaneKrozVeck}). On the
other hand, it is clear that not all polygons are cyclic. For example,
a diamond is a quadrilateral that does not have a circumscribed
circle. In this section we will therefore deal with cyclic
quadrilaterals.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.10.pic}
\caption{} \label{sl.skk.4.5.10.pic}
\end{figure}

Since a square is a regular polygon, it is also a cyclic
quadrilateral. It is not difficult to prove that a rectangle is also a
type of cyclic quadrilateral - the center of the circumscribed circle
is the intersection of its diagonals, which are consistent and
bisect each other. But how would we generally determine if a
quadrilateral is cyclic? It is clear that in a cyclic quadrilateral
(generally also in a polygon) the altitudes of all its sides intersect
in one point (Figure \ref{sl.skk.4.5.10.pic}). This condition is
sufficient for the quadrilateral to be cyclic, but it is not
sufficiently operative in specific cases. For the cyclicity of
quadrilaterals there is a necessary and sufficient condition that is
more useful.



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

($\Rightarrow$) First, let's assume that the quadrilateral $ABCD$
is cyclic. Because it is convex, the vertices $A$ and $C$ are on
different sides of the line $BD$. By \ref{ObodObodKotNaspr}
$\alpha+\gamma=180^0$.

($\Leftarrow)$ Now let's assume that the opposite angles of the
quadrilateral $ABCD$ are supplementary, i.e. $\alpha+\gamma=180^0$.
Let $k$ be the circle drawn through the triangle $ABD$. In this
case, the fourth vertex $C$ of the line $BD$ is seen under the
angle complementary to the angle at the vertex $A$, which means
that the point $C$ also lies on the circle $k$ (\ref{ObodKotGMT}).
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

We use the criterion from \ref{TetivniPogoj} for a parallelogram
and a trapezoid.

            \bizrek \label{paralelogramTetivEnakokr}
            A parallelogram is cyclic if and only if it is a rectangle.
            \eizrek


\textbf{\textit{Proof.}} Let $\alpha$, $\beta$, $\gamma$ and $\delta$
be the interior angles of the parallelogram $ABCD$
 (Figure \ref{sl.skk.4.5.13.pic}).

($\Leftarrow$) If the parallelogram is a rectangle,
$\alpha+\gamma=90^0+90^0=180^0$, which means that $ABCD$ is a cyclic
quadrilateral (\ref{TetivniPogoj}).

($\Rightarrow$) Let's assume that $ABCD$ is a trapezoidal parallelogram.
 Because $ABCD$ is a parallelogram, according to Theorem \ref{paralelogram}
 $\alpha\cong\gamma$. Because it is also a trapezoid, according to Theorem \ref{TetivniPogoj}
$\alpha+\gamma=180^0$. So $\alpha\cong\gamma=90^0$, therefore
  $ABCD$ is a rectangle.
 \kdokaz

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.13.pic}
\caption{} \label{sl.skk.4.5.13.pic}
\end{figure}



            \bizrek \label{trapezTetivEnakokr}
            A trapezium is cyclic if and only if it is isosceles.
            \eizrek

\textbf{\textit{Proof.}} Let $ABCD$ be a trapezoid with a base $AB$ and with
internal angles $\alpha$, $\beta$, $\gamma$ and $\delta$
 (Figure \ref{sl.skk.4.5.13.pic}). In any trapezoid
  it holds that $\alpha+\delta=180^0$ and $\beta+\gamma=180^0$.


($\Leftarrow$) Let's assume that trapezoid $ABCD$ is isosceles, i.e. $AD
\cong BC$. According to Theorem \ref{trapezEnakokraki} in this case
$\alpha\cong\beta$. So $\alpha+\gamma=\beta+\gamma=180^0$, therefore
according to Theorem \ref{TetivniPogoj} $ABCD$ is a cyclic quadrilateral.

($\Rightarrow$) Let trapezoid $ABCD$ be a cyclic quadrilateral and $k$
its circumscribed circle. The bases $AB$ and $CD$ are parallel
chords of this circle, so they have a common perpendicular, which goes through
the center $S$ of the circle $k$ and is perpendicular to the chords $AB$ and
$CD$. This means that the legs $AD$ and $BC$ are symmetrical with respect to this perpendicular, so they are congruent and trapezoid $ABCD$  is isosceles.
 \kdokaz

 Particularly interesting are cyclic quadrilaterals with perpendicular
 diagonals\footnote{\index{Brahmagupta}\textit{Brahmagupta} (598--660), Indian mathematician, who
 studied such quadrilaterals.}.
 The following example applies to
such quadrilaterals.


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

Let $N$ and $M$ be the intersections of the rectangle with the line $AB$ through the point $S$ with the sides $AB$ and $CD$ of the quadrilateral $ABCD$. Then it holds:
 \begin{eqnarray*}
 \angle CDB &\cong& \angle CAB \hspace*{3mm}
 \textrm{(external angle for the appropriate locus } CB
 \textrm{ - izrek \ref{ObodObodKot}})\\
      &\cong& \angle NSB  \hspace*{3mm}
 \textrm{ (angle with
perpendicular arms - izrek \ref{KotaPravokKraki})}\\
     &\cong& \angle MSD  \hspace*{3mm}
 \textrm{(perfect angle)}
 \end{eqnarray*}
 Because $\angle CDB\cong \angle MSD$, $MD \cong MS$ (izrek \ref{enakokraki}).
 Similarly, $MC \cong MS$. Therefore,
 $MD \cong MC$, which means that $M$ is the center of the side $CD$.
 \kdokaz

We will consider one property of cyclic quadrilaterals with perpendicular diagonals
in the example \ref{HamiltonPoslTetiv}.



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

\textbf{\textit{Proof.}} Let $S$ be the intersection of the lines $NL$ and $PM$
(Figure \ref{sl.skk.4.5.0.pic}).
 If we use the izrek \ref{ObodObodKot} and \ref{TockaN} twice, we get:

 \begin{eqnarray*}
  \angle PNS &=& \angle PND +\angle DNL =
\angle PBD +\angle DBL =\\
 &=& \frac{1}{2} \angle ABD +\frac{1}{2}\angle CBD = \frac{1}{2}\angle
 ABC.
 \end{eqnarray*}

We similarly prove that $\angle NPS = \frac{1}{2}\angle
 ADC$. Therefore, according to the statement \ref{TetivniPogoj}:
 $$\angle PNS +\angle NPS = \frac{1}{2} \left(\angle ABC+\angle
 ADC\right)=90^0.$$
 If we use the statement \ref{VsotKotTrik} for the triangle $PSN$, we get
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

\textbf{\textit{Proof.}} We mark with $A_1$, $B_1$, $C_1$ and $D_1$
the incentres of the triangles $BCD$, $ACD$, $ABD$ and $ABC$
and with $N$, $M$, $L$ and $P$ the incentres of those arcs $AB$, $BC$, $CD$ and
$AD$ of the cyclic quadrilateral $ABCD$, which do not contain the other
vertices of this quadrilateral (Figure \ref{sl.skk.4.5.1.pic}). From the statement
\ref{TockaN} it follows that $BL$ and $DM$ are the angle bisectors of the angles $CBD$ and
$BDC$, therefore the point $A_1$ is the intersection of the lines $BL$ and $DM$. Similarly,
the point $B_1$ is the intersection of the lines $CP$ and $AL$. According to the statement
\ref{TockaN.NBNC},
 $LC\cong LA_1\cong LB_1\cong LD$, therefore $A_1LB_1$ is an isosceles triangle
 with the base $A_1B_1$. From the statement \ref{TockaN} it also follows that
 $LN$ is the angle bisector of the angle $ALB$ or $B_1LA_1$. In an isosceles
 triangle $A_1LB_1$ the angle bisector of the angle $B_1LA_1$ contains the altitude
 of this triangle from the point $L$. This means that $LN\perp
 A_1B_1$ holds. Similarly,
 $LN\perp C_1D_1$,  $PM\perp A_1D_1$
 and
 $PM\perp C_1B_1$ hold. From the previous statement \ref{TetŠtirZgl0} we know that $LN\perp PM$,
 therefore the quadrilateral $A_1B_1C_1D_1$ is a rectangle.
  \kdokaz

We have already mentioned that a rectangle is a right-angled quadrilateral. Now we will
prove an interesting property of rectangles that relates to points
that lie on its circumscribed circle.



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
 Let $O$ be the center of the circle $k$ (Figure \ref{sl.skk.4.5.15.pic}).
The quadrilateral $PMOL$ is a right-angled one, because $\angle OLP + \angle OMP
=90^0+90^0= 180^0$ (statement \ref{TetivniPogoj}). We mark with $l$
the circumscribed circle of this quadrilateral. Because the angles $OLP$ and $OMP$ are both
right, the distance $OP$ (or the radius of the circle $k$) is the radius of the
circle $l$. Then $LM$ is the chord of the circle $l$, which belongs to the peripheral angle
$\angle LOM =\angle AOB$, which is constant. Regardless of the choice
of the point $P$, the distance $LM$ is the chord of the circle with a constant radius
$OA$, which belongs to a constant peripheral angle $AOB$ (or the corresponding
constant central angle of this circle). The chords, which belong
to the corresponding central angles of the corresponding circles, are proportional to each other,
so the length of the distance $LM$ does not depend on the position of the point $P$.
 \kdokaz

  The properties of the right-angled quadrilateral are often used to prove
  various
properties of triangles.


            \bzgled \label{PedalniVS}
            The orthocentre of an acute triangle is the incentre of its \index{trikotnik!pedalni} pedal triangle.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.16.pic}
\caption{} \label{sl.skk.4.5.16.pic}
\end{figure}

\textbf{\textit{Proof.}}
 Let $AA'$, $BB'$ and $CC'$ be the altitudes of the triangle $ABC$, which intersect
 in the point $V$ of
the altitude of this
triangle (Figure \ref{sl.skk.4.5.16.pic}). If $A_1$ is the midpoint
of the side $BC$, the points $B'$ and $C'$ lie on the circle $k(A_1,A_1B)$
(statement \ref{TalesovIzrKroz2}). Therefore, the quadrilateral $BC'B'C$
is cyclic, so according to \ref{TetivniPogojZunanji} $\angle
AC'B'\cong \angle ACB = \gamma$. Similarly, we prove that the quadrilateral $AC'A'C$ is cyclic, so $\angle BC'A'\cong
\angle ACB = \gamma$. Therefore, the angles $AC'B'$ and $BC'A'$ are congruent. Because
$CC'\perp AB$, the angles $CC'B'$ and $CC'A'$ are also congruent. This
means that the line $C'C$ is perpendicular to the angle $A'C'B'$. Similarly, the lines $A'A$ and $B'B$ are perpendicular to the corresponding internal angles
of the triangle $A'B'C'$, so the point $V$ is the centre of the triangle $A'B'C'$
of the inscribed circle.
 \kdokaz

 From the proof of the previous statement (\ref{PedalniVS}) we can conclude that the angles, which are determined by the sides
of the pedal triangle $A'B'C'$  with the sides of the triangle
$ABC$, are equal to the corresponding angles of the triangle $ABC$. We will use this fact in the following example.



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

Let $L$ denote the intersection of the lines $OA$ and $B'C'$. It is enough to prove that the internal angle at the vertex $L$ of the triangle $C'LA$ is a right angle. Let us calculate the other two angles of this triangle. From the previous example \ref{PedalniVS} the angle at the vertex $C'$ is equal to $\gamma$. The triangle $AOB$ is isosceles and $\angle AOB=2\gamma$ (statement \ref{SredObodKot}). Therefore (statements \ref{enakokraki} and \ref{VsotKotTrik}) $\angle C' AL=\angle BAO =90^0-\gamma$, which implies that $\angle ALC'=90^0$.
 \kdokaz

A direct consequence of the statement \ref{PedalniVS} and \ref{PedalniLemasPQR} is the following statement.



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
            \pojem{Miquel point}\color{green1}\footnote{The point is named after
            the French mathematician \index{Miquel, A.} \textit{A. Miquel} (1816–-1851), who published
            this statement in 1838 as an article in Liouville's
            (\index{Liouville, J.}\textit{J. Liouville} (1809–-1882), French
            mathematician) journal. But, as is often the case in mathematics, Miquel
            was not the first to prove this statement. Ten years before him, this fact was
            discovered and published by the famous Swiss mathematician
            \index{Steiner, J.} \textit{J. Steiner} (1769--1863).}).
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.2.pic}
\caption{} \label{sl.skk.4.5.2.pic}
\end{figure}

\textbf{\textit{Proof.}} (Figure \ref{sl.skk.4.5.2.pic})

We denote with $k_A$, $k_B$ and $k_C$ the circumcircles of triangles
$AQR$, $PBR$ and $PQC$ and the internal angles of triangle $ABC$ in
order with $\alpha$, $\beta$ and $\gamma$. Let $S$ be the other
intersection of the circles $k_B$ and $k_C$ (the proof is similar in
the case when $S = P$). Quadrilateral $BPSR$ and $PCQS$ are
tangential, so $\angle RSP = 180^0 - \beta$ and $\angle QSP = 180^0
-\gamma$ (statement \ref{TetivniPogoj}). From this it follows that
$\angle RSQ = \beta +\gamma$ and then also $\angle RAQ + \angle RSQ
=\alpha + \beta +\gamma = 180^0$. Quadrilateral $ARSQ$ is also
tangential (statement \ref{TetivniPogoj}) or it has its own
circumcircle, which is actually the circle $k_A$, circumscribed to
triangle $AQR$. This means that the circles $k_A$, $k_B$ and $k_C$
intersect in point $S$.
 \kdokaz

In this chapter \ref{pogINV} we will prove one generalization of the previous
statement (see example \ref{MiquelKroznice}).



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


\textbf{\textit{Proof.}} We mark with $E$ the intersection of the angle bisector
of $BAC$ with the side $BC$ of the triangle $ABC$ (Figure
\ref{sl.skk.4.4.IMO1.pic}). We prove that $E$ is the desired point  i.e.
that it lies on the circumcircles
of both triangles $BML$
        and $CNL$.

Because from the construction of the points $M$ and $N$ it follows that $OM\cong ON$, the triangle $OMN$
is isosceles. This means that the bisector of $OL$ is also the bisector of the side $MN$ (follows from the similarity of the triangles $MSO$ and $NSO$, where $S$ is the center
of the segment $MN$). Therefore, the point $L$ lies on the bisector of the segment $MN$
 of the triangle, so by  \ref{TockaN} it lies on the circumcircle
 $k$
 of the triangle $AMN$. The condition $AB\neq AC$ tells us that the angle bisectors of $BAC$ and
 the side $MN$ (or the angle bisector of $MON$) are different, so their intersection is a point.

  If we use  \ref{TetivniPogojZunanji} and \ref{ObodObodKot},
 we get:
  \begin{eqnarray*}
   \angle BCA &\cong& AMN \cong\angle ALN,\\
   \angle ABC &\cong& ANM \cong\angle ALM.
  \end{eqnarray*}
From these relations and  \ref{TetivniPogojZunanji} it follows that $NLEC$ and $LMBE$ are tangential
quadrilateral. Therefore, the point $E$ lies on the circumcircles
of both triangles $BML$
        and $CNL$.
 \kdokaz

We say that a
\index{tetragon!tangential}\index{polygon!tangential}\pojem{tangential}
\index{tetragon!tangential}\index{polygon!tangential}\pojem{tangential},
if there exists an inscribed circle, or if there is such a
circle that the normals of all the sides of the polygon are its tangents
(Figure \ref{sl.skk.4.6.1.pic}). We have already seen that every
triangle is tangential (\ref{SredVcrtaneKrozn}) and also
a regular polygon is tangential (\ref{sredVcrtaneKrozVeck}). On the other hand, it is clear that not all
polygons are tangential. For example, a rectangle is a tetragon which does not have
an inscribed circle. In this section we will focus on
tangential tetragons.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.1.pic}
\caption{} \label{sl.skk.4.6.1.pic}
\end{figure}

Since a square is a regular polygon, it is also a tangential tetragon. But how would we in general determine whether a tetragon is tangential? It is clear that in a tangential tetragon (in general also in a polygon) the simetrals of all of its internal angles intersect in one point (Figure
\ref{sl.skk.4.6.1.pic}). This condition is sufficient for the tangentiality of a polygon.
Unfortunately, this condition is not very useful in
specific cases. There is a more useful condition that is necessary and
sufficient for the tangentiality of tetragons.



             \bizrek \label{TangentniPogoj}
              A quadrilateral $ABCD$ is tangential if and only if
               $$|AB| + |CD| = |BC| + |AD|.$$
            \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.2.pic}
\caption{} \label{sl.skk.4.6.2.pic}
\end{figure}


\textbf{\textit{Proof.}}  (Figure \ref{sl.skk.4.6.2.pic})

($\Rightarrow$) First, let's assume that the quadrilateral $ABCD$ is tangent and
  $k$ is its inscribed circle.
 Let $P$, $Q$, $R$ and $S$
be the points of tangency of sides $AB$, $BC$, $CD$ and $DA$ with the circle $k$. Because
the appropriate tangent lines are concurrent (by Theorem \ref{TangOdsek}), it holds:
$AP \cong AS$, $BP \cong BQ$, $CQ \cong CR$ and $DR \cong DS$. Therefore
 \begin{eqnarray*}
|AB| + |CD|&=&|AP| + |PB| + |CR| + |RD| \\&=& |AS| + |SD| + |BQ| +
|QC|\\&=&|AD| + |BC|.
 \end{eqnarray*}

 ($\Leftarrow$) We prove the converse statement. Let's assume that in the quadrilateral
 $ABCD$ the sums of the pairs of opposite sides are equal, i.e.
 $|AB| + |CD| = |BC| + |AD|$. There exists a circle $k$, which touches
sides $AB$, $BC$ and $DA$ of this quadrilateral (its center is
the intersection of the internal angle bisectors at vertices $A$ and $B$ of this
quadrilateral). We prove that this circle also touches side
$CD$ of the quadrilateral $ABCD$. Let $D'$ be the intersection of the other tangent from
point $C$ of the circle $k$ and the line $AD$. Let's assume that $D'\neq
D$. Without loss of generality, let $\mathcal{B}(A,D',D)$. Because the quadrilateral $ABCD'$ is tangent to the circle $k$, by the already proven part of the theorem it holds $|AB| + |CD'| = |AD'|+|BC|$. But since by the assumption also $|AB| + |CD| = |AD| + |BC|$, it also holds $|CD|-|CD'| = |DA| - |D'A|=|DD'|$ i.e.  $|CD|= |CD'| + |DD'|$. But this is not possible due to the triangle inequality \ref{neenaktrik} (points $C$,
$D$ and $D'$ cannot be collinear, because otherwise it would hold $C\in
AD$). In a similar way we arrive at a contradiction also in the case when $\mathcal{B}(A,D,D')$. Therefore it holds $D'= D$, thus $ABCD$ is a tangential quadrilateral.
 \kdokaz

 The following theorems are a direct consequence of the previous criterion.

        \bizrek \label{TangDeltoidRomb}
        A rhombus, a deltoid, and a square are
         tangential quadrilaterals (Figure \ref{sl.skk.4.6.3.pic}).
        \eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.3.pic}
\caption{} \label{sl.skk.4.6.3.pic}
\end{figure}

         \bizrek \label{TangParalelogram}
          A parallelogram is a tangential quadrilateral
          if and only if it is a rhombus (Figure \ref{sl.skk.4.6.3.pic}).
        \eizrek

In the next two examples we will consider
tension and tangent quadrilaterals at the same time.



        \bzgled Let $k_A$, $k_B$, $k_C$ and $k_D$ circles with centres $A$,
        $B$, $C$ and $D$, such that two in a row (also $k_A$ and $k_D$)
        are touching each other externally. Prove that the quadrilateral defined by
        the touching points of circles is cyclic, and the quadrilateral $ABCD$ is tangential.
        \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.4.pic}
\caption{} \label{sl.skk.4.6.4.pic}
\end{figure}


\textbf{\textit{Proof.}}
 Let $P$, $Q$, $R$ and $S$ be the touching points of
the given circles in order, and $p$ and $r$ the common tangents of
the corresponding circles at points $P$ and $R$ (Figure \ref{sl.skk.4.6.4.pic}).

First, we have:
 \begin{eqnarray*}
 |AD| + |BC| &=& |AP| + |PD| + |BR| + |RC| =\\
  &=& |AQ| + |SD| + |QB| + |SC| =\\
  &=&  |AB| +
|CD|.
 \end{eqnarray*}
  Therefore, $ABCD$ is a tangent quadrilateral (statement \ref{TangentniPogoj}).

Tangents $p$ and $r$ divide the internal angle at vertices $P$ and $R$
of the quadrilateral $PQRS$ into angles, each of which is equal to half
of the corresponding central angle (statement \ref{ObodKotTang}). The aforementioned
central angles are the internal angles of the quadrilateral $ABCD$. We denote
them with $\alpha$, $\beta$, $\gamma$ and $\delta$. Therefore, (statement
\ref{VsotKotVeck}):
 \begin{eqnarray*}
 \angle QPS+ \angle SRQ&=& \angle QP,p+\angle p,PS+ \angle SR,r+\angle r,RQ=\\
  &=& \frac{1}{2}\alpha+\frac{1}{2}\delta+\frac{1}{2}\gamma+\frac{1}{2}\beta=\\
  &=& \frac{1}{2}\left(\alpha+\delta+\gamma+\beta\right)=\\
  &=& \frac{1}{2}\cdot360^0=180^0,
 \end{eqnarray*}
which means that $PQRS$ is a tension quadrilateral.
  \kdokaz

It is clear that the inscribed
 circle of the quadrilateral $ABCD$ is also the circumscribed circle of the quadrilateral $PQRS$. Because according to the assumption
 $PAQ$, $QBR$, $RCS$ and $SDP$ are equilateral triangles with bases
 $PQ$, $QR$, $RS$ and $SP$, the simetrals of the internal angles of the quadrilateral $ABCD$
 are also the simetrals of the sides of the quadrilateral $PQRS$ (Figure
 \ref{sl.skk.4.6.4a.pic}). This is also the second (simpler)
 way to prove the second part of the previous example - the assertion that $PQRS$
 is a tangential quadrilateral.

\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.4a.pic}
\caption{} \label{sl.skk.4.6.4a.pic}
\end{figure}



            \bzgled \label{tetivTangLema}
            Let $L$ be the intersection of the diagonals of a cyclic quadrilateral  $ABCD$.
            Prove that the foots of the perpendiculars from the point $L$ on the sides of
            this quadrilateral are the vertices of a tangential quadrilateral.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.5.pic}
\caption{} \label{sl.skk.4.6.5.pic}
\end{figure}


        \textbf{\textit{Proof.}}
  Let $P$, $Q$, $R$ and $S$ be the perpendicular projections from the point $L$ on the sides
   $AB$, $BC$, $CD$ and $DA$
of the quadrilateral $ABCD$ (Figure \ref{sl.skk.4.6.5.pic}).
Because of the appropriate right angles, $PBQL$ and $APLS$
are tangential quadrilaterals (statement \ref{TetivniPogoj}). According to the assumption, $ABCD$ is also tangential. If we
use this, we get the equality of the appropriate external angles (statement \ref{ObodObodKot}). Therefore:
$$\angle SPL \cong \angle SAL = \angle DAC \cong \angle DBC
= \angle LBQ \cong \angle LPQ.$$
From this it follows that the line $PL$ is the simetral of the internal angle at
the vertex $P$ of the quadrilateral $PQRS$. Similarly, the lines $QL$, $RL$ and $SL$
are the simetrals of the other three internal angles of this quadrilateral. Therefore, $L$ is the center of the inscribed circle of the quadrilateral $PQRS$,
so this is tangential.
        \kdokaz

We will now prove another interesting property of tangential quadrilaterals.

\bzgled
            Prove that the incircles of triangles $ABC$ and $ACD$ touch each
            other if and only if $ABCD$ is a tangential quadrilateral.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.6.pic}
\caption{} \label{sl.skk.4.6.6.pic}
\end{figure}


        \textbf{\textit{Proof.}}
   (Figure \ref{sl.skk.4.6.6.pic}).

   First, we prove some relations that hold for any convex quadrilateral $ABCD$.
Let $P$, $Q$ and $X$ be the points in which the inscribed circle $k$ of triangle $ABC$ touches its sides
$AB$, $BC$ and $CA$, and $R$, $S$ and $Y$  be the points in which the inscribed circle $l$ of triangle $ACD$ touches its sides $CD$, $DA$ and $AC$. First, it holds (from \ref{TangOdsek}):
 \begin{eqnarray*}
 |AX| &=& |AP|=\frac{1}{2}\left(|AX|+|AP|\right)=\frac{1}{2}\left(|AC|-|CX|+|AB|-|BP|\right)\\
  &=& \frac{1}{2}\left(|AC|-|CQ|+|AB|-|BQ|\right)=
  \frac{1}{2}\left(|AC|+|AB|-|BC|\right),
 \end{eqnarray*}
 therefore it holds:
  $$|AX|=\frac{1}{2}\left(|AC|+|AB|-|BC|\right).$$
  In the same way, we prove that it also holds:
  $$|AY|=\frac{1}{2}\left(|AC|+|AD|-|DC|\right).$$
  Now we can start with proving the equivalence.

The circles $k$ and $l$ touch each other exactly when $X = Y$ or $|AX| = |AY|$. The last equality holds exactly when: $$\frac{1}{2}\left(|AC|+|AB|-|BC|\right)=\frac{1}{2}\left(|AC|+|AD|-|DC|\right)$$
or $|AB| + |DC| = |AD| + |BC|$, which is fulfilled exactly when $ABCD$ is a tangential quadrilateral (from \ref{TangentniPogoj}).
   \kdokaz

The consequence of this is the following claim.

\bzgled
            Let $ABCD$ be a tangential quadrilateral.
            Then the  incircles of the triangles $ABC$ and $ACD$ touch each other
            if and only if
            the  incircles of the triangles $ABD$ and $CBD$ touch each
            other (Figure \ref{sl.skk.4.6.6a.pic}).
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.6.6a.pic}
\caption{} \label{sl.skk.4.6.6a.pic}
\end{figure}


        \textbf{\textit{Proof.}} The statements that the incircles of the triangles $ABC$ and $ACD$ or the triangles $ABD$ and $CBD$ touch, are
        equivalent to the statement that the quadrilateral $ABCD$ is tangent. This means that the initial statements are equivalent.
         \kdokaz

%_______________________________________________________________________________
 \poglavje{Bicentric Quadrilateral} \label{odd4TetivniTangentni}

  Some quadrilaterals are both tangential and chordal. We call them \index{štirikotnik!tetivnotangentni}\pojem{tetivnotangentni} or \index{štirikotnik!bicentrični}\pojem{bicentrični} quadrilaterals. Which
 quadrilaterals are these? The square is certainly one of them. Is it the only one? The answer is negative. The quadrilateral we get from the example \ref{tetivTangLema} is always tangent. In a certain case it will be chordal as well.
 Namely, the following statement is true.



                \bizrek \label{tetivTangIzrek}
                If $L$ is the intersection of the perpendicular diagonals of a cyclic quadrilateral
            $ABCD$, then the foots of the perpendiculars from the point $L$ on the sides of
            this quadrilateral are the vertices of a bicentric quadrilateral.
                \eizrek



\begin{figure}[!htb]
\centering
\input{sl.skk.4.7.2.pic}
\caption{} \label{sl.skk.4.7.2.pic}
\end{figure}


        \textbf{\textit{Proof.}}
   (Figure \ref{sl.skk.4.7.2.pic})

Let's use the same notation as in the example \ref{tetivTangLema}. We have already proven that $PQRS$ is a tangent quadrilateral. We will now prove that it is also a bicentric quadrilateral. From the proof of the statement in the aforementioned example \ref{tetivTangLema} it follows:
\begin{eqnarray*}
        \angle SPQ &=& \angle SPL+\angle LPQ = \angle SAL+\angle LBQ =\\
          &=& \angle DAC + \angle DBC
        = 2\cdot\angle DBC
\end{eqnarray*}
or $\angle SPQ= 2\cdot\angle DBC$. Similarly, $\angle SRQ= 2\cdot\angle ACB$.
   Because, by assumption, $AC\perp BD$, $CLB$ is a right angled triangle, therefore:
  $$\angle SRQ+\angle SRQ=2\cdot(\angle DBC+\angle ACB)=2\cdot 90^0=180^0.$$
   By  \ref{TetivniPogoj} $PQRS$ is a bicentric quadrilateral.
   \kdokaz

 It is not difficult to convince oneself that the converse statement is also true.



        \bizrek
        Let $PQRS$ be a bicentric quadrilateral. Suppose that point $L$ is
        the incentre of this quadrilateral and at the same time the intersection of the diagonals
        of a cyclic quadrilateral $ABCD$. If $P$, $Q$, $R$ and $S$ the foots of the perpendiculars
        from the point $L$ on the sides of quadrilateral $ABCD$, then $AC\perp BD$.
        \eizrek

In the next exercise we will see that for three non-collinear points $A$, $B$ and $C$ there is only one point $D$, such that $ABCD$ is a bicentric quadrilateral.


            \bnaloga\footnote{4.
            IMO Czechoslovakia - 1962, Problem 5.}
             On the circle $k$ there are given three distinct points $A$, $B$, $C$. Construct (using
            only straightedge and compasses) a fourth point $D$ on $k$ such that a circle
            can be inscribed in the quadrilateral thus obtained.
            \enaloga

\begin{figure}[!htb]
\centering
\input{sl.skk.4.5.IMO1.pic}
\caption{} \label{sl.skk.4.5.IMO1.pic}
\end{figure}


\textbf{\textit{Solution.}} Without loss of generality we can assume
that $AB\geq BC$.

Let $D$ be a point that satisfies the conditions of the task, or such that $ABCD$ is a tangent-chord quadrilateral (Figure \ref {sl.skk.4.5.IMO1.pic}). We denote by $a$, $b$, $c$ and $d$ the sides of $AB$, $BC$, $CD$ and $DA$ of this quadrilateral, and by $\alpha$, $\beta$, $\gamma$ and $\delta$ its internal angles at vertices $A$, $B$, $C$ and $D$. From the condition of the tangency of the quadrilateral $ABCD$ (formula \ref {TetivniPogoj}) it follows that $\delta = 180^0 - \beta$, and from its tangency (formula \ref {TangentniPogoj}) that $a + c = b + d$ or $d-c = a-b$. In this way, the task is reduced to the design of the third vertex $D$ of the triangle $ACD$, where the sides $AC$, the angle $\angle ADC = 180^0 - \beta$ and the difference of sides $AD-CD = AB-BC = a-b$ are given. Let $E$ be a point on the line $AD$, for which $DE \cong DC$. Then $AE = AD-DE = AD-CD = a-b$. The triangle $ECD$ is isosceles, so by formula \ref {enakokraki} it follows that $\angle CED \cong \angle DCE$. Therefore, $\angle AEC = 180^0 - \angle DEC = 180^0 - \frac {1}{2} \beta$. This allows us to construct the triangle $ACE$ or the point $E$.

First, we plan the point $E$ as the intersection of the arc $l$ (see the construction described in formula \ref {ObodKotGMT}) $180^0 - \frac {1}{2} \angle ABC$) and the circle $j (A, AB-BC)$ (if $AB \cong AC$, we assume $E = A$). The point $D$ can then be designed as the intersection of the strip $AE$ and the similitude $s_{EC}$ of the line $EC$ (in the case $AB \cong AC$, or $E = A$, $D$ is the second intersection of the similitude $s_{EC} = s_{AC}$ with the circle $k$).

We prove that the point $D$ satisfies the conditions of the task, or that $ABCD$ is a tangent-chord quadrilateral. First, we will consider the case when $AB>BC$.

By construction, the point $D$ lies on the line of symmetry $EC$, so $DE\cong DC$ and also (by statement \ref{enakokraki}) $\angle DEC\cong\angle DCE$. We have drawn the point $E$ so that it lies on the arc $l$ with the string $AC$ and the angular measure $180^0-\frac{1}{2}\angle ABC$, so $\angle AEC=180^0-\frac{1}{2}\angle ABC$. Because, by construction, $\mathcal{B}(A,E,D)$, we have $\angle DCE\cong\angle DEC=\frac{1}{2}\angle ABC$. From the isosceles triangle $EDC$ by statement \ref{VsotKotTrik} it follows that $\angle ADC=\angle EDC=180^0-\angle ABC$. Therefore, $\angle EDC+\angle ABC=180^0$, so by statement \ref{TetivniPogoj} the quadrilateral $ABCD$ is a string quadrilateral, or $D\in k$.

 We will now prove that the quadrilateral $ABCD$ is a tangent quadrilateral. In the first part of the proof (the string property) we have already seen that $DE\cong DC$. The point $E$ by construction lies on the circle $j(A,|AB-BC|)$, so $|AE|=|AB|-|BC|$. Because $\mathcal{B}(A,E,D)$ also holds, we have $|AD|-|CD|=|AD|-|DE|=|AE|=|AB|-|BC|$. From this it follows that $|AD|+|BC|=|AB|+|CD|$ and by statement \ref{TangPogoj} the quadrilateral $ABCD$ is tangent.

 If $AB\cong BC$, the point $D$ by construction already lies on the circle $k$. Because both points $B$ and $D$ lie on the line of symmetry $AC$, the quadrilateral $ABCD$ is a deltoid, so it is also tangent (by statement \ref{TangDeltoidRomb}).

 We will now investigate the number of solutions to the problem. The circle $k(A,AB-AC)$ and the arc $l$ always intersect in one point $E$. Because $ABC<180^0$, we have $\angle AEC=180^0-\frac{1}{2}\beta>90^0$. This means that the line of symmetry $s_{EC}$ always intersects the half-line $AE$ in one point $D$ and $\mathcal{B}(A,E,D)$ holds. This means that the problem always has one and only one solution.
  \kdokaz




  %______________________________________________________________________________
 \poglavje{Simson Line} \label{odd4Simson}

We will first prove the basic statement.

\bizrek \label{SimpsPrem}
The foots of the perpendiculars from an arbitrary point lying on the circumcircle of a triangle to the  lines containing the sides of this triangle  are three collinear points. The line containing these points is the so-called \pojem{Simson\footnote{Premico imenujemo po škotskem matematiku \index{Simson, R.} \textit{R. Simsonu} (1687--1768), čeprav je to lastnost prvi objavil škotski matematik \index{Wallace, W.}  \textit{W. Wallace} (1768--1843) šele leta 1799.} line}\color{blue}.
\eizrek

\begin{figure}[!htb]
\centering
\input{sl.skk.4.7.1a.pic}
\caption{} \label{sl.skk.4.7.1a.pic}
\end{figure}

\textbf{\textit{Proof.}} Let $S$ be an arbitrary point of the circumcircle $k$ of the triangle $ABC$ and $P$, $Q$ and $R$ the orthogonal projections of the point $S$ on the lines containing the sides $BC$, $AC$ and $AB$ (Figure \ref{sl.skk.4.7.1a.pic}). Without loss of generality, we assume that $\mathcal{B}(B,P,C)$, $\mathcal{B}(A,Q,C)$ and $\mathcal{B}(A,B,R)$ hold. In this case, the points $Q$ and $R$ are on different sides of the line $BC$, so it is enough to prove $\angle BPR \cong \angle CPQ$. Because of the appropriate right angles and the position of the point $S$, the quadrilaterals $BRSP$, $ABSC$, $ARSQ$ and $SPQC$ are cyclic, so (from izrek \ref{TetivniPogoj}:
\begin{eqnarray*}
 \angle BPR &=& \angle BSR = \angle RSC - \angle BSC=\\
&=& \angle RSC - (180° - \angle BAC) =\\
&=& \angle RSC - \angle RSQ = \angle CSQ = \angle CPQ,
 \end{eqnarray*}
which means that the points $P$, $Q$ and $R$ are collinear. \kdokaz

In the following we will consider further interesting properties of Simson's line. Because each point $X$, which lies on the circumcircle of some triangle, determines the Simson line, we will denote this line by $x$. In this way, each triangle determines one mapping $X\mapsto x$.

\bzgled \label{SimsZgled1}
            Let $P$ be an arbitrary point of the circumcircle $k$ of a triangle
            $ABC$. Suppose that $P_A$ is the intersection of the perpendicular line of
            the line $BC$ through the point $P$ with the circle $k$.
            Prove that the line $AP_A$ is parallel to the Simson line $p$
            of the triangle at the point $P$.
            \ezgled


\begin{figure}[!htb]
\centering
\input{sl.skk.4.7.1b.pic}
\caption{} \label{sl.skk.4.7.1b.pic}
\end{figure}

 \textbf{\textit{Proof.}}
 Let $X$, $Y$ and $Z$ be the orthogonal projections of the point $P$ on the lines
  $BC$, $AC$ and $AB$ (Figure \ref{sl.skk.4.7.1b.pic}). By izreku \ref{SimpsPrem} the Simson line
  $p$ is determined by the points $X$, $Y$ and $Z$. Similarly to izreku
  \ref{SimpsPrem},
the quadrilateral $PYXC$ is a trapezoid, therefore $\angle YXP \cong \angle ACP$.
By izreku \ref{ObodObodKot} the angles $ACP$ and $AP_AP$ above
the trapezoid $AP$ are supplementary, therefore $\angle YXP \cong \angle AP_AP$
or $XY\parallel AP$ (izrek \ref{KotiTransverzala}).
  \kdokaz



            \bzgled \label{SimsZgled2}
            Let $P$ and $Q$ be arbitrary points lying on the circumcircle
            $k(O,r)$ of a triangle $ABC$ and $p$ and $q$ their Simson lines. Prove that
             $$\angle pq = \frac{1}{2}\angle POQ.$$
           \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.7.1c.pic}
\caption{} \label{sl.skk.4.7.1c.pic}
\end{figure}

\textbf{\textit{Proof.}}
  Let $X_P$ and $X_Q$ be the feet of the perpendiculars from points $P$ and $Q$
   on the line $BC$ and $P_A$ and $Q_A$
the intersections of these perpendiculars with the circle $k$ (Figure
\ref{sl.skk.4.7.1c.pic}). The Simson lines $p$ and $q$ are parallel to the lines $AP_A$ and $AQ_A$ (example \ref{SimsZgled1}).
Therefore, the angle determined by the lines $p$ and $q$ is equal to the inscribed angle $Q_AAP_A$, which is equal to half of the central angle $Q_AOP_A$
(by statement \ref{SredObodKot}) or half of the angle $QOP$ (because the trapezoid $PP_AQ_AQ$ is isosceles and by statement \ref{trapezTetivEnakokr} it is also equilateral, i.e. $PQ \cong P_AQ_A$).
 \kdokaz


            \bzgled \label{SimsZgled3}
            Let $P$ be an arbitrary point of the circumcircle $k$ of a triangle
            $ABC$, $p$ its Simson line and $V$ the orthocentre of this triangle.
             Prove that the line $p$ bisects the line segment $PV$.
            \ezgled

\begin{figure}[!htb]
\centering
\input{sl.skk.4.7.1d.pic}
\caption{} \label{sl.skk.4.7.1d.pic}
\end{figure}

 \textbf{\textit{Proof.}}
Let $P_A$ and $X$ be the points defined as in example
\ref{SimsZgled1} (Figure \ref{sl.skk.4.7.1d.pic}). Let $V'$
and $P'$ be the points that are symmetric to the points $V$ and $P$ with respect to the line $BC$. The point $V'$ lies on the circumscribed circle $k$ of the triangle $ABC$
(by statement \ref{TockaV'}). Because of the properties of symmetry
or the axis of reflection (see subsection \ref{odd6OsnZrc}), statement
\ref{KotiTransverzala}, statement \ref{ObodObodKot} and example
\ref{SimsZgled1} it holds:
   $$\angle VP'P\cong\angle V'PP'\cong\angle AV'P
   \cong\angle AP_AP\cong\angle p,PP'.$$
 Therefore, $\angle VP'P \cong \angle p,PP'$, so by statement
 \ref{KotiTransverzala} the lines $VP'$ and $p$ are parallel. Because
the point $X$ is the midpoint of the segment $PP'$, the line $p$ contains the midpoint
of the triangle $PVP'$ (by statement \ref{srednjicaTrik}) or the midpoint of its
side $PV$.
 \kdokaz

In sections \ref{odd5Hamilton} and \ref{odd7SredRazteg} we will prove two more properties
of Simson lines (see \ref{HamiltonSimson} and \ref{SimsEuler}), which are related to Hamilton's theorem or
Euler's circle of a triangle.




%________________________________________________________________________________
 \poglavje{Torricelli Point} \label{odd4Torricelli}

In this section we will give another famous point of a triangle.


             \bizrek \label{izrekTorichelijev}
             On each side of a triangle $ABC$ the equilateral triangles $BEC$, $CFA$ and $AGB$
             are externally erected. Prove:
            \begin{enumerate}
              \item $AE$, $BF$ and $CG$ are congruent line segments;
              \item the lines $AE$, $BF$ and $CG$ intersect at one point
              (so-called \pojem{Torricelli\footnote{Problem was first posed by French mathematician \index{Fermat, P.} \textit{P.
            Fermat} (1601--1665) as a challenge to Italian mathematician and physicist \index{Torricelli, E.} \textit{E.
            Torricelli} (1608--1647). Torricelli's solution was published by his student - Italian mathematician and physicist \textit{V. Viviani} (1622–-1703) - in 1659. We also call this point \index{point!Fermat's}\pojem{Fermat
            point}.}
             point} \color{blue}of this triangle) and every two of them determine an angle with measure $60^0$.
            \end{enumerate}
             \index{point!Torricelli's}
            \eizrek


\begin{figure}[!htb]
\centering
\input{sl.skk.4.7.1.pic}
\caption{} \label{sl.skk.4.7.1.pic}
\end{figure}

 \textbf{\textit{Proof.}}
  (Figure \ref{sl.skk.4.7.1.pic})

 (\textit{i}) Triangles $AEC$ and $FBC$ are congruent by \textit{SAS} \ref{SKS} theorem ($AC \cong FC$ , $CE \cong CB$ and
$\angle ACE \cong \angle FCB = \angle ACB + 60°$), so $AE\cong BF$. Analogously is $AE\cong CG$.

(\textit{ii}) Let $k$, $l$ and $j$ be the circumscribed circles of the triangles $BEC$, $CFA$ and $AGB$. We shall first prove that these circles intersect in one point. With $T$ we denote the second intersection point of the circles $k$ and $l$ ($T\neq C$). The quadrilaterals $BECT$ and $CFAT$ are cyclic, therefore (by the statement \ref{TetivniPogoj}) both the angles $BTC$ and $ATC$ measure $120^0$. Thus, also the angle $ATB$ measures $120^0$, which means that the quadrilateral $AGBT$ is cyclic (by the statement \ref{TetivniPogoj}) or that the point $T$ also lies on the circle $j$.

We shall prove that each of the lines $AE$, $BF$, $CG$ goes through the point $T$. From the equality of the corresponding
circumscribed angles (by the statement \ref{ObodObodKot}) we obtain:

\begin{eqnarray*}
\angle ATE&=&\angle ATF+\angle FTC+\angle CTE=\\
&=&\angle ACF+\angle FAC+\angle CBE
=3\cdot 60^0=180^0.
\end{eqnarray*}

Thus, $A$, $T$ and $E$ are collinear points, or the point $T$ lies on the line $AE$. Analogously, the point $T$ also
lies on the lines $BF$ and $CG$. It is also clear that:
$\angle AE,BF\cong\angle ATF\cong\angle ACF=60^0$.
 \kdokaz

  In the section \ref{odd9MetrInv} (by the statement \ref{izrekToricheliFerma}) we shall prove another interesting property of the Torricelli's point.


%________________________________________________________________________________
 \poglavje{Excircles of a Triangle} \label{odd4Pricrt}

 We have already proved that for any triangle there exist
 circumscribed and inscribed circle. The first one contains all the vertices
of the triangle, the second one touches all its sides. Now we shall
show that there also exist circles which touch one side
and two lines containing the sides of the triangle.


            \bizrek
            The bisector of the interior angle at vertex $A$ and the bisectors of
            the exterior angles at vertices $B$ and $C$ of a triangle $ABC$ intersect at one point,
            which is the centre of the circle touching the side $BC$ and the lines containing the sides $AB$ and
            $AC$. It is so-called \index{pričrtane krožnice trikotnika} \pojem{excircle of the triangle}\color{blue}.
            \eizrek



\begin{figure}[!htb]
\centering
\input{sl.27.1.94_veliki_zadatak_lema.pic}
\caption{} \label{sl.27.1.94_veliki_zadatak_lema.pic}
\end{figure}

\textbf{\textit{Proof.}} We prove the statement similarly to the inscribed circle of a triangle. The simetrali
of the external angles at the vertices $B$ and $C$ are not parallel and they
intersect at some point - we mark it with $S_a$ (Figure
\ref{sl.27.1.94_veliki_zadatak_lema.pic}). Because the point $S_a$ lies on
these two simetrali, it holds $A,S_a\div BC$ and $S_a$ is equally distant from the lines $AB$, $BC$ and
$AC$. Therefore, $S_a$ also belongs to the simetral of the internal angle at
the vertex $A$ and is the center of the circle that touches the side $BC$ and
the lines $AB$ and $AC$.
 \kdokaz

 Now we are ready to prove the so-called \index{velika naloga}
  \pojem{‘‘velika naloga’’}, which is very useful in
 designing triangles.




              \bizrek \label{velikaNaloga}
              Let $P$, $Q$, $R$ be the touching points of the incircle $k(S,r)$
               of a triangle $ABC$ with the sides $BC=a$, $AC=b$, $AB=c$ ($b>c$) and $P_i$, $Q_i$, $R_i$
                ($i\in \{a,b,c\}$) the touching points of the excircles
              $k_i(S_i,r_i)$ with lines $BC$, $AC$ in $AB$. Let $l(O,R)$
               be the circumcircle of this triangle with the semiperimeter
                $s=\frac{a+b+c}{2}$, $A_1$ the midpoint of the line segments $BC$, $M$ and $N$,
                intersections of the line $OA_1$ with the circle $l$ ($N,A\div BC$) and
                $M’$, $N’$ the foots of the perpendiculars  from these points on the line $AB$ (Figure
                \ref{sl.27.1.94_veliki_zadatak.pic}). Then:
                \vspace*{2mm}

                (\textit{i}) $AQ_a\cong AR_a=s$, \hspace*{0.4mm} (\textit{ii})
                $AQ\cong AR=s-a$, \hspace*{0.4mm} (\textit{iii}) $QQa\cong RRa\cong a$,
                % \vspace*{1mm}

(\textit{iv}) $PPa=b-c$,\hspace*{1mm}
                (\textit{v}) $P_bP_c=b+c$,
                % \vspace*{1mm}

                 (\textit{vi})
                  $A_1$ is the midpoint of the line segment $PP_a$ in $P_bP_c$,
                %\vspace*{1mm}

                 (\textit{vii}) $A_1N= \frac{r_a- r}{2}$,\hspace*{2mm}
               (\textit{viii}) $A_1M= \frac{r_b + r_c }{2} $,\hspace*{1mm}


              (\textit{ix}) $r_a +r_b +r_c =4R+r$,\footnote{To lastnost
               trikotnika je leta 1790 odkril francoski matematik \index{L'Huilier, S. A. J.}
                \textit{S. A. J. L'Huilier}
               (1750--1840).}
             %\vspace*{1mm}

                (\textit{x}) $NN’= \frac{r_a +r}{2}$, \hspace*{1mm} (\textit{xi})
                $MM’= \frac{r_b -r_c }{2 }$,\hspace*{1mm} (\textit{xii})
                $N’B\cong AM’=\frac{ b - c}{2}$,
                % \vspace*{1mm}

                (\textit{xiii}) $AN’\cong BM’= \frac{b + c}{2} $, \hspace*{1mm} (\textit{xiv}) $M’N’\cong b$.
                 \eizrek


\begin{figure}[!htb]
\centering
\input{sl.27.1.94_veliki_zadatak.pic}
\caption{} \label{sl.27.1.94_veliki_zadatak.pic}
\end{figure}

 \textbf{\textit{Proof.}}
  Preden začnemo z dokazovanjem, omenimo, da po izreku \ref{TockaN}
  točka $N$ leži na simetrali notranjega kota $BAC$ trikotnika
  $ABC$.

(\textit{i}) If we use the equality of tangent lines
  (statement \ref{TangOdsek}), we get:
 \begin{eqnarray*}
 AQ_a&\cong &AR_a= \frac{1}{2}\left(AQ_a+AR_a\right)=
 \frac{1}{2}\left(AB+BR_a+AC+CQ_a\right)\\
 &=& \frac{1}{2}\left(AB+BP_a+AC+CP_a\right)=
\frac{1}{2}\left(AB+BC+AC\right)=s.
 \end{eqnarray*}

 (\textit{ii}) In a similar way, we get:
 \begin{eqnarray*}
 AQ&\cong &AR= \frac{1}{2}\left(AQ+AR\right)=
 \frac{1}{2}\left(AB-BR+AC-CQ\right)\\
 &=& \frac{1}{2}\left(AB-BP+AC-CP\right)=
\frac{1}{2}\left(AB+AC-BC\right)=s-a.
 \end{eqnarray*}

 (\textit{iii}) $QQ_a\cong AQ_a-AQ=a$.

 (\textit{iv}) We prove the equality by first calculating:\\ $BP$ and $CP_a\cong CQ_a$.

 (\textit{v}) $P_bP_c\cong CP_c+BP_b-a=2s-a=b+c$.

 (\textit{vi}) It follows from $BP\cong CP_a=s-b$.

 (\textit{vii}) Points $A_1$ and $N$ are the centers of the diagonal of trapezoid
 $SPS_aP_a$ with
 bases $SP\cong r$ and
$S_aP_a\cong r_a$. The equality follows
from statement \ref{srednjTrapez}.

 (\textit{viii}) Lines $NA$ and $S_cS_b$
  are perpendicular (the internal
 and external angles at point
$A$ are symmetrical), so point $M$ lies on line $S_cS_b$. The desired equality follows
from the fact that line $A_1M$ is the median of trapezoid
$S_cP_cP_bS_b$ (statement \ref{srednjTrapez}).

 (\textit{ix}) It follows directly from $2\cdot R=NM=NA_1+A_1M$ and
 (\textit{vii}) and (\textit{viii}).

(\textit{x}) It follows from statement \ref{srednjTrapez} and the fact that 
$NN'$ is the median of trapezoid $SRR_aS_a$.

(\textit{xi}) Points $M$ and $M'$ are the centers of the diagonal of trapezoid
$R_cS_cR_bS_b$ with bases $R_cS_c\cong r_c$ and $R_bR_b\cong r_b$. The equality
follows from statement \ref{srednjTrapez}.

 (\textit{xii}) Point $N$ is the center of line $RR_a$, so:
  $$N'B=AN'-AB= \frac{1}{2}\left(AR_a+AR\right)-c=
  \frac{1}{2}\left(s+(s-a)\right)-c= \frac{1}{2}\left(b-c\right).$$

(\textit{xiii}) and (\textit{xiv}) follow
  directly from the proven equality (\textit{xii}).
 \kdokaz

%KONSTRUKCIJA (VN)

        \bzgled
         Construct a triangle $ABC$,  with given:

         (\textit{a}) $a$, $b-c$, $r$, \hspace*{3mm} (\textit{b})
        $b-c$, $r$, $v_b$, \hspace*{3mm} (\textit{c})  $a$, $b+c$, $r$,
        \hspace*{3mm}(\textit{č}) $R$, $r$, $r_a$.
         \ezgled



\textbf{\textit{Solution.}}
 For each construction we will use the big task - \ref{velikaNaloga}.
 We will use
  the same labels.

\begin{figure}[!htb]
\centering
\input{sl.27.1.94_veliki_zadatak_konstr.pic}
\caption{} \label{sl.27.1.94_veliki_zadatak_konstr.pic}
\end{figure}

\begin{figure}[!htb]
\centering
\input{sl.27.1.94_veliki_zadatak_konstr2.pic}
\caption{} \label{sl.27.1.94_veliki_zadatak_konstr2.pic}
\end{figure}



(\textit{a}) Because $PP_a=b-c$ and point $A_1$ is the common center
of side
 $BC$ and
 the line $PP_a$, it also holds that $PA_1 = \frac{1}{2}( b - c)$ (Figure
\ref{sl.27.1.94_veliki_zadatak_konstr.pic}).
First, we plan the side $BC$, then its center
$A_1$, point $P$, the inscribed circle of the triangle, tangents from
the vertices $B$ and $C$, and finally the vertices $A$.



(\textit{b}) Similarly to the previous example. First, we plan
the line $PA_1$, then the inscribed circle of the triangle $ABC$ (Figure
\ref{sl.27.1.94_veliki_zadatak_konstr.pic}).
We also need to use the condition of the height from the vertex $B$. With $L$
we mark the orthogonal projection from the point $A_1$ onto the line $AC$.
The line $A_1L$ is the median of the triangle $CBB'$, so $A_1L
=\frac{1}{2}BB'=\frac{1}{2} v_b$. Therefore, the line $AC$ can
be constructed as the common tangent of the inscribed circle and the circle
$k(A_1, \frac{1}{2}v_b)$. Thus we get the vertex $C$, then the vertices $B$ and $A$.

(\textit{c}) We know that $RR_a\cong a$ and $AN'=\frac{1}{2}(b+c)$, and that $N'$ is the center of the line $RR_a$ (Figure \ref{sl.27.1.94_veliki_zadatak_konstr2.pic}). So, from the given
data,
 we first construct the points $A$, $N'$, $R$ and $R_a$, and then also $S$, $N$
  and
$S_a$. In the end, we draw the dotted and the dashed circle -
the sides of the triangle lie on their common tangents.


(\textit{č}) Because $A_1N =\frac{1}{2}(r_a -r)$ and $MN = 2R$, we can
first plan the points $N$, $A_1$ and $M$, and then also the dotted
circle of the triangle $ABC$ and the side $BC$ (Figure \ref{sl.27.1.94_veliki_zadatak_konstr2.pic}). The construction can
be finished in two ways. In the first case, we translate the task into a construction of a triangle that we already know: $a$, $R$, $r$ (example \ref{konstr_Rra}), in
the second case, we use the equality $RR_a\cong a$.
 \kdokaz




%________________________________________________________________________________
\naloge{Exercises}

\begin{enumerate}

\item   The sides of a triangle are $6$, $7$ and $9$. Let $k_1$, $k_2$ and $k_3$ be the circles with centers
in the vertices of this triangle. The circles touch each other so that
 the circle with the center in the vertex of the smallest angle of the triangle touches the other two circles from the inside,
while the remaining two circles touch from the outside. Calculate the lengths of the radii of these three circles.

\item Prove that the angle formed by the secants of a circle that intersect each other outside the circle is equal to half the difference of the central angles corresponding to the arcs that lie between the arms of this angle.

\item   The apex of the angle $\alpha$ is an external point of the circle $k$. Between the arms of this angle, on the circle, there are two
arcs, which are in the ratio $3:10$. The larger of these arcs corresponds to the central angle $40^0$. Determine
the measure of the angle $\alpha$.

\item  Prove that the angle formed by the tangents of a circle is equal to half the difference of the central angles corresponding to the arcs that lie between the arms of this angle.

\item Let $L$ be the orthogonal projection of an arbitrary point $K$ of the circle $k$
on its tangent $t$ through the point $T\in k$ and $X$ the point that is
symmetric to the point $L$ with respect to the line $KT$. Determine the geometric
position of the points $X$.

\item Let $BB'$ and $CC'$ be the altitudes of the triangle $ABC$ and $t$
the tangent of this triangle at the point $A$. Prove that
 $B'C'\parallel t$.

\item In the right triangle $ABC$ is above the cathetus $AC$ as the diameter
drawn circle that intersects the hypotenuse $AB$ at the point $E$. The tangent of this
circle at the point $E$ intersects the other cathetus $BC$ at the point $D$. Prove that $BDE$
is an isosceles triangle.

\item In the right angle with the vertex $A$ is drawn a circle that touches the sides of this angle
at the points $B$ and $C$. Any tangent of this circle intersects the lines $AB$ and $AC$, in order
in the points $M$ and $N$ (so that $\mathcal{B}(A,M,B)$). Prove that:
$$\frac{1}{3}\left(|AB|+|AC|\right) < |MB|+|NC| <
\frac{1}{2}\left(|AB|+|AC|\right).$$

\item Prove that in the right triangle the sum of the sides is equal to the sum
of the diameters of the inscribed and drawn circle.

\item Let the similitudes of the internal angles of the convex quadrilateral intersect in six different points.
Prove that four of these points are the vertices of the pedal quadrilateral.

\item Let: $c$ be the length of the hypotenuse, $a$ and $b$ the lengths
of the catheti and $r$ the radius of the inscribed circle of the right triangle. Prove that:
\begin{enumerate}
 \item $2r + c \geq 2 \sqrt{ab}$, \item $a + b + c > 8r$.
\end{enumerate}

\item Let $P$ and $Q$ be the centers of the shorter arcs $AB$ and $AC$
of the regular triangle $ABC$ of the drawn circle. Prove that the sides $AB$ and $AC$ of this triangle divide
the chord $PQ$ into three proportional segments.

\item Let $k_1$, $k_2$, $k_3$, $k_4$ be four circles, each of which from the outside touches one side   and two sides of an arbitrary convex
quadrilateral. Prove that the centers of these circles are concircular points.

\item Circles $k$ and $l$ touch each other from the outside in point $A$. Points $B$ and $C$ are the points of contact of the common external tangent of these two circles. Prove that $\angle BAC$ is a right angle.

\item Let $ABCD$ be a deltoid ($AB\cong AD$ and $CB\cong CD$). Prove:
\begin{enumerate}
 \item $ABCD$ is a tangent quadrilateral,
 \item  $ABCD$ is a parallelogram exactly when $AB\perp BC$.
\end{enumerate}

\item Circles $k$ and $k_1$ touch each other from the outside in point $T$, where they intersect lines $p$ and $q$. Line $p$ has two more intersections with the circles, $P$ and  $P_1$, line $q$ has $Q$ and $Q_1$.  Prove that $PQ\parallel P_1Q_1$.

\item Let $MN$ be the common tangent of circles $k$ and $l$ ($M$ and $N$ are the points of contact), which intersect in points $A$ and $B$. Calculate the measure of the sum $\angle MAN+\angle MBN$.

\item Let $t$ be the tangent of triangle $ABC$ of the circumscribed circle in point $A$. A line parallel to the tangent $t$ intersects sides $AB$ and $AC$ in points $D$ and $E$.
Prove that points $B$, $C$, $D$ and $E$ are concyclic.

\item Let $D$ and $E$ be any points of the semicircle drawn over diameter $AB$. Let $AD\cap BE= \{F\}$ and $AE\cap BD= \{G\}$.
Prove that $FG\perp AB$.

\item Let $M$ be a point of circle $k(O,r)$. Determine the geometric location of the centers of all the tangents of this circle that have one endpoint in point $M$.

\item Let $M$ and $N$ be points that are symmetric to the vertex $A'$ of altitude $AA'$ of triangle $ABC$ with respect to side $AB$ and $AC$, and let $K$ be the intersection of lines $AB$ and $MN$. Prove that points $A$, $K$, $A'$, $C$ and $N$ are concyclic.

\item Let $ABCD$ be a parallelogram, $E$ the altitude point of triangle $ABD$, and $F$ the altitude point of triangle $ABC$. Prove that quadrilateral $CDEF$
is a parallelogram.

\item Circles with centers $O_1$ and $O_2$ intersect in points $A$ and $B$. The line $p$,
which goes through point $A$, intersects these two circles in points $M_1$ and $M_2$. Prove that
$\angle O_1M_1B\cong\angle O_2M_2B$.

\item The circle with center $O$ is drawn over the diameter $AB$.
Let $C$ and $D$ be such points on the line $AB$, that $CO\cong OD$. Parallel lines through points $C$ and $D$ intersect the circle in points $E$ and $F$.
Prove that lines $CE$ and $DF$ are perpendicular to the line $EF$.

\item On the string $AB$ of the circle $k$ with center $O$ lies the point $C$, point $D$ is the other intersection of the circle $k$ with the drawn circle of the triangle $ACO$. Prove that
$CD\cong CB$.

\item Let $AB$ be the transversal of the circle $k$. Lines $AC$ and $BD$ are tangents
to the circle $k$ in points $C$ and $D$.
Prove that:
 $$||AC|-|BD||< |AB| < |AC|+|BD|.$$

\item Let $S$ be the intersection of the sides $AD$ and $BC$
of the trapezoid $ABCD$ with the base $AB$. Prove that the drawn circles of the triangles $SAB$ and
$SCD$ touch in point $S$.

\item Lines $PB$ and $PD$ touch the circle $k(O,r)$ in points $B$ and $D$.
Line $PO$ intersects the circle $k$ in points $A$ and $C$ ($\mathcal{B}(P,A,C)$). Prove that the
line $BA$ is the angle bisector of the angle $PBD$.

\item Quadrilateral $ABCD$ is inscribed in the circle with center $O$. Diagonals $AC$ and
$BD$ are perpendicular. Let $M$ be the perpendicular projection of the center $O$
on the line $AD$. Prove that
 $$|OM|=\frac{1}{2}|BC|.$$

\item Lines $AB$ and $BC$ are adjacent sides of a regular nonagon, which is inscribed in the circle $k$ with center $O$.
Point $M$ is the center of the side $AB$, point $N$ is the center
of the radius $OX$ of the circle $k$, which is perpendicular to the line $BC$. Prove that
$\angle OMN=30^0$.

\item Circles $k_1$ and $k_2$ intersect in points $A$ and $B$. Let $p$ be a line that goes through point $A$, circle $k_1$ intersects also in point $C$, circle $k_2$ intersects also in point $D$, and $q$ be a line that goes through point $B$, circle $k_1$ intersects also in point $E$, circle $k_2$ intersects also in point $F$. Prove that $\angle CBD\cong\angle EAF$.

\item Circles $k_1$ and $k_2$ intersect in points $A$ and $B$. Draw a line $p$, that goes through point $A$, so that the length of the line $MN$, where $M$ and $N$ are the intersections of line $p$ with circles $k_1$ and $k_2$, is maximal.

\item Let $L$ be the orthogonal projection of an arbitrary point $K$ of the circle $k$ on its tangent through the point $T\in k$ and $X$ be the point that is symmetric to the point $L$ with respect to the line $KT$. Determine the geometric position of the points $X$.

\item Prove that the string polygon with an even number of vertices, that has all the internal angles congruent, is a regular polygon.

\item Two circles touch each other from the inside in the point $A$. The line $AB$ is the diameter of the larger circle, the string $BK$ of the larger circle touches the smaller circle in the point $C$. Prove that the line $AC$ is the bisector of the angle $BAK$.

\item Let $BC$ be the string of the circle $k$. Determine the geometric position of the altitude points of all the triangles $ABC$, where $A$ is an arbitrary point that lies on the circle $k$.

\item We have a quadrilateral with three acute internal angles. Prove that the longer diagonal goes through the vertex that belongs to the acute angle.

\item Let $ABCDEF$ be a string hexagon, $AB\cong DE$ and $BC\cong EF$. Prove that $CD\parallel AF$.

\item Let $ABCD$ be a convex quadrilateral, where $\angle ABD=50^0$, $\angle ADB=80^0$, $\angle ACB=40^0$ and $\angle DBC=\angle BDC +30^0$. Calculate the measure of the angle $\angle DBC$.

\item Let $M$ be an arbitrary internal point of the angle with the vertex $A$, points $P$ and $Q$ the orthogonal projections of the point $M$ on the sides of this angle, and point $K$ the orthogonal projection of the vertex $A$ on the line $PQ$. Prove that $\angle MAP\cong \angle QAK$.

\item In the archery octagon $A_1A_2\ldots A_8$ it holds that $A_1A_2\parallel A_5A_6$, $A_2A_3\parallel A_6A_7$,
$A_3A_4\parallel A_7A_8$. Prove that $A_8A_1\cong A_4A_5$.

\item A circle intersects each side of a quadrilateral in two points and thus on all sides of the quadrilateral it determines the consistent tautologies.
Prove that this quadrilateral is tangent.

\item The lengths of the sides of the tangent pentagon $ABCDE$ are natural numbers and at the same time $|AB|=|CD|=1$.
The inscribed circle of the pentagon touches the side $BC$ in the point $K$.
Calculate the length of the line $BK$.

\item Prove that the circle that passes through the adjacent vertices $A$ and $B$ of the regular
pentagon $ABCDE$ and its center $O$, also passes through the intersection
of its diagonals $AD$ and $BE$.

\item Let $H$ be the altitude point of the triangle $ABC$, $l$ the circle above  the diameter $AH$
and $P$ and $Q$ the intersections of this circle with the sides $AB$ and $AC$. Prove that the
tangents of the circle $k$ through the points $P$ and $Q$ intersect on the side $BC$.

\item The circle $l$ touches the circle $k$ from the inside in the point $C$. Let $M$ be any point
of the circle $l$ (different from $C$). The tangent of the circle $l$ in the point $M$ intersects the circle $k$ in
the points $A$ and $B$. Prove that $\angle ACM \cong \angle MCB$.

\item Let $k$ be the inscribed circle of the triangle $ABC$ and $R$ the center of that arc $AB$ of this circle,
which does not contain the point $C$. The lines $RP$ and $RQ$ are the tautologies of this circle. The first one
is parallel, the second one is perpendicular to the internal angle  $\angle BAC$. Prove:
\begin{enumerate}
\item The line $BQ$ is the internal angle $\angle CBA$,
\item  The triangle, which is determined by the lines $AB$, $AC$ and $PR$, is a right triangle.
 \end{enumerate}

\item Let $X$ be such an internal point of the triangle $ABC$, that it holds:
 $\angle BXC =\angle BAC+60^0$,  $\angle AXC =\angle ABC+60^0$ and  $\angle AXB =\angle AC B+60^0$. Let
$P$, $Q$ and $R$ be the other intersections of the lines $AX$, $BX$ and $CX$ with the inscribed circle of the triangle $ABC$. Prove that the  triangle $PQR$ is a right triangle.

\item Prove that the tangent points of an inscribed circle of a triangle $ABC$ divide its sides into segments of lengths $s-a$, $s-b$ and $s-c$ ($a$, $b$ and $c$ are the lengths of the sides, $s$ is the semi-perimeter of the triangle).


 \item Circles $k$, $l$ and $j$ touch each other from the outside in non-linear points $A$, $B$ and $C$. Prove that the circumscribed circle of the triangle $ABC$ is perpendicular to the circles $k$, $l$ and $j$.


 \item Let $ABCD$ be a square with the center of the circumscribed circle in the point $O$. With $E$ we denote the intersection of its diagonals $AC$ and $BD$ and with $F$, $M$ and $N$ the centers of the lines $OE$, $AD$ and $BC$. If $F$, $M$ and $N$ are collinear points, then $AC\perp BD$ or $AB\cong CD$. Prove.



\item Draw a triangle $ABC$ (see the labels in section \ref{odd3Stirik}):

 (\textit{a}) $a$, $\alpha$, $r$, \hspace*{2mm}
 (\textit{b}) $a$, $\alpha$, $r_a$, \hspace*{2mm}
 (\textit{c}) $a$, $v_b$, $v_c$, \hspace*{2mm}

 (\textit{d}) $\alpha$, $v_a$, $s$, \hspace*{2mm}
 (\textit{e}) $v_a$, $l_a$, $r$, \hspace*{2mm}
(\textit{f}) $\alpha$, $v_a$, $l_a$, \hspace*{2mm}

 (\textit{g}) $\alpha$, $\beta$, $R$, \hspace*{2mm}
 (\textit{h}) $c$, $r$, $R$, \hspace*{2mm}
 (\textit{i}) $a$, $v_b$, $R$, \hspace*{2mm}

 \item Draw a circle $k$ so that:

  \begin{enumerate}
    \item it touches two given non-parallel lines $p$ and $q$, and the tangent that determines the touch points is consistent with the given distance $t$,
    \item its center is the given point $S$, and the given line $p$ determines on it the tangent that is consistent with the given distance $t$,
    \item it passes through the given points $A$ and $B$, and its center lies on the given circle $l$,
    \item it has the given radius $r$ and it touches the two given circles $l$ and $j$,
    \item it touches the line $p$ in the point $P$ and passes through the given point $A$.
  \end{enumerate}

  \item Draw a square $ABCD$, if the given vertex $B$ and two points $E$ and $F$ that lie on the sides $AD$ and $CD$ are given.

\item Given is a line $CD$ and points $A$ and $B$ ($A,B\notin CD$). On the line $CD$ draw a point $M$, such that $\angle AMC\cong2\angle BMD$.


  \item Draw a triangle $ABC$ with the following data:

   (\textit{a}) $v_a$, $t_a$, $\beta-\gamma$, \hspace*{2mm}
   (\textit{b}) $v_a$, $l_a$, $R$, \hspace*{2mm}
   (\textit{c}) $R$, $\beta-\gamma$, $t_a$, \hspace*{2mm}

   (\textit{d}) $R$, $\beta-\gamma$, $v_a$, \hspace*{2mm}
   (\textit{e}) $R$, $\beta-\gamma$, $a$. \hspace*{2mm}


\item On the beam of the side $AB$ of the rectangle $ABCD$ draw a point $E$, from which the sides $AD$ and $DC$ are seen under the same angle. When does the task have a solution?

    \item In the convex quadrilateral $ABCD$ it holds that $BC\cong CD$. Draw this quadrilateral, if the sides $AB$ and $AD$ and the internal angle at the vertices $B$ and $D$ are given.

    \item In the given circle $k$ draw a triangle $ABC$, if the vertex $A$, the line $p$, which is parallel to the altitude $AA'$, and the intersection point $B_2$ of the altitude beam $BB'$ and this circle are given.

    \item Draw a regular triangle $ABC$, if its side $BC$ is congruent to the distance $a$, the altitude beams of the sides $AB$ and $AC$ and the line of symmetry of the internal angle $BAC$ go through the given points $M$, $N$ and $P$ one after another.

\item Draw a triangle $ABC$, if the following are given:
  \begin{enumerate}
    \item the vertex $A$, the center of the circumscribed circle $O$ and the center of the inscribed circle $S$,
    \item the center of the circumscribed circle $O$, the center of the inscribed circle $S$ and the center of the escribed circle $S_a$,
    \item the vertex $A$, the center of the circumscribed circle $O$ and the altitude point $V$,
    \item the vertices $B$ and $C$ and the internal angle bisector of the internal angle $BAC$,
    \item the vertex $A$, the center of the circumscribed circle $O$ and the intersection point $E$ of the side $BC$ with the internal angle bisector of the internal angle $BAC$,
    \item the points $M$, $P$ and $N$, in which the altitude and the centroid from the vertex $A$ and the internal angle bisector of the internal angle $BAC$ intersect the circumscribed circle of the triangle,
    \item the vertex $A$, the center of the circumscribed circle $O$, the point $N$, in which the internal angle bisector of the internal angle $BAC$ intersects the circumscribed circle of the triangle, and the distance $a$, which is parallel to the side $BC$.
  \end{enumerate}

  \item Draw a triangle $ABC$ with the following data:

   (\textit{a}) $a$, $b$, $\alpha=3\beta$, \hspace*{3mm}
   (\textit{b}) $t_a$, $t_c$, $v_b$.\hspace*{3mm}

\item Through the point $M$, which lies inside the given circle $k$, draw such a cord that the difference of its segments (from the point $M$) is equal to the given distance $a$.

\item Draw a triangle $ABC$, if you know:

 (\textit{a}) $b-c$, $r$, $r_a$, \hspace*{1.8mm}
 (\textit{b}) $a$, $r$, $r_a$, \hspace*{1.8mm}
 (\textit{c}) $a$, $r_b+r_c$, $v_a$, \hspace*{1.8mm}
 (\textit{d}) $b+c$, $r_b$, $r_c$,

 (\textit{e}) $R$, $r_b$, $r_c$, \hspace*{1.8mm}
 (\textit{f}) $b$, $R$, $r+r_a$, \hspace*{1.8mm}
(\textit{g}) $a$, $v_a$, $r_a-r$, \hspace*{1.8mm}
 (\textit{h}) $\alpha$, $r$, $b+c$.


 \item The following are given: the circle $k$, its diameter $AB$ and the point $M\notin k$. With only a straightedge, draw a rectangle from the point $M$ to the line $AB$.

\item The given are: square $ABCD$ and such points $M$ and $N$ on sides $BC$ and $CD$, that $\angle MAN=45^0$.
 With only a straightedge draw a rectangle from point $A$ to line $MN$.

\end{enumerate}





% DEL 5 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
%________________________________________________________________________________
% VEKTORJI
%________________________________________________________________________________

  \del{Vectors} \label{pogVEKT}


%________________________________________________________________________________
\poglavje{Vector Definition. The Sum of Vectors} \label{odd5DefVekt}

Intuitively, a vector is a directed line segment that can be moved parallel\footnote{The concept of a vector was known to the ancient Greeks. The modern concept of vectors, associated with linear algebra and analytic geometry, began to develop in the 19th century as a generalization of complex numbers. In this sense, the English mathematician \index{Hamilton, W. R.}\textit{W. R. Hamilton} (1805--1865) defined the so-called \index{quaternions}\textit{quaternions} $q = w + ix + jy + kz$, $i^2 = j^2 = k^2 = -ijk = -1$ as a generalization of complex numbers in four-dimensional space}. In this sense, the vector $\overrightarrow{AB}$ would represent the entire set of line segments that are consistent, parallel and have the same direction as a given line segment $AB$. We could also write $\overrightarrow{CD}=\overrightarrow{AB}$ for each line segment $CD$ from this set of line segments (Figure \ref{sl.vek.5.1.1.pic}).

\begin{figure}[!htb]
\centering
\input{sl.vek.5.1.1.pic}
\caption{} \label{sl.vek.5.1.1.pic}
\end{figure}

In this way, we get an idea for a formal definition of vectors. First, we introduce the relation $\varrho$ on the set of pairs of points. Let $A$, $B$, $C$ and $D$ be points in the same plane
(Figure \ref{sl.vek.5.1.2.pic}). We say that $(A,B)\varrho (C,D)$, if one of the three conditions\footnote{In this way - in \index{geometry!affine}affine geometry (without the axioms of congruence) - the vector was defined by the Serbian mathematician \index{Veljković, M.}\textit{M. Veljković} (1954--2008), professor at the Mathematical Gymnasium in Belgrade.}\index{relation!$\varrho$} is fulfilled:

\begin{enumerate}
  \item The quadrilateral $ABDC$ is a parallelogram,
  \item There exist points $P$ and $Q$, such that the quadrilaterals $ABQP$ and $CDQP$ are parallelograms,
  \item $A=B$ and $C=D$.
\end{enumerate}

\begin{figure}[!htb]
\centering
\input{sl.vek.5.1.2.pic}
\caption{} \label{sl.vek.5.1.2.pic}
\end{figure}

It is intuitively clear that the second condition needs to be added due to the example when points $A$, $B$, $C$ and $D$ are collinear. The third condition will apply to the so-called vector of zero.

From the definition of the relation $\varrho$ itself, we get the following proposition.



                \bizrek \label{vektRelRo}
                If $(A,B)\varrho (C,D)$ and $A\neq B$, then the line segments $AB$ and $CD$
                 are congruent, parallel, and have the same direction.
                \eizrek

\textbf{\textit{Proof.}} Because $A\neq B$, only the first two conditions from the definition remain. In this case, the relations $AB\parallel CD$ and $AB\cong CD$ are direct consequences of the definition of a parallelogram and proposition \ref{paralelogram}.

Regarding the orientation of the line segments, we would use the definition: parallel line segments $XY$ and $UV$ are \pojem{equally oriented}, if one of the conditions is fulfilled:

... (truncated 20259 lines) ...
```

**Note**: Source truncated for display. Full file is 30259 lines.

## High-Level Overview

Source file of type .tex.

## Detailed Analysis

File contains 30259 lines with structured content.

## Usage & Examples

See file content for usage details.

## Performance & Security Notes

📊 **Performance**: Contains nested loops - consider complexity
📊 **Performance**: Large file - may impact load times

## Related Files

**Same directory**:
- [geometry_slovenian.tex](./geometry_slovenian.tex_docs.md)

**Imported modules**:
- `1435`
- `1672.`
- `1882.`
- `1899.`
- `1988`
- `Alexandria`
- `Arabic`
- `Athens`
- `Axiom`
- `Euclid`
- `Euclidean`
- `Example`
- `Helly`
- `Kios`
- `Miletus`

## Testing & Execution

See project documentation for testing procedures.

---
*Generated by Repo Book Generator v1.0.0*

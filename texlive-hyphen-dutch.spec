%global tl_name hyphen-dutch
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Dutch hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/nehyph.tex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-dutch.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Dutch in T1/EC and UTF-8 encodings. These
patterns don't handle cases like 'menuutje' > 'menu-tje', and don't
hyphenate words that have different hyphenations according to their
meaning.


%global tl_name hyphen-dutch
%global tl_revision 79618
%global tl_version 1.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Dutch in T1/EC and UTF-8 encodings. These
patterns don't handle cases like 'menuutje' > 'menu-tje', and don't
hyphenate words that have different hyphenations according to their
meaning.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-dutch:
dutch loadhyph-nl.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-dutch:
\addlanguage{dutch}{loadhyph-nl.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-dutch:
['dutch'] = {
	loader = 'loadhyph-nl.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-nl.pat.txt',
	hyphenation = 'hyph-nl.hyp.txt',
},
TL_HYPHEN_EOF

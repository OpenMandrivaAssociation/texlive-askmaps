Name:		texlive-askmaps
Version:	56730
Release:	1
Summary:	Typeset American style Karnaugh maps
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/askmaps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/askmaps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/askmaps.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides 2, 3, 4 and 5 variable Karnaugh maps, in
the style used in numerous textbooks on digital design. The
package draws K-maps where the most significant input variables
are placed on top of the columns and the least significant
variables are placed left of the rows.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/askmaps/askmaps.sty
%doc %{_texmfdistdir}/doc/latex/askmaps/README
%doc %{_texmfdistdir}/doc/latex/askmaps/askmaps.pdf
%doc %{_texmfdistdir}/doc/latex/askmaps/askmaps.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

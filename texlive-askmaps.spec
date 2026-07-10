%global tl_name askmaps
%global tl_revision 56730

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Typeset American style Karnaugh maps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/askmaps
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/askmaps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/askmaps.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides 1, 2, 3, 4 and 5 variable Karnaugh maps, in the
style used in numerous American textbooks on digital design. The package
draws K-maps where the most significant input variables are placed on
top of the columns and the least significant variables are placed left
of the rows.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/askmaps
%dir %{_datadir}/texmf-dist/tex/latex/askmaps
%doc %{_datadir}/texmf-dist/doc/latex/askmaps/README
%doc %{_datadir}/texmf-dist/doc/latex/askmaps/askmaps.pdf
%doc %{_datadir}/texmf-dist/doc/latex/askmaps/askmaps.tex
%{_datadir}/texmf-dist/tex/latex/askmaps/askmaps.sty

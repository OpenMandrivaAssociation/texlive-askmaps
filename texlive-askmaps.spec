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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides 1, 2, 3, 4 and 5 variable Karnaugh maps, in the
style used in numerous American textbooks on digital design. The package
draws K-maps where the most significant input variables are placed on
top of the columns and the least significant variables are placed left
of the rows.


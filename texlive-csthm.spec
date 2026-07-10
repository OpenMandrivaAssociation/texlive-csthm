%global tl_name csthm
%global tl_revision 73506

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Customized theorem environments for computer science documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/csthm
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csthm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csthm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csthm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides customized theorem-like environments specifically
designed for computer science documents. It offers a set of pre-defined
theorem styles and environments to streamline the creation of theorems,
definitions, remarks, and other common structures in computer science
papers and documents. Features: Predefined theorem styles tailored for
computer science Environments for theorems, lemmas, definitions,
examples, remarks, and more Special environments for cases and axioms
Customizable accent color Optional cleveref support for enhanced cross-
referencing The package requires the following packages to be installed:
amsmath, amssymb, amsthm, enumitem, and thmtools. If using the cleveref
option, hyperref and cleveref are also required.


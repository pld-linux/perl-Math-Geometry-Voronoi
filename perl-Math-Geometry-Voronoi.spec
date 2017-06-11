#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Geometry-Voronoi
%include	/usr/lib/rpm/macros.perl
Summary:	Math::Geometry::Voronoi - compute Voronoi diagrams from sets of points
Name:		perl-Math-Geometry-Voronoi
Version:	1.3
Release:	5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	44392be55ff56870aaff286dd735a5e2
URL:		http://search.cpan.org/dist/Math-Geometry-Voronoi/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Params-Validate
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module computes Voronoi diagrams from a set of input points. Info
on Voronoi diagrams can be found here:

http://en.wikipedia.org/wiki/Voronoi_diagram

This module is a wrapper around a C implementation found here:

http://www.derekbradley.ca/voronoi.html

Which is itself a modification of code by Steve Fortune, the inventor
of the algorithm used (Fortune's algorithm):

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Math/Geometry/Voronoi.pm
%dir %{perl_vendorarch}/auto/Math/Geometry/Voronoi
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Geometry/Voronoi/Voronoi.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

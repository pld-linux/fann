Summary:	A fast artificial neural network library
Summary(pl.UTF-8):   Szybka biblioteka do tworzenia sztucznych sieci neuronowych
Name:		fann
Version:	2.0.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/fann/%{name}-%{version}.tar.bz2
# Source0-md5:	4224efa533265dcf39237667973d0e20
Source1:	http://dl.sourceforge.net/fann/%{name}_doc_complete_1.0.pdf
# Source1-md5:	8117a677afc79dfaa31de39ca84d82da
Patch0:		%{name}-python.patch
URL:		http://leenissen.dk/fann/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	sed >= 4.0
BuildRequires:	swig-python >= 1.3.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast Artificial Neural Network (FANN) Library is written in ANSI C.
The library implements multilayer feedforward ANNs, up to 150 times
faster than other libraries. FANN supports execution in fixed point,
for fast execution on systems like the iPAQ.

%description -l pl.UTF-8
FANN (Fast Artificial Neural Network - szybkie sztuczne sieci
neuronowe) to biblioteka napisana w ANSI C, implementująca
wielowarstwowe sztuczne sieci neuronowe, do 150 razy szybsza od innych
bibliotek. FANN obsługuje operacje stałoprzecinkowe w celu szybkiego
działania na systemach typu iPAQ.

%package devel
Summary:	Development libraries for FANN
Summary(pl.UTF-8):   Pliki nagłówkowe FANN
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package is only needed if you intend to develop and/or compile
programs based on the FANN library.

%description devel -l pl.UTF-8
Pliki nagłówkowe FANN, potrzebne do tworzenia programów napisanych w
oparciu o bibliotekę FANN.

%package doc
Summary:	FANN documentation
Summary(pl.UTF-8):   Dokumentacja do FANN
Group:		Documentation

%description doc
Documentation for FANN.

%description doc -l pl.UTF-8
Dokumentacja do FANN.

%package static
Summary:	FANN static libraries
Summary(pl):    Biblioteki statyczne FANN
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FANN static libraries.
 
%description static -l pl.UTF-8
Biblioteki statyczne FANN.

%package -n python-%{name}
Summary:	Python support for FANN
Summary(pl.UTF-8):   Moduł języka Python dla biblioteki FANN
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-%{name}
Python support for FANN.

%description -n python-%{name} -l pl.UTF-8
Moduł języka Python dla biblioteki FANN.

%prep
%setup -q
cp %{SOURCE1} .
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
cd python

CFLAGS="%{rpmcflags}" \
%{__make}
%py_comp .
%py_ocomp .

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd python
%{__make} install \
	ROOT=$RPM_BUILD_ROOT

cd ..
install -d $RPM_BUILD_ROOT%{_examplesdir}/{python-,}%{name}-%{version}

install python/examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version} 
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/pyfann/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/fann.pc
%{_examplesdir}/%{name}-%{version}

%files doc
%defattr(644,root,root,755)
%doc fann_doc_complete_1.0.pdf doc/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyfann/*.so
%dir %{py_sitedir}/pyfann
%{py_sitedir}/pyfann/*.py[co]
%{_examplesdir}/python-%{name}-%{version}

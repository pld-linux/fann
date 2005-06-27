Summary:	A fast artificial neural network library
Summary(pl):	Szybka biblioteka do tworzenia sztucznych sieci neuronowych
Name:		fann
Version:	1.1.0
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	f8280e9849cfbf5ddf769713ce7f7fba
Patch0:		%{name}-python.patch
URL:		http://fann.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-utils
BuildRequires:	libtool
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	swig-python >= 1.3.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast Artificial Neural Network (FANN) Library is written in ANSI C.
The library implements multilayer feedforward ANNs, up to 150 times
faster than other libraries. FANN supports execution in fixed point,
for fast execution on systems like the iPAQ.

%description -l pl
FANN (Fast Artificial Neural Network - szybkie sztuczne sieci
neuronowe) to biblioteka napisana w ANSI C, implementuj±ca
wielowarstwowe sztuczne sieci neuronowe, do 150 razy szybsza od innych
bibliotek. FANN obs³uguje operacje sta³oprzecinkowe w celu szybkiego
dzia³ania na systemach typu iPAQ.

%package devel
Summary:	Development libraries for FANN
Summary(pl):	Pliki nag³ówkowe FANN
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package is only needed if you intend to develop and/or compile
programs based on the FANN library.

%description devel -l pl
Pliki nag³ówkowe FANN, potrzebne do tworzenia programów napisanych w
oparciu o bibliotekê FANN.

%package static
Summary:	FANN static libraries
Summary(pl):    Biblioteki statyczne FANN
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FANN static libraries.
 
%description static -l pl
Biblioteki statyczne FANN.

%package -n python-%{name}
Summary:	Python support for FANN
Summary(pl):	Modu³ jêzyka Python dla biblioteki FANN
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-%{name}
Python support for FANN.

%description -n python-%{name} -l pl
Modu³ jêzyka Python dla biblioteki FANN.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
%{__make} -C doc html-single
cd python
CFLAGS="%{rpmcflags}" \
%{__make}
%py_comp .
%py_ocomp .

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{py_sitedir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/{python-%{name}-%{version},%{name}-%{version}}

install python/{fann.pyc,fann.pyo,_fann.so} $RPM_BUILD_ROOT%{py_sitedir}
install python/simple_train.py $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%doc doc/fann.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/fann.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%{_examplesdir}/python-%{name}-%{version}

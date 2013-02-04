Summary:	A fast artificial neural network library
Summary(pl.UTF-8):	Szybka biblioteka do tworzenia sztucznych sieci neuronowych
Name:		fann
Version:	2.2.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/fann/FANN-%{version}-Source.tar.gz
# Source0-md5:	c9d6c8da5bb70276352a1718a668562c
Source1:	http://downloads.sourceforge.net/fann/%{name}_doc_complete_1.0.pdf
# Source1-md5:	8117a677afc79dfaa31de39ca84d82da
Patch0:		%{name}-link.patch
URL:		http://leenissen.dk/fann/
BuildRequires:	cmake >= 2.8
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
Summary(pl.UTF-8):	Pliki nagłówkowe FANN
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
Summary(pl.UTF-8):	Dokumentacja do FANN
Group:		Documentation

%description doc
Documentation for FANN.

%description doc -l pl.UTF-8
Dokumentacja do FANN.

%prep
%setup -q -n FANN-%{version}-Source
cp %{SOURCE1} .
%patch0 -p1

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt datasets/*
%attr(755,root,root) %{_libdir}/libdoublefann.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdoublefann.so.2
%attr(755,root,root) %{_libdir}/libfann.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfann.so.2
%attr(755,root,root) %{_libdir}/libfixedfann.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfixedfann.so.2
%attr(755,root,root) %{_libdir}/libfloatfann.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfloatfann.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdoublefann.so
%attr(755,root,root) %{_libdir}/libfann.so
%attr(755,root,root) %{_libdir}/libfixedfann.so
%attr(755,root,root) %{_libdir}/libfloatfann.so
%{_includedir}/*.h
%{_pkgconfigdir}/fann.pc
%{_examplesdir}/%{name}-%{version}

%files doc
%defattr(644,root,root,755)
%doc fann_doc_complete_1.0.pdf

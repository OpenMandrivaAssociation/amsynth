Summary:	Virtual-analog polyphonic synthesizer for ALSA, OSS and JACK
Name:	amsynth
Version:	1.13.4
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://amsynth.github.io/
Source0:	https://github.com/amsynth/amsynth/releases/download/release-%{version}/%{name}-%{version}.tar.gz
Patch0:	amsynth-1.13.4-use-ladish-instead-of-lash.patch
Patch1:	amsynth-1.13.4-fix-desktop-file.patch
BuildRequires:	autoconf-archive
BuildRequires:	gettext
BuildRequires:	intltool
# For man pages - not provided yet
#BuildRequires:	pandoc
BuildRequires:	alsa-oss-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dssi)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.20.0
BuildRequires:	pkgconfig(gtkmm-2.4) >= 2.6.0
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblash)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(lv2)

%description
Amsynth is a standalone polyphonic subtractive synthesizer. It supports OSS,
ALSA and JACK for Audio and MIDI I/O.
Features are as follows:
o Dual oscillators with classic waveforms (sine, saw, square, noise).
o 12/24 dB/oct resonant filter (low-pass, high-pass, band-pass, notch).
o Independent ADSR envelopes for filter & amplitude.
o LFO which can module the oscillators, filter, and amplitude.
o Distortion effect.
o Reverb.
o Lot of presets.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/appdata/*.metainfo.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#-----------------------------------------------------------------------------

%package dssi
Summary:	Amsynth DSSI synthesizer plugin
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description dssi
This is the DSSI synthesizer plugin of amsynth, which can be used with DSSI
hosts like qtractor, ghostess, rosegarden and others.

%files dssi
%{_libdir}/dssi/%{name}_dssi.so
%{_libdir}/dssi/%{name}_dssi/%{name}_dssi_gtk

#-----------------------------------------------------------------------------

%package plugin-lv2
Summary:	Amsynth LV2 synthesizer plugin
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description plugin-lv2
This is the LV2 synthesizer plugin of amsynth, which can be used with LV2
hosts like qtractor, ardour, zynjacku and others.

%files plugin-lv2
%{_libdir}/lv2/%{name}.lv2/*

#-----------------------------------------------------------------------------

%package plugin-vst
Summary:	Amsynth VST synthesizer plugin
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-vst
This is the VST synthesizer plugin of amsynth, which can be used with VST
hosts.

%files plugin-vst
%{_libdir}/vst/%{name}_vst.so

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}


%build
autoreconf -vfi
export LDFLAGS="%{ldflags} -lX11"
%configure	--disable-static \
	--with-alsa \
	--with-gui \
	--with-jack \
	--with-lash \
	--with-lv2 \
	--with-oss \
	--with-nsm \
	--without-pandoc

%make_build


%install
%make_install

%find_lang %{name}

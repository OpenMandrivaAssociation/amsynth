Name:            amsynth
Version:         1.3.1
Release:         1

Summary:        Virtual-analog polyphonic synthesizer for ALSA, OSS and JACK
Source:         http://%{name}.googlecode.com/files/amSynth-%{version}.tar.gz
URL:            http://code.google.com/p/%{name}
License:        GPLv2
Group:          Sound
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  alsa-oss-devel
BuildRequires:  dssi-devel

%description
AmSynth is a standalone polyphonic subtractive synthesizer. It supports
OSS, ALSA and JACK for Audio and MIDI I/O. Features are as follows.

o Dual oscillators with classic waveforms - sine / saw / square / noise
o 24 dB/oct low-pass resonant filter
o Independent ADSR envelopes for filter & amplitude
o LFO which can module the oscillators, filter, and amplitude
o Distortion effect
o Reverb

%package dssi
Summary:	DSSI synthesizer plugin
Group:		Sound
License:	GPLv2+
Requires:	%{name} = %{version}-%{release}

%description dssi
This is the DSSI synthesizer plugin of amSynth, which can be used
with DSSI hosts like qtractor, ghostess, rosegarden and others.


%prep
%setup -q -n amSynth-%{version}
perl -pi -le 'print "#include <unistd.h>" if $. == 10' src/Config.cc

%build
LIBS='-lX11' %configure2_5x --without-lash
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%files
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/amSynth
%{_datadir}/amSynth
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files dssi
%{_libdir}/dssi/amsynth_dssi.so
%{_libdir}/dssi/amsynth_dssi/amsynth_dssi_gtk

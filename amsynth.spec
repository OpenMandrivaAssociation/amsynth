%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define beta beta2
%endif

Name:            amsynth
Version:         1.3

%if %branch
Release:        0.%{beta}.1
%else
Release:        1
%endif

Summary:        Virtual-analog polyphonic synthesizer for ALSA, OSS and JACK

%if %branch
Source:         http://%{name}.googlecode.com/files/amSynth-%{version}-%{beta}.tar.gz
%else
Source:         http://%{name}.googlecode.com/files/amSynth-%{version}.tar.gz
%endif
URL:            http://code.google.com/p/%{name}
License:        GPLv2
Group:          Sound
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  alsa-oss-devel

%description
AmSynth is a standalone polyphonic subtractive synthesizer. It supports
OSS, ALSA and JACK for Audio and MIDI I/O. Features are as follows.

o Dual oscillators with classic waveforms - sine / saw / square / noise
o 24 dB/oct low-pass resonant filter
o Independent ADSR envelopes for filter & amplitude
o LFO which can module the oscillators, filter, and amplitude
o Distortion effect
o Reverb

%prep
%if %branch
%setup -q -n amSynth-%{version}-%{beta}
%else
%setup -q -n amSynth-%{version}
%endif
perl -pi -le 'print "#include <unistd.h>" if $. == 10' src/Config.cc

%build
LIBS='-lX11' %configure2_5x --without-lash
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/amSynth
%{_datadir}/amSynth
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


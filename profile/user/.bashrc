# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    #alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
#alias ll='ls -l'
#alias la='ls -A'
#alias l='ls -CF'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

export PS1="> "

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

alias dir='dir --color'
alias ls='ls -lh --color --group-directories-first'
alias ll='ls'
alias df='df -h'
alias blk='lsblk'
alias free='free -m'
alias uname='uname -ap'

alias set-sink="pacmd set-default-sink "
alias set-source="pacmd set-default-source "

alias cards='cat /proc/asound/cards'
alias list-sinks="pacmd list-sinks | grep -e 'name:' -e 'index:'"
alias list-sources="pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'"
alias audio='cards && list-sinks && list-sources'
alias drum='aplaymidi -p 14:0'
alias synth='aplaymidi -p 130:0'

alias youtube='youtube-dl -x --audio-format wav'
#alias explorer='wine ~/.wine/drive_c/windows/explorer.exe'

alias p='python3 -W ignore'

alias redzeppelin='jalv http://gareus.org/oss/lv2/avldrums#RedZeppelinMulti'
alias blackpearl='jalv http://gareus.org/oss/lv2/avldrums#BlackPearlMulti'

alias clone='git clone'
alias cache="git config --global credential.helper 'cache --timeout=14400'"
alias clearcache="git credential-cache exit"
alias commit='git commit -m 'Updated' -a'
alias push='git push'
alias pull='git pull'

alias psaudio="ps axu|egrep 'jack|pulse'"
alias calfdrumstack='calfjackhost multibandcompressor ! multibandlimiter ! eq8 ! reverb !'
alias calfusb='calfjackhost flanger ! saturator ! crusher ! vintagedelay ! eq5 !'
alias calfmin='calfjackhost flanger ! saturator ! crusher ! eq5 ! vintagedelay !'
alias acousticladspa='carla-single ladspa /usr/lib/ladspa/tap_tubewarmth.so & carla-single ladspa /usr/lib/ladspa/tap_dynamics_st.so & carla-single ladspa /usr/lib/ladspa/stereo-plugins.so &'
#alias record='jack_capture -d 60 -p system:capture* -f wav out.wav'
alias record='jack_capture -d 60 -p system:playback* -f wav out.wav'
#alias record='jack_capture -d 60 -p "Calf Studio Gear:Equalizer*" -f wav out.wav'
#alias record='jack_capture -d 60 -p "Calf Studio Gear:Vintage*" -f wav out.wav'

alias x='startx'

alias pyhttp='cd /var/www/html && python -m SimpleHTTPServer'
alias installtensorflow='npm -y init && npm install @tensorflow/tfjs-node'

if [ -f `which powerline-daemon` ]; then
  powerline-daemon -q
  POWERLINE_BASH_CONTINUATION=1
  POWERLINE_BASH_SELECT=1
  . /usr/share/powerline/bindings/bash/powerline.sh
fi


export PATH=$PATH:/opt/node-v8.12.0-linux-x64/bin/

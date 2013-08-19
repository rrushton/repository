# Begin /etc/profile.d/50-prompt.sh

export PS1="\[\e[1;32m\]\u\[\e[1;33m\]@\[\e[1;31m\]\H \[\e[1;34m\]\w 
\[\e[1;32m\]\$ \[\e[0;0m\]"
if [ "${TERM:0:5}" = "xterm" ]; then
  export PS1="\[\e]2;\u@\H :: \w\a\]$PS1"
fi

shopt -s checkwinsize

# End /etc/profile.d/50-prompt.sh

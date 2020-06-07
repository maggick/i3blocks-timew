#!/bin/bash

INFO_TIMEW=$(timew 2>/dev/null)

if [[ $? -eq 0 ]]; then
    INFO_TASK=$(echo "${INFO_TIMEW}" | sed -n -e 's/^.*Tracking//p' | sed -e 's/^[ \t]*//')
    INFO_TIME=$(echo "${INFO_TIMEW}" | sed -n -e 's/^.*Total//p' | sed -e 's/^[ \t]*//')
else
  OUT_TEXT=''
fi

if [[ "${INFO_TASK}" ]] && [[ "${INFO_TIME}" ]]; then
  OUT_TEXT=" ${INFO_TASK} - ${INFO_TIME}"
elif [[ "${INFO_TIME}" ]]; then
  OUT_TEXT="${INFO_TIME}"
fi

echo "${OUT_TEXT}"



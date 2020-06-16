# shellcheck disable=SC1113
# /bin/bash

# shellcheck disable=SC2006
result=`make run --dir='Cpp_source/'`

# shellcheck disable=SC2181
if [ "$?" = "0"  ]
then
  echo  "every thing was successfull"
  echo "result: ${result}"
else
  echo "failed with exit status ${?}"
fi




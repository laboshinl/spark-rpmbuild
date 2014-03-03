SPARK_USER=spark
if ! id $SPARK_USER > /dev/null 2>&1 ; then
  if ! id -g $SPARK_USER > /dev/null 2>&1 ; then
    groupadd --system $SPARK_USER
  fi
  useradd  --system \
  --home / --no-create-home -g $SPARK_USER $SPARK_USER
fi


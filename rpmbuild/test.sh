SPARK_USER=spark
/usr/sbin/groupadd -r $SPARK_USER &>/dev/null || :
/usr/sbin/useradd -r -s /sbin/nologin -M -g $SPARK_USER $SPARK_USER &>/dev/null || :


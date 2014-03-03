Name: spark
Version: 0.9.0
Release: 1
Summary: Description
License: GPL
URL: http://cloud-technologies.ru/
BuildRequires: bash, redhat-lsb, coreutils, bigtop-utils, initscripts
%description

%pre
DISTCC_USER=spark
if [ -s /etc/redhat-release ]; then
  # sadly, can't useradd -s /sbin/nologin on rh71, since
  # then starting the service as user distcc fails,
  # since it uses su - without overriding the shell :-(
  # See https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=26894
  /sbin/service distcc stop &>/dev/null || :
  if fgrep 'nice initlog $INITLOG_ARGS -c "su - $user' /etc/init.d/functions | fgrep -v '.-s ' > /dev/null 2>&1 ; then
    # Kludge: for Red Hat 6.2, don't use -s /sbin/nologin
    /usr/sbin/useradd -d /var/run/distcc -m -r $DISTCC_USER &>/dev/null || :
  else
    # but do for everyone else
    /usr/sbin/useradd -d /var/run/distcc -m -r -s /sbin/nologin $DISTCC_USER &>/dev/null || :
  fi
else
  echo Creating $DISTCC_USER user...
  if ! id $DISTCC_USER > /dev/null 2>&1 ; then
    if ! id -g $DISTCC_USER > /dev/null 2>&1 ; then
      addgroup --system --gid 11 $DISTCC_USER
    fi
    adduser --quiet --system --gid 11 \
      --home / --no-create-home --uid 15 $DISTCC_USER
  fi
fi

%files
/usr/assembly/target/scala-2.10/spark-assembly_2.10-0.9.0-incubating-hadoop2.2.0.jar
/usr/bin/compute-classpath.cmd  
/usr/bin/pyspark2.cmd  
/usr/bin/run-example2.cmd  
/usr/bin/spark-class2.cmd  
/usr/bin/spark-shell.cmd
/usr/bin/compute-classpath.sh   
/usr/bin/pyspark.cmd   
/usr/bin/run-example.cmd   
/usr/bin/spark-class.cmd
/usr/bin/pyspark                
/usr/bin/run-example   
/usr/bin/spark-class       
/usr/bin/spark-shell
/etc/spark/fairscheduler.xml
/etc/spark/metrics.properties
/etc/spark/spark-env.sh
/etc/spark/log4j.properties
/etc/spark/slaves
/etc/init.d/spark-master
/etc/init.d/spark-worker


%attr(755, root, root) /etc/init.d/spark-master
%attr(755, root, root) /etc/init.d/spark-worker
%attr(644, spark, spark) /var/log/spark
 
%dir /var/run/spark
%dir /var/lib/spark
%dir /var/lock/spark
%dir /var/log/spark
%dir /etc/spark

%changelog

%preun
rm /var/log/spark/* -rf
rm /var/run/spark/* -rf

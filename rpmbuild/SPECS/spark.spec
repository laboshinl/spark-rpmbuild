Name: spark
Version: 0.9.0
Release: 1
Summary: Description
License: GPL
URL: http://cloud-technologies.ru/
#Requires: bash, redhat-lsb, coreutils, bigtop-utils, initscripts
Requires(pre): /usr/sbin/useradd /usr/sbin/groupadd
Requires(postun): /usr/sbin/userdel /usr/sbin/groupdel

%description

%pre
/usr/sbin/groupadd -r spark &>/dev/null || :
/usr/sbin/useradd  -r -s /sbin/nologin -M -g spark spark &>/dev/null || :

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

%config 
/etc/spark/fairscheduler.xml
/etc/spark/metrics.properties
/etc/spark/spark-env.sh
/etc/spark/log4j.properties
/etc/spark/slaves

%attr(755, root, root) 
/etc/init.d/spark-master
/etc/init.d/spark-worker
 
%dir 
/var/run/spark
/var/lib/spark
/var/lock/spark
/etc/spark

%defattr(755, spark, spark)
/var/log/spark

#%post
#chown spark.spark /var/log/spark -R
#chmod 755 /var/log/spark -R

%preun
/etc/init.d/spark-master stop
/etc/init.d/spark-worker stop
rm /var/log/spark/* -rf
rm /var/run/spark/* -rf
killall -u spark

%postun
SPARK_USER=spark
/usr/sbin/userdel $SPARK_USER &>/dev/null || :
/usr/sbin/groupdel $SPARK_USER &>/dev/null || :

%clean

%changelog

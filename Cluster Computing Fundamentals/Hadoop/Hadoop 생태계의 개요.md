# Hadoop 생태계의 개요

Written at 2022-04-15

![Hadoop ecosystem](/Cluster%20Computing%20Fundamentals/Hadoop/asset/Hadoop%20Ecosystem.png)

Hadoop Ecosystem을 정리한 이미지이다.

## Core Hadoop Ecosystem

![Core Hadoop ecosystem](/Cluster%20Computing%20Fundamentals/Hadoop/asset/core-hadoop-system.png)
Core Hadop Ecosystem에서 소개되는 기술 스택들은 Hadoop 플랫폼에 직접 개발되었다.분행색은 Hadoop 자체의 부분이다. 나머지는 시간이 지나 덧붙여진 add-on Project이다

- **HDFS**
  <br>
  Hadoop Distributed File System (하둡 분산 파일 시스템) 의 약어이다. 데이터를 클러스터의 컴퓨터들에 분산 저장하는 시스템이다. HDFS는 클러스터의 드라이브들을 하나의 거대한 파일 시스템으로 사용한다. 단순 저장뿐만 아니라 복사본을 만들어 데이터가 손실되었을 때, 자동으로 복구한다. Hadoop의 "분산 데이터 저장소" 역할을 담당한다.

<br>

- **YARN**
  <br>
  Yet Antoher Resource Negotiator의 약어로, "또 다른 리소스 교섭자"라는 뜻이다. YARN은 데이터 처리 부분을 담당한다. YARN은 컴퓨터 클러스터의 리소스를 관리하는 시스템이다. 누가 작업을 언제 실행하고 어떤 노드가 추가 작업을 할 수 있고 없고 등을 결정한다.

<br>

- **MapReduce**
  <br>
  데이터를 클러스터 전체에 걸쳐 처리하도록 하는 프로그래밍 메타포 혹은 프로그래밍 모델이다. MapReduce는 Mapper와 Reducer로 구성되어 있다. Mapper는 클러스테 분산 돼 있는 데이터를 효율적으로 동시에 변형시킬 수 있다. Reducer는 그 데이터를 집계한다.
  원래는 YARN과 MapReduce가 거의 같은 역할을 했는데 최근에는 분리되었다.

<br>

- **Pig**
  <br>
  Java나 Python으로 MapReduce를 코딩하기보다 SQL 스타일 구문을 사용하는 스크립트 언어에 익숙하다면 Pig가 적격이다. 고수준의 API로써, SQL과 비슷한 간단한 스크립트를 작성해 쿼리를 연결하고 복잡한 답을 구할 수 있다. 정리하자면, Pig는 작성된 스크립트를 MapReduce가 읽을 수 있도록 번역하고 MapReduce는 다시 YARN과 HDFS에게 데이터를 처리하고 원하는 답을 가져오게 한다.

<br>

- **HIVE**  
  HIVE는 실제 SQL 쿼리를 받고 파일 시스템에 분산된 데이터를 SQL 데이터베이스처럼 취급한다. 셸 클라이언트나 ODBC(Open Database Connectivity) 등을 통해 데이터베이스에 접속할 수 있으며, Hadoop 클러스터에 저장 돼 있는 데이터가 내부적으로는 관계형 데이터베이스가 아님에도 불구하고 SQL로 쿼리한다. SQL에 익숙하다면 Hive API를 유용하게 사용할 수 있다.

  <br>

- **Apache Ambari**
  위에서 말한 것들 위에서 동작하는 것이다. Ambari는 클러스터 전체를 보여준다. 클러스터에서 어떤 시스템을 사용하고, 얼마나 많은 리소슬 사용하는지 등을 시각화해서 보여준다. 또 Hive나 Pig 쿼리를 실행하거나 데이터베이스를 불러올 수 있다. 정리하자면, 클러스터와 작동하는 애플리케이션의 상태를 볼 수 있게 해 준다. 참고로 Ambari는 Hortonworks의 제품 중 하나이고 경쟁품에는 Cloudera의 MapR 등이 있다.

<br>

- **Mesos**
  Mesos는 엄밀히 말하면 Hadoop의 일부는 아니다. 하지만 YARN의 대안 정도로 볼 수 있기 때문에 Core Hadoop Ecosystem에 포함했다. Mesos 또한 YARN과 같이 리소스 교섭자이지만 서로 다른 방식을 가진다.

<br>

- **Spark**
  Spark는 YARN이나 Mesos를 기반으로 데이터에 쿼리를 실행할 수 있다. Python, Java 혹은 Scala를 사용해서 Spark 스크립트를 작성해야 되는데 Scala를 가장 많이 사용한다. 클러스터의 데이터를 신속하고 효율적이며 안정적으로 처리하고 싶다면 Spark는 좋은 선택지이다. 또한 다양성을 가지고 있다. 클러스터에 걸친 정보로 머신 러닝을 수행하는 SQL 쿼리도 처리 가능하고 실시간으로 스트리밍 되는 데이터를 처리하는 등 다양한 작업을 처리할 수 있다.

<br>

- **TEZ**
  Spark와 비슷한 기술을 많이 사용한다. TEZ의 특징으로는 "Directed Acyclic Graph"(방향성 비사이클 그래프)가 있다. 이는 쿼리 실행에 더 효율적인 계획을 세워 MapReduce를 할 때 효과적이다. TEZ는 보통 Hive와 함께 사용되어 성능을 가속한다. (Hive가 MapReduce를 통과할 때보다 TEZ를 통과할 때 더 빠를 수도 있다)

<br>

- **HBASE**
  클러스터의 데이터를 트랜잭션 플랫폼으로 노출하는 역할을 하며 NoSQL 데이터베이스라고 불린다. Columnar Data Store이고 단위 시간 당 실행되는 트랜잭션의 수가 큰 아주 빠른 데이터베이스이다. 그러므로 데이터를 웹 애플리케이션이나 웹사이트에 노출시켜 OLTP(Online Transaction Processing) 트랜잭션을 하는데 적합하다. 정리하면, HBase는 클러스터에 저장된 데이터를 노출시킨다.

<br>

- **Apache STORM**
  STORM은 스트리밍 데이터를 처리하는 방식이다. 만약 센서나 웹 로그으로부터 데이터를 스트리밍 한다면 STROM이나 Spark Streaming을 통해 실시간으로 처리할 수 있다. 데이터가 실시간으로 입력됨에 따라 실시간으로 기계 학습을 업데이트하거나 데이터를 데이터베이스에 저장할 수 있다.

<br>

- **OOZIE**
  OOZIE는 클러스터의 작업을 스케쥴링한다. Hadoop 클러스터에 여러 단계나 시스템이 필요한 작업을 OOZIE를 통해서 순차적으로 스케쥴링 할 수 있다.

<br>

- **Zookeeper**
  클러스터의 모든 것을 조직화하는 기술이다. Zookeeper을 사용해 어떤 노드가 살아있는지 추적할 수 있고, 여러 애플리케이션이 사용하는 클러스터의 공유 상태를 안정적으로 확인한다. 예를 들어, 어떤 노드가 마스터 노드이며, 어떤 노드가 살아있고 다운되어 있는지 추적하는데 사용될 수 있다.

<br>

- **Sqoop**
  Hadoop의 데이터베이스를 관계형 데이터베이스로 엮어낸다. ODBC나 JDBC(Jsava Database Connectivity)로 연결 가능한 데이터는 Sqoop을 통해서 HDFS의 파일로 변형할 수 있다. 다시 말해 Sqoop은 레거시 데이터베이스와 Hadoop을 잇는 연결 장치로 볼 수 있다.

<br>

- **FLUME**
  대규모 웹로그를 안정적으로 클러스터에 불러올 수 있다. 실시간으로 웹 서버의 웹 로그를 감시하고 클러스터에 게시해 STORM이나 Spark Streaming을 사용해 처리한다.

<br>

- **Kafka**
  Kafka도 데이터 수집을 하지만 좀 더 포괄적으로 사용된다. PC 혹은 웹 서버 클러스터에서 모든 종류의 데이터를 수집해 Hadoop 클러스터로 보낸다.

## External Data Storage

- **MySQL**
  Sqoop을 통해 Hadoop 클러스터로 데이터를 가져올 뿐 아니라 MySQL로 내보낼 수도 있다. Spark와 같은 기술은 JDBC나 ODBC 데이터베이스에 기록할 수 있고 중앙 데이터베이스에 직접 저장하거나 필요하다면 결과를 검색할 수도 있다.

<br>

- **Cassandra & MongoDB**
  HBase처럼 Columnar Data Store이고 웹 애플리케이션 등에 데이털르 실시간으로 노출하는데 사용될 수 있다. 따라서 실시간 애플리케이션과 클러스터 사이에 Cassandra나 MongoDB 같은 Layer을 만드는 것을 추천한다.

## Query Engines

아래와 같은 기술을 사용해서 대화형으로 SQL 쿼리를 입력할 수 있다

<br>

- **Apache DRILL**
  다양한 NoSQL 데이터베이스에 SQL 쿼리를 작성해 사용할 수 있도록 한다. DRILL은 HBase, Cassandra, MongoDB의 데이터베이스와 연결될 수 있으며, 연결한 내용을 엮어서 이질적인 데이터 스토어들에 걸쳐 쿼리르 작성하고 그 결과를 한데 모아줄 수 있다

<br>

- **HUE**
  HUE를 사용해 Hive, HBase에 작동하는 쿼리를 대화형으로 생성할 수 있다. Cloudera에서는 HUE가 Ambari의 역할을 담당하여 Hadoop 클러스터를 시각화한다.

<br>

- **Apache PHOENIX**
  Apache DRILL과 유사한 기술로 전체 데이터 스토리지 기술에 걸쳐 SQL 스타일의 쿼리를 할 수 있게 한다. 더 나아가 ACID(Atomicity, Consistency, Isolation, Durability)를 보장하고 OLTP를 제공한다.

<br>

- **Presto**
  전체 클러스터에 쿼리를 실행할 수 있는 방법 중 하나이다.

<br>

- **Apache Zeppelin**
  클러스터와의 상호작용과 사용자 인터페이스를 노트북 유형으로 접근했다.
